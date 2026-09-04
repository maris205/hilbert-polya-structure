#!/usr/bin/env python3
"""Isolated byte replay for C356 evidence."""
from __future__ import annotations
import os, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; SCRIPT=ROOT/'code/c356_qwz_producer.py'
def main():
    if sys.flags.optimize: raise RuntimeError('C356 replay refuses optimized Python')
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',TZ='UTC'); blobs=[]
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix='c356-replay-') as d:
            p=Path(d)/'evidence.json'; out=subprocess.check_output([sys.executable,'-B',str(SCRIPT),'--output',str(p)],env=env,text=True)
            if 'C356_PRODUCER_PASS' not in out: raise AssertionError('producer sentinel')
            blobs.append(p.read_bytes())
    checked=(ROOT/'results/c356_qwz_evidence.json').read_bytes()
    if blobs[0]!=blobs[1] or blobs[0]!=checked: raise AssertionError('nonidentical replay')
    print(f'C356 byte replay: PASS ({len(checked)} bytes, 2 isolated runs)')
if __name__=='__main__': main()
