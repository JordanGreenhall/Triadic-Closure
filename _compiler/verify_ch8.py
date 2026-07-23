from pathlib import Path

root = Path(__file__).resolve().parents[1]
owner = (root / "ch8-reaction-site-taxonomy-and-acid-base-readings.md").read_text()
control = (root / "ch8-supersession-control.md").read_text()
status = (root / "chemistry-domain-mature-status.md").read_text()
index = (root / "index.md").read_text()
inventory = (root / "repository-inventory.md").read_text()

required = [
    "Shell-edge re-partnering",
    "Charge transfer",
    "Mixed passages",
    "Brønsted face",
    "Lewis face",
    "CH8-F1",
    "CH8-F2",
    "CH8-F3",
]
for token in required:
    assert token in owner, token

for excluded in [
    "Conservation ledgers",
    "Oxidation state",
    "Activation barrier",
    "Catalyst cycle",
    "Thermodynamic direction",
]:
    assert excluded not in owner, excluded

assert "CH8 owns only" in control
assert "CH9 owns activation, rates, and catalysis" in control
assert "ch8-reaction-site-taxonomy-and-acid-base-readings.md" in status
assert "ch8-reaction-site-taxonomy-and-acid-base-readings.md" in index
assert "ch8-reaction-site-taxonomy-and-acid-base-readings.md" in inventory
assert "ch8-chemical-passages-conservation-acid-base-and-oxidation-state.md" not in index
assert "ch8-chemical-passages-conservation-acid-base-and-oxidation-state.md" not in inventory

print("CH8 specification repair verification PASS")
