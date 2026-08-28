#!/usr/bin/env python3
"""Byte-replay the C211 producer in a temporary output path."""
import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c211_lv_producer.py"
EXPECTED = ROOT / "results/c211_lv_evidence.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c211-replay-") as directory:
        output = Path(directory) / "evidence.json"
        environment = dict(os.environ)
        environment["C211_OUTPUT"] = str(output)
        subprocess.run([sys.executable, str(PRODUCER)], check=True,
                       env=environment, stdout=subprocess.PIPE, text=True)
        assert output.read_bytes() == EXPECTED.read_bytes()
    print(f"C211 byte replay: PASS sha256={digest(EXPECTED)}")


if __name__ == "__main__":
    main()
