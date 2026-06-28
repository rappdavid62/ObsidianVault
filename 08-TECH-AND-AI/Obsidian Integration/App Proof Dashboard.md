---
type: dashboard
status: active
tags:
  - obsidian/integration
last_reviewed: 2026-06-28
---

# App Proof Dashboard

## Bottom Line

The detailed machine-readable truth lives in `app-proof-tracker.json`. This dashboard is the human scan view.

As of the current tracker: 11 apps are complete, 8 are deferred on demand, and 7 are deferred low priority.

## Definition Of Done

An app is complete only when all four checks are backed by evidence:

- Capture: a real app item lands in Obsidian.
- Metadata: the note includes source metadata such as `source_app`, `source_url` or `source_id`, and `captured_at`.
- Linkback: the note can reopen the original app item or source.
- Retrieval: the app workflow can use the Obsidian note later.

## Complete

| App | Evidence note |
|---|---|
| Browser | `00-CAPTURE\App Captures\Clippings\TMWLBB.md` |
| Chrome | `00-CAPTURE\App Captures\Clippings\TMWLBB.md` |
| Codex | `00-CAPTURE\App Captures\Codex Integration Proof.md` |
| GitHub | `08-TECH-AND-AI/Obsidian Integration/Apps - GitHub.md` |
| Gmail | `08-TECH-AND-AI/Obsidian Integration/Apps - Gmail.md` |
| Google Calendar | `08-TECH-AND-AI/Obsidian Integration/Apps - Google Calendar.md` |
| Google Drive | `00-CAPTURE\App Captures\Google Drive - SNF Locked Proof.md` |
| Google Sheets | `08-TECH-AND-AI/Obsidian Integration/Apps - Google Sheets.md` |
| Netlify | `00-CAPTURE\App Captures\Netlify - State Not Fate Proof.md` |
| Obsidian Web Clipper | `00-CAPTURE\App Captures\Clippings\TMWLBB.md` |
| Slack | `08-TECH-AND-AI/Obsidian Integration/Apps - Slack.md` |

## Deferred On Demand

Complete these only when the app becomes actively useful:

- Airtable
- Box
- Figma
- Google Docs
- Google Slides
- OpenAI Developers
- Product Design
- Scite

## Deferred Low Priority

Keep these out of the daily loop unless a specific project needs them:

- CircleCI
- Computer Use
- Build Web Apps
- Build Web Data Visualization
- HyperFrames
- Life Science Research
- Life Sciences NGS Analysis

## Operating Rule

Do not chase proof for every connector as busywork. Promote an app to active proof only when it supports job search, State Not Fate, vault maintenance, writing, or a current project.
