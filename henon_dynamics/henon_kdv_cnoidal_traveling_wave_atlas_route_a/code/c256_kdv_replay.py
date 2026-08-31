#!/usr/bin/env python3
"""Clean-process byte replay for C256 canonical evidence."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "results/c256_kdv_evidence.json"
PRODUCER = ROOT / "code/c256_kdv_producer.py"


def main() -> None:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory(prefix="c256-kdv-replay-") as td:
        out = Path(td) / "evidence.json"
        proc = subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(out)], env=env, text=True, capture_output=True, check=True)
        if "C256_PRODUCER_PASS" not in proc.stdout:
            raise AssertionError("producer status missing")
        if out.read_bytes() != CANONICAL.read_bytes():
            raise AssertionError("canonical evidence is not byte-reproducible")
    print("C256 byte replay: PASS")


if __name__ == "__main__":
    main()
