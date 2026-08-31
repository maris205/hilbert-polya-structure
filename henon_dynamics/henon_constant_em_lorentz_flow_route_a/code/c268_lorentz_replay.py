#!/usr/bin/env python3
import hashlib,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];P=ROOT/"results/c268_lorentz_evidence.json";before=P.read_bytes();h=hashlib.sha256(before).hexdigest()
subprocess.run([sys.executable,"-B",str(ROOT/"code/c268_lorentz_producer.py")],check=True,stdout=subprocess.DEVNULL)
after=P.read_bytes();assert before==after and hashlib.sha256(after).hexdigest()==h
print(f"C268 byte replay: PASS ({len(after)} bytes; sha256={h})")
