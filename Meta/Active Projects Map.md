---
Status: Active
Primary Deployment Target: AI Infrastructure
Expected Use Case: Live map of active projects, source-truth paths, blockers, and next actions.
Archive or Active: Active
Supersedes:
Replaced By:
Canonical Home: Meta/Active Projects Map.md
Related Files:
  - Meta/Vault Master Index.md
  - Meta/Master Context.md
  - Meta/Vault Cleanup Queue.md
Last Reviewed: 2026-06-22
---

# Active Projects Map

## Bottom Line

This file tells David and AI agents what projects are active and where their source-truth files live.

## Active Projects

### 1. Obsidian Second Brain / AI Infrastructure

Status: Active  
Primary Deployment Target: AI Infrastructure  
Source Path: `Meta/`, `08-TECH-AND-AI/`, `09-PROMPTS/Library/`  
Source Truth:

- `Meta/Master Context.md`
- `Meta/System Governance.md`
- `Meta/AI Command Layer.md`
- `Meta/Vault Master Index.md`
- `09-PROMPTS/Library/Hubs/00-Hub.md`

Current Blocker: fragmented canonical files and duplicate older AI_SYSTEM material.

Next Action: install `Meta/` command layer and archive/supersede old AI_SYSTEM copies.

### 2. Prompt / Skill Library

Status: Active  
Primary Deployment Target: Prompt Library  
Source Path: `09-PROMPTS/Library/`  
Source Truth:

- `09-PROMPTS/Library/Hubs/00-Hub.md`
- `09-PROMPTS/Library/Dictionary.md`
- `09-PROMPTS/Library/SCHEMA.md`
- `09-PROMPTS/Library/Skills/`
- `09-PROMPTS/Library/Protocols/`

Current Blocker: duplicate older prompt files exist under `09-PROMPTS/Prompt-Library/`.

Next Action: keep `09-PROMPTS/Library/` as source truth; review `Prompt-Library/` for migration/archive.

### 3. State Not Fate / Polaris

Status: Active  
Primary Deployment Target: State Not Fate / Polaris  
Source Path Candidates:

- `01-PROJECTS/2026-SNF-Substrate-Systems-Project/`
- `01-PROJECTS/STATENOTFATE 1/`
- `01-PROJECTS/STATENOTFATE/`
- `08-TECH-AND-AI/BUILD/`

Live Deployment Rule: production source must be verified against `SNF_DEPLOY`; do not assume zip exports or old folders are live source.

Current Blocker: multiple project/export folders and app zips create source confusion.

Next Action: add a clear source-truth note pointing live site work to `SNF_DEPLOY` and treat zips as archives unless explicitly restored.

### 4. Job Search / Financial Stabilization

Status: Active  
Primary Deployment Target: Job Search System  
Source Path: likely `01-PROJECTS/2026-SNF-Substrate-Systems-Project/04-Tracking/job_search_tracker.md` plus future job-search files.

Current Blocker: job search files are not yet clearly separated as their own system.

Next Action: create or update a dedicated job search project folder only if current tracker is insufficient.

### 5. Writing / Voice Corpus

Status: Active  
Primary Deployment Target: Personal Operating Manual / Personal IP  
Source Path: `05-WRITING/`

Current Blocker: some writing may be public-safe voice material; some may be private/adult and should move to `_PRIVATE/SMUT/`.

Next Action: triage writing folder for public voice corpus vs private material.

## Paused / Archive Candidates

- `State_Not_Fate_Core_Frame.zip`
- `State_Not_Fate_Core_Recovery_OS.zip`
- `State_Not_Fate_Main_Frame_Beta (2).zip`
- `.cursorrules` exports
- old `08-TECH-AND-AI/AI_SYSTEM/` copies after `Meta/` install

## Next Project Review

Review this map after installing the Meta command layer and after the first clean `git status`.
