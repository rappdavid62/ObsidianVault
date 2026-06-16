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
last_reviewed: 2026-06-08
tags: [meta, tools, ai-setup]
---

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
- [[ai-setup-audit]] (the bigger audit skill)
- All the skills (this one decides which to load)
- The original "08_Tool_Mode_Decider.md"

## Notes & History
- This is a meta-skill that protects your attention and the quality of every other skill.
- Update as your tool landscape changes (new local models, new Obsidian plugins, new Grok features, etc.).
