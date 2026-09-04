#!/usr/bin/env python3
"""Isolated byte replay for HCS-C377."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c377 replay refuses optimized Python")

import argparse
import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c377_periodic_clm_producer.py"
EVIDENCE = ROOT / "results/c377_periodic_clm_evidence.json"


def main():
    argparse.ArgumentParser().parse_args()
    with tempfile.TemporaryDirectory(prefix="c377-replay-") as directory:
        output = Path(directory) / "evidence.json"
        process = subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(output)], capture_output=True, text=True)
        assert process.returncode == 0, process.stdout + process.stderr
        actual, expected = output.read_bytes(), EVIDENCE.read_bytes()
        assert actual == expected
        print("C377 replay PASS: bytes=" + str(len(actual)) + " sha256=" + hashlib.sha256(actual).hexdigest())


if __name__ == "__main__":
    main()
