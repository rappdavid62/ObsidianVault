# Grok Skills — Consolidated from .grok/skills

**Source:** C:\Users\rappd\.grok\skills\ (and bundled)

This consolidates the skills from the Grok Build system, including the create-skill, best-of-n, check-work, docx, help, imagine, pptx, xlsx, and bundled ones. These are the "skills from all the AI" in the .grok setup. Copy of SKILL.md content for the OBSIDIAN LIBRARY.

## create-skill/SKILL.md
[Full content from read:
---
name: create-skill
description: >
  Interactively create a new Grok skill (SKILL.md + optional scripts/references).
  Use when the user wants to create a skill, scaffold a skill, or runs /create-skill.
metadata:
  short-description: "Create a new Grok skill"
---

# Create Skill

Interactively gather requirements from the user and create a fully working Grok skill on disk.

## Step 1: Gather information

Ask the user the following questions **one at a time as regular conversation questions** (do NOT use structured option prompts for free-text inputs):

1. **Skill name** - ask the user to type a name. Lowercase letters (a-z), digits (0-9), and hyphens (-) only. Must start and end with a letter or digit. Must be 2-64 characters long (e.g. `deploy-k8s`). Validate the name before proceeding.
2. **Scope** - present the user with two options:
   - **Project** (Recommended): `<repo-root>/.grok/skills/<name>/SKILL.md` - available only in this repo, shareable with teammates
   - **User**: `~/.grok/skills/<name>/SKILL.md` - available in all projects
   - Default to **Project** if inside a git repo, otherwise **User**.
3. **What it should do** - ask the user to describe the workflow, paste an example prompt they keep repeating, or explain the task the skill should automate.

## Step 2: Draft the description

Write a `description` frontmatter value that includes:
- What the skill does (1-2 sentences)
- Trigger phrases and keywords so Grok knows when to auto-invoke it
- The slash command name (e.g. "Use when the user runs /deploy-k8s")

Show the drafted description to the user and let them approve or edit it.

## Step 3: Create the directory

Run this bash command to create the skill directory:

```bash
mkdir -p <SKILL_DIR>
```

Where `<SKILL_DIR>` is:
- User scope: `~/.grok/skills/<name>`
- Project scope: `<repo-root>/.grok/skills/<name>`

If the skill needs helper scripts, also create `<SKILL_DIR>/scripts/`.
If the skill needs reference docs, also create `<SKILL_DIR>/references/`.

## Step 4: Write SKILL.md

Use `search_replace` with an empty `old_string` to create the file at `<SKILL_DIR>/SKILL.md`.

The file MUST follow this exact format:

```
---
name: <skill-name>
description: <the description from Step 2>
---

<markdown body with instructions, steps, code blocks>
```

Also write any supporting files (scripts, references) using the same create method.

## Step 5: Verify and confirm

1. Run `cat <SKILL_DIR>/SKILL.md` to verify the file was written correctly.
2. Tell the user the skill is ready and how to use it:
   - Slash command: `/<skill-name>`
   - TUI menu: `/skills <skill-name>`
   - Automatic: Grok will invoke it when the description matches user intent
3. Tell the user the skill should appear in the slash menu within a few seconds (skills auto-reload when files change on disk).

## Guidelines

- Keep the SKILL.md body focused and actionable. It is a prompt for the agent, not documentation.
- The `description` field is critical. It controls auto-invocation. Be specific with trigger words.
- Prefer referencing existing CLI tools over writing custom scripts.
- Do NOT skip creating the directory. The file will fail to save without it.
- Always use absolute paths when creating files to avoid writing to the wrong location.
]

## best-of-n/SKILL.md
[Full content from read:
---
name: best-of-n
description: >
  Implement a task N ways in parallel and pick the best. Spawns multiple
  subagents in isolated worktrees, evaluates all candidates, and applies the
  winner. Use when asked to "best of n", "try multiple approaches", "parallel
  implementations", "/best-of-n", or "/bon".
metadata:
  short-description: "Parallel implementation tournament"
---

# /best-of-n -- Parallel Implementation Tournament

Implement a task multiple different ways in parallel, evaluate all candidates,
and apply the best one.

## Usage

`/best-of-n [N] <task>`

- If the first token is a number 2-10, it sets the candidate count; the rest is the task.
- If omitted, N defaults to 3.

Examples:
- `/best-of-n implement the login page` (3 candidates)
- `/best-of-n 5 refactor the auth module` (5 candidates)

## Steps

1. Parse the user's message to extract **N** (candidate count, default 3) and
   the **task description**.

2. Spawn **N** subagents in a single message (parallel tool calls). Use the
   `task` tool for each with:
   - `subagent_type`: `"general-purpose"`
   - `isolation`: `"worktree"`
   - `run_in_background`: `true`
   - `description`: `"Candidate <number>"`
   - `prompt`: the task description, plus
     `"You are candidate <number> of <N> independent implementations. Implement the task fully. When done, summarize your approach and the changes you made."`

3. Wait for all candidates to complete using `get_task_output` with `block: true`
   or `wait_tasks` with `mode: "wait_all"`.

4. Evaluate and pick the winner using the criteria below.

5. Apply the winner's changes from its worktree to the main workspace.
   Review the changes in context and fix any remaining issues.

6. End your response with `WINNER: <number>` (1-N).

## Evaluation Criteria

Evaluate each candidate on these axes, in order of importance:

1. **Correctness** -- Does the candidate actually solve the task? Does it handle
   the requirements completely, or does it miss important aspects? Are there
   logic errors, type errors, or broken imports?

2. **Code Quality** -- Is the code clean, readable, and well-structured? Does it
   follow the patterns and conventions of the surrounding codebase? Does it
   avoid unnecessary complexity?

3. **Safety** -- Does the candidate avoid introducing bugs, security issues, or
   breaking changes to existing functionality?

## How to Decide

- Focus on correctness first. A candidate that fully solves the task with minor
  style issues beats one that is beautifully written but incomplete or wrong.
- If multiple candidates are equally correct, prefer the one with cleaner code
  and better codebase integration.
- If a candidate introduces unnecessary changes beyond the task scope, count
  that against it.
- If all candidates are poor, still pick the least bad one.

## Presenting Your Evaluation

Before announcing your choice, present a structured comparison:

| Dimension | Candidate 1 | Candidate 2 | ... |
|-----------|-------------|-------------|-----|
| Correctness | Short verdict | Short verdict | ... |
| Code Quality | Short verdict | Short verdict | ... |
| Safety | Short verdict | Short verdict | ... |

Then list key findings:

| Finding | Severity | Candidate 1 | Candidate 2 | ... |
|---------|----------|-------------|-------------|-----|
| Specific issue | High/Medium/Low | How handled | How handled | ... |

State which candidate you chose and why.
]

**Note:** Other .grok/skills include check-work, docx (with scripts for editing), help, imagine, pptx (with scripts), xlsx (with scripts), and bundled (design, execute-plan, implement, pr-babysit, review, etc.). Copied key ones here; see .grok/skills/ for complete SKILL.md and scripts/tiny tools.

## Tiny Tools from .grok/skills
- docx/scripts/: __init__.py, accept_changes.py, comment.py, office/helpers/, pack.py, unpack.py, validate.py, etc.
- pptx/scripts/: __init__.py, add_slide.py, clean.py, office/, thumbnail.py
- xlsx/scripts/: office/helpers/, pack.py, recalc.py
- Other skills have references like editing.md, pptxgenjs.md.

These are the little tiny tools. Copied locations and key content for the OBSIDIAN LIBRARY.