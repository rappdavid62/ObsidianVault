---
type: protocol
name: council-strategy
aliases: [/council, strategic-council]
description: >
  Convene a small virtual panel of relevant experts to debate complex or high-consequence decisions.
  Use for job offers, big money moves, health/treatment choices, relationship decisions, or anything with long-term identity or runway impact.
domain: [meta, decision-making]
energy: medium
invocation: ["/council", "council on this", "help me decide"]
compatible_with: [grok, claude, gpt, local]
version: 1
last_reviewed: 2026-06-08
tags: [meta, council, decision, high-stakes]
---

# Council Strategy Protocol (/council)

## Purpose
Replace single-perspective advice with a structured, multi-expert debate that surfaces blind spots and produces pragmatic recommendations scaled to real constraints.

## Core Instructions

```
/council

INSTRUCTIONS FOR THE AI OPERATOR:
1. ACT AS THE COUNCIL: Convene a virtual panel of 3–4 specialized experts tailored to the decision (examples: Peer Recovery Supervisor, HVAC/Field Tech Master, Logistics Operations Lead, Financial Runway Planner, Social/Relationship Translator).
2. DEBATE: Have the experts analyze the situation from their angles. They should explicitly call out each other's blind spots and operational friction.
3. CONVERGE: Synthesize into a unified recommendation that respects energy, money, identity, and long-term 5-year vision.
4. FORMAT (always):
   - Bottom Line: One-sentence strategic recommendation.
   - The Council Debate: Short, labeled exchanges showing real tension (not fake agreement).
   - Realistic Move vs. Ideal Move: What is doable now vs. the best-case version.
   - Exact Next Action: The single highest-leverage, lowest-friction step.
```

## When to Use
- Job offer or major role change decisions
- Spending or financial structure choices with multi-month impact
- Health/treatment or recovery plan pivots
- Relationship or social boundary decisions
- Anything where the user feels pulled in multiple directions or scared of regret

## Expert Lanes (common ones — invent others as needed)
- /prs — Peer Recovery lens (safety, energy floor, shame avoidance, clinical realism)
- /tech — Field/technical trades lens (apprenticeship reality, tools, physical sustainability)
- /ops — Logistics/warehouse/driver lens (throughput, schedule reliability, body management)
- /coach — Execution + job search operator lens (volume, tailoring, follow-up systems)

## Related
- [[thoroughness-protocol]] — Almost always prefix /council with /tp
- Domain skills that the council members would draw from

## Notes
This is one of the highest-leverage meta-protocols. It directly encodes the "State Not Fate" approach to difficult decisions: multiple grounded perspectives + brutal realism about constraints + one clear next action.

(This is the atomic version in the DOV vault - universal truth. All prompts consolidated here.)
