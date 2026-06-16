---
type: skill
name: daily-job-search
aliases: [jobsearch, hunt-jobs, /jobsearch]
description: >
  Execute a focused, low-friction daily job search session.
  Use when the user wants structured help with leads, applications, tailoring, or maintaining pipeline momentum without burning out.
domain: [job, execution]
energy: low
invocation: ["/jobsearch", "daily job search", "help with job hunt today"]
compatible_with: [grok, claude, gpt, local]
version: 1
last_reviewed: 2026-06-08
tags: [job, daily, low-energy, prs-track]
---

# Daily Job Search

## Purpose
Turn vague "I should look for jobs" into a concrete, bounded, proof-generating session that respects current energy while moving the needle on applications and leads.

## When to Use
- Morning or early in the day when energy is at least "medium" or "low but not collapse".
- As part of a weekly rhythm (e.g. 3–5 focused sessions per week).
- When the status block shows runway pressure or job search has gone cold.

## Core Instructions
1. Start with the user's current status block (runway, energy, top target roles, recent activity).
2. Pull or suggest 3–8 realistic leads or applications that match the priority list (PRS, HVAC helper, low-voltage/field tech, maintenance, warehouse, driving).
3. For each lead or application, produce the minimal high-leverage next action (tailor resume, send message, fill form, follow up).
4. Generate exact copy-paste artifacts when useful (tailored bullets, message drafts, application notes).
5. End with a tiny "floor win" that counts as progress even on a bad day (e.g. "saved 2 good leads", "sent one low-friction message").
6. Update or suggest updates to the job_search_tracker.

Always separate:
- **Ideal Move** (what a high-energy, well-resourced version would do)
- **Realistic Move** (what is actually doable today given energy/money/fog/transport)

## Output Format (Bottom Line First)
- **Bottom Line**: One sentence summary of today's job search focus and expected output volume.
- **Leads / Targets** (3–8 items with source, why it fits, next action).
- **Artifacts** (ready-to-use resume bullets, cover letter snippets, outreach messages).
- **Tracking Note**: Suggested rows or status changes.
- **Floor Win**: The smallest thing that still counts as movement today.
- **Risks / Friction**: What could stop execution and how to reduce it.

## Context to Inject
- Current status block (especially job targets, runway, energy)
- Recent job_search_tracker entries
- Master bio / constraints (PRS cert, work history with Eleeo/D2C, Clark And Sons, etc.)
- Priority role list

## Related Skills & Prompts
- [[low-energy-execution]] (scale way down or skip entirely on true collapse days)
- [[resume-tailoring]]
- [[apply-today]]
- [[council-strategy]] (for big decisions about which roles to chase hard)
- The full David AI Prompt Library commands for the classic 12-command flow

## Notes & History
- Designed for the specific constraint set: money runway pressure, variable energy, PRS career path + trade skills as parallel tracks.
- Prefers volume of low-friction actions over perfection on any single application.
- Update this note after any session where the real workflow diverged significantly from the instructions.

(This is the atomic version in the Laptop Sync vault - universal truth. All prompts consolidated here.)
