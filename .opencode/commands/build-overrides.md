---
description: Merge reviewed batches and generate a minimal override file
agent: build
---
For project `$1`, run the local consolidation workflow.

Steps:

1. Merge reviewed batches back into `translations/projects/$1/merged/pt_BR.po`.
2. Generate `translations/projects/$1/overrides/messages.po` with only changed entries.
3. Validate the generated files.
4. Summarize the output paths and any validation failures.
