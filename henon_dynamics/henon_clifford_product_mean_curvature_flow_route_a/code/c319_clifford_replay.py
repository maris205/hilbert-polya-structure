#!/usr/bin/env python3
"""Byte-for-byte evidence replay for HCS-C319."""
import subprocess, sys, tempfile
from pathlib import Path

if sys.flags.optimize:
    raise RuntimeError("C319 replay refuses optimized Python")
root = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix="c319-replay-") as tmp:
    out = Path(tmp) / "evidence.json"
    run = subprocess.run([sys.executable, "-B", str(root / "code/c319_clifford_producer.py"), "--output", str(out)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if run.returncode or out.read_bytes() != (root / "results/c319_clifford_evidence.json").read_bytes():
        raise AssertionError(run.stdout)
print("C319 byte replay: PASS")
