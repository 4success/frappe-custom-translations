#!/usr/bin/env python3

from __future__ import annotations

import argparse

from po_utils import block_key, ensure_project_dirs, parse_quoted, split_blocks, write_po


def msgstr_values(block: str) -> dict[str, str]:
    values: dict[str, str] = {}
    lines = block.splitlines()
    index = 0
    while index < len(lines):
        stripped = lines[index].strip()
        if stripped.startswith("msgstr"):
            parts = stripped.split(" ", 1)
            field = parts[0]
            text = parse_quoted(parts[1].strip()) if len(parts) > 1 else ""
            index += 1
            while index < len(lines) and lines[index].strip().startswith('"'):
                text += parse_quoted(lines[index].strip())
                index += 1
            values[field] = text
            continue
        index += 1
    return values


def has_msgstr(block: str) -> bool:
    return any(value for value in msgstr_values(block).values())


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate minimal override PO files.")
    parser.add_argument("--project", required=True, help="Project key")
    args = parser.parse_args()

    paths = ensure_project_dirs(args.project)
    source_file = paths["source"] / "pt_BR.po"
    merged_file = paths["merged"] / "pt_BR.po"
    if not source_file.exists():
        raise SystemExit(f"Missing source file: {source_file}")
    if not merged_file.exists():
        raise SystemExit(f"Missing merged file: {merged_file}")

    source_header, source_entries = split_blocks(source_file.read_text(encoding="utf-8"))
    merged_header, merged_entries = split_blocks(merged_file.read_text(encoding="utf-8"))
    source_map = {block_key(entry): msgstr_values(entry) for entry in source_entries}

    changed_entries = []
    for entry in merged_entries:
        key = block_key(entry)
        if has_msgstr(entry) and source_map.get(key, {}) != msgstr_values(entry):
            changed_entries.append(entry)

    target = paths["overrides"] / "messages.po"
    write_po(target, merged_header or source_header, changed_entries)
    print(f"wrote {target} with {len(changed_entries)} changed entries")


if __name__ == "__main__":
    main()
