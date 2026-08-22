#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
evidence = ROOT / "results/c107_open_hole_evidence.json"
before = hashlib.sha256(evidence.read_bytes()).hexdigest()
subprocess.run([sys.executable, str(ROOT / "code/c107_open_hole_producer.py")], check=True, capture_output=True, text=True)
after = hashlib.sha256(evidence.read_bytes()).hexdigest()
assert before == after
print("C107_REPLAY_PASS", after)
