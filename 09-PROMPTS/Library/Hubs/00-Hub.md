---
type: hub
name: skill-prompt-hub
domain: [meta, library]
tags: [hub, dataview, entry-point, source-of-truth]
last_reviewed: 2026-06-08
---

# Skill & Prompt Hub — Source of Truth

**This Library (in the Laptop Sync vault) is the single source of truth for all AI.**

Obsidian `08 PROMPTS/Library/` (this folder and its atomic notes) is the canonical home for every skill, prompt, protocol, and context you use with Grok, Claude, ChatGPT, local models, Cursor, phone, etc.

Everything else is derivative. Start here for discovery and maintenance.

## Quick Start — Ubiquitous Usage

**On desktop (CLI emitter — recommended daily):**
```powershell
# Add once to PowerShell profile for one-word access from anywhere
function skill { & "C:\Users\rappd\My Drive\INBOX\AI Learning\Laptop Sync\08 PROMPTS\Library\Tools\emit-skill.ps1" @args }

skill --daily --clip          # core low-energy daily execution pack + status placeholder
skill --favorites             # broader high-value collection (energy-balanced)
skill --validate mvd-anchors  # check against Dictionary
```

**On phone:**
Run `python export-for-phone.py` from the Tools folder periodically. Open the generated `Mobile-Favorites.md` (synced via Google Drive) and copy blocks directly.

**Into any AI (Grok, Claude, GPT, Cursor, local, phone chat...):**
Use the pattern in `How-to-Use-Ubiquitously.md` or the powerful output of `build-master-context.py --daily`.

**In this Grok CLI environment:**
Many skills are synced to `~/.grok/skills/` and are natively available (description-driven). You can also say "use the library version of daily-job-search with my current status" — the agent can read the vault directly.

**Claude (Anthropic):**
- Best: Create a Claude Project and upload key files from `08 PROMPTS/Library/` (master-bio, Dictionary, core Skills/Protocols, Hub, How-to-Use). Paste the Master Context (from build-master-context.py) into Project instructions.
- Or paste emitted blocks + status into chats.

**Gemini (Google):**
- Paste the Master Context or Favorites block (generated with --clip) at the start of conversations.
- Upload Library files if the interface supports.
- Use phone export for Gemini mobile chats.

## Core Views (Dataview)

### All Skills (by domain)

```dataview
TABLE domain as Domain, energy as Energy, last_reviewed as "Last Reviewed", version
FROM "08 PROMPTS/Library/Skills"
SORT domain ASC, name ASC
```

### Low-Energy / Fog Day Skills (highest daily value)

```dataview
TABLE name, domain, description
FROM "08 PROMPTS/Library"
WHERE energy = "low" OR energy = "any" OR energy = "collapse"
SORT name ASC
```

### Protocols & Core Meta

```dataview
TABLE name, domain, invocation
FROM "08 PROMPTS/Library/Protocols"
```

### Dictionary Compliance (run these in every Gardener / ai-setup-audit pass)

**Notes using domains not in the Dictionary** (expand the list as Dictionary grows):
```dataview
TABLE file.name, domain, "Possible issue: domain not in Dictionary"
FROM "08 PROMPTS/Library"
WHERE !contains(domain, "meta") AND !contains(domain, "library") AND !contains(domain, "job") AND !contains(domain, "execution") AND !contains(domain, "social") AND !contains(domain, "research") AND !contains(domain, "decision-making") AND !contains(domain, "recovery") AND !contains(domain, "health") AND !contains(domain, "creative") AND !contains(domain, "ai-setup") AND !contains(domain, "philosophy") AND !contains(domain, "philosophy-snf") AND !contains(domain, "finance") AND !contains(domain, "prs") AND !contains(domain, "sobriety") AND !contains(domain, "career") AND !contains(domain, "systems")
```

**Notes using tags not in the Dictionary** (example; expand exclude list from Dictionary):
```dataview
TABLE file.name, tags, "Possible issue: tag not in Dictionary"
FROM "08 PROMPTS/Library"
WHERE !contains(tags, "low-energy") AND !contains(tags, "mvd") AND !contains(tags, "floor") AND !contains(tags, "anchors") AND !contains(tags, "floor-wins") AND !contains(tags, "proof") AND !contains(tags, "restart") AND !contains(tags, "no-shame") AND !contains(tags, "daily") AND !contains(tags, "weekly") AND !contains(tags, "routine") AND !contains(tags, "low-friction") AND !contains(tags, "job") AND !contains(tags, "prs") AND !contains(tags, "hvac") AND !contains(tags, "logistics") AND !contains(tags, "maintenance") AND !contains(tags, "driver") AND !contains(tags, "resume") AND !contains(tags, "application") AND !contains(tags, "cover-letter") AND !contains(tags, "prs-track") AND !contains(tags, "certification") AND !contains(tags, "career") AND !contains(tags, "job-search") AND !contains(tags, "tailoring") AND !contains(tags, "follow-up") AND !contains(tags, "social") AND !contains(tags, "communication") AND !contains(tags, "calibration") AND !contains(tags, "boundaries") AND !contains(tags, "professional") AND !contains(tags, "dating") AND !contains(tags, "relationships") AND !contains(tags, "research") AND !contains(tags, "deep-work") AND !contains(tags, "synthesis") AND !contains(tags, "options") AND !contains(tags, "analysis") AND !contains(tags, "meta") AND !contains(tags, "library") AND !contains(tags, "schema") AND !contains(tags, "maintenance") AND !contains(tags, "gardener") AND !contains(tags, "dictionary") AND !contains(tags, "tools") AND !contains(tags, "ai-setup") AND !contains(tags, "model-selection") AND !contains(tags, "ubiquity") AND !contains(tags, "standards") AND !contains(tags, "state-not-fate") AND !contains(tags, "philosophy") AND !contains(tags, "sobriety") AND !contains(tags, "recovery") AND !contains(tags, "depression-as-state") AND !contains(tags, "anchors") AND !contains(tags, "proof-based-hope") AND !contains(tags, "ideal-vs-realistic") AND !contains(tags, "bottom-line-first") AND !contains(tags, "reading-error") AND !contains(tags, "visible-proof") AND !contains(tags, "external-memory") AND !contains(tags, "restart-speed") AND !contains(tags, "resilience-rate") AND !contains(tags, "hope-meter") AND !contains(tags, "systems-failure") AND !contains(tags, "load-bearing") AND !contains(tags, "substrate") AND !contains(tags, "neuroplasticity") AND !contains(tags, "cognitive-offloading") AND !contains(tags, "evidence-based") AND !contains(tags, "prediction-error") AND !contains(tags, "dopamine-reward")
```

Use these (or improved versions) in every Library Gardener pass. They make "unknown value" auditing automatic and visible in the Hub.

## Dictionary & Schema (the rules)

- [[../Dictionary]] — The controlled vocabulary. All `domain`, `energy`, `tags`, `type`, etc. must come from here.
- [[../SCHEMA]] — The structural contract. Every note must follow this.

## How to Add New Skills

1. Use the template in `TEMPLATES/New Skill.md` (or the one in the vault root TEMPLATES folder).
2. Follow the SCHEMA and pick values only from the Dictionary.
3. Place it in the correct subfolder (`Skills/`, `Prompts/`, or `Protocols/`).
4. Link it from related notes and update the Hub if appropriate.
5. Run the emitter tools to test it.
6. (Optional but recommended) Run the `library-gardener` afterward.

## Maintenance

The **library-gardener** skill is the official meta-process for keeping everything sharp, atomic, dictionary-compliant, and actually useful.

Run it regularly. It will keep the Library as a healthy, consistent, and truly usable source of truth for all AI.

## Current High-Value Packs (via emitter)

- `--daily` → Core low-energy execution set (thoroughness-protocol + low-energy-execution + mvd-anchors + floor-wins + social-calibration + daily-job-search)
- `--favorites` → Broader quick-access collection (adds apply-today, resume-tailoring, deep-research, career-strategy, tool-mode-decider, weekly-review, library-gardener, prs-safety-check, snf-proof-registration, snf-hope-activation, systems-audit, sobriety-anchors, circadian-anchors, 5-year-vision-alignment, cover-letter-followup, financial-stability, ai-setup-audit, substrate-reminders, etc.)

**New**: Use `python emit-skill.py --validate <name>` for improved frontmatter + basic Dictionary presence checks.

**Library expanded and improved** (26+ Skills + Protocols + Contexts + full Dictionary/SCHEMA). New: substrate-reminders (daily substrate reminders with scientific grounding for the core SNF metaphor "effort can still shape the substrate"). Enhanced snf-proof-registration, snf-hope-activation, and systems-audit with "Scientific Basis" sections (neuroplasticity, cognitive offloading, hope theory / prediction error, external memory research, etc.). Updated Dictionary tags and Hub. Use with existing SNF skills for stronger evidence-based reinforcement.

This Hub + the atomic Library + the Tools = the complete ubiquitous system with Obsidian (Laptop Sync vault) as the single source of truth.

---

*Everything starts and ends here. This is the universal truth.*
