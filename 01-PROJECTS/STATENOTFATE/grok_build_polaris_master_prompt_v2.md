# Grok Build Master Prompt v2 — StateNotFateBeta Polaris / Smart Welcome / Adaptive Profile

## Library Gardener Pass 2026-06-13 (Whole Project)
**DO NOT DELETE ANYTHING** – this prompt (and related artifacts) preserved. Part of full SNF project review.

**Premise sharpened** (consistent across vault): "State is information. Depression is a temporary multi-system state, not identity or fate. Proof (visible evidence that effort still shapes the substrate) is the corrective. Small actions + registration = progress. Restart without punishment. Energy sovereignty."

See BUILD/README.md and polaris-24.x/BUILD_24X_NOTES.md for complete gardener report (no deletions, premise updates, Dictionary audit, cross-refs to 09-PROMPTS/Library and STATENOTFATE/). Vault is single source of truth.

Paste the prompt below into Grok Build.

---

You are Grok Build acting as a repository-aware implementation planning and build agent for StateNotFateBeta / State Not Fate.

Important naming rule: Grok Build is the build tool. StateNotFateBeta / State Not Fate is the product.

Your mission is to inspect the real repository and build a practical, low-friction Polaris / Smart Welcome / Re-Entry / Adaptive Recovery Profile layer into the existing static PWA without inventing architecture, overbuilding, or hiding help behind intake.

Do not treat this as a greenfield app. Do not assume React, Next, routing libraries, backend services, cloud sync, databases, or analytics unless the repository proves they exist.

SOURCE HIERARCHY
1. The live GitHub repository and local working tree are the implementation source of truth once accessible.
2. If the repo is not accessible, use the provided file bundle and GIT_CONTEXT as provisional source truth.
3. Uploaded project files, clinical overview documents, Polaris files, and prior prompt material are design/source context, not proof of current implementation unless present in repo.
4. Safety/scope rules override older copy.

KNOWN CONTEXT TO RECONCILE
Known GitHub remote from supplied context: https://github.com/rappdavid62/StateNotFate.git
Known local source folder from supplied context: C:\Users\rappd\OneDrive\Desktop\SNF_Deploy
Known tracked files from supplied context: app.js, index.css, index.html, manifest.json, service-worker.js
Current target: build Polaris into the real static PWA using index.html, index.css, app.js, manifest.json, netlify.toml if present, and service-worker.js unless repo inspection shows a newer architecture.

MANDATORY PREFLIGHT GATE
Before designing or editing, run or inspect the equivalent of:
- pwd
- git status
- git remote -v
- git branch --show-current
- git log -1 --oneline
- git fetch --all --prune if network/auth allows
- git status -sb
- gh auth status if gh exists, otherwise verify whether push/pull auth is configured
- ls / dir of project root
- inspect package files if present

Report:
A. Repository preflight result: repo path, repo name, remote URL, branch, latest commit, dirty/ahead/behind/diverged status, GitHub write status, freshness status.
B. Detected technical context: framework, package manager, routing model, app entry points, current source files, existing screens/components, existing data/state logic, docs present/missing.
C. Build mode decision: connected implementation mode, local-only implementation mode, or manual repo-ready artifact mode.
D. Approval checkpoint for destructive actions, commits, pushes, or broad refactors.

Critical correction: if repo or GitHub write access is unavailable, do not stop after asking for permission to output a plan. Continue in manual repo-ready artifact mode in the same response and produce complete copy-paste-ready artifacts, issue drafts, and proposed diffs. Stop only before actual file writes, commits, pushes, deletes, or destructive refactors.

CURRENT BUG / RISK TRIAGE TO CHECK FIRST
Before adding new features, inspect and resolve current integration issues.

Check specifically:
1. index.html references a Polaris script. Confirm the referenced filename exists in the repo. If index.html references polaris-complete.js but the file is absent or named differently, fix by either adding the correctly named file or updating the script reference.
2. Confirm script load order works with app.js state/saveState/loadState. Do not rely on globals that are unavailable at call time.
3. Inspect Polaris state initialization. Ensure state.polaris initializes all nested objects used later: day, anchors, quests, proof, resilience, profile, questionnaire, routing.
4. Confirm the Polaris tab actually renders when opened. If showTab does not call PolarisUI.render for the polaris tab, add that hook.
5. Confirm service-worker.js caches any required new JS/CSS files so the PWA works offline.
6. Run syntax checks. If no test framework exists, run at least browser-console-oriented smoke checks or node --check on JS files where valid.
7. Verify the app’s “local encryption” or privacy claims. If the code only obfuscates data, do not call it encryption in user-facing text.
8. Do not let the old Polaris copy violate the product language rules. Replace “You missed” or “failed” style copy with no-shame restart language.

PRODUCT FRAME
State Not Fate is a supportive self-management and functional stabilization system. It is not a diagnostic tool, psychotherapy, psychiatry, medical care, medication management, emergency care, or a validated clinical protocol.

Core model:
- Depression is treated as a current state and systems failure pattern, not permanent identity.
- The app targets the execution gap: the user may know what might help but cannot act because energy, initiation, reward prediction, shame, rhythm, environment, or self-trust are impaired.
- The first usable form of hope is proof: one small believable action that happened.
- Small visible action, restartable structure, friction reduction, self-language protection, meditation/mantra support, and biological floor protection are the operating mechanisms.
- Clinical care, diagnosis, prescribed medication adherence, and crisis support stay above the self-management layer.

NON-NEGOTIABLE PRODUCT PRINCIPLES
- State, not fate.
- No catch-up debt.
- No shame.
- Restart fidelity over compliance.
- One small action beats full understanding.
- Progress pauses; it never resets.
- Default to low friction.
- Depth is always available.
- Personalization is optional.
- Help is never locked behind intake completion.
- Users can explore the full program anytime.
- Collapse mode gets action before questions.

VOICE AND COPY RULES
Write like a calm, intelligent operating system. Not a therapist, not a coach, not a friend, not a productivity app, not a motivational brand.

Use language like:
- You’re here.
- No catch-up.
- Pick the current state.
- We’ll keep this small.
- Nothing reset.
- Start with the floor.
- Make it smaller.
- State, not fate.
- Action happened.
- Proof logged.

Avoid:
- journey
- empower
- thrive
- crush your goals
- be your best self
- try harder
- you should
- just
- back on track
- failed
- streak broken
- lost progress
- start over
- what’s your why?
- unlock your potential
- forced positivity
- therapy clichés

SMART WELCOME / RE-ENTRY OBJECTIVE
Create a first layer that appears on first open, first open of day, meaningful re-entry, collapse mode, emergency mode, or repeated friction. It is a routing engine, not a motivational welcome screen.

It must serve three user types:
1. Collapsed user: can barely press one button; needs the smallest useful action.
2. Curious user: wants to understand the whole program before acting; needs full access without forced intake.
3. High-agency user: wants precision; needs optional deeper questionnaire and personalization.

First screen must offer four paths:
- Start Small
- Explore Full Program
- Personalize More
- Emergency Floor

Never hide the program. Never force intake before help.

STATE SELECTOR
Question: “What is blocking action right now?”
Use 5–6 options maximum, functional language only:
- I can’t start
- My rhythm is broken
- My space is dragging me down
- My body needs the floor
- My mind is spiraling
- Emergency mode

No open text fields before action. No mood scale before action.

FIRST TINY ANCHOR RULES
For each selected blocker, recommend one tiny anchor that is 30 seconds to 2 minutes, concrete, physical when possible, no journaling, no complex reflection, no belief required, no motivation required, no explanation required.

Recommended mapping:
- I can’t start → Put both feet on the floor and stand once.
- My rhythm is broken → Open blinds or stand by a window for 30 seconds.
- My space is dragging me down → Put one visible piece of trash in a trash bag/bin.
- My body needs the floor → Drink water or take prescribed meds if due.
- My mind is spiraling → Say: “This is a state, not a fate,” then touch one physical object and name it.
- Phone/bed trap, if detected → Place phone one arm-length away and sit upright.
- Social withdrawal, only after floor stability → Send one low-demand check-in or save a draft.
- Emergency mode → Route to Emergency Floor; do not gamify.

After anchor attempt, ask only:
- Did the action happen?
Choices: Done / Too hard / Make it easier / Go to 10-Minute Floor / Personalize More / Explore Full Program.
Optional second question: Was it too hard, okay, or easy?
Do not ask “Did this make you feel better?”

RESTART / PAUSE PROGRESSION RULES
States:
- New User
- Active Returning: last active under 48 hours
- Short Gap: away 2–3 days
- Medium Gap: away 4–14 days
- Long Gap: away 15+ days
- Collapse Mode
- Emergency Mode

Copy examples:
- Under 48 hours: “You’re here. Continue or make it smaller.”
- 2–3 days: “No reset. Pick the floor.”
- 4–14 days: “Progress paused. Nothing is erased.”
- 15+ days: “Long gap. Still not zero. Start with the floor.”
- Base too hard twice: “Make it smaller. Friction is data.”

Behavior:
- Preserve earned status.
- Pause progression, do not reset.
- Do not ask why the user was gone.
- Offer a smaller version of the last known base.
- Route to Debug/Friction Mode if “Too hard” repeats.

ADAPTIVE RECOVERY PROFILE
Do not call it a diagnostic questionnaire in user-facing language. Call it Adaptive Recovery Profile or Personalization.

It must be optional, transparent, editable, progressively built, skippable, useful when incomplete, local-first, exportable, resettable, and deletable.

Personalization choices:
- No personalization. Just start.
- One question.
- Short guided intake.
- Full questionnaire.
- Review or change previous answers.

Profile domains may include energy, sleep/wake rhythm, food/hydration, medication routine if relevant, hygiene, movement, psychomotor slowing, initiation difficulty, environmental drag, phone/bed trap, anhedonia, shame/rumination, anxiety/panic overlap, social isolation, admin/financial stress, work/job stress, substance-use impact, pain/disability, attention/brain fog, avoidance loops, self-worth beliefs, current safety risk, professional-care status, preferred time of day, best cue type, smallest believable action, preferred tone, reading tolerance, sensory sensitivities, restart pattern, recovery stage, and disliked/forbidden interventions.

Do not ask all domains at once unless the user explicitly chooses Full Questionnaire.

QUESTIONNAIRE EVOLUTION RULES
- Never force a question before a tiny action in collapse mode.
- Never ask more than one micro-question after an anchor unless the user chooses more.
- Prioritize missing fields that immediately improve routing.
- Deprioritize sensitive fields unless needed for safety or voluntarily opened.
- If “Too hard” repeats, ask friction questions, not motivation questions.
- If skips repeat, reduce question frequency.
- Always allow edit, reset, review, skip, and continue later.
- Explain why a question is asked in one short sentence when useful.

RECOMMENDATION LOGIC RULES
Do not recommend social tasks first if main blocker is room chaos.
Do not recommend journaling first if main blocker is psychomotor slowing.
Do not recommend meaning-work first if biological floor is unstable.
Do not recommend complex planning to initiation paralysis.
Do not recommend intense exercise in collapse.
Do not recommend shame-heavy tracking to restart failure.

Mapping:
- Rhythm Collapse → light, wake cue, water, food, phone boundary, sleep gate.
- Environmental Drag → trash, dishes, laundry, launch surface, floor path.
- Initiation Paralysis → feet on floor, stand, second location, first physical step.
- Biological Depletion → water, food, meds-if-prescribed, bathroom, hygiene.
- Shame Spiral → operating sentence plus physical action, no self-analysis first.
- Anhedonia → proof-based action, sensory sampling, movement, low-pressure reward test.
- Social Isolation → low-demand contact only after floor stability.
- Admin/Financial Threat → one document, one call attempt, one message draft.
- Phone/Bed Trap → phone relocation, bed exit, light, body transition.

GAME / ENGAGEMENT DESIGN RULES
Build return loops around proof, relief, identity continuity, and small visible progress — not streak pressure.

Allowed engagement mechanics:
- Proof Ledger: action happened.
- Return Wins: coming back counts.
- Floor Wins: collapse-day minimums count.
- Resilience Rate: restart speed, not streak purity.
- Tiny Quests: one physical action, one screen.
- Companion presence: calm, slightly mythic, optional.
- Optional avatar skins including goth/dark/funny choices such as bat, skeleton, mummy, ghost, bear, raven, moth.
- Unlocks must be cosmetic, explanatory, or narrative only; never lock core help.

Forbidden engagement mechanics:
- streak shame
- loss aversion that punishes depression
- red failure states
- social sharing prompts
- leaderboards
- guilt badges
- “comeback” language implying failure
- gamifying emergency mode

UI / UX RULES FOR DEPRESSED AND LOW-ENERGY USERS
- Mobile-first.
- One decision per screen in collapse mode.
- No dense text on first screens.
- No hidden primary action.
- Big buttons: minimum 44px tap target.
- Strong contrast, low visual noise.
- Minimize scrolling on first action screens.
- One-thumb operation where possible.
- Animation subtle, optional, and never blocking.
- Persistent escape paths: Make Smaller, Emergency Floor, Explore Full Program, Skip.
- Reading tolerance should affect copy length.

SAFETY AND CLINICAL SCOPE
Any feature touching emergency mode, self-harm, medication, diagnosis, crisis routing, severe intoxication/withdrawal, mania, psychosis, or professional-care boundaries requires clinical/safety review before release.

Emergency Floor should route to stabilizing language and crisis/professional support. It must not diagnose, treat, promise safety, or replace emergency help. It must never tell users to stop prescribed medication.

Use careful language: “This is outside the self-management layer.”

REQUIRED IMPLEMENTATION DELIVERABLES
Produce a complete plan and, when approved, small coherent diffs. Use the existing static PWA architecture unless repo inspection proves otherwise.

Required sections:
1. Repo inspection summary.
2. Current bug triage and fix order.
3. Product spec: Smart Welcome / Re-Entry, Adaptive Recovery Profile, Evolving Questionnaire.
4. UX copy library.
5. Logic rules: routing, triggers, recommendations, questionnaire evolution, restart/pause progression.
6. Data schema: profile fields, questionnaire bank, routing decision, recommendation, restart status, safety flag.
7. Suggested file changes mapped to actual repo structure.
8. MVP / Soon / Later split.
9. GitHub-ready issues.
10. Tests/smoke checks.
11. Risks, rollback plan, and approval checkpoint.

MVP IMPLEMENTATION PRIORITY
MVP must include:
- current Polaris integration hotfixes
- Smart Welcome first screen
- State Selector
- tiny anchor mapping
- restart logic basics
- personalization depth choice
- Adaptive Recovery Profile minimal schema
- questionnaire bank MVP
- recommendation matching MVP
- full program access path
- Emergency Floor route stub with safety-review flag
- service worker update if new files are added
- docs/update notes or issue backlog

Soon:
- evolving questionnaire refinement
- profile edit/reset screen
- recommendation explanations
- profile completeness indicators
- friction debugging
- restart pattern analysis
- accessibility polish
- export/import profile data

Later:
- advanced personalization
- clinician/share summaries
- deeper evidence notes
- optional analytics dashboard only with explicit approval
- multi-device sync only with explicit approval
- automated GitHub issue creation only if authenticated and approved

OUTPUT FORMAT FOR THIS RUN
If connected implementation is available and you have approval to edit, propose file changes first, then wait for explicit approval before editing.
If local-only mode, produce diffs but do not commit or push.
If manual mode, produce copy-paste-ready file contents and issue drafts in the same response.

Do not end with only “Approve this plan and I will output the plan.” The plan is part of this response. End with: “Approve these file changes and I will implement the MVP as small diffs.”

FINAL STANDARD
Immediate usefulness first.
Full transparency always.
Personalization by choice.
Depth available on demand.
No punishment for collapse.
State, not fate.

## Synthesized additions from Grok organization session (June 2026)
AI systems and execution layer integrated:

- AI Life Coach Friend: blunt execution operator, bottom-line first, no fluff/therapy. Response format: Bottom Line / Reality Check / Ideal Move / Realistic Move / Exact Next Action / Risks / Updated Status Suggestion. Daily status block ritual, trackers, templates for low energy, social, job, weekly review.
- David AI Prompt Library: 12 action commands (job search, apply, resume, research, low energy execution, social calibration, etc.). Master context with bio (David, Cincinnati, PRS cert APS.006470, job targets field tech/PRS/HVAC priority, constraints, work history).
- Shared with PWA: Same principles (proof/anchors, low friction, restart without shame, ideal/realistic, energy awareness, external memory, blunt tone). Life Coach + Prompt Library for stabilization layer (job as floor-building). Anti-Gravity for PWA-specific (Polaris, Floor Win, exact UI).
- Past sessions (Grok/Build) built/refined these and PWA (repo-aware preflight, bug triage for Polaris/state, media for explainers).

See [[00_grok_organization_log]], [[02_ai_systems_moc]], [[01_snf_pwa_antigravity_engine]], [[02_ai_life_coach_and_prompt_library]] for full.
