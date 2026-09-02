#!/usr/bin/env python3
"""Replay the C301 producer twice and require byte identity with the archive."""
from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c301_fragmentation_producer.py"
ARCHIVE = ROOT / "results/c301_fragmentation_evidence.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c301-replay-") as folder:
        first = Path(folder) / "first.json"
        second = Path(folder) / "second.json"
        for target in (first, second):
            subprocess.run([sys.executable, str(PRODUCER), "--output", str(target)], check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if first.read_bytes() != second.read_bytes():
            raise AssertionError("two producer executions differ")
        if first.read_bytes() != ARCHIVE.read_bytes():
            raise AssertionError("replayed evidence differs from archived evidence")
    print("C301 deterministic replay PASS (two fresh runs and archived bytes identical)")
    print(f"evidence_sha256={digest(ARCHIVE)}")


if __name__ == "__main__":
    main()
