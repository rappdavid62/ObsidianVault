---
Status: Active
Primary Deployment Target: AI Infrastructure
Expected Use Case: Rules for keeping David’s second brain, AI agents, automations, prompts, frameworks, and artifact streams coherent.
Archive or Active: Active
Supersedes: 08-TECH-AND-AI/AI_SYSTEM/AI SYSTEM SYSTEM GOVERNANCE.md
Replaced By:
Canonical Home: _Meta/System Governance.md
Related Files:
  - _Meta/Master Context.md
  - _Meta/AI Command Layer.md
  - _Meta/Vault Cleanup Queue.md
Last Reviewed: 2026-06-22
---

# System Governance

## Purpose

This file defines governance rules for durable knowledge inside the system.

Its job is to prevent duplicate principles, scattered frameworks, stale prompts, unclear ownership, and AI agents creating redundant files.

Before saving any new durable asset, check this file.

## Canonical Principle Rule v0.1

Before creating a new insight, check whether the core idea already exists elsewhere in the system.

### Ownership

- **Living Memory** = personal patterns and enduring context.
- **Narrative Identity** = meaning, self-story, and identity implications.
- **Low-Energy Protocols** = executable behaviors.
- **Personal IP** = reusable frameworks, products, models, public-facing concepts, and monetizable systems.
- **Prompt Library** = reusable instructions for AI tools.
- **AI Infrastructure** = rules that govern agents, automations, file handling, source truth, sync, and system coherence.

### If multiple streams discover the same principle

1. Store the principle once in its canonical home.
2. Other streams may reference it.
3. Other streams should add only their domain-specific implication.
4. Do not restate the full principle in multiple files.

## Deployment Requirement Rule v0.1

For any new framework, protocol, principle, prompt, workflow, or reusable asset, assign exactly one **Primary Deployment Target** before saving.

Allowed deployment targets:

- State Not Fate
- Polaris
- Job Search System
- AI Infrastructure
- Prompt Library
- Personal Operating Manual
- Archive Only

If no deployment target can be identified, the asset is not mature enough for persistence and should remain a draft.

## Required Metadata Fields

Every durable asset should include:

```yaml
Status:
Primary Deployment Target:
Expected Use Case:
Archive or Active:
Supersedes:
Replaced By:
Canonical Home:
Related Files:
Last Reviewed:
```

## Supersession Rule v0.1

All durable assets should include lifecycle metadata.

Rules:

- **Active** assets are default references.
- **Experimental** assets require validation before promotion.
- **Superseded** assets remain for historical context only.
- **Archived** assets are excluded from operational guidance.
- **Archive Only** material should not be used to direct current behavior unless explicitly restored.

## AI Agent Behavior Rule v0.1

When an AI agent creates, edits, sorts, or recommends a durable file, it must:

1. Identify the file’s deployment target.
2. Identify whether the idea already exists elsewhere.
3. Avoid duplicating the same principle across multiple files.
4. Link related files instead of restating full frameworks.
5. Mark lifecycle status clearly.
6. State whether the file is operational, experimental, archived, or draft.
7. Ask whether new material belongs in an existing canonical file before creating a new one, unless the destination is obvious.

## Second Brain Coherence Rule v0.1

The vault should not become a pile of disconnected good ideas.

Every durable note should answer:

1. What is this?
2. What is it for?
3. Where does it deploy?
4. Is it active?
5. What does it replace?
6. What replaces it?
7. What should AI do with it?
8. What should AI ignore?

If a note cannot answer these, it should stay in Inbox, Drafts, or Cleanup Queue.

## Default Handling for New Ideas

When a new idea appears, classify it before saving.

Classification options:

- Principle
- Prompt
- Protocol
- Framework
- Project note
- Personal memory
- Product/IP concept
- Operational rule
- Archive/reference
- Draft/unclear

Then assign:

- Canonical home
- Primary Deployment Target
- Status
- Expected Use Case
- Next action

## Operational Rule

Do not create new system files just because a new idea sounds important.

First check:

1. Does this already exist?
2. Is this a new principle or just an implication?
3. Is there a canonical home?
4. Is this active or experimental?
5. Is this useful enough to save?
6. Can it be linked instead of duplicated?

If unsure, put it in `_Meta/Vault Cleanup Queue.md` or `00-CAPTURE/`.

## Current Status

This governance layer is active.
