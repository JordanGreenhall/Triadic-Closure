#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNER = ROOT / "ch3-maintenance-relief-and-energetic-ordering.md"
STATUS = ROOT / "chemistry-domain-mature-status.md"

required_owner = [
    "Conjectured as a structural interpretation",
    "symmetry type alone does not determine energetic order",
    "CH3-F1",
    "CH3-F2",
    "CH3-F3",
    "CH4 may inherit only",
]
required_status = ["CH3", "CH3-F1", "CH3-F2", "CH3-F3"]

for text in required_owner:
    if text not in OWNER.read_text():
        raise SystemExit(f"CH3 verification FAIL owner missing: {text}")
for text in required_status:
    if text not in STATUS.read_text():
        raise SystemExit(f"CH3 verification FAIL status missing: {text}")
for ident in ("CH3-F1", "CH3-F2", "CH3-F3"):
    if OWNER.read_text().count(ident) != 1 or STATUS.read_text().count(ident) != 1:
        raise SystemExit(f"CH3 verification FAIL frontier placement: {ident}")
print("CH3 verification: PASS")