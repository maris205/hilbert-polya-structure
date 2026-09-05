#!/usr/bin/env python3
"""Two isolated producer working directories must reproduce the frozen bytes."""
import hashlib
from pathlib import Path
import os
import subprocess
import sys
import tempfile

if sys.flags.optimize:
    raise RuntimeError('C382 replay refuses optimized Python')
root=Path(__file__).resolve().parents[1]
outputs=[]
for lane in range(2):
    with tempfile.TemporaryDirectory(prefix='c382-replay-') as directory:
        path=Path(directory)/'evidence.json'
        subprocess.run([sys.executable,'-B',str(root/'code/c382_cm_producer.py'),
                        '--output',str(path)],cwd=directory,check=True,
                       env=dict(os.environ,PYTHONHASHSEED=str(47+lane)),capture_output=True)
        outputs.append(path.read_bytes())
if outputs[0]!=outputs[1] or outputs[0]!=(root/'results/c382_cm_evidence.json').read_bytes():
    raise ValueError('isolated replay drift')
print('C382 byte replay: PASS',hashlib.sha256(outputs[0]).hexdigest())
