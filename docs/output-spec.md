# Output Specification

`build_icon_system.py` writes a production-oriented PNG asset package.

## Required Inputs

- Source mark: a simple raster PNG mark on a plain background.
- Brand name: used for lockups and documentation.
- Output directory.
- Optional color overrides.

## Asset Outputs

Marks:

- `mark-primary-transparent.png`
- `mark-primary-dark-transparent.png`
- `mark-primary-soft-transparent.png`
- `mark-accent-transparent.png`
- `mark-ink-transparent.png`
- `mark-white-transparent.png`

App icons:

- `app-icon-paper-primary-square-1024.png`
- `app-icon-paper-primary-rounded-1024.png`
- `app-icon-primary-paper-square-1024.png`
- `app-icon-ink-paper-square-1024.png`
- `app-icon-soft-dark-square-1024.png`

Favicons:

- `favicon-16.png`
- `favicon-32.png`
- `favicon-48.png`
- `favicon-64.png`
- `favicon-128.png`
- `favicon-180.png`
- `favicon-192.png`
- `favicon-512.png`

Lockups and previews:

- `lockup-primary-on-paper.png`
- `lockup-paper-on-ink.png`
- `lockup-primary-ink-transparent.png`
- `lockup-white-transparent.png`
- `scenario-header-light.png`
- `scenario-header-dark.png`
- `logo-system-overview.png`

Documentation/debug:

- `manifest.json`
- `README.md`
- `source-mark-mask.png`

## Quality Requirements

- Transparent marks must not contain a white box.
- The favicon must remain recognizable at 32px.
- App icons should have balanced padding.
- Lockups should not crowd the mark.
- The mask should be clean and unclipped.
