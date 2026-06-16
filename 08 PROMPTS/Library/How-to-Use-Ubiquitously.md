---
type: guide
name: how-to-use-ubiquitously
domain: [meta, library]
tags: [guide, ubiquity, onboarding]
last_reviewed: 2026-06-08
---

# How to Use This Skill & Prompt Library Ubiquitously

**Obsidian (this Library in the Laptop Sync vault) is the single source of truth for all AI.**

The goal: Your best thinking, protocols, and execution patterns are available **from any device, to any model, at any time** — with almost zero friction.

## Core Principle

The Library lives in this Obsidian vault as the single source of truth (atomic notes + frontmatter + Dataview + Dictionary for controlled vocab).

Everything else is **derivative**:
- Big compiled files in `Prompt-Library/` (legacy full-bundle snapshots)
- `~/.grok/skills/` (live sync for this CLI)
- Claude Projects / ChatGPT customs / Cursor rules (emitted from here)
- Phone notes (via `export-for-phone.py`)
- Any chat history or one-off prompts (fold back here when useful)

## Methods (from easiest to most powerful)

### 1. Inside Obsidian (best discovery + composition)

- Open the [[Hubs/00-Hub]]
- Search or browse by domain/energy/tags
- Read the note, copy what you need
- Use Templater/QuickAdd (future) for "Insert Skill as Context" or "New Skill from Dictionary"

### 2. Command Line / Desktop Terminal (best for any chat on this machine)

Use the tools in `Library/Tools/`:

```powershell
# Recommended: add to PowerShell profile
function skill { & "C:\Users\rappd\My Drive\INBOX\AI Learning\Laptop Sync\08 PROMPTS\Library\Tools\emit-skill.ps1" @args }

skill --daily --clip          # full daily execution pack + status placeholder
skill --favorites             # broader high-value collection
skill daily-job-search low-energy-execution --with-master
skill --validate mvd-anchors  # check against Dictionary
skill --search "job low"      # discover
```

The emitter outputs clean, ready-to-paste Markdown blocks (strips Obsidian syntax).

### 3. "Tell the model about the library" (most powerful, lowest friction long-term)

In any new chat:

```
You are operating from my personal skill & prompt library.
The canonical versions live in my Obsidian vault at:
08 PROMPTS/Library/ (Laptop Sync vault, synced via Google Drive).

Relevant skill(s) for this conversation:
[paste one or more emitted skills here]

My current status:
[paste your status block + one non-negotiable]

Use the skill's instructions exactly. Bottom line first. Be realistic about my energy and constraints. Use values and language from the Dictionary when relevant.
```

This pattern turns any model into "you with your full Library loaded."

### 4. Phone / On the Go

1. Run `python export-for-phone.py` (from the Tools folder).
2. The generated `Mobile-Favorites.md` syncs via Google Drive / OneDrive.
3. On phone: open the file → long-press the skill you need → Copy → paste into any chat app.

Keep a small "Daily Use" section at the top with your current top 5–7 skills.

### 5. This Grok CLI Environment (special integration)

- High-value skills are kept in sync with `~/.grok/skills/` via `sync-to-grok.py`.
- They become real, description-driven, auto-triggerable skills in this environment.
- You can say: "Use the library version of daily-job-search with my current status" or "Build a pack with mvd-anchors and floor-wins".
- The agent here can read the vault directly when helpful.

### 6. Other Tools

- **Claude Projects**: Upload the whole `Library/` folder (now includes complete SNF set: mvd-anchors etc.) + your current status + a couple of key notes as project knowledge. Or paste emitted blocks + status at the start of conversations. See Claude-Project-Instructions.md in Library root for the exact paste pattern + "reference Library as source of truth" rules.
- **Gemini (Google AI Studio / app / mobile)**: Paste Master Context block (from build-master-context.py) or Favorites at start of chat. Upload key files for long context. See Gemini-System-Prompt.md. Use phone export for mobile.
- **ChatGPT Custom GPTs / GPTs with memory**: Use the emitted full context as the core of your custom instructions. Update periodically from the Library.
- **Cursor / Windsurf / other IDEs**: Point `.cursorrules` or project rules at key notes (especially master-bio + relevant skills). Or use the emitter to generate a rules block.
- **Local models / SillyTavern / etc.**: Use the emitter to build system prompts or lorebook entries. The plain Markdown + frontmatter format works well.
- **NotebookLM**: Upload selected folders or the whole Library for synthesis and "podcast" overviews of your own system.

## Recommended Daily/Weekly Patterns

- **Morning (on desktop)**: Update status block → `skill --daily --clip` → paste into main AI for the day.
- **When stuck or on phone**: Open Mobile-Favorites.md → grab the relevant skill (usually low-energy-execution + mvd-anchors + thoroughness-protocol + one domain skill).
- **Big decisions**: `/tp` + `/council` + the relevant expert lanes from the Library.
- **Library maintenance**: Run the `library-gardener` skill (weekly or after big sessions). It now explicitly audits against the Dictionary.

## Anti-Patterns

- Don't treat the big compiled files in `Prompt-Library/` as the place you edit day-to-day. They are legacy snapshots.
- Don't collect skills as a hobby. The rule from the original David library still applies: pick one, run it, save useful output, take real-world action.
- Don't let the library get stale. `last_reviewed` and `version` exist for a reason. Use the Dictionary for consistency.

The system is only as good as your willingness to keep the canonical atomic notes in this vault accurate and actually use the emit/injection patterns.

**This Library in the Laptop Sync vault is the universal truth for all AI.** 

---

*See [[../Library/README]] for the full declaration and [[../Library/Dictionary]] for the controlled vocabulary.*