#!/usr/bin/env python3
"""Byte-for-byte producer replay for HCS-C321."""
import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c321_preferential_attachment_evidence.json"
PRODUCER = ROOT / "code/c321_preferential_attachment_producer.py"


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C321 replay refuses optimized Python")
    with tempfile.TemporaryDirectory(prefix="c321-replay-") as directory:
        target = Path(directory) / "evidence.json"
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
        subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(target)],
                       check=True, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if target.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("producer replay differs")
    digest = hashlib.sha256(EVIDENCE.read_bytes()).hexdigest()
    print(f"C321 byte replay: PASS {digest}")


if __name__ == "__main__":
    main()
