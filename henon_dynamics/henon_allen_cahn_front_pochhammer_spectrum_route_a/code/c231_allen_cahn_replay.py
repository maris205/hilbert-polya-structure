#!/usr/bin/env python3
"""Byte-level replay of the C231 producer in an isolated process."""
from __future__ import annotations

from hashlib import sha256
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c231_allen_cahn_evidence.json"
PRODUCER = ROOT / "code/c231_allen_cahn_producer.py"


def main() -> None:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory(prefix="c231-replay-") as td:
        out = Path(td) / "replayed.json"
        subprocess.check_call([sys.executable, "-B", str(PRODUCER), "--output", str(out)], env=env, stdout=subprocess.DEVNULL)
        a = EVIDENCE.read_bytes()
        b = out.read_bytes()
        assert a == b, "producer replay bytes differ"
    print(f"C231 byte replay: PASS sha256={sha256(a).hexdigest()}")


if __name__ == "__main__":
    main()
