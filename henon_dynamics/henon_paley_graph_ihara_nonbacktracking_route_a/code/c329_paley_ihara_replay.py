#!/usr/bin/env python3
"""Isolated byte replay for HCS-C329 evidence."""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c329_paley_ihara_producer.py"
EVALUATION = ROOT / "evaluations/route_a/HCS-C329/2026-09-03.yaml"
EVIDENCE = ROOT / "results/c329_paley_ihara_evidence.json"


def main():
    if sys.flags.optimize:
        raise RuntimeError("C329 replay refuses optimized Python")
    with tempfile.TemporaryDirectory(prefix="c329-replay-") as directory:
        root = Path(directory)
        producer = root / "producer.py"
        evaluation = root / "evaluation.yaml"
        output = root / "evidence.json"
        shutil.copy2(PRODUCER, producer)
        shutil.copy2(EVALUATION, evaluation)
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
        subprocess.run([sys.executable, "-B", str(producer), "--output", str(output),
                        "--evaluation", str(evaluation)], check=True, env=env,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if output.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("isolated replay differs")
    print(f"C329 byte replay: PASS ({len(EVIDENCE.read_bytes())} bytes identical)")


if __name__ == "__main__":
    main()
