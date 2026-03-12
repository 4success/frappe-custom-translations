#!/usr/bin/env python3

from __future__ import annotations

import argparse

from po_utils import block_key, ensure_project_dirs, split_blocks, write_po


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
    source_map = {block_key(entry): entry.strip() for entry in source_entries}

    changed_entries = []
    for entry in merged_entries:
        key = block_key(entry)
        normalized = entry.strip()
        if source_map.get(key) != normalized:
            changed_entries.append(entry)

    target = paths["overrides"] / "messages.po"
    write_po(target, merged_header or source_header, changed_entries)
    print(f"wrote {target} with {len(changed_entries)} changed entries")


if __name__ == "__main__":
    main()
