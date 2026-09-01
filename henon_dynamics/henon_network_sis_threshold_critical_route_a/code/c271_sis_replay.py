#!/usr/bin/env python3
"""Fresh-path byte replay for HCS-C271."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results/c271_sis_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c271-replay-") as td:
        out = Path(td) / "evidence.json"
        env = dict(os.environ)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        env["C271_OUTPUT_PATH"] = str(out)
        subprocess.check_call([sys.executable, "-B", str(ROOT / "code/c271_sis_producer.py")], env=env)
        assert SOURCE.read_bytes() == out.read_bytes()
    print("C271 byte replay: PASS")


if __name__ == "__main__":
    main()
