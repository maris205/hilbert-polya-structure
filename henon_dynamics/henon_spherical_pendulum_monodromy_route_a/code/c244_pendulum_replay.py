#!/usr/bin/env python3
"""Byte-level deterministic replay for C244."""
from __future__ import annotations
import sys
sys.dont_write_bytecode=True
from hashlib import sha256
import os, subprocess, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EVIDENCE=ROOT/"results/c244_pendulum_evidence.json"
PRODUCER=ROOT/"code/c244_pendulum_producer.py"
def main():
    env=dict(os.environ); env["PYTHONDONTWRITEBYTECODE"]="1"
    with tempfile.TemporaryDirectory(prefix="c244-replay-") as td:
        out=Path(td)/"replayed.json"
        subprocess.check_call([sys.executable,"-B",str(PRODUCER),"--output",str(out)],env=env,stdout=subprocess.DEVNULL)
        original=EVIDENCE.read_bytes(); replayed=out.read_bytes(); assert original==replayed,"producer replay bytes differ"
    print(f"C244 byte replay: PASS sha256={sha256(original).hexdigest()}")
if __name__=="__main__": main()
