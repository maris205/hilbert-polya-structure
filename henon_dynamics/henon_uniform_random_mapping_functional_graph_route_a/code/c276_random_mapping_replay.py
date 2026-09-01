#!/usr/bin/env python3
"""Fresh-process byte replay for HCS-C276."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c276_random_mapping_evidence.json"
PRODUCER = ROOT / "code/c276_random_mapping_producer.py"


def main() -> None:
    environment = dict(os.environ)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    with tempfile.TemporaryDirectory(prefix="c276-replay-") as directory:
        replay = Path(directory) / "evidence.json"
        output = subprocess.check_output(
            [sys.executable, "-B", str(PRODUCER), "--output", str(replay)],
            env=environment,
            text=True,
        )
        assert "C276_PRODUCER_PASS" in output
        assert replay.read_bytes() == EVIDENCE.read_bytes()
    print(f"C276 byte replay: PASS ({EVIDENCE.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
