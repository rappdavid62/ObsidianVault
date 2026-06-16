# ChatGPT -> Grok Bridge Options

## Bottom line
There is no clean native one-click sync between ChatGPT and Grok chat workspaces.
The practical bridge is a neutral handoff layer.

## Best bridge options

### Option 1 - Manual bundle handoff (best right now)
Use this folder or zip.
Upload the bundle into Grok chat or to Grok Collections.
Use 00_START_HERE.md and the prompts first so Grok understands the project before reading every file.

### Option 2 - Shared Google Drive folder (best recurring bridge)
Put this bundle in a dedicated Google Drive folder.
If your Grok plan includes Google Drive integration, connect that folder to Grok.
If your ChatGPT account has Google Drive app/sync enabled, keep the same folder as the shared source of truth.
This makes Drive the neutral bridge instead of trying to sync model memory directly.

### Option 3 - API / Collections bridge
Upload these files to xAI Collections.
Then use Grok with collection search enabled for persistent retrieval.
This is cleaner than repeatedly attaching files to new chats.

### Option 4 - MCP bridge for advanced use
If you run Grok through API workflows, you can expose a project source through an MCP server.
That is the only real path to a live programmable bridge.
It is more technical but better for durable research infrastructure.

## What not to assume
- ChatGPT project memory does not automatically appear inside Grok.
- Grok chat memory does not automatically ingest ChatGPT chats.
- Shared links are not a true cross-platform knowledge base.

## Recommended practical setup
1. Keep the source-of-truth folder in Drive.
2. Keep a zipped snapshot for backup.
3. Keep a plain-text export layer for easier AI ingestion.
4. Keep one master brief and one master prompt.
5. Rebuild the bundle whenever core documents materially change.
