---
name: brand-logo-refine
description: Refine a selected logo exploration candidate into clean AI-generated PNG mark options. Use after the user chooses candidate numbers from a logo exploration contact sheet, or when an existing rough mark needs to become a production-ready isolated raster logo.
---

# Brand Logo Refine

Turn an approved exploration direction into a clean isolated mark suitable for production exports.

## Preconditions

Start only when one of these is true:

- the user selected one or more candidate numbers from an exploration contact sheet;
- the user supplied a specific rough mark file to refine;
- the user explicitly authorized autonomous selection.

If no candidate or source mark is available, ask for a selection instead of generating final assets.

## Prepare Candidate

When the source is an exploration board, prepare a selected candidate:

```bash
BRAND_ICON_SYSTEM_HOME="/absolute/path/to/skills/brand-icon-system"
python3 "$BRAND_ICON_SYSTEM_HOME/scripts/split_exploration_board.py" \
  --board /absolute/path/source/<slug>-exploration-board.png \
  --out /absolute/path/exploration-candidates \
  --selected 7
```

Use the selected candidate as visual reference when the active image tool supports reference images. Otherwise, describe its shape logic in the prompt.

## Generate Refined Marks

Generate one to four isolated PNG mark options. Keep the mark source simple enough for clean mask extraction.

Prompt shape:

```text
Minimal premium app logo mark for [brand/theme], based on direction #[N] from the exploration board.
No text, simple rounded geometric symbol, strong negative space, crisp solid black silhouette on pure white background.
Make it readable at 32px, with natural proportions and no tiny interior fragments.
High-resolution PNG, no shadow, no gradient, no mockup, no texture, no background pattern.
```

## Quality Gate

Reject or regenerate marks that:

- depend on gradients, lighting, glass, texture, or photoreal effects;
- include fragile hairlines, tiny holes, or noisy edges;
- feel too close to the reference brand or any known logo;
- cannot be described as one simple mark without text;
- lose their idea at 32px.

## Response

If there is one refined mark and the user requested autonomous mode, hand it to `brand-logo-produce`.

If there are multiple options, show the options with absolute image paths and ask which one should become the production mark. Do not run production until the user approves a final mark.
