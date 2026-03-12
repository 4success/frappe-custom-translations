#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

from po_utils import ROOT, ensure_project_dirs, load_projects, split_blocks


OUTPUT_ROOT = ROOT / "output"
OUTPUT_README = OUTPUT_ROOT / "README.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync override files to output/ and refresh entry counts."
    )
    parser.add_argument(
        "--project",
        action="append",
        dest="projects",
        help="Project key to sync (can be passed multiple times)",
    )
    return parser.parse_args()


def count_entries(po_file: Path) -> int:
    header, entries = split_blocks(po_file.read_text(encoding="utf-8"))
    return len(entries)


def sync_project(project: str) -> tuple[Path, int]:
    paths = ensure_project_dirs(project)
    source = paths["overrides"] / "messages.po"
    if not source.exists():
        raise SystemExit(f"Missing override file: {source}")

    target = OUTPUT_ROOT / project / "messages.po"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    return target, count_entries(target)


def update_output_readme(counts: dict[str, int]) -> None:
    text = OUTPUT_README.read_text(encoding="utf-8")
    for project, count in counts.items():
        pattern = rf"- `{re.escape(project)}`: \d+ entradas"
        replacement = f"- `{project}`: {count} entradas"
        text, replaced = re.subn(pattern, replacement, text, count=1)
        if replaced == 0:
            raise SystemExit(f"Could not update count for {project} in {OUTPUT_README}")
    OUTPUT_README.write_text(text, encoding="utf-8")


def main() -> None:
    args = parse_args()
    all_projects = load_projects().keys()
    projects = args.projects or list(all_projects)

    invalid = [project for project in projects if project not in all_projects]
    if invalid:
        raise SystemExit(f"Unknown project(s): {', '.join(invalid)}")

    counts: dict[str, int] = {}
    for project in projects:
        target, count = sync_project(project)
        counts[project] = count
        print(f"synced {target} with {count} changed entries")

    update_output_readme(counts)
    print(f"updated {OUTPUT_README}")


if __name__ == "__main__":
    main()
