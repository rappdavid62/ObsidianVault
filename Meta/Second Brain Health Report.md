---
Status: Active
Primary Deployment Target: AI Infrastructure
Expected Use Case: Current generated health report for DOV second-brain maintenance.
Archive or Active: Active
Canonical Home: Meta/Second Brain Health Report.md
Last Generated: 2026-06-28 05:26
---

# Second Brain Health Report

## Bottom Line

DOV health is **attention needed**. The canonical Library path is `C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library`.

## Required Surfaces

- OK: `Meta/Master Context.md`
- OK: `Meta/AI Command Layer.md`
- OK: `Meta/AI Handoff Summary.md`
- OK: `Meta/Second Brain Operations Dashboard.md`
- OK: `Meta/Vault Cleanup Queue.md`
- OK: `Meta/Second Brain Completion Audit.md`
- OK: `Meta/Second Brain Runbook.md`
- OK: `Meta/Second Brain Learning Ledger.md`
- OK: `Meta/Legacy Bundle Migration Inventory.md`
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

- OK: `Meta/Second Brain Learning Ledger.md` exists
- INFO: 0 open learning inbox items
- INFO: 4 promoted learning items

## Cleanup Queue

- OK: `Meta/Vault Cleanup Queue.md` exists
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

- INFO: 21 changed/untracked paths
- INFO: 16 modified, 5 untracked, 0 deleted
- `M "08-TECH-AND-AI/Obsidian Integration/All Apps Coverage Index.md"`
- ` M "08-TECH-AND-AI/Obsidian Integration/All Apps Coverage Map.md"`
- ` M "08-TECH-AND-AI/Obsidian Integration/App Coverage Checklist.md"`
- ` M "08-TECH-AND-AI/Obsidian Integration/App Proof Dashboard.md"`
- ` M "08-TECH-AND-AI/Obsidian Integration/Connector Capture Recipes.md"`
- ` M "08-TECH-AND-AI/Obsidian Integration/Integration Hub.md"`
- ` M "08-TECH-AND-AI/Obsidian Integration/app-proof-tracker.json"`
- ` M "09-PROMPTS/Library/External Program Skill Wiring Matrix.md"`
- ` M 09-PROMPTS/Library/Hubs/00-Hub.md`
- ` M 09-PROMPTS/Library/Mobile-Favorites.md`
- ` M 09-PROMPTS/Library/README.md`
- ` M 09-PROMPTS/Library/Skills/second-brain-control-loop.md`
- ` M 09-PROMPTS/Library/Tools/README.md`
- ` M 09-PROMPTS/Library/Tools/master_context_latest.txt`
- ` M 09-PROMPTS/Library/Tools/vault-health-check.py`
- ` M "Meta/Second Brain Operations Dashboard.md"`
- `?? "08-TECH-AND-AI/Obsidian Integration/Apps - Scite.md"`
- `?? "Meta/Second Brain Completion Audit.md"`
- `?? "Meta/Second Brain Health Report.md"`
- `?? "Meta/Second Brain Learning Ledger.md"`
- `?? "Meta/Second Brain Runbook.md"`

## Next Small Action

- Resolve or explicitly defer high-risk cleanup items in `Meta/Vault Cleanup Queue.md` before any push.
- Run `library-gardener` if Library files changed.
- Run `vault-cleaner` for unresolved file-placement or privacy-boundary items.
