#!/usr/bin/env python3
"""Two isolated byte replays for HCS-C324."""
import subprocess
import sys
import tempfile
from pathlib import Path

if sys.flags.optimize:
    raise RuntimeError("C324 replay refuses optimized Python")

root = Path(__file__).resolve().parents[1]
producer = root / "code/c324_hunter_saxton_producer.py"
expected = (root / "results/c324_hunter_saxton_evidence.json").read_bytes()
replays = []
for index in range(2):
    with tempfile.TemporaryDirectory(prefix=f"c324-replay-{index}-") as directory:
        output = Path(directory) / "evidence.json"
        run = subprocess.run([sys.executable, "-B", str(producer), "--output", str(output)],
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if run.returncode:
            raise AssertionError(run.stdout)
        replays.append(output.read_bytes())
if replays[0] != replays[1] or replays[0] != expected:
    raise AssertionError("isolated evidence replay mismatch")
print("C324 byte replay: PASS (2 isolated reproductions)")
