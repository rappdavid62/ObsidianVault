---
type: skill
name: vault-cleaner
aliases: [/vault-cleaner, vault-cleanup, file-gardener, cleanup-queue]
description: >
  Clean and organize the DOV vault without destructive surprises: identify misplaced files, stale paths, duplicate source-truth claims, private-boundary risks, and cleanup queue updates.
domain: [meta, systems, library]
energy: medium
invocation: ["/vault-cleaner", "run vault cleaner", "clean up the vault", "file gardener"]
compatible_with: [all, obsidian, gpt, claude, local]
version: 1
last_reviewed: 2026-06-28
tags: [meta, maintenance, systems, external-memory, standards]
---

# Vault Cleaner

## Purpose

Keep DOV organized without turning cleanup into chaos. This skill audits file placement, source-truth drift, privacy boundaries, stale paths, and unresolved cleanup tasks, then makes the smallest safe improvements.

## When to Use

- Weekly or before syncing/pushing the vault.
- After large imports, zips, app captures, generated packs, or AI-assisted reorgs.
- When old folder names, duplicate notes, or stale paths make the vault hard to trust.
- Before moving, archiving, deleting, or renaming anything.
- When `Meta/Vault Cleanup Queue.md` needs review.

## Safety Rules

- Do not permanently delete files unless David explicitly confirms deletion in that environment.
- Prefer queueing, marking, or archiving over destructive cleanup.
- Do not open or quote private/adult/sensitive content unless David explicitly asks.
- Before any commit/push, inspect `.gitignore` and `git status`.
- Treat `09-PROMPTS/Library` as canonical for reusable skills and prompts.
- Treat generated packs, old bundles, zips, and build artifacts as derivatives or archives unless a file explicitly says it is canonical.

## Core Process

1. **Read governance**
   - `Meta/System Governance.md`
   - `Meta/AI Command Layer.md`
   - `Meta/Vault Cleanup Queue.md`
   - `09-PROMPTS/Library/Hubs/00-Hub.md`

2. **Inspect current state**
   - File tree for new, duplicate, misplaced, or untracked files.
   - `.gitignore` for private/local-only protection.
   - `git status --short` if this is a Git worktree.
   - Known capture and integration paths.

3. **Classify cleanup items**
   - Privacy/sensitive risk.
   - Source-of-truth conflict.
   - Stale path/reference.
   - Duplicate or derivative file.
   - Inbox/capture item needing routing.
   - Generated output needing regeneration.
   - Safe archive candidate.

4. **Act conservatively**
   - Fix small path/reference drift when the correct current path is proven.
   - Add unresolved work to `Meta/Vault Cleanup Queue.md`.
   - Regenerate derivative files only through existing tools.
   - Move files only when the destination and safety rule are clear.
   - Do not mass rename, delete, or flatten folders without explicit approval.

5. **Report**
   - What was checked.
   - What changed.
   - What was queued.
   - What needs David approval.
   - The next smallest cleanup action.

## Output Format

- **Bottom Line**: Current cleanup health in one sentence.
- **Checked**: Files, folders, trackers, and commands inspected.
- **Fixed Now**: Small safe corrections made.
- **Queued**: Cleanup items added or left in `Meta/Vault Cleanup Queue.md`.
- **Risks**: Privacy, source-truth, or sync risks.
- **Needs Approval**: Any move/delete/archive action that should not be automatic.
- **Next Small Action**: One concrete cleanup step.

## Related

- `second-brain-control-loop`
- `library-gardener`
- `ai-setup-audit`
- `Meta/Vault Cleanup Queue.md`
- `Meta/System Governance.md`
- `09-PROMPTS/Library/README.md`

## Notes & History

- Created on 2026-06-28 to turn the existing cleanup queue into a reusable, cross-program skill.
- This skill is intentionally conservative. A trusted second brain should make cleanup safer, not more dramatic.
