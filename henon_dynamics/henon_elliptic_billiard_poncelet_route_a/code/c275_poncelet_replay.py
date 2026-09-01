#!/usr/bin/env python3
"""Fresh-path byte replay for HCS-C275."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c275-replay-") as directory:
        output = Path(directory) / "evidence.json"
        environment = dict(os.environ)
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        environment["C275_OUTPUT_PATH"] = str(output)
        subprocess.check_call(
            [sys.executable, "-B", str(ROOT / "code/c275_poncelet_producer.py")],
            env=environment,
        )
        assert output.read_bytes() == (ROOT / "results/c275_poncelet_evidence.json").read_bytes()
    print("C275 byte replay: PASS")


if __name__ == "__main__":
    main()
