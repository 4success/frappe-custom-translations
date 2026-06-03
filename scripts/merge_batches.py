#!/usr/bin/env python3

from __future__ import annotations

import argparse

from po_utils import ROOT, block_key, ensure_project_dirs, read_msgid_and_msgstr_text, split_blocks, write_po


def has_msgstr(block: str) -> bool:
    return bool(read_msgid_and_msgstr_text(block)[1])


def msgstr_lines(block: str) -> list[str]:
    lines = block.splitlines()
    result: list[str] = []
    index = 0
    while index < len(lines):
        stripped = lines[index].lstrip()
        if stripped.startswith("msgstr"):
            result.append(lines[index])
            index += 1
            while index < len(lines) and lines[index].lstrip().startswith('"'):
                result.append(lines[index])
                index += 1
            continue
        index += 1
    return result


def apply_msgstr(source_block: str, translated_block: str) -> str:
    replacement = msgstr_lines(translated_block)
    if not replacement:
        return source_block

    lines = source_block.splitlines()
    merged: list[str] = []
    index = 0
    replaced = False
    while index < len(lines):
        stripped = lines[index].lstrip()
        if not replaced and stripped.startswith("msgstr"):
            merged.extend(replacement)
            replaced = True
            index += 1
            while index < len(lines) and lines[index].lstrip().startswith('"'):
                index += 1
            continue
        merged.append(lines[index])
        index += 1
    return "\n".join(merged) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge reviewed PO batches into one file.")
    parser.add_argument("--project", required=True, help="Project key")
    args = parser.parse_args()

    paths = ensure_project_dirs(args.project)
    source_file = paths["source"] / "main.pot"
    if not source_file.exists():
        raise SystemExit(f"Missing source file: {source_file}")

    header, source_entries = split_blocks(source_file.read_text(encoding="utf-8"))

    translations = {}
    baseline_file = paths["source"] / "pt_BR.po"
    if baseline_file.exists():
        baseline_header, baseline_entries = split_blocks(baseline_file.read_text(encoding="utf-8"))
        header = baseline_header or header
        translations.update({block_key(entry): entry for entry in baseline_entries if has_msgstr(entry)})

    output_file = ROOT / "output" / args.project / "messages.po"
    if output_file.exists():
        _, output_entries = split_blocks(output_file.read_text(encoding="utf-8"))
        translations.update({block_key(entry): entry for entry in output_entries if has_msgstr(entry)})

    reviewed_files = sorted(paths["reviewed"].glob("batch-*.po"))
    for batch in reviewed_files:
        _, entries = split_blocks(batch.read_text(encoding="utf-8"))
        translations.update({block_key(entry): entry for entry in entries if has_msgstr(entry)})
        print(f"included {batch}")

    merged_entries = [
        apply_msgstr(entry, translations[key]) if (key := block_key(entry)) in translations else entry
        for entry in source_entries
    ]

    target = paths["merged"] / "pt_BR.po"
    write_po(target, header, merged_entries)
    print(f"wrote {target} with {len(merged_entries)} source-aligned entries")


if __name__ == "__main__":
    main()
