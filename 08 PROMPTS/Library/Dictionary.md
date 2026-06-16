---
type: meta
name: dictionary
domain: [meta, library]
tags: [dictionary, vocabulary, standards, taxonomy]
last_reviewed: 2026-06-08
version: 2
---

# Skill & Prompt Dictionary (Controlled Vocabulary)

This is the **official dictionary** for the Library in the Laptop Sync vault (the universal truth). All frontmatter values (especially `domain`, `energy`, `tags`, `type`, `compatible_with`) **must** come from this list for consistency across all AI.

Use this when:
- Creating new skills/prompts (reference the allowed values)
- Querying with Dataview (`WHERE contains(domain, "recovery")`)
- Emitting or syncing (tools can validate against this)
- Reviewing the Library (Library Gardener skill)

## Types (`type`)

| Value     | Description                                      | When to use                                      | Example notes                  |
|-----------|--------------------------------------------------|--------------------------------------------------|--------------------------------|
| skill     | Structured, repeatable capability with steps/rules | Agentic behaviors you want to invoke or compose | daily-job-search, low-energy-execution |
| prompt    | Lighter, one-shot or template-style instructions | Quick reusable prompts or command blocks        | Specific command templates     |
| protocol  | High-level meta-instructions or frameworks       | Universal ways of thinking/operating            | thoroughness-protocol, council-strategy |
| context   | Reusable background information or status        | Persistent facts that get injected              | master-bio                     |
| guide     | Explanatory or how-to documentation              | Usage instructions for the system itself        | how-to-use-ubiquitously        |
| hub       | Dashboard / MOC for discovery and overview       | Central indexes and live views                  | 00-Hub                         |
| meta      | Self-referential notes about the Library         | Schema, dictionary, gardener processes          | SCHEMA, dictionary, library-gardener |

## Domains (`domain`)

Use arrays. Keep them specific but not too granular. New domains should be added here first.

| Domain            | Description                                      | Related to user's life                          | Example skills                     |
|-------------------|--------------------------------------------------|--------------------------------------------------|------------------------------------|
| meta              | Anything about the system itself                 | Library maintenance, tool decisions             | library-gardener, tool-mode-decider |
| library           | Core Library operations and standards            | Schema, dictionary, hub                         | schema (in meta), dictionary       |
| job               | Career, applications, tailoring, search          | PRS, HVAC, logistics, maintenance roles         | daily-job-search, apply-today, resume-tailoring, cover-letter-followup |
| execution         | Daily action, planning, follow-through           | Low energy days, routines, anchors              | low-energy-execution, weekly-review |
| social            | Communication, relationships, calibration        | Texts, boundaries, professional interactions    | social-calibration                 |
| research          | Deep dives, synthesis, option generation         | Understanding roles, industries, options        | deep-research, career-strategy     |
| decision-making   | High-stakes choices, council processes           | Job offers, life changes, big moves             | council-strategy                   |
| recovery          | Mental health, sobriety, self-management         | State Not Fate, PRS work, depression as state   | mvd-anchors, floor-wins, prs-safety-check |
| health            | Physical, biological, energy management          | MVD, light exposure, sleep, nutrition           | circadian-anchors                  |
| creative          | Roleplay, writing, idea generation, BE mode      | BE_Roleplay, creative projects                  | (link to BE_Roleplay_Generator)    |
| ai-setup          | Choosing tools, models, context management       | Tool Mode Decider, which LLM for what           | tool-mode-decider, ai-setup-audit  |
| philosophy        | Core principles and frameworks                   | State Not Fate, anchors, proof-based hope       | snf-proof-registration, snf-hope-activation |
| philosophy-snf    | State Not Fate specific principles and mechanics | Hope as prediction, anchors as substrate, visible proof, external memory, restart speed over streaks, ideal vs realistic, bottom-line-first, reading errors from inside the state, state-based scaling | snf-proof-registration, snf-hope-activation, systems-audit, substrate-reminders |
| finance           | Money, runway, budgeting decisions               | Runway tracking, job vs stability choices       | financial-stability |
| prs               | Peer Recovery Supporter specific practices       | Clinical safety, intake, support work           | prs-safety-check                   |
| sobriety          | Sobriety maintenance, triggers, daily practices  | Sober since 2019-11-01, recovery as foundation  | sobriety-anchors                   |
| career            | Long-term career pathing, trades + PRS balance   | 5-year vision, parallel tracks (PRS + HVAC)     | career-strategy, 5-year-vision-alignment |
| systems           | Systems thinking, multi-factor models            | Depression as system failure, State Not Fate    | systems-audit                      |

**Adding new domains**: Only when a clear cluster of 3+ skills emerges. Update this dictionary and the Hub queries. Prefer broad but meaningful categories over one-off tags.

## Energy Levels (`energy`)

| Value    | Description                                      | When to use / example behavior                   |
|----------|--------------------------------------------------|--------------------------------------------------|
| collapse | Near-zero capacity, biological floor only        | MVD only, 1-3 tiny anchors, no ambition          |
| low      | Fog, low motivation, need minimal friction       | Floor + 1 micro action, permission to drop everything |
| medium   | Functional but not optimal                       | Standard daily plans, some ambition OK           |
| high     | Good energy, can handle complexity               | Deep work, multiple parallel actions, ideal moves |
| any      | Works across most states                         | Meta protocols like /tp that scale               |
| variable | Depends heavily on daily status                  | Skills that check current energy first           |

**Rule**: Always pair with `When to Use` section that references energy.

## Tags (`tags`)

Use specific, searchable tags. Prefer hyphenated. Group them in your mind as:

**Core Execution Tags**
- low-energy, mvd, floor, anchors, floor-wins, proof, restart, no-shame
- daily, weekly, routine, low-friction

**Job / Career Tags**
- job, prs, hvac, logistics, maintenance, driver, resume, application, cover-letter, prs-track, certification, career
- job-search, tailoring, follow-up

**Social / Communication**
- social, communication, calibration, boundaries, professional, dating, relationships

**Research / Synthesis**
- research, deep-work, synthesis, options, analysis

**Meta / System**
- meta, library, schema, maintenance, gardener, dictionary
- tools, ai-setup, model-selection, ubiquity, standards

**Philosophy / State-Not-Fate**
- state-not-fate, philosophy, sobriety, recovery, depression-as-state, anchors, proof-based-hope, ideal-vs-realistic, bottom-line-first, reading-error, visible-proof, external-memory, restart-speed, resilience-rate, hope-meter, state-based-scaling, systems-failure, load-bearing, substrate, startup-design-problem, systems-audit, career-strategy, 5-year-vision, neuroplasticity, cognitive-offloading, evidence-based, prediction-error, dopamine-reward

**Clinical / Safety**
- clinical-safety, prs, intake, mvd, floor, no-shame, energy-aware

**Other useful / Situational**
- high-stakes, decision, council, protocol, context, bio, constraints, guide, onboarding, schema, standards
- creative, be-mode, roleplay
- finance, runway, budgeting
- 5-year-vision, partnership, family, cincinnati, field-tech, hvac, logistics, maintenance, driver, certification
- circadian, sobriety-practice, deep-dive, option-generation, systems-thinking, career-planning, rhythm, light-exposure, sleep-anchoring

**SNF-Specific Proof & Activation**
- visible-proof, external-memory, restart-speed, resilience-rate, hope-meter, floor-win, proof-registration, hope-activation, effort-reconnection, reading-error-interruption, substrate-reminder, neuroplasticity, prediction-error, habit-formation, mastery-experience, implementation-intention, relapse-prevention, cue-response, reward-normalization

**Adding tags**: Add to this dictionary first. Keep the list under ~60 active tags. Use compound tags (e.g. prs-track, floor-wins, proof-based-hope) for precision. Avoid single-word generics like "work" or "plan" — qualify them (e.g. job-plan, daily-routine).

**Dataview power users**: Tags are great for `contains(tags, "prs")` or `contains(tags, "low-energy")`. Combine with domains: `WHERE contains(domain, "recovery") AND contains(tags, "anchors")`.

## Compatible Models / Environments (`compatible_with`)

- grok (this CLI + .grok/skills)
- claude
- gpt-4o (or gpt)
- local (Ollama, LM Studio, etc.)
- all (works everywhere)
- obsidian (purely for inside the vault / Dataview)
- phone (optimized for mobile copy-paste)
- cursor (IDE context injection)
- notebooklm (document synthesis / audio overview)

**Recommendation**: Default to "all" or a short list of your primary tools. Use specific ones when a skill relies on unique capabilities (e.g. Grok's tool use or file system access).

## Other Recommended Properties (from SCHEMA)

- `last_used` (date) — for "recently used" Dataview views
- `success_rate` or qualitative notes in body
- `requires_status_block: true/false`
- `complexity`: low | medium | high (optional, for time/energy estimation)
- `estimated_time`: "5-15 min", "30+ min", etc.
- `frequency`: daily | weekly | as-needed | high-stakes
- `audience`: self | prs-client | employer | therapist | family | council (for who the output is optimized)
- `output_style`: bottom-line-first | checklist | narrative | structured | copy-paste-ready
- `priority`: high | medium | low (for Library Gardener focus)

## How to Use This Dictionary

1. When creating a new note → reference this for `domain`, `energy`, `tags`.
2. In the Hub and Dataview → use these exact strings for reliable queries.
3. In the emitter tools → can be extended to suggest or validate values.
4. When syncing to `.grok/skills` → the description + tags help with discoverability.
5. Library Gardener reviews → check that all notes only use dictionary values.

**Source of truth**: This file. Update it before creating new notes that would introduce new terms.

## Future Expansions

- Add "Audience" (self, therapist, employer, family)
- Add "Output Style" (bottom-line-first, narrative, checklist, json)
- Link each term to example notes that best exemplify it.

---

*Maintained by the Library Gardener skill. Last major expansion: 2026-06-08. This is the universal truth in the Laptop Sync vault.*
