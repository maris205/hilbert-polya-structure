#!/usr/bin/env python3
"""Byte-replay check for the deterministic C235 producer."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c235_rps_producer.py"
EVIDENCE = ROOT / "results/c235_rps_evidence.json"


def main() -> None:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory(prefix="c235-replay-") as td:
        one = Path(td) / "one.json"
        two = Path(td) / "two.json"
        for out in (one, two):
            subprocess.check_call([sys.executable, "-B", str(PRODUCER), "--output", str(out)], env=env, stdout=subprocess.DEVNULL)
        canonical = EVIDENCE.read_bytes()
        if one.read_bytes() != two.read_bytes() or one.read_bytes() != canonical:
            raise AssertionError("producer bytes are not reproducible")
    print("C235_REPLAY_PASS (canonical bytes match two fresh producer runs)")


if __name__ == "__main__":
    main()
