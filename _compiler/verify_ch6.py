from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNER = ROOT / "ch6-catenation-branching-isomerism-and-functional-groups.md"
SUPERSESSION = ROOT / "ch6-supersession-control.md"
STATUS = ROOT / "chemistry-domain-mature-status.md"
INDEX = ROOT / "index.md"
INVENTORY = ROOT / "repository-inventory.md"

required_owner = [
    "Catenation, Branching, Isomerism, and Functional Groups",
    "residual-edge recursion",
    "composition and constitution",
    "functional group",
    "a ring is not aromaticity",
    "CH7 is still owed in full",
]

text = OWNER.read_text()
for token in required_owner:
    assert token.lower() in text.lower(), token

for forbidden_path in [
    ROOT / "ch6-delocalization-recursion-and-aromaticity.md",
]:
    assert not forbidden_path.exists(), forbidden_path

for token in ["cyclic delocalization", "ring modes", "4k+2", "aromatic closure"]:
    assert token.lower() in text.lower(), f"missing explicit CH7 deferral: {token}"

assert "canonical CH6 owner" in SUPERSESSION.read_text()
assert "CH7" in SUPERSESSION.read_text()
assert "ch6-catenation-branching-isomerism-and-functional-groups.md" in STATUS.read_text()
assert "ch6-catenation-branching-isomerism-and-functional-groups.md" in INDEX.read_text()
assert "ch6-catenation-branching-isomerism-and-functional-groups.md" in INVENTORY.read_text()

print("CH6 verifier: PASS")