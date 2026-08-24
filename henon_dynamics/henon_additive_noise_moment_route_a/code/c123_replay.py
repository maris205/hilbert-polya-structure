#!/usr/bin/env python3
"""Replay C123 evidence generation in an isolated temporary path."""
from hashlib import sha256
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
canonical = ROOT / "results" / "c123_noise_evidence.json"
with tempfile.TemporaryDirectory(prefix="c123-replay-") as td:
    out = Path(td) / "evidence.json"
    subprocess.run([sys.executable, str(ROOT / "code" / "c123_noise_producer.py"), "--output", str(out)], check=True, stdout=subprocess.DEVNULL)
    if out.read_bytes() != canonical.read_bytes():
        raise SystemExit("C123_REPLAY_FAIL")
print("C123_REPLAY_PASS", sha256(canonical.read_bytes()).hexdigest())
