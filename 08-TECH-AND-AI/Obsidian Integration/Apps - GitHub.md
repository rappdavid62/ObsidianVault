---
type: app-integration
source_app: GitHub
status: active
tags:
  - obsidian/integration
---

# Apps - GitHub

## Capture Path

This vault is connected to GitHub at `https://github.com/rappdavid62/ObsidianVault.git` on the `main` branch, serving as the universal source of truth for all notes, prompts, trackers, and systems.

Syncing occurs in two ways:
1. **Automated Sync (Obsidian UI)**:
   - Configured via the `obsidian-git` community plugin.
   - Automatically pulls, commits, and pushes every **10 minutes** while Obsidian is active.
   - Automatically pulls changes from GitHub upon Obsidian boot.

2. **CLI Sync (Terminal)**:
   - Automated by running the script at the root: [git-sync.ps1](file:///c:/ROOT_OBSIDIAN/DOV/git-sync.ps1)
   - Stages all modified and untracked files (excluding `.codex/` and other files defined in `.gitignore`), commits with a timestamped message, pulls remote changes, and pushes to origin.

## Metadata

- source_app: GitHub
- source_url: https://github.com/rappdavid62/ObsidianVault
- source_id: main
- captured_at: 2026-06-16

## Linkback

- Repo URL: https://github.com/rappdavid62/ObsidianVault

## Retrieval

- Emitters and scripts (e.g. `sync-to-grok.py`, `build-master-context.py`) pull directly from this synced vault, ensuring cross-platform tools stay updated to the canonical GitHub source.

## Test Capture

- [x] Configure git remote connection
- [x] Setup `obsidian-git` plugin auto-push & auto-pull
- [x] Create and verify [git-sync.ps1](file:///c:/ROOT_OBSIDIAN/DOV/git-sync.ps1)
- [x] Complete initial full sync to GitHub main

