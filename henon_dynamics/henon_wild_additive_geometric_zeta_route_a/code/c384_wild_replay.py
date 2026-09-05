#!/usr/bin/env python3
"""Recompute identical evidence from two isolated working directories."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]

def main():
    if sys.flags.optimize:raise RuntimeError('C384 replay refuses optimized Python')
    results=[]
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix='c384-replay-') as directory:
            path=Path(directory)/'evidence.json'
            p=subprocess.run([sys.executable,'-B',str(ROOT/'code/c384_wild_producer.py'),'--output',str(path)],
              cwd=directory,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),text=True,capture_output=True)
            if p.returncode:raise ValueError(p.stdout+p.stderr)
            results.append(path.read_bytes())
    if not results[0]==results[1]==(ROOT/'results/c384_wild_evidence.json').read_bytes():raise ValueError('byte replay drift')
    print('C384_REPLAY_PASS isolated_directories=2 exact_byte_match=true')

if __name__=='__main__':main()
