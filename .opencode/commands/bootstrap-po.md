---
description: Fetch all configured pt_BR.po source files from GitHub
agent: build
---
Bootstrap the translation workspace by running the local fetch script.

- Use branch `$1` when provided.
- If no branch argument is provided, default to `version-16`.
- Run `python3 scripts/fetch_po.py --all` with the appropriate branch.
- Then summarize which project files were downloaded.
