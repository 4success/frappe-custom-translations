---
description: Run the orthography orchestrator on one reviewed PO batch
agent: orthography-orchestrator
subtask: true
---
Review orthography and safe UI phrasing in the provided reviewed PO batch at `$1`.

Requirements:

- inspect only `msgstr`
- apply only high-confidence fixes
- preserve gettext structure exactly
- respect `translations/glossary.md`
- validate the file at the end

Return:

- number of entries changed
- ambiguous entries left unchanged
- validation status
