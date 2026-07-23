from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required = [
    ROOT / "README.md",
    ROOT / "index.md",
    ROOT / "SCHEMA.md",
    ROOT / "repository-inventory.md",
]
for path in required:
    assert path.exists(), f"missing governing file: {path.name}"

assert not (ROOT / "overview" / "triadic-closure-reading-order.md").exists()
assert not (ROOT / "overview" / "corpus-cleanup-pass-report.md").exists()

index = (ROOT / "index.md").read_text(encoding="utf-8")
readme = (ROOT / "README.md").read_text(encoding="utf-8")
schema = (ROOT / "SCHEMA.md").read_text(encoding="utf-8")
inv = (ROOT / "repository-inventory.md").read_text(encoding="utf-8")

assert "canonical reader path" in index.lower()
assert "preserves semantics, not documents" in readme.lower()
assert "extract -> compress -> integrate -> verify -> delete" in schema
assert "work queue, not a retention class" in inv.lower()
assert "overview/triadic-closure-reading-order.md" not in index
assert "overview/corpus-cleanup-pass-report.md" not in index

print("global architecture and semantic compression verification: PASS")
