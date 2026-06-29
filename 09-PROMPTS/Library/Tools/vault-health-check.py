#!/usr/bin/env python3
"""
vault-health-check.py

Creates a compact DOV second-brain health report.

Default behavior is read-only: print the report to stdout.
Use --write to refresh _Meta/Second Brain Health Report.md.
Use --fail-on-attention to exit 2 when unresolved risks need attention.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


TOOL_PATH = Path(__file__).resolve()
VAULT = TOOL_PATH.parents[3]
META_DIR_NAME = "_Meta"
META_DISPLAY = "_Meta"
REPORT_REL = f"{META_DIR_NAME}/Second Brain Health Report.md"
REPORT_PATH = VAULT / REPORT_REL

REQUIRED_PATHS = [
    f"{META_DIR_NAME}/Master Context.md",
    f"{META_DIR_NAME}/AI Command Layer.md",
    f"{META_DIR_NAME}/AI Handoff Summary.md",
    f"{META_DIR_NAME}/Second Brain Operations Dashboard.md",
    f"{META_DIR_NAME}/Vault Cleanup Queue.md",
    f"{META_DIR_NAME}/Second Brain Completion Audit.md",
    f"{META_DIR_NAME}/Second Brain Runbook.md",
    f"{META_DIR_NAME}/Second Brain Learning Ledger.md",
    f"{META_DIR_NAME}/Legacy Bundle Migration Inventory.md",
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
    "09-PROMPTS/Library/Tools/vault-watcher.py",
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
    META_DIR_NAME,
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

APP_TRACKER_PATH = VAULT / "08-TECH-AND-AI" / "Obsidian Integration" / "app-proof-tracker.json"
LEARNING_LEDGER_PATH = VAULT / META_DIR_NAME / "Second Brain Learning Ledger.md"
CLEANUP_QUEUE_PATH = VAULT / META_DIR_NAME / "Vault Cleanup Queue.md"

PRIVATE_REVIEW_CANDIDATES = [
    "00-CAPTURE/App Captures/TMHLBB.md",
    "00-CAPTURE/App Captures/Clippings/TMWLBB.md",
    "09-PROMPTS/Prompt-Library/BE_Roleplay_Generator.md",
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


def app_note_name(app: str) -> str:
    return f"Apps - {app}.md"


def check_app_tracker() -> list[str]:
    if not APP_TRACKER_PATH.exists():
        return ["- MISSING: `08-TECH-AND-AI/Obsidian Integration/app-proof-tracker.json`"]

    try:
        data = json.loads(APP_TRACKER_PATH.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as exc:
        return [f"- RISK: app proof tracker JSON is invalid: {exc}"]

    apps = data.get("apps", [])
    counts: dict[str, int] = {}
    missing_notes = []
    for app in apps:
        status = app.get("status", "unknown")
        counts[status] = counts.get(status, 0) + 1
        note = VAULT / "08-TECH-AND-AI" / "Obsidian Integration" / app_note_name(app.get("app", ""))
        evidence = str(app.get("evidenceNote", ""))
        if not note.exists() and not evidence.startswith("00-CAPTURE"):
            missing_notes.append(app.get("app", "<unnamed>"))

    lines = [f"- OK: {len(apps)} apps tracked"]
    for status in sorted(counts):
        lines.append(f"- INFO: {counts[status]} `{status}`")
    if missing_notes:
        lines.append("- RISK: app tracker entries without app notes: " + ", ".join(missing_notes))
    else:
        lines.append("- OK: every tracker app has an app note or capture evidence")
    return lines


def check_learning_ledger() -> list[str]:
    if not LEARNING_LEDGER_PATH.exists():
        return [f"- MISSING: `{META_DISPLAY}/Second Brain Learning Ledger.md`"]

    text = read_text(LEARNING_LEDGER_PATH)
    open_items = 0
    promoted_items = 0
    in_fence = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.lstrip().startswith("- [ ]"):
            open_items += 1
        if line.lstrip().startswith("- [x]"):
            promoted_items += 1
    lines = [
        f"- OK: `{META_DISPLAY}/Second Brain Learning Ledger.md` exists",
        f"- INFO: {open_items} open learning inbox items",
        f"- INFO: {promoted_items} promoted learning items",
    ]
    if "## Inbox" not in text or "## Promoted" not in text:
        lines.append("- RISK: learning ledger is missing `Inbox` or `Promoted` sections")
    return lines


def check_cleanup_queue() -> tuple[list[str], bool]:
    if not CLEANUP_QUEUE_PATH.exists():
        return [f"- MISSING: `{META_DISPLAY}/Vault Cleanup Queue.md`"], True

    text = read_text(CLEANUP_QUEUE_PATH)
    high_risks = text.count("Risk Level: High")
    medium_risks = text.count("Risk Level: Medium")
    low_risks = text.count("Risk Level: Low")
    existing_private_candidates = [
        item for item in PRIVATE_REVIEW_CANDIDATES if (VAULT / item).exists()
    ]

    lines = [
        f"- OK: `{META_DISPLAY}/Vault Cleanup Queue.md` exists",
        f"- INFO: {high_risks} high-risk cleanup items, {medium_risks} medium-risk, {low_risks} low-risk",
    ]
    if existing_private_candidates:
        lines.append("- RISK: private/adult review candidates still exist and need explicit human approval before move/archive:")
        for item in existing_private_candidates:
            tracked_code, tracked_output = run(["git", "ls-files", "--", item])
            ignored_code, ignored_output = run(["git", "check-ignore", "-v", "--", item])
            tracked = bool(tracked_output.strip())
            ignored = ignored_code == 0
            state = "tracked by Git" if tracked else "not tracked by Git"
            if ignored:
                first_ignore = ignored_output.splitlines()[0] if ignored_output else "ignored"
                state += f"; ignored ({first_ignore})"
            else:
                state += "; not ignored"
            lines.append(f"  - `{item}` ({state})")
    else:
        lines.append("- OK: no configured private/adult review candidates currently exist at the watched paths")

    if "Do not delete files permanently" not in text:
        lines.append("- RISK: cleanup queue is missing the non-destructive deletion rule")

    return lines, bool(existing_private_candidates or high_risks)


def count_learning_ledger_items() -> tuple[int, int]:
    if not LEARNING_LEDGER_PATH.exists():
        return 0, 0

    text = read_text(LEARNING_LEDGER_PATH)
    open_items = 0
    promoted_items = 0
    in_fence = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.lstrip().startswith("- [ ]"):
            open_items += 1
        if line.lstrip().startswith("- [x]"):
            promoted_items += 1
    return open_items, promoted_items


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
            if path in {TOOL_PATH, REPORT_PATH}:
                continue
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


def check_git_status() -> tuple[list[str], bool]:
    code, output = run(["git", "status", "--short", "--untracked-files=all"])
    if code != 0:
        return [f"- UNKNOWN: `git status` failed: {output or 'no output'}"], True
    if not output:
        return ["- OK: worktree is clean"], False

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
    if deleted:
        summary.append("- RISK: tracked files are deleted in Git state; resolve or explicitly approve the rename/removal before push.")
    return summary, bool(deleted)


def build_report() -> tuple[str, bool]:
    active_drift, allowed_drift = check_drift()
    open_learning, _promoted_learning = count_learning_ledger_items()
    cleanup_lines, cleanup_attention = check_cleanup_queue()
    git_lines, git_attention = check_git_status()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    attention_needed = bool(active_drift or cleanup_attention or git_attention)
    health = "attention needed" if attention_needed else "stable with known open loops"

    parts = [
        "---",
        "Status: Active",
        "Primary Deployment Target: AI Infrastructure",
        "Expected Use Case: Current generated health report for DOV second-brain maintenance.",
        "Archive or Active: Active",
        f"Canonical Home: {META_DISPLAY}/Second Brain Health Report.md",
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
        "## App Proof Tracker",
        "",
        *check_app_tracker(),
        "",
        "## Learning Ledger",
        "",
        *check_learning_ledger(),
        "",
        "## Cleanup Queue",
        "",
        *cleanup_lines,
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

    parts.extend(["", "## Git State", "", *git_lines])

    next_actions = ["", "## Next Small Action", ""]
    if active_drift:
        next_actions.append("- Review active Source-Truth Drift items first.")
    elif git_attention:
        next_actions.append("- Resolve or explicitly approve tracked-file deletions/renames in Git state before any push.")
    elif cleanup_attention:
        next_actions.append(f"- Resolve or explicitly defer high-risk cleanup items in `{META_DISPLAY}/Vault Cleanup Queue.md` before any push.")
    elif open_learning:
        next_actions.append(f"- Promote or clarify open items in `{META_DISPLAY}/Second Brain Learning Ledger.md`.")
    else:
        next_actions.append(f"- Run the weekly loop in `{META_DISPLAY}/Second Brain Runbook.md` after the current changes settle.")
    next_actions.append("- Run `library-gardener` if Library files changed.")
    next_actions.append("- Run `vault-cleaner` for unresolved file-placement or privacy-boundary items.")
    parts.extend(next_actions)

    return "\n".join(parts) + "\n", attention_needed


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a DOV second-brain health report.")
    parser.add_argument("--write", action="store_true", help=f"Write {REPORT_REL}")
    parser.add_argument(
        "--fail-on-attention",
        action="store_true",
        help="Exit 2 when the generated report says attention is needed",
    )
    args = parser.parse_args()

    report, attention_needed = build_report()
    if args.write:
        REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        REPORT_PATH.write_text(report, encoding="utf-8")
        print(f"Wrote {REPORT_PATH}")
    else:
        print(report)
    if args.fail_on_attention and attention_needed:
        print("vault-health-check: attention needed; exiting 2", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
