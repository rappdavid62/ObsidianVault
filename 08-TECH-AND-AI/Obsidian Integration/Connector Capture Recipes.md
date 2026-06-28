---
type: reference
status: active
tags:
  - obsidian/integration
---

# Connector Capture Recipes

Use this note to turn connector output into durable Obsidian notes.

## Required Capture Shape

```yaml
---
type:
source_app:
source_url:
source_id:
captured_at:
status: inbox
project:
people:
tags:
  - obsidian/integration
---
```

## Connector Families

| App | Capture | Proof |
|---|---|---|
| Airtable | Base/table/view summary | Link back to Airtable and answer a future ops question |
| Box | File/folder summary | Link back to Box and preserve document summary |
| Gmail | Actionable thread | Sender, subject, date, action, thread link |
| Google Calendar | Meeting note | Event link, daily-note link, decisions/tasks |
| Google Drive | File/folder summary | Drive URL, summary, next action |
| Google Docs | Document summary/review | Doc URL, owner, status, requested action |
| Google Sheets | Analysis/range note | Sheet URL and range/table |
| Google Slides | Deck review | Deck URL, audience, purpose, next revision |
| GitHub | Issue/PR/CI/release | Repo, URL, status, next action |
| Slack | Thread/decision/task | Channel, participants, permalink, owner |
| Figma | Frame/file/component decision | Figma URL, what changed, why |
| Netlify | Deploy/incident/env change | Deploy/admin URL, status, follow-up |
| OpenAI Developers | API/key/agent decision | Docs URL or project path, model/tool choice |
| Product Design | Brief/direction/critique | Artifact URL/path and design decision |
| Scite | Citation/evidence check | Source URL, claim, support/contrast status |
| CircleCI | Build/config/deploy note | Build/job/config URL and evidence |
| HyperFrames | Composition/render decision | Composition path or render URL |
| Life Science Research | Paper/dataset evidence | Source URL, key claim, evidence strength |
| Life Sciences NGS Analysis | Intake/run/QC/report | Dataset id/path, workflow, QC, report path |
| Computer Use | Desktop workflow | App/window, steps, result, screenshot path if any |
| Browser / Chrome / Web Clipper | Page/tab/source | Title, URL, selection/summary, timestamp |
```
