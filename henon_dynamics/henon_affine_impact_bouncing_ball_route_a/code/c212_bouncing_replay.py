#!/usr/bin/env python3
"""Byte-replay the C212 producer in a temporary output path."""
import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c212_bouncing_producer.py"
EXPECTED = ROOT / "results/c212_bouncing_evidence.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c212-replay-") as directory:
        output = Path(directory) / "evidence.json"
        environment = dict(os.environ)
        environment["C212_OUTPUT"] = str(output)
        subprocess.run([sys.executable, str(PRODUCER)], check=True,
                       env=environment, stdout=subprocess.PIPE, text=True)
        assert output.read_bytes() == EXPECTED.read_bytes()
    print(f"C212 byte replay: PASS sha256={digest(EXPECTED)}")


if __name__ == "__main__":
    main()
