#!/usr/bin/env python3
"""Byte-replay the deterministic HCS-C190 producer."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c190_bulgarian_necklace_producer.py"
EVIDENCE = ROOT / "results/c190_bulgarian_necklace_evidence.json"


with tempfile.TemporaryDirectory(prefix="c190-replay-") as temporary:
    target = Path(temporary) / "evidence.json"
    subprocess.run(
        [sys.executable, str(PRODUCER), "--output", str(target)],
        check=True,
        capture_output=True,
        text=True,
    )
    expected = EVIDENCE.read_bytes()
    obtained = target.read_bytes()
    if obtained != expected:
        raise AssertionError("byte replay differs")

print(json.dumps({
    "status": "C190_REPLAY_PASS",
    "bytes": len(expected),
    "sha256": sha256(expected).hexdigest(),
}, sort_keys=True))
