#!/usr/bin/env python3
"""Isolated deterministic byte replay for HCS-C326."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c326_two_site_inclusion_producer.py"
CHECKER = ROOT / "code/c326_two_site_inclusion_checker.py"
EVIDENCE = ROOT / "results/c326_two_site_inclusion_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C326/2026-09-03.yaml"


def main():
    if sys.flags.optimize:
        raise RuntimeError("C326 replay refuses optimized Python")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c326-replay-") as directory:
        output = Path(directory) / "evidence.json"
        produced = subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(output)],
                                  env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if produced.returncode or output.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("producer byte replay")
        checked = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(output),
                                  "--evaluation", str(EVALUATION)], env=env,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if checked.returncode or "C326 independent checker: PASS" not in checked.stdout:
            raise AssertionError("isolated checker")
    print(f"C326 byte replay: PASS ({hashlib.sha256(EVIDENCE.read_bytes()).hexdigest()})")


if __name__ == "__main__":
    main()
