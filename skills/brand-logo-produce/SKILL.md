---
name: brand-logo-produce
description: Convert an approved raster logo mark into a complete PNG asset system with transparent marks, app icons, favicons, lockups, theme-color variants, previews, manifest, and README. Use only after the user approves a final mark or explicitly requests an autonomous end-to-end logo production run.
---

# Brand Logo Produce

Build the production PNG logo system from one approved raster mark.

## Preconditions

Run this stage only after a final mark is approved, or when the user clearly requested an autonomous end-to-end run. Do not use this stage directly after an exploration board unless a candidate has already been selected.

Required inputs:

- approved source mark PNG;
- brand name;
- output directory;
- color system: ink, paper, primary, primary-dark, primary-soft, and accent;
- optional tagline and wordmark dot preference.

## Build

Use the shared production script:

```bash
BRAND_ICON_SYSTEM_HOME="/absolute/path/to/skills/brand-icon-system"
python3 "$BRAND_ICON_SYSTEM_HOME/scripts/build_icon_system.py" \
  --mark /absolute/path/source-mark.png \
  --brand "BrandName" \
  --out /absolute/path/logo-system \
  --tagline "Short product promise" \
  --primary "#2F6F64" \
  --primary-dark "#24574F" \
  --primary-soft "#D9E8E3" \
  --paper "#F7F8F6" \
  --ink "#171B18" \
  --accent "#B7791F"
```

Useful options:

- `--no-dot` removes the small punctuation dot after the wordmark.
- `--threshold <n>` adjusts background removal; increase for noisy backgrounds, lower if the mark gets eaten.
- `--mark-scale <0.70-0.86>` adjusts mark size inside app icons.
- `--font-weight` and `--font-opsz` tune Newsreader; defaults are `680` and `56`.

## Expected Outputs

The script writes:

- `mark-*-transparent.png` transparent mark variants;
- `app-icon-*-square-1024.png` app-icon-ready square PNGs;
- `favicon-*.png` and touch-icon sizes;
- `lockup-primary-on-paper.png`, `lockup-paper-on-ink.png`, and transparent lockups;
- `scenario-header-light.png` and `scenario-header-dark.png`;
- `logo-system-overview.png`;
- `manifest.json`, `README.md`, and `source-mark-mask.png`.

## Handoff

After production, use `brand-logo-audit` on the output folder before presenting the result as final.
