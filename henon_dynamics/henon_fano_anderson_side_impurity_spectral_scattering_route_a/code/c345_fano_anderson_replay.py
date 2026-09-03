#!/usr/bin/env python3
"""Two-directory byte-for-byte evidence replay for HCS-C345."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "code/c345_fano_anderson_producer.py"
EVIDENCE = ROOT / "results/c345_fano_anderson_evidence.json"


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C345 replay refuses optimized Python")
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c345-replay-a-") as first_dir:
        with tempfile.TemporaryDirectory(prefix="c345-replay-b-") as second_dir:
            outputs = [Path(first_dir)/"evidence.json", Path(second_dir)/"evidence.json"]
            for target in outputs:
                result = subprocess.check_output(
                    [sys.executable, "-B", str(SCRIPT), "--output", str(target)],
                    env=environment, text=True,
                )
                if "C345_PRODUCER_PASS" not in result:
                    raise AssertionError("producer sentinel absent")
            if outputs[0].read_bytes() != outputs[1].read_bytes():
                raise AssertionError("isolated evidence outputs differ")
            if outputs[0].read_bytes() != EVIDENCE.read_bytes():
                raise AssertionError("checked-in evidence is stale")
            digest = hashlib.sha256(outputs[0].read_bytes()).hexdigest()
    print(f"C345 byte replay: PASS ({digest})")


if __name__ == "__main__":
    main()
