#!/usr/bin/env python3
"""Isolated byte replay for the HCS-C305 evidence producer."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c305_zermelo_producer.py"
EVIDENCE = ROOT / "results/c305_zermelo_evidence.json"


def main() -> None:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c305-replay-") as temporary:
        outputs = [Path(temporary) / "first.json", Path(temporary) / "second.json"]
        for output in outputs:
            completed = subprocess.run([sys.executable, "-B", str(PRODUCER), "--output", str(output)], env=env, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if "C305_PRODUCER_PASS" not in completed.stdout:
                raise AssertionError("producer sentinel absent")
        if outputs[0].read_bytes() != outputs[1].read_bytes() or outputs[0].read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("isolated replay differs from archive")
        print(f"C305 byte replay: PASS ({hashlib.sha256(outputs[0].read_bytes()).hexdigest()})")


if __name__ == "__main__":
    main()
