---
name: brand-icon-system
description: Orchestrate a staged Agent Skills suite for AI-generated PNG logo and icon systems from a product theme, brand name, existing logo, or rough visual direction. Use when the user asks for an app icon, logo mark, logo exploration board, brand icon set, favicon/app-icon package, theme-color variants, lockups, or a brand-kit overview, especially when they should choose from visual candidates before final production.
---

# Brand Icon System

Use this as the suite entry point. It routes work through smaller stage skills so logo generation stays interactive instead of becoming a one-shot export.

## Suite

Read the relevant sibling `SKILL.md` before executing that stage:

- `brand-logo-brief`: turn a loose theme into a compact logo brief.
- `brand-logo-explore`: generate a black-and-white 4x6 exploration board, split candidates, and pause for selection.
- `brand-logo-refine`: turn a selected candidate into clean isolated mark options.
- `brand-logo-produce`: export the approved mark into a complete PNG asset system.
- `brand-logo-audit`: inspect the generated assets before handoff or production replacement.

## Default Flow

1. Use `brand-logo-brief` unless the user already supplied a complete brief.
2. Use `brand-logo-explore` to generate and split a black-and-white candidate board.
3. Stop and ask the user to choose candidate numbers from `exploration-contact-sheet.png`.
4. Use `brand-logo-refine` only after the user chooses a candidate or authorizes autonomous selection.
5. Stop again if multiple refined marks are generated.
6. Use `brand-logo-produce` only after one final mark is approved.
7. Use `brand-logo-audit` before presenting the output as final.

## Interaction Contract

Default to staged interaction. Do not generate the final logo system immediately after the first exploration board.

Pause after:

- the exploration contact sheet is ready;
- refined mark variants are ready;
- an audit fails and needs a rerun choice.

Autonomous mode is allowed only when the user clearly says something like "你自己选", "直接跑完整流程", "no need to ask", or "pick the best one and finish". Do not treat silence, a broad theme, or "生成一套" as permission to skip selection.

## Shared Resources

Find the installed `brand-icon-system` skill directory before running shared scripts. In a repository checkout, it is usually `<repo>/skills/brand-icon-system`. In an installed user skill directory, it is usually beside the sibling `brand-logo-*` skills.

```bash
BRAND_ICON_SYSTEM_HOME="/absolute/path/to/skills/brand-icon-system"
"$BRAND_ICON_SYSTEM_HOME/scripts/split_exploration_board.py"
"$BRAND_ICON_SYSTEM_HOME/scripts/build_icon_system.py"
"$BRAND_ICON_SYSTEM_HOME/assets/fonts/Newsreader[opsz,wght].ttf"
```

Stage skills should reuse these resources rather than copying them.

## Quality Bar

Prefer one memorable mark over many decorative variants. Reject marks that are copied from known brands, depend on gradients or photoreal effects, use fragile tiny details, recolor poorly, fail at favicon size, or feel disconnected from the product theme.

Do not replace production app assets unless the user explicitly asks for that.
