#!/usr/bin/env python3
"""Two independent working directories, exact byte equality, checker replay."""
if not __debug__:
    raise RuntimeError("c388 replay refuses optimized Python")
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parents[1]
def run(cmd,cwd):
    p=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True)
    assert p.returncode==0,p.stdout+p.stderr
def main():
    blobs=[]
    for k in range(2):
        with tempfile.TemporaryDirectory(prefix="c388-replay-") as d:
            out=Path(d)/"evidence.json"
            run([sys.executable,"-B",str(ROOT/"code/c388_algebraic_producer.py"),"--output",str(out)],d)
            run([sys.executable,"-B",str(ROOT/"code/c388_algebraic_checker.py"),"--evidence",str(out)],d)
            blobs.append(out.read_bytes())
    assert blobs[0]==blobs[1]==(ROOT/"results/c388_algebraic_evidence.json").read_bytes()
    print("C388 two-directory replay PASS: "+hashlib.sha256(blobs[0]).hexdigest())
if __name__=="__main__":main()
