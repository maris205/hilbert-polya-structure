#!/usr/bin/env python3
"""Canonical-byte replay for C117."""
from __future__ import annotations

from hashlib import sha256
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c117_markov_evidence.json"
before = EVIDENCE.read_bytes()
subprocess.run([sys.executable, str(ROOT / "code/c117_markov_producer.py")], check=True,
               stdout=subprocess.DEVNULL)
after = EVIDENCE.read_bytes()
assert before == after
print("C117_REPLAY_PASS", sha256(after).hexdigest())
