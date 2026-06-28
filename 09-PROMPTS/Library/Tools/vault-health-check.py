#!/usr/bin/env python3
"""
vault-health-check.py

Creates a compact DOV second-brain health report.

Default behavior is read-only: print the report to stdout.
Use --write to refresh Meta/Second Brain Health Report.md.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path


TOOL_PATH = Path(__file__).resolve()
VAULT = TOOL_PATH.parents[3]
REPORT_PATH = VAULT / "Meta" / "Second Brain Health Report.md"

REQUIRED_PATHS = [
    "Meta/Master Context.md",
    "Meta/AI Command Layer.md",
    "Meta/AI Handoff Summary.md",
    "Meta/Second Brain Operations Dashboard.md",
    "Meta/Vault Cleanup Queue.md",
    "Meta/Legacy Bundle Migration Inventory.md",
    "09-PROMPTS/Library/README.md",
    "09-PROMPTS/Library/Hubs/00-Hub.md",
    "09-PROMPTS/Library/External Program Skill Wiring Matrix.md",
    "09-PROMPTS/Library/Skills/second-brain-control-loop.md",
    "09-PROMPTS/Library/Skills/vault-cleaner.md",
    "09-PROMPTS/Library/Skills/library-gardener.md",
    "09-PROMPTS/Library/Tools/emit-skill.py",
    "09-PROMPTS/Library/Tools/build-master-context.py",
    "09-PROMPTS/Library/Tools/export-for-phone.py",
    "09-PROMPTS/Library/Tools/vault-health-check.py",
    "08-TECH-AND-AI/Obsidian Integration/Integration Hub.md",
    "08-TECH-AND-AI/Obsidian Integration/app-proof-tracker.json",
    "00-CAPTURE/App Captures",
]

PRIVATE_IGNORE_PATTERNS = [
    "_PRIVATE/",
    "99_PRIVATE/",
    "99-PRIVATE/",
]

DRIFT_PATTERNS = [
    "Laptop Sync vault / DOV",
    "08 PROMPTS/Library",
    "08-PROMPTS/Library",
    "00-INBOX/App Captures",
    "C:\\ROOT_OBSIDIAN\\master-laptop-vault",
    "file:///C:/ROOT_OBSIDIAN/master-laptop-vault",
]

DRIFT_SCAN_ROOTS = [
    "Meta",
    "09-PROMPTS/Library",
    "08-TECH-AND-AI/Obsidian Integration",
]

ALLOW_DRIFT_FILES = {
    "09-PROMPTS/Library/Hubs/00-Hub.md",
    "09-PROMPTS/Library/Skills/second-brain-control-loop.md",
    "09-PROMPTS/Library/Mobile-Favorites.md",
    "09-PROMPTS/Library/Tools/build-master-context.py",
    "09-PROMPTS/Library/Tools/sync-all.py",
    "09-PROMPTS/Library/Tools/sync-to-grok.py",
    "08-TECH-AND-AI/Obsidian Integration/Source Code Registry.md",
}

GENERATED_CHECKS = [
    (
        "09-PROMPTS/Library/Mobile-Favorites.md",
        "# Source: C:\\ROOT_OBSIDIAN\\DOV\\09-PROMPTS\\Library",
    ),
    (
        "09-PROMPTS/Library/Tools/master_context_latest.txt",
        "C:\\ROOT_OBSIDIAN\\DOV\\09-PROMPTS\\Library",
    ),
]


def rel(path: Path) -> str:
    try:
        return path.relative_to(VAULT).as_posix()
    except ValueError:
        return str(path)


def run(args: list[str]) -> tuple[int, str]:
    try:
        proc = subprocess.run(
            args,
            cwd=VAULT,
            text=True,
            capture_output=True,
            check=False,
        )
    except FileNotFoundError as exc:
        return 127, str(exc)
    output = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode, output.strip()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def check_required_paths() -> list[str]:
    lines = []
    for item in REQUIRED_PATHS:
        path = VAULT / item
        mark = "OK" if path.exists() else "MISSING"
        lines.append(f"- {mark}: `{item}`")
    return lines


def check_private_boundaries() -> list[str]:
    lines = []
    gitignore = VAULT / ".gitignore"
    if gitignore.exists():
        text = read_text(gitignore)
        for pattern in PRIVATE_IGNORE_PATTERNS:
            mark = "OK" if pattern in text else "MISSING"
            lines.append(f"- {mark}: `.gitignore` contains `{pattern}`")
    else:
        lines.append("- MISSING: `.gitignore`")

    for item in ["_PRIVATE/SMUT", "99-PRIVATE"]:
        code, output = run(["git", "check-ignore", "-v", item])
        if code == 0:
            first = output.splitlines()[0] if output else "ignored"
            lines.append(f"- OK: `{item}` ignored by Git ({first})")
        else:
            lines.append(f"- RISK: `{item}` was not proven ignored by Git")
    return lines


def check_generated_outputs() -> list[str]:
    lines = []
    for item, expected in GENERATED_CHECKS:
        path = VAULT / item
        if not path.exists():
            lines.append(f"- MISSING: `{item}`")
            continue
        text = read_text(path)
        mark = "OK" if expected in text else "STALE"
        lines.append(f"- {mark}: `{item}` contains `{expected}`")
    return lines


def iter_markdown_and_text_files(root: Path):
    suffixes = {".md", ".txt", ".json", ".py", ".ps1"}
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in suffixes:
            yield path


def check_drift() -> tuple[list[str], list[str]]:
    active = []
    allowed = []
    for root_name in DRIFT_SCAN_ROOTS:
        root = VAULT / root_name
        if not root.exists():
            continue
        for path in iter_markdown_and_text_files(root):
            rel_path = rel(path)
            text = read_text(path)
            for pattern in DRIFT_PATTERNS:
                if pattern not in text:
                    continue
                entry = f"- `{rel_path}` contains `{pattern}`"
                if rel_path in ALLOW_DRIFT_FILES:
                    allowed.append(entry)
                else:
                    active.append(entry)
    return active, allowed


def check_git_status() -> list[str]:
    code, output = run(["git", "status", "--short", "--untracked-files=all"])
    if code != 0:
        return [f"- UNKNOWN: `git status` failed: {output or 'no output'}"]
    if not output:
        return ["- OK: worktree is clean"]

    lines = output.splitlines()
    modified = sum(1 for line in lines if line.startswith(" M") or line.startswith("M "))
    untracked = sum(1 for line in lines if line.startswith("??"))
    deleted = sum(1 for line in lines if line.startswith(" D") or line.startswith("D "))
    summary = [
        f"- INFO: {len(lines)} changed/untracked paths",
        f"- INFO: {modified} modified, {untracked} untracked, {deleted} deleted",
    ]
    for line in lines[:25]:
        summary.append(f"- `{line}`")
    if len(lines) > 25:
        summary.append(f"- ... {len(lines) - 25} more paths omitted")
    return summary


def build_report() -> str:
    active_drift, allowed_drift = check_drift()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    health = "attention needed" if active_drift else "stable with known open loops"

    parts = [
        "---",
        "Status: Active",
        "Primary Deployment Target: AI Infrastructure",
        "Expected Use Case: Current generated health report for DOV second-brain maintenance.",
        "Archive or Active: Active",
        "Canonical Home: Meta/Second Brain Health Report.md",
        f"Last Generated: {now}",
        "---",
        "",
        "# Second Brain Health Report",
        "",
        "## Bottom Line",
        "",
        f"DOV health is **{health}**. The canonical Library path is `C:\\ROOT_OBSIDIAN\\DOV\\09-PROMPTS\\Library`.",
        "",
        "## Required Surfaces",
        "",
        *check_required_paths(),
        "",
        "## Private Boundaries",
        "",
        *check_private_boundaries(),
        "",
        "## Generated Outputs",
        "",
        *check_generated_outputs(),
        "",
        "## Source-Truth Drift",
        "",
    ]

    if active_drift:
        parts.extend(active_drift[:50])
        if len(active_drift) > 50:
            parts.append(f"- ... {len(active_drift) - 50} more active drift hits omitted")
    else:
        parts.append("- OK: no active stale source-truth phrases found outside allowed watchlist files.")

    parts.extend(["", "## Allowed Watchlist Hits", ""])
    if allowed_drift:
        parts.extend(allowed_drift[:50])
        if len(allowed_drift) > 50:
            parts.append(f"- ... {len(allowed_drift) - 50} more allowed hits omitted")
    else:
        parts.append("- OK: no allowed watchlist hits.")

    parts.extend(["", "## Git State", "", *check_git_status()])

    parts.extend(
        [
            "",
            "## Next Small Action",
            "",
            "- Review any active Source-Truth Drift items first.",
            "- Then run `library-gardener` if Library files changed.",
            "- Then run `vault-cleaner` for unresolved file-placement or privacy-boundary items.",
        ]
    )

    return "\n".join(parts) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a DOV second-brain health report.")
    parser.add_argument("--write", action="store_true", help="Write Meta/Second Brain Health Report.md")
    args = parser.parse_args()

    report = build_report()
    if args.write:
        REPORT_PATH.write_text(report, encoding="utf-8")
        print(f"Wrote {REPORT_PATH}")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
