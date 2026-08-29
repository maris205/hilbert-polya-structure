#!/usr/bin/env python3
"""Clean-process canonical-byte replay for HCS-C228."""
from __future__ import annotations

from hashlib import sha256
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c228_coagulation_producer.py"
EVIDENCE = ROOT / "results/c228_coagulation_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c228-replay-") as tmpdir:
        output = Path(tmpdir) / "evidence.json"
        env = {"PATH": os.environ.get("PATH", ""), "PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1", "LC_ALL": "C.UTF-8"}
        subprocess.run([sys.executable, str(PRODUCER), "--output", str(output)], check=True,
                       env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        released, replayed = EVIDENCE.read_bytes(), output.read_bytes()
        if released != replayed:
            raise AssertionError(f"byte mismatch released={sha256(released).hexdigest()} replay={sha256(replayed).hexdigest()}")
    print(f"C228 canonical byte replay: PASS ({len(released)} bytes; sha256={sha256(released).hexdigest()})")


if __name__ == "__main__":
    main()
