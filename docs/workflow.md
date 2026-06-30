# Workflow

Brand Icon System is staged because logo work has subjective decision points. The agent should not generate final production assets before the user sees candidate directions.

## 1. Brief

Use `brand-logo-brief` to turn a loose product theme into:

- brand name;
- product category;
- audience;
- tone;
- design tension;
- visual core;
- candidate territories;
- avoid list;
- color system;
- production notes.

## 2. Explore

Use `brand-logo-explore` to generate a black-and-white 4x6 board of 24 directions. The board must be flat, monochrome, and label-free.

Split the board with:

```bash
BRAND_ICON_SYSTEM_HOME="/absolute/path/to/skills/brand-icon-system"
python3 "$BRAND_ICON_SYSTEM_HOME/scripts/split_exploration_board.py" \
  --board /absolute/path/source/brand-exploration-board.png \
  --out /absolute/path/exploration-candidates
```

Then show `exploration-contact-sheet.png` and stop for selection.

## 3. Refine

Use `brand-logo-refine` only after the user picks a candidate number or explicitly asks the agent to pick. Generate one to four clean isolated mark options. If there are multiple options, pause again.

## 4. Produce

Use `brand-logo-produce` only after one final mark is approved. It runs:

```bash
BRAND_ICON_SYSTEM_HOME="/absolute/path/to/skills/brand-icon-system"
python3 "$BRAND_ICON_SYSTEM_HOME/scripts/build_icon_system.py" \
  --mark /absolute/path/source-mark.png \
  --brand "BrandName" \
  --out /absolute/path/logo-system
```

## 5. Audit

Use `brand-logo-audit` before handoff. Check the mask, transparent PNGs, app icon padding, favicon readability, lockups, colors, and overview board.
