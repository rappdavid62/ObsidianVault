---
Status: Active
Primary Deployment Target: AI Infrastructure
Expected Use Case: Track legacy prompt bundles and superseded AI-system files so they are not mistaken for canonical skill sources.
Archive or Active: Active
Supersedes:
Replaced By:
Canonical Home: Meta/Legacy Bundle Migration Inventory.md
Related Files:
  - Meta/Second Brain Operations Dashboard.md
  - Meta/Vault Cleanup Queue.md
  - 09-PROMPTS/Library/README.md
  - 09-PROMPTS/Library/Hubs/00-Hub.md
Last Reviewed: 2026-06-28
---

# Legacy Bundle Migration Inventory

## Bottom Line

The canonical reusable skill layer is `09-PROMPTS/Library/`. The files below are legacy bundles, archives, or superseded system copies. They should inform migration only; they should not override the atomic Library.

## Legacy Prompt-Library Files

Path: `09-PROMPTS/Prompt-Library/`

| File | Current role | Recommended action |
|---|---|---|
| `AI_Life_Coach_Friend.md` | Legacy full-bundle reference | Keep as reference; migrate only missing durable patterns into atomic Library notes |
| `ANTI_GRAVITY_Master_Prompt.md` | Legacy State Not Fate / AI prompt reference | Keep as reference; use atomic SNF skills and project notes for active guidance |
| `BE PROMPT.md` | Private/adult-adjacent prompt candidate by filename | Treat as private-review candidate; do not quote or surface content casually |
| `BE_Roleplay_Generator.md` | Private/adult-adjacent prompt candidate by filename | Treat as private-review candidate; likely move to `_PRIVATE/SMUT/` with approval |
| `David_AI_Prompt_Library.md` | Legacy prompt bundle | Keep as reference; migrate missing reusable commands into `09-PROMPTS/Library/Skills` or `Prompts` |
| `Grok Vault Master Update.pdf` | Historical/update artifact | Keep as archive/reference unless a specific migration task needs it |
| `Grok_Skills.md` | Legacy compiled skills reference | Keep as reference; atomic skills are canonical |
| `Tucked_Away_AI_Skills_and_Tiny_Tools.md` | Legacy discovery/reference note | Keep as reference; migrate missing tools only if still useful |

## Superseded AI-System Copies

Path: `04-ARCHIVES/Superseded-AI-System/`

The old `08-TECH-AND-AI/AI_SYSTEM/` folder is not present in the current `08-TECH-AND-AI/` root. Superseded copies already live under the archive path above.

| Archived item | Current role | Canonical replacement |
|---|---|---|
| `AI SYSTEM SYSTEM GOVERNANCE.md` | Archived governance copy | `Meta/System Governance.md` |
| `AI_SYSTEM/AI SYSTEM SYSTEM GOVERNANCE.md` | Archived governance copy | `Meta/System Governance.md` |
| `AI_SYSTEM/CURRENT_STATUS.md` | Archived status copy | `Meta/Master Context.md` plus active project status notes |
| `AI_SYSTEM/MASTER_CONTEXT.md` | Archived master context copy | `Meta/Master Context.md` |
| `AI_SYSTEM/SKILL.md` | Archived AI-system skill copy | `Meta/AI Command Layer.md` and `09-PROMPTS/Library/Skills/second-brain-control-loop.md` |

## Migration Rule

Do not bulk-copy legacy bundle text into the active Library. Extract only durable, reusable behavior that is still missing, then place it in one atomic canonical note with Dictionary-compliant frontmatter.

## Approval-Required Items

- Moving private/adult-adjacent legacy files into `_PRIVATE/SMUT/`.
- Deleting any legacy bundle or archive.
- Reclassifying a legacy file as active canonical source.
