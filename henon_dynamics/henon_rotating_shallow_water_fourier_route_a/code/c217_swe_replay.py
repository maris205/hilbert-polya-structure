#!/usr/bin/env python3
"""Byte-replay the C217 producer in a temporary output path."""
import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c217_swe_producer.py"
EXPECTED = ROOT / "results/c217_swe_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c217-replay-") as directory:
        output = Path(directory) / "evidence.json"
        env = dict(os.environ)
        env["C217_OUTPUT"] = str(output)
        subprocess.run([sys.executable, str(PRODUCER)], check=True, env=env,
                       stdout=subprocess.PIPE, text=True)
        assert output.read_bytes() == EXPECTED.read_bytes()
    digest = hashlib.sha256(EXPECTED.read_bytes()).hexdigest()
    print(f"C217 byte replay: PASS sha256={digest}")


if __name__ == "__main__":
    main()
