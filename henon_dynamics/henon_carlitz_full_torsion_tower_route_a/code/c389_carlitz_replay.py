#!/usr/bin/env python3
"""Replay frozen producer source from two independent working directories."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]
def main():
    if not __debug__: raise SystemExit('optimized mode forbidden')
    outputs=[]
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix='c389-replay-') as folder:
            out=Path(folder)/'evidence.json'
            subprocess.run([sys.executable,'-B',str(ROOT/'code/c389_carlitz_producer.py'),'--output',str(out)],
                 cwd=folder,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),check=True,capture_output=True)
            outputs.append(out.read_bytes())
    if not outputs[0]==outputs[1]==(ROOT/'results/c389_carlitz_evidence.json').read_bytes(): raise ValueError('replay differs')
    print(json.dumps({'status':'PASS','independent_working_directories':2,'identical_frozen_source':True,
                      'sha256':hashlib.sha256(outputs[0]).hexdigest()}))
if __name__=='__main__': main()
