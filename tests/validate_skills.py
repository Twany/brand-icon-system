#!/usr/bin/env python3
"""Validate the repository's Agent Skills layout."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REQUIRED_SKILLS = {
    "brand-icon-system",
    "brand-logo-brief",
    "brand-logo-explore",
    "brand-logo-refine",
    "brand-logo-produce",
    "brand-logo-audit",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter is not closed")
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            fail(f"Invalid frontmatter line: {line}")
        fields[match.group(1)] = match.group(2).strip().strip('"')
    return fields


def validate_skill(path: Path) -> None:
    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        fail(f"{path.name} is missing SKILL.md")
    text = skill_md.read_text(encoding="utf-8")
    fields = parse_frontmatter(text)
    if fields.get("name") != path.name:
        fail(f"{path.name} frontmatter name does not match folder")
    if not fields.get("description"):
        fail(f"{path.name} missing description")
    if "TODO" in text or "[TODO" in text:
        fail(f"{path.name} contains TODO template text")
    if len(text.splitlines()) > 500:
        fail(f"{path.name} SKILL.md is too long for progressive disclosure")


def main() -> None:
    if not SKILLS.exists():
        fail("skills/ directory is missing")
    names = {p.name for p in SKILLS.iterdir() if p.is_dir()}
    missing = REQUIRED_SKILLS - names
    if missing:
        fail(f"Missing skills: {', '.join(sorted(missing))}")
    for name in sorted(REQUIRED_SKILLS):
        validate_skill(SKILLS / name)
    for rel in (
        "skills/brand-icon-system/scripts/split_exploration_board.py",
        "skills/brand-icon-system/scripts/build_icon_system.py",
        "skills/brand-icon-system/assets/fonts/Newsreader[opsz,wght].ttf",
        "examples/ai-white-noise/exploration-contact-sheet.png",
        "examples/ai-white-noise/logo-system-overview.png",
    ):
        if not (ROOT / rel).exists():
            fail(f"Missing required file: {rel}")
    print("Skill repository is valid.")


if __name__ == "__main__":
    main()
