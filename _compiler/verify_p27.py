#!/usr/bin/env python3
"""Deterministic verifier for normalization unit P27.

An optional overlay directory replaces repository-relative text files for
failure-capability tests without changing the worktree.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import NoReturn

ROOT = Path(__file__).resolve().parents[1]
OWNER = "p27-horizon-area-entropy-temperature-and-information.md"
GLOBAL = "physics-domain-mature-status.md"
BASE = "e945b65c5b67afa2818a55cc363eb42f2dc5306c"


def fail(message: str) -> NoReturn:
    print(f"P27 verification: FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def git(*args: str) -> str:
    try:
        return subprocess.check_output(
            ["git", *args], cwd=ROOT, text=True, stderr=subprocess.STDOUT
        ).strip()
    except subprocess.CalledProcessError as exc:
        fail(f"git {' '.join(args)} failed: {exc.output.strip()}")


def corpus_text(relative: str, overlay: Path | None) -> str:
    path = Path(relative)
    if overlay is not None and (overlay / path).is_file():
        return (overlay / path).read_text(encoding="utf-8")
    full = ROOT / path
    if not full.is_file():
        fail(f"required file absent: {relative}")
    return full.read_text(encoding="utf-8")


def require(text: str, needle: str, where: str) -> None:
    if needle not in text:
        fail(f"{where} lacks required text: {needle}")


def forbid(text: str, needle: str, where: str) -> None:
    if needle in text:
        fail(f"{where} retains forbidden text: {needle}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    parser.add_argument("--overlay", type=Path, help="temporary semantic-check overlay")
    args = parser.parse_args()
    if args.base != BASE:
        fail(f"base must be exact merged P26 head {BASE}, got {args.base}")
    git("cat-file", "-e", f"{args.base}^{{commit}}")
    overlay = args.overlay.resolve() if args.overlay else None

    changed = set(git("diff", "--name-only", f"{args.base}...HEAD").splitlines())
    working_changed = set(git("diff", "--name-only").splitlines())
    working_changed.update(git("diff", "--cached", "--name-only").splitlines())
    working_changed.update(git("ls-files", "--others", "--exclude-standard").splitlines())
    required_paths = {
        OWNER,
        GLOBAL,
        "grqm-conflict-status.md",
        "grqm-problem-locator.md",
        "_compiler/verify_p27.py",
        "_compiler/verify_p27_algebra.py",
        "_compiler/verification/p27-unit-opening.md",
        "_compiler/verification/p27-exact-finite-algebra.txt",
    }
    missing = required_paths - (changed | working_changed)
    if missing:
        fail(f"required changed paths absent: {sorted(missing)}")
    forbidden = {
        "p17-mass-as-closure-maintenance.md",
        "p22-weak-field-gravity-as-participation-curvature.md",
        "p23-stress-energy-as-three-office-source.md",
        "p24-full-einstein-form-as-conditional-rigidity.md",
        "p25-grqm-background-conflict-and-nonrenormalizability.md",
        "p26-matter-sourced-geometry-holonomy-and-bmv.md",
        "lambda-derived.md",
    }
    for path in changed | working_changed:
        if path in forbidden or path.startswith(("p28-", "p29-")):
            fail(f"neighbor or later-unit owner changed in P27: {path}")

    owner = corpus_text(OWNER, overlay)
    required_owner = (
        "physical horizon remains **Conjectured and Unregistered**",
        "source-coupled horizon solution is **Open and Unregistered**",
        "Physical horizon area as straddling-link count is therefore **Conjectured and Unregistered**",
        "Horizon entropy and an area law are **Open and Unregistered**",
        "physical relation `T=kappa/(2 pi)` are **Open and Unregistered**",
        "`S=A/4` is therefore **Open and Unregistered as a framework law**",
        "information preservation/unitary evaporation is **Open and Unregistered**",
        "P27-F1",
        "P27-F2",
        "P27-F3",
        "P22 selects a bounded weak-field clock model",
        "Sealed conditional algebra",
        "Conservation is not unitarity",
        "Page curve",
    )
    for needle in required_owner:
        require(owner, needle, OWNER)
    for stale in (
        "physical horizon is Registered",
        "horizon area is Registered",
        "temperature is Registered",
        "S=A/4 is Registered",
        "unitary evaporation is Registered",
    ):
        forbid(owner, stale, OWNER)

    status = corpus_text("grqm-conflict-status.md", overlay)
    locator = corpus_text("grqm-problem-locator.md", overlay)
    for text, where in ((status, "grqm-conflict-status.md"), (locator, "grqm-problem-locator.md")):
        require(text, OWNER, where)
        require(text, "physical horizon", where)
        require(text, "Conjectured", where)
        require(text, "Open", where)
        require(text, "Unregistered", where)
        require(text, "unitary", where)
    for stale in (
        "| Native horizon: mass = self-closure; horizon = total self-closure | Registered |",
        "| Area = straddling-link count | Registered shape |",
        "| `2π` temperature period | Registered, not Sealed |",
        "unitary-side by principle",
    ):
        forbid(status, stale, "grqm-conflict-status.md")
        forbid(locator, stale, "grqm-problem-locator.md")

    global_text = corpus_text(GLOBAL, overlay)
    for field in ("P27-F1", "P27-F2", "P27-F3"):
        require(global_text, field, GLOBAL)
        require(owner, field, OWNER)
        living = []
        for path in ROOT.rglob("*.md"):
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith((".git/", "_compiler/verification/")):
                continue
            text = corpus_text(rel, overlay)
            if field in text:
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
        "02-04-items-2-3-4-status.md",
    ):
        require(corpus_text(route, overlay), OWNER, route)

    algebra_evidence = corpus_text("_compiler/verification/p27-exact-finite-algebra.txt", overlay)
    for result in (
        "rotation_vector=",
        "boost_vector=",
        "cube_L=5 crossing_links=25 bulk_vertices=125",
        "conditional_dS_coefficient=1/4",
        "surjective=no",
        "P27 exact finite algebra: PASS",
    ):
        require(algebra_evidence, result, "p27-exact-finite-algebra.txt")
    algebra_run = subprocess.run(
        [sys.executable, str(ROOT / "_compiler/verify_p27_algebra.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if algebra_run.returncode != 0:
        fail(f"P27 algebra reproducer failed: {algebra_run.stderr.strip()}")
    if algebra_run.stdout != algebra_evidence:
        fail("P27 algebra output is not byte-identical to committed evidence")

    for path in (
        "_compiler/verification/p27-failure-horizon.txt",
        "_compiler/verification/p27-failure-area-entropy.txt",
        "_compiler/verification/p27-failure-temperature.txt",
        "_compiler/verification/p27-failure-unitarity.txt",
        "_compiler/verification/p27-failure-frontier.txt",
        "_compiler/verification/p27-failure-boundary.txt",
    ):
        require(corpus_text(path, overlay), "Result: REJECTED", path)

    markdown_changed = [p for p in changed | working_changed if p.endswith(".md")]
    links = sum(corpus_text(path, overlay).count("](") for path in markdown_changed)
    print(
        "P27 verification: PASS "
        f"(base {BASE}; {len(changed | working_changed)} changed files; "
        f"{len(markdown_changed)} changed Markdown files; {links} Markdown links scanned)"
    )


if __name__ == "__main__":
    main()
