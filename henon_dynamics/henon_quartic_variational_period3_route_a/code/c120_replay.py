#!/usr/bin/env python3
"""Require byte-identical regeneration of the canonical C120 evidence."""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c120_variational_period3_evidence.json"
before = EVIDENCE.read_bytes()
subprocess.run([sys.executable, str(ROOT / "code/c120_variational_period3_producer.py")], check=True, stdout=subprocess.DEVNULL)
after = EVIDENCE.read_bytes()
assert before == after
print("C120_REPLAY_PASS", sha256(after).hexdigest())
