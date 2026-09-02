#!/usr/bin/env python3
"""Byte-for-byte deterministic replay for HCS-C318 evidence."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c318_ssh_producer.py"
EVIDENCE = ROOT / "results/c318_ssh_evidence.json"


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C318 replay refuses optimized Python")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c318-replay-") as directory:
        first = Path(directory) / "first.json"
        second = Path(directory) / "second.json"
        for target in (first, second):
            output = subprocess.check_output(
                [sys.executable, "-B", str(PRODUCER), "--output", str(target)], env=env, text=True
            )
            if "C318_PRODUCER_PASS" not in output:
                raise AssertionError("producer sentinel missing")
        if first.read_bytes() != second.read_bytes():
            raise AssertionError("two fresh evidence runs differ")
        if first.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("checked-in evidence is stale")
        digest = hashlib.sha256(first.read_bytes()).hexdigest()
        print(f"C318 byte replay: PASS ({digest})")


if __name__ == "__main__":
    main()
