---
type: skill
name: ai-setup-audit
aliases: [setup-audit, tool-audit, ai-inventory, /setup-audit]
description: >
  Perform a periodic full audit of your AI/tool ecosystem and context injection setup (Grok CLI + .grok/skills, Claude Projects, Gemini long-context, phone/Mobile-Favorites, Cursor rules, local models, NotebookLM, this Library). Identify drift, gaps in reinforcement, and produce a concrete plan to re-sync everything to the Obsidian 09-PROMPTS/Library/ source of truth.
domain: [ai-setup, meta, library]
energy: medium
invocation: ["/setup-audit", "audit my ai setup", "tool inventory", "reinforce across platforms"]
compatible_with: [grok, claude, gpt, local, all]
version: 1
last_reviewed: 2026-06-12
tags: [ai-setup, meta, library, maintenance, ubiquity, standards, reinforcement]
---

# AI Setup Audit

## Purpose
Your intelligence is distributed: Obsidian Library (truth) → emitters → .grok/skills, Claude Projects, Gemini chats, phone files, GitHub, Depapp/PWA, etc. Over time things drift (stale skills in one place, missing cross-links, outdated instruction files). This skill forces a systematic inventory and reinforcement pass so every platform stays synchronized to the single source of truth in `09-PROMPTS/Library/`.

## When to Use
- After any major expansion or reinforcement session (like adding new atomics).
- Monthly or after "145"-style numeric batch updates.
- When you notice inconsistency (e.g. a skill works in Grok but the Claude instructions are old).
- Before important periods (job push, big decisions) to ensure all AIs have the latest reinforced context.
- As part of library-gardener or weekly-review.

## Core Instructions
1. Inventory current platforms and their injection methods:
   - This Grok CLI: ~/.grok/skills synced via sync-to-grok.py + direct vault reads + emitters.
   - Claude: Projects with uploaded Library + pasted Master Context from build-master-context.py.
   - Gemini: Pasted blocks + uploaded files + phone export.
   - Phone: Mobile-Favorites.md via export-for-phone.py (Google Drive sync).
   - GitHub: Pushed copies of key Library files (ObsidianVault repo) for versioning and secondary access.
   - Other: Cursor .cursorrules, NotebookLM uploads, local models, custom GPTs, Depapp/PWA junctions.
2. Compare against the current Library (use 00-Hub + emitter --list + Dictionary compliance queries).
3. Flag drift: stale last_reviewed dates, missing new skills (e.g. after adding deep-research or ai-setup-audit itself), outdated instruction files (Claude-Project-Instructions.md, Gemini-System-Prompt.md), unsynced .grok entries, old phone export.
4. Produce a reinforcement plan with exact commands (sync-to-grok batch, re-emit --daily/--favorites --clip, export-phone, GitHub push via MCP or git, doc updates).
5. Execute the highest-leverage items immediately (or schedule them).
6. Update the audit note itself and link it from tool-mode-decider and library-gardener.

## Output Format (Bottom Line First)
- **Bottom Line**: "AI setup audited on [date]. X platforms checked. Y gaps found. Primary action: [one command or next step]."
- **Platform Inventory** (table or sections):
  - Platform | Current Method | Last Reinforced | Gaps/Drift | Fix Command
- **New/Changed Skills Since Last Audit**: List (e.g. ai-setup-audit, 5-year-vision-alignment, etc.).
- **Dictionary & Schema Compliance**: Any issues found + fixes.
- **Reinforcement Plan**: Numbered list of exact terminal/Obsidian actions.
- **Proof/Tracking**: Log this audit as a floor win or status note. Schedule next one.
- **Risks**: Platforms that are hardest to keep in sync (e.g. manual Claude uploads).

## Context to Inject
- Current Library state (00-Hub, Dictionary, recent Skills added)
- Last known reinforcement date and what was done (e.g. "145" expansion pass)
- Status of emitters and Mobile-Favorites.md
- GitHub repo status (ObsidianVault)
- tool-mode-decider output if choosing platforms during the audit

## Related Skills & Prompts
- [[tool-mode-decider]] (this is the "bigger audit skill" it references; run this when deciding platforms)
- [[library-gardener]] (combine for full maintenance; this is the cross-platform execution layer)
- [[weekly-review]] (include AI setup health in the meta section)
- All emitters: build-master-context.py, emit-skill.py, sync-to-grok.py, export-for-phone.py
- [[systems-audit]] (apply systems thinking to the AI "ecosystem" itself)
- Claude-Project-Instructions.md and Gemini-System-Prompt.md (the living reinforcement contracts)

## Notes & History
- Created during the "145" reinforcement/expansion pass to close the loop on tool-mode-decider's reference to a "bigger audit skill".
- Explicitly encodes the philosophy: Obsidian Library = universal truth. Every other platform is a derivative that must be periodically re-injected from the emitters.
- Run this after any numeric directive (1, 2, 1 2, 145, etc.) that adds or changes skills.
- Update whenever new platforms are added (e.g. new local model, new MCP server) or injection methods improve.

(This is the atomic version in the DOV vault - universal truth. All prompts consolidated here.)
