---
description: Run the translation orchestrator on one PO batch
agent: translation-orchestrator
subtask: true
---
Review and improve the gettext batch at `$1`.

Requirements:

- apply `translations/glossary.md`
- follow `docs/translation-guidelines.md`
- infer the project from the path
- if the file lives in `batches/`, create or update the matching file in `reviewed/`
- use `po-translator`, then `po-reviewer`, then `po-validator` as needed
- keep a concise note in `translations/notes.md` for any unresolved ambiguity
