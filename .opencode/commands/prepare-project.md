---
description: Fetch and split one project into review batches
agent: build
---
Prepare project `$1` for translation review.

Steps:

1. Ensure `translations/projects/$1/source/pt_BR.po` exists, fetching it from branch `version-16` if needed.
2. Split the source file into incremental batches of `$2` pending entries. If `$2` is empty, use `150`.
3. Summarize the generated files under `translations/projects/$1/batches/`.
