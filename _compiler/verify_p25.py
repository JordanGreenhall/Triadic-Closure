#!/usr/bin/env python3
"""Deterministic P25 normalization verifier.

Run from any directory inside the repository:
    python3 _compiler/verify_p25.py --base a965f72d339c18bb03cfe15bb036393d0c6cb378

An optional overlay directory replaces repository-relative text files for
failure-capability tests without mutating the worktree.
"""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path


LOCAL = "p25-grqm-background-conflict-and-nonrenormalizability.md"
GLOBAL = "physics-domain-mature-status.md"
FRONTIERS = ("P25-F1", "P25-F2")
P25_BASE = "a965f72d339c18bb03cfe15bb036393d0c6cb378"


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=root, check=False, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {detail}")
    return result.stdout


def require(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def corpus_text(root: Path, relative: str | Path, overlay: Path | None) -> str:
    relative_path = Path(relative)
    if overlay is not None and (overlay / relative_path).is_file():
        return (overlay / relative_path).read_text(encoding="utf-8")
    return (root / relative_path).read_text(encoding="utf-8")


def changed_markdown(root: Path, base: str) -> list[Path]:
    names = git(root, "diff", "--name-only", "--diff-filter=ACMR", f"{base}...HEAD")
    return sorted(
        (root / name for name in names.splitlines() if name.endswith(".md")),
        key=lambda path: path.relative_to(root).as_posix(),
    )


def check_links(root: Path, paths: list[Path], errors: list[str]) -> int:
    pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    checked = 0
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for raw_target in pattern.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            target = target.strip("<>").replace("%20", " ")
            checked += 1
            resolved = (path.parent / target).resolve()
            require(errors, resolved.exists(), f"broken local link in {path.relative_to(root)}: {raw_target}")
    return checked


def verify_bounded_logic(errors: list[str]) -> None:
    """Show exactly that G2 standing does not logically entail a completed G3."""
    valuations = [(g2, g3) for g2 in (False, True) for g3 in (False, True)]
    countermodels = [(g2, g3) for g2, g3 in valuations if g2 and not g3]
    require(errors, countermodels == [(True, False)],
            f"G2=>G3 independence countermodel changed: {countermodels}")

    deployments = {
        "spatial_arena": ("With-image", "horizontal", "P7 carrier debt"),
        "internal_pairing": ("This-image", "vertical", "P18 pairing boundary"),
    }
    require(errors, deployments["spatial_arena"] != deployments["internal_pairing"],
            "internal pairing incorrectly collapsed into the spatial arena")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default=P25_BASE, help="exact base ref for the PR diff")
    parser.add_argument("--overlay", type=Path, help="temporary semantic-check overlay")
    args = parser.parse_args()

    root_result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], check=False, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if root_result.returncode:
        print("FAIL repository discovery")
        return 1
    root = Path(root_result.stdout.strip()).resolve()
    overlay = args.overlay.resolve() if args.overlay else None
    errors: list[str] = []

    try:
        base_sha = git(root, "rev-parse", f"{args.base}^{{commit}}").strip()
    except RuntimeError as error:
        print(f"FAIL base resolution: {error}")
        return 1
    require(errors, base_sha == P25_BASE,
            f"base must resolve to exact P25 base {P25_BASE}; got {base_sha}")

    local = corpus_text(root, LOCAL, overlay)
    global_text = corpus_text(root, GLOBAL, overlay)
    required_local = (
        "# P25 GR/QM Background Conflict and Non-Renormalizability Diagnosis",
        "## Standing summary",
        "## Semantic boundary",
        "## Authority and lineage",
        "## Claim and warrant ledger",
        "## Essential form and mature accretions",
        "## Adversarial distinctions",
        "## Downstream use rules",
        "## Local research frontiers",
        "## Verification obligations",
        "## Source disposition",
        "Within a settled step the basis is flattened",
        "internal carrier pairing is not the spatial arena",
        "Conjectured overall and Unregistered as a completed framework derivation",
        "No framework-native perturbative integral, regulator, power-counting argument",
        "Discreteness is not automatic finiteness",
        "P26 owns",
        "P27 owns",
        "P28 owns",
    )
    for item in required_local:
        require(errors, item in local, f"missing canonical P25 element: {item}")

    for frontier in FRONTIERS:
        files: list[str] = []
        for path in root.rglob("*.md"):
            rel = path.relative_to(root)
            if ".git" in rel.parts or "_compiler/verification" in rel.as_posix():
                continue
            if frontier in corpus_text(root, rel, overlay):
                files.append(rel.as_posix())
        require(errors, sorted(files) == sorted([GLOBAL, LOCAL]),
                f"{frontier} must occur only in local/global files; got {sorted(files)}")
        require(errors, local.count(f"### {frontier} —") == 1,
                f"{frontier} must have one local heading")
        require(errors, global_text.count(f"**{frontier} —") == 1,
                f"{frontier} must have one global entry")

    for field in (
        "**Standing:**", "**Current strongest achieved result:**", "**Missing:**",
        "**Dependencies and downstream claims affected:**", "**False-completion warning:**",
        "**Next legitimate research action:**",
    ):
        require(errors, local.count(field) == 2,
                f"both local P25 frontiers must contain {field}; got {local.count(field)}")
    for frontier in FRONTIERS:
        entry = next((line for line in global_text.splitlines() if f"**{frontier} —" in line), "")
        for field in (
            "**Standing:**", "**Current strongest achieved result:**", "**Missing:**",
            "**Dependencies and downstream claims affected:**", "**False-completion warning:**",
            "**Local owner:**", "**Next legitimate research action:**",
        ):
            require(errors, field in entry, f"global {frontier} lacks Section 10.2 field {field}")

    source_guards = {
        "grqm-conflict-status.md": (
            "Current concise multi-unit status page",
            "Conjectured and Unregistered as a completed framework derivation",
            "concise multi-unit shadow",
        ),
        "grqm-problem-locator.md": (
            "This page is retained detailed provenance",
            "Conjectured overall and Unregistered as a completed derivation",
            "not the warrant for the framework identity",
            "not a calculation establishing the traditional failure",
        ),
        "sm-content-smuggle-audit-frontier.md": (
            "turning discreteness", "P25 GR/QM Background Conflict",
        ),
        "supersession-map.md": (
            "P25 GR/QM background-conflict and non-renormalizability standing",
            "Do not use a shared `g` symbol as the warrant",
        ),
    }
    for name, phrases in source_guards.items():
        text = corpus_text(root, name, overlay)
        for phrase in phrases:
            require(errors, phrase in text, f"{name} lacks P25 authority guard: {phrase}")

    active_files = (
        LOCAL, GLOBAL, "grqm-conflict-status.md", "grqm-problem-locator.md",
        "physics-domain-work-plan.md", "physics-section-guide.md", "physics-source-map.md",
        "physics-registration-theorem.md", "sm-content-smuggle-audit-frontier.md",
        "supersession-map.md", "index.md", "overview/triadic-closure-reading-order.md",
        "repository-inventory.md",
    )
    combined = "\n".join(corpus_text(root, name, overlay) for name in active_files)
    for phrase in (
        "flattened/live", "internal carrier pairing", "spatial arena",
        "Conjectured overall", "Unregistered as a completed", "perturbative",
        "P7", "P16", "P18", "P22", "P24", "P26", "P27", "P28",
    ):
        require(errors, phrase in combined, f"P25 consumer guard missing: {phrase}")

    banned_active = (
        "The dissolution (G2) and its symptom (G3) are Registered",
        "to be *explained as a symptom* (now done",
        "framework predicts the exact asymmetry the tradition observes",
        "G3 non-renormalizability as mislocated V/H crossing | Registered",
        "P25 non-renormalizability diagnosis | Registered",
        "discreteness proves finiteness",
        "P25 derives ultraviolet completion",
    )
    for phrase in banned_active:
        require(errors, phrase not in combined, f"obsolete active P25 formulation remains: {phrase}")

    guide = corpus_text(root, "physics-section-guide.md", overlay)
    sequence = (
        "24. [P24 Full Einstein Form as Conditional Tensor Rigidity]",
        "25. [P25 GR/QM Background Conflict and Non-Renormalizability Diagnosis]",
    )
    require(errors, all(item in guide for item in sequence),
            "physics section guide lacks P24/P25 sequence")
    require(errors, guide.index(sequence[0]) < guide.index(sequence[1]),
            "physics section guide does not route P24 before P25")

    routing_pairs = {
        "index.md": ("P25 GR/QM Background Conflict", "GR/QM Conflict Status"),
        "physics-section-guide.md": ("P25 GR/QM Background Conflict", "GR/QM Conflict Status"),
        "physics-source-map.md": ("p25-grqm-background-conflict-and-nonrenormalizability", "grqm-conflict-status"),
        "repository-inventory.md": ("p25-grqm-background-conflict-and-nonrenormalizability.md", "grqm-conflict-status.md"),
    }
    for name, (canonical, shadow) in routing_pairs.items():
        text = corpus_text(root, name, overlay)
        require(errors, canonical in text and shadow in text and text.index(canonical) < text.index(shadow),
                f"{name} lacks canonical-before-shadow P25 routing")

    verify_bounded_logic(errors)
    changed = changed_markdown(root, base_sha)
    link_count = check_links(root, changed, errors)
    require(errors, LOCAL in [path.relative_to(root).as_posix() for path in changed],
            "canonical P25 owner is not in exact-base changed Markdown")

    if errors:
        print("P25 normalization verification: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("P25 normalization verification: PASS")
    print(f"exact base: {base_sha}")
    print(f"changed Markdown checked: {len(changed)}")
    print(f"changed-file local links checked: {link_count}")
    print("frontier placement: local owner + global summary only")
    print("G2/G3 independence countermodel: G2=true, completed-G3=false")
    print("canonical routing and P7/P16/P18/P22/P24/P26-P28 boundaries: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
