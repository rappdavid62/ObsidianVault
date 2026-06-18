"""Shared project/private boundary for Library sync and emit tools."""

from __future__ import annotations

import re

# Core meta skills — always export even if body mentions SNF in Related/Notes.
UNIVERSAL_ALWAYS_INCLUDE = frozenset({
    "thoroughness-protocol",
    "council-strategy",
    "tool-mode-decider",
    "library-gardener",
})

PROJECT_SPECIFIC_SKILL_NAMES = frozenset({
    "snf-hope-activation",
    "snf-proof-registration",
    "sobriety-anchors",
    "substrate-reminders",
    "mvd-anchors",
    "floor-wins",
    "prs-safety-check",
    "master-bio",
    "nightly-personal-systems-review",
})

PROJECT_SPECIFIC_DOMAINS = frozenset({"philosophy-snf", "sobriety", "prs"})
PROJECT_SPECIFIC_TAGS = frozenset({
    "philosophy-snf",
    "sobriety",
    "state-not-fate",
    "hope-activation",
    "proof-registration",
})


def parse_frontmatter_list_field(raw: str) -> set[str]:
    if not raw:
        return set()
    return {
        part.strip("[]'\" ").lower()
        for part in re.split(r"[\[\],;\s]+", raw)
        if part.strip("[]'\" ")
    }


def _frontmatter_domains_and_tags(fm_text: str) -> tuple[set[str], set[str]]:
    domains: set[str] = set()
    tags: set[str] = set()
    for line in fm_text.splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip().lower()
        val = val.strip()
        if key in ("domain", "domains"):
            domains |= parse_frontmatter_list_field(val)
        elif key == "tags":
            tags |= parse_frontmatter_list_field(val)
    return domains, tags


def is_project_specific(name: str, fm_text: str = "", body: str = "") -> bool:
    """
    True when a skill should stay out of .cursorrules and external sync.

    Classification uses slug + frontmatter only. Incidental mentions in the
    note body (e.g. Related links to sobriety-anchors) do not trigger exclusion.
    """
    del body  # body kept for call-site compatibility; not scanned
    stem = name.lower().strip()
    if stem in UNIVERSAL_ALWAYS_INCLUDE:
        return False
    if stem in PROJECT_SPECIFIC_SKILL_NAMES or stem.startswith("snf-"):
        return True

    domains, tags = _frontmatter_domains_and_tags(fm_text)
    if domains & PROJECT_SPECIFIC_DOMAINS:
        return True
    if tags & PROJECT_SPECIFIC_TAGS:
        return True
    return False
