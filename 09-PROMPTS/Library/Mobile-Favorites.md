# Mobile Favorites – Obsidian Skill & Prompt Library
# Generated for quick copy-paste on phone
# Source: 09-PROMPTS/Library (syncs via OneDrive)
# Tip: Prefix with /tp or /council when needed.


## tool-mode-decider
```
---
type: skill
name: tool-mode-decider
aliases: [tool-mode, which-tool, /toolmode, decide-tool]
description: >
  Given a task, decide the best AI/tool/setup to use (Grok CLI, ChatGPT Project, NotebookLM, local model, Obsidian + emit, etc.) and the right context/skill pack to load.
  Use when you have work to do and want to avoid context pollution or using the wrong hammer.
domain: [meta, execution, ai-setup]
energy: low
invocation: ["/toolmode", "what tool for this", "best way to do this task"]
compatible_with: [grok, claude, gpt, local]
version: 1
last_reviewed: 2026-06-12
tags: [meta, tools, ai-setup]
---
```

# Tool Mode Decider

## Purpose
Stop wasting cognitive energy and tokens by defaulting to "just paste everything into ChatGPT." Match the task to the right environment, context size, and skill injection method.

## When to Use
- Before starting any non-trivial piece of work (research, planning, writing, coding, job materials).
- When you feel decision fatigue about "where do I even do this?"

## Core Instructions
1. Clarify the exact task + constraints (energy today, need for persistence, privacy, speed, depth, collaboration).
2. Map to the best primary tool:
   - **This Grok CLI** (with synced skills): coding, rigorous execution, file system work, best-of-n, deep refactors, anything needing the full .grok toolset.
   - **ChatGPT Project or Claude Project**: long-term coaching, large context memory, the AI Life Coach Friend bundle.
   - **NotebookLM**: synthesis of many documents, "podcast" style overviews, studying your own materials.
   - **Obsidian + emit tools**: pure thinking, linking ideas, creating new atomic skills, daily notes, when you want to stay in your own knowledge graph.
   - **Local models**: privacy-sensitive or high-volume low-stakes tasks.
   - **PWA / custom tools** (State Not Fate app): daily anchors, PHQ-9, media consumption, floor tracking.
3. Decide what context/skill pack to load:
   - Master bio + current status block (almost always).
   - Specific skills (e.g. daily-job-search + low-energy-execution).
   - Full bundles only when the task justifies the context cost.
4. Output the exact "setup command": which tool + which files/skills to load + opening prompt.

## Output Format (Bottom Line First)
- **Bottom Line**: Recommended primary tool + why.
- **Context to Load**:
  - Required: master bio + status.
  - Skills/Prompts: list with brief why.
  - Bundles (if any).
- **Opening Prompt**: Suggested first message / system instruction.
- **Alternatives**: Second-best option and when you might switch.
- **Why Not the Others**: Brief anti-recommendations.

## Context to Inject
- The task description
- Current energy + any hard constraints (time, tokens, privacy)
- Recent status

## Related
- ai-setup-audit (the bigger periodic full ecosystem reinforcement audit skill)
- All the skills (this one decides which to load)
- The original "08_Tool_Mode_Decider.md"

## Notes & History
- This is a meta-skill that protects your attention and the quality of every other skill.
- Update as your tool landscape changes (new local models, new Obsidian plugins, new Grok features, etc.).

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)


## library-gardener
```
---
type: skill
name: library-gardener
aliases: [prompt-surgeon, maintain-library, library-maintenance]
description: >
  Maintain the health, atomicity, and usefulness of the entire Skill & Prompt Library.
  Use regularly (weekly or after major sessions) to review, improve, deduplicate, and keep the system rigorous.
domain: [meta, library]
energy: medium
invocation: ["library gardener", "review the prompt library", "prompt surgeon", "maintain skills"]
compatible_with: [grok, claude, gpt, local]
version: 1
last_reviewed: 2026-06-12
tags: [meta, maintenance, library]
---
```

# Library Gardener (Prompt Surgeon)

## Purpose
The library is only valuable if it stays accurate, non-redundant, well-linked, and actually used. This skill is the meta-process for keeping it that way.

## When to Use
- Weekly review (Sunday evening or Monday morning is good).
- After any significant real-world use of multiple skills (you discovered improvements, gaps, or better ways to phrase things).
- When the Hub starts feeling messy or you notice duplicate concepts.
- Before a big "scour and consolidate" session.

## Core Process

1. **Open the Hub** (`Library/Hubs/00-Hub.md`) and the Schema.

2. **Review "Needing Attention"** (items with old `last_reviewed` or low version).

3. **For each skill/prompt in active use recently**:
   - Read the real session output where it was used.
   - Update the note with what actually worked, what was missing, better phrasing, new related skills, or energy adjustments.
   - Bump `version` and set `last_reviewed` to today.
   - Add a short "History" bullet if the change is meaningful.

4. **Atomicity & Redundancy Check**:
   - Look for big compiled files that should be broken into atomic notes.
   - Look for near-duplicate skills (e.g. two versions of low-energy planning).
   - Merge or clearly differentiate them. Update links.

5. **Link & Discoverability**:
   - Make sure every skill has good `Related Skills` links.
   - Ensure the Hub queries still surface everything usefully.
   - Add or improve tags and `domain` / `energy` properties where they are missing or wrong.

6. **Dictionary Audit** (explicit):
   - Open the Dictionary.
   - For every note reviewed, verify that `type`, `domain`, `energy`, `tags`, and `compatible_with` values are from the approved lists in the Dictionary.
   - Flag any non-compliant values:
     - Either correct the note, or
     - Propose the term for addition to the Dictionary (with description and examples).
   - Run a quick Dataview in the Hub for any notes using unknown domains/tags.
   - This ensures the controlled vocabulary stays the single source of truth for queries, emitters, and syncs.

7. **Ubiquity & Emit Testing**:
   - Run the emit tools on 2–3 skills you actually used.
   - Verify they come out clean and useful when pasted into a fresh chat.
   - Test --validate on a few notes.
   - Note any friction in `Tools/` or this note.

8. **Grok / External Sync** (when relevant):
   - Decide which skills deserve to be live in `~/.grok/skills/`.
   - Update or create the corresponding SKILL.md (or run the sync script from Tools/).
   - Note the mapping in the skill's "Notes & History".

9. **Output**:
   - Bottom Line: Summary of what was cleaned, added, or retired this session.
   - List of updated notes with version bumps.
   - Dictionary Compliance: Number of notes audited, outliers found (list them), terms proposed for Dictionary.
   - Any new meta-skills or protocols that emerged.
   - One concrete improvement to the system itself (e.g. "added energy-aware section to the Hub").

## Output Format (Bottom Line First)
- **Bottom Line**: One sentence on the state of the library after this pass.
- **Updates Made**: Specific notes + what changed + new version.
- **Dictionary Compliance**: Notes audited this pass, outliers flagged (with suggested fixes or Dictionary additions).
- **Gaps Found**: Things that are still weak or missing.
- **Next Gardener Focus**: What to pay special attention to next time.
- **System Improvement**: One change to the Library structure, schema, or tools.

## Related
- SCHEMA (re-read this every time)
- ../Dictionary (the controlled vocabulary — audit against it in every pass)
- The Hub (your main working view)
- How-to-Use-Ubiquitously
- Any "prompt-surgeon" or consolidation notes from previous work (they contain the history of how the library was built)
- Tools/emit-skill.py (use --validate during reviews)
- New expanded domains: deep-research, career-strategy, systems-audit, sobriety-anchors, circadian-anchors, 5-year-vision-alignment (audit these first in future passes)

## Notes & History
- This role combines the spirit of the old "Prompt Surgeon" scour work with ongoing stewardship.
- The goal is not to collect more prompts. It is to keep the ones that actually move the needle sharp, atomic, and easy to reach from anywhere.
- Treat this skill like any other: run it, capture the useful output in the relevant notes, take the real-world maintenance actions.

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)
