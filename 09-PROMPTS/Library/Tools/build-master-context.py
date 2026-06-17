#!/usr/bin/env python3
"""
build-master-context.py

Builds a complete, ready-to-paste "Master Context" block for any AI.
This is the highest-leverage ubiquity tool: it combines your canonical master-bio,
core protocols, selected skills, and a status block template into one coherent injection.

Usage:
  python build-master-context.py
  python build-master-context.py --skills mvd-anchors,floor-wins,prs-safety-check
  python build-master-context.py --daily          # uses a sensible low-energy daily set
  python build-master-context.py --clip           # copy to clipboard (Windows)

This makes Obsidian the true source of truth while giving you a single block you can paste
into Claude, ChatGPT, Cursor, local models, or even start a new Grok conversation with.
"""

import sys
import subprocess
from pathlib import Path

# Adjust if your vault location is different
VAULT_PATH = Path(r"C:\ROOT_OBSIDIAN\master-laptop-vault")
if not VAULT_PATH.exists():
    VAULT_PATH = Path(r"C:\ROOT_OBSIDIAN\DOV")
if not VAULT_PATH.exists():
    VAULT_PATH = Path(r"C:\Users\rappd\OneDrive\Desktop\ObsidianVault")
LIBRARY_ROOT = VAULT_PATH / "09-PROMPTS" / "Library"

# Default "daily" skills when --daily is used (low-energy first, then practical)
DEFAULT_DAILY_SKILLS = [
    "thoroughness-protocol",
    "low-energy-execution",
    "mvd-anchors",
    "floor-wins",
    "social-calibration",
    "daily-job-search",
]

def load_note(path: Path) -> str:
    if not path.exists():
        return f"[MISSING: {path.name}]"
    text = path.read_text(encoding="utf-8", errors="ignore")
    # Strip frontmatter for cleaner injection (optional — you can keep it if you want the AI to see the metadata)
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return text.strip()

def build_context(skill_names: list[str], include_status_placeholder: bool = True) -> str:
    parts = []

    # 1. Master Bio (always first — core identity + constraints)
    master = load_note(LIBRARY_ROOT / "Contexts" / "master-bio.md")
    parts.append("# MASTER CONTEXT — Source of Truth: Obsidian 09-PROMPTS/Library/")
    parts.append("You are operating from my personal, canonical skill & prompt library.")
    parts.append("The single source of truth lives in my Obsidian vault (synced via OneDrive).")
    parts.append("All skills below come from there. Use them exactly as written.\n")
    parts.append("## Core Identity & Constraints (master-bio)")
    parts.append(master)
    parts.append("")

    # 2. Core Protocols (always useful meta-layer)
    parts.append("## Core Protocols (always apply these patterns)")
    for proto in ["thoroughness-protocol", "council-strategy"]:
        content = load_note(LIBRARY_ROOT / "Protocols" / f"{proto}.md")
        parts.append(f"### {proto}")
        parts.append(content)
        parts.append("")

    # 3. Selected Skills
    parts.append("## Relevant Skills from the Library")
    for name in skill_names:
        # Try Skills, then Protocols, then Prompts
        for sub in ["Skills", "Protocols", "Prompts"]:
            p = LIBRARY_ROOT / sub / f"{name}.md"
            if p.exists():
                content = load_note(p)
                parts.append(f"### {name}")
                parts.append(content)
                parts.append("")
                break
        else:
            parts.append(f"### {name} (not found in Library)")
            parts.append("")

    # 4. Current Status (user must fill or replace with their actual block)
    if include_status_placeholder:
        parts.append("## Current Status (UPDATE THIS BEFORE EVERY SESSION)")
        parts.append("```")
        parts.append("Energy: [low / medium / high / collapse]")
        parts.append("Runway (weeks): [number]")
        parts.append("One non-negotiable today: [whatever must happen]")
        parts.append("Job search / main focus: [current targets or blockers]")
        parts.append("Other relevant context: [recent events, mood, constraints]")
        parts.append("```")
        parts.append("")

    parts.append("---")
    parts.append("Instructions: Follow the skill instructions precisely. Bottom line first. Be realistic about my current energy and constraints. Use the language and scaling from the skills above. Treat the Master Bio as always-true background.")

    return "\n".join(parts)

def copy_to_clipboard(text: str) -> bool:
    try:
        subprocess.run("clip", input=text.encode("utf-8"), check=True, shell=True)
        return True
    except Exception:
        return False

def main():
    args = sys.argv[1:]
    use_clip = "--clip" in args
    use_daily = "--daily" in args

    skill_names = []
    for arg in args:
        if arg.startswith("--"):
            continue
        if "," in arg:
            skill_names.extend([s.strip() for s in arg.split(",")])
        else:
            skill_names.append(arg)

    if use_daily or (not skill_names and not use_daily):
        skill_names = DEFAULT_DAILY_SKILLS
        print("# Using default daily pack (low-energy first)\n")

    context = build_context(skill_names)

    print(context)

    if use_clip and copy_to_clipboard(context):
        print("\n[Copied to clipboard — ready to paste into any AI]")

if __name__ == "__main__":
    main()
