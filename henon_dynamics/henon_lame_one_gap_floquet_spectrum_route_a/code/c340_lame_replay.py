#!/usr/bin/env python3
"""Two-isolated-directory byte replay for HCS-C340."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c340_lame_producer.py"
EXPECTED = ROOT / "results/c340_lame_evidence.json"


def main():
    if sys.flags.optimize:
        raise RuntimeError("C340 replay lane refuses optimized Python")
    outputs = []
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for label in ("left", "right"):
        with tempfile.TemporaryDirectory(prefix=f"c340-replay-{label}-") as directory:
            target = Path(directory) / "evidence.json"
            subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(target)],
                           check=True, env=environment, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT, text=True)
            outputs.append(target.read_bytes())
    if outputs[0] != outputs[1] or outputs[0] != EXPECTED.read_bytes():
        raise AssertionError("isolated producer bytes differ or checked-in evidence is stale")
    print(f"C340 byte replay: PASS {len(outputs[0])} bytes")


if __name__ == "__main__":
    main()
