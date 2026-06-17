---
type: reference
source_app: browser
status: active
tags:
  - obsidian/integration
  - web
---

# Web Clipper Templates

## Source - Article

Destination:

```text
03-RESOURCES/Sources/{{title}}
```

```markdown
---
type: source
source_app: browser
source_url: {{url}}
captured_at: {{date}}
author: {{author}}
status: inbox
project:
tags:
  - source
  - web
---

# {{title}}

## Summary

{{description}}

## Highlights

{{highlights}}

## Selection

{{selection}}

## Notes

{{notes}}

## Source

- URL: {{url}}
```

## Source - App Page

Destination:

```text
00-INBOX/App Captures/{{title}}
```

```markdown
---
type: capture
source_app: browser
source_url: {{url}}
captured_at: {{date}}
status: inbox
project:
people:
tags:
  - obsidian/integration
  - web
---

# {{title}}

## Captured Context

{{selection}}

## Page Notes

{{notes}}

## Action

- [ ] Triage this capture

## Source

- URL: {{url}}
```
