#!/usr/bin/env python3
r"""
emit-skill.py - Ubiquitous Skill & Prompt Emitter

Makes your Obsidian Library usable from ANY chat, device, or terminal.

Core philosophy: The vault is source of truth. These tools make it ubiquitous.

Usage examples:
  python emit-skill.py daily-job-search
  python emit-skill.py daily-job-search low-energy-execution --with-master
  python emit-skill.py --daily                    # full daily execution pack
  python emit-skill.py --list
  python emit-skill.py --search "job low-energy"
  python emit-skill.py --daily --clip             # Windows: copy straight to clipboard
  python emit-skill.py --validate mvd-anchors

New in this version (focus on ubiquity):
- Multi-skill emission
- --daily : ready-to-paste daily context pack (master + key protocols + core skills)
- --with-master : automatically includes your master-bio context
- --favorites : broader quick-access pack
- Better frontmatter parsing (shows energy, domain, description)
- --clip : copies output to Windows clipboard (clip.exe)
- Improved --list and new --search
- --validate <name> : check a note against the Dictionary for compliance
- Automatic validation note during normal emit if issues found
- Cleaner pasteable output (easy to drop into Grok, Claude, ChatGPT, local models, phone notes)

Requirements: Python 3. Python is usually available or easy to install on Windows.

Tip: Add an alias in your PowerShell profile:
  function skill { & "C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library\Tools\emit-skill.ps1" @args }
Then just type: skill --daily
"""

import sys
import re
import subprocess
from pathlib import Path
from typing import Optional, List, Dict

# Ensure UTF-8 output on Windows terminals and redirected output.
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))
from library_filter import is_project_specific

# === CONFIGURATION - tweak for your machine ===
VAULT_PATHS = [
    Path(r"C:\ROOT_OBSIDIAN\DOV"),
    Path(r"C:\Users\rappd\OneDrive\Desktop\ObsidianVault"),
    Path.home() / "OneDrive" / "Desktop" / "ObsidianVault",
]

LIBRARY_ROOT = "09-PROMPTS/Library"

# Skills that are almost always useful in a daily pack (low energy / high frequency)
DAILY_DEFAULT_SKILLS = [
    "bootstrap-session",
    "daily-execution",
    "thoroughness-protocol",
    "low-energy-execution",
    "tool-mode-decider",
    "daily-job-search",
    "social-calibration",
]

# Favorites for quick access (used by --favorites). Energy-balanced collection.
FAVORITES = DAILY_DEFAULT_SKILLS + [
    "second-brain-control-loop",
    "vault-cleaner",
    "priority-audit",
    "council-decision",
    "apply-today",
    "resume-tailoring",
    "deep-research",
    "weekly-review",
    "library-gardener",
]

# Simple energy-based packs (can be extended)
LOW_ENERGY_PACK = ["bootstrap-session", "daily-execution", "low-energy-execution", "social-calibration"]
MEDIUM_ENERGY_PACK = DAILY_DEFAULT_SKILLS + ["apply-today", "resume-tailoring", "priority-audit"]
HIGH_ENERGY_PACK = ["second-brain-control-loop", "vault-cleaner", "daily-job-search", "deep-research", "tool-mode-decider", "weekly-review", "library-gardener", "council-decision"]

# === END CONFIG ===


def find_vault() -> Path:
    for p in VAULT_PATHS:
        if (p / "09-PROMPTS").exists():
            return p
    print("ERROR: Could not find your ObsidianVault.")
    print("Edit VAULT_PATHS at the top of this script.")
    sys.exit(1)


def load_note(path: Path) -> tuple[str, str]:
    """Return (frontmatter_str, body)"""
    text = path.read_text(encoding="utf-8", errors="ignore")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].strip()
    return "", text


def parse_frontmatter(fm_text: str) -> Dict[str, str]:
    """Very lightweight YAML frontmatter parser for our schema."""
    data: Dict[str, str] = {}
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


def find_skill(name: str, vault: Path) -> Optional[Path]:
    lib = vault / LIBRARY_ROOT
    # Direct matches first
    for subdir in ["Skills", "Prompts", "Protocols", "Contexts"]:
        p = lib / subdir / f"{name}.md"
        if p.exists():
            return p

    # Fuzzy search across the library
    for subdir in ["Skills", "Prompts", "Protocols", "Contexts"]:
        folder = lib / subdir
        if not folder.exists():
            continue
        for f in folder.glob("*.md"):
            if name.lower() in f.stem.lower():
                return f
    return None


def get_skill_description(path: Path) -> str:
    fm, _ = load_note(path)
    data = parse_frontmatter(fm)
    return data.get("description", "").replace("\n", " ").strip()[:120]


def clean_body(body: str) -> str:
    """Remove Obsidian-specific syntax for clean pasting."""
    body = re.sub(r'\[\[([^\]|]+)(\|[^\]]+)?\]\]', r'\1', body)  # wikilinks
    body = re.sub(r'!\[\[[^\]]+\]\]', '', body)  # remove embedded images
    return body.strip()


def build_emission(paths: List[Path], include_master: bool = False, vault: Optional[Path] = None) -> str:
    """Build a clean, ready-to-paste block for one or more skills."""
    lines = []
    lines.append("# Emitted from Obsidian Skill & Prompt Library")
    lines.append("# Source of truth: 09-PROMPTS/Library (Obsidian)")
    lines.append("# Usage: Start with /bootstrap, then add /tp, /daily-execution, /low, or /council as needed.")
    lines.append("")

    if include_master and vault:
        master_path = find_skill("master-bio", vault)
        if master_path:
            fm, body = load_note(master_path)
            if not is_project_specific(master_path.stem, fm, body):
                lines.append("## Master Context (inject this in most conversations)")
                lines.append("```markdown")
                if fm:
                    lines.append("---")
                    lines.append(fm)
                    lines.append("---")
                lines.append(clean_body(body))
                lines.append("```")
                lines.append("")

    for p in paths:
        fm_text, body = load_note(p)
        if is_project_specific(p.stem, fm_text, body):
            continue
        data = parse_frontmatter(fm_text)
        name = data.get("name", p.stem)
        desc = data.get("description", "")
        energy = data.get("energy", "")
        domain = data.get("domain", "")

        lines.append(f"## Skill / Protocol: {name}")
        if desc:
            lines.append(f"**Description:** {desc}")
        if energy or domain:
            meta = []
            if energy: meta.append(f"Energy: {energy}")
            if domain: meta.append(f"Domain: {domain}")
            lines.append(f"**Meta:** {' | '.join(meta)}")
        lines.append("")
        lines.append("```markdown")
        if fm_text:
            lines.append("---")
            lines.append(fm_text)
            lines.append("---")
            lines.append("")
        lines.append(clean_body(body))
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def list_skills(vault: Path, search_term: str = "") -> None:
    lib = vault / LIBRARY_ROOT
    categories = {
        "Skills": lib / "Skills",
        "Prompts": lib / "Prompts",
        "Protocols": lib / "Protocols",
        "Contexts": lib / "Contexts",
    }

    for cat_name, folder in categories.items():
        if not folder.exists():
            continue
        items = []
        for f in sorted(folder.glob("*.md")):
            if search_term and search_term.lower() not in f.stem.lower():
                continue
            fm, _ = load_note(f)
            data = parse_frontmatter(fm)
            desc = data.get("description", "")[:80]
            energy = data.get("energy", "")
            items.append((f.stem, energy, desc))

        if items:
            print(f"\n=== {cat_name} ===")
            for name, energy, desc in items:
                energy_str = f"[{energy}]" if energy else ""
                print(f"  {name} {energy_str}")
                if desc:
                    print(f"      {desc}")


def copy_to_clipboard(text: str) -> bool:
    """Windows clipboard via clip.exe. Returns True on success."""
    try:
        subprocess.run("clip", input=text.encode("utf-8"), check=True, shell=True)
        return True
    except Exception:
        return False


def load_dictionary(vault: Path) -> dict:
    """Load allowed values from the Library Dictionary.md for validation.
    Returns dict with sets: 'types', 'domains', 'energies', 'tags'."""
    result = {
        "types": set(),
        "domains": set(),
        "energies": set(),
        "tags": set(),
    }
    dict_path = vault / LIBRARY_ROOT / "Dictionary.md"
    if not dict_path.exists():
        # Fallback: minimal known good values for generic library work.
        result["types"] = {"skill", "prompt", "protocol", "context", "guide", "hub", "meta"}
        result["energies"] = {"collapse", "low", "medium", "high", "any", "variable"}
        result["domains"] = {"meta", "library", "context", "job", "execution", "social", "research", "decision-making", "recovery", "health", "creative", "ai-setup", "philosophy", "philosophy-snf", "finance", "prs", "sobriety", "career", "systems"}
        result["tags"] = {"low-energy", "routine", "low-friction", "daily", "weekly", "external-memory", "cognitive-offloading", "systems", "research", "career"}
        return result

    text = dict_path.read_text(encoding="utf-8", errors="ignore")

    # Very lightweight extraction from the known Dictionary format (markdown tables + lists)
    # Types
    for line in text.splitlines():
        if "|" in line and "type" in line.lower():
            continue
        if "skill" in line.lower() or "prompt" in line.lower() or "protocol" in line.lower():
            for t in ["skill", "prompt", "protocol", "context", "guide", "hub", "meta"]:
                if t in line.lower():
                    result["types"].add(t)

    # Energies (from the energy table section)
    for e in ["collapse", "low", "medium", "high", "any", "variable"]:
        if e in text.lower():
            result["energies"].add(e)

    # Domains (from the domain table)
    known_domains = ["meta", "library", "context", "job", "execution", "social", "research", "decision-making", "recovery", "health", "creative", "ai-setup", "philosophy", "philosophy-snf", "finance", "prs", "sobriety", "career", "systems"]
    for d in known_domains:
        if d in text:
            result["domains"].add(d)

    # Tags: harvest from the core tags lists and generic usage.
    tag_candidates = ["low-energy", "routine", "low-friction", "daily", "weekly", "external-memory", "cognitive-offloading", "systems", "research", "career"]
    for t in tag_candidates:
        if t in text or t.replace("-", "") in text.replace(" ", "").lower():
            result["tags"].add(t)

    result["domains"].update({"context", "execution", "systems", "research"})
    result["tags"].update({"external-memory", "low-friction", "systems"})
    result["energies"].update({"low", "collapse", "medium"})
    result["types"].update({"skill"})

    return result


def validate_against_dictionary(path: Path, vault: Path, allowed: dict) -> list:
    """Return list of issues (empty = compliant)."""
    issues = []
    fm_text, _ = load_note(path)
    data = parse_frontmatter(fm_text)

    # type
    t = data.get("type", "").strip().lower()
    if t and t not in allowed.get("types", set()):
        issues.append(f"type '{t}' not in Dictionary types")

    # energy
    e = data.get("energy", "").strip().lower()
    if e and e not in allowed.get("energies", set()):
        issues.append(f"energy '{e}' not in Dictionary energies")

    # domain (can be list-like or comma)
    dom_raw = data.get("domain", "") or data.get("domains", "")
    for dpart in re.split(r"[\[\],;\s]+", dom_raw):
        d = dpart.strip("[]'\" ").lower()
        if d and d not in allowed.get("domains", set()):
            issues.append(f"domain '{d}' not in Dictionary domains")

    # tags (loose check; many are free-form but core ones should be known)
    tags_raw = data.get("tags", "") or ""
    for tpart in re.split(r"[\[\],;\s]+", tags_raw):
        tg = tpart.strip("[]'\" ").lower()
        if tg and tg not in allowed.get("tags", set()) and len(tg) > 2:
            # Only warn on very core expected ones; others are allowed to be project-specific
            if tg in {"visible-proof", "external-memory"}:
                issues.append(f"core tag '{tg}' not recognized (consider adding to Dictionary)")

    return issues


def main():
    args = sys.argv[1:]

    if not args:
        print(__doc__)
        print("\nExamples:")
        print("  python emit-skill.py --list")
        print("  python emit-skill.py --daily --clip")
        print("  python emit-skill.py daily-job-search low-energy-execution --with-master")
        print("  python emit-skill.py --validate mvd-anchors")
        print("  python emit-skill.py --favorites")
        sys.exit(0)

    vault = find_vault()
    allowed = load_dictionary(vault)
    do_clip = "--clip" in args
    include_master = "--with-master" in args or "--daily" in args
    search_term = ""
    skill_names: List[str] = []
    do_list = False
    do_daily = False
    do_favorites = False
    do_validate = None

    for i, arg in enumerate(args):
        if arg in ("--list", "-l"):
            do_list = True
        elif arg in ("--daily", "-d"):
            do_daily = True
        elif arg in ("--favorites", "-f"):
            do_favorites = True
        elif arg.startswith("--search="):
            search_term = arg.split("=", 1)[1]
        elif arg == "--search" and i + 1 < len(args):
            search_term = args[i + 1]
        elif arg in ("--validate", "-v") and i + 1 < len(args):
            do_validate = args[i + 1]
        elif not arg.startswith("--"):
            skill_names.append(arg)

    if do_list or search_term:
        list_skills(vault, search_term)
        return

    if do_validate:
        p = find_skill(do_validate, vault)
        if not p:
            print(f"Could not find {do_validate}")
            sys.exit(1)
        issues = validate_against_dictionary(p, vault, allowed)
        if issues:
            print(f"Validation issues for {do_validate}:")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"{do_validate} is compliant with the Dictionary.")
        return

    if do_daily:
        # Build a powerful daily pack
        paths = []
        for name in DAILY_DEFAULT_SKILLS:
            p = find_skill(name, vault)
            if p:
                paths.append(p)
        if not paths:
            print("Could not find daily default skills. Check DAILY_DEFAULT_SKILLS in the script.")
            sys.exit(1)

        output = build_emission(paths, include_master=True, vault=vault)
        output = "# DAILY EXECUTION PACK\n\n" + output
        output += "\n\n## Your Current Status Block (fill this in)\n"
        output += "```\n[Energy: | Runway weeks: | One non-negotiable today: | Job search activity: ]\n```"

        print(output)
        if do_clip and copy_to_clipboard(output):
            print("\n[Copied to clipboard]")
        return

    if do_favorites:
        # Emit the favorites pack (great for quick access)
        paths = []
        for name in FAVORITES:
            p = find_skill(name, vault)
            if p:
                paths.append(p)
        if not paths:
            print("No favorites found.")
            sys.exit(1)

        output = build_emission(paths, include_master=True, vault=vault)
        output = "# FAVORITES PACK (most used / high value skills)\n\n" + output
        output += "\n\nTip: Use --daily for the core low-energy daily set, or --favorites for the broader quick-access collection."

        print(output)
        if do_clip and copy_to_clipboard(output):
            print("\n[Copied to clipboard]")
        return

    if not skill_names:
        print("No skill names provided. Use --list or --daily.")
        sys.exit(1)

    paths = []
    for name in skill_names:
        p = find_skill(name, vault)
        if not p:
            print(f"Warning: Could not find '{name}'")
            continue
        # Validate on emit
        issues = validate_against_dictionary(p, vault, allowed)
        if issues:
            print(f"Note: {name} has dictionary compliance issues (run with --validate {name} for details).")
        paths.append(p)

    if not paths:
        sys.exit(1)

    output = build_emission(paths, include_master=include_master, vault=vault)

    print(output)
    if do_clip and copy_to_clipboard(output):
        print("\n[Copied to clipboard]")


if __name__ == "__main__":
    main()
