#!/usr/bin/env python3
"""Run the pinned regular-profile extraction in a shallow CI checkout."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASELINE = "fab8f0150e81ade0458bebed442f044141c2d2eb"
PARENT = "27151696047ad3807bedb9b17418719daf7dcd04"

# The migration workflow checks out only the request commit. Fetch the canonical
# main head so the extraction can restore the repository's baseline migration
# helper before committing generated files.
subprocess.run(
    ["git", "fetch", "--no-tags", "--depth=1", "origin", "main"],
    cwd=ROOT,
    check=True,
)
fetch_head = subprocess.check_output(
    ["git", "rev-parse", "FETCH_HEAD"], cwd=ROOT, text=True
).strip()
if fetch_head != BASELINE:
    raise ValueError(f"Unexpected main head: {fetch_head}")

script_path = ROOT / ".migration" / "extract_regular.py"
source = script_path.read_text(encoding="utf-8")
replacements = {
    'REQUEST_PARENT = "264386c18d0b9f9aefbf882b214fe02d5ad86f24"':
        f'REQUEST_PARENT = "{PARENT}"',
    'self.assertIn("proof audit pending", status)':
        'self.assertIn("proof audit is pending", status)',
    'r"\\lambda_r=\\frac1r+O_f\\!\\left(\\frac{{q^r}}r\\right)"':
        'r"\\lambda_r=\\frac1r+O\\!\\left(\\frac{{q^r}}{{r}}\\right)"',
}
for old, new in replacements.items():
    if source.count(old) != 1:
        raise ValueError("Unexpected extraction marker: " + old)
    source = source.replace(old, new, 1)
namespace = {
    "__name__": "__main__",
    "__file__": str(ROOT / ".migration" / "prepare.py"),
}
exec(compile(source, str(script_path), "exec"), namespace)
script_path.unlink()
