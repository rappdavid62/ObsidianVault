---
type: index
status: active
created: 2026-06-17
updated: 2026-06-17
source_app: Codex
tags:
  - obsidian/integration
  - source-code
  - registry
---

# Source Code Registry

## Purpose

This is the map of important source code that should be available to AI work across devices and programs without copying every file into every chat.

Rule: code lives in code folders and repos. This vault stores the index, intent, runbook, decisions, and proof.

## Local Code Inventory

| Codebase | Path | Role | Status | Next Proof Needed |
|---|---|---|---|---|
| DOV Library Tools | `09-PROMPTS/Library/Tools` | Emits, exports, and syncs canonical skills across AI systems | active | Run emitter, validator, phone export, and controlled sync dry-run pattern |
| Deprecated Polaris Build Notes | `08-TECH-AND-AI/BUILD` | Historical Markdown notes only; runnable artifacts removed from active code | deprecated | Decide later whether to archive or delete written history |
| Vault Git Sync | `git-sync.ps1` | Local vault Git sync helper | active utility | Confirm intended remote/branch and safe sync behavior |
| App Proof Tracker | `08-TECH-AND-AI/Obsidian Integration/app-proof-tracker.json` | Machine-readable app integration proof state | active data | Confirm it matches dashboard/checklist notes |
| GitHub Publish Workflow | `.github/workflows/npm-publish.yml` | Package publishing workflow | needs review | Confirm whether this belongs to this vault and what package it publishes |
| Codex Environment | `.codex/environments/environment.toml` | Local Codex environment metadata | active config | Confirm expected workspace settings |
| Obsidian Config | `.obsidian/*.json` | Vault behavior and plugin configuration | active config | Back up before broad plugin/config edits |

## Dependency Code

These are installed dependencies. Do not edit them as personal source code unless intentionally patching or replacing a plugin:

- `.obsidian/plugins/dataview`
- `.obsidian/plugins/obsidian-excalidraw-plugin`
- `.obsidian/plugins/obsidian-git`
- `.obsidian/plugins/omnisearch`
- `.obsidian/plugins/table-editor-obsidian`
- `.obsidian/plugins/templater-obsidian`

## Candidate External Codebases To Confirm

These are known from prior work or project memory, but should be verified before treating them as current:

| Candidate | Remembered Path | Why It Matters | Confirmation Needed |
|---|---|---|---|
| Shared Obsidian Vault | `C:\Users\rappd\OneDrive\Desktop\ObsidianVault` | Older or parallel skill library location | Confirm whether it is legacy, mirror, or still active |
| Playground Sync Vault | `C:\Users\rappd\My Drive\INBOX\AI Learning\sync-playground-laptop` | Sync target from `sync-all.py` | Confirm it should be overwritten by core library sync |

## Source Note Template

Create one source note per important codebase using this structure:

```markdown
---
type: source
source_app: local
source_url:
source_id:
captured_at: 2026-06-17
status: active
project:
tags:
  - source-code
---

# Codebase Name

## Purpose

## Canonical Location

## Main Entry Points

## How To Run

## How To Test

## How To Deploy Or Export

## AI Working Rules

## Latest Proof

## Open Questions
```

## Integration Checklist

- [ ] Create a source note for DOV Library Tools.
- [ ] Confirm whether deprecated Polaris Markdown history should be archived or deleted.
- [ ] Confirm whether `ObsidianVault` is legacy or a live mirror.
- [ ] Confirm whether playground sync overwrites are intentional.
- [ ] Link each confirmed codebase to the relevant project hub.
- [ ] Add run/test/deploy proof for each active codebase.
