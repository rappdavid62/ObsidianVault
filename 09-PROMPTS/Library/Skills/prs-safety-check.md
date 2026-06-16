---
type: skill
name: prs-safety-check
aliases: [prs-check, safety-floor, clinical-anchors]
description: >
  Run a quick, non-shaming clinical safety and self-management check using PRS principles before, during, or after any difficult day or decision.
  Use when energy is low, after a trigger, before high-stakes actions, or as a daily/weekly floor audit aligned with your Peer Recovery Supporter training.
domain: [prs, recovery, health]
energy: low
invocation: ["/prs", "safety check", "clinical floor", "prs check"]
compatible_with: [grok, claude, gpt, local]
version: 2
last_reviewed: 2026-06-13
tags: [prs, recovery, clinical-safety, low-energy, sobriety, mvd, floor, no-shame, state-not-fate, prs-track]
---

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
- [[low-energy-execution]] and [[mvd-anchors]] — the operational follow-through after a safety check says "floor only".
- [[thoroughness-protocol]] — run lightly; safety checks must stay grounded, not overly analytical.
- [[council-strategy]] — use the PRS expert lane when the check is Yellow/Red and big decisions are pending.
- [[social-calibration]] — for reaching out to safe contacts without over-explaining.
- Original State Not Fate safety screening and PRS training materials.

## Notes & History
- This skill is the clinical application of your Peer Recovery Supporter certification (APS.006470) turned inward.
- It is deliberately non-therapeutic: it is peer support + State Not Fate floor protection.
- Update whenever your personal safety contacts, local resources, or medication regimen change.
- This is a "use before you use other skills" gate on difficult days.
- Library Gardener pass 2026-06-13: Fixed domain compliance (removed 'low-energy' domain value not in Dictionary; now [prs, recovery, health]). Validated compliant post-edit. Included in full review packs + Favorites/Daily/low-energy emits. All emitter tests (--list/--validate/--search/packs) passed. Re-synced to .grok/skills/ and GitHub pushed. Links to mvd-anchors, sobriety-anchors, low-energy-execution, social-calibration, council-strategy confirmed. No body content changes.

Starter note created from Dictionary placeholders (prs + clinical-safety). Expand with your exact safety screening questions, personal safe contacts, and recent examples of when this check changed the plan.
