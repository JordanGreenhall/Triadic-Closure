#!/usr/bin/env python3
"""Content verifier for normalized CH1 artifacts."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "owner": ROOT / "ch1-chemical-domain-gate-and-bond-primitive.md",
    "status": ROOT / "chemistry-domain-mature-status.md",
    "index": ROOT / "index.md",
    "inventory": ROOT / "repository-inventory.md",
    "opening": ROOT / "_compiler/verification/ch1-unit-opening.md",
    "authority": ROOT / "_compiler/verification/ch1-authority-adjudication.md",
}
REQUIRED = {
    "owner": [
        "Conjectured-strong as the selected candidate chemistry-D1 form",
        "Unregistered as an established chemistry occupant",
        "CH1-F1", "CH1-F2", "CH1-F3",
        "CH2 has not begun",
    ],
    "status": [
        "CH1-F1", "CH1-F2", "CH1-F3",
        "No chemistry D1 occupant is Registered",
    ],
    "index": [
        "CH1 Chemical Domain Gate and Bond Primitive",
        "Chemistry Domain Mature Status",
        "CH2 has not begun",
    ],
    "inventory": [
        "ch1-chemical-domain-gate-and-bond-primitive.md",
        "chemistry-domain-mature-status.md",
    ],
    "opening": ["CH1 — Chemical domain gate and bond primitive", "Do not begin CH2"],
    "authority": ["Claim 2 — a bond is a joint standing", "Conjectured-strong"],
}

for key, path in FILES.items():
    if not path.exists():
        raise SystemExit(f"CH1 verification: FAIL: missing {path}")
    text = path.read_text()
    for needle in REQUIRED[key]:
        if needle not in text:
            raise SystemExit(f"CH1 verification: FAIL: {path.name} lacks required text: {needle}")

owner = FILES["owner"].read_text()
status = FILES["status"].read_text()
for frontier in ("CH1-F1", "CH1-F2", "CH1-F3"):
    if owner.count(frontier) != 1 or status.count(frontier) != 1:
        raise SystemExit(f"CH1 verification: FAIL: frontier placement {frontier}")

for forbidden in ("bond is Registered", "chemistry entry is established", "Born–Oppenheimer is derived"):
    if forbidden in owner:
        raise SystemExit(f"CH1 verification: FAIL: false completion: {forbidden}")

print("CH1 verification: PASS")
print("semantic/control files verified: 6")
print("frontier placements verified: 3 local + 3 global")
print("CH2 boundary: preserved")
