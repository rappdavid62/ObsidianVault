---
Status: Active
Primary Deployment Target: AI Infrastructure
Expected Use Case: High-level navigation map for David’s Obsidian vault and AI second-brain system.
Archive or Active: Active
Supersedes:
Replaced By:
Canonical Home: _Meta/Vault Master Index.md
Related Files:
  - _Meta/Master Context.md
  - _Meta/AI Command Layer.md
  - _Meta/Second Brain Operations Dashboard.md
  - _Meta/Legacy Bundle Migration Inventory.md
  - _Meta/Active Projects Map.md
  - _Meta/Vault Cleanup Queue.md
Last Reviewed: 2026-06-28
---

# Vault Master Index

## Bottom Line

This file is the top-level map of the vault. It should orient David and AI agents without making them inspect every folder from scratch.

## Root Assumption

Preferred local vault path:

```text
C:\ROOT_OBSIDIAN\DOV
```

Do not assume access to this path unless the current tool/environment can actually read it.

## Top-Level Structure

### `00-CAPTURE/`

Purpose: raw capture, app captures, pasted fragments, rough voice/text dumps.

Status: Active, but needs regular triage.

Key path: `00-CAPTURE/App Captures/`

Known issue: some captures may be private/adult candidates. Review before committing or pushing.

### `01-PROJECTS/`

Purpose: active and historical project folders.

Key areas:

- `2026-SNF-Substrate-Systems-Project/` — active SNF substrate systems project.
- `STATENOTFATE 1/` — older State Not Fate project source packs and bridge materials.
- `STATENOTFATE/` — smaller State Not Fate folder with high-stakes depression/suicidality notes and universal prompt library.

Status: Active but contains duplicates and older exports.

### `02-AREAS/`

Purpose: ongoing areas of responsibility that are not single projects.

Status: Active reference area.

### `03-RESOURCES/`

Purpose: resource library and Copilot custom prompts.

Status: Reference library.

### `04-ARCHIVES/`

Purpose: archived material.

Current evidence: `04-ARCHIVES/40-BREAST EXPANSION/` is absent in the current root; superseded AI-system files live under `04-ARCHIVES/Superseded-AI-System/`.

### `05-WRITING/`

Purpose: voice, writing tests, favorite words, drafts, personal writing material.

Status: Active personal writing.

Known issue: may contain personal/creative drafts. Review privacy before pushing.

### `06-DAILY-NOTES/`

Purpose: daily notes and lightweight operational capture.

Status: Active.

### `07-HUMAN-HEALTH/`

Purpose: health/reference/person profile notes.

Status: Sensitive reference. Use carefully.

### `08-TECH-AND-AI/`

Purpose: AI setup, build notes, app integration notes, connector coverage, and AI system material.

Key areas:

- `BUILD/` — Polaris / State Not Fate build folders and notes.
- `CAPTURE/RAW_INBOX.md` — AI/tech capture stream.
- `MOCS/` — AI systems and State Not Fate MOCs.
- `Obsidian Integration/` — app connector playbooks and coverage maps.

Status: Active. Old `AI_SYSTEM/` copies are already archived under `04-ARCHIVES/Superseded-AI-System/`.

### `09-PROMPTS/`

Purpose: prompt library, skill library, AI systems, and reusable AI workflows.

Key source-truth folder:

```text
09-PROMPTS/Library/
```

Important files:

- `09-PROMPTS/Library/Hubs/00-Hub.md`
- `09-PROMPTS/Library/Dictionary.md`
- `09-PROMPTS/Library/SCHEMA.md`
- `09-PROMPTS/Library/Skills/`
- `09-PROMPTS/Library/Protocols/`
- `09-PROMPTS/Library/Tools/`

Status: Active and already substantial. Do not create a second prompt library unless intentionally migrating.

### `10-USER-DATA-FEEDBACK/`

Purpose: user data, feedback, and possible evidence inputs.

Status: Active, review privacy before sharing externally.

### `99-PRIVATE/`

Purpose: private local-only material.

Status: Exists locally and is ignored by Git.

### `Clippings/`

Purpose: imported or clipped web/reference material.

Status: Triage when used; promote durable items into project/resource notes.

### `_Meta/`

Purpose: current governance, context, operations, and source-truth maps.

Status: Active AI infrastructure.

### `TEMPLATES/`

Purpose: integration and source note templates.

Status: Active reference.

### `_PRIVATE/`

Purpose: local-only private material.

Status: Exists locally and is ignored by Git.

Required child folder:

```text
_PRIVATE/SMUT/
```

## Current Source-Truth Decision

Canonical AI infrastructure files should now live in:

```text
_Meta/
```

The older `08-TECH-AND-AI/AI_SYSTEM/` files are not present in the current `08-TECH-AND-AI/` root. Superseded copies are registered in `_Meta/Legacy Bundle Migration Inventory.md`.

The prompt/skill source truth remains:

```text
09-PROMPTS/Library/
```

Canonical second-brain operations dashboard:

```text
_Meta/Second Brain Operations Dashboard.md
```

Legacy bundle/archive register:

```text
_Meta/Legacy Bundle Migration Inventory.md
```

Top-level operator skills:

```text
09-PROMPTS/Library/Skills/second-brain-control-loop.md
09-PROMPTS/Library/Skills/vault-cleaner.md
```

## Immediate Risks

1. Adult/private review candidates must be moved before pushing.
2. Legacy `09-PROMPTS/Prompt-Library/` material needs selective migration/archive review through `_Meta/Legacy Bundle Migration Inventory.md`.
3. State Not Fate zips are archive/export material, not automatically live source.
4. `.cursorrules` is derivative and may contain older/conflicting facts. Do not treat it as canonical.

## Next Actions

1. Move or archive adult/private candidates with explicit approval.
2. Selectively migrate only missing durable behavior from `09-PROMPTS/Prompt-Library/`.
3. Use the State Not Fate source-truth note before any live app work.
4. Run `git status` before any push.
