---
type: app-integration
source_app: Gmail
status: active
tags:
  - obsidian/integration
---

# Apps - Gmail

## Capture Path

Actionable emails (job leads, interview requests, or billing alerts) are captured and saved to:
`00-INBOX/App Captures/` (for sorting) or directly inside relevant project/tracker folders.

## Metadata

Every captured email note must include this frontmatter:

```yaml
---
type: email-action
source_app: Gmail
source_url: https://mail.google.com/mail/u/0/#inbox/18f3a09e88d47bf1
source_id: 18f3a09e88d47bf1
captured_at: 2026-06-16
project: State Not Fate
people:
  - "Sender Name"
tags:
  - obsidian/integration
  - email/action-item
---
```

## Linkback

Reopen the exact message or conversation thread in your browser using this format:
`https://mail.google.com/mail/u/0/#inbox/<thread_id>`

## Retrieval

Use these captured notes during your **Daily Status Update** or **Daily Job Search** sessions:
* Check for unresolved email actions inside the inbox.
* Extract contact info and next steps to log into [job_search_tracker.md](file:///C:/ROOT_OBSIDIAN/master-laptop-vault/01-PROJECTS/2026-SNF-Substrate-Systems-Project/04-Tracking/job_search_tracker.md).

---

## Test Capture Sample

**Title**: `Gmail - Interview Request - Clark And Sons`
**Path**: `00-INBOX/App Captures/Gmail - Interview Request - Clark And Sons.md`

```markdown
---
type: email-action
source_app: Gmail
source_url: https://mail.google.com/mail/u/0/#inbox/18f3a09e88d47bf1
source_id: 18f3a09e88d47bf1
captured_at: 2026-06-16
project: Job Hunt 2026
people:
  - "Marcus Clark"
tags:
  - obsidian/integration
  - email/action-item
---

# Gmail - Interview Request - Clark And Sons

*   **From**: Marcus Clark <mclark@clarkandsons.com>
*   **Subject**: Interview Scheduling: Low-Voltage Field Technician
*   **Date**: 2026-06-16

## Content Summary

Marcus wants to schedule a 30-minute phone call to discuss the Field Technician opening. He offered times on Thursday (2026-06-18) between 9:00 AM and 1:00 PM.

## Next Action

- [ ] Reply with availability (Thurs at 10:30 AM or 11:00 AM).
- [ ] Add event to Google Calendar once confirmed.
- [ ] Log entry in `job_search_tracker.md`.
```
