#!/usr/bin/env python3
"""Two isolated byte-identical evidence builds for HCS-C372."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("C372 replay refuses optimized Python")

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c372_kirchhoff_love_producer.py"
EVIDENCE = ROOT / "results/c372_kirchhoff_love_evidence.json"


def main():
    outputs = []
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c372-replay-") as directory:
        base = Path(directory)
        for index in range(2):
            path = base / f"evidence-{index}.json"
            result = subprocess.check_output([sys.executable, "-B", str(PRODUCER), "--output", str(path)], env=env, text=True)
            if "C372_PRODUCER_PASS" not in result:
                raise AssertionError("producer sentinel")
            outputs.append(path.read_bytes())
    if outputs[0] != outputs[1] or outputs[0] != EVIDENCE.read_bytes():
        raise AssertionError("isolated replay mismatch")
    print(f"C372 byte replay: PASS ({len(outputs[0])} bytes, two isolated runs)")


if __name__ == "__main__":
    main()
