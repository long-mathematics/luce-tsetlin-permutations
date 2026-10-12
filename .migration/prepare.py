#!/usr/bin/env python3
"""Run the reconciler with the final status-test update."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
impl = ROOT / ".migration/status_impl.py"
source = impl.read_text(encoding="utf-8")
source = source.replace(
    'REQUEST_PARENT = "520fbfc5e3894afd3fd6e5eadb9ac9e0d59793b0"',
    'REQUEST_PARENT = "169210c6d8d85aab7afaabec0387dd8200b8e134"',
    1,
)
marker = "# Verify the frozen archive.\n"
injection = '''# Reconcile the extraction-only boundary regression with the completed audit.\nboundary_test_path = ROOT / "tests/test_boundary_extraction.py"\nboundary_test = boundary_test_path.read_text(encoding="utf-8")\nboundary_test = replace_once(\n    boundary_test,\n    'self.assertIn("proof audit is pending", status)',\n    'self.assertIn("audit passed, repairs pending", status)',\n    "boundary audit-status assertion",\n)\nboundary_test_path.write_text(boundary_test, encoding="utf-8")\n\n'''
if source.count(marker) != 1:
    raise ValueError("Unexpected archive-verification marker")
source = source.replace(marker, injection + marker, 1)
namespace = {
    "__name__": "__main__",
    "__file__": str(ROOT / ".migration/prepare.py"),
}
exec(compile(source, str(impl), "exec"), namespace)
impl.unlink()
# The shared workflow owns removal of this marker after preparation.  The
# reconciler removes its working copy, so recreate it for the workflow's
# unconditional `rm` step; it is not included in the final commit.
(ROOT / ".migration/request.json").write_text(
    '{\n  "stage": "integration",\n  "task": "monolith-decomposition-status",\n  "baseline_commit": "654a25c0ed0abfa267aee2970fd311544be39866"\n}\n',
    encoding="utf-8",
)
