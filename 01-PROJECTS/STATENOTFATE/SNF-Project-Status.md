---
type: context
tags: [snf, project-status, living-document]
updated: 2026-06-18
---

# SNF Project Status
*Living document. Update after every meaningful session.*
*Last updated: 2026-06-18*

## Where We Are Right Now

**Phase**: Active maintenance + vault integration
**Deployed**: https://statenotfate.netlify.app (live, stable)
**Tests**: 17/17 passing
**Node**: v24.16.0 / npm 11.13.0 (bare npm now works in PowerShell)

## What's Done ✅

### Core PWA
- [x] Full onboarding flow (welcome → state selector → intake)
- [x] 150-question evolving companion tree (branching by severity)
- [x] PHQ-9 with exact clinical language
- [x] Safety screening (suicide/psychosis/mania)
- [x] Dashboard with 9 tabs
- [x] Polaris coaching tab as default
- [x] Proof points system (today/total/ledger)
- [x] Possibility Collapse Modal (3 lanes, proof points)
- [x] Startup Drag Modal (10s timer, 2 proof points)
- [x] Rumination Stop-Loss (3-step grounding workflow)
- [x] Future Narrowing toggle
- [x] Smart Re-Entry Card (1 day / multiple days / low energy)
- [x] Safebox (crisis contacts, reasons to live)
- [x] Media Console (11 items: 6 video + 5 audio)
- [x] Progression roadmap (layers 0-9)
- [x] Cognitive Lab (thought corrections + gratitude)
- [x] PIN lock / security
- [x] Service worker (offline + cache)
- [x] Netlify deploy + netlify.toml
- [x] Safety modules (detection, crisis protocol, polaris integration)
- [x] Playwright test suite (17 tests across 12 files)

### Vault & Tooling
- [x] sync-all.py — syncs 16 skills to Grok (~/.grok/skills)
- [x] Obsidian Local REST API live (v4.1.3)
- [x] SNF-Current-State.md created (2026-06-18)
- [x] Vault audit completed (2026-06-18)

## In Progress 🔄

- [ ] **Gemini skills wiring** — GEMINI_SKILLS_DIR = None in sync-all.py, needs path set
- [ ] **Vault → code sync loop** — no process to close the loop after code changes
- [ ] **Daily notes** — last entry 2026-06-13, 5 days stale

## Not Done / Unverified ❓

These appeared in vault BUILD notes (24.x) but NOT confirmed in live code:
- [ ] Resilience & Restart Meter (visual progress display)
- [ ] Vault Tracker Sync button
- [ ] In-app Mini Systems Audit panel
- [ ] Emit Custom Pack (Skills tab)
- [ ] v24.x version stamp in app header

*Need to verify: open app.js and search for these.*

## Known Issues 🔴

- [ ] STATENOTFATE/ and STATENOTFATE 1/ duplicate folders in vault (confusing)
- [ ] Contexts/master-bio 1.md duplicate (confusing)
- [ ] Untitled.md + Untitled 1.md junk files in Library root
- [ ] MOC files (State-Not-Fate-MOC.md, AI-Systems-MOC.md) describe old AI sessions, not live code

## Next Actions (Priority Order)

1. Set GEMINI_SKILLS_DIR in sync-all.py → re-run → skills reach Gemini
2. Delete/merge duplicates (STATENOTFATE 1/, master-bio 1.md, Untitled files)
3. Verify 24.x unconfirmed features against app.js
4. Update State-Not-Fate-MOC.md to link to SNF-Current-State.md
5. Resume daily notes (even a one-liner per session)

## Vault Integration (as of 2026-06-18)

| Tool | Connected | How |
|---|---|---|
| Grok | ✅ | sync-all.py → ~/.grok/skills (16 skills) |
| Gemini | ❌ | GEMINI_SKILLS_DIR = None — not wired |
| Obsidian REST API | ✅ | Port 27123, token confirmed |
| Antigravity IDE | ✅ | Can read/write vault live via REST API |
| Cursor | ✅ | .cursorrules written to vault roots by sync-all.py |
| Claude | ⚠️ | Claude-Project-Instructions.md exists but manual upload |

## 5-Year Vision Link
See [[Human/Personal-Profile-5Year-Vision]] for the full picture.
Stable income + meaningful PRS/trades contribution + energy floor + external proof + relationships.
This PWA is floor-building infrastructure. It's working.