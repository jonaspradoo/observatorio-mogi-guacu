const indicators = [
  { label: "Projetos legislativos", value: "—", note: "Aguardando integração com a Câmara" },
  { label: "Despesas públicas", value: "—", note: "Aguardando dados oficiais" },
  { label: "Votações registradas", value: "—", note: "Aguardando registros nominais" },
];

const sections = [
  { number: "01", name: "Atividade legislativa", description: "Projetos, tramitações, sessões e votações da Câmara Municipal.", status: "Integração em preparação" },
  { number: "02", name: "Dinheiro público", description: "Despesas, contratos e evolução dos custos da administração.", status: "Integração em preparação" },
  { number: "03", name: "Análises independentes", description: "Artigos e investigações com referências verificáveis.", status: "Publicações em preparação" },
];

export default function Home() {
  return (
    <main className="min-h-screen bg-[#f6f5f1] text-[#202520]">
      <header className="border-b border-[#deded7]">
        <div className="mx-auto flex max-w-6xl flex-wrap items-center justify-between gap-5 px-6 py-6">
          <a href="#" className="flex items-center gap-3" aria-label="Observatório Mogi Guaçu — início">
            <span className="flex size-11 items-center justify-center rounded-md bg-[#263b32] text-sm font-bold tracking-tight text-white">OM</span>
            <span className="leading-tight">
              <span className="block text-sm font-bold tracking-wide">OBSERVATÓRIO</span>
              <span className="block text-xs tracking-[0.2em] text-[#69756c]">MOGI GUAÇU</span>
            </span>
          </a>
          <nav aria-label="Navegação principal" className="flex flex-wrap gap-x-7 gap-y-2 text-sm text-[#536158]">
            <a href="#indicadores" className="hover:text-[#202520]">Indicadores</a>
            <a href="#acompanhamento" className="hover:text-[#202520]">Acompanhamento</a>
            <a href="#editorial" className="hover:text-[#202520]">Editorial</a>
          </nav>
        </div>
      </header>

      <section className="mx-auto max-w-6xl px-6 pb-24 pt-20 md:pt-28">
        <div className="mb-7 flex items-center gap-3 text-xs font-semibold uppercase tracking-[0.18em] text-[#627f6b]">
          <span className="h-px w-8 bg-[#779480]" />
          Informação pública. Interesse coletivo.
        </div>
        <h1 className="max-w-4xl text-5xl font-semibold leading-[1.08] tracking-[-0.055em] md:text-7xl">
          O poder público sob o olhar da população.
        </h1>
        <p className="mt-8 max-w-2xl text-lg leading-8 text-[#5a625c]">
          Um observatório independente para acompanhar decisões, atividades legislativas e gastos públicos de Mogi Guaçu. Dados verificáveis, sem intermediários.
        </p>
        <div className="mt-10 flex flex-wrap gap-3">
          <a href="#indicadores" className="rounded-md bg-[#263b32] px-6 py-3 text-sm font-medium text-white transition hover:bg-[#355243]">
            Explorar indicadores
          </a>
          <a href="#acompanhamento" className="rounded-md border border-[#cbd0c8] px-6 py-3 text-sm font-medium transition hover:bg-white">
            Como acompanhamos
          </a>
        </div>
      </section>

      <section id="indicadores" className="border-y border-[#deded7] bg-white">
        <div className="mx-auto max-w-6xl px-6 py-16">
          <p className="text-xs font-semibold uppercase tracking-[0.18em] text-[#778079]">Painel municipal</p>
          <div className="mt-3 flex flex-wrap items-end justify-between gap-4">
            <h2 className="text-3xl font-semibold tracking-tight md:text-4xl">Os números da cidade</h2>
            <span className="rounded-full bg-[#edf1eb] px-3 py-1 text-xs text-[#536c58]">Fontes em integração</span>
          </div>
          <div className="mt-9 grid gap-4 md:grid-cols-3">
            {indicators.map((item) => (
              <article key={item.label} className="rounded-xl border border-[#e4e6e0] p-7">
                <h3 className="text-sm text-[#657067]">{item.label}</h3>
                <p className="mt-5 text-5xl font-semibold tracking-tight">{item.value}</p>
                <p className="mt-4 text-xs text-[#7d847e]">{item.note}</p>
              </article>
            ))}
          </div>
          <p className="mt-5 text-xs leading-5 text-[#7b817b]">
            Não publicamos números estimados ou fictícios. Os indicadores serão exibidos após a validação das fontes oficiais.
          </p>
        </div>
      </section>

      <section id="acompanhamento" className="mx-auto max-w-6xl px-6 py-20">
        <p className="text-xs font-semibold uppercase tracking-[0.18em] text-[#778079]">Transparência em acompanhamento</p>
        <h2 className="mt-3 text-3xl font-semibold tracking-tight md:text-4xl">O que será monitorado</h2>
        <div className="mt-10 divide-y divide-[#deded7] border-y border-[#deded7]">
          {sections.map((item) => (
            <article key={item.number} className="grid gap-4 py-7 md:grid-cols-[64px_1fr_1.2fr] md:items-start md:gap-8">
              <span className="font-mono text-sm text-[#7e8b80]">{item.number}</span>
              <div>
                <h3 className="text-xl font-semibold">{item.name}</h3>
                <p className="mt-2 text-xs text-[#718076]">{item.status}</p>
              </div>
              <p className="text-sm leading-7 text-[#616a63]">{item.description}</p>
            </article>
          ))}
        </div>
      </section>

      <section id="editorial" className="bg-[#e9ebe5]">
        <div className="mx-auto max-w-6xl px-6 py-20">
          <p className="text-xs font-semibold uppercase tracking-[0.18em] text-[#647266]">Editorial independente</p>
          <h2 className="mt-4 max-w-2xl text-3xl font-semibold tracking-tight md:text-4xl">Questionar também é exercer cidadania.</h2>
          <p className="mt-6 max-w-2xl text-base leading-8 text-[#5c675e]">
            Aqui serão publicados artigos, análises críticas e investigações sobre a gestão municipal, sempre distinguindo opinião de informação documental.
          </p>
          <p className="mt-8 text-sm text-[#738076]">Primeiras publicações em preparação.</p>
        </div>
      </section>

      <footer className="border-t border-[#deded7] bg-white">
        <div className="mx-auto flex max-w-6xl flex-wrap justify-between gap-4 px-6 py-8 text-xs text-[#718076]">
          <p>© {new Date().getFullYear()} Observatório Mogi Guaçu</p>
          <p>Iniciativa independente. Sem vínculo com órgãos governamentais.</p>
        </div>
      </footer>
    </main>
  );
}
