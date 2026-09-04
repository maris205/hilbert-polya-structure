#!/usr/bin/env python3
"""Byte-for-byte isolated replay for HCS-C375."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

if sys.flags.optimize:
    raise RuntimeError("C375 replay refuses optimized Python")

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c375_lps_nonbacktracking_producer.py"
STORED = ROOT / "results/c375_lps_nonbacktracking_evidence.json"


def build(directory: str) -> bytes:
    output = Path(directory) / "evidence.json"
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    process = subprocess.run(
        [sys.executable, "-B", str(PRODUCER), "--output", str(output)],
        env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )
    if process.returncode or "C375_PRODUCER_PASS" not in process.stdout:
        raise AssertionError(process.stdout)
    return output.read_bytes()


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c375-replay-a-") as first_dir:
        first = build(first_dir)
    with tempfile.TemporaryDirectory(prefix="c375-replay-b-") as second_dir:
        second = build(second_dir)
    stored = STORED.read_bytes()
    if first != second or first != stored:
        raise AssertionError("isolated producer bytes disagree")
    print(f"C375 byte replay: PASS {hashlib.sha256(stored).hexdigest()}")


if __name__ == "__main__":
    main()
