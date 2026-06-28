---
type: skill
name: second-brain-control-loop
aliases: [/brain, second-brain-operator, vault-operator, learning-loop]
description: >
  Operate the DOV vault as a living second brain: monitor the core surfaces, run the Library Gardener and Vault Cleaner loops, surface problems, and fold useful discoveries back into the canonical skill layer.
domain: [meta, systems, library, ai-setup]
energy: medium
invocation: ["/brain", "run second brain control loop", "monitor and improve the vault", "make the vault smarter"]
compatible_with: [all, obsidian, gpt, claude, local, phone]
version: 1
last_reviewed: 2026-06-28
tags: [meta, maintenance, systems, external-memory, standards]
---

# Second Brain Control Loop

## Purpose

Turn DOV from a folder of notes into a learning operating system. This skill tells any AI program how to monitor the vault, run the maintenance routines, report problems, and promote durable learning back into the one canonical Library.

## When to Use

- Weekly or after any major vault, project, or AI-session change.
- When the vault feels scattered or stale.
- Before trusting exported packs, custom instructions, phone prompts, or external AI project instructions.
- When a session finds a better prompt, habit, workflow, tracker, app proof, or cleanup rule.
- When preparing a handoff to ChatGPT, Claude, Gemini, Grok, Codex, Cursor, or a phone chat.

## Core Rule

The canonical skill layer is:

```text
C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library
```

Everything else is a derivative, snapshot, app-specific surface, or project artifact unless it is explicitly named as canonical.

## Core Process

1. **Bootstrap the current state**
   - Read `Meta/Master Context.md`.
   - Read `Meta/AI Command Layer.md`.
   - Read `09-PROMPTS/Library/Hubs/00-Hub.md`.
   - Read `08-TECH-AND-AI/Obsidian Integration/Integration Hub.md`.
   - Read `Meta/Second Brain Completion Audit.md` before claiming full-goal completion.
   - Read `Meta/Second Brain Runbook.md`.
   - Read `Meta/Vault Cleanup Queue.md`.
   - Read `Meta/Second Brain Learning Ledger.md`.
   - Run `Tools/vault-health-check.py` when local command execution is available.
   - Check current worktree/file state before relying on prior memory.

2. **Classify the run**
   - Library maintenance.
   - Vault cleanup.
   - App integration proof.
   - Project priority audit.
   - Export/sync refresh.
   - Handoff/context update.
   - Problem report only.

3. **Run the right loops**
   - Use `library-gardener` for skill/prompt quality, Dictionary compliance, duplicates, and emit testing.
   - Use `vault-cleaner` for file organization, source-truth drift, old inbox paths, private/local-only boundaries, and cleanup queue updates.
   - Use `ai-setup-audit` when external AI tools or app-specific instructions have drifted.
   - Use `priority-audit` when projects compete for attention.

4. **Monitor for drift**
   - Old source roots such as `08 PROMPTS/Library`, old Laptop Sync language, or stale external paths.
   - Capture paths that do not match `00-CAPTURE/App Captures`.
   - Generated packs that disagree with atomic notes.
   - App proof notes that disagree with `app-proof-tracker.json`.
   - Private/adult/sensitive material outside local-only areas.
   - Duplicate source-of-truth claims across `Meta/`, `09-PROMPTS/`, and project folders.

5. **Promote learning**
   - Review `Meta/Second Brain Learning Ledger.md` for unresolved lessons.
   - If a session produces a better reusable instruction, add it to the relevant atomic skill/prompt/context note.
   - If the learning is a one-off fact, put it in the relevant project or context note.
   - If the learning is unresolved, add it to `Meta/Vault Cleanup Queue.md` or the relevant tracker.
   - If the lesson is useful but not ready to promote, add or update an inbox item in `Meta/Second Brain Learning Ledger.md`.
   - Bump `version` and `last_reviewed` only on notes actually reviewed or changed.

6. **Regenerate derivatives**
   - Run `Tools/vault-health-check.py --write` after major maintenance to refresh the current health report.
   - Run `Tools/export-for-phone.py` after mobile-relevant Library changes.
   - Run `Tools/emit-skill.py --validate <name>` on changed skills/prompts.
   - Run `Tools/build-master-context.py --daily` after changing core daily context.
   - Treat `sync-all.py` as a broader external-sync operation; run only when writing to external skill/plugin destinations is intended and allowed.

7. **Report honestly**
   - Separate what was changed, what was verified, what remains unresolved, and what was not accessible.
   - Never claim Gmail, Drive, browser, GitHub, phone, or external apps were checked unless the current session actually checked them.
   - Prefer one concrete next action over a giant backlog.

## Output Format

- **Bottom Line**: One sentence on vault health and the main improvement made.
- **Control Surfaces Checked**: Files or tools inspected.
- **Changes Made**: Notes/tools/trackers updated.
- **Learning Promoted**: New reusable insight added to the Library or project notes.
- **Problems Found**: Ranked by risk.
- **Verification**: Commands run and what they proved.
- **Next Loop**: The next smallest useful maintenance action.

## Related

- `library-gardener`
- `vault-cleaner`
- `ai-setup-audit`
- `priority-audit`
- `tool-mode-decider`
- `09-PROMPTS/Library/Hubs/00-Hub.md`
- `Meta/Second Brain Completion Audit.md`
- `Meta/Second Brain Runbook.md`
- `Meta/Vault Cleanup Queue.md`
- `Meta/Second Brain Learning Ledger.md`
- `Meta/Second Brain Health Report.md`
- `08-TECH-AND-AI/Obsidian Integration/App Proof Dashboard.md`
- `09-PROMPTS/Library/Tools/vault-health-check.py`

## Notes & History

- Created on 2026-06-28 to make the second-brain layer explicit instead of implied across scattered governance notes.
- 2026-06-28: Added the learning ledger as the durable holding surface for lessons before promotion into Library, project, app-proof, or cleanup notes.
- 2026-06-28: Added the runbook as the daily/weekly/triggered cadence for running the second-brain loops.
- 2026-06-28: Added the completion audit as the requirement-by-requirement gate before marking the full DOV goal complete.
- This is the top-level operator skill. It coordinates other skills; it does not replace them.
- Default stance is non-destructive: report, link, archive, or queue before deleting/moving unless David explicitly approves a specific cleanup action.
