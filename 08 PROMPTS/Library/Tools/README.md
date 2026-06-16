# Library Tools — The Ubiquity Layer (Laptop Sync Vault - Universal Truth)

These scripts make the Obsidian Library (the single source of truth in this Laptop Sync vault) usable from *anywhere* and *any* AI.

The philosophy is simple:
- Obsidian Library = canonical, versioned, queryable, atomic source of truth for all AI.
- These tools = the "emit / export / sync" layer that turns the Library into something you can drop into any chat, IDE, or device with minimal friction.

## Core Tools

### emit-skill.py (and .ps1 wrapper) — The daily workhorse

The most important tool for day-to-day use.

**Key commands:**
- `python emit-skill.py --daily --clip` (or via the .ps1 wrapper)
- `python emit-skill.py --favorites --clip`
- `python emit-skill.py daily-job-search low-energy-execution --with-master`
- `python emit-skill.py --validate mvd-anchors` (checks against the Dictionary)
- `python emit-skill.py --search "job low"`

It supports:
- Multiple skills at once
- --daily (core low-energy execution pack)
- --favorites (broader high-value collection)
- Automatic and explicit validation against the Dictionary
- --clip on Windows
- Clean, ready-to-paste output with minimal Obsidian noise

**Recommended alias** (add to PowerShell profile):
```powershell
function skill { & "C:\Users\rappd\My Drive\INBOX\AI Learning\Laptop Sync\08 PROMPTS\Library\Tools\emit-skill.ps1" @args }
```

Then from any terminal: `skill --daily --clip`

### build-master-context.py — The power move for serious sessions

Builds a complete, high-signal injection block that combines:
- Master bio / core identity
- Core protocols (thoroughness-protocol, council-strategy)
- Selected skills
- A clear status block placeholder

Usage:
```powershell
python build-master-context.py --daily --clip
python build-master-context.py --skills mvd-anchors,floor-wins,prs-safety-check
```

This is the best way to give any AI (Claude, GPT, local, Cursor, etc.) a strong "you + your full Library" context in one go.

### export-for-phone.py — Mobile ubiquity

Generates a single clean `Mobile-Favorites.md` (or custom path) containing the most useful skills in a format that's easy to open and copy on a phone.

```powershell
python export-for-phone.py
```

Open the resulting file on your phone (via Google Drive) and you have a portable "quick copy" version of your best tools.

### sync-to-grok.py — Live integration with this Grok environment

Exports selected atomic notes from the Library into real `~/.grok/skills/<name>/SKILL.md` format.

This is how the best skills become native, description-driven, auto-triggerable skills inside this Grok CLI.

```powershell
python sync-to-grok.py daily-job-search --output-dir "C:\Users\rappd\.grok\skills"
```

Run this (or a wrapper) after you improve or create important skills.

## How These Tools Support "Obsidian as Source of Truth"

- You edit only in the Library (atomic notes + Dictionary + SCHEMA).
- The tools generate clean, consistent, version-aware output for other systems.
- After using something in another AI, you bring improvements back into the atomic notes here.
- The Library Gardener skill + emitter `--validate` keep everything consistent with the Dictionary.

## Recommended Daily Flow

1. Update your status / trackers in Obsidian.
2. `skill --daily --clip` (or `build-master-context.py --daily --clip` for bigger sessions).
3. Paste into whatever AI you're talking to today.
4. After the session, update the relevant Library notes with what actually worked.

This is how Obsidian (Laptop Sync vault) becomes the real brain, and every other AI becomes a temporary, well-informed executor.

## Future / Nice-to-Haves (if you want them)

- More sophisticated batch context builders (e.g., "build pack for job search today")
- Direct integration with other tools (e.g., auto-updating a Claude Project knowledge base)
- Obsidian Templater/QuickAdd commands that call these scripts or insert emitted blocks
- A small web UI or Tauri app that sits on top of the Library for even lower friction

For now, the current set of tools + the atomic Library structure + the Dictionary already gives you an extremely strong "source of truth + ubiquitous access" system with this vault as the universal truth.

Use the Library for truth. Use the tools for access. Keep the loop closed.
