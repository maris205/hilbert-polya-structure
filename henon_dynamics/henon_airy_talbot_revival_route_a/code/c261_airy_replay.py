#!/usr/bin/env python3
"""Clean-process byte replay for C261 canonical evidence."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "results/c261_airy_evidence.json"
PRODUCER = ROOT / "code/c261_airy_producer.py"


def main() -> None:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory(prefix="c261-airy-replay-") as directory:
        output = Path(directory) / "evidence.json"
        proc = subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(output)], env=env, text=True, capture_output=True, check=True)
        if "C261_PRODUCER_PASS" not in proc.stdout:
            raise AssertionError("producer status missing")
        if output.read_bytes() != CANONICAL.read_bytes():
            raise AssertionError("canonical evidence is not byte-reproducible")
    print("C261 byte replay: PASS")


if __name__ == "__main__":
    main()
