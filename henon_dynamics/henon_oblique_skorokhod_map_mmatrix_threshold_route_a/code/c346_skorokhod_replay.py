#!/usr/bin/env python3
"""Two isolated byte-identical evidence replays for HCS-C346."""
import subprocess
import sys
import tempfile
from pathlib import Path

if sys.flags.optimize:
    raise RuntimeError("C346 replay refuses optimized Python")
root = Path(__file__).resolve().parents[1]
producer = root / "code/c346_skorokhod_producer.py"
expected = (root / "results/c346_skorokhod_evidence.json").read_bytes()
copies = []
for index in range(2):
    with tempfile.TemporaryDirectory(prefix=f"c346-replay-{index}-") as directory:
        output = Path(directory) / "evidence.json"
        run = subprocess.run([sys.executable, "-B", str(producer), "--output", str(output)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if run.returncode:
            raise AssertionError(run.stdout)
        copies.append(output.read_bytes())
if copies[0] != copies[1] or copies[0] != expected:
    raise AssertionError("isolated evidence replay mismatch")
print("C346 byte replay: PASS (2 isolated reproductions)")
