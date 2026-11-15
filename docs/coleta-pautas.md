# Coleta de pautas — Observatório Mogi Guaçu

Primeiro coletor experimental, em Python e somente biblioteca padrão (sem chave de API ou IA).

## Fonte

[Portal oficial: Pautas das Sessões](https://camaramogiguacu.sp.gov.br/pautas-das-sessoes/)

O coletor extrai **links das pautas publicadas** e as respectivas datas. **Não** extrai o texto dos PDFs, autores de projetos, votações ou projetos aprovados. Uma pauta representa assunto previsto para sessão, não decisão tomada.

## Executar

```powershell
python -m unittest discover -s tests -v
python scripts/collect_pautas.py
```

O script cria/atualiza `dados/pautas.json` somente após identificar registros válidos. Mantém registros antigos e evita duplicação pelo identificador estável da combinação data + URL.

## Limitações e próximos passos

- A página poderá mudar de estrutura; nesse caso o coletor falha sem apagar a última coleta.
- Antes de agendar, executar uma coleta real e conferir links, datas e respeito às condições do portal.
- O JSON será posteriormente importado no Cloudflare D1; ainda não há agendamento, implantação nem indicadores no site.
- Para verificar atualização de conteúdo de um PDF existente precisaremos de uma coleta de metadados ou hash do próprio documento.
