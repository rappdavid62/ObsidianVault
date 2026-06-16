# Highest-Impact Missing Information

## Bottom line

The project already has a strong thesis, a strong startup frame, a workable intake layer, and a good long-horizon model. What it does **not** yet have is enough decision logic and operational specificity to make the system consistently deployable by an AI or another human.

## Highest-priority missing pieces

### 1. Canonical branching algorithm from intake -> first plan
The project has good questions and good principles, but not a formal decision tree.

What is missing:
- score interpretation rules
- thresholds for "start with hope repair" vs "start with sleep / circadian repair" vs "start with environment drag reduction"
- starter templates matched to battery level
- explicit branching for low / medium / strong / collapse-day planning

Why this matters:
Without this, personalization remains intelligent but loose. Two helpers or two AI runs could produce meaningfully different first plans from the same intake.

### 2. Dedicated triage and exclusion protocol
The source base names complexity flags, but does not yet package them into a clean gate.

What is missing:
- one-page triage SOP
- mania / bipolar red flags
- psychosis flags
- severe self-neglect thresholds
- substance destabilization thresholds
- medical rule-out prompts
- "self-management is not enough here" decision rule

Why this matters:
This is one of the biggest trust and safety gaps in the whole project.

### 3. Measurement-based care packet
Measurement is referenced, but not operationalized enough.

What is missing:
- a small standard battery, such as PHQ-9 plus a few project-specific function/hope items
- baseline / weekly / monthly cadence
- score interpretation bands
- what changes in the plan when scores move or stall
- a simple dashboard or review sheet

Why this matters:
You need a way to tell whether the system is working besides vibes, especially if AI is helping run it.

### 4. Worked case examples
The project has almost no concrete examples of full translation from intake -> formulation -> first month plan.

What is missing:
- 5 to 10 sample users
- completed sample intakes
- interpretation notes
- first-plan examples
- how the plan changes after setbacks
- examples for shutdown/anhedonia, chaotic environment, shame-heavy cases, sleep-drift cases, substance-heavy cases, and socially withdrawn cases

Why this matters:
Examples would massively improve consistency, training value, and AI retrieval quality.

### 5. One canonical operational manual
The current source base still has overlapping drafts.

What is missing:
- one authoritative v1 canon
- version number and date
- explicit "use this, ignore these drafts" note
- stable file naming

Why this matters:
AI retrieval gets worse when several similar files overlap and disagree at the margins.

### 6. Fully specified daily-state SOPs
The project references low/medium/strong/collapse days constantly, but the SOPs are not yet fully crystallized.

What is missing:
- one-page sheet for each day type
- minimum viable day template
- collapse-day rescue sequence
- re-entry-after-collapse steps
- "do less, but do not disappear" logic in concrete checklist form

Why this matters:
This is one of the most load-bearing mechanisms in the project and still too implicit.

### 7. Module-level intervention sheets
The project names core modules but most are still architectural placeholders.

Highest-value module sheets to add first:
- sleep / circadian repair
- movement / activation
- rumination interruption
- environment drag reduction
- social contact protection
- treatment / medication integration
- substance reality module

Why this matters:
Right now the project explains the framework better than it delivers the actual intervention packets.

### 8. Real-world pilot data
The project is conceptually strong but has no visible user-testing layer.

What is missing:
- where people drop out
- which intro language gets read vs rejected
- which first tasks actually get completed
- what people misinterpret
- what makes them return after bad weeks

Why this matters:
Pilot data would sharpen the language and make the system less theoretical.

## Best order to fill the gaps

1. branching algorithm
2. triage / exclusion protocol
3. daily-state SOPs
4. worked examples
5. measurement packet
6. module sheets
7. canonical v1 manual
8. pilot data and iteration
