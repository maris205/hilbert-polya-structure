#!/usr/bin/env python3
"""Byte-for-byte replay gate for HCS-C317 evidence."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c317_newton_schulz_evidence.json"
PRODUCER = ROOT / "code/c317_newton_schulz_producer.py"


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C317 replay refuses optimized Python")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c317-replay-") as tmp:
        target = Path(tmp) / "evidence.json"
        run = subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(target)],
                             env=env, check=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, text=True)
        if "C317_PRODUCER_PASS" not in run.stdout:
            raise AssertionError("producer sentinel missing")
        if target.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("producer byte replay mismatch")
    sha = hashlib.sha256(EVIDENCE.read_bytes()).hexdigest()
    print(f"C317 byte replay: PASS ({sha})")


if __name__ == "__main__":
    main()
