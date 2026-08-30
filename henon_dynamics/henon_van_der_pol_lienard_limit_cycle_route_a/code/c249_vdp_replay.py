#!/usr/bin/env python3
"""Clean-process byte replay for the C249 canonical evidence."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "results/c249_vdp_evidence.json"
PRODUCER = ROOT / "code/c249_vdp_producer.py"


def main() -> None:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory(prefix="c249-replay-") as td:
        out = Path(td) / "evidence.json"
        proc = subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(out)], env=env, text=True, capture_output=True, check=True)
        if "C249_PRODUCER_PASS" not in proc.stdout:
            raise AssertionError("producer status missing")
        if out.read_bytes() != CANONICAL.read_bytes():
            raise AssertionError("canonical evidence is not byte-reproducible")
    print("C249 byte replay: PASS")


if __name__ == "__main__":
    main()
