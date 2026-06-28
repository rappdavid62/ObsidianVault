Note: mvd-anchors has dictionary compliance issues (run with --validate mvd-anchors for details).
Note: floor-wins has dictionary compliance issues (run with --validate floor-wins for details).
# Emitted from Obsidian Skill & Prompt Library
# Source of truth: 09-PROMPTS/Library (Obsidian)
# Usage: Prefix with /tp or /council when appropriate.

## Master Context (inject this in most conversations)
```markdown
---
type: context
name: master-bio
aliases: [david-bio, core-context, who-i-am]
description: >
  Core persistent facts about you: bio, constraints, job targets, work history, recovery timeline, and key principles. Inject this into most serious conversations.
domain: [context, meta]
energy: any
invocation: ["use my master bio", "who I am context"]
compatible_with: [grok, claude, gpt, local]
version: 1
last_reviewed: 2026-06-08
tags: [context, bio, constraints]
---
# Master Bio & Context

**Name / Location**: David, Cincinnati area.

**Recovery**: Sober since 2019-11-01. Treating depression as a temporary multi-system state (not identity). Using State Not Fate principles: anchors, proof, low-friction moves, MVD floor, restart speed over streaks, energy-adaptive planning.

**Job Targets** (priority order):
1. Peer Recovery Supporter (PRS) roles ΓÇö leveraging APS.006470 certification (40hr training).
2. HVAC helper / apprentice.
3. Alarm / security / low-voltage / field tech.
4. Maintenance / facilities.
5. Warehouse / logistics.
6. Driver roles.

**Relevant Experience**:
- Eleeo / D2C: customer service, reliability, de-escalation.
- Clark And Sons: moving, packing, physical work, logistics.
- Strong on following procedures, showing up, learning trades.

**Constraints** (always factor these in):
- Variable energy / brain fog / low motivation days (collapse is real).
- Financial runway pressure (need income stability soon).
- Location: Cincinnati area, transportation considerations.
- Building 5-year vision while stabilizing floor (job + routines + money + social).

**Core Principles** (from State Not Fate):
- State Γëá Fate.
- Action before motivation; tiny anchors create proof.
- Ideal Move vs Realistic Move (scale to today's energy).
- Bottom Line first. Exact Next Action. Risks called out.
- External memory (status blocks, trackers, Obsidian) over relying on brain.
- No shame on floor days. Floor wins count.

**Daily Ritual Context**:
- Update status block (energy, runway, one non-negotiable, job search activity).
- Use low-energy plans when needed.
- Job search volume + quality, not perfection.

Use this as the persistent "who I am and what matters" layer in any coaching, planning, or decision conversation.
```

## Skill / Protocol: snf-hope-activation
**Description:** >
**Meta:** Energy: low | Domain: [philosophy-snf, recovery, execution, sobriety]

```markdown
---
type: skill
name: snf-hope-activation
aliases: [hope-activation, hope-prediction, effort-reconnection, agency-repair, activate-hope]
description: >
  Treat hope as the brain's damaged prediction that effort can still lead to improvement. Deliberately generate one small, believable, visible piece of counter-evidence to repair that prediction ΓÇö without fake optimism, cheerleading, or promises of mood change. "One action small enough to survive resistance + one result visible enough to count as evidence."
  Primary use: low hope / "what's the point" / post-lapse restart / fragile energy states. Core layer of State Not Fate (SNF) "Hope and Activation Start".
domain: [philosophy-snf, recovery, execution, sobriety]
energy: low
invocation: ["/hope", "activate hope", "repair the prediction", "effort can still matter", "one visible win"]
compatible_with: [grok, claude, gpt, local]
version: 2
last_reviewed: 2026-06-13
tags: [state-not-fate, philosophy-snf, recovery, hope, hope-activation, effort-reconnection, visible-proof, reading-error, low-energy, no-shame, anchors, proof-based-hope, prediction-error, external-memory, substrate, restart-speed]
---

# SNF Hope Activation

**Source:** DOV Obsidian Library (C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library)
**Last synced / enhanced:** 2026-06-13

## Purpose
Hope is not a feeling or slogan. It is a working prediction in the brain: "If I do this small thing, something might improve." Depression (as multi-system state, not fate) damages this prediction system. The corrective is not cheerleading; it is **engineered, visible, low-stakes evidence** that effort can still change the substrate. This is the "Hope and Activation Start" layer of State Not Fate. It bridges the floor (MVD) to any later expansion.

Never promise mood change. Promise only "one result visible enough to count as evidence" that updates the forward model.

## When to Use
- User reports low hope, "what's the point", resistance to plans, or "the system feels fake".
- Immediately after a lapse, bad night, or emotional spike when the brain treats the whole recovery/project as broken.
- Opening of any planning, daily execution, or job-search conversation when energy/hope is fragile.
- Scaling plans: very low hope ΓåÆ survival anchors + **one** visible win only.
- During intake/personalization or 5-year vision work to assess hope signal strength.
- Any morning in the 2026 SNF Substrate Systems Project when the job_search_tracker or Proof-Log feels empty.

## Core Instructions
1. Acknowledge the damaged prediction without fake positivity: "Your brain currently predicts that effort won't change anything. We're going to generate one tiny piece of counter-evidence today."
2. Anchor ruthlessly to the user's actual constraints, current energy/status block, and recent lapses or "reading errors" (no over-ambition).
3. Generate **one (or at most two)** action small enough to survive resistance + one result visible enough to register as external evidence (e.g. tracker cell filled, Proof-Log entry, 10% less hostile room, one lead saved).
4. Explicitly link: "This is proof that effort can still shape tomorrow" or "interrupting the reading error that bad day = total system failure."
5. Force external registration (Proof-Log.md, job_search_tracker, status block, or physical marker) so it survives the next low day / memory distortion.
6. Scale by energy/hope:
   - Very low / collapse: survival anchors (from mvd-anchors or sobriety-anchors) + one visible win only.
   - Low-moderate: core anchors + one practical block that produces observable change.
   - After success: note the evidence and offer "next evidence opportunity" for tomorrow.

## Output Format (Bottom Line First)
- **Bottom Line**: "Current hope prediction is damaged. One small action + one visible result to generate counter-evidence. This shows effort can still shape the substrate."
- **Damaged Prediction Check**: Exact "what's the point" statements, recent lapse language, or low-hope markers from user/status.
- **Survival / Core Anchors** (cross-ref mvd-anchors, sobriety-anchors): The absolute minimum biological/identity floor that must still happen today.
- **One Visible Win**: The smallest action + the exact observable/recorded result (e.g. "Saved 1 lead in job_search_tracker ΓÇö now 3 in pipeline this week instead of zero").
- **Evidence Language** (exact for log/speech): "This is proof that effort can still shape the substrate." or "A rough day no longer erases the week."
- **Risk / Reading Error Interrupted**: How this specific win breaks "bad day = total failure" or "lapse = back to zero".
- **Next Evidence Opportunity**: What tiny action could produce more proof tomorrow if this one lands (keeps the prediction system online).

## Context to Inject
- Current energy, status block, recent lapses/"reading errors", and any visible proof already logged this week.
- Existing MVD anchors, sobriety anchors, or floor wins (cross-ref mvd-anchors, floor-wins, sobriety-anchors).
- SNF principles from core philosophy: depression as temporary multi-system state (not identity/fate), hope as prediction (Snyder agency + pathways), visible proof + external memory as the repair mechanism, state-based scaling, restart speed over streak purity, "State, not fate."
- 2026 Project specifics: job_search_tracker.md entries, Proof-Log.md in the SNF project folder, financial runway pressure, PRS + trades parallel tracks, Cincinnati 5-year vision (stable function ΓåÆ partnership/family).
- Prior proof data showing "a rough week no longer erases everything" (weekly-review aggregates, library-gardener metrics).
- Master bio recovery section (sober since 2019-11-01 as load-bearing proof already achieved).

## Related Skills & Prompts
- mvd-anchors and floor-wins / snf-proof-registration ΓÇö anchors generate the raw material; proof-registration makes it visible/logged and feeds the hope meter.
- sobriety-anchors ΓÇö the foundational identity/biological layer; sobriety continuity is one of the strongest existing sources of "effort still shapes the substrate."
- low-energy-execution ΓÇö the primary operational container that holds hope-activation on collapse days.
- thoroughness-protocol ΓÇö use lightly to keep the "one visible win" truly small, believable, and shame-free.
- weekly-review and library-gardener ΓÇö audit whether repeated hope-activation is actually repairing the prediction (resilience-rate, hope metrics, restart speed).
- systems-audit and substrate-reminders ΓÇö treat hope repair as one measurable substrate system among others (energy, recovery, career, finance).
- council-strategy ΓÇö route low-hope blocks through the hope/activation expert lane during high-stakes decisions (job offers, moves, 5-year vision pivots).
- prs-safety-check ΓÇö combine on high-risk mornings before social or PRS-related work.

## Notes & History
- Core SNF canonicals (from 01_canonical_project_system, 04_Hope_and_Activation_Start, 01_snf_core_philosophy, ANTI-GRAVITY, etc.): "hope is the brain's prediction that effort can still change something", "one action small enough to survive resistance and one result visible enough to count as evidence", "early success is defined by continuity and proof, not dramatic mood transformation", "written proof that a bad day no longer erases the week", "State, not fate."
- Explicitly rejects fake optimism and motivational language: "hopeful without sounding fake." Tone must be blunt, respectful of low functioning, evidence-only.
- 2026-06-13 enhancement: Full scientific basis + concrete 2026 SNF project + DOV/GitHub sync + job_search_tracker + Proof-Log integration + sobriety as co-anchor + richer ubiquitous frontmatter. Aligned to 09 Library standards + Dictionary (philosophy-snf domain).
- This skill is the critical bridge between the floor (MVD + sobriety) and any later ambition/expansion in the 5-year vision.

## Scientific Basis (substrate reminders)
Hope here is explicitly Snyder's (2002) "hope theory" ΓÇö agency ("I can") + pathways ("I know how") ΓÇö damaged in depression but repairable via small counter-evidence:
- Prediction updating & reward prediction error: The brain constantly runs forward models; visible small results create positive prediction errors that gradually restore striatal dopamine signaling and agency (Schultz dopamine work; human fMRI goal-progress studies; reviews on anhedonia in *Nature Reviews Neuroscience*).
- Implementation intentions: Gollwitzer & Sheeran (2006) meta-analysis ΓÇö "if-then" planning (one action + one visible result) roughly doubles follow-through likelihood even under low motivation.
- Neuroplasticity of reward & self-efficacy: Repeated small successes increase BDNF, can reverse hypofrontality; most powerful efficacy source is "performance accomplishments" made salient (Bandura 1997; Doidge *The Brain That Changes Itself*; behavioral activation meta-analyses).
- External memory as extended mind: Clark & Chalmers (1998) + modern offloading research ΓÇö writing proof outside the brain literally changes what the biological substrate has to compute on the next low day (Risko & Gilbert 2016 *Trends in Cognitive Sciences*).
- Additional: Behavioral activation outcomes (Dimidjian et al. COBRA trial: non-inferior to CBT, scalable); habit formation supporting long-term agency (Wood & Neal); learned helplessness counter (Abramson et al. 1978 attributional style).

Use the exact phrasing "This shows effort can still shape the substrate" as a deliberate counter-script to depressive attributional style.

## Enhanced Practical Ties to Your 2026 SNF Substrate Systems Project, DOV, Trackers & 5-Year Vision
- Low-hope morning in project: Emit this skill + current status + job_search_tracker snippet. Generate "save one lead or update one cell" as the visible win; immediately register in Proof-Log.md with the exact phrase.
- Job search resistance / runway stress: One visible win = "1 new lead saved + note in tracker" (feeds financial-stability and career-strategy). Register proof so the pipeline itself becomes hope data.
- Post-lapse or collapse day: survival anchors (MVD + sobriety date contact) + one visible win only. Log in both project Proof-Log and main status. "I restart without punishment."
- Weekly systems-audit / library-gardener input: Feed the "one visible win" count and quality into resilience-rate, hope-meter, and restart-speed metrics. Track whether the prediction is measurably repairing over 30/90 days.
- DOV / GitHub / OneDrive sync: The external memory (trackers + Proof-Log in the synced vault + Library source) survives device changes and low-energy brain. GitHub keeps the canonical; emit packs for Claude/Gemini/Grok on any machine. Pull updates regularly.
- 5-year vision alignment (Cincinnati stable function ΓåÆ partnership/family): Every registered proof is literal building material for the "stable platform" layer. Low-hope days are data, not verdict. Use with 5-year-vision-alignment and career-strategy when the long view feels unreachable.
- PRS / trades parallel tracks: Before high-stakes social or interview, quick hope-activation + one micro-proof (text to safe contact or one lead) to keep agency online. Pair with prs-safety-check and social-calibration.

(This is the canonical version in the DOV 09-PROMPTS/Library ΓÇö the universal truth for all AI. All prompts consolidated here. Prefer editing source in vault and re-syncing/emitting to .grok and other models.)

---
This skill was generated from the canonical Obsidian note in the DOV vault (the universal truth) and enhanced 2026-06-13 with full scientific basis, 2026 project integration, and Dictionary-aligned frontmatter.
```

## Skill / Protocol: snf-proof-registration
**Description:** >
**Meta:** Energy: low | Domain: [philosophy-snf, recovery, execution, sobriety]

```markdown
---
type: skill
name: snf-proof-registration
aliases: [visible-proof, external-memory, proof-registration, floor-win-log, register-proof]
description: >
  Deliberately record small, visible evidence that effort can still produce change, even on bad days or after lapses. Interrupts the "reading error" where the depressed brain treats any miss as proof the whole system (recovery, project, self-trust) is fake.
  Use immediately after any anchor/MVD/micro-action, at end of low days, and during weekly aggregation. Foundational external-memory mechanism of State Not Fate.
domain: [philosophy-snf, recovery, execution, sobriety]
energy: low
invocation: ["/proof", "register this win", "log visible proof", "external memory", "this shows effort"]
compatible_with: [grok, claude, gpt, local]
version: 2
last_reviewed: 2026-06-13
tags: [state-not-fate, philosophy-snf, recovery, visible-proof, external-memory, proof, floor-win, restart-speed, resilience-rate, hope-meter, low-energy, no-shame, mvd, anchors, prediction-error, cognitive-offloading, substrate]
---

# SNF Proof Registration

**Source:** DOV Obsidian Library (C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library)
**Last synced / enhanced:** 2026-06-13

## Purpose
Depression damages the brain's ability to register that small actions still matter. "Visible proof" and "external memory" are the corrective mechanisms: you write it down (in tracker, Proof-Log, status block) so the future self or the low-hope brain on the next bad day can see the evidence that effort can still shape tomorrow. This directly supports **restart speed** (how fast you recover from a lapse without self-attack) and the **hope meter** (accumulated proof that action ΓåÆ observable results). It is literal data that survives the damaged reward prediction system.

Never let a day with any action go unregistered on low-energy or post-lapse days.

## When to Use
- Immediately after any anchor, MVD, sobriety anchor, or micro-action completion ΓÇö no matter how small.
- At the end of a low/collapse day when you still managed one floor win (or even just "I made contact with the date today").
- After a lapse or "bad day" to prevent the whole week from being erased in memory/identity.
- When updating job_search_tracker, Proof-Log.md, status blocks, or any persistent record.
- During weekly-review, library-gardener, or systems-audit passes to aggregate proof and compute resilience metrics.
- Before high-stakes social/PRS work or when the "what's the point" voice is loud.

## Core Instructions
1. Start with the user's report of what actually happened (even if "only" one thing or "I just survived the day").
2. Translate the action into "visible proof" language: what changed in the external world or record *because of* the effort (tracker row filled, lead saved, Proof-Log entry, 10% less hostile environment, text sent, med taken on time).
3. Record it in a persistent, reviewable, cross-device place (Proof-Log.md in the SNF project, job_search_tracker.md, main status block, or physical marker) so it survives memory distortion and device switches.
4. Explicitly counter the "reading error": "A rough day/week does not prove the plan is fake." "I restart without punishment."
5. Link it to restart speed, hope, or substrate impact if relevant: "This is evidence I can still return / the pipeline is still alive / self-trust is intact."

## Output Format (Bottom Line First)
- **Bottom Line**: "Visible proof registered: [specific evidence]. This shows effort can still shape the substrate."
- **Action Performed**: The tiny thing done (timestamped if possible, energy level noted).
- **Visible Change / Record**: What is now different or written down because of it (exact tracker cell, log line, or observable state change).
- **Counter to Reading Error**: How this interrupts "bad day = total failure" or "lapse = back to zero / system fake."
- **Link to Metrics**: How it feeds resilience-rate (restart), hope-meter (evidence of agency), or other substrates (energy, career pipeline, financial runway, sobriety continuity).
- **Next Proof Opportunity** (optional): What small action could generate more evidence tomorrow (keeps momentum without pressure).

## Context to Inject
- Current energy and any recent lapse, weak period, or "reading error" language.
- The specific anchor or MVD that was completed (cross-ref mvd-anchors, floor-wins, sobriety-anchors).
- Recent status, job_search_tracker entries, or Proof-Log data.
- SNF principles from core philosophy: depression as temporary multi-system state (not identity or fate), external memory over internal judgment, restart speed over streak purity, "State, not fate."
- 2026 Project trackers and 5-year vision constraints (PRS cert, trades path, Cincinnati vision, runway).

## Related Skills & Prompts
- mvd-anchors and floor-wins ΓÇö the actions that generate the proof; this skill is the registration layer that makes them survive and compound.
- sobriety-anchors ΓÇö sobriety proofs (contact with the date, counter-script, safe person touch) are some of the highest-leverage visible evidence; register them explicitly.
- snf-hope-activation ΓÇö proof is one of the main inputs that repairs the damaged hope prediction. Always pair on low-hope days.
- low-energy-execution ΓÇö primary context where proof registration is most needed and most powerful (turns "I only did the floor" into data).
- weekly-review and library-gardener ΓÇö aggregate registrations ΓåÆ resilience-rate, hope metrics, systems health. Input to 5-year-vision-alignment.
- thoroughness-protocol ΓÇö use lightly so you don't over-explain or perfection the proof; one line of "what changed" is enough.
- systems-audit and substrate-reminders ΓÇö treat proof accumulation as measurable work on the recovery/career/energy substrates.
- daily-job-search / apply-today ΓÇö every lead saved or application is a proof candidate; register it.

## Notes & History
- Core State Not Fate mechanism from canonicals (01_canonical_project_system, 01_snf_core_philosophy, ANTI-GRAVITY, Hope and Activation Start, etc.): "written proof that a bad day no longer erases the week", "visible proof that tomorrow can still be shaped", "external memory", "the project should be measured by restart speed, not streak purity."
- "Proof" here is not motivational fluff; it is literal externalized data that survives the damaged reward prediction system and the hostile interpretive bias of the state.
- 2026-06-13 enhancement: Full scientific basis + concrete integration with 2026 SNF project (job_search_tracker, Proof-Log.md), DOV/GitHub sync for ubiquity, sobriety-anchors as co-equal generator, Dictionary-aligned frontmatter + tags, expanded personal examples.
- Update this note whenever your logging/tracking method changes (new column in job_search_tracker, new Proof-Log format, status block evolution).
- This skill is foundational for long-term restartability, self-trust rebuild, and the 5-year vision of stable function.

## Scientific Basis (substrate reminders)
The "substrate" that proof registration targets is the brain's reward prediction, memory, and self-efficacy systems, which depression blunts.
- Cognitive offloading: Writing things down reduces working memory load and improves follow-through (Risko & Gilbert, 2016, *Trends in Cognitive Sciences* ΓÇö "Cognitive offloading").
- Reward prediction error & dopamine: Small visible successes reliably update striatal dopamine signaling even when mood is low (reviews in *Nature Reviews Neuroscience* on anhedonia and behavioral activation; Schultz work on prediction errors).
- Self-efficacy via mastery experiences: Bandura (1997) ΓÇö the most powerful source of efficacy beliefs is "performance accomplishments" that are made salient and recorded.
- Behavioral activation evidence: Dimidjian et al. (2006) and COBRA trial meta-analyses show structured small-action registration outperforms many other depression treatments on long-term outcomes and is highly scalable.
- Extended mind + habit: Clark & Chalmers (1998); implementation intentions (Gollwitzer & Sheeran 2006); habit formation (Wood & Neal 2007).
- Counter to learned helplessness: Explicit registration + the phrase "This shows effort can still shape the substrate" directly attacks depressive attributional style (Abramson et al., 1978).

## Enhanced Practical Ties to Your 2026 SNF Substrate Systems Project, DOV, Trackers & 5-Year Vision
- Any project action or MVD: Log in the project's Proof-Log.md (or dedicated section) with the exact phrasing + visible change + substrate impact. Example: "2026-06-13 | Saved 1 lead (HVAC helper, Indeed) | Tracker now shows 3 this week vs 0 last | This shows effort can still shape the substrate | Energy: low | Next: tailor resume 5 min."
- Job search day: Register "saved X leads + updated tracker" or "one application submitted" as visible proof. Tie to financial-stability (runway) and career-strategy (PRS + trades balance). The tracker itself becomes hope data.
- Sobriety anchor completion: "Made contact with 2019-11-01 date + spoke counter-script aloud" registered as proof of continuity. Highest-leverage on high-trigger days (money, loneliness, social).
- Post-lapse / low day: Even "I got out of bed and took meds on time" or "one text to safe person" counts. Register to accelerate restart speed and prevent week erasure. "I restart without punishment."
- Weekly-review / systems-audit / library-gardener input: Aggregate proof registrations ΓåÆ quantitative view of resilience-rate (how many lapses followed by quick return with proof) and hope-meter (cumulative visible wins). Feed into 5-year vision alignment (stable platform building).
- DOV / OneDrive / GitHub sync: The external memory (Proof-Log + job_search_tracker + Library in the synced vault) survives device changes, low-energy fog, and travel. GitHub (via any sync) keeps the source canonical for cross-AI use. Emit packs for Claude/Gemini on laptop or phone; fold improvements back into vault.
- 5-year vision (Cincinnati stable function ΓåÆ partnership/family): Every registered proof is literal infrastructure. The "stable platform" layer is built from accumulated visible evidence that the systems (recovery, career, energy, social) are still responsive to effort. Use with 5-year-vision-alignment when the long horizon feels abstract or unreachable.
- PRS work / trades interviews: Before or after, register the micro-action (one prep step, one safe contact text, one boundary held) as proof. Combines with prs-safety-check and social-calibration.

(This is the canonical version in the DOV 09-PROMPTS/Library ΓÇö the universal truth for all AI. All prompts consolidated here. Prefer editing source in vault and re-syncing/emitting to .grok and other models.)

---
This skill was generated from the canonical Obsidian note in the DOV vault (the universal truth) and enhanced 2026-06-13 with full scientific basis, 2026 project + tracker integration, sobriety co-anchor, and Dictionary-aligned frontmatter.
```

## Skill / Protocol: sobriety-anchors
**Description:** >
**Meta:** Energy: low | Domain: [sobriety, philosophy-snf, recovery, execution]

```markdown
---
type: skill
name: sobriety-anchors
aliases: [sobriety, sober-floor, 2019-11-01, recovery-foundation]
description: >
  Turn the fact of sobriety (since 2019-11-01) into a tiny, repeatable, proof-generating set of daily anchors and counter-practices that survive low energy, bad nights, cravings, or emotional spikes. Prevents the "one bad day erases everything" reading error. Load-bearing foundation for all other systems (energy, job reliability, self-trust, 5-year vision).
domain: [sobriety, philosophy-snf, recovery, execution]
energy: low
invocation: ["/sober", "sobriety anchors", "contact the date", "sober floor", "2019-11-01"]
compatible_with: [grok, claude, gpt, local]
version: 2
last_reviewed: 2026-06-13
tags: [sobriety, recovery, philosophy-snf, state-not-fate, anchors, floor, proof, no-shame, restart, triggers, counter-script, prs, mvd, external-memory, 2019-11-01]
---

# Sobriety Anchors

**Source:** DOV Obsidian Library (C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library)
**Last synced / enhanced:** 2026-06-13

## Purpose
Sobriety (since 2019-11-01) is the load-bearing foundation for everything else: energy management, job reliability, self-trust, PRS work, trades path, and the 5-year vision. This skill turns the abstract "I'm sober" into a tiny, repeatable, proof-generating set of anchors and counter-practices that survive low energy, bad nights, or cravings. It prevents the "one bad day erases everything" reading error and keeps the identity fact ("I made contact with the date today") alive as visible external evidence.

Recovery is not a side project; it is the substrate on which job, energy, social, and long-horizon vision are built. Protecting it with tiny daily anchors is the highest-leverage thing you do.

## When to Use
- Every morning as part of MVD/status update or before any planning.
- On days with known triggers (stress, social/PRS work, money/runway pressure, loneliness, poor sleep, emotional spike).
- After any near-miss craving, bad night, or "what's the point of all this recovery work" voice.
- In weekly-review, systems-audit, or library-gardener to confirm the sobriety system is green and generating proof.
- Before high-stakes social, interview, or PRS-related interactions (pair with prs-safety-check and social-calibration).
- Anytime the state tries to make the sober milestone feel abstract or irrelevant.

## Core Instructions
1. Acknowledge the date (2019-11-01) and the fact of sobriety as external proof already achieved (not a feeling to maintain or a streak to protect perfectly).
2. Define or reaffirm the personal non-negotiable anchors for today (2-4 tiny items max, all under 2 minutes even in collapse): speak one line of counter-script aloud, review one reason-why or safe memory, log one sobriety proof (status or Proof-Log), reach one safe contact if needed, avoid one high-risk environment, take meds/water/light as biological floor.
3. Check for today's specific triggers or vulnerabilities (energy collapse, runway stress, social calendar, PRS exposure) and pre-plan the exact micro-response.
4. Make every anchor so small it is biologically and identity-possible even in total fog or low energy.
5. End with explicit registration of the anchor(s) as visible proof (tracker, status block, Proof-Log) that feeds hope, restart speed, and self-trust.
6. Give explicit permission: missing a secondary anchor does not threaten the primary sobriety system. "I restart without punishment."

## Output Format (Bottom Line First)
- **Bottom Line**: "Sobriety floor protected today with X anchors. Everything else is optional. This is proof of continuity."
- **Core Sobriety Anchors** (2-4 tiny, personalized, energy-scaled):
  - Counter-script contact (specific line or memory of the date + reasons, spoken aloud).
  - Trigger scan + pre-planned micro-response for today.
  - One micro-proof action (log in status/Proof-Log, physical marker, text).
  - Connection or safe person touch (if energy allows; otherwise just "I can").
- **Today's Specific Risks**: Known triggers + the exact smallest response (no over-planning).
- **What Can Be Dropped**: Non-essential activities without self-attack or identity evidence.
- **Proof Registration**: Where and how this anchor is logged today (e.g. "2026-06-13 | Contacted 2019-11-01 date + logged in Proof-Log | This shows effort can still shape the substrate").
- **If Craving or Spike Hits**: Exact next tiny action + who to contact (988 or personal safe list). Pre-commit now.

## Context to Inject
- Master bio recovery section (sober since 2019-11-01, treating depression as temporary systems state, PRS credential + trades path as expansion after floor).
- Current energy and status block (especially runway, social calendar, sleep, emotional load).
- Recent triggers or near-misses from trackers/notes or job_search_tracker stress.
- Personal reasons-to-live / counter-script lines (if documented in vault; keep short and believable).
- PRS lens from prs-safety-check (self as "client" ΓÇö professional safety first).
- SNF principles: sobriety as identity fact and substrate, not performance; external proof over internal feeling; restart without punishment.

## Related Skills & Prompts
- mvd-anchors and low-energy-execution ΓÇö sobriety anchors are often the first biological/identity layer of the MVD on any given day; the floor that protects everything else.
- prs-safety-check ΓÇö run this before or with sobriety anchors on high-risk mornings (PRS exposure, social, interviews). Self as client.
- floor-wins and snf-proof-registration ΓÇö register sobriety anchors as floor wins / visible proof. They are some of the highest-value evidence for the hope meter.
- snf-hope-activation ΓÇö sobriety continuity is one of the strongest existing sources of "effort still shapes the substrate." Use hope-activation when the sober milestone itself feels abstract on a bad day.
- systems-audit ΓÇö sobriety is a primary system; green sobriety enables (or blocks) all other substrates (energy, career, social, 5-year vision).
- social-calibration ΓÇö for safe contact scripts or boundary setting around triggers (especially PRS work or money conversations).
- substrate-reminders and circadian-anchors ΓÇö biological supports (light, sleep timing, meds) that make sobriety anchors easier on low-energy days.
- Original State Not Fate recovery materials, PRS training, and master-bio.

## Notes & History
- Recovery is not a side project; it is the substrate on which job, energy, social, and 5-year vision are built. Protecting it with tiny daily anchors is the highest-leverage thing you do.
- Language must stay non-heroic and proof-oriented: "I made contact with the fact of my sobriety today" beats motivational slogans or identity performance.
- 2026-06-13 enhancement: Promoted to full first-class skill in 09 Library with rich frontmatter (Dictionary-aligned: sobriety + philosophy-snf domains), full scientific basis, concrete 2026 project + PRS + job-search integration, DOV sync notes, and tight pairing with snf-hope-activation + snf-proof-registration as the "SNF recovery trio." Added to Hubs/favorites.
- Update whenever personal triggers evolve, safe contacts change, or you discover a new counter-script line that actually lands on bad days.
- Added and reinforced during the full Library expansion (08/09) and 2026 SNF Substrate Systems Project to make sobriety explicit, first-class, and proof-generating alongside other anchors and systems.

## Scientific Basis (substrate reminders)
- Habit formation & automaticity: Wood & Neal (2007, *Psychological Review*) ΓÇö repeated cue-response anchors (e.g. "upon waking, speak the date 2019-11-01") build automatic sobriety behaviors that require less willpower on low-energy or high-craving days.
- Neurobiology of sustained recovery: Volkow et al. (various NIH reviews on addiction recovery) ΓÇö small consistent actions support normalization of dopamine systems and prefrontal control, reducing craving intensity over months/years.
- Self-efficacy through mastery: Bandura (1997) ΓÇö logging visible sobriety anchors creates "mastery experiences" that build confidence in the ability to handle high-stakes situations (PRS work, trades interviews, social reintegration, financial stress).
- Relapse prevention & high-risk situations: Marlatt & Donovan (2005, *Relapse Prevention*) ΓÇö pre-planned micro-anchors for known triggers (money stress, loneliness, PRS exposure, poor sleep) interrupt the chain before a lapse escalates. "If trigger X, then tiny action Y + contact Z."
- External memory + counter to shame: Writing the proof (even "I contacted the date") changes what the substrate has to compute on the next spike. Prevents the reading error that one near-miss = "I'm back to pre-2019."

## Enhanced Practical Ties to Your 2026 SNF Substrate Systems Project, PRS Work, DOV & 5-Year Vision
- High-trigger day (money runway pressure, social calendar, PRS exposure): Counter-script "Sober since 2019-11-01 ΓÇö this is temporary systems state" (spoken aloud) + log one micro-proof in status block or Proof-Log. Ties directly to financial-stability and career-strategy.
- Before PRS-related social, group, or interview: Quick anchor review of reasons + one safe contact text (or just "I can reach out"). Use with prs-safety-check and social-calibration. Register the prep action as proof of professional reliability.
- Post-lapse or low-energy collapse: "I made contact with the date today" (or meds + light + one counter-script line) as the floor win. Register in Proof-Log (project + main) to feed snf-hope-activation and accelerate restart speed. "I restart without punishment."
- Daily MVD integration: Sobriety anchors are often the non-negotiable first 1-2 items on any MVD list. They protect the identity floor so job search, trades training, and social reintegration can happen on top of a stable substrate.
- Weekly systems-audit / 5-year vision: Sobriety proof aggregate (days with registered anchors, trigger responses that worked, continuity despite low energy) shows the foundation enabling the parallel tracks (PRS credential + trades/HVAC path) and the long-horizon Cincinnati vision (stable function ΓåÆ partnership/family). Green sobriety = permission to expand.
- DOV / OneDrive / GitHub sync: The anchors and their proofs live in the synced vault (status blocks, Proof-Log, Library source). Emit packs for any AI on any device. The fact "sober since 2019-11-01" is now external data that survives fog, travel, or device loss. Pull Library updates so the counter-scripts and trigger lists stay current.
- PRS credential + trades expansion: Sobriety is the credibility foundation for the work you want to do (supporting others in recovery while building stable income in trades). Every registered anchor is evidence you can show up for clients and for yourself.

(This is the canonical version in the DOV 09-PROMPTS/Library ΓÇö the universal truth for all AI. All prompts consolidated here. Prefer editing source in vault and re-syncing/emitting to .grok and other models.)

---
This skill was generated from the canonical Obsidian note in the DOV vault (the universal truth), promoted to full 09 Library status, and enhanced 2026-06-13 with complete frontmatter, scientific basis, 2026 SNF project + PRS integration, and explicit ties to the other SNF skills as the recovery substrate trio.
```

## Skill / Protocol: mvd-anchors
**Description:** >
**Meta:** Energy: low | Domain: [recovery, execution, low-energy]

```markdown
---
type: skill
name: mvd-anchors
aliases: [mvd, minimum-viable-day, floor-anchors]
description: >
  Define and protect your Minimum Viable Day (MVD) anchors ΓÇö the smallest set of biological and identity actions that must happen even on collapse days to preserve self-trust and restart speed.
  Use daily when building or reviewing your floor, or when energy is low/collapse and you need to strip everything else away.
domain: [recovery, execution, low-energy]
energy: low
invocation: ["/mvd", "set my anchors", "minimum viable day", "floor plan"]
compatible_with: [grok, claude, gpt, local]
version: 1
last_reviewed: 2026-06-08
tags: [recovery, mvd, anchors, floor, low-energy, prs, sobriety, state-not-fate, no-shame]
---

# MVD Anchors

## Purpose
On days when motivation, energy, or executive function is near zero, you still have a non-negotiable floor. These anchors are the proof that you showed up for yourself. They are the foundation for all State Not Fate work: stabilize the biological and identity floor first, then expand.

## When to Use
- Every morning (or the night before) to define or reaffirm your MVD.
- On low/collapse energy days when the usual plan feels impossible.
- After a relapse or bad night ΓÇö restart speed matters more than perfection.
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
- low-energy-execution ΓÇö use this first on collapse days; MVD anchors are the core of it.
- thoroughness-protocol ΓÇö run /tp lightly when setting MVD so you don't over-ambition.
- floor-wins ΓÇö the logging and proof side (pairs with snf-proof-registration for registration).
- weekly-review ΓÇö review MVD effectiveness weekly.
- library-gardener ΓÇö audit that your anchors are still tiny and aligned.

## Notes & History
- Directly descended from the original State Not Fate MVD work and the 09_Low_Energy_Execution_Command in the David library.
- The goal is never "more anchors" ΓÇö it is "anchors small enough that you can still do them when everything else collapses."
- Update this note whenever your actual biological or identity floor changes (new meds, new living situation, new non-negotiables).
- This skill is foundational. Almost every other skill assumes the floor is protected.

Starter note created from Dictionary placeholders. Expand with personal MVD details and examples from your trackers.
```

## Skill / Protocol: floor-wins
**Description:** >
**Meta:** Energy: low | Domain: [recovery, execution, low-energy]

```markdown
---
type: skill
name: floor-wins
aliases: [floor-win, mvd-win, proof-log]
description: >
  Capture and log the smallest possible wins on low/collapse days so they feed your resilience rate, hope meter, and long-term proof that "action is possible" even when motivation is absent.
  Use at the end of any low-energy day or after completing MVD anchors.
domain: [recovery, execution, low-energy]
energy: low
invocation: ["/floor", "log my floor win", "what counts today"]
compatible_with: [grok, claude, gpt, local]
version: 1
last_reviewed: 2026-06-08
tags: [recovery, floor, floor-wins, proof, low-energy, prs, sobriety, state-not-fate, no-shame, mvd]
---

# Floor Wins

## Purpose
Depression and low energy destroy the brain's ability to register small victories. Floor wins are the deliberate, externalized proof that you did something that mattered when everything felt impossible. They are the raw material for the resilience calculation (restart speed) and the hope meter (action ΓåÆ results ΓåÆ repetition).

## When to Use
- At the end of any day where you used low-energy-execution or MVD anchors.
- Immediately after completing even one tiny anchor on a collapse day.
- When reviewing the week and you only have "floor" level activity to show.
- After any relapse or missed day ΓÇö to accelerate restart speed.
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
- mvd-anchors ΓÇö the actions that create floor wins; this skill is the logging/proof layer.
- low-energy-execution ΓÇö primary consumer of floor wins.
- weekly-review ΓÇö aggregate floor wins into weekly proof.
- thoroughness-protocol ΓÇö use lightly so you don't dismiss small wins.
- library-gardener ΓÇö review whether floor wins are actually being captured and feeding the system.

## Notes & History
- Core State Not Fate mechanism: external memory + proof registration repairs the damaged reward system.
- "Floor win" language is deliberately non-heroic. A floor win on a collapse day is worth more than a "productive" day on high energy in terms of long-term self-trust.
- Update this note whenever your logging method changes (new tracker, app, notebook, etc.).
- This skill pairs especially well with the hope meter and resilience rate calculations in the broader system.

Starter note created from Dictionary placeholders (recovery + floor-wins). Flesh out with your actual logging method and personal proof examples.
```


