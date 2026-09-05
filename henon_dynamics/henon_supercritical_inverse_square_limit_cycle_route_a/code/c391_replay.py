#!/usr/bin/env python3
"""Replay canonical producer from two unrelated working directories."""
if not __debug__: raise RuntimeError("c391 replay refuses optimized Python")
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
ROOT=Path(__file__).resolve().parents[1]
def run():
    blobs=[]
    for prefix in ("c391-replay-a-","c391-replay-b-"):
      with tempfile.TemporaryDirectory(prefix=prefix) as directory:
        out=Path(directory)/"receipt.json"
        subprocess.run([sys.executable,"-B",str(ROOT/"code/c391_producer.py"),"--output",str(out)],cwd=directory,check=True,capture_output=True)
        subprocess.run([sys.executable,"-B",str(ROOT/"code/c391_checker.py"),str(out)],cwd=directory,check=True,capture_output=True)
        blobs.append(out.read_bytes())
    assert blobs[0]==blobs[1]==(ROOT/"results/c391_evidence.json").read_bytes()
    print("C391 two-directory replay PASS",hashlib.sha256(blobs[0]).hexdigest())
if __name__=="__main__":run()
