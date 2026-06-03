---
description: Fetch and split one project into review batches
agent: build
---
Prepare project `$1` for translation review.

Steps:

1. Ensure `translations/projects/$1/source/main.pot` and `translations/projects/$1/source/pt_BR.po` exist, fetching them from the branch configured for `$1` in `translations/projects.json` if needed.
2. Split the template into incremental batches of `$2` pending entries. If `$2` is empty, use `150`.
3. Summarize the generated files under `translations/projects/$1/batches/`.
