---
name: brand-logo-audit
description: Inspect a generated PNG logo system for mask quality, small-size readability, color behavior, lockup composition, and handoff completeness. Use after brand-logo-produce or when reviewing generated logo asset folders before replacing production app assets.
---

# Brand Logo Audit

Check that a generated logo system is actually usable before handoff or production replacement.

## Inspect

Open or visually inspect these files when present:

- `source-mark-mask.png`
- `mark-primary-transparent.png`
- `mark-ink-transparent.png`
- `app-icon-paper-primary-square-1024.png`
- `app-icon-primary-paper-square-1024.png`
- `favicon-32.png`
- `lockup-primary-on-paper.png`
- `lockup-paper-on-ink.png`
- `logo-system-overview.png`

## Checks

Pass the audit only when:

- the mask is clean, not clipped, and has no background haze;
- the mark reads at favicon sizes and remains recognizable at 32px;
- transparent PNGs have no unwanted white box;
- app icons have balanced scale and safe padding;
- lockups use readable typography and do not crowd the mark;
- color variants preserve contrast on paper and dark backgrounds;
- the overview board is not overlapping, cropped, or misleading;
- `manifest.json` and `README.md` exist for handoff.

## Fixes

- If the mask is fuzzy, rerun `brand-logo-produce` with a different `--threshold`.
- If the mark is too small or crowded in app icons, rerun with `--mark-scale`.
- If the source has shadows, gradients, or background noise, return to `brand-logo-refine` for a cleaner mark.
- If a lockup is typographically weak, adjust `--font-weight`, `--font-opsz`, `--no-dot`, or the tagline.

## Response

For a passing audit, show `logo-system-overview.png` and one primary lockup using absolute image paths, then list the output directory.

For a failed audit, state the failed checks and the exact rerun or refinement needed. Do not recommend replacing production app assets until the audit passes.
