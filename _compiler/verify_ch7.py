from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNER = ROOT / "ch7-cyclic-delocalization-and-aromatic-closure.md"
STATUS = ROOT / "chemistry-domain-mature-status.md"
INDEX = ROOT / "index.md"
INVENTORY = ROOT / "repository-inventory.md"
SUPERSESSION = ROOT / "ch7-supersession-control.md"

required_owner = [
    "CH7 — Cyclic Delocalization and Aromatic Closure",
    "A ring is a CH6 topology",
    "4k+2",
    "Secured conditionally",
    "aromatic stabilization",
    "CH7-F1",
    "CH7-F2",
    "CH7-F3",
]

for token in required_owner:
    assert token in OWNER.read_text(), f"missing owner token: {token}"

for path in [STATUS, INDEX, INVENTORY, SUPERSESSION]:
    text = path.read_text()
    assert "ch7-cyclic-delocalization-and-aromatic-closure.md" in text or path == SUPERSESSION

owner = OWNER.read_text()
for forbidden in [
    "CH7 owns reaction taxonomy",
    "aromatic stabilization is Secured",
    "heterocycle extension is Secured",
]:
    assert forbidden not in owner, f"forbidden promotion: {forbidden}"

assert "ch7" in SUPERSESSION.read_text().lower()
print("CH7 verification PASS")
