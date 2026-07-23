from pathlib import Path

root = Path(__file__).resolve().parents[1]
owner = (root / "ch10-thermodynamic-direction-and-equilibrium.md").read_text()
control = (root / "ch10-supersession-control.md").read_text()
status = (root / "chemistry-domain-mature-status.md").read_text()
index = (root / "index.md").read_text()
inventory = (root / "repository-inventory.md").read_text()

required = [
    "Thermodynamic direction",
    "Reversible passage balance",
    "Conditional exponential equilibrium form",
    "Equilibrium",
    "Separation from CH9",
    "CH10-F1",
    "CH10-F2",
    "CH10-F3",
]
for token in required:
    assert token in owner, token

for excluded in [
    "CH10 owns activation ridges",
    "CH10 owns reaction-site taxonomy",
    "derives Gibbs free energy",
    "derives numerical equilibrium constants",
]:
    assert excluded not in owner

assert "CH8 retains reaction-site taxonomy" in control
assert "CH9 retains activation, rates, and catalysis" in control
assert "CH10" in status
assert "ch10-thermodynamic-direction-and-equilibrium.md" in index
assert "ch10-thermodynamic-direction-and-equilibrium.md" in inventory

print("CH10 verification PASS")