---
type: app-integration
source_app: Slack
status: active
tags:
  - obsidian/integration
---

# Apps - Slack

## Capture Path

Key decisions, project briefs, and task details shared in Slack channels are captured and saved to:
`00-INBOX/App Captures/` or mapped directly into project logs.

## Metadata

Every captured Slack note must include this frontmatter:

```yaml
---
type: chat-decision
source_app: Slack
source_url: https://myworkspace.slack.com/archives/C01234567/p1623891823000200
source_id: C01234567/p1623891823000200
captured_at: 2026-06-17
project: State Not Fate
people:
  - "Team Member"
tags:
  - obsidian/integration
  - slack/decision-log
---
```

## Linkback

Reopen the original Slack message thread using the Slack web/client permalink structure:
`https://<workspace_name>.slack.com/archives/<channel_id>/p<timestamp_digits>`

*Note: For the desktop client to open directly, use `slack://channel?id=<channel_id>&message=<message_timestamp>`.*

## Retrieval

* Extract action items from Slack threads during **Daily Reviews**.
* Reference decision notes in project logs to verify design consensus.

---

## Test Capture Sample

**Title**: `Slack - PWA Database Choice Consensus`
**Path**: `00-INBOX/App Captures/Slack - PWA Database Choice Consensus.md`

```markdown
---
type: chat-decision
source_app: Slack
source_url: https://statenotfate.slack.com/archives/C09876543/p1623891823000200
source_id: C09876543/p1623891823000200
captured_at: 2026-06-17
project: State Not Fate
people:
  - "John Database Guy"
tags:
  - obsidian/integration
  - slack/decision-log
---

# Slack - PWA Database Choice Consensus

*   **Channel**: `#dev-backend`
*   **Workspace**: `statenotfate.slack.com`
*   **Permalink**: [Slack Message Thread](https://statenotfate.slack.com/archives/C09876543/p1623891823000200)

## Conversation Context

Discussion regarding database tooling for local offline storage in the PWA. John suggested using IndexedDB via Dexie.js for simple key-value lookups instead of full SQLite WASM to keep the bundle size small.

## Decision
We will use **Dexie.js (IndexedDB wrapper)** to manage offline user data, status logs, and task structures.

## Next Action
- [ ] Install dexie package in client app source.
- [ ] Initialize local schema.
```
