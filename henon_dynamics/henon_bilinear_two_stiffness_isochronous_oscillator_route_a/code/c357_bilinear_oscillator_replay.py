#!/usr/bin/env python3
"""Two-directory byte replay for HCS-C357."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT/"code/c357_bilinear_oscillator_producer.py"
EVIDENCE = ROOT/"results/c357_bilinear_oscillator_evidence.json"


def main():
    if sys.flags.optimize:
        raise RuntimeError("C357 replay refuses optimized Python")
    blobs = []; env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix="c357-replay-") as directory:
            output = Path(directory)/"evidence.json"
            subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(output)], check=True, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            blobs.append(output.read_bytes())
    if blobs[0] != blobs[1] or blobs[0] != EVIDENCE.read_bytes():
        raise AssertionError("C357 byte replay mismatch")
    print(f"C357 byte replay: PASS ({len(blobs[0])} bytes, two isolated directories)")


if __name__ == "__main__":
    main()
