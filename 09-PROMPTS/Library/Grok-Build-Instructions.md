---
type: guide
name: grok-build-instructions
domain: [meta, library]
energy: any
compatible_with: [grok, all]
version: 1
last_reviewed: 2026-06-28
tags: [guide, grok, integration, skills]
---

# Grok Build Instructions

## Sync and Execution

Grok utilizes the native generated skills directory `~/.grok/skills` which is updated via `sync-all.py`.

- Editing Surface: Edit only the canonical files inside `09-PROMPTS/Library/` inside Obsidian.
- Live Surface: Grok loads skills automatically from `~/.grok/skills/<name>/SKILL.md`.

## Core Behavior
- If Grok discovers or improves a skill during a coding or debugging run, it must instruct the user to update the canonical note in the Obsidian vault and run `sync-all.py` to regenerate the Grok version.
- Use Grok Build prompts for implementation work (git status, remote check, preflight branch verification).
