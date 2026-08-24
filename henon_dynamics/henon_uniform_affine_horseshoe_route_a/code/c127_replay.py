#!/usr/bin/env python3
"""Byte-for-byte replay of the C127 producer."""
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "results" / "c127_uniform_horseshoe_evidence.json"
PRODUCER = ROOT / "code" / "c127_uniform_horseshoe_producer.py"

with tempfile.TemporaryDirectory() as tmp:
    out = Path(tmp) / "evidence.json"
    subprocess.run([sys.executable, str(PRODUCER), "--output", str(out)], check=True, stdout=subprocess.DEVNULL)
    assert out.read_bytes() == EXPECTED.read_bytes()
print("C127 deterministic replay: PASS")
