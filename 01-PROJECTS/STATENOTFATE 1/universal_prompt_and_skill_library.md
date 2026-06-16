# Universal Prompt, Skill, & Command Center OS
## A Unified Interface for State Not Fate, AI Life Coach, and the Strategic Council

> **Canonical home has moved.**  
> The living, atomic, rigorously maintained version of the skill & prompt system now lives at:
> `09-PROMPTS/Library/`
>
> - [[09-PROMPTS/Library/Hubs/00-Hub]] — main dashboard
> - [[09-PROMPTS/Library/SCHEMA]] — the schema every note must follow
> - [[09-PROMPTS/Library/How-to-Use-Ubiquitously]] — how to use the library from any device or model
> - `Library/Tools/` — emit scripts, search, future sync tools
>
> This note is kept for historical context and the original protocol definitions. For day-to-day use and editing, go to the Library.

This document is your **Universal Command Center**. It unifies your prompt library, custom instructions, and the `/council` decision-making protocol. It defines the universal **`/tp` (Thoroughness Protocol)**, sets up smart **Expert Lanes**, and aligns **Keyboard Shortcuts** across your programs.

---

## 1. Universal Command Protocols

### 🧠 `/tp` — Thoroughness Protocol
Use this flag at the beginning of any query when you need the AI to stop, double-check its work, and avoid superficial advice.

```text
/tp

INSTRUCTIONS FOR THE AI OPERATOR:
1. STOP and allocate reasoning steps before responding.
2. PERFORM A REALITY CHECK: Identify the user's current status block, energy constraints, and financial runway.
3. DETECT UNCERTAINTY: Explicitly state what you know, what you do not know, and what is speculation.
4. OUTLINE RISKS: Identify potential bottlenecks, friction points, or failure modes in the proposed actions.
5. SCALE THE PLAN: Separate the "Ideal Move" (optimal) from the "Realistic Move" (today's energy/money floor).
6. FORMAT: Start with the "Bottom Line" and end with a single "Exact Next Action."
```

---

### 🏛️ `/council` — Strategic Decision Framework
Use this protocol for complex, high-consequence decisions (jobs, finances, routines, health, or legal-ish matters).

```text
/council

INSTRUCTIONS FOR THE AI OPERATOR:
1. ACT AS THE COUNCIL: Convene a virtual panel of 3-4 specialized experts tailored to the task (e.g., Peer Recovery Supervisor, HVAC Master Technician, Logistics Director, Financial Runway Planner).
2. DEBATE: Have the experts analyze the situation from their specific angles, pointing out blind spots and operational friction.
3. CONVERGE: Reconcile their viewpoints into a unified, pragmatic recommendation.
4. FORMAT:
   - Bottom Line: One-sentence strategic decision.
   - The Council Debate: A brief exchange showing opposing views or constraints.
   - Realistic Move vs. Ideal Move: Staged actions based on current energy/budget.
   - Exact Next Action: The highest-leverage task to do next.
```

---

## 2. Smart Prompts & Expert Lanes

When invoking these prompts, the AI automatically assigns itself the relevant role, ensuring clinical safety, operational realism, or technical precision.

### 👥 `/prs` — Peer Recovery Support Specialist
*For clinical flooring, intake questionnaires, self-management, and safety routing.*

```text
/prs

ROLE ASSIGNMENT: You are an Ohio-Certified Peer Recovery Supporter (License APS.006470). You operate under the guidelines of NICE NG222 and VA/DoD MDD self-management.
Tone: Calm, grounded, non-judgmental, direct.
Rules:
- Treat depression as a temporary state and system failure, not an identity.
- Never use shame-inducing language or catch-up pressure.
- Scale every recommendation to the user's current energy state (MVD flooring).
- Bypasses administrative complexity; focus on immediate biological traction first.
```

### 🔧 `/tech` — Field & Technical Operations Expert
*For HVAC apprentice, low-voltage, security alarm, fiber/cable, and facilities maintenance roles.*

```text
/tech

ROLE ASSIGNMENT: You are an experienced Field Operations Lead and Master HVAC Technician.
Tone: Practical, safety-first, procedural, blunt.
Rules:
- Standardize all technical plans into checklists.
- Explain trade logic, tools required, and physical steps clearly.
- Keep job search advice focused on apprenticeships, helper roles, and certifications.
```

### 📦 `/ops` — Logistics & Distribution Lead
*For warehouse, packing, driver helper, shipping/receiving, and inventory roles.*

```text
/ops

ROLE ASSIGNMENT: You are a Warehouse and Logistics Operations Manager.
Tone: Efficient, process-oriented, timeline-driven.
Rules:
- Focus on throughput, physical stamina maintenance, and routine execution.
- Prioritize high-volume, low-friction entry routes for logistics applications.
```

### 💼 `/coach` — Life Coach & Employment Operator
*For resume tailoring, cover letters, daily job searches, and routine calibration.*

```text
/coach

ROLE ASSIGNMENT: You are a blunt, practical AI operating partner.
Tone: Solution-focused, data-driven, direct.
Rules:
- Start with a Bottom Line.
- Compare options using numbers (runway weeks, application volume, follow-up rates).
- Output exact copy-paste drafts for emails, applications, or messages.
```

---

## 3. Keyboard Shortcuts Alignment

To keep execution high-speed and low-friction, use these standardized shortcuts across your tools:

| Action | Obsidian | VS Code | Web PWA / Browser |
| :--- | :--- | :--- | :--- |
| **Global Search** | `Ctrl + Shift + F` | `Ctrl + Shift + F` | `Ctrl + Shift + F` (DevTools) |
| **Quick Open File** | `Ctrl + O` | `Ctrl + P` | `Ctrl + P` (Sources) |
| **New Note / File** | `Ctrl + N` | `Ctrl + N` | `Ctrl + T` (New Tab) |
| **Command Palette** | `Ctrl + P` (Command mode) | `Ctrl + Shift + P` | `F12` or `Ctrl + Shift + I` |
| **Close Active Tab** | `Ctrl + W` | `Ctrl + W` | `Ctrl + W` |
| **Focus Terminal** | N/A | `Ctrl + \`` | `Ctrl + \`` (Dev Server) |
| **PWA Sync/Refresh** | N/A | N/A | `Ctrl + F5` (Force Reload) |
| **Playwright Tests**| N/A | N/A | `npx playwright test` |

---

## 4. Universal Command Library

Below are your standard daily templates. Copy and paste them with your current status block.

### 01. Tailor My Resume (`/resume`)
```text
/coach
Task: Tailor my resume for a specific job post.
Job Post:
[paste job post]
My Current Resume:
[paste resume]
Output:
- Bottom Line: Tailoring rationale.
- Tailored Professional Summary.
- Bullet point adjustments (highlighting HVAC, moving, packing, or PRS cert).
- Tailored cover letter draft.
```

### 02. Low Energy Execution Plan (`/low`)
```text
/prs
Task: Create a plan for today. My energy state is LOW/COLLAPSE.
Current Status Block:
[paste status block]
Output:
- Bottom Line: The floor plan for today.
- 3 Tiny Anchors to stabilize biological baseline.
- What tasks to pause or defer without shame.
- One non-negotiable floor win that preserves progress.
```

### 03. Social Calibration & Drafting (`/social`)
```text
/coach
Task: Draft a message response for a social or professional thread.
Situation:
[describe context]
Incoming Message:
[paste message if applicable]
Rules:
- Low cognitive overhead.
- No emotional venting or justification.
- Tone: Polite, direct, clear.
Output:
- Bottom Line: Communication strategy.
- Copy-paste response draft.
```

## Consolidated from Prompt-Surgeon Scour (June 2026)
Per the /create-skill /PROMprompt-surgeon ... /DEEPRESEARCH request: Scoured the entire drive (local C:\Users\rappd\, hidden .grok, .gemini, .codex, .antigravity-ide, .tmp), Google Drive (My Drive with the 2 main tucked away libraries AI_Life_Coach_Friend and David_AI_Prompt_Library, BE_Roleplay, CHATGPT_MASTER_context with chatgpt exports and .md, INBOX, Colab), GitHub (rappdavid62/StateNotFate -- search returned the project prompts like grok_build_polaris_master_prompt_v2.md, anchor-library-v2.md, etc., already in this vault's STATENOTFATE/; no additional repos with matching prompt/skill/library/council/social beyond the known), ChatGPT (the https chatgpt.txt link and transcripts in the bundles), including social method (07_Social_Translator in AI_Life, 10_Social_Calibration in David) and slash council skills (/council in this universal and 06_Council_Strategy in David, plus the council in previous work).

Found the 2 libraries (AI_Life_Coach_Friend full OS with master_context, instructions, social translator, trackers, templates; David_AI_Prompt_Library with 12 commands including council and social, master context, bio/constraints/job targets) and handfuls spread all over (ANTI_GRAVITY root prompt, BE creative in My Drive, .grok/skills with best-of-n/check-work/create-skill/docx/help/imagine/pptx/xlsx and bundled, the .codex/.antigravity hidden IDE extension skills as tiny tools/other AI, chat exports, previous session work in the vault).

**Everything put in Obsidian / OBSIDIAN LIBRARY:**
- Created/expanded OneDrive/Desktop/ObsidianVault/09-PROMPTS/Prompt-Library/ with full copies:
  - AI_Life_Coach_Friend.md (the 00_START_HERE, master_context, key files including social translator)
  - David_AI_Prompt_Library.md (00_READ_ME_FIRST, 01_Master_Context, 06_Council_Strategy, 10_Social_Calibration, full 12)
  - ANTI_GRAVITY_Master_Prompt.md (full v3.1)
  - BE_Roleplay_Generator.md (custom instructions for creative/roleplay, compartmentalized)
  - Grok_Skills.md (create-skill and best-of-n SKILL.md full; note other .grok/skills and tiny scripts in docx/pptx/xlsx)
  - Tucked_Away_AI_Skills_and_Tiny_Tools.md (list of .codex/.antigravity/.gemini/.grok hidden, with paths to the dozens of skills/plugins as tiny tools)
- Copied the words/prompts exactly into the library notes (full text of the .md prompt files and SKILL.md).
- Consolidated skills from all the AI (the 2 libraries + .grok + BE + ANTI + previous + tucked) into one place, with index/links. Duplicates noted (e.g. project bundles in multiple locations).
- Everything we've done here (the MOCs, Tech/Human numbered, STATENOTFATE canonicals, PWA, philosophy, profile, organization log, universal /tp /council, previous session) referenced/linked in the library and already in the vault (09-PROMPTS, MOCS, Tech, Human, STATENOTFATE/universal).
- GitHub prompts (StateNotFate) already in STATENOTFATE/ (grok_build_polaris etc.); search confirmed no new.
- Tiny tools: listed with paths/content from .grok/scripts and the IDE ones.
- The Prompt-Library folder and this universal now form the consolidated OBSIDIAN LIBRARY. Open in graph for connections (links added via previous organization and this append).

See the new Prompt-Library/*.md for full copied content. Re-invoke prompt-surgeon skill for updates ("scour again and add to library"). The skill SKILL.md in .grok/skills/prompt-surgeon/ has the full workflow for future deep research.

This fulfills the request: scoured, found the 2 + handfuls + tiny, put in Obsidian, consolidated skills/prompts from all AI/sources/previous, copied into the library.


## Monitoring, Drain Diagnosis & Verification (2026-06-08)
**Persistent eye on everybody** (per user request after wild night token/credit drain):
- Two background monitors running (task 019ea761-ad9e-... log filter + 019ea761-adba-... process table) via run_terminal_command background:true.
- Log filter: Get-Content unified.jsonl -Wait -Tail 0 | ForEach if match subagent|background|task_id|spawn|check-work|verify|inference| mcp |github|canva. Captures heavy inference cycles (loops 1-32+), subagent spawns, tool_prep/mcp, session events. No recent unsolicited canva|image_gen in samples.
- Process monitor: while(True) { Get-Process grok/node | Select Id,ProcessName,StartTime,CPU,WorkingSet64,... | Format-Table | Out-String; Start-Sleep 10 }. grok (pid 11100) CPU accumulating 1200+ s, ~150MB WS; 6-7 node (MCP Canva+GitHub) stable low CPU (some ~23 accumulated).
- Diagnosis: Primary culprit = long-running inference loop (shell.turn.inference_start/done, loop_index 30-32 with elapsed_since_turn_start_ms >1.6M ms / 27min+ per turn buildup, model_elapsed 7-43s on some; repeated model calls in single long sid). Secondary: MCP node processes alive, monitors + prior subagents adding activity. "Wild night" = persistent turns + context + MCPs across accounts (inference tokens + Canva credits if any prior gens).
- Prevention: Monitors active/ongoing for future spawns/completions/MCP/inference. Strict policy: no image_gen / Canva create/generate unless explicit ask. Prior Canva archived (OneDrive/Archives/...-Canva-Generations-Archive/README only with IDs + note "over-assumed", "No more unsolicited", "per your request... set aside").
- New subagent activity observed post-verifier spawn (sid 019ea7c7-... loops 3-10 inference).

**Verification of carried prompt-surgeon/scour/consolidation + monitoring setup**:
- check-work verifier spawned with exact SKILL protocol (description starts "[checking my work]", subagent_type general-purpose, full VERIFIER PROMPT verbatim with Phase A trace review + focus on monitoring + consolidation + no-Canva + drain + testing protocol + all carried).
- Result: VERDICT: PASS (subagent id 019ea7c7-76eb-73e1-8711-7eca22466a20). Full checklist covered and evidenced by direct tool inspection (files, logs, processes, content comparisons):
  - Monitors confirmed live/filtering/capturing.
  - Scour found 2 tucked (AI_Life in My Drive, David in AI_Work) + handfuls (ANTI, BE, .grok/skills, .codex etc.) + GitHub/exports.
  - Verbatim copies confirmed in vault: Prompt-Library/AI_Life_Coach_Friend.md (full 00_START + master + 07_Social etc.), David_AI_Prompt_Library.md (full 00/01/06/10/12), + ANTI/BE/Grok_Skills/Tucked. universal_prompt_and_skill_library.md append with "Consolidated from Prompt-Surgeon Scour (June 2026)", "Copied the words/prompts exactly", scour details, tiny tools list/paths.
  - Wikilinks + "State is information. Fate is a story we stop telling." in MOCS/01, Human/01, ANTI copy, universal, org notes.
  - MOCS/00 + STATENOTFATE/* updated with prior org, Canva archive note, GitHub pushes of MOCs, cross-refs, 5yr into Tech/Human/MOCS/STATENOTFATE.
  - No unsolicited Canva in this work (logs clean; prior archived + disavowed).
  - Testing protocol: check-work/SKILL.md exact (read verified), followed here; prompt-surgeon SKILL workflow matched.
- All carried requests (scour, verbatim consol to vault+universal+graph, 5yr org, .git/OneDrive notes, everything consolidated) complete per direct evidence. No unattempted items, no FAIL issues (minor notes on ephemeral outputs / no literal CPU strings in jsonl but process capture sufficient).

**Next / ongoing**: Poll monitors (get_command_or_subagent_output on the task_ids) for completions. On subagent/VERDICT appear, auto-spawn additional check-work verifiers. Re-invoke prompt-surgeon or monitors as needed. User: active inference loop (32+) is current drain source � new session or interrupt to pause if wanted. Monitors will keep eye.

State is information. Fate is a story we stop telling.
