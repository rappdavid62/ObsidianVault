---
type: skill
name: new-skill-name-kebab-case
aliases: [short-name, /invocation]
description: >
  One or two sentences that tell an AI *exactly when and why* to use this.
  This field is critical for auto-invocation (matches .grok SKILL.md style).
domain: [job, execution, recovery, meta, ...]  # FROM DICTIONARY ONLY
energy: low | medium | high | any | collapse | variable  # FROM DICTIONARY
invocation: ["/short", "natural language trigger"]
compatible_with: [grok, claude, gpt, local, all]  # FROM DICTIONARY
version: 1
last_reviewed: 2026-06-12
tags: [tag1, tag2, ...]  # FROM DICTIONARY
---

# Human Readable Skill Name

## Purpose
One-sentence "what this does for me".

## When to Use
- Bullet conditions, including energy state, context, frequency.
- Reference the user's real constraints (runway, PRS cert, variable energy, Cincinnati location, etc.).

## Core Instructions
1. Numbered, precise, opinionated steps the AI must follow.
2. Include "Always separate Ideal Move vs Realistic Move scaled to energy."
3. Be blunt, practical, SNF-aligned (state-not-fate, visible-proof, external memory, floor wins, restart speed, no shame).

## Output Format (Bottom Line First)
- **Bottom Line**: One crisp sentence.
- **Ideal vs Realistic**:
- **Exact Next Action**:
- **Proof / Tracking**:
- Other structured sections as needed.

## Context to Inject
- Current status block
- master-bio elements
- Specific trackers or previous outputs
- Relevant constraints

## Related Skills & Prompts
- [[other-skill-1]]
- [[protocol-name]]
- Link back to [[../Dictionary]] concepts used.

## Notes & History
- What worked / didn't on which models.
- Changes in this version.
- Created/updated as part of expansion of the Laptop Sync Library (universal truth).

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)
