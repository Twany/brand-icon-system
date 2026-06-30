---
name: brand-logo-explore
description: Generate a 4x6 black-and-white AI logo exploration board, split it into numbered PNG candidates, and pause for user selection. Use when the user wants logo directions, concept candidates, a first-pass logo board, or the exploration stage of the brand icon system.
---

# Brand Logo Explore

Generate varied black-and-white logo directions, split the board into numbered candidate PNGs, and stop before final production.

## Inputs

Use a `brand-logo-brief` output when available. If only a theme is available, infer a brief inline and continue.

Choose an output folder before generation, for example:

```bash
/absolute/project/path/public/assets/brand/skill-tests/<slug>/
```

## Generate Board

Use `imagegen` or the available image generation tool to create one flat 4 columns x 6 rows exploration board. Keep it raster PNG.

Prompt shape:

```text
Create a minimalist black-and-white logo exploration board for [brand/theme].
4 columns x 6 rows, 24 distinct concepts, pure white background, black flat graphics only.
Each cell is independently centered with generous whitespace. Explore different directions:
negative space, bold geometric mass, modular mark, letter fusion, visual pun, product action,
calm symbol, rhythmic repetition, custom wordmark, and abstract emblem.
The work should feel like a restrained identity-studio exploration archive.
No color, gradients, shadows, 3D, mockups, texture, labels, numbering, UI, watermark, or cartoon illustration.
```

This exploration logic is inspired by `fucha1122/minimalist-bw-logo-skill`: use broad black-and-white concept coverage first, then produce from a selected direction. Do not copy that project's prompt text verbatim.

## Split Board

Save the board as `source/<slug>-exploration-board.png`, then run:

```bash
BRAND_ICON_SYSTEM_HOME="/absolute/path/to/skills/brand-icon-system"
python3 "$BRAND_ICON_SYSTEM_HOME/scripts/split_exploration_board.py" \
  --board /absolute/path/source/<slug>-exploration-board.png \
  --out /absolute/path/exploration-candidates
```

If AI shadows or soft borders make crops too loose, rerun with `--trim-threshold 120` to `--trim-threshold 180`.

## Quality Gate

Regenerate the board before showing it if it has:

- color, gradients, shadows, mockups, or background texture;
- labels or numbers baked into cells;
- obvious copies of known brands;
- too many text lockups instead of standalone marks;
- tiny details that will fail at favicon sizes.

## Response

Show `exploration-contact-sheet.png` with an absolute image path, list the candidate directory, and ask the user to pick candidate numbers or request another board.

Stop here by default. Do not run refinement or production unless the user explicitly requested autonomous mode, such as "pick the best one and finish".
