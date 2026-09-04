#!/usr/bin/env python3
"""Two-isolated-directory byte replay for HCS-C371 evidence."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "code/c371_harper_producer.py"
CHECKED = ROOT / "results/c371_harper_evidence.json"


def main():
    if sys.flags.optimize:
        raise RuntimeError("C371 replay refuses optimized Python")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    blobs = []
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix="c371-replay-") as directory:
            path = Path(directory) / "evidence.json"
            output = subprocess.check_output(
                [sys.executable, "-B", str(SCRIPT), "--output", str(path)],
                env=env,
                text=True,
            )
            if "C371_PRODUCER_PASS" not in output:
                raise AssertionError("producer sentinel missing")
            blobs.append(path.read_bytes())
    checked = CHECKED.read_bytes()
    if blobs[0] != blobs[1] or blobs[0] != checked:
        raise AssertionError("nonidentical evidence replay")
    print(f"C371 byte replay: PASS ({len(checked)} bytes, 2 isolated runs)")


if __name__ == "__main__":
    main()
