# BUILD FOLDER — State Not Fate Polaris PWA Versions

**DO NOT DELETE ANYTHING IN THIS FOLDER OR SUBFOLDERS.**

This is the official build artifacts directory for the Polaris front-end of the State Not Fate (SNF) project.

## Easy to Find Structure (clearly labeled)
- `polaris-22.x/` — Base build (Smart Welcome, energy tiers, core SNF skills). Preserved.
- `polaris-23.x/` — PHQ-9 exact clinical engine + deeper library-gardener self-audit + more adaptive quests + tweaks. Preserved.
- `polaris-24.x/` — **CURRENT (24.X NOW, Netlify-fixed + premise sharpened)**: Resilience & Restart Meter + Vault Tracker Sync + Enhanced Adaptive Quests (more Library skills) + In-app Mini Systems-Audit + Emit Custom Pack + full prior features + sharpened SNF premise language + Netlify _redirects + SW no-cache headers + explicit premise boxes in UI. Deploy this entire folder (with _redirects + netlify.toml) to https://statenotfate.netlify.app. All previous versions (22.x/23.x) untouched in sibling folders.
- `PROGRESS_PROOFS.md` — Running external memory / proof log (new in 24.x cycle).
- `README.md` (this file) — Master index. Always start here.

**Rule**: Never delete previous versions. Archive by keeping the dated folders. New builds go in their own `polaris-XX.x/` sibling folder. Everything is clearly labeled with version in filenames, headers, manifests, and dedicated NOTES.md files.

## Quick Navigation
- For the live daily tool: Use `polaris-24.x/`
- For reference to previous: `polaris-23.x/` or `polaris-22.x/`
- Proofs & history: `PROGRESS_PROOFS.md`
- Each version has its own `BUILD_XX_X_NOTES.md` with preflight, features, usage, and push plan.

## Project Context (Vault = Single Source of Truth)
- Prompt / Skill Library: `../09-PROMPTS/Library/` (full gardener pass + SNF trio at v3, etc.)
- Core philosophy, trackers, project files: `../STATENOTFATE/`, `../01-PROJECTS/2026-SNF-Substrate-Systems-Project/`, `../MOCS/`, `../Tech/`
- This BUILD/ folder = frontend artifacts derived from the vault (for easy reference, local testing, and pushing to the separate StateNotFate repo).

## Library Gardener Pass 2026-06-13 (Whole Project)
**DO NOT DELETE ANYTHING** – all historical Polaris builds (22.x, 23.x, 24.x), notes, and artifacts are preserved exactly as-is in clearly labeled sibling folders and files. This gardener pass reviews the entire State Not Fate (SNF) project artifacts and integration with the prompt library, without any deletions or overwrites of prior work.

- Reviewed the full BUILD structure as the "frontend artifacts" layer derived from the vault (source of truth).
- Confirmed easy-to-find labeling: Root README indexes everything; each polaris-XX.x/ has its own BUILD_XX_X_NOTES.md with preflight, features, usage, push plan, and now gardener history.
- Sharpened the core premise across docs and UI: "State is information. Depression is a temporary multi-system state (not identity/fate). Proof (visible evidence that effort still shapes the substrate) is the corrective mechanism. Small actions + registration = progress. Restart without punishment. Energy sovereignty." (Made explicit in 24.x header/welcome/Polaris plan, and cross-referenced in STATENOTFATE/ and 09-PROMPTS/Library SNF skills.)
- Audited Dictionary compliance: New terms from 24.x (resilience-meter, vault-tracker-sync, substrate-systems-check, adaptive-quests) align with existing "philosophy-snf", "proof", "restart", "energy", "floor-wins" entries. No new domains needed; added to relevant tags in 09-PROMPTS/Library/Dictionary.md (via note).
- Atomicity: The three versioned builds are intentional historical artifacts (not redundant); 24.x is the active, with prior as reference. Core SNF philosophy files in STATENOTFATE/ remain the canonical layer.
- Links & discoverability: Added cross-refs in this README, each NOTES.md, SNF_Deploy_README.md, and grok_build_polaris_master_prompt_v2.md to the gardener pass, 09-PROMPTS/Library, STATENOTFATE/00-Hub equivalents, and Netlify site.
- Ubiquity testing: 24.x includes library integration (copy skills from 09-PROMPTS/Library, emit packs). Netlify deploy (https://statenotfate.netlify.app) uses hardened config (_redirects + netlify.toml with SPA fallback, SW no-cache headers). Local test via python -m http.server works. Emitter tests from prior gardener pass still apply.
- Grok/External sync: Artifacts in BUILD/ are manual repo-ready for StateNotFate repo push (as documented in 24.x notes). No changes to .grok/skills needed beyond existing SNF trio.
- Premise sharpened project-wide: Consistent language now in PWA UI (24.x), deploy notes, core philosophy files, and prompt skills. "State, not fate. Small actions + proof = progress." is the explicit header in key places.
- Dictionary audit complete for project artifacts; no outliers.

**Bottom Line**: Whole SNF project (prompt library + Polaris PWA artifacts + core philosophy) gardened. 24.x is the sharpened, Netlify-updated active front-end. All history preserved and easy to find. No deletions. Loop closed on recent builds/fixes.

**Updates Made**:
- This README: Added full gardener pass section + premise sharpening note.
- BUILD/polaris-24.x/BUILD_24X_NOTES.md: Appended "Library Gardener pass 2026-06-13" section with review, no-deletion confirmation, premise updates.
- BUILD/polaris-23.x/BUILD_23X_NOTES.md and polaris-22.x/BUILD_22X_NOTES.md: Added matching gardener pass notes (historical context only).
- STATENOTFATE/SNF_Deploy_README.md: Appended gardener pass + premise note.
- STATENOTFATE/grok_build_polaris_master_prompt_v2.md: Added "Library Gardener pass 2026-06-13" history bullet.
- BUILD/PROGRESS_PROOFS.md: Added entry for this pass as proof.
- 09-PROMPTS/Library/Dictionary.md (noted): Tags updated for new 24.x terms (no new domains).
- Cross-links added project-wide for discoverability.

**Dictionary Compliance**: All project notes/artifacts audited. SNF-related terms (philosophy-snf, proof, anchors, energy, restart, floor-wins, etc.) compliant. New 24.x terms folded into existing without issues. Prompt library SNF skills already at v3 from prior pass.

**Gaps Found**: 
- The actual PWA source code lives in separate StateNotFate repo/SNF_Deploy (vault BUILD/ is artifacts only). Recommend back-porting any post-deploy tweaks.
- Some STATENOTFATE/ files (e.g., bundles) could use more explicit premise sharpening in next pass.
- No major atomicity issues; versions are intentional.

**Next Gardener Focus**: 
- After real-world use of 24.x on Netlify, run in-PWA self-audit + fold back (update 09-PROMPTS/Library skills if needed).
- 25.x ideas from notes (media console, 5-year vision view, deeper job sync).
- Full re-gardener on STATENOTFATE/ canonicals + 09-PROMPTS/Library SNF skills.

**System Improvement**: 
- BUILD/ structure now serves as excellent "artifact history" layer alongside vault source of truth. Added explicit "no delete / easy to find" enforcement in all READMEs.
- Premise is now project-wide header: "State is information. Proof updates the substrate. Small actions + proof = progress."

**State noted. Small action logged. You're here.**

**State, not fate. Small actions + proof = progress.**