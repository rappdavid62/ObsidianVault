# Library — The Single Source of Truth for All AI

**This folder (and the atomic notes within) is the canonical, living source of truth for every AI interaction you have. REINFORCED + EXPANDED 2026-06-12 with full SNF, career, health, and systems coverage.**

All skills, prompts, protocols, contexts, and system knowledge for Grok, Claude, ChatGPT, local models, Cursor, phone, etc. live here or are directly derived from here.

Everything else is a **derivative**:
- Big compiled files in `Prompt-Library/` (legacy full-bundle snapshots for convenience; do not edit as primary)
- `~/.grok/skills/` (live synced copies for this CLI — generated from here)
- Claude Projects / ChatGPT customs / Cursor rules (emitted from here via the emitter tools)
- Phone notes (via export-for-phone.py)
- Any chat history or one-off prompts (should be folded back into atomic notes here when useful)

## Core Principles

- **Atomic**: One skill/prompt = one note when possible. Easier to link, version, query, compose, and maintain.
- **Structured**: Every note follows the [[SCHEMA]] and uses values from the [[Dictionary]] (controlled vocabulary for type, domain, energy, tags, compatible_with, etc.).
- **Ubiquitous**: Designed to be emitted cleanly into *any* AI (Grok, Claude, GPT, local models, phone, etc.).
- **Observable & Auditable**: Use Dataview in the Hubs. The Library Gardener skill + emitter `--validate` keep it healthy.
- **State Not Fate aligned**: Low-friction, proof-oriented, energy-aware, restartable, external memory over internal state.

## Current Structure

- **Skills/** — Actionable, repeatable, agentic capabilities (e.g. daily-job-search, low-energy-execution, mvd-anchors, floor-wins, prs-safety-check, snf-proof-registration, snf-hope-activation, library-gardener, etc.).
- **Prompts/** — Lighter one-shot or command-style (the classic David 12 live here as atomic notes).
- **Protocols/** — Universal command frameworks (`thoroughness-protocol` /tp, `council-strategy` /council, expert lanes).
- **Contexts/** — Persistent background (master-bio, status templates, etc.).
- **Dictionary.md** — The controlled vocabulary. **Single source of truth for allowed values**. All new notes must use values from here.
- **SCHEMA.md** — The structural contract. Every note must follow this.
- **Hubs/00-Hub.md** — Living dashboard with Dataview. Start here for discovery.
- **Tools/** — The "ubiquity layer":
  - `emit-skill.py` + PowerShell wrapper (multi-skill, --daily, --favorites, energy-based packs, --validate against Dictionary, --clip, --with-master).
  - `build-master-context.py` — Combines master-bio + protocols + selected skills + status placeholder into one powerful injection block.
  - `export-for-phone.py` — Generates phone-optimized `Mobile-Favorites.md`.
  - `sync-to-grok.py` — Keeps high-value skills live in `~/.grok/skills/`.
- **How-to-Use-Ubiquitously.md** — Detailed patterns for every environment.
- **README.md** (this file) — The declaration that this is the source of truth.

## Daily / Weekly Workflow (to keep Obsidian as the Source of Truth)

1. Update your status block / trackers in Obsidian.
2. Run the emitter for the relevant pack (`skill --daily` or `skill --favorites` or `python build-master-context.py --daily`).
3. Paste the emitted block + your current status into whatever AI you're using today (Grok, Claude, GPT, local, phone, Cursor, etc.).
4. After the session, fold useful output, new patterns, or corrections back into the relevant atomic note(s) here.
5. Periodically run the Library Gardener skill (it now explicitly audits against the Dictionary).

## Maintenance

- The **Library Gardener** skill is the official meta-process for keeping everything sharp, atomic, dictionary-compliant, and actually useful.
- Never edit the big compiled files in `Prompt-Library/` as primary sources. They are snapshots.
- When your life changes (new job target, new energy realities, new 5-year vision details), update the relevant notes here first.

This is your external prefrontal cortex and long-term memory for **all AI**. Keep it in this vault. Emit from here. Everything else is temporary.

**Everything starts and ends here. This is the universal truth.**

---

*Maintained by the Library Gardener skill. Last major update: consolidated all prompts here as the single source of truth.*
