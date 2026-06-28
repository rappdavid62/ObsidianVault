---
type: system
status: active
created: 2026-06-17
updated: 2026-06-17
source_app: Codex
tags:
  - obsidian/integration
  - ai-setup
  - source-of-truth
  - skills
---

# Universal AI Integration Blueprint

## Bottom Line

Use this vault as the command center, not as a junk drawer. Important code stays in its real repo or build folder and is indexed here. Important skills live as atomic Markdown in `09-PROMPTS/Library`. Every AI, app, and device gets generated exports or capture notes from that source.

## Current Inventory Snapshot

- Primary vault: `C:\ROOT_OBSIDIAN\DOV`
- Integration hub: `08-TECH-AND-AI/Obsidian Integration`
- Canonical skill library: `09-PROMPTS/Library`
- Atomic skills: 27 files in `09-PROMPTS/Library/Skills`
- Protocols: 2 files in `09-PROMPTS/Library/Protocols`
- Library tools: `build-master-context.py`, `emit-skill.py`, `emit-skill.ps1`, `export-for-phone.py`, `sync-all.py`, `sync-to-grok.py`
- Mobile quick-copy surface: `09-PROMPTS/Library/Mobile-Favorites.md`
- Deprecated build notes: `08-TECH-AND-AI/BUILD` keeps Markdown history only; runnable Polaris artifacts were removed from active code.
- App integration proof files: `App Proof Dashboard.md`, `App Coverage Checklist.md`, `app-proof-tracker.json`
- Installed Obsidian plugin code exists under `.obsidian/plugins`, but it is dependency code, not personal source code.

## Source Of Truth Rules

1. Skills and prompts are canonical only in `09-PROMPTS/Library`.
2. Source code is canonical in its owning repo or build folder; this vault should store index notes, proof notes, runbooks, decisions, and links.
3. External app content enters through capture notes in `00-CAPTURE/App Captures` or source notes in `03-RESOURCES/Sources`.
4. Generated exports are disposable. If an AI improves a skill, the improvement must come back to the atomic note.
5. Public output must stay explicitly gated. Missing `publish: true` means private by default.
6. Secrets, API keys, private medical details, and credentials do not belong in emitted skill packs or public output.

## Integration Layers

| Layer | Purpose | Home |
|---|---|---|
| Capture | Bring useful external material into the vault | `00-CAPTURE/App Captures`, `03-RESOURCES/Sources` |
| Canonicalize | Turn captures into durable skills, prompts, decisions, source notes, or project hubs | `09-PROMPTS/Library`, `01-PROJECTS`, `08-TECH-AND-AI` |
| Emit | Send the right subset to an AI, device, or program | `09-PROMPTS/Library/Tools` |
| Prove | Verify that capture, metadata, linkback, and retrieval work | `App Proof Dashboard.md`, `App Coverage Checklist.md` |
| Review | Retire stale items, update versions, and close loops | `library-gardener`, daily/weekly reviews |

## Platform Distribution Map

| Target | What it should receive | Mechanism |
|---|---|---|
| ChatGPT / Codex | Master context plus selected skills and project files | `build-master-context.py`, `emit-skill.py`, direct vault reads |
| Claude / other LLM chats | Pasteable master context or selected skills | `emit-skill.py --daily`, `emit-skill.py --favorites` |
| Gemini / Grok style skill systems | Native generated skill folders | Controlled `sync-all.py` or `sync-to-grok.py` run |
| Cursor / local coding tools | Current master context and repo-specific instructions | `.cursorrules`, project hub, source notes |
| Phone / tablet | Small copy-paste skill pack | `export-for-phone.py`, `Mobile-Favorites.md` |
| GitHub / Netlify / CI | Project-specific code, deploy notes, incidents, and decisions | Source notes plus app capture notes |
| Google Drive / Docs / Sheets / Slides | Source summaries and linkback notes | App capture templates and connector notes |
| Browser / Chrome | Clips, app pages, URLs, and retrieval proof | Web clipper templates and app capture notes |

## Code Integration Rule

Do not paste every code file into a prompt library. For each important codebase, create or maintain a source note with:

- Repo or folder path
- Purpose
- Owner or project
- Main entry points
- How to run
- How to test
- How to deploy
- Current known risks
- Link to latest proof or QA result

The code itself remains in Git. The vault remembers what matters, why it matters, and how an AI should safely work with it.

## Skill Integration Rule

Every reusable AI behavior should become one atomic file in `09-PROMPTS/Library/Skills` or `09-PROMPTS/Library/Protocols`.

Required qualities:

- Clear trigger in `description`
- Plain Markdown body
- YAML frontmatter matching `SCHEMA.md`
- Related skills listed when composition matters
- Version and `last_reviewed`
- No private secrets

After real use, update the atomic skill first, then regenerate downstream copies.

## Controlled Sync Procedure

Use this when you intentionally want the library pushed outward:

1. Review changed skills and prompts in Obsidian.
2. Run validation for the changed skill or pack.
3. Generate the pasteable pack or mobile pack.
4. Only run `sync-all.py` when you want external writes to Gemini/Grok folders, other vaults, and `.cursorrules`.
5. Update proof notes after the target app successfully uses the exported material.

`sync-all.py` is an export tool, not a casual save button.

## First 7-Day Integration Sweep

- [ ] Create source notes for each active codebase: DOV tools and any current non-deprecated GitHub projects that matter.
- [ ] Fix any hardcoded old vault paths in high-use tools.
- [ ] Validate all 27 skills and 2 protocols against `SCHEMA.md`.
- [ ] Regenerate `Mobile-Favorites.md`.
- [ ] Build one current master context and verify it works in ChatGPT/Codex.
- [ ] Prove one app integration per day using the App Proof Dashboard.
- [ ] Mark anything generated, stale, or duplicate as archive instead of canonical.

## Definition Of Done

The integration is working when:

- You know where the real source of truth is for every important codebase and skill.
- Any major AI can receive the right context in under two minutes.
- Phone access works without digging.
- Every external app has at least one proof note showing capture, metadata, linkback, and retrieval.
- No private-only material leaks into public output or broad AI context by accident.

## Next Useful Build

Turn each row in `Source Code Registry.md` into a full source note with run command, test command, deployment surface, and latest proof.
