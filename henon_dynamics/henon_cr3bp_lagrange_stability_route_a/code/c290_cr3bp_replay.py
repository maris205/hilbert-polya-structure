#!/usr/bin/env python3
"""Two isolated byte-for-byte evidence replays for HCS-C290."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PRODUCER=ROOT/"code/c290_cr3bp_producer.py"
EVIDENCE=ROOT/"results/c290_cr3bp_evidence.json"


def digest(path: Path)->str: return hashlib.sha256(path.read_bytes()).hexdigest()


def main()->None:
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c290-replay-a-") as a,tempfile.TemporaryDirectory(prefix="c290-replay-b-") as b:
        pa,pb=Path(a)/"evidence.json",Path(b)/"evidence.json"
        subprocess.check_call([sys.executable,"-B",str(PRODUCER),"--output",str(pa)],env=env)
        subprocess.check_call([sys.executable,"-B",str(PRODUCER),"--output",str(pb)],env=env)
        assert pa.read_bytes()==pb.read_bytes()==EVIDENCE.read_bytes()
        print(f"C290 byte replay: PASS {digest(pa)}")


if __name__=="__main__": main()
