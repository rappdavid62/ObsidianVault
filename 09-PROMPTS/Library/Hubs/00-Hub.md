---
type: hub
name: skill-prompt-hub
domain: [meta, library]
energy: any
compatible_with: [all, obsidian, phone, gpt, claude, local]
version: 3
last_reviewed: 2026-06-28
tags: [hub, onboarding, library, external-memory, standards]
---

# Skill & Prompt Hub

## Bottom Line

The single reusable skill layer lives at `C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library`.

Use this hub to find the canonical note, then emit or paste that note into whatever program you are using.

## Fast Start

- Daily execution: `Tools/emit-skill.ps1 --daily --clip`
- Full context block: `python Tools/build-master-context.py --daily --clip`
- Phone surface: `python Tools/export-for-phone.py`
- External program wiring: `External Program Skill Wiring Matrix.md`
- Second brain loop: `Skills/second-brain-control-loop.md`
- Second brain runbook: `_Meta/Second Brain Runbook.md`
- Learning ledger: `_Meta/Second Brain Learning Ledger.md`
- Vault cleanup loop: `Skills/vault-cleaner.md`
- Maintenance pass: `Skills/library-gardener.md`
- Current app integration map: `08-TECH-AND-AI/Obsidian Integration/Integration Hub.md`

## Core Command Layer

| Command | Canonical note | Use when |
|---|---|---|
| `/brain` | `Skills/second-brain-control-loop.md` | Monitor, improve, and learn from the vault |
| `/vault-cleaner` | `Skills/vault-cleaner.md` | Safe file cleanup and cleanup queue work |
| `/bootstrap` | `Prompts/bootstrap-session.md` | Starting a new AI session |
| `/daily-execution` | `Prompts/daily-execution.md` | Turning today into a small plan |
| `/priority-audit` | `Prompts/priority-audit.md` | Too many active threads |
| `/council` | `Prompts/council-decision.md` and `Skills/council-strategy.md` | Complex decisions |
| `/tp` | `Skills/thoroughness-protocol.md` | Any non-trivial request |
| `/low` | `Skills/low-energy-execution.md` | Collapse, fog, low energy |
| `/jobsearch` | `Skills/daily-job-search.md` | Job-search execution |
| `/apply` | `Skills/apply-today.md` | Specific job application |
| `/social` | `Skills/social-calibration.md` | Replies, boundaries, social reading |
| `/tcouncil` | `Skills/tech-council.md` | Tool/app/platform decisions |

## What Counts As Canonical

- Edit active skills in `Skills/`.
- Edit portable command prompts in `Prompts/`.
- Edit durable context in `Contexts/`.
- Treat `Prompt-Library/` and generated packs as snapshots unless a note says otherwise.
- Bring improvements from ChatGPT, Claude, Gemini, Grok, Codex, Cursor, phone, and local models back into this folder.
- Use `External Program Skill Wiring Matrix.md` to keep all external instructions pointed at this one Library.
- Use `second-brain-control-loop` to coordinate vault monitoring, Library gardening, cleanup, export refreshes, and learning promotion.
- Use `_Meta/Second Brain Runbook.md` to decide daily, weekly, and triggered maintenance cadence.
- Use `_Meta/Second Brain Learning Ledger.md` for lessons that are useful but not yet promoted.

## Review Checklist

- [ ] New skills follow `SCHEMA.md`.
- [ ] Frontmatter values are allowed by `Dictionary.md`.
- [ ] Related skills are linked.
- [ ] Mobile favorites still reflect the highest-use commands.
- [ ] Tool defaults emit the same core pack this hub names.
- [ ] External program instructions point to this vault path, not old Laptop Sync or `08 PROMPTS` paths.
- [ ] Claude, Gemini, Grok, ChatGPT, Codex, Cursor, phone, local model, and Obsidian wiring matches `External Program Skill Wiring Matrix.md`.
- [ ] Maintenance cadence matches `_Meta/Second Brain Runbook.md`.
- [ ] Durable lessons are either promoted or queued in `_Meta/Second Brain Learning Ledger.md`.
- [ ] `second-brain-control-loop` and `vault-cleaner` are used for monitoring and cleanup instead of ad hoc reorgs.

## Dataview Views

### Active Skills

```dataview
TABLE domain as Domain, energy as Energy, last_reviewed as "Last Reviewed", version
FROM "09-PROMPTS/Library/Skills"
SORT domain ASC, file.name ASC
```

### Portable Prompts

```dataview
TABLE domain as Domain, energy as Energy, invocation, last_reviewed as "Last Reviewed"
FROM "09-PROMPTS/Library/Prompts"
SORT file.name ASC
```

### Low-Energy / Fog-Day Surface

```dataview
TABLE domain as Domain, invocation, description
FROM "09-PROMPTS/Library"
WHERE energy = "collapse" OR energy = "low" OR energy = "any"
SORT file.name ASC
```

## Gardener Rule

The Library gets smarter by being used, corrected, and folded back into atomic notes. If an external chat produces a better instruction, do not leave it stranded in that chat. Promote the durable part here, validate it, and regenerate the outputs.
