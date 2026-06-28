---
Status: Active
Primary Deployment Target: AI Infrastructure
Expected Use Case: Operating rules for AI tools working with David’s vault, files, projects, prompts, and second brain.
Archive or Active: Active
Supersedes: 08-TECH-AND-AI/AI_SYSTEM/SKILL.md
Replaced By:
Canonical Home: Meta/AI Command Layer.md
Related Files:
  - Meta/Master Context.md
  - Meta/System Governance.md
  - Meta/AI Handoff Summary.md
Last Reviewed: 2026-06-22
---

# AI Command Layer

## Bottom Line

This is the command file for any AI working on David’s vault.

## Tool / Source Honesty

Do not claim access to David’s computer, phone, Obsidian vault, Gmail, Drive, GitHub, browser, prior chats, or files unless that access is actually available in the current session.

If the source is missing, ask for one of:

- pasted content
- uploaded file
- folder tree
- zip
- GitHub repo access
- Google Drive access
- PowerShell output

## Canonical Context Files

Read these first when available:

1. `Meta/Master Context.md`
2. `Meta/System Governance.md`
3. `Meta/Vault Master Index.md`
4. `Meta/Active Projects Map.md`
5. `Meta/Vault Cleanup Queue.md`
6. `09-PROMPTS/Library/Hubs/00-Hub.md`

## Canonical Skill Layer

The reusable skill layer is:

```text
C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library
```

Use it for ChatGPT, Claude, Gemini, Grok, Codex, Cursor, local models, phone copy/paste, and any future AI program.

Treat `09-PROMPTS/Prompt-Library/` and generated packs as historical or derivative unless a note explicitly says otherwise.

When a session discovers a better reusable behavior, fold the durable part back into `09-PROMPTS/Library/Skills`, `09-PROMPTS/Library/Prompts`, or `09-PROMPTS/Library/Contexts`, then regenerate exports.

For broad vault monitoring, run `09-PROMPTS/Library/Skills/second-brain-control-loop.md`.

For file cleanup, source-truth drift, private-boundary checks, and cleanup queue work, run `09-PROMPTS/Library/Skills/vault-cleaner.md`.

## Project Classification

Classify every request before acting:

- setup problem
- source-of-truth problem
- prompt problem
- code/build problem
- sync problem
- file organization problem
- research problem
- deployment problem
- personal workflow problem
- privacy/security problem

Then identify the real bottleneck:

- missing source
- bad prompt
- wrong tool
- unclear project
- stale file
- memory contamination
- local access limitation
- overcomplicated workflow

## Response Contract

Use this default response format:

1. Bottom line
2. What this does
3. Why it matters
4. Step count
5. Steps
6. Next step
7. Estimated time
8. Risk / source honesty

## File Creation Rule

Before creating any new durable file, apply `Meta/System Governance.md`:

- assign one Primary Deployment Target
- check for existing canonical home
- mark lifecycle status
- link related files instead of duplicating full concepts

## Privacy Rule

Private/local-only material belongs in `_PRIVATE/`.

Adult/smut/roleplay material belongs in `_PRIVATE/SMUT/`.

Do not quote, summarize, expose, or classify private/adult content in detail unless David explicitly asks.

Before any commit or push, check `.gitignore` and `git status`.

## Git Safety Rule

Before any commit, push, delete, move, or mass rename, inspect:

```powershell
git status
git branch --show-current
git remote -v
git log -1 --oneline
```

Explain what is modified, untracked, deleted, safe, risky, and the next command.

Do not push private material.

Do not rewrite history unless David explicitly asks.

## Anti-Overbuild Rule

Do not create dashboards, MOCs, command layers, or indexes unless they solve a real navigation or execution problem.

Prefer one useful canonical file over five decorative files.
