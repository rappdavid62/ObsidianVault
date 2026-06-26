#!/usr/bin/env python3
"""
export-for-phone.py

Generates a phone-friendly "Favorites" file with the most commonly used skills
in a clean, minimal format that's easy to open on mobile and copy-paste into any chat.

This is the "ubiquitous on the go" piece.

Usage:
  python export-for-phone.py
  python export-for-phone.py --output "Mobile-Favorites.md"

It creates a single compact file with the highest-utility skills (low-energy, job, social, protocols).
You can sync this file to your phone via OneDrive and have instant access.
"""

import sys
from pathlib import Path

VAULT_PATHS = [
    Path(__file__).resolve().parents[3],
    Path(r"C:\ROOT_OBSIDIAN\DOV"),
    Path(r"C:\Users\rappd\OneDrive\Desktop\ObsidianVault"),
]
LIBRARY_ROOT = "09-PROMPTS/Library"

# Skills that are most useful on a phone (quick copy when you're out and about)
PHONE_FAVORITES = [
    "thoroughness-protocol",
    "low-energy-execution",
    "daily-job-search",
    "social-calibration",
    "apply-today",
    "council-strategy",
    "tech-council",
]

def find_vault():
    for p in VAULT_PATHS:
        if (p / "09-PROMPTS").exists():
            return p
    print("Vault not found.")
    sys.exit(1)

def load_note(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].strip()
    return "", text

def clean_body(body: str) -> str:
    import re
    body = re.sub(r'\[\[([^\]|]+)(\|[^\]]+)?\]\]', r'\1', body)
    return body.strip()

def main():
    vault = find_vault()
    lib = vault / LIBRARY_ROOT

    output_lines = []
    output_lines.append("# Mobile Favorites – Obsidian Skill & Prompt Library")
    output_lines.append("# Generated for quick copy-paste on phone")
    output_lines.append("# Source: 09-PROMPTS/Library (syncs via OneDrive)")
    output_lines.append("# Tip: Prefix with /tp or /council when needed.")
    output_lines.append("")

    for name in PHONE_FAVORITES:
        found = False
        for sub in ["Skills", "Prompts", "Protocols"]:
            p = lib / sub / f"{name}.md"
            if p.exists():
                fm, body = load_note(p)
                output_lines.append(f"\n## {name}")
                if fm:
                    output_lines.append("```")
                    output_lines.append("---")
                    output_lines.append(fm)
                    output_lines.append("---")
                    output_lines.append("```")
                output_lines.append("")
                output_lines.append(clean_body(body))
                output_lines.append("")
                found = True
                break
        if not found:
            output_lines.append(f"\n## {name} (not found)")

    output = "\n".join(output_lines)

    out_path = vault / "09-PROMPTS" / "Library" / "Mobile-Favorites.md"
    if len(sys.argv) > 1 and sys.argv[1] == "--output":
        out_path = Path(sys.argv[2])

    out_path.write_text(output, encoding="utf-8")
    print(f"Phone-friendly favorites exported to:\n{out_path}")
    print("\nSync this file to your phone via OneDrive for always-available skills.")

if __name__ == "__main__":
    main()
