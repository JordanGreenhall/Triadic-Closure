#!/usr/bin/env python3
"""Deterministic P21 normalization verifier.

Run from any directory inside the repository:
    python3 _compiler/verify_p21.py --base 71a6f42de3b1f3c2ef26666a32f9d829777a5da6

An optional overlay directory replaces repository-relative text files for
failure-capability tests without mutating the worktree.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


LOCAL = "with-to-this-closure.md"
GLOBAL = "physics-domain-mature-status.md"
FRONTIERS = ("P21-F1", "P21-F2", "P21-F3")
INHERITED_P20_FRONTIERS = ("P20-F1", "P20-F2")
P21_BASE = "71a6f42de3b1f3c2ef26666a32f9d829777a5da6"


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
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
            target = target.replace("%20", " ")
            checked += 1
            resolved = (path.parent / target).resolve()
            require(
                errors,
                resolved.exists(),
                f"broken local link in {path.relative_to(root)}: {raw_target}",
            )
    return checked


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default=P21_BASE, help="exact base ref for the PR diff")
    parser.add_argument("--overlay", type=Path, help="temporary semantic-check overlay")
    args = parser.parse_args()

    root_result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
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
    require(
        errors,
        base_sha == P21_BASE,
        f"base must resolve to exact P21 base {P21_BASE}; got {base_sha}",
    )

    local = corpus_text(root, LOCAL, overlay)
    global_text = corpus_text(root, GLOBAL, overlay)
    required_local = (
        "# P21 With-to-This Closure and Decay Boundary",
        "## Unit opening note",
        "## Authority adjudication",
        "## Mature status",
        "## The mechanism",
        "## P6 boundary",
        "## Inverse closure and the decay skeleton",
        "## Neutron-specific candidate",
        "## Conservation, coupling, and product boundary",
        "## Claim record",
        "## Local frontier",
        "## Verdict",
        "**Direct Jordan rulings:** none carries unique P21 theory work.",
    )
    for item in required_local:
        require(errors, item in local, f"missing canonical P21 element: {item}")

    for frontier in FRONTIERS:
        files: list[str] = []
        for path in root.rglob("*.md"):
            rel = path.relative_to(root)
            if ".git" in rel.parts or "_compiler/verification" in rel.as_posix():
                continue
            if frontier in corpus_text(root, rel, overlay):
                files.append(rel.as_posix())
        require(
            errors,
            sorted(files) == sorted([GLOBAL, LOCAL]),
            f"{frontier} must occur only in local/global files; got {sorted(files)}",
        )
        require(
            errors,
            local.count(f"### {frontier} —") == 1,
            f"{frontier} must have one local heading",
        )
        require(
            errors,
            global_text.count(f"**{frontier} —") == 1,
            f"{frontier} must have one global entry",
        )

    for frontier in INHERITED_P20_FRONTIERS:
        files = []
        for path in root.rglob("*.md"):
            rel = path.relative_to(root)
            if ".git" in rel.parts or "_compiler/verification" in rel.as_posix():
                continue
            if frontier in corpus_text(root, rel, overlay):
                files.append(rel.as_posix())
        require(
            errors,
            sorted(files)
            == sorted([GLOBAL, "p20-baryon-closure-and-proton-neutron-relation.md"]),
            f"{frontier} inherited placement must remain P20 local/global only; got {sorted(files)}",
        )

    required_status = (
        "**Generic structural decay classifier:** Registered",
        "office reading `This -> With + From` is Conjectured",
        "`udd -> uud` as the framework transition is **Conjectured**",
        "Electron as decay product | Open as a framework derivation; empirical as observation",
        "Antineutrino as From-With receipt | Conjectured role-reading; empirical as observed particle label",
        "Lifetime, rate, branching ratios | Open as framework derivations; empirical as measurements",
        "A coherence barrier is included only when a barrier is actually exhibited",
        "P20's sign, access-weight, and magnitude frontiers remain inherited and unchanged",
    )
    for phrase in required_status:
        require(errors, phrase in local, f"canonical P21 status guard missing: {phrase}")

    active_files = (
        LOCAL,
        GLOBAL,
        "03-10-physics-concept-load-pass-ledger.md",
        "07-particle-identity-ledger.md",
        "11-decay-product-registration.md",
        "06-spin-helicity-chirality-lift.md",
        "06-spin-helicity-chirality-lift/06-spin-helicity-chirality-lift Readme.md",
        "p12-spin-helicity-handedness-and-chiral-coupling.md",
        "chiral-coupling-result.md",
        "d6-persistence.md",
        "flavor-mark-metric-and-neutron.md",
        "p13-particle-identity-and-native-role-taxonomy.md",
        "physics-domain-work-plan.md",
        "physics-section-guide.md",
        "physics-source-map.md",
        "physics-walk-checklist.md",
        "physics-walk-D1-D5-consolidated.md",
        "physics-walk-d1-d5-consolidated.md",
        "realizability-weighting-law.md",
        "amplitude-readout-theorem.md",
        "sm-content-smuggle-audit-frontier.md",
        "index.md",
    )
    combined = "\n".join(corpus_text(root, name, overlay) for name in active_files)
    banned = (
        "P21 material not yet normalized",
        "awaits P21 normalization",
        "P21 transition structure not yet normalized",
        "metastable standing escaping over a coherence-barrier",
        "[Registered: structure of the drain.]",
        "products are forced, not incidental",
        "binary handedness L/R + maximal chirality / V-A + parity violation",
        "maximal chirality/V-A and parity violation follow",
        "frequency proportional to coherence-participation",
        "**Boltzmann** the energy-measure instance",
    )
    for phrase in banned:
        require(errors, phrase not in combined, f"obsolete active formulation remains: {phrase}")

    consumer_guards = (
        "P21 Registers the generic structural decay classifier while keeping the neutron-specific inverse passage Conjectured",
        "Electron production is Open internally and empirical observationally",
        "No Registered native decay-product role",
        "relative channel propensity requires the amplitude/readout conditions",
        "not an independent source of decay doctrine",
    )
    for phrase in consumer_guards:
        require(errors, phrase in combined, f"P21 consumer guard missing: {phrase}")

    correction_guards = (
        "The chiral/vectorial coupling distinction and binary handedness are Registered at their bounded structural scopes.",
        "Weak-interaction chirality is empirical corroboration only.",
        "Maximal chirality and exact `V−A` as framework derivations remain Open",
        "identity of weight with observed long-run frequency remains Open",
        "claimed Boltzmann end-to-end instance remains undone",
        "escape weights are not rates",
        "Weight is not frequency",
    )
    for phrase in correction_guards:
        require(errors, phrase in combined, f"correction standing guard missing: {phrase}")

    historical = corpus_text(root, "neutron-consideration.md", overlay)
    require(
        errors,
        "status: historical-adversarial" in historical,
        "retained neutron draft is not marked historical/adversarial",
    )
    require(
        errors,
        "**Historical/adversarial section.**" in historical,
        "historical neutron decay route lacks a local authority guard",
    )
    require(
        errors,
        "Former Registered labels in this section do not govern" in historical,
        "historical Registered labels are not explicitly superseded",
    )

    supporting = corpus_text(root, "flavor-mark-metric-and-neutron.md", overlay)
    require(
        errors,
        "status: supporting-partially-superseded" in supporting,
        "integrated neutron source is not marked supporting/partially superseded",
    )
    require(
        errors,
        "is not an alternative canonical owner" in supporting,
        "integrated neutron source lacks its canonical-authority guard",
    )

    shadow = corpus_text(root, "11-decay-product-registration.md", overlay)
    require(errors, "status: supporting" in shadow, "Item 11 shadow is not supporting")
    require(
        errors,
        "P21 With-to-This Closure and Decay" in shadow,
        "Item 11 shadow does not route to P21",
    )
    require(
        errors,
        not (root / "11-decay-product-registration" / "11-decay-product-registration Readme.md").exists(),
        "redundant nested Item 11 loop README remains",
    )

    for upstream in (
        "p19-native-electron-ruler-and-proton-electron-ratio.md",
        "p20-baryon-closure-and-proton-neutron-relation.md",
    ):
        require(
            errors,
            not git(root, "diff", "--name-only", f"{args.base}...HEAD", "--", upstream).strip(),
            f"P21 reopened protected upstream owner {upstream}",
        )

    changed_names = git(root, "diff", "--name-only", f"{args.base}...HEAD").splitlines()
    forbidden_neighbor_patterns = ("p22", "gravity", "stress-energy", "lambda")
    for name in changed_names:
        lowered = name.lower()
        require(
            errors,
            not any(pattern in lowered for pattern in forbidden_neighbor_patterns),
            f"P21 changed excluded gravity neighbor: {name}",
        )

    changed = changed_markdown(root, args.base)
    link_count = check_links(root, changed, errors)
    diff_check = subprocess.run(
        ["git", "diff", "--check", f"{args.base}...HEAD"],
        cwd=root,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    require(
        errors,
        diff_check.returncode == 0,
        "diff hygiene failed: " + (diff_check.stdout + diff_check.stderr).strip(),
    )

    print("P21 deterministic normalization verification")
    print(f"base: {args.base}")
    print(f"changed Markdown files checked: {len(changed)}")
    print(f"local Markdown links checked: {link_count}")
    print("frontier placement: canonical local + global summary only")
    print("inherited P20-F1/P20-F2 placement: P20 local + global summary only")
    print("P19/P20 boundary: inherited, not reopened")
    print("P22 gravity boundary: excluded")
    print("Item 11 nested loop README: absent")

    if errors:
        print(f"FAIL ({len(errors)} errors)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("inverse passage: Conjectured, not inferred from forward closure")
    print("products: bounded by internal standing versus observation")
    print("rate/frequency/mechanism: Open, empirical, or quarantined")
    print("chirality: bounded structural result preserved; exact V−A Open")
    print("weighting: conditional measure preserved; observed frequency bridge Open")
    print("diff hygiene: checked")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
