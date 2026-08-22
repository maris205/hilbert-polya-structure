#!/usr/bin/env python3
"""Replay producer output and check byte stability."""
from __future__ import annotations
import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c105_kneading_evidence.json"
before = hashlib.sha256(EVIDENCE.read_bytes()).hexdigest()
subprocess.run([sys.executable, str(ROOT / "code/c105_kneading_producer.py")], check=True, capture_output=True, text=True)
after = hashlib.sha256(EVIDENCE.read_bytes()).hexdigest()
assert before == after, (before, after)
print("C105_REPLAY_PASS", after)
