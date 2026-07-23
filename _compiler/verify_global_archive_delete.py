from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DELETED = [
    "jordan-decisions.md",
    "cover-letter.md",
    "phi-forward-reconstruction.md",
    "mathematization-F10-status.md",
    "mathematization-F8-F11.md",
    "d3-color-forcing-argument.md",
    "d3-su3-conditional-theorem.md",
    "d3-as-established.md",
    "d4-as-established.md",
    "internal-structure-walk-move1.md",
    "internal-structure-walk-move2.md",
    "neutron-consideration.md",
    "physics-chemistry-gate-crossing.md",
]

REQUIRED = [
    "global-semantic-compression-rule.md",
    "repository-inventory.md",
    "p22-weak-field-gravity-as-participation-curvature.md",
    "gauge-structure-result.md",
    "p20-baryon-closure-and-proton-neutron-relation.md",
    "with-to-this-closure.md",
    "x1-physics-maturity-and-chemistry-entry-gate.md",
]

errors = []
for rel in DELETED:
    if (ROOT / rel).exists():
        errors.append(f"obsolete candidate still exists: {rel}")

for rel in REQUIRED:
    if not (ROOT / rel).exists():
        errors.append(f"required living owner/control missing: {rel}")

inventory = (ROOT / "repository-inventory.md").read_text(encoding="utf-8")
for rel in DELETED:
    if f"- `{rel}`" in inventory:
        errors.append(f"deleted candidate still listed as live inventory item: {rel}")

if "No historical-retention queue remains" not in inventory:
    errors.append("inventory does not close the provenance-candidate queue")

if errors:
    raise SystemExit("\n".join(errors))

print(f"PASS: {len(DELETED)} obsolete containers absent; living owners present; inventory reconciled")
