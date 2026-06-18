#!/usr/bin/env python3
r"""
sync-all.py

Unified sync script that:
1. Scans Obsidian Library Skills and Protocols (09-PROMPTS/Library/).
2. Validates each note's frontmatter against the Dictionary.md standards.
3. Formats and writes non-project-specific skills for Grok (~/.grok/skills/) and Gemini (~/.gemini/config/plugins/dov-library-plugin/skills/).
4. Re-runs phone favorites export to Library/Mobile-Favorites.md.
5. Builds a consolidated master context and writes it to:
   - Library/Tools/master_context_latest.txt
   - .cursorrules (vault root)

Usage:
  python sync-all.py
"""

import sys
import re
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))
from library_filter import is_project_specific

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

VAULT_PATHS = [
    Path(r"C:\ROOT_OBSIDIAN\master-laptop-vault"),
    Path(r"C:\ROOT_OBSIDIAN\DOV"),
    Path(r"C:\Users\rappd\OneDrive\Desktop\ObsidianVault"),
    Path(r"C:\Users\rappd\My Drive\INBOX\AI Learning\sync-playground-laptop"),
]

GEMINI_SKILLS_DIR = None
GROK_SKILLS_DIR = Path(r"C:\Users\rappd\.grok\skills")

# Playground vault — safe scratchpad that mirrors the core library (read-only zone)
# Personal note folders here are NEVER touched by this script.
PLAYGROUND_VAULT = Path(r"C:\Users\rappd\My Drive\INBOX\AI Learning\sync-playground-laptop")

# Subfolders inside the playground that are CORE (will be overwritten each sync)
# Everything else in the playground is personal / safe to edit freely.
PLAYGROUND_CORE_SUBDIRS = ["09-PROMPTS"]

DAILY_DEFAULT_SKILLS = [
    "thoroughness-protocol",
    "tool-mode-decider",
    "library-gardener",
]

PHONE_FAVORITES = [
    "tool-mode-decider",
    "library-gardener",
]

def find_all_vaults() -> list[Path]:
    vaults = []
    # Prioritize the vault containing this running script dynamically
    try:
        own_vault = Path(__file__).resolve().parents[3]
        if (own_vault / "09-PROMPTS").exists():
            vaults.append(own_vault)
    except Exception:
        pass

    for p in VAULT_PATHS:
        if (p / "09-PROMPTS").exists():
            resolved_p = p.resolve()
            if resolved_p not in [v.resolve() for v in vaults]:
                vaults.append(resolved_p)
                
    if not vaults:
        print("ERROR: No vault paths found. Please edit VAULT_PATHS in the script.")
        sys.exit(1)
    return vaults

def load_note(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].strip()
    return "", text

def parse_frontmatter(fm_text: str) -> dict:
    data = {}
    lines = fm_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
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
                data[key] = " ".join(part for part in block if part).strip()
                continue
            data[key] = val
        i += 1
    return data

def clean_body(body: str) -> str:
    # Remove Obsidian wikilinks but keep labels: [[page|label]] -> label, [[page]] -> page
    body = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', body)
    body = re.sub(r'\[\[([^\]]+)\]\]', r'\1', body)
    # Remove embedded images
    body = re.sub(r'!\[\[[^\]]+\]\]', '', body)
    return body.strip()

def safe_write_text(path: Path, content: str, label: str) -> bool:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return True
    except PermissionError as exc:
        print(f"  [Skip] No permission to write {label}: {path} ({exc})")
        return False

def to_grok_skill(name: str, fm: dict, body: str) -> str:
    desc = fm.get("description", "A useful skill from the Obsidian Prompt Library.")
    desc_one_line = " ".join(desc.split())
    
    out = []
    out.append("---")
    out.append(f"name: {name}")
    out.append("description: >")
    out.append(f"  {desc_one_line}")
    out.append("---")
    out.append("")
    out.append(f"# {name.replace('-', ' ').title()}")
    out.append("")
    out.append("**Source:** Obsidian Library (09-PROMPTS/Library)")
    out.append(f"**Last synced:** {datetime.now().strftime('%Y-%m-%d')}")
    out.append("")
    out.append(body)
    out.append("")
    out.append("---")
    out.append("This skill was generated from the canonical Obsidian note.")
    out.append("Prefer editing the source in the vault and re-syncing.")
    return "\n".join(out)

def load_dictionary(vault: Path) -> dict:
    result = {
        "types": set(),
        "domains": set(),
        "energies": set(),
        "tags": set(),
    }
    dict_path = vault / "09-PROMPTS" / "Library" / "Dictionary.md"
    if not dict_path.exists():
        result["types"] = {"skill", "prompt", "protocol", "context", "guide", "hub", "meta"}
        result["energies"] = {"collapse", "low", "medium", "high", "any", "variable"}
        result["domains"] = {"meta", "library", "job", "execution", "social", "research", "decision-making", "health", "creative", "ai-setup", "philosophy", "finance", "career", "systems"}
        result["tags"] = {"low-energy", "routine", "low-friction", "daily", "weekly", "external-memory", "cognitive-offloading", "systems", "research", "career"}
        return result

    text = dict_path.read_text(encoding="utf-8", errors="ignore")

    for e in ["collapse", "low", "medium", "high", "any", "variable"]:
        if e in text.lower():
            result["energies"].add(e)

    in_domains = False
    for line in text.splitlines():
        if re.match(r"^##\s+Domains\b", line, re.I):
            in_domains = True
            continue
        if in_domains and re.match(r"^##\s+", line):
            break
        if in_domains:
            m = re.match(r"^\|\s*([a-z0-9-]+)\s*\|", line)
            if m:
                domain = m.group(1).lower()
                if domain not in ("domain", "---"):
                    result["domains"].add(domain)

    result["types"].update({"skill", "prompt", "protocol", "context", "guide", "hub", "meta"})
    return result

def validate_skill(path: Path, allowed: dict) -> list[str]:
    issues = []
    fm_text, _ = load_note(path)
    data = parse_frontmatter(fm_text)

    t = data.get("type", "").strip().lower()
    if t and t not in allowed.get("types", set()):
        issues.append(f"type '{t}' not in Dictionary types")

    e = data.get("energy", "").strip().lower()
    if e and e not in allowed.get("energies", set()):
        issues.append(f"energy '{e}' not in Dictionary energies")

    dom_raw = data.get("domain", "") or data.get("domains", "")
    for dpart in re.split(r"[\[\],;\s]+", dom_raw):
        d = dpart.strip("[]'\" ").lower()
        if d and d not in allowed.get("domains", set()):
            issues.append(f"domain '{d}' not in Dictionary domains")

    return issues

def build_master_context(vault: Path, skill_names: list[str]) -> str:
    lib_root = vault / "09-PROMPTS" / "Library"
    parts = []

    parts.append("# MASTER CONTEXT - Source of Truth: Obsidian 09-PROMPTS/Library/")
    parts.append("Use the DOV vault as the source of truth for reusable AI skills, prompts, source-code indexes, and integration notes.")
    parts.append("Do not inject private project or health material unless the user explicitly asks for that exact context.\n")
    parts.append("## Relevant Non-Project Skills From The Library")

    for name in skill_names:
        found = False
        for sub in ["Skills", "Protocols"]:
            p = lib_root / sub / f"{name}.md"
            if p.exists():
                fm, body = load_note(p)
                if is_project_specific(name, fm, body):
                    parts.append(f"### {name} (skipped: project-specific content)")
                else:
                    parts.append(f"### {name}")
                    parts.append(clean_body(body))
                parts.append("")
                found = True
                break
        if not found:
            parts.append(f"### {name} (not found in Library)\n")

    parts.append("## Current Status (UPDATE THIS BEFORE EVERY SESSION)")
    parts.append("```")
    parts.append("Goal:")
    parts.append("Workspace:")
    parts.append("Constraints:")
    parts.append("Files or apps involved:")
    parts.append("Definition of done:")
    parts.append("```")
    parts.append("")
    parts.append("---")
    parts.append("Instructions: Stay scoped, use local source-of-truth files, preserve privacy boundaries, and avoid project-specific assumptions.")
    return "\n".join(parts)

    # 1. Header
    parts.append("# MASTER CONTEXT — Source of Truth: Obsidian 09-PROMPTS/Library/")
    parts.append("You are operating from my personal, canonical skill & prompt library.")
    parts.append("The single source of truth lives in my Obsidian vault (synced via OneDrive/Google Drive).")
    parts.append("All skills below come from there. Use them exactly as written.\n")

    # 2. Master Bio
    master_paths = [
        lib_root / "Contexts" / "master-bio.md",
        lib_root / "Skills" / "master-bio.md"
    ]
    master_content = ""
    for mp in master_paths:
        if mp.exists():
            _, body = load_note(mp)
            master_content = clean_body(body)
            break
    
    if master_content:
        parts.append("## Core Identity & Constraints (master-bio)")
        parts.append(master_content)
        parts.append("")

    # 3. Protocols
    parts.append("## Core Protocols (always apply these patterns)")
    for proto in ["thoroughness-protocol", "council-strategy"]:
        p_path = lib_root / "Protocols" / f"{proto}.md"
        if not p_path.exists():
            p_path = lib_root / "Skills" / f"{proto}.md"
        if p_path.exists():
            _, body = load_note(p_path)
            parts.append(f"### {proto}")
            parts.append(clean_body(body))
            parts.append("")

    # 4. Daily Skills
    parts.append("## Relevant Skills from the Library")
    for name in skill_names:
        found = False
        for sub in ["Skills", "Protocols"]:
            p = lib_root / sub / f"{name}.md"
            if p.exists():
                _, body = load_note(p)
                parts.append(f"### {name}")
                parts.append(clean_body(body))
                parts.append("")
                found = True
                break
        if not found:
            parts.append(f"### {name} (not found in Library)\n")

    # 5. Status block template
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

def export_mobile_favorites(vault: Path):
    lib = vault / "09-PROMPTS" / "Library"
    output_lines = []
    output_lines.append("# Mobile Favorites – Obsidian Skill & Prompt Library")
    output_lines.append("# Generated for quick copy-paste on phone")
    output_lines.append("# Source: 09-PROMPTS/Library (syncs via OneDrive)")
    output_lines.append("# Tip: Prefix with /tp or /council when needed.")
    output_lines.append("")

    for name in PHONE_FAVORITES:
        found = False
        for sub in ["Skills", "Protocols", "Contexts"]:
            p = lib / sub / f"{name}.md"
            if p.exists():
                fm, body = load_note(p)
                if is_project_specific(name, fm, body):
                    continue
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
    out_path = lib / "Mobile-Favorites.md"
    out_path.write_text(output, encoding="utf-8")
    print(f"  [Mobile] Wrote Mobile-Favorites.md to {vault.name}/{out_path.name}")

def main():
    print("=== SYNCHRONIZING PROMPT LIBRARY SYSTEM ===")
    existing_vaults = find_all_vaults()
    source_vault = existing_vaults[0]
    lib = source_vault / "09-PROMPTS" / "Library"
    print(f"Source Vault (for notes): {source_vault.resolve()}")
    print("All detected vaults: " + ", ".join([v.name for v in existing_vaults]))

    allowed = load_dictionary(source_vault)

    # 1. Collect all skills and protocols
    notes_to_sync = []
    for subdir in ["Skills", "Protocols"]:
        folder = lib / subdir
        if folder.exists():
            for f in folder.glob("*.md"):
                # Skip Obsidian auto-duplicate files like "skill 1.md", "skill 2.md"
                if re.search(r' \d+\.md$', f.name) or f.stem.endswith(" copy"):
                    continue
                notes_to_sync.append(f)

    # Ensure no duplicates
    notes_to_sync = list(set(notes_to_sync))

    gemini_count = 0
    grok_count = 0
    validation_issues = {}

    for path in notes_to_sync:
        name = path.stem
        # Load content
        fm, body = load_note(path)
        fm_parsed = parse_frontmatter(fm)

        # Skip contexts/hubs that aren't intended to be active skills
        if fm_parsed.get("type") in ("hub", "meta") or name in ("master-bio", "README", "Dictionary", "SCHEMA", "Mobile-Favorites"):
            continue
        if is_project_specific(name, fm, body):
            continue

        # Validate only notes eligible for export.
        issues = validate_skill(path, allowed)
        if issues:
            validation_issues[name] = issues

        body_cleaned = clean_body(body)

        content = to_grok_skill(name, fm_parsed, body_cleaned)

        # Write to Gemini plugins
        if GEMINI_SKILLS_DIR and GEMINI_SKILLS_DIR.exists():
            target_gemini = GEMINI_SKILLS_DIR / name / "SKILL.md"
            if safe_write_text(target_gemini, content, "Gemini skill"):
                gemini_count += 1

        # Write to Grok skills
        if GROK_SKILLS_DIR.exists():
            target_grok = GROK_SKILLS_DIR / name / "SKILL.md"
            if safe_write_text(target_grok, content, "Grok skill"):
                grok_count += 1

    print(f"  [Sync] Synced {gemini_count} skills to Gemini plugins directory")
    print(f"  [Sync] Synced {grok_count} skills to Grok skills directory ({GROK_SKILLS_DIR})")

    # 2. Build and export files for each detected vault
    for vault in existing_vaults:
        # A. Build Mobile Favorites
        try:
            export_mobile_favorites(vault)
        except PermissionError as exc:
            print(f"  [Skip] No permission to export Mobile-Favorites.md for {vault}: {exc}")

        # B. Build master context
        master_context_str = build_master_context(vault, DAILY_DEFAULT_SKILLS)
        
        # Save context snapshot
        context_file = vault / "09-PROMPTS" / "Library" / "Tools" / "master_context_latest.txt"
        if safe_write_text(context_file, master_context_str, "master context"):
            print(f"  [Context] Wrote master_context_latest.txt to {vault.name}/Tools/")

        # Write .cursorrules to the vault root
        cursor_rules_file = vault / ".cursorrules"
        if safe_write_text(cursor_rules_file, master_context_str, ".cursorrules"):
            print(f"  [Cursor] Wrote .cursorrules to vault root: {vault.name}/.cursorrules")

    # Display validation report
    if validation_issues:
        print("\n=== Validation Warnings (non-blocking) ===")
        for name, issues in validation_issues.items():
            print(f"  {name}:")
            for issue in issues:
                print(f"    - {issue}")
    else:
        print("\nAll skills compliant with Dictionary standards!")

    # 3. Mirror core library files into the playground vault
    try:
        mirror_library_to_playground(source_vault)
    except PermissionError as exc:
        print(f"  [Playground] Skipped - no permission to mirror playground vault: {exc}")

    print("\nIntegration Complete! The Obsidian vaults are now the active source of truth.")

def mirror_library_to_playground(source_vault: Path):
    """
    One-way mirror: DOV/09-PROMPTS/Library → playground/09-PROMPTS/Library

    SAFE ZONES (never touched by this function):
      - 00-INBOX, 01-PLAYGROUND, 02-AREAS, 02-DRAFTS, 03-RESOURCES
      - 04-ARCHIVES, 05-WRITING, 06-DAILY-NOTES, 07-HUMAN-HEALTH
      - 08-TECH-AND-AI (your personal notes there)
      - Any file you create outside of 09-PROMPTS/Library/

    CORE ZONE (overwritten each sync — do NOT edit in playground):
      - 09-PROMPTS/Library/Skills/
      - 09-PROMPTS/Library/Protocols/
      - 09-PROMPTS/Library/Contexts/
      - 09-PROMPTS/Library/Tools/  (scripts only)
    """
    if not PLAYGROUND_VAULT.exists():
        print(f"  [Playground] Skipped — playground vault not found at {PLAYGROUND_VAULT}")
        return

    READONLY_BANNER = (
        "<!-- ⚠️  CORE LIBRARY FILE — DO NOT EDIT HERE.\n"
        "     Edit the master in: c:\\ROOT_OBSIDIAN\\DOV\\09-PROMPTS\\Library\\\n"
        "     then run sync-all.py to push changes everywhere.\n"
        "     Changes you make here WILL BE OVERWRITTEN on next sync. -->\n\n"
    )

    src_lib = source_vault / "09-PROMPTS" / "Library"
    dst_lib = PLAYGROUND_VAULT / "09-PROMPTS" / "Library"

    # Subdirs to mirror (core library content only)
    mirror_subdirs = ["Skills", "Protocols", "Contexts"]

    total_copied = 0
    for subdir in mirror_subdirs:
        src_dir = src_lib / subdir
        dst_dir = dst_lib / subdir
        if not src_dir.exists():
            continue
        dst_dir.mkdir(parents=True, exist_ok=True)

        for src_file in src_dir.glob("*.md"):
            # Skip known duplicates
            if "1" in src_file.stem and src_file.stem != "1":
                continue
            raw = src_file.read_text(encoding="utf-8", errors="ignore")
            dst_file = dst_dir / src_file.name

            # Inject read-only banner after frontmatter (or at top if no frontmatter)
            if raw.startswith("---"):
                parts = raw.split("---", 2)
                if len(parts) >= 3:
                    new_content = "---" + parts[1] + "---\n\n" + READONLY_BANNER + parts[2].lstrip()
                else:
                    new_content = READONLY_BANNER + raw
            else:
                new_content = READONLY_BANNER + raw

            dst_file.write_text(new_content, encoding="utf-8")
            total_copied += 1

    # Also copy Tools scripts (without banner — they're code)
    src_tools = src_lib / "Tools"
    dst_tools = dst_lib / "Tools"
    if src_tools.exists():
        dst_tools.mkdir(parents=True, exist_ok=True)
        for src_file in src_tools.glob("*.py"):
            import shutil as _shutil
            _shutil.copy2(src_file, dst_tools / src_file.name)
            total_copied += 1
        # Copy key reference .md files
        for ref_file in ["README.md", "Dictionary.md", "SCHEMA.md"]:
            src_ref = src_lib / ref_file
            if src_ref.exists():
                dst_ref = dst_lib / ref_file
                dst_ref.write_text(
                    READONLY_BANNER + src_ref.read_text(encoding="utf-8", errors="ignore"),
                    encoding="utf-8"
                )
                total_copied += 1

    print(f"  [Playground] Mirrored {total_copied} core files → {PLAYGROUND_VAULT.name}/09-PROMPTS/Library/")
    print(f"  [Playground] Your personal notes (inbox, daily notes, drafts, etc.) were NOT touched.")


if __name__ == "__main__":
    main()
