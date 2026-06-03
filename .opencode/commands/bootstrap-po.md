---
description: Fetch configured POT and pt_BR baseline files from GitHub
agent: build
---
Bootstrap the translation workspace by running the local fetch script.

- Run `python3 scripts/fetch_po.py --all` by default, respecting the pinned branches in `translations/projects.json`.
- Use branch `$1` only when the user explicitly wants a manual branch override for this bootstrap run.
- Do not default to a global `version-16` override, because `crm` and `helpdesk` may use different configured branches.
- Then summarize which project template and baseline files were downloaded.
