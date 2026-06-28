---
Status: Active
Primary Deployment Target: AI Infrastructure
Expected Use Case: Compact operations dashboard for monitoring DOV, running gardener/cleaner loops, refreshing exports, and reporting unresolved problems.
Archive or Active: Active
Supersedes:
Replaced By:
Canonical Home: Meta/Second Brain Operations Dashboard.md
Related Files:
  - Meta/Master Context.md
  - Meta/AI Command Layer.md
  - Meta/Vault Master Index.md
  - Meta/Vault Cleanup Queue.md
  - Meta/Legacy Bundle Migration Inventory.md
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
| Master context | `Meta/Master Context.md` | Stable user/system context |
| Command layer | `Meta/AI Command Layer.md` | Rules for AI agents |
| System governance | `Meta/System Governance.md` | Persistence/source-truth rules |
| Vault index | `Meta/Vault Master Index.md` | Folder map |
| Active projects | `Meta/Active Projects Map.md` | Current project map |
| Cleanup queue | `Meta/Vault Cleanup Queue.md` | Unresolved cleanup risks |
| Legacy migration | `Meta/Legacy Bundle Migration Inventory.md` | Prompt bundle and superseded AI-system inventory |
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
```

## Monitoring Loop

Run weekly or after major imports/AI sessions:

1. Read this dashboard.
2. Run `/brain` (`second-brain-control-loop`).
3. Run `library-gardener` if the Library changed.
4. Run `/vault-cleaner` if files, paths, privacy, or source truth changed.
5. Regenerate `Mobile-Favorites.md` after mobile-relevant Library changes.
6. Check `External Program Skill Wiring Matrix.md` when an external AI surface changes.
7. Update `Meta/Vault Cleanup Queue.md` with unresolved items only.

## Current Verified State

- `00-CAPTURE/App Captures/` exists and is the active app-capture path.
- `00-INBOX/` does not currently exist and should not be recreated by default.
- `.gitignore` includes `_PRIVATE/`, `99_PRIVATE/`, `99-PRIVATE/`, and adult/private archive patterns.
- `_PRIVATE/SMUT/` exists locally and is ignored by Git through `_PRIVATE/`.
- `99-PRIVATE/` exists and is ignored by Git.
- `second-brain-control-loop` and `vault-cleaner` validate against the Library Dictionary.
- `Mobile-Favorites.md` begins with the second-brain control loop.

## Remaining Risks

1. Private/adult review candidates still need human-approved move/archive decisions.
2. `09-PROMPTS/Prompt-Library/` remains a legacy bundle area; review through `Meta/Legacy Bundle Migration Inventory.md`.
3. State Not Fate live deploy work still requires verification of the external deploy repo before production claims.
4. Generated packs and older external-tool instruction files may still contain historical wording; treat atomic Library notes as canonical.

## Project Source Boundaries

- State Not Fate deploy boundary: `01-PROJECTS/STATENOTFATE/Source Truth - Live Deploy vs Vault Artifacts.md`
- Legacy prompt/system migration inventory: `Meta/Legacy Bundle Migration Inventory.md`

## Reporting Rule

Every maintenance run should report:

- What was checked.
- What changed.
- What was verified.
- What remains unresolved.
- The next smallest action.
