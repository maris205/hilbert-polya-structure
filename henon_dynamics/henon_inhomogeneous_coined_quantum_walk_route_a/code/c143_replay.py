#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[1]
def main():
    with tempfile.TemporaryDirectory(prefix='c143-replay-') as tmp:
        out=Path(tmp)/'evidence.json';subprocess.run([sys.executable,str(ROOT/'code/c143_quantum_walk_producer.py'),'--output',str(out)],check=True,capture_output=True,text=True)
        if out.read_bytes()!=(ROOT/'results/c143_quantum_walk_evidence.json').read_bytes():raise SystemExit('C143 replay mismatch')
    print(json.dumps({'status':'PASS','byte_replay':True},sort_keys=True))
if __name__=='__main__':main()
