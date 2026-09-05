#!/usr/bin/env python3
"""Two isolated working directories, byte equality and source-evidence equality."""
if not __debug__:
    raise RuntimeError("c385 replay refuses optimized Python")
import subprocess
import sys
import tempfile
from pathlib import Path

def main():
    root=Path(__file__).resolve().parents[1]; blobs=[]
    for lane in ("a","b"):
        with tempfile.TemporaryDirectory(prefix="c385-replay-"+lane+"-") as d:
            work=Path(d); out=work/"result.json"
            p=subprocess.run([sys.executable,"-B",str(root/"code/c385_lozi_producer.py"),"--output",str(out)],cwd=work,capture_output=True,text=True)
            assert p.returncode==0,p.stderr
            blobs.append(out.read_bytes())
    assert blobs[0]==blobs[1]==(root/"results/c385_lozi_evidence.json").read_bytes()
    print("C385 isolated replay PASS: two directories and canonical bytes agree")

if __name__=="__main__":main()
