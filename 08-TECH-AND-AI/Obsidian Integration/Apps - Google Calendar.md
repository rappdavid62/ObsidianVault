---
type: app-integration
source_app: Google Calendar
status: active
tags:
  - obsidian/integration
---

# Apps - Google Calendar

## Capture Path

Meeting notes and scheduled events are captured and saved to:
`06-DAILY-NOTES/Meetings/` or referenced directly inside your daily review files.

## Metadata

Every captured meeting note must include this frontmatter:

```yaml
---
type: meeting-note
source_app: Google Calendar
source_url: https://www.google.com/calendar/event?eid=NDVnbjZyaTI4OW1uOXIyaThtbjhwcjk4Z28gcmFwcGRhdmlkNjJAdQ
source_id: 45gn6ri289mn9r2i8mn8pr98go
captured_at: 2026-06-17
project: State Not Fate
people:
  - "Collaborator Name"
tags:
  - obsidian/integration
  - calendar/meeting
---
```

## Linkback

Reopen the calendar event in your Google Calendar interface using this URL:
`https://www.google.com/calendar/event?eid=<event_id>`

## Retrieval

* Link meeting notes directly inside the relevant Daily Note under a `## Meetings` header.
* Aggregate tasks and action items identified during the meeting into your primary task list.

---

## Test Capture Sample

**Title**: `Meeting - SNF PWA Design Review`
**Path**: `06-DAILY-NOTES/Meetings/Meeting - SNF PWA Design Review.md`

```markdown
---
type: meeting-note
source_app: Google Calendar
source_url: https://www.google.com/calendar/event?eid=NDVnbjZyaTI4OW1uOXIyaThtbjhwcjk4Z28gcmFwcGRhdmlkNjJAdQ
source_id: 45gn6ri289mn9r2i8mn8pr98go
captured_at: 2026-06-17
project: State Not Fate
people:
  - "Sarah Dev"
tags:
  - obsidian/integration
  - calendar/meeting
---

# Meeting - SNF PWA Design Review

*   **Time**: 2026-06-17 10:00 AM - 10:30 AM
*   **Attendees**: David Rapp, Sarah Dev
*   **Calendar Link**: [GCal Event](https://www.google.com/calendar/event?eid=NDVnbjZyaTI4OW1uOXIyaThtbjhwcjk4Z28gcmFwcGRhdmlkNjJAdQ)

## Agenda
Review current PWA frontend styling and determine HSL color tokens for the dark mode.

## Decisions
- Keep HSL-tailored colors strictly in `index.css`.
- Avoid using Tailwind styling utility overrides for the header.

## Action Items
- [ ] Refactor CSS header class in Polaris layout.
- [ ] Verify color contrast meets AA requirements.
```
