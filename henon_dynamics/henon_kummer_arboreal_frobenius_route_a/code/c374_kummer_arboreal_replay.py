#!/usr/bin/env python3
"""Two-isolated-directory byte replay for HCS-C374 evidence."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c374_kummer_arboreal_producer.py"
CANONICAL = ROOT / "results/c374_kummer_arboreal_evidence.json"


def build(directory: str) -> bytes:
    output = Path(directory) / "evidence.json"
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    subprocess.run(
        [sys.executable, "-B", str(PRODUCER), "--output", str(output)],
        env=env,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    return output.read_bytes()


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C374 replay refuses optimized Python")
    with tempfile.TemporaryDirectory(prefix="c374-replay-a-") as left, tempfile.TemporaryDirectory(prefix="c374-replay-b-") as right:
        first = build(left)
        second = build(right)
    if first != second:
        raise AssertionError("isolated producer builds differ")
    if first != CANONICAL.read_bytes():
        raise AssertionError("canonical evidence differs from isolated replay")
    print(f"C374 byte replay: PASS ({len(first)} bytes identical across two isolated builds)")


if __name__ == "__main__":
    main()
