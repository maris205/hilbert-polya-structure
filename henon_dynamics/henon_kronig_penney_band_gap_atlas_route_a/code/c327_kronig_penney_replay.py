#!/usr/bin/env python3
"""Isolated byte-for-byte replay for HCS-C327 evidence."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c327_kronig_penney_producer.py"
EVIDENCE = ROOT / "results/c327_kronig_penney_evidence.json"


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C327 replay refuses optimized Python")
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c327-replay-") as directory:
        first = Path(directory) / "first.json"
        second = Path(directory) / "second.json"
        for target in (first, second):
            output = subprocess.check_output(
                [sys.executable, "-B", str(PRODUCER), "--output", str(target)],
                env=environment, text=True,
            )
            if "C327_PRODUCER_PASS" not in output:
                raise AssertionError("producer sentinel absent")
        if first.read_bytes() != second.read_bytes():
            raise AssertionError("isolated evidence runs differ")
        if first.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("checked-in evidence is stale")
        print(f"C327 byte replay: PASS ({hashlib.sha256(first.read_bytes()).hexdigest()})")


if __name__ == "__main__":
    main()
