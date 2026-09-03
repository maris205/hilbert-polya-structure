#!/usr/bin/env python3
"""Isolated byte-for-byte evidence replay for HCS-C337."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c337_kicked_rotor_producer.py"
EVIDENCE = ROOT / "results/c337_kicked_rotor_evidence.json"


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C337 replay refuses optimized Python")
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c337-replay-") as directory:
        work = Path(directory)
        outputs = [work / "first.json", work / "second.json"]
        for target in outputs:
            result = subprocess.check_output(
                [sys.executable, "-B", str(PRODUCER), "--output", str(target)],
                env=environment, text=True,
            )
            if "C337_PRODUCER_PASS" not in result:
                raise AssertionError("producer sentinel absent")
        if outputs[0].read_bytes() != outputs[1].read_bytes():
            raise AssertionError("isolated producer outputs differ")
        if outputs[0].read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("checked-in evidence is stale")
        print(f"C337 byte replay: PASS ({hashlib.sha256(outputs[0].read_bytes()).hexdigest()})")


if __name__ == "__main__":
    main()
