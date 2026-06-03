#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json

from po_utils import ROOT, block_key, ensure_project_dirs, iter_field_values, split_blocks, write_po


def has_msgstr(block: str) -> bool:
    return any("".join(iter_field_values(block, field)) for field in ["msgstr", "msgstr[0]", "msgstr[1]"])


def main() -> None:
    parser = argparse.ArgumentParser(description="Split a pt_BR.po file into review batches.")
    parser.add_argument("--project", required=True, help="Project key")
    parser.add_argument("--size", type=int, default=150, help="Entries per batch")
    parser.add_argument("--all", action="store_true", help="Include all source entries instead of only untranslated entries")
    args = parser.parse_args()

    paths = ensure_project_dirs(args.project)
    source_file = paths["source"] / "pt_BR.po"
    if not source_file.exists():
        raise SystemExit(f"Missing source file: {source_file}")

    header, entries = split_blocks(source_file.read_text(encoding="utf-8"))
    if not entries:
        raise SystemExit("No PO entries found")

    if args.all:
        selected_entries = entries
    else:
        output_file = ROOT / "output" / args.project / "messages.po"
        output_keys = set()
        if output_file.exists():
            _, output_entries = split_blocks(output_file.read_text(encoding="utf-8"))
            output_keys = {block_key(entry) for entry in output_entries if has_msgstr(entry)}
        selected_entries = [
            entry
            for entry in entries
            if not has_msgstr(entry) and block_key(entry) not in output_keys
        ]

    for batch_path in paths["batches"].glob("batch-*.po"):
        batch_path.unlink()

    manifest = []
    for index in range(0, len(selected_entries), args.size):
        batch_number = (index // args.size) + 1
        batch_entries = selected_entries[index:index + args.size]
        batch_path = paths["batches"] / f"batch-{batch_number:03d}.po"
        write_po(batch_path, header, batch_entries)
        manifest.append({
            "batch": batch_path.name,
            "entries": len(batch_entries),
            "start": index + 1,
            "end": index + len(batch_entries),
        })
        print(f"wrote {batch_path}")

    manifest_path = paths["meta"] / "batches.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    mode = "all" if args.all else "pending"
    print(f"manifest {manifest_path}")
    print(f"selected {len(selected_entries)} of {len(entries)} entries ({mode})")


if __name__ == "__main__":
    main()
