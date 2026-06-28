---
type: guide
name: codex-instructions
domain: [meta, library]
energy: any
compatible_with: [codex, all]
version: 1
last_reviewed: 2026-06-28
tags: [guide, codex, integration, skills]
---

# Codex Instructions

## Local Execution Environment

Codex is the local agent goal-running framework.

- Working directory: `C:\ROOT_OBSIDIAN\DOV`
- Configuration directory: `.codex/`

## Core Integration Rules
- Goal logs, implementation decisions, blockers, and output links must be documented in `00-CAPTURE/App Captures/` with:
  ```markdown
  source_app: Codex
  source_id: <goal-or-thread-id>
  captured_at: <timestamp>
  ```
- Before beginning execution, load the master context rules via `.cursorrules` or read the latest context from `09-PROMPTS/Library/Tools/master_context_latest.txt`.
- When completing a task, write back any durable improvements or new templates to the Obsidian vault rather than storing them in temporary logs.
