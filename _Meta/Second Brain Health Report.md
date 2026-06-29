---
Status: Active
Primary Deployment Target: AI Infrastructure
Expected Use Case: Current generated health report for DOV second-brain maintenance.
Archive or Active: Active
Canonical Home: _Meta/Second Brain Health Report.md
Last Generated: 2026-06-28 15:26
---

# Second Brain Health Report

## Bottom Line

DOV health is **attention needed**. The canonical Library path is `C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library`.

## Required Surfaces

- OK: `_Meta/Master Context.md`
- OK: `_Meta/AI Command Layer.md`
- OK: `_Meta/AI Handoff Summary.md`
- OK: `_Meta/Second Brain Operations Dashboard.md`
- OK: `_Meta/Vault Cleanup Queue.md`
- OK: `_Meta/Second Brain Completion Audit.md`
- OK: `_Meta/Second Brain Runbook.md`
- OK: `_Meta/Second Brain Learning Ledger.md`
- OK: `_Meta/Legacy Bundle Migration Inventory.md`
- OK: `09-PROMPTS/Library/README.md`
- OK: `09-PROMPTS/Library/Hubs/00-Hub.md`
- OK: `09-PROMPTS/Library/External Program Skill Wiring Matrix.md`
- OK: `09-PROMPTS/Library/Skills/second-brain-control-loop.md`
- OK: `09-PROMPTS/Library/Skills/vault-cleaner.md`
- OK: `09-PROMPTS/Library/Skills/library-gardener.md`
- OK: `09-PROMPTS/Library/Tools/emit-skill.py`
- OK: `09-PROMPTS/Library/Tools/build-master-context.py`
- OK: `09-PROMPTS/Library/Tools/export-for-phone.py`
- OK: `09-PROMPTS/Library/Tools/vault-health-check.py`
- OK: `09-PROMPTS/Library/Tools/vault-watcher.py`
- OK: `08-TECH-AND-AI/Obsidian Integration/Integration Hub.md`
- OK: `08-TECH-AND-AI/Obsidian Integration/app-proof-tracker.json`
- OK: `00-CAPTURE/App Captures`

## Private Boundaries

- OK: `.gitignore` contains `_PRIVATE/`
- OK: `.gitignore` contains `99_PRIVATE/`
- OK: `.gitignore` contains `99-PRIVATE/`
- OK: `_PRIVATE/SMUT` ignored by Git (.gitignore:48:_PRIVATE/	_PRIVATE/SMUT)
- OK: `99-PRIVATE` ignored by Git (.gitignore:60:99-PRIVATE/	99-PRIVATE)

## Generated Outputs

- OK: `09-PROMPTS/Library/Mobile-Favorites.md` contains `# Source: C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library`
- OK: `09-PROMPTS/Library/Tools/master_context_latest.txt` contains `C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library`

## App Proof Tracker

- OK: 26 apps tracked
- INFO: 11 `complete`
- INFO: 7 `deferred_low_priority`
- INFO: 8 `deferred_on_demand`
- OK: every tracker app has an app note or capture evidence

## Learning Ledger

- OK: `_Meta/Second Brain Learning Ledger.md` exists
- INFO: 0 open learning inbox items
- INFO: 6 promoted learning items

## Cleanup Queue

- OK: `_Meta/Vault Cleanup Queue.md` exists
- INFO: 2 high-risk cleanup items, 2 medium-risk, 2 low-risk
- RISK: private/adult review candidates still exist and need explicit human approval before move/archive:
  - `00-CAPTURE/App Captures/TMHLBB.md` (tracked by Git; not ignored)
  - `00-CAPTURE/App Captures/Clippings/TMWLBB.md` (tracked by Git; not ignored)
  - `09-PROMPTS/Prompt-Library/BE_Roleplay_Generator.md` (tracked by Git; not ignored)

## Source-Truth Drift

- OK: no active stale source-truth phrases found outside allowed watchlist files.

## Allowed Watchlist Hits

- `09-PROMPTS/Library/Mobile-Favorites.md` contains `08 PROMPTS/Library`
- `09-PROMPTS/Library/Skills/second-brain-control-loop.md` contains `08 PROMPTS/Library`
- `09-PROMPTS/Library/Tools/build-master-context.py` contains `C:\ROOT_OBSIDIAN\master-laptop-vault`
- `09-PROMPTS/Library/Tools/sync-all.py` contains `C:\ROOT_OBSIDIAN\master-laptop-vault`
- `09-PROMPTS/Library/Tools/sync-to-grok.py` contains `C:\ROOT_OBSIDIAN\master-laptop-vault`

## Git State

- INFO: 43 changed/untracked paths
- INFO: 12 modified, 16 untracked, 15 deleted
- `M .cursorrules`
- ` M 09-PROMPTS/Library/Claude-Project-Instructions.md`
- ` M "09-PROMPTS/Library/External Program Skill Wiring Matrix.md"`
- ` M 09-PROMPTS/Library/Gemini-System-Prompt.md`
- ` M 09-PROMPTS/Library/How-to-Use-Ubiquitously.md`
- ` M 09-PROMPTS/Library/Hubs/00-Hub.md`
- ` M 09-PROMPTS/Library/Mobile-Favorites.md`
- ` M 09-PROMPTS/Library/README.md`
- ` M 09-PROMPTS/Library/Skills/second-brain-control-loop.md`
- ` M 09-PROMPTS/Library/Skills/vault-cleaner.md`
- ` M 09-PROMPTS/Library/Tools/README.md`
- ` M 09-PROMPTS/Library/Tools/vault-health-check.py`
- ` D "Meta/AI Command Layer.md"`
- ` D "Meta/AI Handoff Summary.md"`
- ` D "Meta/Active Projects Map.md"`
- ` D Meta/Device_Sync_Protocol.md`
- ` D "Meta/Legacy Bundle Migration Inventory.md"`
- ` D "Meta/Master Context.md"`
- ` D Meta/Project_Priority_Tracker.md`
- ` D "Meta/Second Brain Completion Audit.md"`
- ` D "Meta/Second Brain Health Report.md"`
- ` D "Meta/Second Brain Learning Ledger.md"`
- ` D "Meta/Second Brain Operations Dashboard.md"`
- ` D "Meta/Second Brain Runbook.md"`
- ` D "Meta/System Governance.md"`
- ... 18 more paths omitted
- RISK: tracked files are deleted in Git state; resolve or explicitly approve the rename/removal before push.

## Next Small Action

- Resolve or explicitly approve tracked-file deletions/renames in Git state before any push.
- Run `library-gardener` if Library files changed.
- Run `vault-cleaner` for unresolved file-placement or privacy-boundary items.
