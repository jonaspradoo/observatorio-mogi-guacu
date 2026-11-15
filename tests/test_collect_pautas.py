import unittest
from scripts.collect_pautas import parse_pautas


class PautasParserTests(unittest.TestCase):
    def test_extrai_anos_e_datas_sem_confundir_com_outros_links(self):
        html = """
        <a href="/qualquer">03 de novembro</a>
        <h1>PAUTAS DAS SESSÕES</h1>
        <h2>2026</h2>
        <ul><li><a href="/wp-content/uploads/2026/10/pauta.pdf">03 de novembro</a></li>
            <li><a href="/wp-content/uploads/2026/10/pauta.pdf">03 de novembro</a></li></ul>
        <h2>2025</h2>
        <a href="https://camaramogiguacu.sp.gov.br/doc.pdf">15 de dezembro</a>
        <a href="https://dominio-externo.example/documento.pdf">20 de dezembro</a>
        """
        records = parse_pautas(html)
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0]["data_sessao"], "2026-11-03")
        self.assertEqual(records[1]["data_sessao"], "2025-12-15")
        self.assertEqual(records[0]["tipo"], "pauta_publicada")

    def test_rejeita_data_invalida(self):
        html = '<h1>PAUTAS DAS SESSÕES</h1><h2>2026</h2><a href="/a.pdf">31 de fevereiro</a>'
        self.assertEqual(parse_pautas(html), [])


if __name__ == "__main__":
    unittest.main()
