# Translation Guidelines

## Non-negotiable rules

- Never change `msgid`.
- Preserve placeholders, tags, escapes, and line breaks exactly.
- Preserve plural structures and all `msgstr[n]` indexes.
- If the current translation is already good, keep it.
- Prefer Brazilian ERP terminology over literal translation.

## Style

- Use concise pt-BR suitable for UI labels and help text.
- Avoid overly formal Portuguese.
- Avoid English leakage unless the term is intentionally kept by glossary.
- Avoid translating product names, module names, or framework identifiers unless the glossary says otherwise.

## Consistency priorities

1. Same `msgid` should receive the same translation unless context clearly differs.
2. Repeated business concepts should follow the glossary.
3. Framework-level actions should stay uniform across all four projects.

## High-risk items

- Python interpolation: `%s`, `%d`, `%(name)s`
- JS style placeholders: `{0}`, `{name}`
- Inline HTML like `<b>`, `<a>`, `<br>`
- Sentence fragments that appear as button labels

## Review heuristic

When reviewing an entry, prefer this order:

1. technical correctness
2. business meaning
3. glossary consistency
4. natural pt-BR
5. brevity
