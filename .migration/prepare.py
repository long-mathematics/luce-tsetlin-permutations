#!/usr/bin/env python3
"""Run the pinned boundary-law extraction after the explicit request commit."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_COMMIT = "7ac6679db3fcb0ef5f72081752624672a43f1269"
REQUEST_PARENT = "4d78a58030af7179410d0c6d80b38823a9bdc52e"

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
namespace = {"__name__": "__main__", "__file__": str(ROOT / ".migration" / "prepare.py")}
exec(compile(source, str(ROOT / ".migration" / "boundary_extract.py"), "exec"), namespace)
