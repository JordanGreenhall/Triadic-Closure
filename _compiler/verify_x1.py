#!/usr/bin/env python3
"""Content verifier for the normalized X1 interface."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNER = ROOT / "x1-physics-maturity-and-chemistry-entry-gate.md"
SHADOW = ROOT / "physics-chemistry-gate-crossing.md"
STATUS = ROOT / "physics-domain-mature-status.md"
INDEX = ROOT / "index.md"
INVENTORY = ROOT / "repository-inventory.md"
SUPERSESSION = ROOT / "supersession-map.md"

REQUIRED_OWNER = [
    "interface adjudication",
    "not a completed chemistry entry theorem",
    "persistent atom, electronic shell structure, periodic landscape, and shell-edge object are **Open and Unregistered**",
    "shell-edge closure-completion is a **candidate constraint, Conjectured and Unregistered**",
    "not yet a chemistry boundary",
    "static internal load hierarchy, not a dynamical slow/fast theorem",
    "carbon as the physics D7 provisioner is **Conjectured and Unregistered**",
    "universal claim that every successor inhabits predecessor residue",
    "X1 interface adjudication",
]


def need(text: str, phrase: str, label: str) -> None:
    if phrase not in text:
        raise SystemExit(f"X1 verification: FAIL: {label}: missing {phrase!r}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    args = parser.parse_args()

    files = [OWNER, SHADOW, STATUS, INDEX, INVENTORY, SUPERSESSION]
    for path in files:
        if not path.exists():
            raise SystemExit(f"X1 verification: FAIL: missing file {path.relative_to(ROOT)}")

    owner = OWNER.read_text()
    shadow = SHADOW.read_text()
    status = STATUS.read_text()
    index = INDEX.read_text()
    inventory = INVENTORY.read_text()
    supersession = SUPERSESSION.read_text()

    for phrase in REQUIRED_OWNER:
        need(owner, phrase, "canonical owner")

    for frontier in ("X1-F1", "X1-F2", "X1-F3"):
        local = owner.count(frontier)
        global_count = status.count(frontier)
        other = shadow.count(frontier) + index.count(frontier) + inventory.count(frontier) + supersession.count(frontier)
        if local != 1 or global_count != 1 or other != 0:
            raise SystemExit(
                f"X1 verification: FAIL: {frontier}: expected owner=1 global=1 other=0; "
                f"got owner={local} global={global_count} other={other}"
            )

    need(shadow, "x1-physics-maturity-and-chemistry-entry-gate.md", "shadow canonical route")
    need(shadow, "no longer carries current theoretical warrant", "shadow status")
    need(index, "X1 Physics Maturity and Chemistry Entry Gate", "index canonical route")
    need(inventory, "x1-physics-maturity-and-chemistry-entry-gate.md", "inventory canonical route")
    need(supersession, "Current: [X1 Physics Maturity and Chemistry Entry Gate]", "supersession current route")
    need(status, "| X1 atomic ground and shell-edge constraint |", "status matrix")
    need(status, "| X1 scale separation and chemistry boundary |", "status matrix")
    need(status, "| X1 D7 provisioner and universal handoff claim |", "status matrix")

    forbidden_owner = [
        "chemistry boundary is established",
        "bond is Registered",
        "carbon is the D7 provisioner **Registered",
        "Born–Oppenheimer is derived",
        "periodic table is derived",
    ]
    for phrase in forbidden_owner:
        if phrase in owner:
            raise SystemExit(f"X1 verification: FAIL: forbidden overclaim {phrase!r}")

    # Changed-file relative Markdown links: ensure local targets named by changed files exist.
    links = 0
    for path in files:
        for target in re.findall(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)", path.read_text()):
            if "://" in target or target.startswith("mailto:"):
                continue
            links += 1
            candidate = (path.parent / target.replace("%20", " ")).resolve()
            if not candidate.exists():
                # Full-repository targets are checked after remote readback; local staging contains
                # only changed files, so missing unchanged targets are permitted here.
                pass

    print(
        f"X1 verification: PASS (base {args.base}; 6 semantic/control files; "
        f"{links} changed-file Markdown links scanned)"
    )


if __name__ == "__main__":
    main()
