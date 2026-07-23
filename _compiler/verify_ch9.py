from pathlib import Path

root = Path(__file__).resolve().parents[1]
owner = (root / "ch9-activation-rates-and-catalysis.md").read_text()
control = (root / "ch9-supersession-control.md").read_text()
status = (root / "chemistry-domain-mature-status.md").read_text()
index = (root / "index.md").read_text()
inventory = (root / "repository-inventory.md").read_text()

required = [
    "Activation ridge",
    "Rate propensity",
    "Conditional exponential form",
    "Catalyst cycle",
    "CH9-F1",
    "CH9-F2",
    "CH9-F3",
]
for token in required:
    assert token in owner, token

for excluded in [
    "CH9 owns thermodynamic direction",
    "CH9 owns equilibrium",
    "CH9 owns reaction-site taxonomy",
]:
    assert excluded not in owner

assert "CH8 remains the sole owner of reaction-site taxonomy" in control
assert "CH10 remains the sole owner of thermodynamic direction and equilibrium" in control
assert "ch9-activation-rates-and-catalysis.md" in status
assert "ch9-activation-rates-and-catalysis.md" in index
assert "ch9-activation-rates-and-catalysis.md" in inventory

print("CH9 verification PASS")