---
Status: Active
Primary Deployment Target: AI Infrastructure
Expected Use Case: Guidance for safe git sync and conflict resolution across devices.
Archive or Active: Active
Supersedes:
Replaced By:
Canonical Home: Meta/Device_Sync_Protocol.md
Related Files:
  - git-sync.ps1
  - Meta/Master Context.md
Last Reviewed: 2026-06-25
---

# Device Sync Protocol

## Purpose
This document governs safe synchronization of David's second brain vault across different devices (laptop, desktop, phone) using Git.

## Core Sync Rules
1. **Always Pull Before Committing**: To prevent merge conflicts, always pull remote changes before staging and committing local updates.
2. **Never Force Push**: Never use `git push --force` or `--force-with-lease` unless resolving a specific detached head or history rewrite requested by David.
3. **Verify Gitignore Before Sync**: Ensure sensitive/private content (e.g., `_PRIVATE/`, `99-PRIVATE/`, `40-BREAST EXPANSION/`) is ignored and not tracked.
4. **Use Local Backups**: Keep automated local zip snapshots under `.backups/` as a safety net in case of sync failures.
5. **Reorg Alignment**: Maintain folders like `00-CAPTURE/`, `02-PROJECTS/`, `99-PRIVATE/` across all instances instead of recreating deprecated `00-INBOX/` or `01-PROJECTS/` paths.
