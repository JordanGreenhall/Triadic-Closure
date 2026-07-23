from pathlib import Path

root = Path(__file__).resolve().parents[1]
owner = (root / "ch8-chemical-passages-conservation-acid-base-and-oxidation-state.md").read_text()
control = (root / "ch8-supersession-control.md").read_text()
status = (root / "chemistry-domain-mature-status.md").read_text()
index = (root / "index.md").read_text()
inventory = (root / "repository-inventory.md").read_text()

required = [
    "Chemical passage boundary",
    "Conservation ledgers",
    "Passage taxonomy by site",
    "Acid/base unification",
    "Oxidation state",
    "CH8-F1",
    "CH8-F2",
    "CH8-F3",
]
for token in required:
    assert token in owner, token

for excluded in ["functional groups as carried local invariants", "4k+2 closed-shell arithmetic"]:
    assert excluded not in owner

assert "CH6 remains the sole owner of functional groups" in control
assert "CH7 remains the sole owner of cyclic delocalization" in control
assert "CH8" in status
assert "ch8-chemical-passages-conservation-acid-base-and-oxidation-state.md" in index
assert "ch8-chemical-passages-conservation-acid-base-and-oxidation-state.md" in inventory

print("CH8 verification PASS")
