#!/usr/bin/env python3
"""Two-isolated-directory byte replay for HCS-C373."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c373 replay refuses optimized Python")

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c373_higgs_oscillator_producer.py"
EVIDENCE = ROOT / "results/c373_higgs_oscillator_evidence.json"


def main():
    argparse.ArgumentParser().parse_args()
    blobs = []
    for run_index in range(2):
        with tempfile.TemporaryDirectory(prefix=f"c373-replay-{run_index}-") as directory:
            output = Path(directory) / "evidence.json"
            process = subprocess.run(
                [sys.executable, "-B", str(PRODUCER), "--output", str(output)],
                capture_output=True, text=True,
            )
            assert process.returncode == 0, process.stdout + process.stderr
            blobs.append(output.read_bytes())
    assert blobs[0] == blobs[1] == EVIDENCE.read_bytes()
    print(f"C373 replay PASS: bytes={len(blobs[0])} isolated_runs=2")


if __name__ == "__main__":
    main()
