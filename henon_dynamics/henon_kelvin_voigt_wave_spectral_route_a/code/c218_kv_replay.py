#!/usr/bin/env python3
"""Byte-replay the C218 producer."""
import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c218_kv_producer.py"
EXPECTED = ROOT / "results/c218_kv_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c218-replay-") as directory:
        output = Path(directory) / "evidence.json"
        env = dict(os.environ)
        env["C218_OUTPUT"] = str(output)
        subprocess.run([sys.executable, str(PRODUCER)], check=True, env=env,
                       stdout=subprocess.PIPE, text=True)
        assert output.read_bytes() == EXPECTED.read_bytes()
    print(f"C218 byte replay: PASS sha256={hashlib.sha256(EXPECTED.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
