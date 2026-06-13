---
type: hub
name: skill-prompt-hub
domain: [meta, library]
tags: [hub, dataview, entry-point, source-of-truth]
last_reviewed: 2026-06-08
---

# Skill & Prompt Hub — Source of Truth

**This Library is the single source of truth for all AI interactions.**

Obsidian `09-PROMPTS/Library/` (this folder and its atomic notes) is the canonical home. Everything else — .grok/skills/, Claude Projects, ChatGPT customs, Cursor rules, phone notes, one-off chats — is derived from here via the emitter tools.

Start here for discovery. Use the emitter tools to inject into any AI.

## Quick Start — Ubiquitous Usage

**On desktop (recommended):**
```powershell
# Add once to your PowerShell profile for one-word access from anywhere
function skill { & "C:\Users\rappd\OneDrive\Desktop\ObsidianVault\09-PROMPTS\Library\Tools\emit-skill.ps1" @args }

skill --daily --clip           # best daily pack (core protocols + low-energy skills + status placeholder)
skill --favorites              # broader high-value collection
skill --validate mvd-anchors   # check against the Dictionary
```

**On phone:**
Run `python export-for-phone.py` occasionally. Open the generated `Mobile-Favorites.md` (synced via OneDrive) and copy blocks directly.

**Into any AI (Grok, Claude, GPT, local, Cursor...):**
Use the pattern in `How-to-Use-Ubiquitously.md` or the output of `build-master-context.py --daily`.

**In this Grok CLI:** Many skills are synced to `~/.grok/skills/` and are natively available. You can also say "use the library version of..." and the agent can read the vault directly.

## Core Views (Dataview)

### All Skills

```dataview
TABLE domain as Domain, energy as Energy, last_reviewed as "Last Reviewed", version
FROM "09-PROMPTS/Library/Skills"
SORT domain ASC, name ASC
```

### Low-Energy / Fog Day Skills (highest daily value)

```dataview
TABLE name, domain, description
FROM "09-PROMPTS/Library"
WHERE energy = "low" OR energy = "any" OR energy = "collapse"
SORT name ASC
```

### Protocols & Core Meta

```dataview
TABLE name, domain, invocation
FROM "09-PROMPTS/Library/Protocols"
```

### Dictionary Compliance (run these regularly)

```dataview
TABLE file.name, domain, tags
FROM "09-PROMPTS/Library"
WHERE !contains(domain, "meta") AND !contains(domain, "library") AND !contains(domain, "job") AND !contains(domain, "execution") AND !contains(domain, "social") AND !contains(domain, "research") AND !contains(domain, "decision-making") AND !contains(domain, "recovery") AND !contains(domain, "health") AND !contains(domain, "creative") AND !contains(domain, "ai-setup") AND !contains(domain, "philosophy") AND !contains(domain, "philosophy-snf") AND !contains(domain, "finance") AND !contains(domain, "prs") AND !contains(domain, "sobriety") AND !contains(domain, "career") AND !contains(domain, "systems")
```

(Expand the list above as the Dictionary grows. Any results here mean a note is using a domain that hasn't been officially added yet.)

Similar queries can be written for tags.

## Dictionary & Schema (the rules)

- [[../Dictionary]] — The controlled vocabulary. All `domain`, `energy`, `tags`, `type`, etc. must come from here.
- [[../SCHEMA]] — The structural contract. Every note must follow this format.

## How to Add New Skills

1. Use the template in `TEMPLATES/New Skill.md` (or the one in the vault root TEMPLATES folder).
2. Follow the SCHEMA and pick values only from the Dictionary.
3. Place it in the correct subfolder (`Skills/`, `Prompts/`, or `Protocols/).
4. Link it from related notes and update the Hub if appropriate.
5. Run the emitter tools to test it.
6. (Optional but recommended) Run `library-gardener` afterward.

## Maintenance

The **library-gardener** skill is the official process. It now includes an explicit Dictionary compliance audit step.

Run it regularly. It will keep the Library as a healthy, consistent, and truly usable source of truth.

## Current High-Value Packs (via emitter)

- `--daily` → Core low-energy execution set (thoroughness-protocol + low-energy-execution + mvd-anchors + floor-wins + social-calibration + daily-job-search)
- `--favorites` → Broader quick-access collection (adds apply-today, resume-tailoring, deep-research, tool-mode-decider, weekly-review, library-gardener, mvd-anchors, floor-wins, prs-safety-check, snf-hope-activation, snf-proof-registration, sobriety-anchors, etc.)
- SNF (State Not Fate) recovery / philosophy-snf core: sobriety-anchors (load-bearing daily foundation since 2019-11-01), snf-hope-activation (repair hope as prediction with one visible win), snf-proof-registration (external memory + proof that effort shapes the substrate). Pair with mvd-anchors and floor-wins.
- Emitter now robust: emit-skill.py includes load_dictionary + validate_against_dictionary so new skills (like the SNF trio) validate and emit cleanly against the Dictionary.
- You can also build custom packs with `build-master-context.py`

This Hub + the atomic Library + the Tools = the complete ubiquitous system with Obsidian as the single source of truth.

**Loop closed on SNF skills enhancement (2026-06-13).** All changes in vault as source of truth; synced to .grok; packs exported; emitter fixed for future refinements from any AI.

**Full Library Gardener pass 2026-06-13 complete.** All 15+ vault Skills/Protocols/Contexts now Dictionary compliant (fixed low-energy/daily/context domain misuse in mvd/floor/low-energy-exec/prs/master-bio). Version bumps + history on touched notes. New Full-Review-Pack emitted. --list/--search/--validate/--daily/--favorites/custom packs all tested and clean post-fixes. .grok re-synced for updates. GitHub batch push with verification. Dictionary + Hub + gardener self updated. Source of truth (vault) propagated ubiquitously. Next: backport .grok-only skills (systems-audit etc.) to Library. 

Everything starts and ends here (full library now gardened).

---

*Everything starts and ends here.*
