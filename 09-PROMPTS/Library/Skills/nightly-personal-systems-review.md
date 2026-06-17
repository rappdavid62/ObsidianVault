---
type: skill
name: nightly-personal-systems-review
aliases: [nightly-review, daily-9pm, /nightly]
description: >
  Run David's daily 9 PM cross-platform review by checking the available local computer, Obsidian vault, Google Drive, Codex memory, and current status, then produce a bottom-line-first plan scaled to energy. Use when the user asks for the nightly review, daily 9 PM run, personal systems check, or a cross-device skill that considers local files, Drive, and known context.
domain: [execution, meta, recovery, ai-setup]
energy: variable
invocation: ["/nightly", "nightly review", "daily 9 PM", "personal systems review"]
compatible_with: [all, obsidian, phone, gpt, grok, claude, local]
version: 1
last_reviewed: 2026-06-16
tags: [daily, routine, state-not-fate, bottom-line-first, external-memory, visible-proof, low-energy, ai-setup, ubiquity, systems-audit]
frequency: daily
estimated_time: "10-25 min"
requires_status_block: true
output_style: bottom-line-first
priority: high
---

# Nightly Personal Systems Review

## Purpose
Turn the end of the day into one reliable external-memory pass: gather what changed, register proof, protect the floor, and decide tomorrow's first move without shame or overbuilding.

## When to Use
- Run daily at 9 PM local time.
- Use when the user asks for `/nightly`, "daily 9 PM", "search my computer and Google Drive", "what should I do tomorrow", or "consider everything you know about me".
- Use after a long Codex/Drive/Obsidian session to preserve what mattered.
- Use on low-energy or collapse days, but scale the output down to floor protection only.

## Core Instructions
1. Start with the current status block: date, time, energy, mood/state, sleep, meds/food/water, sobriety status, money/runway pressure, job/search pressure, urgent commitments, and today's main friction.
2. Search only the sources that are actually available in the current environment. Prefer targeted search over broad rummaging.
3. Separate evidence by source:
   - **Local computer / Codex**: Obsidian vault, active repos, recent outputs, automation memories, logs, and current workspace.
   - **Google Drive**: recent documents, Obsidian/AI library folders, State Not Fate docs, resumes, run reports, and handoff files.
   - **Obsidian**: `09-PROMPTS/Library`, `06-DAILY-NOTES`, `07-HUMAN-HEALTH`, `08-TECH-AND-AI`, `09-PROMPTS`, and `STATENOTFATE`.
   - **Known profile context**: State Not Fate, PRS/career path, sobriety since 2019-11-01, variable energy, Windows/PowerShell, preference for exact evidence over vague narration.
4. Preserve the user's operating style:
   - Bottom line first.
   - Concrete evidence over reassurance.
   - Separate live-host state, local source state, and what was actually verified.
   - Add tests first and make minimum website changes when working in `SNF_Deploy`.
   - Do not delete safety checks or weaken crisis/safety coverage.
   - Inspect risky PowerShell installers before execution.
5. Register proof before planning: identify 1-5 concrete things that happened today, even if tiny.
6. Identify unresolved loops: open tasks, broken automations, stale deploys, job/application next steps, health/recovery anchors, money/runway risks, social messages, or library maintenance.
7. Scale tomorrow's plan:
   - **Collapse**: sobriety/contact with the date, water/meds/food, light, hygiene, one visible proof action.
   - **Low**: MVD anchors, one admin/job/system micro-action, one proof log.
   - **Medium**: one focused work block, one career/money action, one health/recovery anchor, one cleanup/update.
   - **High**: deeper build/research/testing block, but cap scope and preserve tomorrow's floor.
8. End with a single first action for tomorrow morning and where to log tonight's result.

## Tool-Specific Search Pattern

### If Running In Codex On Windows
- Search local notes and repos with targeted file/name searches first.
- Useful paths:
  - `C:\Users\rappd\OneDrive\Desktop\ObsidianVault`
  - `C:\Users\rappd\OneDrive\Desktop\SNF_Deploy`
  - `C:\Users\rappd\.codex\memories`
  - `C:\Users\rappd\.codex\automations`
  - current Codex workspace outputs
- Prefer `rg` or native PowerShell searches.
- If a location is outside the sandbox, ask for the narrowest read-only permission.
- Do not claim a live deploy or public site is fixed unless it was actually verified.

### If Google Drive Is Available
- Check recent files first.
- Then search concise terms: `Obsidian`, `Codex`, `State Fate`, `skill`, `resume`, `handoff`, `run report`.
- Fetch only files that appear relevant.
- Summarize findings with links or exact titles; do not dump private content unless asked.

### If On Phone Or A Tool-Limited AI
- Ask the user for a quick status block and optionally the latest `Mobile-Favorites.md` / current daily note.
- Use this skill as the prompt.
- Do not pretend to search unavailable files. Say what context is missing and still produce a scaled nightly plan.

## Output Format
- **Bottom Line**: One sentence on tonight's state and tomorrow's priority.
- **What I Checked**: Local / Drive / Obsidian / Memory / User-provided context, with "not available" where true.
- **Proof Registered**: 1-5 concrete wins or survival proofs.
- **Open Loops**: Severity-ranked, with source and why it matters.
- **Tomorrow Plan**:
  - Ideal Move
  - Realistic Move
  - Floor Move
- **First Action Tomorrow**: One tiny action, written as an instruction.
- **Where To Save This**: Daily note, relevant project note, tracker, or library note.

## Safety And Privacy Rules
- Do not search for or expose secrets, API keys, passwords, private medical details, or sensitive personal content unless the user explicitly asks and the task requires it.
- If a file looks like a credential or key file, report the risk and stop short of quoting the secret.
- For health/recovery content, stay adjunctive and practical; do not diagnose or replace professional care.
- For public web work, preserve crisis/safety language and report anything unsavory or inappropriate plainly.
- If uncertainty remains, label it as unverified instead of smoothing it over.

## Context To Inject
- Current status block.
- Recent daily note or tracker row if available.
- Current Obsidian Library Hub or `Mobile-Favorites.md` if running on phone.
- Current Codex memory summary if available.
- Any active project path, especially `SNF_Deploy`.

## Related Skills & Prompts
- [[mvd-anchors]]
- [[low-energy-execution]]
- [[floor-wins]]
- [[snf-proof-registration]]
- [[snf-hope-activation]]
- [[systems-audit]]
- [[tool-mode-decider]]
- [[library-gardener]]
- [[daily-job-search]]
- [[financial-stability]]
- [[sobriety-anchors]]
- [[circadian-anchors]]

## Notes & History
- Created 2026-06-16 after searching local Obsidian vaults, Google Drive, and Codex memory.
- Designed for the Laptop Sync / ObsidianVault system as the cross-device source of truth.
- Daily automation target: 9 PM America/New_York.
- Keep this skill compact enough to paste into any AI, but specific enough to preserve David's real operating rules.

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)
