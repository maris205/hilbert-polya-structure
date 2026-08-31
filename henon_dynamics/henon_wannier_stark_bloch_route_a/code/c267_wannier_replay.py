#!/usr/bin/env python3
import hashlib,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; P=ROOT/"results/c267_wannier_evidence.json"
before=P.read_bytes(); h=hashlib.sha256(before).hexdigest()
subprocess.run([sys.executable,"-B",str(ROOT/"code/c267_wannier_producer.py")],check=True,stdout=subprocess.DEVNULL)
after=P.read_bytes(); assert before==after and hashlib.sha256(after).hexdigest()==h
print(f"C267 byte replay: PASS ({len(after)} bytes; sha256={h})")
