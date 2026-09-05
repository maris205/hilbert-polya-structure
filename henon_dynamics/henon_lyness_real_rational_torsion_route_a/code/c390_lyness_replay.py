#!/usr/bin/env python3
"""Fresh, distinct working directories; compare exact evidence bytes."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c390 replay refuses optimized Python")
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parents[1]
def main():
    blobs=[]
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix="c390-replay-") as d:
            out=Path(d)/"evidence.json"
            subprocess.run([sys.executable,"-B",str(ROOT/"code/c390_lyness_producer.py"),"--output",str(out)],cwd=d,capture_output=True,text=True,check=True)
            subprocess.run([sys.executable,"-B",str(ROOT/"code/c390_lyness_checker.py"),"--evidence",str(out)],cwd=d,capture_output=True,text=True,check=True)
            blobs.append(out.read_bytes())
    assert blobs[0]==blobs[1]==(ROOT/"results/c390_lyness_evidence.json").read_bytes()
    print("C390 two-directory byte replay PASS: "+hashlib.sha256(blobs[0]).hexdigest())
if __name__=="__main__":main()
