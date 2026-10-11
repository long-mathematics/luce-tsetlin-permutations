#!/usr/bin/env python3
"""Rebuild snapshots after the audited regular-profile clarification repair."""
from pathlib import Path
import hashlib, json, os, subprocess

ROOT=Path(__file__).resolve().parents[1]
PARENT="b2f6192a595a6632f0ad2e71813738a633cf5a82"
BASE_BRANCH="migration/regular-profile-extraction"
BASE_HEAD="1f40456f23e2eba20561539637f286ed490ff688"

request=json.loads((ROOT/".migration/request.json").read_text())
expected={"stage":"integration","task":"regular-profile-repair-snapshot","baseline_commit":PARENT}
if request != expected:
    raise ValueError("Unexpected repair snapshot request")
if not os.environ.get("GITHUB_REF_NAME","").startswith("migration/"):
    raise SystemExit("Snapshot preparation requires migration branch")
headers=subprocess.check_output(["git","cat-file","-p","HEAD"],cwd=ROOT,text=True).split("\n\n",1)[0].splitlines()
if "parent "+PARENT not in headers:
    raise ValueError("Snapshot request must directly follow repaired source head")

manifest=json.loads((ROOT/"archive/manifest.json").read_text())["files"]
for rec in manifest:
    p=ROOT/rec["path"]
    got=hashlib.sha256(p.read_bytes()).hexdigest()
    if got != rec["sha256"]:
        raise ValueError("Frozen archive changed: "+rec["path"])

subprocess.run(["git","fetch","--no-tags","--depth=1","origin",BASE_BRANCH],cwd=ROOT,check=True)
head=subprocess.check_output(["git","rev-parse","FETCH_HEAD"],cwd=ROOT,text=True).strip()
if head != BASE_HEAD:
    raise ValueError("Unexpected audited extraction branch head")
baseline=subprocess.check_output(["git","show","FETCH_HEAD:.migration/prepare.py"],cwd=ROOT)
(ROOT/".migration/prepare.py").write_bytes(baseline)
print("Regular-profile repair verified; frozen archive unchanged; rebuilding deterministic snapshots.")
