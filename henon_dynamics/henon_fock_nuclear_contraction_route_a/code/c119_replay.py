#!/usr/bin/env python3
"""Canonical byte replay for C119 evidence."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "results/c119_fock_evidence.json"
raw = source.read_bytes()
data = json.loads(raw)
canonical = (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()
assert raw == canonical
with tempfile.TemporaryDirectory() as tmp:
    replay = Path(tmp) / "evidence.json"
    subprocess.run([sys.executable, str(ROOT / "code/c119_fock_producer.py"), str(replay)], check=True, capture_output=True, text=True)
    assert replay.read_bytes() == raw
print("C119_REPLAY_PASS", sha256(raw).hexdigest())
