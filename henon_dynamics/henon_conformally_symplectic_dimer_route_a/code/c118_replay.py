#!/usr/bin/env python3
from hashlib import sha256
from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parents[1]; E=ROOT/'results/c118_damped_dimer_evidence.json'
before=E.read_bytes(); subprocess.run([sys.executable,str(ROOT/'code/c118_damped_dimer_producer.py')],check=True,stdout=subprocess.DEVNULL); after=E.read_bytes(); assert before==after
print('C118_REPLAY_PASS',sha256(after).hexdigest())
