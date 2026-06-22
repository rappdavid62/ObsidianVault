---
Status: Active
Primary Deployment Target: AI Infrastructure
Expected Use Case: Queue of unresolved vault cleanup, privacy, duplicate, archive, and source-truth tasks.
Archive or Active: Active
Supersedes:
Replaced By:
Canonical Home: Meta/Vault Cleanup Queue.md
Related Files:
  - Meta/Vault Master Index.md
  - Meta/System Governance.md
Last Reviewed: 2026-06-22
---

# Vault Cleanup Queue

## Bottom Line

This queue tracks cleanup tasks so loose material does not become permanent chaos.

## Highest Priority

### 1. Fix `.gitignore` private rules

Path: `.gitignore`  
Issue: Uploaded backup `.gitignore` did not show `_PRIVATE/`, `99_PRIVATE/`, or smut/adult ignore rules.  
Recommended Action: Add ignore rules.  
Risk Level: High.  
Next Step: Install `gitignore_private_addendum.txt` rules or run `INSTALL_SECOND_BRAIN_LAYER.ps1`.

### 2. Create private local-only folders

Path: `_PRIVATE/SMUT/`  
Issue: Adult/private material needs a local-only target.  
Recommended Action: Create `_PRIVATE/SMUT/`.  
Risk Level: High.  
Next Step: Move adult/private candidates there before pushing.

### 3. Move adult/private review candidates

Paths to review without quoting contents:

- `00-INBOX/Untitled.md`
- `Untitled.md`
- `00-INBOX/App Captures/TMHLBB.md`
- `00-INBOX/App Captures/Clippings/TMWLBB.md`
- `04-ARCHIVES/40-BREAST EXPANSION/`
- `09-PROMPTS/Prompt-Library/BE_Roleplay_Generator.md`

Issue: Likely private/adult content or adult-adjacent prompt material.  
Recommended Action: Move to `_PRIVATE/SMUT/` unless intentionally sanitized for non-public use.  
Risk Level: High.  
Next Step: Use `Move-Private-Candidates.ps1`.

## Source-Truth Cleanup

### 4. Promote AI system files to `Meta/`

Old Paths:

- `08-TECH-AND-AI/AI_SYSTEM/MASTER_CONTEXT.md`
- `08-TECH-AND-AI/AI_SYSTEM/AI SYSTEM SYSTEM GOVERNANCE.md`
- `08-TECH-AND-AI/AI SYSTEM SYSTEM GOVERNANCE.md`

New Paths:

- `Meta/Master Context.md`
- `Meta/System Governance.md`
- `Meta/AI Command Layer.md`

Issue: Same governance/context ideas are split across old paths.  
Recommended Action: Keep Meta as canonical. Archive or mark old copies superseded.  
Risk Level: Medium.  
Next Step: Install Meta files, then move old AI_SYSTEM folder to archive.

### 5. Prompt library duplication

Paths:

- `09-PROMPTS/Library/`
- `09-PROMPTS/Prompt-Library/`

Issue: `Library/` is structured and governed; `Prompt-Library/` appears older/looser.  
Recommended Action: Treat `09-PROMPTS/Library/` as canonical. Review `Prompt-Library/` for migration/archive.  
Risk Level: Medium.  
Next Step: Do not delete yet; create migration list first.

### 6. State Not Fate source confusion

Paths:

- `01-PROJECTS/STATENOTFATE 1/`
- `01-PROJECTS/STATENOTFATE/`
- `08-TECH-AND-AI/BUILD/`
- uploaded zips
- `SNF_DEPLOY` local repo/folder

Issue: Multiple folders and zips can be mistaken for live production source.  
Recommended Action: Treat `SNF_DEPLOY` as live source if available; zips are archive/export unless explicitly restored.  
Risk Level: High for deployment confusion.  
Next Step: Add source-truth note to State Not Fate project area.

## Inbox / Loose Notes

### 7. Empty or junk notes

Paths:

- `00-INBOX/clone.md`
- `00-INBOX/Untitled 1.md`
- `Untitled 1.md`
- empty `00-INBOX/Untitled 2/`

Issue: Unprocessed or junk capture.  
Recommended Action: Delete if truly junk, otherwise classify.  
Risk Level: Low.  
Next Step: Review filenames only first; avoid opening private candidates in public contexts.

### 8. Depression question fragment

Path: `00-INBOX/depress q.md`  
Issue: Useful concept fragment about depression narrowing perceived outcomes.  
Recommended Action: Move to State Not Fate concept/inbox or Personal IP draft.  
Risk Level: Low.  
Next Step: Convert into a short principle note if useful.

## Rule

Do not delete files permanently during cleanup unless there is a backup and David explicitly confirms the deletion in that environment.

Prefer move-to-archive over deletion for system files.
