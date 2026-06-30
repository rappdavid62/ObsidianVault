#!/usr/bin/env python3
"""Quick validation check before/after sync-all."""
import importlib.util
import re
import sys
from pathlib import Path

tools = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("sync_all", tools / "sync-all.py")
sync_all = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync_all)

vault = Path(r"C:\ROOT_OBSIDIAN\DOV")
lib = vault / "09-PROMPTS" / "Library"
allowed = sync_all.load_dictionary(vault)

print("Dictionary domains:", ", ".join(sorted(allowed["domains"])))
print("Dictionary energies:", ", ".join(sorted(allowed["energies"])))
print()

issues = {}
for sub in ["Skills", "Protocols", "Prompts"]:
    folder = lib / sub
    if not folder.exists():
        continue
    for path in sorted(folder.glob("*.md")):
        if re.search(r" \d+\.md$", path.name):
            continue
        found = sync_all.validate_skill(path, allowed)
        if found:
            issues[path.stem] = found

if issues:
    print("VALIDATION ISSUES:")
    for name, errs in sorted(issues.items()):
        print(f"  {name}:")
        for e in errs:
            print(f"    - {e}")
    sys.exit(1)

print("All skills/prompts/protocols pass Dictionary validation.")
sys.exit(0)
