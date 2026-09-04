#!/usr/bin/env python3
"""Isolated two-copy byte replay for HCS-C358."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c358_may_leonard_producer.py"
CHECKER = ROOT / "code/c358_may_leonard_checker.py"
EVALUATION = ROOT / "evaluations/route_a/HCS-C358/2026-09-03.yaml"


def main():
    if sys.flags.optimize:
        raise RuntimeError("C358 replay refuses optimized Python")
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c358-replay-a-") as first, \
         tempfile.TemporaryDirectory(prefix="c358-replay-b-") as second:
        outputs = [Path(first)/"evidence.json", Path(second)/"evidence.json"]
        for output in outputs:
            subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(output),
                            "--evaluation", str(EVALUATION)], check=True, env=environment,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(output),
                            "--evaluation", str(EVALUATION)], check=True, env=environment,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if outputs[0].read_bytes() != outputs[1].read_bytes():
            raise AssertionError("isolated producer bytes differ")
    print("C358 byte replay: PASS 2 isolated copies")


if __name__ == "__main__":
    main()
