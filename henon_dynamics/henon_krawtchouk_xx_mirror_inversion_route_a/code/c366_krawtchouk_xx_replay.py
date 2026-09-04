#!/usr/bin/env python3
"""Isolated byte replay for HCS-C366."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c366_krawtchouk_xx_producer.py"
EVIDENCE = ROOT / "results/c366_krawtchouk_xx_evidence.json"


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C366 replay refuses optimized Python")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    blobs = []
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix="c366-replay-") as directory:
            output = Path(directory) / "evidence.json"
            subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(output)],
                           check=True, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            assert not list(Path(directory).rglob("__pycache__"))
            blobs.append(output.read_bytes())
    assert blobs[0] == blobs[1] == EVIDENCE.read_bytes()
    print(f"C366 byte replay: PASS ({len(blobs[0])} bytes)")


if __name__ == "__main__":
    main()
