#!/usr/bin/env python3
"""Replay the C302 producer twice and compare it with the archive."""
from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c302_quicksort_producer.py"
ARCHIVE = ROOT / "results/c302_quicksort_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c302-replay-") as folder:
        first = Path(folder)/"first.json"; second = Path(folder)/"second.json"
        for path in (first,second):
            subprocess.run([sys.executable,str(PRODUCER),"--output",str(path)],check=True,
                           stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if first.read_bytes()!=second.read_bytes():
            raise AssertionError("two fresh producer outputs differ")
        if first.read_bytes()!=ARCHIVE.read_bytes():
            raise AssertionError("fresh output differs from archive")
    print("C302 deterministic replay PASS (two fresh runs and archived bytes identical)")
    print("evidence_sha256="+hashlib.sha256(ARCHIVE.read_bytes()).hexdigest())


if __name__=="__main__":
    main()
