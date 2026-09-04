#!/usr/bin/env python3
"""Two-isolated-directory byte replay for HCS-C359."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "code/c359_pais_uhlenbeck_producer.py"
EVIDENCE = ROOT / "results/c359_pais_uhlenbeck_evidence.json"


def main():
    if sys.flags.optimize:
        raise RuntimeError("C359 replay refuses optimized Python")
    blobs = []
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix="c359-replay-") as directory:
            target = Path(directory) / "evidence.json"
            subprocess.run([sys.executable, "-B", str(BUILDER), "--output", str(target)], check=True, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            blobs.append(target.read_bytes())
    if blobs[0] != blobs[1] or blobs[0] != EVIDENCE.read_bytes():
        raise AssertionError("C359 byte replay mismatch")
    print(f"C359 byte replay: PASS ({len(blobs[0])} bytes, two isolated directories)")


if __name__ == "__main__":
    main()
