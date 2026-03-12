# Frappe pt-BR Translation Workflow

This repository is a working area for reviewing and overriding pt-BR translations for Frappe v16 apps with OpenCode.

It is set up for these projects:

- `frappe/frappe`
- `frappe/erpnext`
- `frappe/crm`
- `frappe/helpdesk`

## What is included

- OpenCode project rules in `AGENTS.md`
- project config in `opencode.json`
- custom subagents in `.opencode/agents/`
- custom commands in `.opencode/commands/`
- helper scripts in `scripts/`
- translation workspace in `translations/`

## Recommended flow

1. Fetch the original `pt_BR.po` files from the matching branch:

   ```bash
   python3 scripts/fetch_po.py --all --branch version-16
   ```

2. Split one project into smaller review batches:

   ```bash
   python3 scripts/split_po.py --project frappe --size 150
   ```

3. Open OpenCode in this directory and use the custom agents or commands.

4. Merge reviewed batches back into one file:

   ```bash
   python3 scripts/merge_batches.py --project frappe
   ```

5. Generate a minimal override file with only changed entries:

   ```bash
   python3 scripts/build_overrides.py --project frappe
   ```

6. Validate the result:

   ```bash
   python3 scripts/check_po.py --project frappe
   ```

7. Import the generated override into another project or custom app using the file:

   ```text
   translations/projects/<project>/overrides/messages.po
   ```

   This is the import-ready artifact. The `merged/pt_BR.po` file is the full reviewed result, while `overrides/messages.po` contains only entries that differ from the original source file.

## Applying the overrides in an environment

The generated `overrides/messages.po` files are meant to be shipped inside a custom Frappe app.

Recommended approach:

1. Create or use an existing custom app in the target environment.

2. Place the override file in the app locale directory using the target language code:

   ```text
   your_app/locale/pt_BR.po
   ```

3. If your environment needs overrides from more than one product, combine the relevant override files into a single `pt_BR.po` file for that app while preserving gettext structure, contexts, plural forms, placeholders, and HTML.

4. Ensure the custom app is installed on the target site.

5. Compile the translations so the application can load the updated gettext catalog.

6. Clear application cache after compilation.

7. Make sure the user or site language is set to `pt-BR` / `pt_BR`.

Notes:

- In Frappe v16, `.po` files are the standard translation format.
- The custom app acts as an override layer for core apps such as Frappe, ERPNext, CRM, and Helpdesk.
- If a translated string does not change immediately, clear cache again and reload the UI.
- If a string still does not match, verify the exact `msgid`, optional `msgctxt`, and plural form entries.

## OpenCode shortcuts

- `/bootstrap-po version-16`
- `/prepare-project frappe 150`
- `/translate-batch translations/projects/frappe/batches/batch-001.po`
- `/review-batch translations/projects/frappe/reviewed/batch-001.po`
- `/build-overrides frappe`

## Output layout

After bootstrap, each project uses this shape:

```text
translations/projects/<project>/
  source/pt_BR.po
  batches/batch-001.po
  reviewed/batch-001.po
  merged/pt_BR.po
  overrides/messages.po
```

## Notes

- Keep the branch aligned with production, usually `version-16`.
- `crm` and `helpdesk` currently default to `main` in `translations/projects.json` because their repos publish v16-compatible translations there.
- Edit the glossary in `translations/glossary.md` before large review passes.
- The override output is the file you can ship inside your custom app.
- After updating reviewed batches, run `scripts/merge_batches.py`, `scripts/build_overrides.py`, and `scripts/check_po.py` before exporting files for import.
