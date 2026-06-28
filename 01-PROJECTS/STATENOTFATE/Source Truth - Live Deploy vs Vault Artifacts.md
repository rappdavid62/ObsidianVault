---
Status: Active
Primary Deployment Target: State Not Fate
Expected Use Case: Prevent agents from confusing DOV vault artifacts, build archives, exports, and zips with the live State Not Fate deploy source.
Archive or Active: Active
Supersedes:
Replaced By:
Canonical Home: 01-PROJECTS/STATENOTFATE/Source Truth - Live Deploy vs Vault Artifacts.md
Related Files:
  - Meta/Second Brain Operations Dashboard.md
  - Meta/Active Projects Map.md
  - Meta/Vault Cleanup Queue.md
  - 08-TECH-AND-AI/BUILD/
  - 01-PROJECTS/STATENOTFATE/
Last Reviewed: 2026-06-28
---

# Source Truth - Live Deploy vs Vault Artifacts

## Bottom Line

Do not treat DOV vault copies, build folders, zips, downloaded exports, or historical prompt packs as the live State Not Fate production source.

Before any deployment, code validation, package install, Playwright run, Netlify update, or production fix, verify the actual external live deploy repository/folder in the current environment.

## Current Rule

Inside DOV:

- `01-PROJECTS/STATENOTFATE/` is project knowledge, source maps, exports, and context.
- `08-TECH-AND-AI/BUILD/` is vault-preserved build/artifact history.
- uploaded zips and copied bundles are archive/export materials unless explicitly restored.
- prompt and skill behavior belongs in `09-PROMPTS/Library/`.

Outside DOV:

- the expected live deploy source is a separate local repo/folder named `SNF_Deploy` or similar.
- verify the exact path, branch, remote, and current files before claiming production readiness.

## Agent Instructions

1. If the task is about concepts, prompts, project knowledge, or Obsidian organization, work in DOV.
2. If the task is about the live app, deployment, Netlify behavior, tests, package scripts, or production bugs, first verify the external live repo/folder.
3. Do not run Node/npm/Playwright from DOV unless a specific DOV artifact intentionally contains a runnable project for inspection.
4. Do not copy vault artifacts into a deploy repo without an explicit approval and a source/destination check.
5. Report local vault state, live deploy repo state, and hosted site state separately.

## Verification Checklist

Before production work, capture:

```text
Live repo path:
Git branch:
Git remote:
Last commit:
Package/test command present:
Hosted URL checked:
Vault artifact consulted:
```

## Why This Exists

DOV is the second brain and source-of-truth library. It can preserve build history and guide the project, but it is not automatically the deploy repo. Keeping this boundary explicit prevents false confidence, stale tests, and accidental edits to the wrong copy.
