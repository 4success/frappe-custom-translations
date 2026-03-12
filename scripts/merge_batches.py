#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path

from po_utils import ensure_project_dirs, split_blocks, write_po


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge reviewed PO batches into one file.")
    parser.add_argument("--project", required=True, help="Project key")
    args = parser.parse_args()

    paths = ensure_project_dirs(args.project)
    source_file = paths["source"] / "pt_BR.po"
    if not source_file.exists():
        raise SystemExit(f"Missing source file: {source_file}")

    header, _ = split_blocks(source_file.read_text(encoding="utf-8"))
    reviewed_files = sorted(paths["reviewed"].glob("batch-*.po"))
    if not reviewed_files:
        raise SystemExit(f"No reviewed batch files found in {paths['reviewed']}")

    merged_entries: list[str] = []
    for batch in reviewed_files:
        _, entries = split_blocks(batch.read_text(encoding="utf-8"))
        merged_entries.extend(entries)
        print(f"included {batch}")

    target = paths["merged"] / "pt_BR.po"
    write_po(target, header, merged_entries)
    print(f"wrote {target}")


if __name__ == "__main__":
    main()
