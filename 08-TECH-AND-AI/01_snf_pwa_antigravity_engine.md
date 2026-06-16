# SNF PWA & Anti-Gravity Engine (Update 3 Architecture)

**The implementation of State Not Fate as a static, offline-capable Progressive Web App (PWA) plus its integrated AI coaching layer (Anti-Gravity Engine / Grok Build prompts). Ground truth from ANTI-GRAVITY_2.0_MASTER_PROMPT_vUpdate3_Refined_Structure.md (canonical as of 2026-06-07), the Grok Build Polaris prompt v2 in vault, session history (PWA edits, Polaris integration), SNF_Locked_v2.0_2026-06-01/ + V2/ + INBOX backups in My Drive, and Depapp/SNF_Deploy files.**

**Live PWA is the single source of truth for UI/state/behavior.** (http://localhost:8080 or deployed; test with `python -m http.server 8080` from SNF_Deploy). Service worker cache v3; offline reload supported; mobile responsive.

## Energy Model (Critical — Adaptive Everything)
Four tiers. PWA UI + AI responses map reported state instantly:
- **High**: Full checklist + high-agency tasks; anchors = expansion + meaningful.
- **Medium**: Standard checklist; balanced anchors.
- **Low**: MVD (Minimum Viable Day) only; safety + regulation focused.
- **Collapse**: MVD floor + warning banner; minimal safety anchors only.

Never push high-agency on low/collapse. Respect "Energy Sovereignty."

## Polaris Tab (Default Landing for Onboarded / Returning Users)
- Enable/disable toggle (clean switch; re-enable button when off).
- **Today’s Plan**: Contextual paragraph (AI generates/adapts by energy tier).
- **Anchors Checklist**: Interactive, energy-adaptive. Each completion = +1 today proof. Collapse = minimal safety only.
- **Proof Points**: Running total + today’s count. Ledger updates on anchor complete or Floor Win.
- **Resilience Info**: Current streak, longest streak, missed days.
- **Action Row**:
  - 🔥 Log Floor Win (teal toast) — legitimate proof of presence, no performance requirement.
  - Restart Day (resets only today’s anchors/proof; confirmation toast).
- **Settings Row** (first button primary lavender): 📊 View Full Dashboard (switches tab), Customize Treatment Plan, Safe Box.
- Polaris state shape (initialized on migration, non-clinical data only; clinical notes would use existing PIN scramble):
  ```js
  polaris: {
    enabled: boolean,
    proof: { total, today, ledger: [...] },
    anchors: { active: [...] },
    streaks: { current, longest, missed },
    lastReset: timestamp
  }
  ```

**Security/Privacy rule (verbatim)**: Polaris stores only non-clinical data. If clinical notes or free-text reflections ever added to proof ledger or quests, encrypt with existing PIN scramble/descramble. Update saveState() + decryptStateData().

## Other Key Screens / Features (Quick Reference)
- **Welcome / Onboarding (Phase 0 / Trust Landing)**: Four buttons — Start Small (→ state-selector 6 states → energy + Dashboard), Explore Full Program (Intake or Dashboard), Personalize More (Quick/Standard/Minimal profile), Emergency Floor (Safe Box + auto-onboard).
- **Dashboard**: Energy check-in, adaptive daily tasks, hope meter, mantra, analytics.
- **Safe Box**: Crisis plan, hotlines (988+), linked writings, emergency resources.
- **Progression**: Timeline + PHQ-9 history (with prior interpretations).
- **Worksheets**: Gratitude journal, thought challenge, Treatment Plan Customizer.
- **Document Center**: PHQ-9 history table + file explorer.
- **Media Console**: Playlist + playback (explainers: State Not A Fate, The Depression Project, The Mechanics of State vs..., The Broken Firmware, Reprogramming Protocol, etc.).
- **Explorer**: Concept reference.
- **PHQ-9 Assessment + Clinical Interpretation Engine** (modal, 9 questions): On submit → in-place result panel with color-coded score badge, severity text, **full clinical interpretation paragraph using exact language below (never paraphrase)**, actionable rec box. Saved to state.phq9History[].
  Exact (from master prompt):
  - 0–4 (Minimal) — Teal: “Minimal or no depressive symptoms. This is measurable progress.” → Maintain current anchors.
  - 5–9 (Mild) — Lavender: “Some difficult days but retain partial functioning.” → Monitor, reassess in 2 weeks.
  - 10–14 (Moderate) — Orange: “Persistent low energy, disrupted sleep, difficulty starting tasks.” → Consider treatment plan review.
  - 15–19 (Moderately Severe) — Orange/Red: “Routine daily tasks significantly harder, self-motivation unreliable.” → Active treatment recommended.
  - 20–27 (Severe) — Red: “Significantly impairs daily functioning, requires professional intervention.” → Contact clinician immediately. 988 if in crisis.
- **Toast Notification System** (replaces all alert()): Top-right glassmorphism; types success (teal: Floor Win, anchor done, plan saved), warning (orange), error (red: PIN wrong), info (lavender). ~4s auto-dismiss. Slide-in. Zero blocking popups.
- **Smart Welcome & Back buttons**: Proper nesting, state management via app.js.

## PWA Technical Notes
- Static: index.html, app.js (main logic/state/save/load/DEFAULT_STATE with ratings for sleep/morning/initiation/clutter/energy/shame/hygiene/eating/social/meaning + safety suicide/psychosis/mania + customMantra + MVD list + negativeBeliefs etc.), index.css, manifest.json, service-worker.js.
- State persistence local (with PIN scramble option for sensitive).
- GitHub: https://github.com/rappdavid62/StateNotFate (from build prompts); local SNF_Deploy, locked v2 copies, V2, INBOX/State_Not_Fate_v2.0_Full_Backup in Drive.
- Preflight for builds (Grok Build prompt): pwd, git status/remote/branch/log/fetch, gh auth, ls, inspect files. Report repo freshness, tech context (static HTML/JS), build mode (connected vs manual artifact). Bug triage first (Polaris script name match, state init for nested polaris objects, render hook in showTab, sw cache for new assets, no-shame language, "local encryption" claims accurate to obfuscation).
- Product frame: Supportive self-management/functional stabilization. Not diagnostic, psychotherapy, psychiatry, medical, emergency, or validated clinical protocol. "Depression is treated as a current state and systems failure pattern, not permanent identity."

## Anti-Gravity Engine (AI Coaching Layer for the PWA)
You (Grok/AI) are the **Anti-Gravity Engine** — integrated intelligence/coaching for the SNF PWA and broader project.
- **Core Mandate**: Make the next right action obvious, low-friction, and proof-generating — even on zero-motivation days. Treat current state as data, never identity or fate.
- **Non-negotiables**: PWA = ground truth (never contradict arch); clinical accuracy (exact PHQ-9 language); fantasy boundary (GF MODE ON only for creative/roleplay/BE; never blend); no blocking alerts (use toasts); energy sovereignty (respect tiers); Floor Wins valid; self-compassionate precise tone (dry wit OK, no judgment).
- **Interaction Protocols** (A: state/energy/plan request; B: PHQ-9 shared; C: simulate UI action; D: general):
  1. Acknowledge without judgment: “State, not fate. This is data.”
  2. Map to tier + state what PWA will display.
  3. Deliver/refine Today’s Plan paragraph for Polaris.
  4. Generate 3–7 energy-appropriate anchors (checklist format).
  5. Explain proof mechanics briefly.
  6. Offer Floor Win on low/collapse.
  7. Exact UI action: “Open Polaris tab → toggle anchors... For instant proof, hit 🔥 Log Floor Win.”
  8. Tie to 5-year vision only when natural.
  9. Always end with one concrete micro-action in the actual PWA in next 60s.
- **Output standards**: Direct ack of state/question; exact clinical PHQ-9; reference specific PWA elements (tab names, buttons, toast colors); low-friction/proof-oriented; one clear next micro-action.
- **Model self-audit** (internal before reply): Map to correct tier? Exact PHQ-9? Fantasy boundary respected? PWA UI elements referenced? Floor Win offered on low days? One micro-action in PWA? Tone precise/non-shaming/infrastructure-focused?
- Also governed by Grok Build v2 prompt for implementation work (repo-aware, preflight, bug triage, manual artifacts if needed, no overbuilding).

## How It Connects to the Rest
- **Philosophy** ([[01_snf_core_philosophy]], [[../STATENOTFATE/]] canonicals): Energy-adaptive anchors, proof, restart no-shame, stabilization before expansion, front-end trust, matched moves — all implemented in UI + AI layer.
- **AI Execution** ([[../MOCS/02_ai_systems_moc]], [[../Tech/02_ai_life_coach_and_prompt_library]]): Shared blunt operator rules, status blocks, ideal/realistic, trackers, low-energy plans, context engineering. AI Life Coach Friend for broader life/job; Anti-Gravity specific to PWA/Polaris.
- **Human context** ([[02_personal_profile_5year_vision]]): 5yr vision, PRS cert, sober date, constraints, history → shape adaptive rules + realistic moves.
- **Past conversations** (.grok/sessions chat_history/updates, bundles): Used to build/debug PWA (HTML/JS edits, Polaris, media), refine these exact prompts, explore sources, create bundles that fed back into the system.
- **Knowledge**: Obsidian (this vault + MOCS + STATENOTFATE + Human/ + Tech/) + GitHub (code) + Drive (bundles, backups, locked v2) as external memory.

**The PWA + Anti-Gravity is the living embodiment of "State, not fate" — proof infrastructure you interact with daily, coached by an AI that knows the exact UI and your real constraints.**

Sources: ANTI_GRAVITY master prompt (full), vault grok_build_polaris...v2.md, session artifacts (app.js snippets with DEFAULT_STATE/MVD/mantra, HTML welcome/Polaris), My Drive SNF_Locked_v2.0_2026-06-01/ + V2/ + INBOX backups + codex bundles, Depapp/, local SNF_Deploy if present, comprehensive project PDFs.

See [[../MOCS/00_grok_organization_log]] (parent), [[../MOCS/01_state_not_fate_moc]], [[../MOCS/02_ai_systems_moc]], Human/ notes, [[SNF_Deploy_README]] and Polaris prompt, live PWA files.
