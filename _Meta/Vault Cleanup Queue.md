---
Status: Active
Primary Deployment Target: AI Infrastructure
Expected Use Case: Queue of unresolved vault cleanup, privacy, duplicate, archive, and source-truth tasks.
Archive or Active: Active
Supersedes:
Replaced By:
Canonical Home: _Meta/Vault Cleanup Queue.md
Related Files:
  - _Meta/Vault Master Index.md
  - _Meta/System Governance.md
  - _Meta/Legacy Bundle Migration Inventory.md
  - 09-PROMPTS/Library/Skills/vault-cleaner.md
  - 09-PROMPTS/Library/Skills/second-brain-control-loop.md
Last Reviewed: 2026-06-28
---

# Vault Cleanup Queue

## Bottom Line

This queue tracks cleanup tasks so loose material does not become permanent chaos.

## Highest Priority

### 1. Review private/adult candidates before any push

Existing paths to review without quoting contents:

- `00-CAPTURE/App Captures/TMHLBB.md`
- `00-CAPTURE/App Captures/Clippings/TMWLBB.md`
- `09-PROMPTS/Prompt-Library/BE_Roleplay_Generator.md`

Issue: Likely private/adult content or adult-adjacent prompt material.  
Recommended Action: Move to `_PRIVATE/SMUT/` unless intentionally sanitized for non-public use.  
Risk Level: High.  
Current Evidence: `.gitignore` protects `_PRIVATE/`, `99_PRIVATE/`, `99-PRIVATE/`, and adult/private archive patterns; `_PRIVATE/SMUT/` exists locally; current root has `00-CAPTURE/`, not `00-INBOX/`; currently existing candidates from this list are `00-CAPTURE/App Captures/TMHLBB.md`, `00-CAPTURE/App Captures/Clippings/TMWLBB.md`, and `09-PROMPTS/Prompt-Library/BE_Roleplay_Generator.md`.  
Next Step: Move existing candidates only with explicit approval.

Absent historical paths from older queue snapshots:

- `00-INBOX/Untitled.md`
- `Untitled.md`
- `04-ARCHIVES/40-BREAST EXPANSION/`

## Resolved This Pass

- `.gitignore` private rules are present.
- `_PRIVATE/SMUT/` exists locally.
- `00-CAPTURE/App Captures/` is the current capture path.
- `second-brain-control-loop` and `vault-cleaner` now exist as canonical Library skills.
- `01-PROJECTS/STATENOTFATE/Source Truth - Live Deploy vs Vault Artifacts.md` now separates DOV vault artifacts from live deploy work.
- `_Meta/Legacy Bundle Migration Inventory.md` now inventories `09-PROMPTS/Prompt-Library/` and archived AI_SYSTEM copies.

## Source-Truth Cleanup

### 2. Promote AI system files to `_Meta/`

Old Paths:

- `08-TECH-AND-AI/AI_SYSTEM/MASTER_CONTEXT.md`
- `08-TECH-AND-AI/AI_SYSTEM/AI SYSTEM SYSTEM GOVERNANCE.md`
- `08-TECH-AND-AI/AI SYSTEM SYSTEM GOVERNANCE.md`

New Paths:

- `_Meta/Master Context.md`
- `_Meta/System Governance.md`
- `_Meta/AI Command Layer.md`

Issue: Same governance/context ideas are split across old paths.  
Recommended Action: Keep Meta as canonical. Archive or mark old copies superseded.  
Risk Level: Medium.  
Current Evidence: `08-TECH-AND-AI/AI_SYSTEM/` is absent; superseded copies are already under `04-ARCHIVES/Superseded-AI-System/`.  
Next Step: Use `_Meta/Legacy Bundle Migration Inventory.md` as the register; do not recreate `08-TECH-AND-AI/AI_SYSTEM/`.

### 3. Prompt library duplication

Paths:

- `09-PROMPTS/Library/`
- `09-PROMPTS/Prompt-Library/`

Issue: `Library/` is structured and governed; `Prompt-Library/` appears older/looser.  
Recommended Action: Treat `09-PROMPTS/Library/` as canonical. Review `Prompt-Library/` for migration/archive.  
Risk Level: Medium.  
Current Evidence: `_Meta/Legacy Bundle Migration Inventory.md` lists current legacy bundle files and recommended action.  
Next Step: Migrate only missing durable behavior into atomic Library notes; do not bulk-copy legacy bundles.

### 4. State Not Fate source confusion

Paths:

- `01-PROJECTS/STATENOTFATE 1/`
- `01-PROJECTS/STATENOTFATE/`
- `08-TECH-AND-AI/BUILD/`
- uploaded zips
- `SNF_DEPLOY` local repo/folder

Issue: Multiple folders and zips can be mistaken for live production source.  
Recommended Action: Treat `SNF_DEPLOY` as live source if available; zips are archive/export unless explicitly restored.  
Risk Level: High for deployment confusion.  
Next Step: Use `01-PROJECTS/STATENOTFATE/Source Truth - Live Deploy vs Vault Artifacts.md` before any SNF deployment work.

## Inbox / Loose Notes

### 5. Empty or junk notes

Paths:

- `00-INBOX/clone.md` (folder not present in current root)
- `00-INBOX/Untitled 1.md` (folder not present in current root)
- `Untitled 1.md`
- empty `00-INBOX/Untitled 2/` (folder not present in current root)

Issue: Unprocessed or junk capture.  
Recommended Action: Delete if truly junk, otherwise classify.  
Risk Level: Low.  
Next Step: Review filenames only first; avoid opening private candidates in public contexts.

### 6. Depression question fragment

Path: `00-INBOX/depress q.md` (old path; current root has `00-CAPTURE/`)  
Issue: Useful concept fragment about depression narrowing perceived outcomes.  
Recommended Action: Move to State Not Fate concept/inbox or Personal IP draft.  
Risk Level: Low.  
Next Step: Convert into a short principle note if useful.

## Rule

Do not delete files permanently during cleanup unless there is a backup and David explicitly confirms the deletion in that environment.

Prefer move-to-archive over deletion for system files.
