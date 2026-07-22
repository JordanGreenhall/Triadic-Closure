#!/usr/bin/env python3
"""Run stale-state mutations; every mutation must be rejected."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "79e113e4fce6498b303c5fdbc4a76b841a014f69"
FILES = [
    "x1-physics-maturity-and-chemistry-entry-gate.md",
    "physics-chemistry-gate-crossing.md",
    "physics-domain-mature-status.md",
    "index.md",
    "repository-inventory.md",
    "supersession-map.md",
]


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text()
    if old not in text:
        raise RuntimeError(f"mutation source missing in {path.name}: {old!r}")
    path.write_text(text.replace(old, new))


def main() -> None:
    mutations = [
        ("remove non-completion boundary", "x1-physics-maturity-and-chemistry-entry-gate.md", "not a completed chemistry entry theorem", ""),
        ("overgrade shell-edge constraint", "x1-physics-maturity-and-chemistry-entry-gate.md", "shell-edge closure-completion is a **candidate constraint, Conjectured and Unregistered**", "shell-edge closure-completion is **Secured and Registered**"),
        ("erase boundary failure", "x1-physics-maturity-and-chemistry-entry-gate.md", "not yet a chemistry boundary", "a chemistry boundary"),
        ("delete local atomic frontier", "x1-physics-maturity-and-chemistry-entry-gate.md", "X1-F1", "X1-REMOVED"),
        ("delete global atomic frontier", "physics-domain-mature-status.md", "X1-F1", "X1-REMOVED"),
        ("duplicate scale frontier in shadow", "physics-chemistry-gate-crossing.md", "## Downstream routing", "X1-F2\n\n## Downstream routing"),
        ("break canonical shadow route", "physics-chemistry-gate-crossing.md", "x1-physics-maturity-and-chemistry-entry-gate.md", "missing-x1-owner.md"),
        ("remove canonical index route", "index.md", "X1 Physics Maturity and Chemistry Entry Gate", "X1 Interface"),
        ("restore stale supersession route", "supersession-map.md", "Current: [X1 Physics Maturity and Chemistry Entry Gate]", "Candidate: [X1 Physics Maturity and Chemistry Entry Gate]"),
        ("claim Born–Oppenheimer derivation", "x1-physics-maturity-and-chemistry-entry-gate.md", "## Bottom line", "Born–Oppenheimer is derived\n\n## Bottom line"),
        ("register carbon selection", "x1-physics-maturity-and-chemistry-entry-gate.md", "## Bottom line", "carbon is the D7 provisioner **Registered\n\n## Bottom line"),
    ]

    results: list[str] = []
    for i, (name, filename, old, new) in enumerate(mutations, 1):
        with tempfile.TemporaryDirectory(prefix="x1-mutation-") as td:
            tmp = Path(td)
            (tmp / "_compiler").mkdir()
            for file in FILES:
                shutil.copy2(ROOT / file, tmp / file)
            shutil.copy2(ROOT / "_compiler/verify_x1.py", tmp / "_compiler/verify_x1.py")
            replace_once(tmp / filename, old, new)
            run = subprocess.run(
                ["python", str(tmp / "_compiler/verify_x1.py"), "--base", BASE],
                text=True,
                capture_output=True,
            )
            rejected = run.returncode != 0
            results.append(f"{i:02d}. {name}: {'REJECTED' if rejected else 'ACCEPTED-ERROR'}")
            if not rejected:
                print("\n".join(results))
                raise SystemExit(f"failure simulation accepted mutation: {name}")

    print("X1 stale-state failure simulations")
    print("\n".join(results))
    print(f"X1 failure simulations: PASS ({len(mutations)} mutation classes rejected)")


if __name__ == "__main__":
    main()
