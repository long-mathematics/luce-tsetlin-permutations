#!/usr/bin/env python3
"""Prepare the endpoint short-cycle mechanical extraction."""
from pathlib import Path
import json
import os
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = "83702a015ba84aa41fb9fe71d34300561b109224"
CONFIG = ROOT / ".migration" / "short-config.json"

request = json.loads((ROOT / ".migration/request.json").read_text())
expected = {"stage":"integration","task":"endpoint-short-cycles-extraction","baseline_commit":BASE}
if request != expected:
    raise ValueError("Unexpected endpoint short-cycle extraction request")
if not os.environ.get("GITHUB_REF_NAME", "").startswith("migration/"):
    raise SystemExit("Extraction requires a migration branch")
subprocess.run(["python3", "scripts/extract_monolith_section.py", str(CONFIG)], cwd=ROOT, check=True)
CONFIG.unlink()
subprocess.run(["git", "fetch", "--no-tags", "--depth=1", "origin", BASE], cwd=ROOT, check=True)
(ROOT / ".migration/prepare.py").write_bytes(
    subprocess.check_output(["git", "show", f"{BASE}:.migration/prepare.py"], cwd=ROOT)
)
print("Prepared endpoint short-cycle extraction and restored migration helper.")
