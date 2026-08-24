#!/usr/bin/env python3
"""Replay the producer in isolation and compare canonical bytes."""
import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
canonical = ROOT / "results" / "c122_adaptive_evidence.json"
with tempfile.TemporaryDirectory(prefix="c122-replay-") as td:
    out = Path(td) / "evidence.json"
    subprocess.run([sys.executable, str(ROOT / "code" / "c122_adaptive_producer.py"), "--output", str(out)], check=True, stdout=subprocess.DEVNULL)
    if out.read_bytes() != canonical.read_bytes():
        raise SystemExit("C122_REPLAY_FAIL")
print("C122_REPLAY_PASS", hashlib.sha256(canonical.read_bytes()).hexdigest())
