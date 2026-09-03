#!/usr/bin/env python3
"""Isolated deterministic byte replay for HCS-C338."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c338_wilson_ust_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C338/2026-09-03.yaml"
PRODUCER = ROOT / "code/c338_wilson_ust_producer.py"
CHECKER = ROOT / "code/c338_wilson_ust_checker.py"


def main():
    if sys.flags.optimize:
        raise RuntimeError("C338 replay refuses optimized Python")
    original = EVIDENCE.read_bytes()
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c338-replay-") as directory:
        output = Path(directory) / "evidence.json"
        command = [sys.executable, "-B", str(PRODUCER), "--output", str(output),
                   "--evaluation", str(EVALUATION)]
        for _ in range(2):
            subprocess.run(command, env=environment, check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if output.read_bytes() != original:
                raise AssertionError("isolated producer bytes differ from checked evidence")
        checked = subprocess.run(
            [sys.executable, "-B", str(CHECKER), "--evidence", str(output),
             "--evaluation", str(EVALUATION)],
            env=environment, check=True, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, text=True,
        )
        if "C338 independent Wilson/UST checker: PASS" not in checked.stdout:
            raise AssertionError("isolated checker sentinel absent")
    if EVIDENCE.read_bytes() != original:
        raise AssertionError("checked evidence changed during replay")
    print(f"C338 byte replay: PASS {len(original)} bytes "
          f"sha256={hashlib.sha256(original).hexdigest()}")


if __name__ == "__main__":
    main()
