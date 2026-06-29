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
| ChatGPT | Uploaded files, Custom GPT instructions, or pasted emits | `ChatGPT-System-Prompt.md`, `README.md`, `Hubs/00-Hub.md`, `Mobile-Favorites.md` | Turn durable improvements into Library note edits, not chat-only memory |
| Antigravity IDE | Direct workspace file-system reads | `Antigravity-Instructions.md`, direct vault files, `.cursorrules` | Read/write files directly; run `sync-all.py` on changes to propagate |
| Codex | Local goal runs and env toml config | `Codex-Instructions.md`, `_Meta/AI Handoff Summary.md`, `Hubs/00-Hub.md` | Log task summaries to `00-CAPTURE/App Captures/` with source_app: Codex |
| Grok Build | Native skills in `~/.grok/skills` | `Grok-Build-Instructions.md`, sync-all output from DOV Library | Edit DOV source note, then resync |
| Claude | Project instructions plus uploaded Library files | `Claude-Project-Instructions.md`, `master_context_latest.txt`, and core skills | Fold useful Claude outputs back into atomic notes before regenerating exports |
| Gemini | System prompt, native skills, or uploaded files | `Gemini-System-Prompt.md`, `master_context_latest.txt`, `Mobile-Favorites.md` | Same as Claude: no separate Gemini-only skill fork |
| Cursor / IDE agents | Repo instructions or pasted context | `AI Handoff Summary.md`, `/tp`, `/brain`, task skill | Keep code/project facts separate from vault source-truth notes |
| Phone | Generated phone export | `Mobile-Favorites.md` | Capture rough notes, then promote durable pieces in DOV |
| Local models | Pasted context window or local retrieval folder | `master_context_latest.txt` plus selected skills | Mark model output as unverified until checked against files |
| Obsidian | Direct vault notes | `_Meta/Second Brain Operations Dashboard.md` and this matrix | DOV remains the source of truth |


## Codex Plugin Routing

Use plugin/app tools as task-specific retrieval or action surfaces. They do not become new sources of truth. Capture durable outputs back into DOV.

| Plugin / app surface | Route through | Capture target | Proof status |
|---|---|---|---|
| GitHub | `Apps - GitHub.md`, repo issue/PR/deploy notes | `00-CAPTURE/App Captures/` or project source note | Complete in tracker, but verify current repo/session before claims |
| Google Drive | `Apps - Google Drive.md`, Drive file summary notes | `00-CAPTURE/App Captures/` or source note | Complete in tracker, but connector access is session-specific |
| OpenAI Developers | `Apps - OpenAI Developers.md`, API/build decision notes | `00-CAPTURE/App Captures/` or project source note | Deferred on demand |
| Life Science Research | `Apps - Life Science Research.md`; use `life-science-research:research-router-skill` for broad questions | Evidence summary note | Deferred low priority until an active research task |
| Scite | `Apps - Scite.md` | Citation/evidence check note | Deferred on demand |
| Netlify | `Apps - Netlify.md`; use `netlify:netlify-ai-gateway` before model choices in Netlify AI work | Deploy or AI gateway decision note | Complete for app proof, but live deploy/model support needs current verification |
| Product Design | `Apps - Product Design.md`; `product-design:url-to-code` requires Product Design get-context and source-capture proof first | Design direction or build note | Deferred on demand |
| Build Web Apps | `Apps - Build Web Apps.md` and relevant frontend skills | App build decision/project note | Deferred low priority until a build task |
| Build Web Data Visualization | `Apps - Build Web Data Visualization.md` and data-viz skills | Chart/data decision note | Deferred low priority until a visualization task |

When a plugin session produces reusable instructions, promote them to `09-PROMPTS/Library/Skills/`, `Prompts/`, `Protocols/`, or `Contexts/`. When it produces one-off evidence, store it in the relevant app capture or project note.

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
6. Update `_Meta/Vault Cleanup Queue.md` only for unresolved risks.

## Guardrails

- Do not claim any app, connector, live repository, Gmail, Drive, browser, or vault state was checked unless it was checked in the current session.
- Do not move private or adult material without explicit approval.
- Do not create a second canonical Library in Claude, Gemini, Grok, ChatGPT, Cursor, or a phone note.
- Generated packs are transport surfaces. Atomic notes are source truth.
