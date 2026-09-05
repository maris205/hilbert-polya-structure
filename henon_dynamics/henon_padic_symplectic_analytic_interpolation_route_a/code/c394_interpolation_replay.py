#!/usr/bin/env python3
"""Two independent working directories; the same frozen producer source."""
if not __debug__:
    raise RuntimeError("c394 replay refuses optimized Python")
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]

def main():
    blobs = []
    with tempfile.TemporaryDirectory(prefix="c394-replay-one-") as one, tempfile.TemporaryDirectory(prefix="c394-replay-two-") as two:
        for directory in (one, two):
            target = Path(directory)/"evidence.json"
            p = subprocess.run([sys.executable, "-B", str(ROOT/"code/c394_interpolation_producer.py"), "--output", str(target)], cwd=directory, capture_output=True, text=True)
            assert p.returncode == 0, p.stdout+p.stderr
            blobs.append(target.read_bytes())
    assert blobs[0] == blobs[1] == (ROOT/"results/c394_interpolation_evidence.json").read_bytes()
    print("C394 two-directory byte replay PASS: sha256="+hashlib.sha256(blobs[0]).hexdigest())

if __name__ == "__main__":
    main()
