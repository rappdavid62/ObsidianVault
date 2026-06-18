---
type: context
tags: [snf, current-state, ground-truth]
updated: 2026-06-18
---

# SNF Current State — Live App Snapshot
*Verified against actual code. Not aspirational. Not from AI sessions.*
*Last updated: 2026-06-18 by vault audit.*

## Deployment
- **Live URL**: https://statenotfate.netlify.app
- **Repo**: https://github.com/rappdavid62/StateNotFate (SNF_Deploy locally)
- **Stack**: Vanilla JS PWA — index.html + app.js + index.css + service-worker.js
- **Tests**: 17 Playwright tests, all passing as of 2026-06-18

## Core App Architecture

### State (localStorage)
All state persists in browser localStorage. No backend. Key fields:
- isOnboarded, ratings (10 domains), safety (suicide/psychosis/mania)
- todayEnergy (high/medium/low/collapse), currentLayer (0-9 roadmap)
- phq9History[], polarisHistory[], polarisRestartLogs[]
- userAnchors[], mantraCompletedToday, customMantra
- reEntry {lastSeenDate, missedDays, lastMessageType}
- startupDrag, rumination, futureNarrowing, socialIsolation
- currentHopeLevel, hopeProgress, ruminationLogs[]

### Screens
- lock → welcome → stateSelector → profileDepth → intake → dashboard

### Tabs (inside dashboard)
1. **Dashboard** — daily plan, energy, today's anchors
2. **Polaris** — primary coaching tab (default if enabled)
3. **Momentum** — proof points, streaks, progress
4. **Safebox** — crisis contacts, reasons to live, safety planning
5. **Media Console** — 11-item playlist (audio + video explainers)
6. **Progression** — roadmap layers 0-9
7. **Cognitive Lab** — thought correction tools
8. **Document Center** — linked files, notes
9. **Explorer** — companion question tree

## Confirmed Live Features

### Onboarding / Intake
- Multi-screen onboarding: welcome → state selector → profile depth → intake
- Evolving companion question tree (150 questions, branching by severity)
- Energy tier selection (high / medium / low / collapse)
- PHQ-9 with exact clinical language (9 questions, scored)
- Safety screening (suicide, psychosis, mania — 0-4 scale)
- Mantra setup + MVD (Minimum Viable Day) defaults
- Dominant pattern selection (Rhythm Collapse etc.)

### Polaris Tab (Primary Coaching Engine)
- Activates as default tab once onboarded
- Proof points system (today + total + ledger with sources)
- **Possibility Collapse Modal** — paralysis bypass with 3 lanes:
  - Rhythm (Circadian Lock), Space (Space Reset), Body (Bio Floor)
  - Earns 1 proof point on lane selection
- **Startup Drag Modal** — 10-second timer intervention
  - User enters blocked task + first 10s step
  - Earns 2 proof points on success
  - Logs to startupDragHistory[]
- **Rumination Stop-Loss Modal** — 3-step grounding workflow
  - Earns 1 proof point on completion
  - Logs to ruminationStopLossCount
- **Future Narrowing toggle** — action vs. avoidance framing
- Polaris Chat (OpenAI key required) — AI coaching interface
- Quick prompt buttons for Polaris chat
- Smart Re-Entry Card — detects days missed, shows appropriate message:
  - Missed yesterday (1 day)
  - Away multiple days (2+ days)
  - Low/collapse energy override
- Anchor checklist with proof increments

### Safety & Crisis
- External safety modules loaded async: safety-detection.js, crisis-protocol.js, polaris-safety-integration.js
- Safebox tab: crisis contacts, reasons to live, distractions list
- crisis.html — standalone crisis page
- Safety check-in card triggers crisis modal on unsafe response
- 988 crisis line referenced

### Media Console
- 11-item playlist: 6 videos + 5 audio
- Titles include "State, Not A Fate" (1:37:42), "Treating depression as a systems failure" (48:09), "The Reprogramming Protocol" (1:21:49)
- Playback speed control, track navigation

### Progression / Roadmap
- 10 layers (0-9): Trust Building → Anchor Building → Stabilization → Trust Repair
- currentLayer tracked in state
- PHQ-9 history tracked for progression

### Cognitive Lab
- Thought correction entries (thoughtCorrections[])
- Gratitude journal (gratitudeJournal[])

### Other
- PIN lock / scramble security
- Personal bests tracking (longestStreak, mostAnchorsInDay, fastestRestart)
- tomorrowAnchor planning
- Custom tasks list

## Safety Modules (src/ directory)
- src/safety-detection.js
- src/crisis-protocol.js  
- src/polaris-safety-integration.js
- src/polaris_tree.js (companion question tree data)

## What Is NOT Currently in the App
*(These were in vault BUILD notes but not verified in live code)*
- Resilience & Restart Meter (24.x feature — not confirmed)
- Vault Tracker Sync button
- In-app Mini Systems Audit panel
- Emit Custom Pack (Skills tab)
- v24.x version stamp in header

## Key Files
- app.js — 5079 lines, 288KB — ALL logic
- index.html — 160KB — all UI markup embedded
- index.css — 67KB — all styles
- service-worker.js — offline + cache
- playwright.config.ts — test config, serves on port 4173