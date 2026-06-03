---
description: Run the full incremental translation update workflow
agent: build
---
Faça uma atualização geral incremental das traduções pt-BR.

Fluxo obrigatório:

1. Rode `python3 scripts/fetch_po.py --all`, respeitando as branches pinadas em `translations/projects.json`.
2. Rode split incremental para todos os projetos configurados:
   - `python3 scripts/split_po.py --project frappe --size 150`
   - `python3 scripts/split_po.py --project erpnext --size 150`
   - `python3 scripts/split_po.py --project crm --size 150`
   - `python3 scripts/split_po.py --project helpdesk --size 150`
3. Identifique quais projetos geraram batches em `translations/projects/<project>/batches/`.
4. Para cada projeto com batches pendentes, revise usando os subagentes definidos:
   - `translation-orchestrator`
   - `po-translator`
   - `po-reviewer`
   - `po-validator`
5. Preserve rigorosamente gettext:
   - não alterar `msgid`
   - preservar `msgctxt`
   - preservar plurais
   - preservar placeholders
   - preservar HTML e quebras de linha
6. Respeite `translations/glossary.md`, `docs/translation-guidelines.md` e `docs/project-context.md`.
7. Para cada projeto revisado, rode:
   - `python3 scripts/merge_batches.py --project <project>`
   - `python3 scripts/build_overrides.py --project <project>`
   - `python3 scripts/check_po.py --project <project>`
   - `python3 scripts/sync_output.py --project <project>`
8. Ao final, reporte:
   - projetos atualizados
   - quantidade de batches revisados
   - contagem de entradas em `merged`, `overrides` e `output`
   - pendências restantes
   - strings órfãs ou hardcoded suspeitas, se encontradas

Modo padrão: incremental. Não use `--all` no `split_po.py` a menos que o usuário peça explicitamente revisão completa.
