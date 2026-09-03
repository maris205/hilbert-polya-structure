#!/usr/bin/env python3
"""Byte-for-byte replay for HCS-C323 evidence."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c323_quantum_search_producer.py"
EVIDENCE = ROOT / "results/c323_quantum_search_evidence.json"


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C323 replay refuses optimized Python")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c323-replay-") as directory:
        first = Path(directory) / "first.json"
        second = Path(directory) / "second.json"
        for target in (first, second):
            output = subprocess.check_output(
                [sys.executable, "-B", str(PRODUCER), "--output", str(target)],
                env=env,
                text=True,
            )
            if "C323_PRODUCER_PASS" not in output:
                raise AssertionError("producer sentinel absent")
        if first.read_bytes() != second.read_bytes():
            raise AssertionError("fresh evidence runs differ")
        if first.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("checked-in evidence is stale")
        digest = hashlib.sha256(first.read_bytes()).hexdigest()
        print(f"C323 byte replay: PASS ({digest})")


if __name__ == "__main__":
    main()
