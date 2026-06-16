---
type: skill
name: deep-research
aliases: [research, deep-dive, /research]
description: >
  Conduct focused, high-signal research on a topic while avoiding rabbit holes and producing actionable synthesis.
  Use for job research, understanding a company/industry, learning a skill area, or investigating options.
domain: [research, execution]
energy: medium
invocation: ["/research", "help me research this", "deep dive on"]
compatible_with: [grok, claude, gpt, local]
version: 1
last_reviewed: 2026-06-08
tags: [research, deep-work, job]
---

# Deep Research

## Purpose
Turn "I need to understand X" into a bounded, high-value research session that produces clear options, risks, next actions, and synthesized knowledge — without spending 4 hours and ending up more confused.

## When to Use
- Researching a specific company, role type, certification path, or industry before applying or deciding.
- Learning the real mechanics of something (e.g., what HVAC apprenticeship actually looks like day-to-day).
- When you have a decision that requires more than surface knowledge.

## Core Instructions
1. Clarify the exact question or decision the research serves.
2. Set tight scope and time box (e.g., "30 focused minutes on day-to-day reality of union vs non-union HVAC helper roles").
3. Pull from high-signal sources first (official sites, recent worker reports, specific forums, official program pages).
4. Explicitly note bias and reliability of sources.
5. Synthesize into:
   - Key facts / realities
   - Pros/cons or tradeoffs relevant to the user's constraints (energy, money, location, recovery)
   - Realistic pathways and timelines
   - Red flags and green flags
6. End with "what this means for my next actions" tied back to the original decision.

Strongly prefer primary sources and recent first-hand accounts over generic career advice sites.

## Output Format (Bottom Line First)
- **Bottom Line**: One-sentence synthesis of the most important reality discovered.
- **Core Findings**: Bullet list of high-confidence facts.
- **Tradeoffs for Me**: How this interacts with the user's specific situation (energy, PRS path, financial runway, location in Cincinnati area, etc.).
- **Pathways & Timelines**: Concrete options with rough steps and time estimates.
- **Red / Green Flags**: Things to watch for or prioritize.
- **Recommended Next Actions**: 1–3 specific moves (research more of X, talk to Y, apply to Z, etc.).

## Context to Inject
- The specific question or decision this research serves
- User's current status, constraints, and job targets
- Any prior research or assumptions the user has

## Related Skills & Prompts
- [[council-strategy]] (use research output as input to a council decision)
- [[daily-job-search]] (research often feeds target identification)
- The original "07_Deep_Research_Command.md"

## Notes & History
- This skill is especially important for someone balancing multiple possible career tracks (PRS + trades) and needing real information rather than inspirational content.
- Update when the user develops better research sources or methods.
