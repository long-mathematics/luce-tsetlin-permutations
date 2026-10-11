#!/usr/bin/env python3
"""Run the explicitly registered finite checks, never claim formal verification."""
import json
from pathlib import Path
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[1]
(ROOT/'.build/verification').mkdir(parents=True, exist_ok=True)
config = ROOT/'verification.json'
checks = json.loads(config.read_text())['checks'] if config.exists() else []
for check in checks:
    command = [sys.executable, str(ROOT/check['script']), *check.get('args', [])]
    print('Checking '+check['script'], flush=True)
    subprocess.run(command, cwd=ROOT, check=True, timeout=300)
print(f'Completed {len(checks)} registered finite consistency programs; no formal proof claim.')
