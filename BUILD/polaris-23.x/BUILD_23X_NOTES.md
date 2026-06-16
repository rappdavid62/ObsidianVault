# Polaris BUILD 23.X — 2026-06-13

**This is the CURRENT version. All previous builds preserved in sibling folders (see ../README.md). DO NOT DELETE.**

## Library Gardener Pass 2026-06-13 (Whole Project – Historical Context)
**DO NOT DELETE ANYTHING** – this 23.x (and 22.x, 24.x) preserved exactly. This pass is part of the full project gardener review (see root BUILD/README.md and polaris-24.x/BUILD_24X_NOTES.md for the complete whole-project report). No changes to prior content.

**Context from this pass**:
- 23.x remains the historical layer with PHQ-9 engine, deeper gardener self-audit, more adaptive quests, and tweaks.
- Premise sharpening (whole project): "State is information. Proof updates the substrate. Small actions + proof = progress. Restart without punishment. Energy sovereignty." Now explicit across 24.x UI and docs (cross-ref here for history).
- All versions easy to find and labeled. Dictionary terms from 23.x (phq9-engine, self-audit-button, adaptive-quests) compliant with philosophy-snf / proof / etc.
- No deletions. This 23.x is reference only; active work in 24.x.

(Full gardener report and updates are in the 24.x notes and root README. Run library-gardener after use.)

## Preflight (per Grok Build Master Prompt v2)
Same as 22.x (see polaris-22.x/BUILD_22X_NOTES.md for details). 
- Source of truth remains the Obsidian vault (09-PROMPTS/Library after full gardener + all SNF skills at v3, STATENOTFATE canonicals, Tech spec).
- Manual artifact mode because PWA code lives in separate StateNotFate repo.
- Bug triage from 22.x carried forward + new 23.x features implemented cleanly (no overbuild, respects energy tiers, no shame language, PWA = ground truth).

## How to Use This Build (Easy to Find)
1. The folder `polaris-23.x/` is self-contained.
2. Copy the **entire contents** of `polaris-23.x/` into your real deploy location (SNF_Deploy folder or StateNotFate repo root).
3. Test: Open index.html directly or `python -m http.server 8080` in the folder.
4. For Netlify: The included netlify.toml makes the whole folder deployable as a static site. It will be an installable PWA.
5. Version stamp is visible in the header as "v23.x".

All files are clearly labeled with "23.x" in titles, comments, and manifest.

## New Features Details

### PHQ-9 Exact Clinical Engine
- Button in Polaris tab: "Run PHQ-9 (exact clinical)".
- Full 9-question assessment.
- On submit: Immediate in-place result with:
  - Color-coded badge (Teal/Lavender/Orange/Red)
  - **Exact clinical interpretation paragraph** (copied verbatim from the architecture spec and master prompt).
  - Actionable recommendation box.
- History saved in state.phq9History (viewable in Dashboard).
- Does not override energy state or require clinical data in Polaris main flow.
- Example exact language (0-4): “Minimal or no depressive symptoms. This is measurable progress.” → Maintain current anchors.
- (Full mappings in app.js — matches the Tech/01_snf_pwa_antigravity_engine.md spec exactly.)

### Deeper library-gardener Self-Audit Button
- Prominent "Library Gardener Self-Audit" button in Polaris and a dedicated section in the Skills tab.
- Opens an in-PWA mini-audit panel:
  - Checklist for recent use of gardened skills (from the 2026-06-13 full pass).
  - Dictionary compliance quick check (references the fixed domains in mvd-anchors etc.).
  - Version & last_reviewed status for core SNF skills.
  - "Run full library-gardener for AI" button — copies the exact gardened library-gardener skill prompt (v3) ready for pasting into Grok/Claude/etc.
- Ties directly back to the recent full gardener work in 09-PROMPTS/Library.

### More Adaptive Quests
- In Polaris tab: New "Adaptive Quests" section (below anchors).
- Generates 2-4 tiny, energy-scaled quests on the fly:
  - High/Medium: Expansion + proof quests (e.g. from snf-hope-activation or daily-job-search).
  - Low: MVD + floor from mvd-anchors / floor-wins.
  - Collapse: Absolute minimal from sobriety-anchors + mvd.
- Each quest has a "Complete as proof" button that logs to the ledger and increments counters.
- Quests reference the exact skills from the library (e.g. "Use snf-proof-registration language when logging").
- Progress is adaptive — completing a quest on low energy can auto-suggest a hope-activation follow-up.

### Tweaks in This Build
- Header now clearly shows "Polaris 23.x — Built from 09-PROMPTS/Library gardener pass".
- Enhanced state management (better migration from 22.x if user copies over).
- More toasts for every proof/anchor/quest action (calm, precise language).
- "Copy full daily pack from Library" improved to include 23.x adaptive notes.
- Safe Box and emergency paths strengthened.
- All copy-to-AI buttons now prefix with "Source: 09-PROMPTS/Library (vault is universal truth)".
- Mobile-first tweaks in CSS (no deletion of 22.x styles — this is a fresh 23.x folder).
- Dashboard now shows recent PHQ-9 results + gardener audit summary + quest completion rate.

## Push Plan for the StateNotFate Repo (Easy & Safe)
**DO NOT DELETE ANYTHING in the StateNotFate repo either.**

Recommended safe process (preserves history):

1. **In your local StateNotFate clone / SNF_Deploy**:
   - Create a new folder or branch for archival: e.g. `git checkout -b archive/v22.x` (or just copy the current main files into a `v22.x-archive/` folder inside the repo).
   - Commit the archive with message: "Archive v22.x before 23.x build (from Obsidian BUILD/polaris-22.x — full gardener integration preserved)".

2. **Bring in 23.x**:
   - Copy the **entire contents** of `OneDrive/Desktop/ObsidianVault/BUILD/polaris-23.x/` into the repo root (overwriting the previous main files).
   - Or, for extra safety, put them in a `v23.x/` subfolder first, then promote.
   - Update any root README in the StateNotFate repo to point to the new version and link back to the Obsidian BUILD folder for reference.

3. **Commit & Tag**:
   ```
   git add .
   git commit -m "BUILD 23.x: PHQ-9 exact clinical engine + deeper library-gardener self-audit + more adaptive quests + tweaks. All features from Obsidian 09-PROMPTS/Library full gardener 2026-06-13. Preserved 22.x in archive. Netlify-ready."
   git tag -a v23.x -m "Polaris 23.x release"
   git push origin main --tags
   ```

4. **Deploy**:
   - If using Netlify on the StateNotFate repo: It should auto-deploy the new files (thanks to netlify.toml in 23.x).
   - For manual: Drag the folder (or the root after copy) to Netlify. Add a note in Netlify deploys: "23.x — PHQ-9 + gardener audit + quests".
   - Test the live URL with the new PHQ-9 modal and self-audit button.

5. **Sync back to vault (source of truth)**:
   - After any future edits in the PWA repo, fold improvements back into `../Tech/01_snf_pwa_antigravity_engine.md` and relevant skills in 09-PROMPTS/Library.
   - Run `library-gardener` skill on the prompt side.
   - Re-build future versions into this BUILD/ folder (never delete 23.x).

6. **Optional branches for safety**:
   - Keep `main` as the latest (23.x).
   - `git branch archive/v22.x` from before the merge if you prefer branches over folders.

This plan keeps everything findable, labeled by version, and nothing is deleted.

## Next Steps / Future Builds
- Run this PWA daily alongside the emitters from 09-PROMPTS/Library.
- After real usage, use the in-PWA library-gardener self-audit button, then run the real `library-gardener` skill in the vault.
- For 24.x: Could add media console, more from the 5-year model, or deeper integration with the 2026-SNF-Substrate-Systems-Project trackers.
- The full project location reminder: Vault at OneDrive/Desktop/ObsidianVault/ (09-PROMPTS/Library + STATENOTFATE + 01-PROJECTS/2026-SNF...).

All artifacts here are easy to find, clearly labeled by version, and preserve the complete history of the build process tied to the gardener work.

Built with the vault as the single source of truth. State, not fate.
