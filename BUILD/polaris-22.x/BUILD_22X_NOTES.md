# Polaris BUILD 22.X — 2026-06-13

**Status**: Complete self-contained static PWA build.

## Preflight (per Grok Build Master Prompt v2)
- Repo context: Primary truth in ObsidianVault (prompt library + specs). PWA code lives in separate StateNotFate repo (https://github.com/rappdavid62/StateNotFate) or local SNF_Deploy folder.
- Local workspace checked: No live frontend files found under current Obsidian path (they live in dedicated deploy folder or the StateNotFate repo). Proceeding in manual repo-ready artifact mode.
- Technical context: Pure static (index.html + app.js + css + sw + manifest). No framework. Offline-first PWA.
- Build mode: Manual artifacts produced here for immediate use / copy to your SNF_Deploy or StateNotFate repo.
- Bug triage addressed in 22.x:
  - Polaris tab always renders correctly.
  - State initialization includes nested polaris objects.
  - Energy-adaptive anchors from gardened SNF skills (09-PROMPTS/Library).
  - Floor Win first-class + direct tie to snf-proof-registration.
  - No-shame restart language throughout.
  - Smart Welcome / Re-Entry per master prompt (4 paths, collapse protection, no forced intake).
  - Library integration: Skills tab with copy-to-AI for the exact gardened skills (sobriety-anchors, hope-activation, proof-registration, mvd, floor-wins, library-gardener).
  - Service worker caches new assets.

## Library Gardener Pass 2026-06-13 (Whole Project – Historical Context)
**DO NOT DELETE ANYTHING** – this 22.x (and 23.x, 24.x) preserved exactly. This pass is part of the full project gardener review (see root BUILD/README.md and polaris-24.x/BUILD_24X_NOTES.md for the complete whole-project report). No changes to prior content.

**Context from this pass**:
- 22.x remains the historical base layer with Smart Welcome, energy sovereignty, SNF skills integration, proof ledger, and Netlify-ready setup.
- Premise sharpening (whole project): "State is information. Proof updates the substrate. Small actions + proof = progress. Restart without punishment. Energy sovereignty." Now explicit across 24.x UI and docs (cross-ref here for history).
- All versions easy to find and labeled. Dictionary terms from 22.x compliant with philosophy-snf / proof / etc.
- No deletions. This 22.x is reference only; active work in 24.x.

(Full gardener report and updates are in the 24.x notes and root README. Run library-gardener after use.)

## How to use this build
1. Copy the entire polaris-22.x folder to your SNF_Deploy / StateNotFate working tree (replace or merge the existing index.html, app.js etc.).
2. Test locally: `cd polaris-22.x && python -m http.server 8080` (or any static server).
3. For Netlify: drag the folder or push to a repo with the included netlify.toml. It will be instantly installable PWA.
4. The PWA pulls its core language and skills directly from the gardened 09-PROMPTS/Library (hardcoded in app.js for offline resilience; update by re-building after future gardener passes).

## Connection to the rest of the project
- Skills come from 09-PROMPTS/Library (after full gardener + tests).
- Philosophy & adaptive rules from STATENOTFATE/ + Tech/01_snf_pwa_antigravity_engine.md.
- This is the front-end embodiment of "State, not fate".

Run `library-gardener` after significant PWA use to keep the prompt side in sync.

Everything from the previous full library gardener pass is now usable inside the actual app a user can install.

Next logical: 23.x could add PHQ-9 exact clinical engine, more adaptive quests, or deeper library-gardener self-audit inside the PWA.

Built with the vault as source of truth. 
