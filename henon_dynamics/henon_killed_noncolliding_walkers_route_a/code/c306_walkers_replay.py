#!/usr/bin/env python3
"""Isolated two-run byte replay for HCS-C306 evidence."""
from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c306_walkers_producer.py"
ARCHIVE = ROOT / "results/c306_walkers_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c306-replay-") as folder:
        first = Path(folder) / "first.json"
        second = Path(folder) / "second.json"
        for path in (first, second):
            result = subprocess.run([sys.executable, str(PRODUCER), "--output", str(path)],
                                    cwd=folder, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if result.returncode:
                raise RuntimeError(result.stdout)
        if first.read_bytes() != second.read_bytes():
            raise AssertionError("two isolated producer runs differ")
        if first.read_bytes() != ARCHIVE.read_bytes():
            raise AssertionError("isolated replay differs from archived evidence")
    print("C306 deterministic replay PASS (two isolated fresh runs and archive are byte-identical)")
    print("evidence_sha256=" + hashlib.sha256(ARCHIVE.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
