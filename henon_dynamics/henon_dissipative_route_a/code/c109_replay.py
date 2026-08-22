#!/usr/bin/env python3
"""Re-run the producer and require byte-identical evidence."""
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
evidence = PROJECT / "results/c109_dissipative_evidence.json"
before = hashlib.sha256(evidence.read_bytes()).hexdigest()
subprocess.run([sys.executable, str(PROJECT / "code/c109_dissipative_producer.py")], check=True, capture_output=True, text=True)
after = hashlib.sha256(evidence.read_bytes()).hexdigest()
assert before == after, (before, after)
print("C109_REPLAY_PASS", after)
