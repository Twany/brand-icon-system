#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-$HOME/.agents/skills}"

mkdir -p "$TARGET"

for skill in "$ROOT"/skills/*; do
  [ -d "$skill" ] || continue
  name="$(basename "$skill")"
  rm -rf "$TARGET/$name"
  cp -R "$skill" "$TARGET/"
  printf 'installed %s\n' "$name"
done

printf 'installed skills to %s\n' "$TARGET"
