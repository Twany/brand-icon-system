#!/usr/bin/env python3
"""Smoke test the exploration board splitter."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/brand-icon-system/scripts/split_exploration_board.py"


def make_board(path: Path) -> None:
    cols, rows = 4, 6
    cell = 220
    board = Image.new("RGB", (cols * cell, rows * cell), "white")
    draw = ImageDraw.Draw(board)
    for index in range(cols * rows):
        row, col = divmod(index, cols)
        x = col * cell + 60
        y = row * cell + 60
        draw.rounded_rectangle((x, y, x + 100, y + 100), radius=22, fill="black")
        draw.rectangle((x + 52, y + 28, x + 138, y + 74), fill="black")
    board.save(path)


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        board = tmp_path / "board.png"
        out = tmp_path / "candidates"
        make_board(board)
        subprocess.run(
            [
                "python3",
                str(SCRIPT),
                "--board",
                str(board),
                "--out",
                str(out),
            ],
            check=True,
        )
        candidates = sorted(out.glob("candidate-*.png"))
        assert len(candidates) == 24, f"expected 24 candidates, got {len(candidates)}"
        assert (out / "exploration-contact-sheet.png").exists()
    print("Split board smoke test passed.")


if __name__ == "__main__":
    main()
