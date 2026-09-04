#!/usr/bin/env python3
"""Two-directory byte replay for HCS-C368 evidence."""
from __future__ import annotations
import os, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'code/c368_pg_producer.py'; CHECKED=ROOT/'results/c368_pg_evidence.json'
def main():
    if sys.flags.optimize: raise RuntimeError('C368 replay refuses optimized Python')
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',TZ='UTC'); blobs=[]
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix='c368-replay-') as d:
            p=Path(d)/'evidence.json'; out=subprocess.check_output([sys.executable,'-B',str(SCRIPT),'--output',str(p)],env=env,text=True)
            if 'C368_PRODUCER_PASS' not in out: raise AssertionError('producer sentinel missing')
            blobs.append(p.read_bytes())
    checked=CHECKED.read_bytes()
    if blobs[0]!=blobs[1] or blobs[0]!=checked: raise AssertionError('nonidentical evidence replay')
    print(f'C368 byte replay: PASS ({len(checked)} bytes, 2 isolated runs)')
if __name__=='__main__': main()
