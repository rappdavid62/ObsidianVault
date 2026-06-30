---
type: course-pack
source_app: Codex
target_app: AI Wisebase
status: active
created: 2026-06-29
last_verified: 2026-06-29
tags:
  - codex
  - ai-wisebase
  - course
  - skills
  - plugins
  - mcp
---

# Codex Course - AI Wisebase Learning Pack

This course teaches David how to use Codex as a practical working partner across coding, research, local files, Obsidian, plugins, browser testing, computer use, automations, and reusable skills.

Primary source: OpenAI Codex manual, refreshed on 2026-06-29 from `https://developers.openai.com/codex/codex-manual.md`.

## Course Promise

By the end, David should be able to:

- Choose the right Codex surface for a task: app, CLI, IDE extension, cloud, Browser, Chrome, Computer Use, or connector.
- Prompt Codex with clear goal, context, constraints, and done-when criteria.
- Use plans, goals, reviews, and tests without overcomplicating the work.
- Understand what skills, plugins, MCP servers, hooks, memories, rules, and automations are for.
- Decide when to let Codex act, when to ask it to inspect first, and when to keep the task read-only.
- Turn repeated workflows into reusable skills or automations.
- Use AI Wisebase as the learning memory: course notes, flashcards, quizzes, knowledge graph, and concept videos.

## Course Structure

### Module 1 - What Codex Is

Codex is OpenAI's software-development agent. It can write code, understand unfamiliar codebases, review code, debug failures, and automate repetitive development tasks.

Core idea: Codex works best when treated like a configured teammate, not a one-off chatbot.

Practice:

```text
Explain what Codex can do in this workspace. Separate coding, research, file editing, browser testing, app control, and connected-app actions.
```

Mastery check:

- David can explain the difference between asking ChatGPT a question and asking Codex to work in a local project.
- David can name at least three risks Codex helps manage through sandboxing, approvals, and review.

Sources:

- https://developers.openai.com/codex/overview
- https://developers.openai.com/codex/learn/best-practices

### Module 2 - The Prompt Formula

Use this default structure:

```text
Goal:
Context:
Constraints:
Done when:
```

Example:

```text
Goal: Create a short guide that teaches me how to use Codex Browser and Computer Use.
Context: I am on Windows in C:\ROOT_OBSIDIAN\DOV and I use Obsidian as my second brain.
Constraints: Keep it beginner-friendly. Separate safe read-only actions from actions that change files or accounts.
Done when: The guide has a 20-minute practice exercise and a checklist I can follow.
```

Practice:

- Rewrite three vague requests into the four-part format.
- Ask Codex to critique the prompt before doing the task.
- Ask Codex to identify missing context.

Mastery check:

- David can turn a fuzzy idea into a scoped prompt without needing a perfect technical vocabulary.

Sources:

- https://developers.openai.com/codex/prompting
- https://developers.openai.com/codex/workflows

### Module 3 - Plans, Goals, Threads, and Context

Use Plan mode when the work is unclear, risky, or multi-step. Use Goal mode when the task may take many steps and needs a persistent definition of success.

Key terms:

- Thread: one Codex working conversation.
- Local thread: runs on this machine and can use local files and commands.
- Cloud thread: runs in an isolated remote environment.
- Context window: the amount of conversation, files, and tool output Codex can actively hold.
- Compaction: Codex summarizes long context so work can continue.

Practice:

```text
/plan
Interview me until this project idea is specific enough to become a Codex goal. Then draft the final /goal text.
```

Mastery check:

- David can decide whether a task should be a one-off prompt, a plan, a goal, or an automation.

Sources:

- https://developers.openai.com/codex/prompting
- https://developers.openai.com/codex/app/commands

### Module 4 - Local Files, Sandbox, Approvals, and Trust

Codex can read and edit files depending on the current permission profile. In this current session, the workspace root is writable, while access outside approved roots is restricted.

Simple rule:

- Read-only tasks are safest.
- Workspace-write tasks are normal for editing files in the project.
- Full-access or network tasks need more care.
- Destructive commands, secrets, account settings, and broad system changes should be explicit.

Practice:

```text
Inspect this vault for Codex learning notes. Do not edit anything. Report only the paths that look relevant and what each one is for.
```

Then:

```text
Create one new learning note in the best location. Keep edits scoped to that file only.
```

Mastery check:

- David can tell whether Codex is reading, editing, running a command, using a connector, or operating the GUI.

Sources:

- https://developers.openai.com/codex/permissions
- https://developers.openai.com/codex/agent-approvals-security

### Module 5 - AGENTS.md, Config, and Reusable Guidance

Use `AGENTS.md` for durable repo instructions: how to run tests, what not to change, project conventions, verification steps, and review expectations.

Use `config.toml` for Codex settings: model defaults, sandbox profiles, MCP servers, hooks, feature flags, and other durable configuration.

Rule of thumb:

- Prompt: applies now.
- `AGENTS.md`: applies to this repo or folder.
- User config: applies across Codex sessions.
- Skill: reusable task workflow.
- Plugin: installable package of skills, apps, MCP servers, and related assets.

Practice:

```text
Read the current project guidance files and summarize what instructions Codex should follow in this vault. Do not change files.
```

Mastery check:

- David can name the smallest durable place to store a repeated instruction.

Sources:

- https://developers.openai.com/codex/guides/agents-md
- https://developers.openai.com/codex/config-basic

### Module 6 - Skills

Skills are reusable workflows. A skill is a folder with a `SKILL.md` file and optional scripts, references, and assets. Codex sees skill names and descriptions first, then reads the full skill only when it decides the task matches.

Use skills when:

- A workflow repeats.
- A task needs special steps or reference files.
- You want Codex to follow a known process reliably.

Practice:

```text
Help me design a Codex skill for turning messy Obsidian capture notes into organized project notes. Ask clarifying questions first, then draft the SKILL.md.
```

Mastery check:

- David can explain the difference between a prompt, a skill, and a plugin.

Sources:

- https://developers.openai.com/codex/skills
- https://agentskills.io

### Module 7 - Plugins and Apps

Plugins bundle reusable Codex capabilities. A plugin can include:

- Skills: reusable instructions and workflows.
- Apps: connected services such as Gmail, Slack, GitHub, Google Drive, or AI Wisebase.
- MCP servers: tool/context providers that Codex can call.

Use plugins when Codex needs an installed capability or an external service. Examples from this session include OpenAI Developers, Browser, Computer Use, Build Web Apps, and AI Wisebase.

Practice:

```text
List the plugins and apps available in this thread. For each one, explain one thing it can do, one thing it should not be used for, and one practice task.
```

Mastery check:

- David can say when to use a connector/plugin instead of web search or memory.

Sources:

- https://developers.openai.com/codex/plugins
- https://developers.openai.com/codex/plugins/build

### Module 8 - MCP Servers and Connectors

MCP connects Codex to tools and context. It can expose docs, browsers, Figma, GitHub, Sentry, local servers, or custom tools.

Use MCP when Codex needs structured access to a system. For private services, prefer a connector or MCP server over asking Codex to guess from memory.

Practice:

```text
Explain which parts of my current task use local files, which use plugins, and which would require MCP. Keep it practical.
```

Mastery check:

- David can explain why "endpoint is running" is not the same as "Codex is configured to use it."

Sources:

- https://developers.openai.com/codex/mcp

### Module 9 - Browser, Chrome, and Computer Use

Use Browser for unauthenticated local previews, public pages, screenshots, rendered UI checks, and web app debugging.

Use Chrome when a task depends on the user's Chrome profile, logged-in state, existing tabs, or extensions.

Use Computer Use when Codex must visually operate a desktop app or GUI. On Windows, Computer Use works in the foreground, so Codex may move the pointer and type in the active desktop.

Practice:

```text
Use @Browser to open the local app route, inspect the rendered state, and report layout issues. Do not edit files until you show me the findings.
```

Practice:

```text
Use @Computer to inspect the visible app window and tell me what task is safe to automate. Do not click account, payment, security, or credential settings.
```

Mastery check:

- David can choose Browser, Chrome, or Computer Use correctly.

Sources:

- https://developers.openai.com/codex/app/browser
- https://developers.openai.com/codex/app/chrome-extension
- https://developers.openai.com/codex/app/computer-use

### Module 10 - Review, Testing, and Git

Codex should not just make changes. It should verify them.

Ask for:

- smallest relevant test
- lint or type check when appropriate
- manual verification steps
- review of the diff before acceptance
- file and line references for findings

Practice:

```text
Review the uncommitted changes like a serious code reviewer. Findings first, ordered by severity, with exact file references. If there are no issues, say so and name any test gaps.
```

Mastery check:

- David can ask for a review in a way that produces actionable findings rather than vague commentary.

Sources:

- https://developers.openai.com/codex/app/review
- https://developers.openai.com/codex/integrations/github

### Module 11 - Automations

Automations run recurring Codex tasks. They can add findings to the inbox or archive themselves if nothing matters.

Use a thread automation when the task should wake up the same conversation. Use a standalone/project automation when each run should be independent.

Good automation prompt ingredients:

- What to check.
- Where to check.
- Cadence.
- What counts as a finding.
- What to ignore.
- Whether to edit, report only, or ask first.
- When to stop.

Practice:

```text
Draft an automation prompt that checks this vault weekly for stale Codex learning notes. It should report only, not edit.
```

Mastery check:

- David can distinguish "remind me in this thread" from "run a recurring project check."

Sources:

- https://developers.openai.com/codex/app/automations

### Module 12 - Subagents, Hooks, Rules, and Memories

Advanced features:

- Subagents: parallel workers for read-heavy exploration, test triage, summaries, or independent reviews.
- Hooks: scripts that run at lifecycle events such as before tool use, after tool use, before compaction, or when a turn stops.
- Rules: command policy that controls what Codex can run outside the sandbox.
- Memories: local recall layer for stable preferences and recurring workflows.

Use these only when the simpler surface is not enough.

Practice:

```text
Use parallel subagents to inspect three separate areas of this vault: Codex notes, Obsidian integration notes, and prompt-library skills. Return one merged summary with file paths.
```

Mastery check:

- David can explain when advanced machinery saves time and when it adds risk or complexity.

Sources:

- https://developers.openai.com/codex/subagents
- https://developers.openai.com/codex/hooks
- https://developers.openai.com/codex/rules
- https://developers.openai.com/codex/memories

## AI Wisebase Study Plan

Use AI Wisebase as the learning layer for this course:

1. Upload this course pack as a knowledge-base document.
2. Generate flashcards for the module terms.
3. Generate a quiz after Modules 1-4, another after Modules 5-8, and a final after Modules 9-12.
4. Build a knowledge graph with these nodes:
   - Codex surfaces
   - Prompt formula
   - Permissions
   - AGENTS.md
   - config.toml
   - Skills
   - Plugins
   - MCP
   - Browser
   - Computer Use
   - Automations
   - Hooks
   - Memories
5. Create short concept videos only for hard-to-visualize topics:
   - "Prompt, AGENTS.md, skill, plugin: which surface should I use?"
   - "Browser vs Chrome vs Computer Use"
   - "Sandbox, approvals, and permissions"

## Four-Week Course Schedule

### Week 1 - Core Use

- Day 1: Module 1
- Day 2: Module 2
- Day 3: Module 3
- Day 4: Module 4
- Day 5: Review flashcards and do one read-only vault inspection

Outcome: David can prompt Codex safely and understand what it is doing.

### Week 2 - Durable Setup

- Day 1: Module 5
- Day 2: Module 6
- Day 3: Module 7
- Day 4: Module 8
- Day 5: Create or revise one small skill draft

Outcome: David can decide where repeated instructions and capabilities belong.

### Week 3 - Real Tools

- Day 1: Module 9
- Day 2: Module 10
- Day 3: Practice Browser on a local or public page
- Day 4: Practice review mode on a small change
- Day 5: Explain the workflow back to AI Wisebase

Outcome: David can test, inspect, and review real work without guessing.

### Week 4 - Automation and Advanced Work

- Day 1: Module 11
- Day 2: Module 12
- Day 3: Draft one reporting-only automation
- Day 4: Draft one subagent task
- Day 5: Final practical exam

Outcome: David can turn repeated work into durable systems.

## Final Practical Exam

Ask Codex:

```text
I want to improve my Codex learning system in this DOV vault.

Goal: Inspect the current Codex, AI, prompt-library, and integration notes. Create one small improvement that helps me learn Codex better.
Context: This is an Obsidian vault at C:\ROOT_OBSIDIAN\DOV.
Constraints: Keep edits minimal. Do not reorganize the vault. Do not touch private files. Use official Codex docs for product claims.
Done when: You create or update one learning note, explain what changed, and give me one next practice exercise.
```

Passing answer:

- Codex inspects before editing.
- It keeps scope small.
- It uses current official documentation for product claims.
- It creates a useful note.
- It reports what changed and how to practice next.

## Quiz Bank

### Checkpoint Quiz 1 - Core Use

1. What are the four parts of the default Codex prompt formula?
2. When should David use Plan mode instead of asking Codex to start editing immediately?
3. What is the difference between a local thread and a cloud thread?
4. Why should "done when" criteria include verification?
5. What is one safe read-only task David can ask Codex to do in this vault?

Answer key:

1. Goal, context, constraints, done when.
2. When the task is unclear, risky, complex, or needs clarification.
3. Local runs on David's machine; cloud runs in an isolated remote environment.
4. So Codex can test or confirm the work instead of only claiming it is done.
5. Inspect relevant notes and report paths without editing files.

### Checkpoint Quiz 2 - Durable Setup

1. What belongs in `AGENTS.md`?
2. What belongs in `config.toml`?
3. What is a skill?
4. What is a plugin?
5. Why is MCP useful?

Answer key:

1. Durable project guidance, commands, conventions, constraints, and verification expectations.
2. Codex settings such as model defaults, sandbox profiles, permissions, MCP servers, hooks, and feature flags.
3. A reusable workflow with `SKILL.md` plus optional scripts, references, and assets.
4. An installable bundle that can include skills, apps, MCP servers, hooks, and assets.
5. It gives Codex structured access to tools and external context.

### Checkpoint Quiz 3 - Real Tools

1. When should David use Browser?
2. When should David use Chrome?
3. When should David use Computer Use?
4. What is the Windows-specific caution for Computer Use?
5. What should Codex report after a code or file change?

Answer key:

1. For unauthenticated local previews, public pages, screenshots, and rendered web-app checks.
2. For logged-in state, cookies, extensions, existing tabs, or the real Chrome profile.
3. For visually operating a desktop app or GUI when structured tools are not enough.
4. It controls the active foreground desktop and may move the pointer or type.
5. What changed, how it was verified, and any remaining risks or test gaps.

### Final Quiz - Surface Choice

For each need, choose the best surface:

1. "Remember this repo's test command every time."
2. "Run this recurring weekly report."
3. "Connect Codex to a documentation server."
4. "Package a reusable workflow for installation."
5. "Click through a visible Windows app."
6. "Preview a local unauthenticated web app."
7. "Store a repeated task workflow."
8. "Do a parallel read-heavy investigation."

Answer key:

1. `AGENTS.md`
2. Automation
3. MCP
4. Plugin
5. Computer Use
6. Browser
7. Skill
8. Subagents

## Quick Reference

| Need | Use |
| --- | --- |
| One-time task constraint | Prompt |
| Unclear task | Plan mode |
| Long task with success criteria | Goal mode |
| Repo-specific durable guidance | `AGENTS.md` |
| Personal or project settings | `config.toml` |
| Reusable workflow | Skill |
| Installable bundle of skills/apps/MCP | Plugin |
| External live tools or context | MCP or connector |
| Local unauthenticated web preview | Browser |
| Logged-in Chrome state | Chrome |
| Desktop GUI operation | Computer Use |
| Recurring check | Automation |
| Command permission policy | Rules |
| Lifecycle script | Hook |
| Stable personal recall | Memories |
| Parallel read-heavy investigation | Subagents |

## Maintenance Rule

Refresh this course when Codex features, plugin availability, or OpenAI docs change. Product claims should come from current official docs, not from memory alone.
