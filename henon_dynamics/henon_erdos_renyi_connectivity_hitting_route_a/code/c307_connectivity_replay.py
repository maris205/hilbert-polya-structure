#!/usr/bin/env python3
"""Isolated two-run byte replay for HCS-C307 evidence."""
from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c307_connectivity_producer.py"
ARCHIVE = ROOT / "results/c307_connectivity_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c307-replay-") as folder:
        first = Path(folder) / "first.json"
        second = Path(folder) / "second.json"
        for path in (first, second):
            result = subprocess.run([sys.executable, str(PRODUCER), "--output", str(path)], cwd=folder,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if result.returncode:
                raise RuntimeError(result.stdout)
        if first.read_bytes() != second.read_bytes():
            raise AssertionError("two isolated outputs differ")
        if first.read_bytes() != ARCHIVE.read_bytes():
            raise AssertionError("isolated output differs from archive")
    print("C307 deterministic replay PASS (two isolated fresh runs and archive are byte-identical)")
    print("evidence_sha256=" + hashlib.sha256(ARCHIVE.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
