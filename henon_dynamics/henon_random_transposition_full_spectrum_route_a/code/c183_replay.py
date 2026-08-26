#!/usr/bin/env python3
"""Byte-replay the deterministic HCS-C183 producer."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c183_random_transposition_producer.py"
EVIDENCE = ROOT / "results/c183_random_transposition_evidence.json"

with tempfile.TemporaryDirectory(prefix="c183-replay-") as tmp:
    target = Path(tmp) / "evidence.json"
    subprocess.run([sys.executable, str(PRODUCER), "--output", str(target)], check=True, capture_output=True, text=True)
    expected, got = EVIDENCE.read_bytes(), target.read_bytes()
    if got != expected:
        raise AssertionError("byte replay differs")
print(json.dumps({"status": "C183_REPLAY_PASS", "bytes": len(expected), "sha256": sha256(expected).hexdigest()}, sort_keys=True))
