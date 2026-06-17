---
type: reference
status: active
tags:
  - obsidian/integration
---

# URI Bridge Recipes

Use Obsidian URI links when an app can open links but cannot write to the vault.

## Create Capture

```text
obsidian://new?vault=DOV&file=00-INBOX%2FApp%20Captures%2FNew%20Capture&content=%23%20New%20Capture
```

## Append To Daily

```text
obsidian://daily?vault=DOV&append=true&content=%0A- Captured item
```

## Search Vault

```text
obsidian://search?vault=DOV&query=project%20name
```

## Protocol Test

```text
obsidian://choose-vault
```

An app integration can use URI bridging as capture proof only when the created note includes metadata and source linkback.
