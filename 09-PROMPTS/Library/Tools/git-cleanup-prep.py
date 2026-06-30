#!/usr/bin/env python3
"""
git-cleanup-prep.py

Prepares the DOV vault Git state for a safe push:
1. Reports current status (modified, untracked, deleted)
2. Identifies private/adult files that must NOT be committed
3. Stages the Meta/ -> _Meta/ rename explicitly
4. Generates a ready-to-run cleanup command sequence

This script is READ-ONLY by default. Run with --execute to apply changes.

Usage:
    python git-cleanup-prep.py           # Report only
    python git-cleanup-prep.py --execute  # Apply the safe steps
"""

import subprocess
import sys
from pathlib import Path

VAULT = Path(r"C:\ROOT_OBSIDIAN\DOV")

PRIVATE_RISK_FILES = [
    "00-CAPTURE/App Captures/TMHLBB.md",
    "00-CAPTURE/App Captures/Clippings/TMWLBB.md",
    "09-PROMPTS/Prompt-Library/BE_Roleplay_Generator.md",
]

PRIVATE_DEST = "_PRIVATE/SMUT"


def run(cmd, cwd=VAULT, capture=True):
    r = subprocess.run(cmd, shell=True, cwd=str(cwd), capture_output=capture, text=True)
    return r.stdout.strip(), r.stderr.strip()


def report():
    out, _ = run("git status --short")
    lines = out.splitlines()
    modified = [l for l in lines if l.startswith(" M") or l.startswith("M ")]
    untracked = [l for l in lines if l.startswith("??")]
    deleted = [l for l in lines if l.startswith(" D") or l.startswith("D ")]

    print("=" * 60)
    print("DOV VAULT GIT STATE REPORT")
    print("=" * 60)
    print(f"Modified:   {len(modified)}")
    print(f"Untracked:  {len(untracked)}")
    print(f"Deleted:    {len(deleted)}")
    print()

    print("PRIVATE RISK FILES (must move before push):")
    for f in PRIVATE_RISK_FILES:
        p = VAULT / f
        exists = "EXISTS" if p.exists() else "MISSING (already moved?)"
        print(f"  [{exists}] {f}")
    print()

    print("DELETED FILES (legacy Meta/ -> _Meta/ rename):")
    for l in deleted:
        print(f"  {l.strip()}")
    print()

    print("MODIFIED LIBRARY FILES:")
    for l in modified:
        if "09-PROMPTS" in l or "_Meta" in l:
            print(f"  {l.strip()}")
    print()

    print("RECOMMENDED STEPS:")
    print("  1. Move private files to _PRIVATE/SMUT/")
    print("  2. git rm --cached <private-files>  (unstage them)")
    print("  3. git add _Meta/  (stage the renamed Meta/ folder)")
    print("  4. git add -u  (stage all other tracked changes)")
    print("  5. git commit -m 'Rename Meta/ to _Meta/, update Library skills'")
    print("  6. git push")
    print()
    print("Run with --execute to apply steps 1-4 automatically.")
    print("Steps 5-6 (commit and push) always require manual confirmation.")


def execute():
    print("EXECUTING SAFE CLEANUP STEPS...")
    print()

    # Step 1: Move private files
    dest_dir = VAULT / PRIVATE_DEST
    dest_dir.mkdir(parents=True, exist_ok=True)
    for f in PRIVATE_RISK_FILES:
        src = VAULT / f
        if src.exists():
            dst = dest_dir / src.name
            print(f"Moving {src.name} -> {PRIVATE_DEST}/")
            src.rename(dst)
        else:
            print(f"Already moved or missing: {f}")

    # Step 2: Unstage private files from git tracking
    for f in PRIVATE_RISK_FILES:
        out, err = run(f'git rm --cached "{f}" 2>/dev/null')
        if out:
            print(f"Unstaged: {f}")

    # Step 3: Stage _Meta/
    out, err = run("git add _Meta/")
    print("Staged: _Meta/")

    # Step 4: Stage all tracked changes
    out, err = run("git add -u")
    print("Staged: all tracked changes (git add -u)")

    print()
    print("READY TO COMMIT. Run this command to finalize:")
    print()
    print("  cd C:\\ROOT_OBSIDIAN\\DOV")
    print("  git commit -m \"Rename Meta/ to _Meta/, update Library skills, move private files\"")
    print("  git push")
    print()
    print("Review `git status` and `git diff --cached` before committing.")


if __name__ == "__main__":
    if "--execute" in sys.argv:
        execute()
    else:
        report()
