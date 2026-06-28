---
type: guide
name: antigravity-instructions
domain: [meta, library]
energy: any
compatible_with: [antigravity, all]
version: 1
last_reviewed: 2026-06-28
tags: [guide, antigravity, integration, skills]
---

# Antigravity IDE Instructions

## Direct Workspace Integration

You are the Antigravity agent running locally inside the user's IDE environment with direct read/write access to the files.

- Path: `C:\ROOT_OBSIDIAN\DOV`
- Do not request clipboard copy/pastes or manual file uploads; read and write files directly using workspace tools.

## Core Behavior
- Treat the DOV Library (`09-PROMPTS/Library/`) as the canonical source of truth for all skills, prompts, and rules.
- Follow the schemas defined in `SCHEMA.md` and terms in `Dictionary.md`.
- End substantial work with what changed, what was verified, and the next smallest action.

## Auto-Sync Rule
- After creating, updating, or modifying any file inside `09-PROMPTS/Library/Skills/`, `Protocols/`, or `Prompts/`, you MUST execute the unified synchronization script `sync-all.py` to regenerate phone exports, update `.cursorrules` and other target platforms:
  ```powershell
  python "C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library\Tools\sync-all.py"
  ```
- Run `vault-health-check.py --write` to update the Second Brain Health Report.
