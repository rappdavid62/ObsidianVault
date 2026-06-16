# Mobile Favorites – Obsidian Skill & Prompt Library (Laptop Sync vault - universal truth)
# Generated for quick copy-paste on phone
# Source: 08 PROMPTS/Library (syncs via Google Drive)
# Tip: Prefix with /tp or /council when needed.


## thoroughness-protocol
```
---
type: protocol
name: thoroughness-protocol
aliases: [/tp, thoroughness]
description: >
  Force the AI to stop, reality-check, and produce grounded plans instead of superficial advice.
  Prefix almost any non-trivial request with this, especially when energy is limited or stakes are real.
domain: [meta, execution]
energy: any
invocation: ["/tp", "be thorough", "thoroughness protocol"]
compatible_with: [grok, claude, gpt, local]
version: 1
last_reviewed: 2026-06-08
tags: [meta, protocol, bottom-line]
---
```

# Thoroughness Protocol (/tp)

## Purpose
A universal prefix that makes any AI (including this one) behave like a careful, constraint-aware operator instead of an optimistic cheerleader or vague advisor.

## Core Instructions (to be given to the model)

```
/tp

INSTRUCTIONS FOR THE AI OPERATOR:
1. STOP and allocate explicit reasoning steps before responding.
2. PERFORM A REALITY CHECK: Identify the user's current status block, energy constraints, and financial runway.
3. DETECT UNCERTAINTY: Explicitly state what you know, what you do not know, and what is speculation or assumption.
4. OUTLINE RISKS: Identify potential bottlenecks, friction points, energy costs, or failure modes in any proposed actions.
5. SCALE THE PLAN: Clearly separate the "Ideal Move" (optimal if everything were easy) from the "Realistic Move" (what is actually doable today given real constraints).
6. FORMAT: Start with a crisp "Bottom Line". End with a single "Exact Next Action" (or very small set of next actions). Use the user's actual energy state to size the recommendation.
```

## When to Use
- At the start of almost any planning, research, decision, or execution conversation.
- Any time the user is low energy, in fog, or has limited runway.
- Before big recommendations or multi-step plans.

## Output Discipline (the AI must follow)
- Bottom Line first (one sentence).
- Reality check + constraints.
- Ideal vs Realistic split.
- Explicit risks / friction.
- Exact Next Action (smallest useful step).
- No fluff, no moralizing, no "you've got this" unless it is earned by the plan.

## Related
- council-strategy (use /tp + /council together for high-stakes decisions)
- Domain skills that the council members would draw from

## Notes
This protocol is the foundation of the entire State Not Fate execution style. It is the single highest-leverage meta-skill in the library.

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)


## low-energy-execution
```
---
type: skill
name: low-energy-execution
aliases: [low-energy, collapse-plan, /low]
description: >
  Generate a realistic, shame-free execution plan when energy is low or collapsed.
  Use whenever the user reports low/collapse energy, brain fog, or "I can't do normal things today."
domain: [execution, low-energy, daily]
energy: low
invocation: ["/low", "low energy plan", "I'm in collapse", "brain fog today"]
compatible_with: [grok, claude, gpt, local]
version: 1
last_reviewed: 2026-06-12
tags: [low-energy, mvd, floor, no-shame]
---
```

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
6. End with a tiny proof element (even just "I chose not to punish myself for a missed day" or "I drank water when I woke up").

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
- daily-job-search (scale way down or skip entirely on true collapse days)
- thoroughness-protocol (use lightly — collapse days are not the time for heavy /tp)
- floor-wins (the logging and proof side)
- weekly-review — review MVD effectiveness weekly.
- The original "09_Low_Energy_Execution_Command.md" from David library

## Notes & History
- Core State Not Fate principle: protect self-trust through consistent small wins rather than heroic efforts followed by shame.
- The plan must be so small that "failure" is almost impossible on a collapse day.
- Update this note whenever your actual biological or identity floor changes (new meds, new living situation, new non-negotiables).

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)


## daily-job-search
```
---
type: skill
name: daily-job-search
aliases: [jobsearch, hunt-jobs, /jobsearch]
description: >
  Execute a focused, low-friction daily job search session.
  Use when the user wants structured help with leads, applications, tailoring, or maintaining pipeline momentum without burning out.
domain: [job, execution]
energy: low
invocation: ["/jobsearch", "daily job search", "help with job hunt today"]
compatible_with: [grok, claude, gpt, local]
version: 1
last_reviewed: 2026-06-08
tags: [job, daily, low-energy, prs-track]
---
```

# Daily Job Search

## Purpose
Turn vague "I should look for jobs" into a concrete, bounded, proof-generating session that respects current energy while moving the needle on applications and leads.

## When to Use
- Morning or early in the day when energy is at least "medium" or "low but not collapse".
- As part of a weekly rhythm (e.g. 3–5 focused sessions per week).
- When the status block shows runway pressure or job search has gone cold.

## Core Instructions
1. Start with the user's current status block (runway, energy, top target roles, recent activity).
2. Pull or suggest 3–8 realistic leads or applications that match the priority list (PRS, HVAC helper, low-voltage/field tech, maintenance, warehouse, driving).
3. For each lead or application, produce the minimal high-leverage next action (tailor resume, send message, fill form, follow up).
4. Generate exact copy-paste artifacts when useful (tailored bullets, message drafts, application notes).
5. End with a tiny "floor win" that counts as progress even on a bad day (e.g. "saved 2 good leads", "sent one low-friction message").
6. Update or suggest updates to the job_search_tracker.

Always separate:
- **Ideal Move** (what a high-energy, well-resourced version would do)
- **Realistic Move** (what is actually doable today given energy/money/fog/transport)

## Output Format (Bottom Line First)
- **Bottom Line**: One sentence summary of today's job search focus and expected output volume.
- **Leads / Targets** (3–8 items with source, why it fits, next action).
- **Artifacts** (ready-to-use resume bullets, cover letter snippets, outreach messages).
- **Tracking Note**: Suggested rows or status changes.
- **Floor Win**: The smallest thing that still counts as movement today.
- **Risks / Friction**: What could stop execution and how to reduce it.

## Context to Inject
- Current status block (especially job targets, runway, energy)
- Recent job_search_tracker entries
- Master bio / constraints (PRS cert, work history with Eleeo/D2C, Clark And Sons, etc.)
- Priority role list

## Related Skills & Prompts
- low-energy-execution (scale way down or skip entirely on true collapse days)
- resume-tailoring
- apply-today
- council-strategy (for big decisions about which roles to chase hard)
- The full David AI Prompt Library commands for the classic 12-command flow

## Notes & History
- Designed for the specific constraint set: money runway pressure, variable energy, PRS career path + trade skills as parallel tracks.
- Prefers volume of low-friction actions over perfection on any single application.
- Update this note after any session where the real workflow diverged significantly from the instructions.

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)


## social-calibration
```
---
type: skill
name: social-calibration
aliases: [social, message-drafting, /social, social-translator]
description: >
  Translate social or professional situations and draft low-cognitive-load responses.
  Use for texts, DMs, emails, dating, awkward conversations, boundary setting, or when you need to understand what someone actually meant.
domain: [social, execution]
energy: low
invocation: ["/social", "help me reply to this", "social calibration", "what did they mean"]
compatible_with: [grok, claude, gpt, local]
version: 1
last_reviewed: 2026-06-08
tags: [social, low-energy, communication, prs]
---
```

# Social Calibration & Drafting

## Purpose
Reduce social paralysis and over-explaining. Produce responses that are clear, polite, direct, and preserve your dignity and intelligence while respecting the other person's reality.

## When to Use
- Incoming message, comment, or situation that feels charged, confusing, or high-stakes.
- You want to reply but your brain is offering either "ghost" or "over-explain everything".
- Boundary setting, dating, professional follow-ups, family, or friend dynamics.

## Core Instructions
1. Analyze the situation from multiple angles without assuming malice or sainthood.
2. Give the user a clear "likely meaning" + "how you are probably being perceived".
3. Offer a risk assessment and a recommended strategy.
4. Produce 2–3 draft versions: Best (your target tone), Safer (lower risk), Bolder (higher agency).
5. Explicitly say what not to say.
6. Keep cognitive load low — short, scannable output.

Tone rules: Polite, direct, clear. Not needy. Not robotic. Not over-explained. Preserve controlled weirdness when it is part of the user's actual voice.

## Output Format
- **Bottom Line**: Recommended overall strategy in one sentence.
- **Reading**: Likely meaning of the other person + how you are probably coming across.
- **Risk / Social Math**: What could go wrong and how bad it actually is.
- **Drafts**:
  - Best response
  - Safer version
  - Bolder version (optional)
- **What Not to Say** (and why)
- **Send / No-send verdict** (when a message is involved)

## Context to Inject
- The exact incoming message or situation description
- Relationship to the other person (power dynamic, history, your goal)
- Your current energy (affects how much "safer" vs "authentic" we bias toward)

## Related Skills & Prompts
- low-energy-execution (on collapse days, default to very short or "no send for now")
- council-strategy (for big relationship or boundary decisions)
- The Social Translator section from the AI Life Coach Friend system

## Notes & History
- Directly descended from the Social_Calibration and Social_Translator pieces in the two main tucked libraries.
- One of the highest daily-use skills for preserving energy and self-trust in a world full of ambiguous social input.

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)


## apply-today
```
---
type: skill
name: apply-today
aliases: [apply, submit-application, /apply]
description: >
  Turn a job lead or posting into a completed, high-quality application with minimal friction.
  Use when you have a specific opportunity in front of you and need to execute the apply step.
domain: [job, execution]
energy: low
invocation: ["/apply", "help me apply to this", "submit this job"]
compatible_with: [grok, claude, gpt, local]
version: 1
last_reviewed: 2026-06-12
tags: [job, application, low-friction]
---
```

# Apply Today

## Purpose
Take a specific job posting or lead and produce everything needed to submit a strong application right now, without getting stuck in perfectionism or research rabbit holes.

## When to Use
- You have a concrete posting, email, or lead in front of you.
- Energy is at least "low" (not full collapse).
- Part of a daily job search session after identifying targets.

## Core Instructions
1. Analyze the posting/lead against your priority roles and constraints.
2. Decide quickly: Strong fit / Decent fit / Stretch / Skip. Only proceed on Strong or Decent.
3. Produce the minimal set of artifacts needed for this specific application:
   - Tailored resume version (or key bullet adjustments)
   - Cover letter or message draft (if required)
   - Any form answers or short responses
4. Include a "why this fits me" note for your own tracking.
5. Give the exact next action: "Copy this into the application portal and submit" or "Send this message to X".

Keep it extremely practical. No long motivational text.

## Output Format (Bottom Line First)
- **Bottom Line**: Go / No-Go + one-sentence rationale.
- **Fit Analysis**: How this matches your targets, what you bring, what might be a gap.
- **Specific Changes**:
  - Bullets to add / reword / move up
  - Summary paragraph (full draft)
  - Section reordering suggestions
- **What to Keep**: Things that are already strong or don't need changing for this target.
- **Honesty Check**: Any areas where you're stretching and how to frame them safely.

## Context to Inject
- The full job posting or lead details
- Your current resume (or key sections)
- Master bio / work history highlights relevant to this role
- Current status (especially if this is a priority role)

## Related Skills & Prompts
- daily-job-search (this is often the execution step after target identification)
- resume-tailoring
- council-strategy (for "should I even apply to this?" on bigger opportunities)

## Notes & History
- Designed for the user's specific mix of PRS certification + trade experience.
- Emphasizes speed and volume on decent fits over perfection on "dream" roles.
- Update this skill when you create new base materials or certifications.

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)


## council-strategy
```
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
```

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
- thoroughness-protocol — Almost always prefix /council with /tp
- Domain skills that the council members would draw from

## Notes
This is one of the highest-leverage meta-protocols. It directly encodes the "State Not Fate" approach to difficult decisions: multiple grounded perspectives + brutal realism about constraints + one clear next action.

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)


## mvd-anchors
```
---
type: skill
name: mvd-anchors
aliases: [mvd, anchors, /mvd]
description: >
  Define and protect the Minimum Viable Day (MVD) floor with tiny, non-negotiable biological and identity anchors on low/collapse energy days. Generate proof, preserve self-trust, and enable fast restart speed. Use every morning or whenever energy is near zero.
domain: [recovery, execution, low-energy]
energy: low
invocation: ["/mvd", "mvd anchors", "floor anchors today", "set my mvd"]
compatible_with: [grok, claude, gpt, local, all]
version: 1
last_reviewed: 2026-06-12
tags: [recovery, mvd, anchors, floor, low-energy, state-not-fate, prs, no-shame]
---
```

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
- low-energy-execution — use this first on collapse days; MVD anchors are the core of it.
- thoroughness-protocol — run /tp lightly when setting MVD so you don't over-ambition.
- floor-wins — the logging and proof side.
- weekly-review — review MVD effectiveness weekly.
- library-gardener — audit that your anchors are still tiny and aligned.

## Notes & History
- Directly descended from the original State Not Fate MVD work and the 09_Low_Energy_Execution_Command in the David library.
- The goal is never "more anchors" — it is "anchors small enough that you can still do them when everything else collapses."
- Update this note whenever your actual biological or identity floor changes (new meds, new living situation, new non-negotiables).
- This skill is foundational. Almost every other skill assumes the floor is protected.

**Scientific Basis (substrate reminders)**
- Neuroplasticity through repetition: Doidge (2007, *The Brain That Changes Itself*); small consistent cues (light exposure, water + meds, counter-script) drive BDNF release and strengthen neural pathways for energy regulation and identity.
- Behavioral activation basics: Lewinsohn (1970s origins) + modern meta-analyses — scheduling minimal biological/identity actions on low days breaks the inactivity-depression cycle and creates upward spirals.
- Implementation intentions for low motivation: Gollwitzer (1999+) — pre-deciding "if collapse, then do the 2-minute light anchor" bypasses decision fatigue.
- Recovery & routine stability: Studies on circadian and sobriety anchors show they improve sleep architecture, reduce craving, and support cognitive function needed for job search/trades learning.

**Practical Examples from Your Life**
- True collapse morning: Wake + water/meds + 5 min light (even if sitting). "I protected the biological floor" as the win.
- Post-lapse restart: Add one identity anchor (speak "sober since 2019-11-01, this is temporary") to the MVD.
- High-stakes day prep (PRS interview or HVAC ride-along): Use realistic MVD so you don't burn out before the event.
- Weekly review input: Track which anchors are still "failure-proof" and adjust (e.g., new transport constraints in Cincinnati).

**DOV Integration Note**
Keep the MVD list visible in your DOV daily notes or a dedicated tracker. The project 2026 daily ritual starts with these anchors. Emit the skill and log the win so the external memory is consistent across your synced devices.

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)


## floor-wins
```
---
type: skill
name: floor-wins
aliases: [floorwin, proof-log, /floorwin]
description: >
  Log even the tiniest actions as visible external proof on low/collapse days. Floor wins repair the damaged reward system, feed the hope meter and resilience-rate, and accelerate restart speed. Never let a day with any action go unregistered.
domain: [recovery, execution, low-energy]
energy: low
invocation: ["/floor", "log floor win", "register proof today"]
compatible_with: [grok, claude, gpt, local, all]
version: 1
last_reviewed: 2026-06-12
tags: [recovery, floor-wins, proof, low-energy, state-not-fate, visible-proof, external-memory, no-shame]
---
```

# Floor Wins

## Purpose
Depression and low energy destroy the brain's ability to register small victories. Floor wins are the deliberate, externalized proof that you did something that mattered when everything felt impossible. They are the raw material for the resilience calculation (restart speed) and the hope meter (action → results → repetition).

## When to Use
- At the end of any day where you used low-energy-execution or MVD anchors.
- Immediately after completing even one tiny anchor on a collapse day.
- When reviewing the week and you only have "floor" level activity to show.
- After any relapse or missed day — to accelerate restart speed.
- As input to weekly-review or library-gardener.

## Core Instructions
1. Start with the user's report of what actually happened (energy, what anchors were hit or missed).
2. Translate even the tiniest action into a "win" framed as proof against the voice that says "nothing matters."
3. Log it in a way that is visible later (tracker, note, or status block) so it compounds.
4. Explicitly name the emotional or identity shift it created ("I kept one promise to myself").
5. If nothing happened, help the user find the micro-proof anyway (e.g., "I chose not to punish myself for a missed day" or "I drank water when I woke up").

Never let the day end with zero recorded proof on low-energy days.

## Output Format (Bottom Line First)
- **Bottom Line**: "Today I protected the floor with X floor win(s)."
- **Floor Wins Logged**:
  - Specific action (tiny, timestamped if possible).
  - Why it counts as proof (against which depressive script).
  - Emotional/identity shift created.
- **Resilience / Hope Impact** (light connection):
  - How this feeds restart speed or the current hope level.
- **Next Floor Opportunity** (if relevant): What would protect the floor tomorrow if today was hard.

## Context to Inject
- Current energy and what was actually done (or not done)
- MVD anchors from the day (cross-reference mvd-anchors)
- Recent tracker entries or status
- Counter-script or personal "reasons to live" / identity statements

## Related Skills & Prompts
- mvd-anchors — the actions that create floor wins; this skill is the logging/proof layer.
- low-energy-execution — primary consumer of floor wins.
- weekly-review — aggregate floor wins into weekly proof.
- thoroughness-protocol — use lightly so you don't dismiss small wins.
- library-gardener — review whether floor wins are actually being captured and feeding the system.

## Notes & History
- Core State Not Fate mechanism: external memory + proof registration repairs the damaged reward system.
- "Floor win" language is deliberately non-heroic. A floor win on a collapse day is worth more than a "productive" day on high energy in terms of long-term self-trust.
- Update this note whenever your logging method changes (new tracker, app, notebook, etc.).
- This skill pairs especially well with the hope meter and resilience rate calculations in the broader system.

**Scientific Basis (substrate reminders)**
- Reward prediction error & dopamine: Schultz (1997 foundational work) + modern reviews (e.g., *Nature Reviews Neuroscience* on anhedonia) — visible small successes create positive prediction errors that gradually restore motivation and "wanting" even when mood is low.
- Implementation intentions & follow-through: Gollwitzer & Sheeran (2006) meta-analysis — "if [low energy day], then [log this tiny win as proof]" roughly doubles the chance the action gets registered.
- Self-efficacy & mastery experiences: Bandura (1997) — accumulated floor wins (especially logged externally) are the strongest source of belief in one's ability to influence outcomes (job pipeline, 5-year vision).
- Behavioral activation for depression: Dimidjian et al. (2006) and subsequent trials — structured small-action registration outperforms many talk therapies for long-term symptom reduction and functioning.

**Practical Examples from Your Life**
- Collapse day after bad night: "I chose not to punish myself and drank water" logged in Proof-Log + status. Counters "nothing matters" script; feeds snf-hope-activation.
- Job search low-volume day: "Saved two realistic PRS/HVAC leads and updated tracker" as floor win. Ties directly to daily-job-search and the project tracker.
- Post-relapse or high-shame moment: "I spoke one line of counter-script today" registered as proof against the "erases the week" reading error.
- Weekly review input: Aggregate floor wins show restart speed improvement; use in systems-audit to see impact on career and recovery systems.

**DOV Integration Note**
The DOV is your primary device-synced vault. These proof practices should live in your daily trackers and status blocks there. Emit the skill from the Library (synced via GitHub) and register wins so the external memory survives across devices. The 2026 project proof log is designed to be usable in the DOV.

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)


## prs-safety-check
```
---
type: skill
name: prs-safety-check
aliases: [safety, prs-check, /safety, /prscheck]
description: >
  Run a structured, compassionate, peer-support safety screen on yourself (leveraging PRS certification). Check risk areas, biological floor, and identity anchors first on difficult mornings or after triggers. Output clear mode guidance: full plan / floor only / reach out.
domain: [prs, recovery, health]
energy: low
invocation: ["/safety", "prs safety check", "run the safety screen", "am I safe to plan"]
compatible_with: [grok, claude, gpt, local, all]
version: 1
last_reviewed: 2026-06-12
tags: [prs, recovery, clinical-safety, low-energy, state-not-fate, anchors, no-shame]
---
```

# PRS Safety Check

## Purpose
As a certified Peer Recovery Supporter, you have training in recognizing when someone (including yourself) is in acute risk or needs immediate biological/identity stabilization. This skill turns that training inward in a structured, compassionate, and action-oriented way. It is the clinical floor underneath all other State Not Fate work.

## When to Use
- First thing in the morning on any day after a trigger, bad night, or high emotional load.
- Before any major decision or social interaction when energy is questionable.
- After any suicidal ideation, heavy substance craving, or dissociation episode (even passive).
- As a weekly or post-relapse audit with weekly-review or library-gardener.
- When the voice says "this is too much" — run the check before deciding what "too much" actually is.

## Core Instructions
1. Use the user's self-report of current state (energy, thoughts, physical sensations, recent events).
2. Apply PRS lens: safety first, no shame, scale to capacity, connect to professional help if needed.
3. Check the big three risk areas (suicidality/passive ideation, psychosis/unreality, mania/racing) using the language from your training and the original State Not Fate safety screening.
4. Check biological floor basics (meds adherence window, hydration, light, sleep debt, nutrition).
5. Check identity anchors (counter-script contact, one act of self-care or connection).
6. Output clear "safe to proceed with X" vs "protect the floor only" vs "reach out now" guidance.
7. Always include the national/local crisis numbers and your personal safe contacts if risk is elevated.

Tone must be calm, grounded, non-judgmental, direct — exactly the PRS voice you would use with a client.

## Output Format (Bottom Line First)
- **Bottom Line**: "Current safety status: Green / Yellow / Red. Recommended mode for the day: full plan / floor only / reach out."
- **Risk Screening** (quick, private):
  - Suicidality / passive ideation level.
  - Reality testing / dissociation.
  - Mania / racing / impulsivity.
- **Biological Floor Check**:
  - Meds / water / light / hygiene / nutrition status.
- **Identity / Connection Floor**:
  - Counter-script contact.
  - One micro act of care.
- **Action Guidance**:
  - What is safe to attempt today.
  - What must be protected or dropped.
  - Who/when to contact if Yellow or Red.
- **Crisis Resources** (always present when risk is not Green):
  - 988 (call or text)
  - Your personal safe contacts
  - Local crisis line or ER guidance

## Context to Inject
- Current energy and recent events
- Any active safety plan or reasons-to-live list
- Medication schedule and recent adherence
- Counter-script / personal identity statements
- Recent status block or tracker notes

## Related Skills & Prompts
- low-energy-execution and mvd-anchors — the operational follow-through after a safety check says "floor only".
- thoroughness-protocol — run lightly; safety checks must stay grounded, not overly analytical.
- council-strategy — use the PRS expert lane when the check is Yellow/Red and big decisions are pending.
- social-calibration — for reaching out to safe contacts without over-explaining.
- Original State Not Fate safety screening and PRS training materials.

## Notes & History
- This skill is the clinical application of your Peer Recovery Supporter certification (APS.006470) turned inward.
- It is deliberately non-therapeutic: it is peer support + State Not Fate floor protection.
- Update whenever your personal safety contacts, local resources, or medication regimen change.
- This is a "use before you use other skills" gate on difficult days.

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)


## snf-proof-registration
```
---
type: skill
name: snf-proof-registration
aliases: [proof, register-proof, visible-proof, /proof]
description: >
  Immediately register any action (even tiny floor wins or anchors) as visible external proof. Counter "reading errors," feed the hope meter and resilience-rate, and make restart speed real. Never let a low-energy or post-lapse day with any effort go unregistered in external memory.
domain: [philosophy-snf, recovery, execution]
energy: low
invocation: ["/proof", "register proof", "log visible proof", "snf proof"]
compatible_with: [grok, claude, gpt, local, all]
version: 1
last_reviewed: 2026-06-12
tags: [philosophy-snf, recovery, proof, visible-proof, external-memory, state-not-fate, floor-wins, restart-speed, reading-error, low-energy]
---
```

# SNF Proof Registration

## Purpose
Depression damages the brain's ability to register that small actions still matter. "Visible proof" and "external memory" are the corrective mechanisms: you write it down so the future self (or the low-hope brain) can see the evidence that effort can shape tomorrow. This directly supports restart speed (how fast you recover from a lapse) and the hope meter (proof that action → results).

## When to Use
- Immediately after any anchor or MVD completion, no matter how small.
- At the end of a low/collapse day when you still managed one floor win.
- After a lapse or "bad day" to prevent the whole week from being erased in your mind.
- When updating trackers or status blocks.
- During weekly-review or library-gardener passes to aggregate proof.

## Core Instructions
1. Start with the user's report of what actually happened (even if "only" one thing).
2. Translate the action into "visible proof" language: what changed in the external world or record because of the effort.
3. Record it in a persistent, reviewable place (tracker, note, log) so it survives memory distortion.
4. Explicitly counter the "reading error": "A rough day/week does not prove the plan is fake."
5. Link it to restart speed or hope if relevant: "This is evidence I can still return."

Never let a day with any action go unregistered on low-energy or post-lapse days.

## Output Format (Bottom Line First)
- **Bottom Line**: "Visible proof registered: [specific evidence]. This shows effort can still shape the substrate."
- **Action Performed**: The tiny thing done (timestamped if possible).
- **Visible Change / Record**: What is now different or written down because of it.
- **Counter to Reading Error**: How this interrupts "bad day = total failure."
- **Link to Metrics**: How it feeds resilience-rate (restart) or hope-meter (evidence of agency).
- **Next Proof Opportunity** (optional): What small action could generate more evidence tomorrow.

## Context to Inject
- Current energy and any recent lapse or weak period.
- The specific anchor or MVD that was completed (cross-ref mvd-anchors or floor-wins).
- Recent status or tracker entries.
- SNF principles: depression as systems failure, hope as prediction, external memory over internal judgment.

## Related Skills & Prompts
- mvd-anchors and floor-wins — the actions that generate the proof; this skill is the registration layer.
- low-energy-execution — primary context where proof is most needed.
- weekly-review and library-gardener — aggregate and audit the accumulated proof.
- thoroughness-protocol — use lightly so you don't over-explain the proof.
- snf-hope-activation — proof is one of the main inputs to hope restoration.

## Notes & History
- Core State Not Fate mechanism from the canonical project system: "written proof that a bad day no longer erases the week", "visible proof that tomorrow can still be shaped", "external memory".
- "Proof" here is not motivational fluff; it is literal externalized data that survives the damaged reward prediction system.
- Update this note whenever your logging/tracking method changes (new app, notebook, status block format).
- This skill is foundational for long-term restartability and the 5-year vision of stable function.

**Scientific Basis (substrate reminders)**
The "substrate" that proof registration targets is the brain's reward prediction and memory systems, which depression blunts. Visible, external registration provides counter-evidence that updates these systems:
- Cognitive offloading: Writing things down reduces working memory load and improves follow-through (Risko & Gilbert, 2016, *Trends in Cognitive Sciences* — "Cognitive offloading").
- Reward prediction error: Small visible successes reliably update striatal dopamine signaling even when mood is low (reviews in *Nature Reviews Neuroscience* on anhedonia and behavioral activation).
- Self-efficacy via mastery experiences: Bandura (1997) — the most powerful source of efficacy beliefs is "performance accomplishments" that are made salient.
- Behavioral activation evidence: Dimidjian et al. (2006) and subsequent meta-analyses show structured small-action registration outperforms many other depression treatments on long-term outcomes.
- Additional: Extended mind (Clark & Chalmers 1998); implementation intentions (Gollwitzer & Sheeran 2006); habit formation (Wood & Neal 2007).
Use the exact phrasing "This shows effort can still shape the substrate" as a deliberate counter-script to depressive attributional style (Abramson et al., 1978 learned helplessness model).

**Enhanced Practical Ties to Your 2026 Project & DOV**
- Any project action: Log in the project's Proof-Log.md with the exact phrasing + visible change.
- Job search day: Register "saved X leads + updated tracker" as visible proof in the job_search_tracker.
- Weekly review input: Aggregate registrations show restart speed; feed into systems-audit.
- DOV sync: The external memory (trackers in the synced vault) survives device changes because GitHub keeps the source (Library) and project structure current.

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)


## snf-hope-activation
```
---
type: skill
name: snf-hope-activation
aliases: [hope, hope-activation, /hope, snf-hope]
description: >
  Engineer one tiny visible win + external proof when hope feels broken ("what's the point"). Hope is a prediction system damaged by depression; this skill generates counter-evidence that effort can still shape the substrate. Scale to current energy; always bottom-line first.
domain: [philosophy-snf, recovery, execution]
energy: low
invocation: ["/hope", "hope is low", "activate hope", "generate proof of agency"]
compatible_with: [grok, claude, gpt, local, all]
version: 1
last_reviewed: 2026-06-12
tags: [philosophy-snf, recovery, hope-activation, proof-based-hope, state-not-fate, visible-proof, low-energy, reading-error]
---
```

# SNF Hope Activation

## Purpose
Hope is not a feeling or slogan. It is a working prediction in the brain: "If I do this small thing, something might improve." Depression damages this prediction system. The corrective is not cheerleading; it is engineered, visible, low-stakes evidence that effort can still change the substrate. This is the "Hope and Activation Start" layer of State Not Fate.

## When to Use
- When the user reports low hope, "what's the point", or resistance to even small plans.
- After a lapse when the brain is treating the whole system as fake.
- In the opening of any planning or daily execution conversation when energy/hope is fragile.
- When scaling plans: very low hope → survival anchors + one visible win only.
- During intake or personalization to assess hope signal strength.

## Core Instructions
1. Acknowledge the damaged prediction without fake positivity: "Your brain currently predicts that effort won't change anything. We're going to generate one tiny piece of counter-evidence."
2. Anchor to the user's actual constraints and recent status (no over-ambition).
3. Generate one (or very few) action small enough to survive resistance + one result visible enough to register as evidence.
4. Explicitly link the action to "proof that effort can still shape tomorrow" or "interrupting the reading error."
5. Record the evidence externally so it survives the next low day.
6. Scale: survival anchors + visible win (very low hope); core anchors + practical block (low-moderate); etc.

Never promise mood change. Promise only "one result visible enough to count as evidence."

## Output Format (Bottom Line First)
- **Bottom Line**: "Current hope prediction is damaged. One small action + one visible result to generate counter-evidence."
- **Damaged Prediction Check**: User's current "what's the point" statements or low-hope markers.
- **Survival / Core Anchors**: The absolute minimum that must still happen (cross-ref mvd-anchors).
- **One Visible Win**: The smallest action that can produce observable change today (e.g., "room 10% less hostile", "tracker shows one floor win instead of zero").
- **Evidence Language**: Exact phrasing to log or say: "This is proof that effort can still shape the substrate."
- **Risk / Reading Error**: How this interrupts "bad day = total failure."
- **Next Evidence Opportunity**: What could produce more proof tomorrow if this lands.

## Context to Inject
- Current energy, status block, and recent lapses or "reading errors."
- Existing anchors or MVD.
- SNF principles: depression as systems failure, hope as prediction not feeling, visible proof, external memory, state-based scaling.
- Any prior proof or tracker data that shows "a rough week no longer erases everything."

## Related Skills & Prompts
- mvd-anchors and floor-wins / snf-proof-registration — anchors generate the raw material; proof-registration makes it visible and logged.
- low-energy-execution — the operational container for hope-activation on bad days.
- thoroughness-protocol — use to keep the "one visible win" truly small and believable.
- weekly-review and library-gardener — track whether hope-activation is actually repairing the prediction over time (via resilience and hope metrics).
- council-strategy — use the hope/activation expert lane when low hope is blocking big decisions.

## Notes & History
- Core from SNF canonicals: "hope is the brain's prediction that effort can still change something", "one action small enough to survive resistance and one result visible enough to count as evidence", "early success is defined by continuity and proof, not dramatic mood transformation", "written proof that a bad day no longer erases the week".
- Explicitly rejects fake optimism: "hopeful without sounding fake."
- Update when your personal proof examples or logging methods evolve.
- This skill is the bridge between the floor (MVD) and any later expansion or ambition.

**Scientific Basis (substrate reminders)**
Hope here is explicitly Snyder's (2002) "hope theory" — agency ("I can") + pathways ("I know how") — damaged in depression but repairable via small counter-evidence:
- Prediction updating: The brain constantly runs forward models; visible small results create positive prediction errors that gradually restore agency (Schultz dopamine work; human fMRI studies on goal progress and striatal response).
- Implementation intentions: Gollwitzer & Sheeran (2006) meta-analysis — "if-then" planning (one action + one visible result) roughly doubles the likelihood of follow-through.
- Neuroplasticity of reward: Repeated small successes increase BDNF and can reverse some hypofrontality seen in depression (Doidge, *The Brain That Changes Itself*; exercise + behavioral activation studies).
- External memory as extended mind: Clark & Chalmers (1998) "The Extended Mind" + modern offloading research shows that writing proof outside the brain literally changes what the biological substrate has to compute.
- Additional: Self-efficacy mastery (Bandura 1997); behavioral activation outcomes (Dimidjian et al.); habit formation supporting long-term agency (Wood & Neal).

**Enhanced Practical Ties to Your 2026 Project & DOV**
- Low-hope morning in project: "One small action + one visible result" using the project's Proof-Log as the external memory.
- Job search resistance: Generate the visible win in the job_search_tracker (synced via DOV/GitHub).
- Post-lapse: Use the "survival anchors + visible win" scale and register in both project log and main status.
- Weekly systems-audit input: Track whether the "one visible win" is actually repairing the prediction (resilience-rate, hope metrics).

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)


## sobriety-anchors
```
---
type: skill
name: sobriety-anchors
aliases: [sobriety, sober-anchors, daily-sobriety, /sobriety]
description: >
  Define and protect a small set of daily and situational sobriety anchors (counter-script contact, trigger awareness, proof of commitment, connection to the date 2019-11-01 and reasons why) that reinforce recovery as the non-negotiable foundation underneath every other system. Use on any day, especially low-energy or high-trigger ones.
domain: [sobriety, recovery, philosophy-snf]
energy: any
invocation: ["/sobriety", "sobriety anchors", "check my sober floor", "recovery check"]
compatible_with: [grok, claude, gpt, local, all]
version: 1
last_reviewed: 2026-06-12
tags: [sobriety, recovery, anchors, state-not-fate, prs, no-shame, floor, proof]
---
```

# Sobriety Anchors

## Purpose
Sobriety (since 2019-11-01) is the load-bearing foundation for everything else: energy management, job reliability, self-trust, 5-year vision. This skill turns the abstract "I'm sober" into a tiny, repeatable, proof-generating set of anchors and counter-practices that survive low energy, bad nights, or cravings. It prevents the "one bad day erases everything" reading error.

## When to Use
- Every morning as part of MVD or status update.
- On days with known triggers (stress, social, money pressure, loneliness).
- After any emotional spike, bad sleep, or near-miss craving.
- In weekly-review or systems-audit to confirm the sobriety system is green.
- Before high-stakes social or career interactions (use with prs-safety-check and social-calibration).
- Anytime the voice says "what's the point of all this recovery work."

## Core Instructions
1. Acknowledge the date and the fact of sobriety as external proof already achieved (not a feeling to maintain).
2. Define or reaffirm the personal non-negotiable anchors for today (e.g., speak one line of counter-script aloud, review one reason-why, log one sobriety proof, reach one safe contact if needed, avoid high-risk environments).
3. Check for today's specific triggers or vulnerabilities (energy collapse, runway stress, social calendar) and pre-plan micro-responses.
4. Make anchors so small they are biologically and identity-possible even in collapse (under 2 minutes each).
5. End with explicit registration of the anchor as visible proof (tracker, status block, note) that feeds hope and restart speed.
6. Give permission: missing a secondary anchor does not threaten the primary sobriety system.

## Output Format (Bottom Line First)
- **Bottom Line**: "Sobriety floor protected today with X anchors. Everything else is optional."
- **Core Sobriety Anchors** (2-4 tiny items, personalized):
  - Counter-script contact (specific line or memory of the date/reasons).
  - Trigger scan + pre-response.
  - One micro-proof action (log, message, physical marker).
  - Connection or safe person touch (if energy allows).
- **Today's Specific Risks**: Known triggers and the exact smallest response.
- **What Can Be Dropped**: Non-essential activities without self-attack.
- **Proof Registration**: Where and how this anchor is logged today so the future low-hope brain can see it.
- **If Craving or Spike Hits**: Exact next tiny action + who to contact (988 or personal safe list).

## Context to Inject
- Master bio recovery section (sober since 2019-11-01, treating depression as temporary systems state)
- Current energy and status block
- Recent triggers or near-misses from trackers/notes
- Personal reasons-to-live / counter-script (if documented)
- PRS lens from prs-safety-check (self as "client")

## Related Skills & Prompts
- mvd-anchors and low-energy-execution (sobriety anchors are often the first biological/identity layer of the MVD)
- prs-safety-check (run this before or with sobriety anchors on high-risk mornings)
- floor-wins and snf-proof-registration (register sobriety anchors as floor wins / visible proof)
- snf-hope-activation (sobriety continuity is one of the strongest sources of "effort still shapes the substrate")
- systems-audit (sobriety is a primary system)
- social-calibration (for safe contact or boundary setting around triggers)
- Original State Not Fate recovery materials and PRS training

## Notes & History
- Recovery is not a side project; it is the substrate on which job, energy, social, and 5-year vision are built. Protecting it with tiny daily anchors is the highest-leverage thing you do.
- Language must stay non-heroic and proof-oriented: "I made contact with the fact of my sobriety today" beats motivational slogans.
- Update whenever personal triggers evolve, safe contacts change, or you discover a new counter-script line that actually lands on bad days.
- Added and reinforced during the full Library expansion to make sobriety explicit and first-class alongside other anchors and systems.

**Scientific Basis (substrate reminders)**
- Habit formation & automaticity: Wood & Neal (2007, *Psychological Review*) — repeated cue-response anchors (e.g., "upon waking, speak the date 2019-11-01") build automatic sobriety behaviors that require less willpower on low-energy days.
- Neurobiology of sustained recovery: Volkow et al. (various NIH reviews on addiction recovery) — small consistent actions support normalization of dopamine systems and prefrontal control, reducing craving intensity over months/years.
- Self-efficacy through mastery: Bandura (1997) — logging visible sobriety anchors creates "mastery experiences" that build confidence in the ability to handle high-stakes situations (PRS work, trades apprenticeships).
- Relapse prevention & high-risk situations: Marlatt & Donovan (2005, *Relapse Prevention*) — pre-planned micro-anchors for known triggers (money stress, loneliness, social events) interrupt the chain before a lapse escalates.

**Practical Examples from Your Life (PRS + trades path)**
- High-trigger day (money runway pressure): Counter-script "Sober since 2019-11-01 — this is temporary systems state" + log one micro-proof in status block. Ties to financial-stability skill.
- Before PRS-related social or interview: Quick anchor review of reasons + one safe contact text. Use with social-calibration and prs-safety-check.
- Post-lapse or low-energy collapse: "I made contact with the date today" as the floor win. Register in Proof-Log to feed snf-hope-activation and restart speed.
- 5-year vision alignment: Weekly sobriety proof aggregate in systems-audit shows the foundation enabling career parallel tracks.

**DOV Integration Note**
Since the DOV (OneDrive/Desktop/ObsidianVault) is your device-synced vault across machines, keep these anchors as part of your daily ritual there too. The Library (pushed to GitHub) provides the source; emit packs in DOV and log proofs so they survive device switches. Pull updates regularly so the scientific language and project ties stay current.

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)


## circadian-anchors
```
---
type: skill
name: circadian-anchors
aliases: [circadian, light, rhythm, sleep-anchors, /circadian]
description: >
  Establish and protect a minimal set of circadian and biological rhythm anchors (light exposure timing, wake/sleep window, meal/movement cues) that regulate energy availability, mood prediction, and floor stability. Treat as non-negotiable MVD layer especially on variable or low-energy days.
domain: [health, recovery, execution]
energy: low
invocation: ["/circadian", "light anchor", "fix my rhythm", "energy biology today"]
compatible_with: [grok, claude, gpt, local, all]
version: 1
last_reviewed: 2026-06-12
tags: [health, circadian, light-exposure, anchors, low-energy, mvd, recovery, rhythm]
---
```

# Circadian Anchors

## Purpose
Energy, motivation, and emotional regulation are heavily downstream of basic biological rhythms (light, sleep timing, food, movement). On days when motivation is gone, these anchors are the external levers that still work. They form the physical floor under all State Not Fate work and directly support restart speed and hope as a prediction.

## When to Use
- Every morning (or night before) as part of setting the MVD.
- On collapse or very low energy days when "normal" plans are impossible.
- After disrupted sleep, travel, or major schedule breaks.
- When reviewing energy patterns in weekly-review or systems-audit.
- Before high-demand days (interviews, social, big job pushes) to pre-load the biology.

## Core Instructions
1. Start with current reality: last sleep window, current light exposure, time of day, any known disruptions (meds timing, stress, previous late night).
2. Define the 2-4 smallest circadian anchors possible today (examples: get outside or to bright window within 30-60 min of waking for 5+ min; consistent wake time window even if sleep was bad; protein + water soon after waking; short movement or posture reset).
3. Make each anchor tiny and nearly failure-proof on collapse (under 5 minutes, no equipment or motivation required).
4. Link explicitly to downstream effects (better light → better sleep prediction tonight → more floor tomorrow).
5. Register the anchors as floor wins / proof (status block, tracker, note) so the system compounds.
6. Give explicit permission to drop everything else while protecting these.

## Output Format (Bottom Line First)
- **Bottom Line**: "Circadian floor set with X anchors. This is the biological substrate for anything else today."
- **Light & Wake Anchors** (timing + exact micro-action):
  - Morning light exposure window and duration.
  - Wake time tolerance.
- **Fuel & Movement Anchors** (minimal):
  - Water/meds/protein cue.
  - 2-5 min movement or posture.
- **Evening Wind-Down** (if relevant): Light reduction, consistent bedtime range.
- **What Can Be Dropped**: All ambitious exercise, perfect meals, etc.
- **Proof & Tracking**: How this is logged and how it will feed tonight's sleep prediction or tomorrow's MVD.
- **Risks**: Known disruptors today and the smallest mitigation.

## Context to Inject
- Current energy report and status block
- Last 24-48h sleep/energy notes
- Meds timing and any recent disruptions
- MVD from mvd-anchors (circadian is often the first biological layer)
- Any known upcoming demands (job search session, appointment)

## Related Skills & Prompts
- mvd-anchors and low-energy-execution (circadian anchors are core biological non-negotiables inside the MVD)
- floor-wins (register light exposure or wake consistency as proof)
- systems-audit (circadian/health is a primary system)
- sobriety-anchors (often performed in the same morning window)
- prs-safety-check (biological floor check includes light/sleep debt)
- weekly-review (track whether circadian consistency is moving energy baseline)

## Notes & History
- Directly addresses the "variable energy / brain fog / low motivation days (collapse is real)" constraint in master-bio.
- State Not Fate principle: you cannot will your way out of a broken rhythm, but you can still put light on your face and water in your body. That is enough to start the prediction repair.
- Update whenever living situation, meds, or season changes the practical levers (new apartment light access, shift work considerations, etc.).
- Created during the reinforce-and-expand pass to make the health/energy biology layer first-class and explicitly linked to the rest of the Library.

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)


## tool-mode-decider
```
---
type: skill
name: tool-mode-decider
aliases: [tool-mode, which-tool, /toolmode, decide-tool]
description: >
  Given a task, decide the best AI/tool/setup to use (Grok CLI, ChatGPT Project, NotebookLM, local model, Obsidian + emit, etc.) and the right context/skill pack to load.
  Use when you have work to do and want to avoid context pollution or using the wrong hammer.
domain: [meta, execution, ai-setup]
energy: low
invocation: ["/toolmode", "what tool for this", "best way to do this task"]
compatible_with: [grok, claude, gpt, local]
version: 1
last_reviewed: 2026-06-12
tags: [meta, tools, ai-setup]
---
```

# Tool Mode Decider

## Purpose
Stop wasting cognitive energy and tokens by defaulting to "just paste everything into ChatGPT." Match the task to the right environment, context size, and skill injection method.

## When to Use
- Before starting any non-trivial piece of work (research, planning, writing, coding, job materials).
- When you feel decision fatigue about "where do I even do this?"

## Core Instructions
1. Clarify the exact task + constraints (energy today, need for persistence, privacy, speed, depth, collaboration).
2. Map to the best primary tool:
   - **This Grok CLI** (with synced skills): coding, rigorous execution, file system work, best-of-n, deep refactors, anything needing the full .grok toolset.
   - **ChatGPT Project or Claude Project**: long-term coaching, large context memory, the AI Life Coach Friend bundle.
   - **NotebookLM**: synthesis of many documents, "podcast" style overviews, studying your own materials.
   - **Obsidian + emit tools**: pure thinking, linking ideas, creating new atomic skills, daily notes, when you want to stay in your own knowledge graph.
   - **Local models**: privacy-sensitive or high-volume low-stakes tasks.
   - **PWA / custom tools** (State Not Fate app): daily anchors, PHQ-9, media consumption, floor tracking.
3. Decide what context/skill pack to load:
   - Master bio + current status block (almost always).
   - Specific skills (e.g. daily-job-search + low-energy-execution).
   - Full bundles only when the task justifies the context cost.
4. Output the exact "setup command": which tool + which files/skills to load + opening prompt.

## Output Format (Bottom Line First)
- **Bottom Line**: Recommended primary tool + why.
- **Context to Load**:
  - Required: master bio + status.
  - Skills/Prompts: list with brief why.
  - Bundles (if any).
- **Opening Prompt**: Suggested first message / system instruction.
- **Alternatives**: Second-best option and when you might switch.
- **Why Not the Others**: Brief anti-recommendations.

## Context to Inject
- The task description
- Current energy + any hard constraints (time, tokens, privacy)
- Recent status

## Related
- ai-setup-audit (the bigger periodic full ecosystem reinforcement audit skill)
- All the skills (this one decides which to load)
- The original "08_Tool_Mode_Decider.md"

## Notes & History
- This is a meta-skill that protects your attention and the quality of every other skill.
- Update as your tool landscape changes (new local models, new Obsidian plugins, new Grok features, etc.).

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)
