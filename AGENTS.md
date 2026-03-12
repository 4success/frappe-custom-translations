# Translation Review Project

This repository is dedicated to reviewing and improving pt-BR gettext translations for the Frappe ecosystem.

## Scope

- Projects in scope: `frappe`, `erpnext`, `crm`, `helpdesk`
- Source language is English via gettext `msgid`
- Target language is Portuguese (Brazil)
- The final deliverable is a minimal override file that contains only changed translations

## Workflow rules

1. Do not rewrite entire `.po` files unless explicitly asked; prefer batch-sized review files.
2. Preserve gettext syntax exactly:
   - `msgid`
   - `msgctxt`
   - `msgid_plural`
   - `msgstr[n]`
   - placeholders like `%s`, `%(customer)s`, `{name}`, `{0}`
   - HTML and line breaks
3. Prefer consistency over creativity.
4. Keep labels short and interface-friendly.
5. When context is ambiguous, record the doubt in `translations/notes.md` instead of guessing aggressively.
6. Use `translations/glossary.md` as the source of truth for recurring business terms.

## Project files to read when relevant

- Global translation guidance: `docs/translation-guidelines.md`
- Project terminology notes: `docs/project-context.md`
- Approved terms and decisions: `translations/glossary.md`

## Expected outputs

- batch review updates under `translations/projects/<project>/reviewed/`
- merged file under `translations/projects/<project>/merged/pt_BR.po`
- minimal override file under `translations/projects/<project>/overrides/messages.po`
