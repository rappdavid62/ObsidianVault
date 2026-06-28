#!/usr/bin/env python3
r"""
sync-to-grok.py (prototype)

Takes an Obsidian Library skill and emits a .grok/skills compatible SKILL.md.

This is the start of making the Obsidian Library the source of truth
while still having live, auto-triggerable skills in this Grok environment.

NOTE: For syncing the entire prompt library to both Gemini plugins and Grok,
use the new unified synchronization script `sync-all.py` instead.

Usage:
  python sync-to-grok.py daily-job-search
  python sync-to-grok.py daily-job-search --output-dir "C:/Users/rappd/.grok/skills"

It will print (or write) a SKILL.md that follows the expected .grok format,
using the `description` from frontmatter as the trigger description.
"""

import sys
import re
from pathlib import Path
from datetime import datetime

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

VAULT_PATHS = [
    Path(r"C:\ROOT_OBSIDIAN\DOV"),
    Path(r"C:\ROOT_OBSIDIAN\master-laptop-vault"),
    Path(r"C:\Users\rappd\OneDrive\Desktop\ObsidianVault"),
]

def find_vault():
    for p in VAULT_PATHS:
        if (p / "09-PROMPTS").exists():
            return p
    print("Vault not found. Edit VAULT_PATHS.")
    sys.exit(1)

def load_skill(name: str, vault: Path):
    lib = vault / "09-PROMPTS" / "Library"
    for sub in ["Skills", "Prompts", "Protocols"]:
        p = lib / sub / f"{name}.md"
        if p.exists():
            return p
    print(f"Could not find {name}")
    sys.exit(1)

def parse_frontmatter(text: str):
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm = {}
    lines = parts[1].strip().splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            key = k.strip()
            val = v.strip().strip('"').strip("'")
            if val in {">", "|"}:
                block = []
                i += 1
                while i < len(lines):
                    next_line = lines[i]
                    if next_line.startswith((" ", "\t")) or not next_line.strip():
                        block.append(next_line.strip())
                        i += 1
                        continue
                    break
                fm[key] = " ".join(part for part in block if part).strip()
                continue
            fm[key] = val
        i += 1
    return fm, parts[2].strip()

def to_grok_skill(name: str, fm: dict, body: str) -> str:
    desc = fm.get("description", "A useful skill from the Obsidian Library.")
    # Clean the description for the description: field (single line preferred)
    desc_one_line = " ".join(desc.split())

    out = []
    out.append("---")
    out.append(f"name: {name}")
    out.append(f"description: >")
    out.append(f"  {desc_one_line}")
    out.append("---")
    out.append("")
    out.append(f"# {name.replace('-', ' ').title()}")
    out.append("")
    out.append("**Source:** DOV Obsidian Library (C:\\ROOT_OBSIDIAN\\DOV\\09-PROMPTS\\Library)")
    out.append(f"**Last synced:** {datetime.now().strftime('%Y-%m-%d')}")
    out.append("")
    out.append(body)
    out.append("")
    out.append("---")
    out.append("This skill was generated from the canonical Obsidian note.")
    out.append("Prefer editing the source in the vault and re-syncing.")
    return "\n".join(out)

def main():
    if len(sys.argv) < 2:
        print("Usage: python sync-to-grok.py <skill-name> [--output-dir PATH]")
        sys.exit(1)

    name = sys.argv[1]
    output_dir = None
    if "--output-dir" in sys.argv:
        idx = sys.argv.index("--output-dir")
        if idx + 1 < len(sys.argv):
            output_dir = Path(sys.argv[idx + 1])

    vault = find_vault()
    note_path = load_skill(name, vault)
    text = note_path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    grok_content = to_grok_skill(name, fm, body)

    if output_dir:
        target = output_dir / name / "SKILL.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(grok_content, encoding="utf-8")
        print(f"Wrote {target}")
    else:
        print(grok_content)
        print("\n---")
        print("To write it directly, use --output-dir \"C:\\Users\\rappd\\.grok\\skills\"")

if __name__ == "__main__":
    main()
