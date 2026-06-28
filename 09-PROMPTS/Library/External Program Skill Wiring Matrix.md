---
type: guide
name: external-program-skill-wiring-matrix
domain: [meta, library]
energy: any
compatible_with: [all, obsidian, phone, gpt, claude, local]
version: 1
last_reviewed: 2026-06-28
tags: [guide, integration, external-memory, standards, skills]
---

# External Program Skill Wiring Matrix

## Bottom Line

Every AI surface should point back to one source:

```text
C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library
```

Claude, Gemini, Grok, ChatGPT, Codex, Cursor, phone notes, and local models are output surfaces. The DOV Library is the editing surface.

## Core Command Set

| Command | Canonical note | Use when |
|---|---|---|
| `/brain` | `Skills/second-brain-control-loop.md` | Monitor, learn from, and improve the vault |
| `/vault-cleaner` | `Skills/vault-cleaner.md` | File placement, stale paths, privacy boundaries, cleanup queue |
| `/bootstrap` | `Prompts/bootstrap-session.md` | Start a new serious AI session |
| `/daily-execution` | `Prompts/daily-execution.md` | Build today's practical plan |
| `/priority-audit` | `Prompts/priority-audit.md` | Choose between too many active threads |
| `/council` | `Prompts/council-decision.md` plus `Skills/council-strategy.md` | Complex decisions |
| `/tp` | `Skills/thoroughness-protocol.md` | Non-trivial tasks needing rigor |
| `/low` | `Skills/low-energy-execution.md` | Low-energy, fog, collapse, restart |
| `/jobsearch` | `Skills/daily-job-search.md` | Job-search execution |
| `/social` | `Skills/social-calibration.md` | Messages, boundaries, social reading |
| `/tcouncil` | `Skills/tech-council.md` | Tool, app, and platform decisions |

## Program Wiring

| Surface | Best input method | What to load | Writeback rule |
|---|---|---|---|
| Codex | Local files in DOV plus emitted skill blocks | Read `Meta/AI Handoff Summary.md`, `Hubs/00-Hub.md`, then the task skill | Patch DOV notes directly only when asked or when completing an active vault task |
| ChatGPT | Uploaded files, pasted emits, or Project knowledge | `README.md`, `Hubs/00-Hub.md`, `Mobile-Favorites.md`, and task skills | Turn durable improvements into Library note edits, not chat-only memory |
| Claude | Project instructions plus uploaded Library files | `Claude-Project-Instructions.md`, `master_context_latest.txt`, and core skills | Fold useful Claude outputs back into atomic notes before regenerating exports |
| Gemini | System prompt or first message plus uploaded files | `Gemini-System-Prompt.md`, `master_context_latest.txt`, `Mobile-Favorites.md` | Same as Claude: no separate Gemini-only skill fork |
| Grok | Generated `.grok/skills` output | `sync-to-grok.py` or `sync-all.py` output from DOV Library | Edit DOV source note, then resync |
| Cursor / IDE agents | Repo instructions or pasted context | `AI Handoff Summary.md`, `/tp`, `/brain`, task skill | Keep code/project facts separate from vault source-truth notes |
| Phone | Generated phone export | `Mobile-Favorites.md` | Capture rough notes, then promote durable pieces in DOV |
| Local models | Pasted context window or local retrieval folder | `master_context_latest.txt` plus selected skills | Mark model output as unverified until checked against files |
| Obsidian | Direct vault notes | `Meta/Second Brain Operations Dashboard.md` and this matrix | DOV remains the source of truth |

## Emit Commands

Run from PowerShell when a surface needs fresh context:

```powershell
python "C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library\Tools\emit-skill.py" --favorites --clip
python "C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library\Tools\emit-skill.py" second-brain-control-loop vault-cleaner --with-master --clip
python "C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library\Tools\build-master-context.py" --daily --clip
python "C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library\Tools\export-for-phone.py"
```

If clipboard access is unavailable, run the same commands without `--clip` and paste the terminal output manually.

## Learning Loop

1. Use the best current skill in the external program.
2. Capture better wording, better steps, or missed constraints.
3. Promote only durable improvements into `09-PROMPTS/Library`.
4. Validate the changed skill or prompt.
5. Regenerate mobile and external outputs.
6. Update `Meta/Vault Cleanup Queue.md` only for unresolved risks.

## Guardrails

- Do not claim any app, connector, live repository, Gmail, Drive, browser, or vault state was checked unless it was checked in the current session.
- Do not move private or adult material without explicit approval.
- Do not create a second canonical Library in Claude, Gemini, Grok, ChatGPT, Cursor, or a phone note.
- Generated packs are transport surfaces. Atomic notes are source truth.
