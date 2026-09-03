#!/usr/bin/env python3
"""Two-directory byte-for-byte evidence replay for HCS-C344."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "code/c344_resonant_triad_producer.py"
EVIDENCE = ROOT / "results/c344_resonant_triad_evidence.json"


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C344 replay refuses optimized Python")
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c344-replay-a-") as first_dir:
        with tempfile.TemporaryDirectory(prefix="c344-replay-b-") as second_dir:
            outputs = [Path(first_dir)/"evidence.json", Path(second_dir)/"evidence.json"]
            for target in outputs:
                output = subprocess.check_output(
                    [sys.executable, "-B", str(SCRIPT), "--output", str(target)],
                    env=environment, text=True,
                )
                if "C344_PRODUCER_PASS" not in output:
                    raise AssertionError("producer sentinel absent")
            if outputs[0].read_bytes() != outputs[1].read_bytes():
                raise AssertionError("isolated producer outputs differ")
            if outputs[0].read_bytes() != EVIDENCE.read_bytes():
                raise AssertionError("checked-in evidence is stale")
            digest = hashlib.sha256(outputs[0].read_bytes()).hexdigest()
    print(f"C344 byte replay: PASS ({digest})")


if __name__ == "__main__":
    main()
