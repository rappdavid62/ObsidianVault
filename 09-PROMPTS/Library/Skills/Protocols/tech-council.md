---
type: protocol
name: tech-council
aliases: [TCOUNCIL, /tcouncil, tech-council, tech-team-council]
description: >
  Convene a five-person tech council to evaluate apps, tools, platforms, and programs for the current situation.
  Use when choosing a stack, comparing AI tools, or deciding what is most useful to adopt next.
domain: [meta, decision-making, ai-setup, research]
energy: medium
invocation: ["TCOUNCIL", "/tcouncil", "run the tech council", "which tools should I use"]
compatible_with: [grok, claude, gpt, local]
version: 2
last_reviewed: 2026-06-18
tags: [meta, council, tools, ai-setup, model-selection, high-stakes, research]
---

# Tech Council Protocol (TCOUNCIL / /tcouncil)

## Purpose
Replace generic "best tools" advice with a structured five-perspective council that first inspects the real machine and real workflow, then ranks the most useful tools for the situation in front of us.

## When to Use
- Choosing between AI tools, apps, platforms, IDEs, note systems, or automation tools.
- Building or revising a personal or project tech stack.
- Deciding what to adopt now versus later.
- When hype is high and you need grounded tradeoff analysis.
- When the user's real workflow, runway, privacy needs, or energy limits matter more than trendiness.
- When you need to distinguish between tools already installed, tools barely used, and tools still missing.

## Core Instructions

```text
TCOUNCIL

INSTRUCTIONS FOR THE AI OPERATOR:
1. CONVENE A FIVE-PERSON TECH COUNCIL with these standing roles:
   - The Magnate: business leverage, market power, distribution, communication, ROI.
   - The Futurist: frontier capability, near-future advantage, strategic optionality.
   - The Learning Architect: cognition, learning loops, memory, motivation, human-AI interaction.
   - The Wellbeing Psychologist: adoption risk, attention cost, behavior change, safety, practical human outcomes.
   - The Engineer-Builder: technical feasibility, extensibility, speed, automation, integration, maintenance.
2. INVENTORY THE REAL MACHINE BEFORE RECOMMENDING ANYTHING.
   - First inspect the local computer for installed programs and relevant executables using available system sources such as Windows installed-program records, package managers, application directories, PATH-visible tools, and developer runtimes.
   - Normalize duplicate entries, launchers, version noise, and vendor helper apps into a clean "actual tools on this machine" list.
   - Separate the inventory into:
     1. installed and likely important
     2. installed but probably low-value or redundant
     3. missing but likely high-value
   - If local machine inspection is unavailable, say that plainly and downgrade confidence.
3. GATHER USAGE CONTEXT BEFORE DECIDING.
   - Search connected sources like Google Drive and local vault notes for workflow clues, constraints, recurring projects, pain points, and prior tool usage.
   - When possible, infer how the user actually uses tools: coding, writing, research, scheduling, note capture, publishing, automation, recovery support, job search, or communication.
   - Distinguish clearly between confirmed usage, strong inference, and speculation.
4. RESEARCH BROADLY AFTER THE LOCAL INVENTORY. Prefer current, concrete evidence over reputation or vibes.
   - Check official product docs or primary sources first.
   - Then check current community discussion when available (developer communities, Reddit, forums, product directories, etc.).
   - Use web research mainly to evaluate gaps, alternatives, and whether a missing tool is worth adding relative to what is already installed.
   - If a source or connector is unavailable, say so plainly instead of pretending it was checked.
5. HAVE EACH COUNCIL MEMBER NOMINATE 20 TOOLS independently with a one-line rationale each.
   - These nominations must be grounded in the machine inventory plus the usage context, not a generic market list.
6. RUN A REAL COUNCIL DEBATE.
   - Surface overlap.
   - Call out disagreement.
   - Compare cost, setup burden, privacy risk, learning curve, durability, lock-in, integration potential, fit for the workflow, and whether the user already has an acceptable substitute installed.
7. RANK FOR ACTUAL USEFULNESS NOW, not abstract prestige.
   - Favor "use what is already installed harder" when that is the real answer.
   - Only recommend adding new tools when the gain clearly beats learning/setup cost.
8. FORMAT THE OUTPUT as:
   - Executive summary: top five ranked with one-sentence reasons.
   - Ranked top five: why each ranked there, first use, setup burden, risks, and why it beat nearby alternatives.
   - Installed programs already owned that matter most.
   - Missing programs worth adding now.
   - Honorable mentions.
   - Council inputs: each member's 20 nominations with concise rationale.
   - Council decision process: disagreements, consensus points, and ranking criteria.
   - Source notes: where you looked and what limitations existed.
9. STAY BLUNT.
   - Do not oversell.
   - Do not flatten meaningful tradeoffs.
   - If the right answer is "you already have enough tools; use the current stack harder," say that.
   - If the machine is cluttered with overlapping tools, say which ones are redundant.
```

## Standing Council Roles
- **The Magnate**: leverage, revenue potential, platform power, communication, business fit.
- **The Futurist**: frontier capability, compounding advantage, defensibility, future-proofing.
- **The Learning Architect**: memory, retrieval, synthesis, teaching loops, user cognition.
- **The Wellbeing Psychologist**: attention cost, adoption friction, behavior sustainability, privacy and safety.
- **The Engineer-Builder**: implementation speed, extensibility, automation, interoperability, maintenance burden.

## Evaluation Criteria
- Current usefulness
- Whether it is already installed
- How much the user appears to use it
- Fit to the real workflow
- Setup burden
- Privacy and control
- Durability and lock-in
- Learning curve
- Integration potential
- Cost relative to leverage
- Evidence quality

## Output Format
- **Executive Summary**: Top five ranked with one-sentence reasons.
- **Installed Programs That Matter Most**: The important tools already on the machine and why they matter.
- **Missing Programs Worth Adding Now**: Only the best few additions, if any.
- **Ranked Top Five**: Why it ranked there, what it helps with, likely first use, setup burden, risks, and why it beat nearby alternatives.
- **Honorable Mentions**: Important near-misses.
- **Council Inputs**: Five distinct lists of 20 tools each with one-line rationale.
- **Council Decision Process**: Reasoning path, disagreements, consensus, and decision criteria.
- **Source Notes**: Main places searched plus limits and unavailable sources.

## Context to Inject
- Current project or workflow
- Existing tool stack
- Installed-program inventory
- Evidence of actual usage frequency or role importance
- Privacy constraints
- Budget/runway realities
- Energy and maintenance tolerance
- Any prior opinions already recorded in the vault

## Related
- [[tool-mode-decider]] for selecting the execution environment after the stack decision.
- [[council-strategy]] for non-tech high-stakes decisions.
- [[thoroughness-protocol]] when you need deeper evidence gathering before the council converges.
- [[ai-setup-audit]] when the question is not "what tool?" but "is the system wired correctly?"

## Notes & History
- Created on 2026-06-17 from the dedicated five-person tech-council automation.
- Revised on 2026-06-18 to require local installed-program inventory and usage-context gathering before ranking.
- This is a specialized council for tools and tech-stack decisions, not a replacement for the general `/council` protocol.

(This is the atomic version in the DOV vault - universal truth. All prompts consolidated here.)
