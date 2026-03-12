#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

from po_utils import ensure_project_dirs, load_projects


def fetch_project(name: str, branch_override: str | None) -> Path:
    projects = load_projects()
    if name not in projects:
        raise SystemExit(f"Unknown project: {name}")

    config = projects[name]
    branch = branch_override or config["branch"]
    url = (
        f"https://raw.githubusercontent.com/{config['owner']}/{config['repo']}"
        f"/{branch}/{config['po_path']}"
    )
    paths = ensure_project_dirs(name)
    target = paths["source"] / "pt_BR.po"
    metadata = paths["meta"] / "source.json"

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        raise SystemExit(f"Failed to fetch {url}: HTTP {exc.code}") from exc

    target.write_text(content, encoding="utf-8")
    metadata.write_text(
        json.dumps({"url": url, "branch": branch, "repo": config["repo"]}, indent=2) + "\n",
        encoding="utf-8",
    )
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch upstream pt_BR.po files from GitHub.")
    parser.add_argument("--project", help="Project key from translations/projects.json")
    parser.add_argument("--all", action="store_true", help="Fetch all configured projects")
    parser.add_argument("--branch", help="Override the configured branch")
    args = parser.parse_args()

    if not args.project and not args.all:
        raise SystemExit("Use --project <name> or --all")

    projects = load_projects()
    selected = list(projects) if args.all else [args.project]

    failures = []
    for project in selected:
        try:
            path = fetch_project(project, args.branch)
        except SystemExit as exc:
            failures.append(f"{project}: {exc}")
            continue
        print(f"fetched {project}: {path}")

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
