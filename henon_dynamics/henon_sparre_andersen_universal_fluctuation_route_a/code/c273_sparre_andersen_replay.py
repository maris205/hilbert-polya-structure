#!/usr/bin/env python3
"""Fresh-process byte replay for HCS-C273."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c273_sparre_andersen_evidence.json"
PRODUCER = ROOT / "code/c273_sparre_andersen_producer.py"


def main() -> None:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory(prefix="c273-replay-") as directory:
        replay = Path(directory) / "evidence.json"
        output = subprocess.check_output(
            [sys.executable, "-B", str(PRODUCER), "--output", str(replay)],
            env=environment,
            text=True,
        )
        assert "C273_PRODUCER_PASS" in output
        assert replay.read_bytes() == EVIDENCE.read_bytes()
    print(f"C273 byte replay: PASS ({EVIDENCE.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
