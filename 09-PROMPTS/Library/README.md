# Library — The Single Source of Truth for All AI

**This is the canonical, living source of truth for every AI system you interact with.**

Obsidian (specifically this `09-PROMPTS/Library/` folder) is the one place where all skills, prompts, protocols, contexts, and system knowledge are defined, versioned, audited, and maintained.

Everything else is a **derivative copy** or **temporary injection**:
- `~/.grok/skills/` → live sync for this Grok CLI (generated from here via `sync-to-grok.py`)
- Claude Projects, ChatGPT customs, Cursor rules → emitted from here
- Phone notes → generated via `export-for-phone.py`
- Any chat history or one-off usage → should flow back here when valuable

## Core Rules (to keep Obsidian as the Source of Truth)

1. **Edit here first** — Atomic notes in `Skills/`, `Prompts/`, `Protocols/`, `Contexts/`.
2. **Follow the SCHEMA** — Every note must match the structure in `SCHEMA.md`.
3. **Use the Dictionary** — All `type`, `domain`, `energy`, `tags`, `compatible_with` values must come from `Dictionary.md`.
4. **Emit, don't duplicate** — Use the Tools to generate clean blocks for other AIs instead of maintaining parallel copies.
5. **Fold improvements back** — After any useful session with any AI, update the relevant atomic note(s) here.
6. **Audit regularly** — Run the `library-gardener` skill. It now explicitly checks compliance with the Dictionary.

## Current Architecture

- **Skills/** — Repeatable, agentic capabilities (the "what to do" layer).
- **Prompts/** — Lighter, command-style or one-shot prompts (the classic David 12 live here as atomic notes).
- **Protocols/** — Universal operating frameworks (`/tp`, `/council`, expert lanes).
- **Contexts/** — Persistent background knowledge (master-bio, status templates, etc.).
- **Dictionary.md** — Controlled vocabulary (the "allowed values" for frontmatter). This is the single source for consistent tagging, querying, and validation.
- **SCHEMA.md** — The structural contract for every note.
- **Hubs/00-Hub.md** — Live dashboard with Dataview. This is your daily entry point.
- **Tools/** — The "ubiquity layer" that makes the Library usable from anywhere:
  - `emit-skill.py` + PowerShell wrapper (multi-skill, --daily, --favorites, --validate against Dictionary, --clip, --with-master).
  - `build-master-context.py` — Combines master-bio + protocols + skills + status placeholder into one powerful injection block.
  - `export-for-phone.py` — Generates a clean mobile-friendly favorites file.
  - `sync-to-grok.py` — Keeps selected skills live in this Grok environment.

## How to Feed This Into Any AI (the Ubiquitous Pattern)

**Best pattern (works with Grok, Claude, GPT, local models, Cursor, etc.):**

```
You are operating from my personal skill & prompt library.
The single source of truth lives in my Obsidian vault at:
09-PROMPTS/Library/ (synced via OneDrive).

Relevant skill(s) for this conversation:
[paste one or more emitted skills here, or the full block from build-master-context.py]

My current status:
[paste your latest status block + one non-negotiable]

Follow the skill instructions exactly. Bottom line first. Be realistic about my current energy and constraints. Use values from the Dictionary when relevant (domains, energy levels, etc.).
```

Use the emitter tools to generate the clean blocks:
- `skill --daily --clip` (or the Python version)
- `python build-master-context.py --daily --clip`

For this Grok CLI specifically: Many skills are kept in `~/.grok/skills/` and are natively available (you can say "use the library version of daily-job-search" or just describe what you need — the agent can read the vault directly when helpful).

## Daily Ritual (to keep Obsidian as the Source)

1. Update your status block / trackers in Obsidian.
2. Run the appropriate emitter (`--daily` for most days, `--favorites` for broader access).
3. Paste into whatever AI you're using today.
4. After the session, fold useful output, new patterns, or corrections back into the atomic notes here.
5. Periodically run `library-gardener` (it audits against the Dictionary and keeps everything sharp).

## Status

This Library is now the designated source of truth for all AI work. The old large compiled files in `Prompt-Library/` are legacy full-bundle snapshots and should not be treated as the primary source going forward.

All new skills, refinements, and context should be created or updated here first.

---

*Maintained by the Library Gardener skill. This note itself is part of the Library and should be kept accurate.*