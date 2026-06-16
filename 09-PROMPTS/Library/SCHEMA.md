---
type: meta
name: skill-prompt-schema
domain: [meta, library]
tags: [schema, standards]
last_reviewed: 2026-06-08
---

# Universal Skill & Prompt Schema (Obsidian + Ubiquitous)

This is the single source of truth for how every skill and prompt in this library is structured. The goal is **rigor + portability**.

Everything must be plain Markdown + YAML frontmatter so it works in:
- Obsidian (with Dataview, Templater, etc.)
- Any text editor
- Any LLM (by pasting the file or folder)
- This Grok environment (via file reads or export to `.grok/skills`)
- Claude Projects, Cursor, local models, phone notes, etc.

## Two Main Types

### 1. Skill (preferred for agentic / repeatable capabilities)

Use this when the thing has:
- A clear trigger description (so an AI can decide to use it automatically)
- Structured steps or rules
- Often benefits from being composed with other skills
- May have references, scripts, or output formats

**Required Frontmatter**

```yaml
---
type: skill
name: kebab-case-unique-name          # e.g. daily-job-search, thoroughness-protocol
aliases: [short, /invocations]        # optional, for human convenience
description: >
  One or two sentences that tell an AI *exactly when and why* to use this.
  This field is critical for auto-invocation (matches .grok SKILL.md style).
domain: [job, execution, social, research, meta, low-energy, ...]
energy: low | medium | high | any
invocation: ["/jobsearch", "daily job hunt"]   # natural language + slash forms
compatible_with: [grok, claude, gpt-4o, local, all]
version: 2
last_reviewed: 2026-06-08
tags: [job, daily, low-friction]
---
```

**Recommended Body Structure** (use headings so it is skimmable when pasted)

```markdown
# Skill Name (human readable)

## Purpose
One-sentence "what this does for me".

## When to Use
- Bullet conditions, including energy state, context, frequency.

## Core Instructions
The actual prompt content the model should follow. Be precise and opinionated.

## Context to Inject (if any)
- Current status block
- Specific files or previous outputs
- ...

## Output Format
- Bottom Line first
- Exact Next Action
- etc.

## Related Skills / Prompts
- [[other-skill]]
- [[supporting-prompt]]

## Notes & History
- What worked / didn't on which models
- Changes in this version
```

### 2. Prompt (lighter, one-shot or template style)

Use for things that are mostly "paste this block + my current data".

Frontmatter is similar but `type: prompt`.

Often shorter body. May still have `description` and `invocation` for discoverability.

## Ubiquity Rules (How to Use This Library From Anywhere)

1. **Inside Obsidian** — Use the Hub (Dataview tables), QuickAdd/Templater commands (to be built), or just `[[wikilink]]` + copy the note.

2. **Any LLM chat (Grok, Claude, ChatGPT, local, phone)**:
   - Best: Paste the entire note (or the relevant sections).
   - Better: Use one of the emit scripts in `Library/Tools/` to get a clean, model-optimized block.
   - Power move: Maintain a small "Master Context" note + the specific skill. Tell the model "You are operating under my personal skill library. Use the following skill exactly: [paste]".

3. **This Grok CLI environment**:
   - Skills can be read directly from the vault.
   - We will maintain a sync/export so high-value skills also appear in `~/.grok/skills/` with proper SKILL.md format.

4. **Composition**:
   - Skills should explicitly list related skills.
   - Meta-skills (like `/tp` Thoroughness Protocol or "Library Gardener") are encouraged.

5. **Maintenance**:
   - Every skill/prompt must have `last_reviewed` and `version`.
   - Use the "Library Gardener" meta-skill regularly.
   - When you improve something in a real session, come back and update the canonical note + bump version.

## Properties for Dataview / Queries (recommended)

In addition to the required frontmatter, add these when useful:

- `energy`
- `domain` (array)
- `last_used` (date, for "recently used" views)
- `success_rate` or qualitative notes in body
- `requires_status_block: true/false`

## Relationship to .grok/skills

- The `description` field is deliberately compatible with the `description` in `.grok/skills/*/SKILL.md`.
- We will keep a generator (or manual curated list) that turns selected Obsidian skills into real `.grok/skills` directories so they are live in this environment.
- Conversely, valuable skills discovered while using Grok should be back-ported into this Obsidian library as the source of truth.

## File Naming & Location

- `Library/Skills/<kebab-name>.md`
- `Library/Prompts/<kebab-name>.md`
- `Library/Protocols/` for the universal command protocols (`/tp`, `/council`, expert lanes, etc.)
- Keep the old big compiled files in `Prompt-Library/` as "full bundle" references if you ever want to upload an entire OS at once, but **do not edit them as the live version**.

This schema is designed to be both **human-editable in Obsidian** and **machine-injectable everywhere**.
