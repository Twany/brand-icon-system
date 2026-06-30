---
name: brand-logo-brief
description: Create a concise logo generation brief from a product theme, brand name, existing logo, or rough visual direction. Use as the first stage of the brand logo suite before generating AI logo candidates, especially when the user gives only a theme or asks for an icon system without a clear visual brief.
---

# Brand Logo Brief

Turn a loose theme into a compact, usable brief for logo exploration. Infer reasonable defaults instead of blocking, and mark assumptions clearly.

## Output Format

Return a brief with these fields:

- Brand name: the literal name if supplied, otherwise a concise working name.
- Product category: what the product does in plain language.
- Audience: the likely user and usage context.
- Tone: 3 to 5 adjectives that should guide the mark.
- Design tension: one useful contrast, such as calm/technical or editorial/tool-like.
- Visual core: the primary metaphor, action, or shape logic the mark should compress.
- Candidate territories: 5 to 8 distinct concept directions for exploration.
- Avoid: marks, motifs, or effects that would be off-brand, too generic, or legally risky.
- Color system: ink, paper, primary, primary-dark, primary-soft, and accent hex colors.
- Production notes: target output folder, brand lockup text, tagline, and any app icon constraints.

## Rules

- Keep the brief short enough to paste into an image prompt.
- Prefer product-specific metaphors over generic AI sparks, chat bubbles, magic wands, or abstract gradients.
- Choose colors for the eventual production system, but keep the next exploration stage strictly black and white.
- If the user provided a reference logo, extract its design logic rather than copying its geometry.
- Ask a question only when the brand name, legal constraint, or target product category is impossible to infer.

## Handoff

Pass the brief directly to `brand-logo-explore`. The next stage should generate a black-and-white 4x6 exploration board and stop for user selection.
