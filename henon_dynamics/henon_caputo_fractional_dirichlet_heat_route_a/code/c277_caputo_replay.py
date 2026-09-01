#!/usr/bin/env python3
"""Fresh-path byte replay for HCS-C277."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c277-replay-") as td:
        out = Path(td) / "evidence.json"
        env = dict(os.environ); env["PYTHONDONTWRITEBYTECODE"] = "1"; env["C277_OUTPUT_PATH"] = str(out)
        subprocess.check_call([sys.executable, "-B", str(ROOT / "code/c277_caputo_producer.py")], env=env)
        assert out.read_bytes() == (ROOT / "results/c277_caputo_evidence.json").read_bytes()
    print("C277 byte replay: PASS")


if __name__ == "__main__":
    main()
