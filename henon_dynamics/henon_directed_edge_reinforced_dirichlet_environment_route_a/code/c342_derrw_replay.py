#!/usr/bin/env python3
"""Two-directory isolated byte replay for HCS-C342."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c342_derrw_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C342/2026-09-03.yaml"
PRODUCER = ROOT / "code/c342_derrw_producer.py"
CHECKER = ROOT / "code/c342_derrw_checker.py"


def main():
    if sys.flags.optimize:
        raise RuntimeError("C342 replay refuses optimized Python")
    original = EVIDENCE.read_bytes()
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    outputs = []
    for index in range(2):
        with tempfile.TemporaryDirectory(prefix=f"c342-replay-{index}-") as directory:
            output = Path(directory) / "evidence.json"
            subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(output),
                            "--evaluation", str(EVALUATION)], env=environment, check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            outputs.append(output.read_bytes())
            checked = subprocess.run([sys.executable, "-B", str(CHECKER),
                "--evidence", str(output), "--evaluation", str(EVALUATION)],
                env=environment, check=True, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, text=True)
            if "C342 independent DERRW checker: PASS" not in checked.stdout:
                raise AssertionError("checker sentinel absent")
    if outputs[0] != outputs[1] or outputs[0] != original:
        raise AssertionError("isolated producer bytes differ")
    if EVIDENCE.read_bytes() != original:
        raise AssertionError("checked evidence changed")
    print(f"C342 byte replay: PASS 2 directories {len(original)} bytes "
          f"sha256={hashlib.sha256(original).hexdigest()}")


if __name__ == "__main__":
    main()
