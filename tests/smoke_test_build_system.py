#!/usr/bin/env python3
"""Smoke test the PNG logo system builder."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/brand-icon-system/scripts/build_icon_system.py"


def make_mark(path: Path) -> None:
    img = Image.new("RGB", (1024, 1024), "white")
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((270, 170, 710, 850), radius=150, fill="black")
    draw.pieslice((250, 395, 820, 965), start=205, end=335, fill="white")
    img.save(path)


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        mark = tmp_path / "mark.png"
        out = tmp_path / "logo-system"
        make_mark(mark)
        subprocess.run(
            [
                "python3",
                str(SCRIPT),
                "--mark",
                str(mark),
                "--brand",
                "Noisewave",
                "--out",
                str(out),
                "--tagline",
                "Focus through calm sound.",
            ],
            check=True,
        )
        for name in (
            "mark-primary-transparent.png",
            "app-icon-paper-primary-square-1024.png",
            "favicon-32.png",
            "lockup-primary-on-paper.png",
            "logo-system-overview.png",
            "manifest.json",
            "README.md",
            "source-mark-mask.png",
        ):
            assert (out / name).exists(), f"missing output {name}"
    print("Build system smoke test passed.")


if __name__ == "__main__":
    main()
