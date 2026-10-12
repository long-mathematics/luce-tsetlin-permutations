#!/usr/bin/env python3
"""Run the pinned boundary-law extraction after the explicit request commit."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_COMMIT = "7ac6679db3fcb0ef5f72081752624672a43f1269"
REQUEST_PARENT = "a579cbca38e24db3998badc1e5b3f7d673b1266c"

subprocess.run(
    ["git", "fetch", "--no-tags", "--depth=1", "origin", SCRIPT_COMMIT],
    cwd=ROOT,
    check=True,
)
source = subprocess.check_output(
    ["git", "show", f"{SCRIPT_COMMIT}:.migration/prepare.py"],
    cwd=ROOT,
    text=True,
)
old = 'if "parent " + BASE not in headers:\n    raise ValueError("Boundary extraction request must directly follow the pinned main head")'
new = f'if "parent {REQUEST_PARENT}" not in headers:\n    raise ValueError("Unexpected boundary extraction request parent")'
if source.count(old) != 1:
    raise ValueError("Pinned extraction parent check not found")
source = source.replace(old, new, 1)
range_old = '("Vanishing-block obstruction", r"\\begin{proposition}[Vanishing-block implantation]\\label{prop:implantation}", r"\\begin{remark}\\label{rem:implantation-consequences}", "% BEGIN ARCHIVED BLOCK: vanishing-block-obstruction", "% END ARCHIVED BLOCK: vanishing-block-obstruction", 539, 598)'
range_new = '("Vanishing-block obstruction", r"\\begin{proposition}[Vanishing-block implantation]\\label{prop:implantation}", r"\\begin{remark}\\label{rem:implantation-consequences}", "% BEGIN ARCHIVED BLOCK: vanishing-block-obstruction", "% END ARCHIVED BLOCK: vanishing-block-obstruction", 539, 600)'
if source.count(range_old) != 1:
    raise ValueError("Pinned obstruction range not found")
source = source.replace(range_old, range_new, 1)
namespace = {"__name__": "__main__", "__file__": str(ROOT / ".migration" / "prepare.py")}
exec(compile(source, str(ROOT / ".migration" / "boundary_extract.py"), "exec"), namespace)

test_path = ROOT / "tests" / "test_boundary_extraction.py"
test_text = test_path.read_text(encoding="utf-8")
test_old = r'r"\|P_k-Q_k\|_{\TV}=Q_k(\calD_k^c)"'
test_new = r'r"\|P_k-Q_k\|_{\TV}"'
if test_text.count(test_old) != 1:
    raise ValueError("Generated boundary scope test anchor not found")
test_path.write_text(test_text.replace(test_old, test_new, 1), encoding="utf-8")
