---
type: skill
name: low-energy-execution
aliases: [low-energy, collapse-plan, /low]
description: >
  Generate a realistic, shame-free execution plan when energy is low or collapsed.
  Use whenever the user reports low/collapse energy, brain fog, or "I can't do normal things today."
domain: [execution]
energy: low
invocation: ["/low", "low energy plan", "I'm in collapse", "brain fog today"]
compatible_with: [grok, claude, gpt, local]
version: 2
last_reviewed: 2026-06-13
tags: [low-energy, mvd, floor, no-shame]
---

# Low Energy Execution

## Purpose
Protect the floor. Turn a day that would otherwise be lost to paralysis or shame into a small number of biological and identity-preserving actions that generate proof and keep self-trust alive.

## When to Use
- User explicitly says energy is low, collapse, fog, or "I can't".
- Morning check-in shows collapse or very low.
- After a bad night, big emotional event, or when the usual plan feels impossible.

## Core Instructions
1. Accept the current energy state without negotiation or "you should try harder."
2. Default to **Minimum Viable Day (MVD)** / floor anchors only.
3. Focus on biological basics first (wake/meds/water, light, hygiene, food, movement that doesn't require motivation).
4. One non-negotiable floor win that is small enough to be almost certain.
5. Explicitly give permission to drop everything else.
6. End with a tiny proof element (even just "I chose the floor plan and executed one thing").

Never:
- Add ambitious items
- Use streak language or "make up for lost time"
- Introduce new projects or big decisions on collapse days

## Output Format (Bottom Line First)
- **Bottom Line**: "Today is a floor day. Here is the minimal plan that still counts."
- **MVD / Biological Anchors** (the 2–4 non-negotiables, customized from user's current MVD).
- **Permitted Drops**: What can be ignored without self-attack.
- **One Floor Win**: The smallest action that still registers as a win.
- **Optional Micro-Add** (only if energy feels slightly better than pure collapse): one 5-minute thing max.
- **End-of-Day Proof**: How to log this so it feeds the resilience / hope system.

## Context to Inject
- User's current MVD (from intake or status)
- Current energy state (user report or morning check-in)
- Any active status block elements that affect the floor (e.g. meds timing, important appointment)

## Related Skills & Prompts
- [[daily-job-search]] (scale way down or skip entirely on true collapse days)
- [[thoroughness-protocol]] (use lightly — collapse days are not the time for heavy /tp)
- Low energy templates from the AI Life Coach Friend system
- The original "09_Low_Energy_Execution_Command.md" from David library

## Notes & History
- Core State Not Fate principle: protect self-trust through consistent small wins rather than heroic efforts followed by shame.
- The plan must be so small that "failure" is almost impossible on a collapse day.
- Update MVD references in this note when the user's actual Minimum Viable Day changes.
- Library Gardener pass 2026-06-13: Fixed domain compliance (removed invalid 'low-energy' and 'daily' from domain array; now strictly [execution] per Dictionary, low-energy specificity via tags + energy field). Re-validated clean. Emitted in Daily, Favorites, Full-Review, and cluster packs. Emitter functionality (validate/list/search/custom) passed all tests. Re-synced to .grok/skills/, GitHub push. Links to mvd-anchors, floor-wins, thoroughness-protocol, daily-job-search intact. No body changes.
