#!/usr/bin/env python3
from __future__ import annotations
import hashlib, os, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; PRODUCER=ROOT/"code/c287_wave_producer.py"; EVIDENCE=ROOT/"results/c287_wave_evidence.json"
def main():
    env=dict(os.environ); env["PYTHONDONTWRITEBYTECODE"]="1"; env["TZ"]="UTC"
    with tempfile.TemporaryDirectory(prefix="c287_a_") as a, tempfile.TemporaryDirectory(prefix="c287_b_") as b:
        pa,pb=Path(a)/"e.json",Path(b)/"e.json"
        subprocess.check_call([sys.executable,"-B",str(PRODUCER),"--output",str(pa)],env=env)
        subprocess.check_call([sys.executable,"-B",str(PRODUCER),"--output",str(pb)],env=env)
        assert pa.read_bytes()==pb.read_bytes()==EVIDENCE.read_bytes()
        print(f"C287 byte replay: PASS {hashlib.sha256(pa.read_bytes()).hexdigest()}")
if __name__=="__main__": main()
