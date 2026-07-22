#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
owner = (ROOT / "ch4-ideal-local-molecular-geometry.md").read_text()
status = (ROOT / "chemistry-domain-mature-status.md").read_text()
index = (ROOT / "index.md").read_text()

required_owner = [
    "Secured conditionally",
    "chemistry selects maximal mutual separation",
    "Conjectured and Unregistered",
    "CH4-F1",
    "CH4-F2",
    "CH4-F3",
    "CH5 and later chemistry",
    "no-privileged-frame is not an energy functional",
]
for text in required_owner:
    assert text in owner, text
for frontier in ("CH4-F1", "CH4-F2", "CH4-F3"):
    assert owner.count(frontier) == 1
    assert status.count(frontier) == 1
assert "ch4-ideal-local-molecular-geometry.md" in status
assert "CH4 Ideal Local Molecular Geometry" in index
assert "CH5 has not begun" in status
assert "hybridization is derived" not in owner.lower()
print("CH4 verification: PASS")
