#!/usr/bin/env python3
"""Regenerate C204 evidence in a temporary directory and compare bytes."""
import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "results" / "c204_finite_linear_evidence.json"
PRODUCER = ROOT / "code" / "c204_finite_linear_producer.py"


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    with tempfile.TemporaryDirectory(prefix="c204-replay-") as d:
        out = Path(d) / "evidence.json"; env = dict(os.environ); env["C204_OUTPUT"] = str(out)
        subprocess.run([sys.executable, str(PRODUCER)], check=True, env=env, stdout=subprocess.PIPE, text=True)
        assert out.read_bytes() == EXPECTED.read_bytes(), (sha(out), sha(EXPECTED))
    print(f"C204 byte replay: PASS sha256={sha(EXPECTED)}")


if __name__ == "__main__": main()
