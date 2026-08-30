#!/usr/bin/env python3
"""Byte replay for the deterministic C245 producer."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c245_pulse_if_producer.py"
EVIDENCE = ROOT / "results/c245_pulse_if_evidence.json"


def main() -> None:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory(prefix="c245-replay-") as td:
        outs = [Path(td) / "one.json", Path(td) / "two.json"]
        for out in outs:
            subprocess.check_call([sys.executable, "-B", str(PRODUCER), "--output", str(out)], env=env, stdout=subprocess.DEVNULL)
        if outs[0].read_bytes() != outs[1].read_bytes() or outs[0].read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("producer bytes are not reproducible")
    print("C245_REPLAY_PASS (canonical bytes match two fresh producer runs)")


if __name__ == "__main__":
    main()
