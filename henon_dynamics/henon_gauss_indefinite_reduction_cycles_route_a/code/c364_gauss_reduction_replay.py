#!/usr/bin/env python3
"""Isolated two-directory byte replay for HCS-C364."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c364_gauss_reduction_producer.py"
CHECKER = ROOT / "code/c364_gauss_reduction_checker.py"
EVALUATION = ROOT / "evaluations/route_a/HCS-C364/2026-09-04.yaml"
CHECKED = ROOT / "results/c364_gauss_reduction_evidence.json"


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C364 replay refuses optimized Python")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    blobs = []
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix="c364-byte-replay-") as directory:
            output = Path(directory) / "evidence.json"
            produced = subprocess.check_output([sys.executable, "-B", str(PRODUCER), "--output", str(output)], cwd=directory, env=env, text=True)
            if "C364_PRODUCER_PASS" not in produced:
                raise AssertionError("producer sentinel missing")
            checked = subprocess.check_output([sys.executable, "-B", str(CHECKER), "--evidence", str(output), "--evaluation", str(EVALUATION)], cwd=directory, env=env, text=True)
            if "C364 independent Gauss-reduction checker: PASS" not in checked:
                raise AssertionError("checker sentinel missing")
            blobs.append(output.read_bytes())
    if blobs[0] != blobs[1] or blobs[0] != CHECKED.read_bytes():
        raise AssertionError("isolated evidence bytes differ")
    print(f"C364 byte replay: PASS ({len(blobs[0])} bytes, two isolated directories)")


if __name__ == "__main__":
    main()
