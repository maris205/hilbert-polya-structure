#!/usr/bin/env python3
"""Isolated byte-for-byte replay for the HCS-C304 evidence producer."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c304_ch_producer.py"
EVIDENCE = ROOT / "results/c304_ch_evidence.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c304-replay-") as temporary:
        first = Path(temporary) / "first.json"
        second = Path(temporary) / "second.json"
        for target in (first, second):
            completed = subprocess.run(
                [sys.executable, "-B", str(PRODUCER), "--output", str(target)],
                env=env,
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            if "C304_PRODUCER_PASS" not in completed.stdout:
                raise AssertionError("producer sentinel absent")
        if first.read_bytes() != second.read_bytes() or first.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("isolated replay differs from archived evidence")
        print(f"C304 byte replay: PASS ({digest(first)})")


if __name__ == "__main__":
    main()
