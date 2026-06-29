---
Status: Active
Primary Deployment Target: AI Infrastructure
Expected Use Case: Compact operations dashboard for monitoring DOV, running gardener/cleaner loops, refreshing exports, and reporting unresolved problems.
Archive or Active: Active
Supersedes:
Replaced By:
Canonical Home: _Meta/Second Brain Operations Dashboard.md
Related Files:
  - _Meta/Master Context.md
  - _Meta/AI Command Layer.md
  - _Meta/Vault Master Index.md
  - _Meta/Vault Cleanup Queue.md
  - _Meta/Second Brain Completion Audit.md
  - _Meta/Second Brain Runbook.md
  - _Meta/Second Brain Learning Ledger.md
  - _Meta/Second Brain Health Report.md
  - _Meta/Legacy Bundle Migration Inventory.md
  - 09-PROMPTS/Library/Hubs/00-Hub.md
  - 09-PROMPTS/Library/External Program Skill Wiring Matrix.md
  - 09-PROMPTS/Library/Skills/second-brain-control-loop.md
  - 09-PROMPTS/Library/Skills/vault-cleaner.md
Last Reviewed: 2026-06-28
---

# Second Brain Operations Dashboard

## Bottom Line

DOV is organized around one canonical skill layer and two maintenance loops:

- Skill source truth: `09-PROMPTS/Library/`
- Top-level operator: `09-PROMPTS/Library/Skills/second-brain-control-loop.md`
- Cleanup operator: `09-PROMPTS/Library/Skills/vault-cleaner.md`

## Current Control Surfaces

| Surface | Current path | Role |
|---|---|---|
| Master context | `_Meta/Master Context.md` | Stable user/system context |
| Command layer | `_Meta/AI Command Layer.md` | Rules for AI agents |
| System governance | `_Meta/System Governance.md` | Persistence/source-truth rules |
| Vault index | `_Meta/Vault Master Index.md` | Folder map |
| Active projects | `_Meta/Active Projects Map.md` | Current project map |
| Cleanup queue | `_Meta/Vault Cleanup Queue.md` | Unresolved cleanup risks |
| Completion audit | `_Meta/Second Brain Completion Audit.md` | Requirement-by-requirement readiness and blocker audit |
| Runbook | `_Meta/Second Brain Runbook.md` | Daily, weekly, and triggered cadence for operating the vault |
| Learning ledger | `_Meta/Second Brain Learning Ledger.md` | Lessons waiting for promotion into durable notes |
| Health report | `_Meta/Second Brain Health Report.md` | Generated snapshot of required surfaces, drift, private boundaries, and Git state |
| Legacy migration | `_Meta/Legacy Bundle Migration Inventory.md` | Prompt bundle and superseded AI-system inventory |
| Skill hub | `09-PROMPTS/Library/Hubs/00-Hub.md` | Canonical Library entry point |
| External wiring | `09-PROMPTS/Library/External Program Skill Wiring Matrix.md` | Keeps external AI surfaces pointed at one Library |
| App integration | `08-TECH-AND-AI/Obsidian Integration/Integration Hub.md` | Connector/app proof map |
| Capture inbox | `00-CAPTURE/App Captures/` | App/web capture landing area |

## Operating Commands

```powershell
python "09-PROMPTS\Library\Tools\emit-skill.py" second-brain-control-loop vault-cleaner --with-master
python "09-PROMPTS\Library\Tools\emit-skill.py" --favorites
python "09-PROMPTS\Library\Tools\export-for-phone.py"
python "09-PROMPTS\Library\Tools\build-master-context.py" --daily
python "09-PROMPTS\Library\Tools\vault-health-check.py" --write
python "09-PROMPTS\Library\Tools\vault-health-check.py" --fail-on-attention
python "09-PROMPTS\Library\Tools\vault-watcher.py"
```

## Monitoring Loop

Run weekly or after major imports/AI sessions:

1. Read this dashboard.
2. Follow `_Meta/Second Brain Runbook.md` for daily, weekly, or triggered cadence.
3. Check `_Meta/Second Brain Completion Audit.md` before claiming the full goal is done.
4. Run `Tools/vault-health-check.py --write`.
5. Run `/brain` (`second-brain-control-loop`).
6. Run `library-gardener` if the Library changed.
7. Run `/vault-cleaner` if files, paths, privacy, or source truth changed.
8. Review `_Meta/Second Brain Learning Ledger.md` and promote durable lessons.
9. Regenerate `Mobile-Favorites.md` after mobile-relevant Library changes.
10. Check `External Program Skill Wiring Matrix.md` when an external AI surface changes.
11. Update `_Meta/Vault Cleanup Queue.md` with unresolved items only.

## Current Verified State

- `00-CAPTURE/App Captures/` exists and is the active app-capture path.
- `00-INBOX/` does not currently exist and should not be recreated by default.
- `.gitignore` includes `_PRIVATE/`, `99_PRIVATE/`, `99-PRIVATE/`, and adult/private archive patterns.
- `_PRIVATE/SMUT/` exists locally and is ignored by Git through `_PRIVATE/`.
- `99-PRIVATE/` exists and is ignored by Git.
- `_Meta/Second Brain Completion Audit.md` exists and marks the full goal not complete while high-risk cleanup remains.
- `second-brain-control-loop` and `vault-cleaner` validate against the Library Dictionary.
- `Mobile-Favorites.md` begins with the second-brain control loop.
- `_Meta/Second Brain Runbook.md` exists as the daily/weekly/triggered operating cadence.
- `_Meta/Second Brain Learning Ledger.md` exists as the learning promotion queue.
- `09-PROMPTS/Library/Tools/vault-watcher.py` exists as a guarded monitor that runs strict health before outbound sync.

## Remaining Risks

1. Private/adult review candidates still need human-approved move/archive decisions.
2. `09-PROMPTS/Prompt-Library/` remains a legacy bundle area; review through `_Meta/Legacy Bundle Migration Inventory.md`.
3. State Not Fate live deploy work still requires verification of the external deploy repo before production claims.
4. Generated packs and older external-tool instruction files may still contain historical wording; treat atomic Library notes as canonical.

## Project Source Boundaries

- State Not Fate deploy boundary: `01-PROJECTS/STATENOTFATE/Source Truth - Live Deploy vs Vault Artifacts.md`
- Legacy prompt/system migration inventory: `_Meta/Legacy Bundle Migration Inventory.md`

## Reporting Rule

Every maintenance run should report:

- What was checked.
- What changed.
- What learning was promoted or queued.
- What was verified.
- What remains unresolved.
- The next smallest action.
