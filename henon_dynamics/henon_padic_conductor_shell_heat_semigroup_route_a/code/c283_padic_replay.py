#!/usr/bin/env python3
"""Fresh-path byte replay for HCS-C283."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c283-replay-") as directory:
        output = Path(directory) / "evidence.json"
        env = dict(os.environ)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        env["C283_OUTPUT_PATH"] = str(output)
        subprocess.check_call([sys.executable, "-B", str(ROOT / "code/c283_padic_producer.py")], env=env)
        assert output.read_bytes() == (ROOT / "results/c283_padic_evidence.json").read_bytes()
    print("C283 byte replay: PASS")


if __name__ == "__main__":
    main()
