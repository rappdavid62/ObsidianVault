---
Status: Active
Primary Deployment Target: AI Infrastructure
Expected Use Case: Practical cadence map for running DOV as a second brain without improvising each maintenance pass.
Archive or Active: Active
Supersedes:
Replaced By:
Canonical Home: Meta/Second Brain Runbook.md
Related Files:
  - Meta/Second Brain Operations Dashboard.md
  - Meta/Second Brain Health Report.md
  - Meta/Second Brain Learning Ledger.md
  - Meta/Vault Cleanup Queue.md
  - 09-PROMPTS/Library/Skills/second-brain-control-loop.md
  - 09-PROMPTS/Library/Skills/nightly-personal-systems-review.md
  - 09-PROMPTS/Library/Skills/library-gardener.md
  - 09-PROMPTS/Library/Skills/vault-cleaner.md
Last Reviewed: 2026-06-28
---

# Second Brain Runbook

## Bottom Line

Use this runbook to keep DOV learning daily without turning maintenance into a giant chore.

The operating principle is:

```text
Nightly review captures the day.
/brain monitors the system.
library-gardener improves the skill layer.
/vault-cleaner handles placement, privacy, and source-truth drift.
vault-health-check proves the current state.
```

## Daily

Run when energy allows, ideally near the existing 9 PM review cadence.

1. Run `/nightly` from `09-PROMPTS/Library/Skills/nightly-personal-systems-review.md`.
2. Register 1-5 concrete proofs from the day.
3. Add useful reusable lessons to `Meta/Second Brain Learning Ledger.md`.
4. Add unresolved cleanup risks to `Meta/Vault Cleanup Queue.md`.
5. Stop after one first action for tomorrow.

Floor version:

1. Record one proof.
2. Name tomorrow's first tiny action.
3. Leave the rest for the weekly loop.

## Weekly

Run when the vault has changed or once per week.

1. Read `Meta/Second Brain Operations Dashboard.md`.
2. Run `python "09-PROMPTS\Library\Tools\vault-health-check.py" --write`.
3. Run `/brain`.
4. Review `Meta/Second Brain Learning Ledger.md`.
5. Run `library-gardener` only if Library notes changed.
6. Run `/vault-cleaner` only if file placement, privacy, stale paths, or source-truth drift changed.
7. Regenerate `Mobile-Favorites.md` if the portable skill surface changed.

## Triggered Runs

Run the relevant loop after these events:

| Event | Run |
|---|---|
| Major AI session found a better instruction | Learning ledger, then `library-gardener` |
| New connector/plugin/app surface used | External Program Skill Wiring Matrix and app-proof tracker |
| New file import, zip, capture batch, or old folder discovered | `/vault-cleaner` |
| Prompt, skill, protocol, or context changed | `emit-skill.py --validate <name>` and phone export if relevant |
| State Not Fate deploy/source claim | Check the SNF source-boundary note before any production claim |
| Private/adult/sensitive file found | Queue in `Meta/Vault Cleanup Queue.md`; do not quote or move without approval |

## Output Contract

Every run should leave behind:

- What was checked.
- What changed.
- What learning was promoted or queued.
- What remains unresolved.
- What was verified.
- The next smallest action.

## Completion Rule

Do not mark the whole second-brain system complete just because one report is green. Completion requires current proof that:

- The canonical skill layer is `09-PROMPTS/Library/`.
- External program surfaces route back to that layer.
- App/connector proof state is tracked honestly.
- Health, learning, cleanup, and gardening loops are wired and runnable.
- Private/sensitive boundaries are protected.
- Remaining human-approval items are explicitly queued.
