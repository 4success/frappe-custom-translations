---
description: Discard local translation memory and start a full review from current POT files
agent: build
---
Faça um refresh geral das traduções pt-BR, descartando a memória local revisada e começando a revisão completa novamente.

Este comando é destrutivo. Antes de apagar qualquer arquivo, confirme explicitamente com o usuário que pode descartar a memória local de tradução.

Escopo destrutivo:

- remover batches antigos em `translations/projects/<project>/batches/`
- remover revisões antigas em `translations/projects/<project>/reviewed/`
- remover artefatos gerados em `translations/projects/<project>/merged/`
- remover artefatos gerados em `translations/projects/<project>/overrides/`
- remover `output/<project>/messages.po`
- preservar `translations/projects/<project>/source/main.pot`
- preservar `translations/projects/<project>/source/pt_BR.po`
- preservar `translations/glossary.md`, docs e notas

Fluxo obrigatório:

1. Pare e peça confirmação explícita ao usuário antes de executar qualquer ação destrutiva.
2. Rode `git status --short` e reporte os arquivos afetados antes da limpeza.
3. Rode `python3 scripts/fetch_po.py --all`, respeitando as branches pinadas em `translations/projects.json`.
4. Limpe os artefatos locais dos projetos configurados conforme o escopo destrutivo acima. Não use `git reset`, `git checkout` ou comandos destrutivos fora desse escopo.
5. Rode split completo com `--all` para todos os projetos configurados:
   - `python3 scripts/split_po.py --project frappe --size 150 --all`
   - `python3 scripts/split_po.py --project erpnext --size 150 --all`
   - `python3 scripts/split_po.py --project crm --size 150 --all`
   - `python3 scripts/split_po.py --project helpdesk --size 150 --all`
6. Revise os batches usando os subagentes definidos:
   - `translation-orchestrator`
   - `po-translator`
   - `po-reviewer`
   - `po-validator`
7. Preserve rigorosamente gettext:
   - não alterar `msgid`
   - preservar `msgctxt`
   - preservar plurais
   - preservar placeholders
   - preservar HTML e quebras de linha
8. Respeite `translations/glossary.md`, `docs/translation-guidelines.md` e `docs/project-context.md`.
9. Para cada projeto revisado, rode:
   - `python3 scripts/merge_batches.py --project <project>`
   - `python3 scripts/build_overrides.py --project <project>`
   - `python3 scripts/check_po.py --project <project>`
   - `python3 scripts/sync_output.py --project <project>`
10. Ao final, reporte:
   - projetos atualizados
   - quantidade de batches revisados
   - contagem de entradas em `merged`, `overrides` e `output`
   - pendências restantes
   - strings órfãs ou hardcoded suspeitas, se encontradas

Modo obrigatório: revisão completa. Use `--all` no `split_po.py`.
