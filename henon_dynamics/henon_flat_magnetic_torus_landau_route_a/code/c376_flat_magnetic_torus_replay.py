#!/usr/bin/env python3
"""Isolated byte-for-byte producer replay for HCS-C376."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c376 replay refuses optimized Python")

import argparse
import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c376_flat_magnetic_torus_producer.py"
EVIDENCE = ROOT / "results/c376_flat_magnetic_torus_evidence.json"


def main():
    argparse.ArgumentParser().parse_args()
    with tempfile.TemporaryDirectory(prefix="c376-replay-") as directory:
        output = Path(directory) / "evidence.json"
        process = subprocess.run(
            [sys.executable, "-B", str(PRODUCER), "--output", str(output)],
            capture_output=True, text=True,
        )
        assert process.returncode == 0, process.stdout + process.stderr
        expected = EVIDENCE.read_bytes()
        actual = output.read_bytes()
        assert actual == expected
        print(
            "C376 replay PASS: bytes=" + str(len(actual))
            + " sha256=" + hashlib.sha256(actual).hexdigest()
        )


if __name__ == "__main__":
    main()
