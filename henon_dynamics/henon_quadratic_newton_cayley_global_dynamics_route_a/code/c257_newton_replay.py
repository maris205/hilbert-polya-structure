#!/usr/bin/env python3
"""Clean-process byte replay for HCS-C257."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "results/c257_newton_cayley_evidence.json"
PRODUCER = ROOT / "code/c257_newton_producer.py"


def main() -> None:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory(prefix="c257-newton-replay-") as td:
        out = Path(td) / "evidence.json"
        proc = subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(out)], env=env, capture_output=True, text=True, check=True)
        if "C257_PRODUCER_PASS" not in proc.stdout:
            raise AssertionError("producer status missing")
        if out.read_bytes() != CANONICAL.read_bytes():
            raise AssertionError("canonical evidence is not byte-reproducible")
    print("C257 byte replay: PASS")


if __name__ == "__main__":
    main()
