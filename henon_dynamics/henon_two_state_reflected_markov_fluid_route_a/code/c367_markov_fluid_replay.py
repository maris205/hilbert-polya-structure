#!/usr/bin/env python3
"""Two-directory byte replay for HCS-C367 evidence."""
from __future__ import annotations
import os, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'code/c367_markov_fluid_producer.py'; CHECKED=ROOT/'results/c367_markov_fluid_evidence.json'
def main():
    if sys.flags.optimize: raise RuntimeError('C367 replay refuses optimized Python')
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',TZ='UTC'); blobs=[]
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix='c367-replay-') as d:
            p=Path(d)/'evidence.json'; out=subprocess.check_output([sys.executable,'-B',str(SCRIPT),'--output',str(p)],env=env,text=True)
            if 'C367_PRODUCER_PASS' not in out: raise AssertionError('producer sentinel missing')
            blobs.append(p.read_bytes())
    checked=CHECKED.read_bytes()
    if blobs[0]!=blobs[1] or blobs[0]!=checked: raise AssertionError('nonidentical evidence replay')
    print(f'C367 byte replay: PASS ({len(checked)} bytes, 2 isolated runs)')
if __name__=='__main__': main()
