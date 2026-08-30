#!/usr/bin/env python3
"""Byte-level deterministic replay for C247."""
from __future__ import annotations
import sys
sys.dont_write_bytecode=True
from hashlib import sha256
import os, subprocess, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; EVIDENCE=ROOT/"results/c247_billiard_evidence.json"; PRODUCER=ROOT/"code/c247_billiard_producer.py"
def main():
    env=dict(os.environ);env["PYTHONDONTWRITEBYTECODE"]="1"
    with tempfile.TemporaryDirectory(prefix="c247-replay-") as td:
        out=Path(td)/"replayed.json"; subprocess.check_call([sys.executable,"-B",str(PRODUCER),"--output",str(out)],env=env,stdout=subprocess.DEVNULL); a=EVIDENCE.read_bytes(); b=out.read_bytes(); assert a==b,"producer replay bytes differ"
    print(f"C247 byte replay: PASS sha256={sha256(a).hexdigest()}")
if __name__=="__main__": main()
