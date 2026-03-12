#!/usr/bin/env python3

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent.parent
PROJECTS_FILE = ROOT / "translations" / "projects.json"
PROJECTS_ROOT = ROOT / "translations" / "projects"


def load_projects() -> dict:
    data = json.loads(PROJECTS_FILE.read_text(encoding="utf-8"))
    return data["projects"]


def ensure_project_dirs(project: str) -> dict[str, Path]:
    base = PROJECTS_ROOT / project
    paths = {
        "base": base,
        "source": base / "source",
        "batches": base / "batches",
        "reviewed": base / "reviewed",
        "merged": base / "merged",
        "overrides": base / "overrides",
        "meta": base / "meta",
    }
    for path in paths.values():
        path.mkdir(parents=True, exist_ok=True)
    return paths


def normalize_text(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def split_blocks(text: str) -> tuple[str, list[str]]:
    normalized = normalize_text(text).strip()
    if not normalized:
        return "", []
    blocks = [block.strip() + "\n" for block in re.split(r"\n\s*\n", normalized) if block.strip()]
    if not blocks:
        return "", []
    if blocks[0].startswith('msgid ""') or '\nmsgid ""' in blocks[0]:
        return blocks[0], blocks[1:]
    return "", blocks


def iter_field_values(block: str, field: str) -> Iterable[str]:
    lines = block.splitlines()
    collecting = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(field + " "):
            collecting = True
            yield parse_quoted(stripped[len(field):].strip())
            continue
        if collecting and stripped.startswith('"'):
            yield parse_quoted(stripped)
            continue
        if collecting:
            break


def parse_quoted(token: str) -> str:
    if not token.startswith('"'):
        return ""
    try:
        return json.loads(token)
    except json.JSONDecodeError:
        return token.strip('"')


def block_key(block: str) -> tuple[str, str, str]:
    msgctxt = "".join(iter_field_values(block, "msgctxt"))
    msgid = "".join(iter_field_values(block, "msgid"))
    msgid_plural = "".join(iter_field_values(block, "msgid_plural"))
    return msgctxt, msgid, msgid_plural


def block_has_translation(block: str) -> bool:
    return any(line.lstrip().startswith("msgstr") for line in block.splitlines())


def write_po(path: Path, header: str, entries: list[str]) -> None:
    parts: list[str] = []
    if header:
        parts.append(header.strip() + "\n")
    parts.extend(entry.strip() + "\n" for entry in entries)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(parts).strip() + "\n", encoding="utf-8")


PERCENT_RE = re.compile(r"%(?:\([^)]+\))?[#0 +\-]?(?:\d+|\*)?(?:\.\d+)?[a-zA-Z]")
BRACE_RE = re.compile(r"\{[a-zA-Z0-9_]+\}")


def extract_placeholders(text: str) -> list[str]:
    return sorted(PERCENT_RE.findall(text) + BRACE_RE.findall(text))


def read_msgid_and_msgstr_text(block: str) -> tuple[str, str]:
    msgid = "".join(iter_field_values(block, "msgid"))
    msgstr_parts: list[str] = []
    for line in block.splitlines():
        stripped = line.strip()
        if stripped.startswith("msgstr"):
            remainder = stripped.split(" ", 1)[1] if " " in stripped else ""
            msgstr_parts.append(parse_quoted(remainder.strip()))
    if not msgstr_parts:
        for index in range(10):
            prefix = f"msgstr[{index}]"
            msgstr_parts.extend(iter_field_values(block, prefix))
    return msgid, "".join(msgstr_parts)
