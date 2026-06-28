---
type: guide
name: library-readme
domain: [meta, library]
energy: any
compatible_with: [all, obsidian, phone, gpt, claude, local]
version: 3
last_reviewed: 2026-06-28
tags: [guide, onboarding, library, external-memory, standards]
---

# DOV Skill & Prompt Library

## Bottom Line

`C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library` is the canonical skill layer for every AI program and device.

Everything else is a derivative surface:

- ChatGPT, Claude, Gemini, Grok, Codex, Cursor, local models, and phone chats should receive emitted or copied material from this folder.
- `09-PROMPTS/Prompt-Library` is legacy bundle/reference material, not the daily editing surface.
- App-specific project instructions should point back here instead of becoming separate sources of truth.
- Improvements discovered in other programs should be folded back into these atomic notes.

## First Files

Read these in order when starting a serious session:

1. `Meta/Master Context.md`
2. `Meta/AI Command Layer.md`
3. `09-PROMPTS/Library/Hubs/00-Hub.md`
4. `09-PROMPTS/Library/External Program Skill Wiring Matrix.md`
5. `09-PROMPTS/Library/How-to-Use-Ubiquitously.md`
6. The relevant note from `Skills/`, `Prompts/`, `Protocols/`, or `Contexts/`

## Library Shape

- `Skills/` - repeatable capabilities with triggers, steps, and output formats.
- `Prompts/` - portable command prompts such as `/bootstrap` and `/daily-execution`.
- `Skills/Protocols/` - mirrored protocol copies kept for compatibility with older paths.
- `Contexts/` - reusable background context.
- `Hubs/00-Hub.md` - the main navigation and review surface.
- `Tools/` - emit, export, sync, and context-building scripts.
- `Dictionary.md` and `SCHEMA.md` - the rules for frontmatter and vocabulary.
- `Mobile-Favorites.md` - generated phone copy surface.
- `External Program Skill Wiring Matrix.md` - how external programs should receive this same skill layer.
- `Skills/second-brain-control-loop.md` - top-level monitor/learn/improve operator skill.
- `Skills/vault-cleaner.md` - safe file organization and cleanup skill.

## Daily Use

Recommended PowerShell alias:

```powershell
function skill { & "C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library\Tools\emit-skill.ps1" @args }
```

High-value commands:

```powershell
skill --daily --clip
skill --favorites --clip
skill second-brain-control-loop vault-cleaner --with-master --clip
skill bootstrap-session daily-execution --with-master --clip
skill --validate library-gardener
python "C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library\Tools\build-master-context.py" --daily --clip
python "C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library\Tools\export-for-phone.py"
```

## Core Portable Commands

- `/brain` -> `Skills/second-brain-control-loop.md`
- `/vault-cleaner` -> `Skills/vault-cleaner.md`
- `/bootstrap` -> `Prompts/bootstrap-session.md`
- `/daily-execution` -> `Prompts/daily-execution.md`
- `/priority-audit` -> `Prompts/priority-audit.md`
- `/council` -> `Prompts/council-decision.md` and `Skills/council-strategy.md`
- `/tp` -> `Skills/thoroughness-protocol.md`
- `/low` -> `Skills/low-energy-execution.md`
- `/jobsearch` -> `Skills/daily-job-search.md`
- `/social` -> `Skills/social-calibration.md`
- `/tcouncil` -> `Skills/tech-council.md`

## Maintenance Loop

Use `Skills/library-gardener.md` as the official review process.

Use `Skills/second-brain-control-loop.md` as the top-level operator when the task is broader than the prompt library alone.

Use `Skills/vault-cleaner.md` when the task involves file placement, source-truth drift, stale paths, privacy boundaries, or cleanup queue work.

The loop is:

1. Capture useful material into the vault.
2. Promote durable patterns into atomic Library notes.
3. Validate against `Dictionary.md` and `SCHEMA.md`.
4. Regenerate `Mobile-Favorites.md` and context exports.
5. Point external programs back to this folder.
6. Log unresolved cleanup in `Meta/Vault Cleanup Queue.md`.

## Source Honesty

Do not claim a connector, app, vault, browser, Gmail, Drive, GitHub, or local path was checked unless the current session actually checked it. If a source is unavailable, mark it plainly and ask for a paste, upload, folder tree, zip, connector access, or command output.

This Library is not supposed to be beautiful. It is supposed to make the next session smarter than the last one.
