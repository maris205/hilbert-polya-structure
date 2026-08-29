#!/usr/bin/env python3
"""Clean-process canonical-byte replay for HCS-C229."""
from __future__ import annotations
from hashlib import sha256
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "code/c229_cir_producer.py"
EVIDENCE = ROOT / "results/c229_cir_evidence.json"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="c229-replay-") as td:
        out = Path(td) / "evidence.json"
        env = {"PATH": os.environ.get("PATH", ""), "PYTHONHASHSEED": "0", "LC_ALL": "C.UTF-8", "PYTHONDONTWRITEBYTECODE": "1"}
        subprocess.run([sys.executable, str(PRODUCER), "--output", str(out)], check=True, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        released = EVIDENCE.read_bytes(); replayed = out.read_bytes()
        if released != replayed:
            raise AssertionError(f"byte mismatch released={sha256(released).hexdigest()} replay={sha256(replayed).hexdigest()}")
    print(f"C229 canonical byte replay: PASS ({len(released)} bytes; sha256={sha256(released).hexdigest()})")


if __name__ == "__main__": main()
