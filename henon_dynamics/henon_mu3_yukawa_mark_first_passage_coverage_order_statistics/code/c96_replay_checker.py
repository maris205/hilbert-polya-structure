#!/usr/bin/env python3
"""Clean-process deterministic checker replay for C96."""
from __future__ import annotations
from hashlib import sha256
import json,os,subprocess,sys
from pathlib import Path
PROJECT=Path(__file__).resolve().parents[1]; EVIDENCE=PROJECT/'results/c96_coverage_order_statistics_evidence.json'; CHECKER=PROJECT/'code/c96_coverage_order_statistics_checker.py'; EXPECTED='75a93c80b5e44f6aca1885073cf12e943de02751ad4e99aa37e83bf211b6ca23'
def main():
 before=sha256(EVIDENCE.read_bytes()).hexdigest(); assert before==EXPECTED; env={**os.environ,'PYTHONHASHSEED':'0','PYTHONDONTWRITEBYTECODE':'1','LC_ALL':'C','TZ':'UTC'}; run=subprocess.run([sys.executable,str(CHECKER)],cwd=PROJECT,capture_output=True,text=True,check=True,env=env); after=sha256(EVIDENCE.read_bytes()).hexdigest(); assert after==before; p=json.loads(run.stdout.strip().splitlines()[-1]); assert p['status']=='C96_INDEPENDENT_CHECK_PASS' and p['rank_count']==20; print(json.dumps({'status':'C96_REPLAY_PASS','rank_count':p['rank_count'],'support_count':p['support_count'],'evidence_sha256':after},sort_keys=True))
if __name__=='__main__': main()
