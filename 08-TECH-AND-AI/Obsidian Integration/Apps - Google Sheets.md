---
type: app-integration
source_app: Google Sheets
status: active
tags:
  - obsidian/integration
---

# Apps - Google Sheets

## Capture Path

Spreadsheet range extracts, data logs, and analysis summaries are captured and saved to:
`03-RESOURCES/Sources/` or directly inside the planning and tracking notes of the associated project.

## Metadata

Every captured spreadsheet note must include this frontmatter:

```yaml
---
type: data-log
source_app: Google Sheets
source_url: https://docs.google.com/spreadsheets/d/1tY8Xp98yZ89uN7r8y2b3c4d5e6f/edit#gid=0
source_id: 1tY8Xp98yZ89uN7r8y2b3c4d5e6f
captured_at: 2026-06-17
project: State Not Fate
tags:
  - obsidian/integration
  - sheets/data-extract
---
```

## Linkback

Reopen the Google Sheet in your browser using the spreadsheet ID and specific tab ID (GID):
`https://docs.google.com/spreadsheets/d/<sheet_id>/edit#gid=<gid>`

## Retrieval

* Use during **Weekly Reviews** to inspect financial runways, application statistics, and system habits.
* Re-inject spreadsheet numbers directly into Obsidian status blocks.

---

## Test Capture Sample

**Title**: `Sheets - Job Applications Tracker Extract`
**Path**: `01-PROJECTS/2026-SNF-Substrate-Systems-Project/04-Tracking/Sheets - Job Applications Tracker Extract.md`

```markdown
---
type: data-log
source_app: Google Sheets
source_url: https://docs.google.com/spreadsheets/d/1tY8Xp98yZ89uN7r8y2b3c4d5e6f/edit#gid=0
source_id: 1tY8Xp98yZ89uN7r8y2b3c4d5e6f
captured_at: 2026-06-17
project: Job Hunt 2026
tags:
  - obsidian/integration
  - sheets/data-extract
---

# Sheets - Job Applications Tracker Extract

*   **Spreadsheet**: [Job Application Pipeline](https://docs.google.com/spreadsheets/d/1tY8Xp98yZ89uN7r8y2b3c4d5e6f/edit#gid=0)
*   **Last Updated GID**: `0` (Main Pipeline)

## Extract (2026-06-17)

| Company | Role | Status | Applied Date | Follow Up |
|---|---|---|---|---|
| Clark And Sons | Field Technician | Interview Scheduled | 2026-06-12 | 2026-06-18 |
| Eleeo Inc | PRS Assistant | Application Sent | 2026-06-15 | 2026-06-22 |
| City Logistics | Dispatch Helper | Not Started | 2026-06-17 | N/A |

## Key Insights
*   **Total Applications**: 3 active.
*   **Runway Safe Zone**: Clark And Sons remains the highest probability lead for this week.
```
