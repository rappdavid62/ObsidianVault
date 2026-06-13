---
type: skill
name: mvd-anchors
aliases: [mvd, minimum-viable-day, floor-anchors]
description: >
  Define and protect your Minimum Viable Day (MVD) anchors — the smallest set of biological and identity actions that must happen even on collapse days to preserve self-trust and restart speed.
  Use daily when building or reviewing your floor, or when energy is low/collapse and you need to strip everything else away.
domain: [recovery, execution]
energy: low
invocation: ["/mvd", "set my anchors", "minimum viable day", "floor plan"]
compatible_with: [grok, claude, gpt, local]
version: 2
last_reviewed: 2026-06-13
tags: [recovery, mvd, anchors, floor, low-energy, prs, sobriety, state-not-fate, no-shame]
---

# MVD Anchors

## Purpose
On days when motivation, energy, or executive function is near zero, you still have a non-negotiable floor. These anchors are the proof that you showed up for yourself. They are the foundation for all State Not Fate work: stabilize the biological and identity floor first, then expand.

## When to Use
- Every morning (or the night before) to define or reaffirm your MVD.
- On low/collapse energy days when the usual plan feels impossible.
- After a relapse or bad night — restart speed matters more than perfection.
- When reviewing weekly with the Library Gardener or weekly-review skill.
- Before any big decision or high-stakes day to protect the floor.

## Core Instructions
1. Start with the user's current energy state and any immediate constraints (meds timing, light, transport, etc.).
2. Identify the absolute biological minimums that must occur to avoid self-trust damage (wake window, water/meds, light exposure, hygiene, basic nutrition, movement if possible).
3. Identify the smallest identity/prs-aligned actions (one sentence of the counter-script, one small act of care for self or others, one note in the tracker).
4. Make each anchor tiny enough that "failure" is almost impossible. If it's bigger than 2-5 minutes on a collapse day, shrink it.
5. Explicitly list what is allowed to be dropped without shame.
6. End with a "floor win" definition for the day and how it will be logged.

Always separate the Ideal MVD (what a high-energy version would look like) from the Realistic MVD (what is possible today).

## Output Format (Bottom Line First)
- **Bottom Line**: "Today's MVD floor is X anchors. Everything else is optional."
- **Biological Anchors** (2-4 items max, with exact timing or triggers where possible):
  - Wake by ___, water + meds.
  - 2-5 min outdoor light.
  - Basic hygiene / nutrition.
- **Identity / PRS Anchors** (1-2 items):
  - Speak one line of the counter-script aloud.
  - One micro act of self-care or connection.
- **What Can Be Dropped** (explicit permission list).
- **Floor Win Definition**: The smallest thing that still counts today (e.g., "I protected the three biological anchors and logged one floor win").
- **Logging / Proof**: How/where to record it so it feeds resilience tracking and hope meter.

## Context to Inject
- Current energy level and status block
- Existing MVD from previous intake or notes
- Any active medical or environmental constraints
- Counter-script / mantra from master-bio or personal profile

## Related Skills & Prompts
- [[low-energy-execution]] — use this first on collapse days; MVD anchors are the core of it.
- [[thoroughness-protocol]] — run /tp lightly when setting MVD so you don't over-ambition.
- [[floor-wins]] — the logging and proof side (pairs with snf-proof-registration for registration).
- [[weekly-review]] — review MVD effectiveness weekly.
- [[library-gardener]] — audit that your anchors are still tiny and aligned.

## Notes & History
- Directly descended from the original State Not Fate MVD work and the 09_Low_Energy_Execution_Command in the David library.
- The goal is never "more anchors" — it is "anchors small enough that you can still do them when everything else collapses."
- Update this note whenever your actual biological or identity floor changes (new meds, new living situation, new non-negotiables).
- This skill is foundational. Almost every other skill assumes the floor is protected.
- Library Gardener pass 2026-06-13: Fixed domain compliance (removed non-Dictionary 'low-energy' from domain array; retained in tags + energy:low; now strictly [recovery, execution]). Validated clean post-fix. Included in full Library-Gardener-Full-Review-Pack + Daily/Favorites/custom low-energy emits. Emitter tests (--validate, --list, --search, --daily, --favorites) passed. Re-synced to .grok/skills/, pushed to GitHub. Links to low-energy-execution, floor-wins, snf-* intact. No content changes beyond frontmatter + history.

Starter note created from Dictionary placeholders. Expand with personal MVD details and examples from your trackers.
