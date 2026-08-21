#!/usr/bin/env python3
"""Clean-process deterministic checker replay for C95."""
from __future__ import annotations
from hashlib import sha256
import json,os,subprocess,sys
from pathlib import Path
PROJECT=Path(__file__).resolve().parents[1]; EVIDENCE=PROJECT/'results/c95_comparable_delay_evidence.json'; CHECKER=PROJECT/'code/c95_comparable_delay_checker.py'; EXPECTED='53e5c9a1dbda2fa7e01af34ce6fc161ac102a312b003e1c86402ae7ec7373a3c'
def main():
 before=sha256(EVIDENCE.read_bytes()).hexdigest(); assert before==EXPECTED; env={**os.environ,'PYTHONHASHSEED':'0','PYTHONDONTWRITEBYTECODE':'1','LC_ALL':'C','TZ':'UTC'}; run=subprocess.run([sys.executable,str(CHECKER)],cwd=PROJECT,capture_output=True,text=True,check=True,env=env); after=sha256(EVIDENCE.read_bytes()).hexdigest(); assert after==before; p=json.loads(run.stdout.strip().splitlines()[-1]); assert p['status']=='C95_INDEPENDENT_CHECK_PASS' and p['pair_count']==102; print(json.dumps({'status':'C95_REPLAY_PASS','pair_count':p['pair_count'],'pmf_cells':p['pmf_cells'],'evidence_sha256':after},sort_keys=True))
if __name__=='__main__': main()
