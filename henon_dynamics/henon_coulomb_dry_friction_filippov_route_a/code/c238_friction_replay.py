#!/usr/bin/env python3
"""Byte-replay check for the deterministic C238 producer."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c238_friction_producer.py"
EVIDENCE = ROOT / "results/c238_friction_evidence.json"


def main() -> None:
    env = dict(os.environ); env["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory(prefix="c238-replay-") as td:
        outputs = [Path(td) / "one.json", Path(td) / "two.json"]
        for out in outputs:
            subprocess.check_call([sys.executable, "-B", str(PRODUCER), "--output", str(out)], env=env, stdout=subprocess.DEVNULL)
        if outputs[0].read_bytes() != outputs[1].read_bytes() or outputs[0].read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("producer bytes are not reproducible")
    print("C238_REPLAY_PASS (canonical bytes match two fresh producer runs)")


if __name__ == "__main__":
    main()
