#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path

from po_utils import ensure_project_dirs, split_blocks, write_po


def main() -> None:
    parser = argparse.ArgumentParser(description="Split a pt_BR.po file into review batches.")
    parser.add_argument("--project", required=True, help="Project key")
    parser.add_argument("--size", type=int, default=150, help="Entries per batch")
    args = parser.parse_args()

    paths = ensure_project_dirs(args.project)
    source_file = paths["source"] / "pt_BR.po"
    if not source_file.exists():
        raise SystemExit(f"Missing source file: {source_file}")

    header, entries = split_blocks(source_file.read_text(encoding="utf-8"))
    if not entries:
        raise SystemExit("No PO entries found")

    manifest = []
    for index in range(0, len(entries), args.size):
        batch_number = (index // args.size) + 1
        batch_entries = entries[index:index + args.size]
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
    print(f"manifest {manifest_path}")


if __name__ == "__main__":
    main()
