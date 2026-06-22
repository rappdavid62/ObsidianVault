---
Status: Active
Primary Deployment Target: AI Infrastructure
Expected Use Case: High-level navigation map for David’s Obsidian vault and AI second-brain system.
Archive or Active: Active
Supersedes:
Replaced By:
Canonical Home: Meta/Vault Master Index.md
Related Files:
  - Meta/Master Context.md
  - Meta/AI Command Layer.md
  - Meta/Active Projects Map.md
  - Meta/Vault Cleanup Queue.md
Last Reviewed: 2026-06-22
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

### `00-INBOX/`

Purpose: raw capture, unprocessed app captures, pasted fragments, rough voice/text dumps.

Status: Active, but needs regular triage.

Known issue: contains adult/private candidates and duplicate loose notes. Review before committing or pushing.

### `01-PROJECTS/`

Purpose: active and historical project folders.

Key areas:

- `2026-SNF-Substrate-Systems-Project/` — active SNF substrate systems project.
- `STATENOTFATE 1/` — older State Not Fate project source packs and bridge materials.
- `STATENOTFATE/` — smaller State Not Fate folder with high-stakes depression/suicidality notes and universal prompt library.

Status: Active but contains duplicates and older exports.

### `03-RESOURCES/`

Purpose: resource library and Copilot custom prompts.

Status: Reference library.

### `04-ARCHIVES/`

Purpose: archived material.

Known issue: contains `40-BREAST EXPANSION/`, which should be reviewed for `_PRIVATE/SMUT/` relocation if this repo may be pushed.

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

- `AI_SYSTEM/` — older canonical AI system files; now superseded by `Meta/` canonical files.
- `BUILD/` — Polaris / State Not Fate build folders and notes.
- `CAPTURE/RAW_INBOX.md` — AI/tech capture stream.
- `MOCS/` — AI systems and State Not Fate MOCs.
- `Obsidian Integration/` — app connector playbooks and coverage maps.

Status: Active, but needs source-truth cleanup.

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

### `TEMPLATES/`

Purpose: integration and source note templates.

Status: Active reference.

### `_PRIVATE/`

Purpose: local-only private material.

Status: Should exist locally and be ignored by Git.

Required child folder:

```text
_PRIVATE/SMUT/
```

## Current Source-Truth Decision

Canonical AI infrastructure files should now live in:

```text
Meta/
```

The older `08-TECH-AND-AI/AI_SYSTEM/` files should be treated as superseded or archived once `Meta/` files are installed.

The prompt/skill source truth remains:

```text
09-PROMPTS/Library/
```

## Immediate Risks

1. `.gitignore` must protect `_PRIVATE/`, `99_PRIVATE/`, and smut/adult folders.
2. Adult/private review candidates must be moved before pushing.
3. State Not Fate zips are archive/export material, not automatically live source.
4. `.cursorrules` is derivative and may contain older/conflicting facts. Do not treat it as canonical.

## Next Actions

1. Install the `Meta/` command-layer files.
2. Update `.gitignore`.
3. Create `_PRIVATE/SMUT/`.
4. Move adult/private candidates.
5. Archive or supersede old `08-TECH-AND-AI/AI_SYSTEM/` duplicates.
6. Run `git status` before any push.
