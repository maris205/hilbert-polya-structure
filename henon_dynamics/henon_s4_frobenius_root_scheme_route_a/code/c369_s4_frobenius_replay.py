#!/usr/bin/env python3
"""Isolated byte replay for HCS-C369."""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c369_s4_frobenius_producer.py"
EVIDENCE = ROOT / "results/c369_s4_frobenius_evidence.json"


def main():
    if sys.flags.optimize:
        raise RuntimeError("C369 replay refuses optimized Python")
    receipts = []
    with tempfile.TemporaryDirectory(prefix="c369-replay-") as directory:
        base = Path(directory)
        for index in range(2):
            path = base / f"evidence-{index}.json"
            output = subprocess.check_output([sys.executable, "-B", str(PRODUCER), "--output", str(path)], text=True)
            if "C369_PRODUCER_PASS" not in output:
                raise AssertionError("producer sentinel absent")
            receipts.append(path.read_bytes())
    if receipts[0] != receipts[1] or receipts[0] != EVIDENCE.read_bytes():
        raise AssertionError("nonidentical isolated evidence replay")
    print(f"C369 byte replay: PASS ({len(receipts[0])} bytes, two isolated runs)")


if __name__ == "__main__":
    main()
