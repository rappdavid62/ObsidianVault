---
Status: Active
Primary Deployment Target: AI Infrastructure
Expected Use Case: Durable ledger for lessons, reusable instructions, and unresolved learning candidates discovered during DOV maintenance or external AI sessions.
Archive or Active: Active
Supersedes:
Replaced By:
Canonical Home: Meta/Second Brain Learning Ledger.md
Related Files:
  - Meta/Second Brain Operations Dashboard.md
  - Meta/Second Brain Health Report.md
  - Meta/Vault Cleanup Queue.md
  - 09-PROMPTS/Library/Hubs/00-Hub.md
  - 09-PROMPTS/Library/Skills/second-brain-control-loop.md
  - 09-PROMPTS/Library/Skills/library-gardener.md
Last Reviewed: 2026-06-28
---

# Second Brain Learning Ledger

## Bottom Line

This is the holding surface for useful lessons that should make DOV smarter over time.

Use it when a session discovers a better instruction, repeatable workflow, connector caveat, cleanup rule, or app-specific habit that should not disappear into chat history.

## Promotion Rule

Learning is not complete until it lands in the right durable home:

| Learning type | Durable home |
|---|---|
| Reusable AI behavior | `09-PROMPTS/Library/Skills/`, `Prompts/`, `Protocols/`, or `Contexts/` |
| Source-truth or cleanup risk | `Meta/Vault Cleanup Queue.md` |
| App/connector evidence | `08-TECH-AND-AI/Obsidian Integration/` or `00-CAPTURE/App Captures/` |
| Project-specific fact | Relevant project note under `01-PROJECTS/` |
| User context that should persist | `Meta/Master Context.md` or a Library context note |

Do not promote speculation. Mark it as unverified until the current session checks the relevant source.

## Inbox

Use this format:

```text
- [ ] YYYY-MM-DD | Source: chat/tool/file | Lesson: ... | Candidate home: ... | Evidence: ... | Next action: ...
```

No open learning items right now.

## Promoted

Use this format:

```text
- [x] YYYY-MM-DD | Lesson: ... | Promoted to: ... | Verification: ...
```

- [x] 2026-06-28 | Lesson: DOV needs a repeatable health report so `/brain` can monitor required surfaces, private boundaries, generated outputs, app proof, drift, and Git state. | Promoted to: `09-PROMPTS/Library/Tools/vault-health-check.py` and `Meta/Second Brain Health Report.md` | Verification: health report generated successfully and tool compiled.
- [x] 2026-06-28 | Lesson: Plugin bursts should be routed through the existing app-proof tracker and External Program Skill Wiring Matrix instead of becoming loose lists. | Promoted to: `09-PROMPTS/Library/External Program Skill Wiring Matrix.md` and `08-TECH-AND-AI/Obsidian Integration/app-proof-tracker.json` | Verification: Scite added to app tracker; plugin routing section added.
- [x] 2026-06-28 | Lesson: Health checks should include app-proof tracker counts, not only required file existence. | Promoted to: `09-PROMPTS/Library/Tools/vault-health-check.py` | Verification: health report shows 26 apps tracked, 11 complete, 8 deferred on demand, 7 deferred low priority.
- [x] 2026-06-28 | Lesson: The second brain needs an explicit daily/weekly/triggered cadence so future AI sessions do not improvise maintenance. | Promoted to: `Meta/Second Brain Runbook.md` | Verification: runbook exists and is linked from dashboard, hub, README, `/brain`, and the health checker.

## Review Loop

During `/brain`:

1. Read this ledger.
2. Promote any durable inbox item into its canonical home.
3. Move promoted items to `Promoted`.
4. Leave uncertain items in `Inbox` with the missing evidence named.
5. Refresh `Meta/Second Brain Health Report.md`.

During `library-gardener`:

1. Review only ledger items that affect the Library.
2. Validate changed Library notes.
3. Regenerate exports if mobile or external instructions changed.

During `/vault-cleaner`:

1. Review only ledger items about placement, privacy, stale paths, source truth, or cleanup queue risk.
2. Queue unresolved cleanup in `Meta/Vault Cleanup Queue.md`.
3. Do not delete or move sensitive material without explicit approval.
