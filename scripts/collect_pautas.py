"""Coleta links de pautas oficiais da Câmara de Mogi Guaçu, sem IA ou APIs pagas.

Uso:
    python scripts/collect_pautas.py

Grava dados/pautas.json. O arquivo é atualizado somente quando a coleta é válida.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

SOURCE_URL = "https://camaramogiguacu.sp.gov.br/pautas-das-sessoes/"
OUTPUT = Path(__file__).resolve().parents[1] / "dados" / "pautas.json"
MONTHS = {
    "janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4,
    "maio": 5, "junho": 6, "julho": 7, "agosto": 8,
    "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12,
}
DATE_RE = re.compile(r"^\s*(\d{1,2})\s+de\s+(" + "|".join(MONTHS) + r")\s*$", re.I)
YEAR_RE = re.compile(r"^20\d{2}$")


class PautasParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_section = False
        self.year: int | None = None
        self.active_heading: str | None = None
        self.heading_text: list[str] = []
        self.href: str | None = None
        self.link_text: list[str] = []
        self.records: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag in ("h1", "h2", "h3"):
            self.active_heading = tag
            self.heading_text = []
        if tag == "a":
            self.href = values.get("href")
            self.link_text = []

    def handle_data(self, data: str) -> None:
        if self.active_heading:
            self.heading_text.append(data)
        if self.href is not None:
            self.link_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == self.active_heading:
            title = " ".join(" ".join(self.heading_text).split())
            if tag == "h1" and "PAUTAS DAS SESSÕES" in title.upper():
                self.in_section = True
            elif self.in_section and tag in ("h2", "h3"):
                if YEAR_RE.fullmatch(title):
                    self.year = int(title)
                elif self.year is not None and tag == "h2":
                    self.year = None
            self.active_heading = None
        if tag == "a" and self.href is not None:
            label = " ".join(" ".join(self.link_text).split()).lower()
            match = DATE_RE.fullmatch(label)
            if self.in_section and self.year and match:
                day = int(match.group(1))
                month = MONTHS[match.group(2)]
                try:
                    iso = datetime(self.year, month, day).date().isoformat()
                except ValueError:
                    iso = ""
                url = urljoin(SOURCE_URL, self.href)
                parsed = urlparse(url)
                if iso and parsed.scheme == "https" and parsed.hostname in {
                    "camaramogiguacu.sp.gov.br", "www.camaramogiguacu.sp.gov.br"
                }:
                    self.records.append({
                        "id": hashlib.sha256(f"{iso}|{url}".encode()).hexdigest()[:20],
                        "data_sessao": iso,
                        "documento_url": url,
                        "tipo": "pauta_publicada",
                        "fonte_url": SOURCE_URL,
                    })
            self.href = None
            self.link_text = []


def parse_pautas(html: str) -> list[dict[str, str]]:
    parser = PautasParser()
    parser.feed(html)
    unique = {item["id"]: item for item in parser.records}
    return sorted(unique.values(), key=lambda item: (item["data_sessao"], item["id"]), reverse=True)


def collect() -> int:
    request = Request(SOURCE_URL, headers={
        "User-Agent": "ObservatorioMogiGuacu/0.1 (coleta de documentos publicos; 1 requisicao por execucao)",
        "Accept": "text/html",
    })
    try:
        with urlopen(request, timeout=25) as response:
            if response.status != 200:
                raise RuntimeError(f"HTTP {response.status}")
            raw = response.read(3_000_001)
            if len(raw) > 3_000_000:
                raise RuntimeError("Página acima do limite de 3 MB")
            html = raw.decode(response.headers.get_content_charset() or "utf-8", errors="replace")
        records = parse_pautas(html)
        if not records:
            raise RuntimeError("Nenhuma pauta encontrada; formato da página pode ter mudado")
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        previous = {}
        if OUTPUT.exists():
            previous = json.loads(OUTPUT.read_text(encoding="utf-8"))
        previous_items = {x["id"]: x for x in previous.get("registros", []) if "id" in x}
        for record in records:
            previous_items[record["id"]] = record
        merged = sorted(previous_items.values(), key=lambda x: (x["data_sessao"], x["id"]), reverse=True)
        payload = {
            "fonte": SOURCE_URL,
            "tipo": "pautas_de_sessoes",
            "nota": "A presença de uma pauta não comprova aprovação, votação ou execução.",
            "registros": merged,
        }
        OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        added = len(previous_items) - len(previous.get("registros", []))
        print(f"Coleta concluída: {len(records)} links localizados; {len(merged)} armazenados; novos: {max(added, 0)}")
        return 0
    except (HTTPError, URLError, OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"Falha na coleta: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(collect())
