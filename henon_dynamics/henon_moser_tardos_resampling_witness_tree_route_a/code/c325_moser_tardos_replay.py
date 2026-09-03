#!/usr/bin/env python3
"""Isolated byte replay for HCS-C325."""
import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c325_moser_tardos_evidence.json"
PRODUCER = ROOT / "code/c325_moser_tardos_producer.py"


def main():
    if sys.flags.optimize:
        raise RuntimeError("C325 replay refuses optimized Python")
    copies = []
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix="c325-replay-") as directory:
            target = Path(directory) / "evidence.json"
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
            subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(target)], check=True,
                           env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            copies.append(target.read_bytes())
    if copies[0] != copies[1] or copies[0] != EVIDENCE.read_bytes():
        raise AssertionError("byte replay differs")
    print(f"C325 byte replay: PASS {hashlib.sha256(copies[0]).hexdigest()}")


if __name__ == "__main__":
    main()
