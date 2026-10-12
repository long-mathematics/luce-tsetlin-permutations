#!/usr/bin/env python3
"""Prepare the Sukhatme fixed-point mechanical extraction."""
from pathlib import Path
import json
import os
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = "edf8983fbbb0515361022b303e54df045b54aaff"
CONFIG = ROOT / ".migration" / "sukhatme-config.json"

request = json.loads((ROOT / ".migration/request.json").read_text())
expected = {"stage":"integration","task":"sukhatme-fixed-points-extraction","baseline_commit":BASE}
if request != expected:
    raise ValueError("Unexpected Sukhatme extraction request")
if not os.environ.get("GITHUB_REF_NAME", "").startswith("migration/"):
    raise SystemExit("Extraction requires a migration branch")
subprocess.run(["python3", "scripts/extract_monolith_section.py", str(CONFIG)], cwd=ROOT, check=True)
CONFIG.unlink()
subprocess.run(["git", "fetch", "--no-tags", "--depth=1", "origin", "main"], cwd=ROOT, check=True)
head = subprocess.check_output(["git", "rev-parse", "FETCH_HEAD"], cwd=ROOT, text=True).strip()
if head != BASE:
    raise ValueError("Unexpected main head while restoring migration helper")
(ROOT / ".migration/prepare.py").write_bytes(
    subprocess.check_output(["git", "show", "FETCH_HEAD:.migration/prepare.py"], cwd=ROOT)
)
print("Prepared Sukhatme fixed-point extraction and restored migration helper.")
