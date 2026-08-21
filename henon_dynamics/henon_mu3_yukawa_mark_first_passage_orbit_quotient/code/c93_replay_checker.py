#!/usr/bin/env python3
from __future__ import annotations
from hashlib import sha256
import json,os,subprocess,sys
from pathlib import Path
PROJECT=Path(__file__).resolve().parents[1]; EVIDENCE=PROJECT/'results/c93_first_passage_orbit_quotient_evidence.json'; CHECKER=PROJECT/'code/c93_first_passage_orbit_quotient_checker.py'; EXPECTED='4104f181b88d83666c9fcff814a7029a148c498e6393ad181c60fe5133adb9fe'
def main():
 before=sha256(EVIDENCE.read_bytes()).hexdigest(); assert before==EXPECTED; env={**os.environ,'PYTHONHASHSEED':'0','PYTHONDONTWRITEBYTECODE':'1','LC_ALL':'C','TZ':'UTC'}; run=subprocess.run([sys.executable,str(CHECKER)],cwd=PROJECT,capture_output=True,text=True,check=True,env=env); after=sha256(EVIDENCE.read_bytes()).hexdigest(); assert after==before; p=json.loads(run.stdout.strip().splitlines()[-1]); print(json.dumps({'status':'C93_REPLAY_PASS','evidence_sha256':after,'target_orbit_count':p['target_orbit_count']},sort_keys=True))
if __name__=='__main__': main()
