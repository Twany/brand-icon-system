# Agent Instructions

This repository contains an Agent Skills suite. Keep the root project host-neutral and keep host-specific metadata inside the relevant platform conventions.

## Skill Rules

- Keep each skill directory self-contained with a required `SKILL.md`.
- Keep the staged workflow intact: brief, explore, select, refine, produce, audit.
- Do not skip the user selection pause unless the user explicitly authorizes autonomous mode.
- Keep shared deterministic scripts in `skills/brand-icon-system/scripts/`.
- Do not add private brand assets, customer logos, tokens, credentials, or account details.
- Run the validation commands before handoff.

## Validation

```bash
python3 tests/validate_skills.py
python3 tests/smoke_test_split_board.py
python3 tests/smoke_test_build_system.py
```
