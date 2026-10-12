#!/usr/bin/env python3
"""Prepare the global endpoint Poisson mechanical extraction."""
from pathlib import Path
import json
import os
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = "12015e922048f0eea543427d396bdc1db18ea7fc"
CONFIG = ROOT / ".migration" / "global-config.json"

request = json.loads((ROOT / ".migration/request.json").read_text())
expected = {"stage":"integration","task":"global-endpoint-poisson-extraction","baseline_commit":BASE}
if request != expected:
    raise ValueError("Unexpected global endpoint extraction request")
if not os.environ.get("GITHUB_REF_NAME", "").startswith("migration/"):
    raise SystemExit("Extraction requires a migration branch")
subprocess.run(["python3", "scripts/extract_monolith_section.py", str(CONFIG)], cwd=ROOT, check=True)
CONFIG.unlink()
subprocess.run(["git", "fetch", "--no-tags", "--depth=1", "origin", BASE], cwd=ROOT, check=True)
(ROOT / ".migration/prepare.py").write_bytes(
    subprocess.check_output(["git", "show", f"{BASE}:.migration/prepare.py"], cwd=ROOT)
)
print("Prepared global endpoint Poisson extraction and restored migration helper.")
