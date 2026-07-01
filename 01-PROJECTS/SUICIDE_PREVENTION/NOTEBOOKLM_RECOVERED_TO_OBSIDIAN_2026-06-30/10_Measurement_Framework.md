# Non-Clinical Measurement Framework

## Core Philosophy
State Not Fate is a peer-support, recovery-scaffolding, and educational tool. **It must never attempt to perform diagnostic assessment, predict suicidal behavior, or assign clinical risk scores (such as "low," "medium," or "high" danger).** 

Instead, this framework measures **system engagement, agency indicators, and help-seeking behaviors**. It treats user interactions as indicators of participation in recovery and connection, not as clinical diagnostic markers.

---

## 1. Metric Architecture

We separate metrics into three categories: **Active Agency Indicators**, **System Engagement**, and **Help-Seeking Prompts**.

### Category A: Active Agency Indicators (Floor Wins)
*What it measures*: Small, repeatable actions that indicate the user is exercising agency over their state.
- **Anchor Completion Rate**: Percentage of daily anchors (e.g., wake regularity, morning light) marked complete.
- **MVD (Minimum Viable Day) Activations**: Frequency of days where user selects "Collapse" or "Low" energy tier and executes basic survival steps.
- **Thought Correction Submissions**: Count of thought corrections logged in the Cognitive Lab.
- **Startup Drag Timer Successes**: Frequency of successfully executing a 10-second task sequence.

### Category B: System Engagement
*What it measures*: Interaction with the educational and coping modules.
- **Educational Module Completion**: Number of course modules completed in the suicide prevention and recovery curriculum.
- **Media Console Playback Time**: Completion rates of educational audio and video files.
- **Safety Plan Creation & Updates**: Frequency of editing the local safety plan.
- **Polaris Restart Log Entries**: Tracking how quickly a user restarts after missing anchors.

### Category C: Help-Seeking Prompts
*What it measures*: Positive movements toward human connection and professional support.
- **Crisis Link Interactions**: Clicks on the 988 or 911 contact buttons.
- **Supporter Script Views**: Number of times the "Supporter Script Library" is opened (indicating intent to communicate).
- **External Resource Navigation**: Clicks routing to external peer support networks or clinical locators.
- **Emergency Checklist Bypasses**: Instances where acute distress is flagged and the app automatically bypasses menus to show support lines.

---

## 2. Privacy & Data Boundaries

To protect user safety and maintain ethical data standards, the app must adhere to strict data residency rules:

- **Local-First Storage**: All logs (anchors, safety plan details, thought corrections, MVD states) reside in the browser's `localStorage` or `IndexedDB`.
- **Zero Server-Side Logging of Crisis States**: Clicks on crisis links, emergency bypasses, or specific safety plan responses must never be transmitted to a centralized server.
- **No Diagnostic Retention**: The app does not save scores in a format that could be interpreted as a clinical chart. PHQ-9 answers are stored only to show individual historical progress to the user, with explicit warning that these scores are educational indicators, not medical records.

---

## 3. Engagement Dashboard Mockup

The user-facing "Momentum" or dashboard panel should display these metrics to build **hope-as-prediction**:

```text
==================================================
              MY MOMENTUM DASHBOARD
==================================================

[Proof Points Earned Today: 5 pts]  [Total: 124 pts]

Daily Anchors (Past 7 Days):
Mon: [X] Tue: [X] Wed: [/] Thu: [X] Fri: [X] Sat: [ ] Sun: [X]
(78% regularity - Rebuilt reward prediction)

System Actions:
- Safety Plan: [Updated 3 days ago]
- Course Modules: [3/10 Completed]
- Startup Drag Wins: [12 Total]

Help-Seeking Inventory:
- Supporter Scripts Accessed: 4 times
- External Connection Prompts: 2 completed
==================================================
```

---

## 4. Measuring Success Without Scoring Risk

Traditional apps fail by telling users "you are at high risk," which can induce panic and helplessness (state narrowing). State Not Fate reframes this by measuring progress:

| Traditional Metric | Reframe / State Not Fate Metric | Why It Matters |
|---|---|---|
| Suicidal Ideation Score (Clinical) | **Crisis Resource Views & Script Access** | Measures *readiness to act/connect* rather than distress severity. |
| Severity of Depressive Symptoms | **Anchor Checklist Regularity** | Focuses on *behavioral activation* and daily floor wins. |
| Compliance Failure Rate | **Restart Fidelity & Speed** | Rebuilt self-trust by celebrating *how quickly* the user gets back up. |
| Severity of Cognitive Distortions | **Thought Correction Logs** | Measures active engagement in cognitive reframing. |
