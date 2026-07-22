from pathlib import Path

required = {
    "ch5-covalent-ionic-closure-and-electronegativity.md": [
        "Covalent–Ionic Closure and Electronegativity",
        "Mass separation is not CH5",
        "CH5-F1",
        "CH5-F2",
        "CH5-F3",
    ],
    "ch5-supersession-control.md": ["X1", "mislabeled", "CH6"],
    "chemistry-domain-mature-status.md": [
        "ch5-covalent-ionic-closure-and-electronegativity.md",
        "Mass separation and Born–Oppenheimer status remain X1-owned",
    ],
    "index.md": ["CH5 Covalent–Ionic Closure and Electronegativity"],
    "repository-inventory.md": ["Mass separation and Born–Oppenheimer status remain X1-owned"],
}

for filename, needles in required.items():
    text = Path(filename).read_text()
    for needle in needles:
        assert needle in text, f"{filename}: missing {needle!r}"

for forbidden in ["ch5-mass-separation-and-configuration-description.md"]:
    assert not Path(forbidden).exists(), f"obsolete mislabeled owner still exists: {forbidden}"

print("CH5 verification PASS")
