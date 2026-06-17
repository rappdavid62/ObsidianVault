---
type: reference
status: active
tags:
  - obsidian/integration
---

# URI Cookbook

Replace `DOV` with the vault name or vault ID if needed.

## Open Vault

```text
obsidian://open?vault=DOV
```

## Open Daily Note

```text
obsidian://daily?vault=DOV
```

## Search

```text
obsidian://search?vault=DOV&query=project%20alpha
```

## Create Inbox Capture

```text
obsidian://new?vault=DOV&file=00-INBOX%2FApp%20Captures%2FNew%20Capture&content=%23%20New%20Capture%0A%0A
```

## Append To Daily Note

```text
obsidian://daily?vault=DOV&append=true&content=%0A%0A- Captured item goes here
```

## Protocol Test

```text
obsidian://choose-vault
```
