#!/usr/bin/env python3
"""Regenerate .cursorrules and master_context_latest.txt for DOV only."""
import importlib.util
from pathlib import Path

tools = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("sync_all", tools / "sync-all.py")
sync_all = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync_all)

vault = Path(r"C:\ROOT_OBSIDIAN\DOV")
ctx = sync_all.build_master_context(vault, sync_all.DAILY_DEFAULT_SKILLS)
(vault / "09-PROMPTS" / "Library" / "Tools" / "master_context_latest.txt").write_text(ctx, encoding="utf-8")
(vault / ".cursorrules").write_text(ctx, encoding="utf-8")
print("Regenerated DOV .cursorrules and master_context_latest.txt")

