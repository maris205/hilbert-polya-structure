#!/usr/bin/env python3
"""Byte-replay the C219 producer in an isolated temporary directory."""
from __future__ import annotations

from hashlib import sha256
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c219_rayleigh_producer.py"
EXPECTED = ROOT / "results/c219_rayleigh_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c219-replay-") as directory:
        output = Path(directory) / "evidence.json"
        env = dict(os.environ)
        env["C219_OUTPUT"] = str(output)
        subprocess.run([sys.executable, str(PRODUCER)], check=True, env=env,
                       stdout=subprocess.PIPE, text=True)
        assert output.read_bytes() == EXPECTED.read_bytes()
    print(f"C219 byte replay: PASS sha256={sha256(EXPECTED.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
