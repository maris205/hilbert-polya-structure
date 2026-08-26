#!/usr/bin/env python3
"""Byte-replay the deterministic HCS-C184 producer."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c184_spectral_decimation_producer.py"
EVIDENCE = ROOT / "results/c184_spectral_decimation_evidence.json"


with tempfile.TemporaryDirectory(prefix="c184-replay-") as temporary:
    target = Path(temporary) / "evidence.json"
    subprocess.run([sys.executable, str(PRODUCER), "--output", str(target)], check=True, capture_output=True, text=True)
    expected = EVIDENCE.read_bytes()
    got = target.read_bytes()
    if got != expected:
        raise AssertionError("C184 byte replay differs")
print(json.dumps({"status": "C184_REPLAY_PASS", "bytes": len(expected), "sha256": sha256(expected).hexdigest()}, sort_keys=True))
