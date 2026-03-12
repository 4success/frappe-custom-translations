#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from po_utils import block_has_translation, ensure_project_dirs, extract_placeholders, read_msgid_and_msgstr_text, split_blocks


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []

    msgfmt = shutil.which("msgfmt")
    if msgfmt:
        result = subprocess.run(
            [msgfmt, "--check-format", "-o", "/dev/null", str(path)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            return [result.stderr.strip() or result.stdout.strip() or f"msgfmt failed for {path}"]

    header, entries = split_blocks(path.read_text(encoding="utf-8"))
    if not header and not entries:
        return [f"{path}: empty or unparsable file"]

    for index, entry in enumerate(entries, start=1):
        if not block_has_translation(entry):
            errors.append(f"{path}: entry {index} has no msgstr")
            continue
        msgid, msgstr = read_msgid_and_msgstr_text(entry)
        if not msgstr:
            continue
        if extract_placeholders(msgid) != extract_placeholders(msgstr):
            errors.append(
                f"{path}: entry {index} placeholder mismatch: {extract_placeholders(msgid)} != {extract_placeholders(msgstr)}"
            )

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate gettext PO files.")
    parser.add_argument("--project", help="Validate a project's merged and override files")
    parser.add_argument("--file", help="Validate one specific PO file")
    args = parser.parse_args()

    if not args.project and not args.file:
        raise SystemExit("Use --project <name> or --file <path>")

    files: list[Path] = []
    if args.project:
        paths = ensure_project_dirs(args.project)
        files.extend([
            paths["source"] / "pt_BR.po",
            paths["merged"] / "pt_BR.po",
            paths["overrides"] / "messages.po",
        ])
    if args.file:
        files.append(Path(args.file))

    failures = []
    for file_path in files:
        if not file_path.exists():
            failures.append(f"missing file: {file_path}")
            continue
        errors = validate_file(file_path)
        if errors:
            failures.extend(errors)
        else:
            print(f"ok {file_path}")

    if failures:
        for failure in failures:
            print(failure)
        sys.exit(1)


if __name__ == "__main__":
    main()
