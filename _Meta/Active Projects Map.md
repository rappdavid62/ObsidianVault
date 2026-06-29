---
Status: Active
Primary Deployment Target: AI Infrastructure
Expected Use Case: Live map of active projects, source-truth paths, blockers, and next actions.
Archive or Active: Active
Supersedes:
Replaced By:
Canonical Home: _Meta/Active Projects Map.md
Related Files:
  - _Meta/Vault Master Index.md
  - _Meta/Master Context.md
  - _Meta/Second Brain Operations Dashboard.md
  - _Meta/Vault Cleanup Queue.md
Last Reviewed: 2026-06-28
---

# Active Projects Map

## Bottom Line

This file tells David and AI agents what projects are active and where their source-truth files live.

## Active Projects

### 1. Obsidian Second Brain / AI Infrastructure

Status: Active  
Primary Deployment Target: AI Infrastructure  
Source Path: `_Meta/`, `08-TECH-AND-AI/`, `09-PROMPTS/Library/`  
Source Truth:

- `_Meta/Master Context.md`
- `_Meta/System Governance.md`
- `_Meta/AI Command Layer.md`
- `_Meta/Second Brain Operations Dashboard.md`
- `_Meta/Vault Master Index.md`
- `09-PROMPTS/Library/Hubs/00-Hub.md`

Current Blocker: remaining generated-surface drift; old AI_SYSTEM copies are already archived and registered.

Next Action: run `/brain` weekly and use `_Meta/Legacy Bundle Migration Inventory.md` for archived AI_SYSTEM reference.

### 2. Prompt / Skill Library

Status: Active  
Primary Deployment Target: Prompt Library  
Source Path: `09-PROMPTS/Library/`  
Source Truth:

- `09-PROMPTS/Library/Hubs/00-Hub.md`
- `09-PROMPTS/Library/Dictionary.md`
- `09-PROMPTS/Library/SCHEMA.md`
- `09-PROMPTS/Library/Skills/second-brain-control-loop.md`
- `09-PROMPTS/Library/Skills/vault-cleaner.md`
- `09-PROMPTS/Library/Skills/`
- `09-PROMPTS/Library/Protocols/`

Current Blocker: legacy prompt bundle files exist under `09-PROMPTS/Prompt-Library/`.

Next Action: use `_Meta/Legacy Bundle Migration Inventory.md`; migrate only missing durable behavior into atomic Library notes.

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

Source Boundary Note: `01-PROJECTS/STATENOTFATE/Source Truth - Live Deploy vs Vault Artifacts.md`

Next Action: before live app work, verify the external live deploy repo/folder, branch, remote, and hosted state separately from DOV vault artifacts.

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
- archived old AI_SYSTEM copies registered in `_Meta/Legacy Bundle Migration Inventory.md`

## Next Project Review

Review this map after installing the Meta command layer and after the first clean `git status`.
