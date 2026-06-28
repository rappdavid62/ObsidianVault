---
type: reference
status: active
tags:
  - obsidian/integration
---

# App Integration Playbooks

An app is integrated only when all four checks are proven with a real sample:

- Capture: a real item lands in Obsidian.
- Metadata: the note includes `source_app`, `source_url` or `source_id`, and `captured_at`.
- Linkback: the source can be reopened from the note.
- Retrieval: the source app workflow can use the Obsidian note later.

## Browser / Web Clipper

- Capture web pages into `03-RESOURCES/Sources`.
- Capture unprocessed app pages into `00-CAPTURE/App Captures`.
- Verify title, URL, selected text, and notes are preserved.

## Codex

- Capture goal summaries, implementation decisions, blockers, and output links.
- Use `source_app: Codex` and the goal or thread id as `source_id`.

## Gmail

- Capture important threads as task, person, project, or decision notes.
- Preserve sender, subject, thread URL, and next action.

## Google Calendar

- Create meeting notes with attendees, agenda, decisions, and tasks.
- Link each meeting note from the relevant daily note.

## Google Drive

- Capture Docs, Sheets, and Slides as source or project notes.
- Preserve the Drive URL and relevant file context.

## Slack

- Capture important threads with channel, participants, permalink, and action.

## GitHub

- Capture issues, PRs, CI failures, and releases.
- Preserve repo, issue or PR number, URL, status, and next action.

## Figma

- Capture design reviews, frame decisions, and component notes.
- Preserve file or frame URL.

## Airtable

- Capture base, table, view, schema, and operational-decision summaries.

## Netlify

- Capture deploys, incidents, environment changes, and site decisions.
