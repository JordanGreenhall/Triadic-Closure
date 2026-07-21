#!/usr/bin/env python3
"""Deterministic verifier for normalization unit P26."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import NoReturn

ROOT = Path(__file__).resolve().parents[1]
OWNER = "p26-matter-sourced-geometry-holonomy-and-bmv.md"
GLOBAL = "physics-domain-mature-status.md"
BASE = "7071e4d6e95f90765f70db18826f0f6952c13de2"


def fail(message: str) -> NoReturn:
    print(f"P26 verification: FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def git(*args: str) -> str:
    try:
        return subprocess.check_output(
            ["git", *args], cwd=ROOT, text=True, stderr=subprocess.STDOUT
        ).strip()
    except subprocess.CalledProcessError as exc:
        fail(f"git {' '.join(args)} failed: {exc.output.strip()}")


def require(text: str, needle: str, where: str) -> None:
    if needle not in text:
        fail(f"{where} lacks required text: {needle}")


def forbid(text: str, needle: str, where: str) -> None:
    if needle in text:
        fail(f"{where} retains forbidden text: {needle}")


def read(path: str) -> str:
    p = ROOT / path
    if not p.is_file():
        fail(f"required file absent: {path}")
    return p.read_text()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    args = parser.parse_args()
    if args.base != BASE:
        fail(f"base must be exact merged P25 head {BASE}, got {args.base}")
    git("cat-file", "-e", f"{args.base}^{{commit}}")

    changed = set(git("diff", "--name-only", f"{args.base}...HEAD").splitlines())
    required_paths = {
        OWNER,
        GLOBAL,
        "grqm-conflict-status.md",
        "grqm-problem-locator.md",
        "_compiler/verify_p26.py",
        "_compiler/verification/p26-unit-opening.md",
        "_compiler/verification/p26-exact-finite-algebra.txt",
    }
    missing = required_paths - changed
    if missing:
        fail(f"required changed paths absent: {sorted(missing)}")
    forbidden_prefixes = (
        "p27-",
        "p28-",
        "p29-",
        "lambda-derived.md",
        "mass-as-self-closure.md",
    )
    for path in changed:
        if path.startswith(forbidden_prefixes):
            fail(f"later-unit owner changed in P26: {path}")

    owner = read(OWNER)
    for needle in (
        "General modal foundation",
        "Matter-fork / geometry-fork application",
        "No actual geometric superposition",
        "Imaginary-part algebra",
        "Postcosm edge connection and non-exactness",
        "BMV-positive as a framework implication",
        "No intrinsic gravitational decoherence floor",
        "Entanglement without on-shell gravitational radiation",
        "Standard BMV phase form",
        "external comparison",
        "does not imply",
        "not yet a framework-level falsifier",
        "P26-F1",
        "P26-F2",
        "P26-F3",
        "P27 owns the phase-period",
        "AUD-015",
    ):
        require(owner, needle, OWNER)
    for stale in (
        "BMV-positive is forced",
        "non-exactness is proven given complexness",
        "no intrinsic gravitational decoherence floor is Registered",
    ):
        forbid(owner, stale, OWNER)

    status = read("grqm-conflict-status.md")
    locator = read("grqm-problem-locator.md")
    for text, where in ((status, "grqm-conflict-status.md"), (locator, "grqm-problem-locator.md")):
        require(text, OWNER, where)
        require(text, "Conjectured / Unregistered", where)
        require(text, "not yet a framework-level falsifier", where)
        require(text, "AUD-015", where)
    forbid(status, "BMV-positive is forced", "grqm-conflict-status.md")
    forbid(locator, "non-exactness is **proven given", "grqm-problem-locator.md")

    global_text = read(GLOBAL)
    for field in ("P26-F1", "P26-F2", "P26-F3"):
        require(global_text, field, GLOBAL)
        require(owner, field, OWNER)
        living = []
        for path in ROOT.rglob("*.md"):
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith(".git/") or rel.startswith("_compiler/verification/"):
                continue
            if field in path.read_text():
                living.append(rel)
        if sorted(living) != sorted([OWNER, GLOBAL]):
            fail(f"{field} living placement is {sorted(living)}")

    for route in (
        "index.md",
        "physics-section-guide.md",
        "physics-source-map.md",
        "repository-inventory.md",
        "overview/triadic-closure-reading-order.md",
        "physics-domain-work-plan.md",
        "physics-registration-theorem.md",
        "supersession-map.md",
        "sm-content-smuggle-audit-frontier.md",
    ):
        require(read(route), OWNER, route)

    algebra = read("_compiler/verification/p26-exact-finite-algebra.txt")
    for result in (
        "imaginary-part antisymmetry: PASS",
        "complex-carrier nonvanishing countermodel: PASS",
        "exact-connection telescoping: PASS",
        "nonzero-loop obstruction to exactness: PASS",
        "No entry above establishes a BMV phase",
    ):
        require(algebra, result, "p26-exact-finite-algebra.txt")

    scripts = git("ls-files", "_compiler/scripts/*", "_compiler/*.py").splitlines()
    sim_scripts = [s for s in scripts if any(k in s.lower() for k in ("bmv", "holonomy", "postcosm"))]
    if sim_scripts:
        fail(f"unexpected claim that no P26 simulation reproducer is tracked; found {sim_scripts}")
    require(owner, "no tracked script", OWNER)
    require(locator, "documentary provenance only", "grqm-problem-locator.md")

    markdown_changed = [p for p in changed if p.endswith(".md")]
    links = 0
    for path in markdown_changed:
        text = read(path)
        links += text.count("](")
    print(
        "P26 verification: PASS "
        f"(base {BASE}; {len(changed)} changed files; "
        f"{len(markdown_changed)} changed Markdown files; {links} Markdown links scanned)"
    )


if __name__ == "__main__":
    main()
