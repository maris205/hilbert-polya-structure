#!/usr/bin/env python3
"""Byte-identical producer replays in unrelated fresh directories."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c395 replay refuses optimized Python")
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parents[1]
def main():
    blobs=[]
    with tempfile.TemporaryDirectory(prefix="c395-left-") as left,tempfile.TemporaryDirectory(prefix="c395-right-") as right:
        for folder in (left,right):
            p=Path(folder)/"evidence.json"
            for cmd in ([sys.executable,"-B",str(ROOT/"code/c395_bcz_producer.py"),"--output",str(p)],[sys.executable,"-B",str(ROOT/"code/c395_bcz_checker.py"),"--evidence",str(p)]):
                x=subprocess.run(cmd,cwd=folder,capture_output=True,text=True);assert x.returncode==0,x.stdout+x.stderr
            blobs.append(p.read_bytes())
    assert blobs[0]==blobs[1]==(ROOT/"results/c395_bcz_evidence.json").read_bytes()
    print("C395 two-directory replay PASS: "+hashlib.sha256(blobs[0]).hexdigest())
if __name__=="__main__":main()
