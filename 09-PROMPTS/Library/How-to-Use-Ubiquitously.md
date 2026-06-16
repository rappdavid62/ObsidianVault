---
type: guide
name: how-to-use-ubiquitously
domain: [meta, library]
tags: [guide, ubiquity, onboarding]
last_reviewed: 2026-06-08
---

# How to Use This Skill & Prompt Library Ubiquitously

**Obsidian (this Library) is the single source of truth for all AI you talk to.**

The goal is frictionless injection of high-quality, consistent, energy-aware, State-Not-Fate-aligned context into *any* model on *any* device.

## Core Pattern (works everywhere)

1. Keep your live status block / trackers up to date in Obsidian.
2. Use the emitter tools (or direct copy) to pull the relevant atomic notes.
3. Paste the emitted block(s) + your current status into the AI.
4. After the conversation, fold anything useful back into the Library (new notes, improvements to existing ones, updated examples).

This turns every AI into "you + your full Library loaded."

## 1. Inside Obsidian (best for discovery, linking, and maintenance)

- Start at the [[Hubs/00-Hub]] — Dataview tables by domain, energy, recently reviewed, low-energy favorites, etc.
- Use graph view and search to find related skills.
- The Library is designed to be read and edited here. Atomic notes + links + Dataview = powerful.

**Recommended plugins for maximum power** (if not already installed):
- Dataview (essential for the Hub)
- Templater or QuickAdd (for fast creation of new skills using the schema + Dictionary)
- Buttons / Commander (for one-click "emit this" actions)
- Git (for versioning the entire Library)

## 2. Command Line / Desktop Terminal (best for any chat on this machine)

The `Tools/` folder contains the main "ubiquity layer".

```powershell
# Recommended: add this to your PowerShell profile once
function skill { & "C:\Users\rappd\OneDrive\Desktop\ObsidianVault\09-PROMPTS\Library\Tools\emit-skill.ps1" @args }

# Then from anywhere:
skill --daily --clip          # full daily pack, copied to clipboard
skill --favorites             # broader high-value pack
skill daily-job-search low-energy-execution --with-master
skill --search "job low"      # discover
skill --validate mvd-anchors  # check against Dictionary
```

The emitter outputs clean, ready-to-paste Markdown blocks. It strips Obsidian-specific syntax and adds helpful headers.

**Daily recommended flow on desktop**:
1. Update your status block.
2. `skill --daily --clip`
3. Paste into whichever AI you're using today (Grok, Claude, GPT, local, etc.).
4. After the chat, update the relevant Library notes with what worked.

## 3. Phone / On the Go (true mobile ubiquity)

1. Periodically run:
   ```powershell
   python export-for-phone.py
   ```
   This generates `Mobile-Favorites.md` (or specify your own path).

2. The file syncs via OneDrive.

3. On your phone: open the file → long-press the skill you need → Copy → paste into any chat app.

Keep a small "Daily Use" section at the top of Mobile-Favorites.md with your current top 5–7 skills.

## 4. Other AI Frontends

- **Claude Projects**: Upload the whole `Library/` folder (or key subfolders) as project knowledge. Or paste emitted blocks + status at the start of conversations.
- **ChatGPT Custom GPTs / GPTs with memory**: Use the emitted full context as the core of your custom instructions. Update periodically from the Library.
- **Cursor / Windsurf / other IDEs**: Point `.cursorrules` or project rules at key notes (especially master-bio + relevant skills). Or use the emitter to generate a rules block.
- **Local models / SillyTavern / etc.**: Use the emitter to build system prompts or lorebook entries. The plain Markdown + frontmatter format works well.
- **NotebookLM**: Upload selected folders or the whole Library for synthesis and "podcast" overviews of your own system.

**Strong general pattern for any web LLM**:
```
You are operating from my personal skill & prompt library.
The canonical source of truth lives in my Obsidian vault at 09-PROMPTS/Library/ (synced via OneDrive).

Relevant skill(s) for this conversation:
[paste one or more emitted skills here]

My current status:
[paste your live status block + one non-negotiable]

Follow the skill instructions exactly. Bottom line first. Be realistic about my current energy and constraints. Use values and language from the Dictionary when relevant.
```

## 5. This Grok CLI Environment (deep integration)

- High-value skills are kept in sync with `~/.grok/skills/` (see `sync-to-grok.py`).
- They become real, description-driven, auto-triggerable skills in this environment.
- You can say things like:
  - "Use the library version of snf-hope-activation with my current status"
  - "Emit a daily pack including mvd-anchors and floor-wins"
  - Or just describe what you need — the agent can read the vault directly.

The emitter here is especially powerful because it can combine with the full local file system and tool use.

## 6. Keeping Obsidian as the Source of Truth

- **Never** treat big compiled files in `Prompt-Library/` as the place you do ongoing work. They are legacy full-bundle exports.
- After any useful session with *any* AI, bring the improvements back into the atomic Library notes.
- Run the Library Gardener skill regularly (it now explicitly audits against the Dictionary).
- When your life situation changes (new job target, new energy realities, new 5-year vision details), update the relevant notes here first.

## Quick Reference — Most Common Daily Injections

- Always consider: `thoroughness-protocol` (/tp) + your current status.
- Low energy / collapse days: `low-energy-execution` + `mvd-anchors` + `floor-wins`.
- Job work: `daily-job-search` + `apply-today` + `resume-tailoring` + master-bio.
- Social / communication: `social-calibration`.
- Big decisions: `council-strategy` + relevant expert lanes.
- Self-maintenance of the system: `library-gardener`.

All of the above are available via the emitter tools or direct from the Hub.

This is your external brain for every AI. Keep it in Obsidian. Emit from here. Everything else is temporary.