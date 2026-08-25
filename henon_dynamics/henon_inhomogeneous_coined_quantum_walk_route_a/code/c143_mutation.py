#!/usr/bin/env python3
from __future__ import annotations
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[1];E=ROOT/'results/c143_quantum_walk_evidence.json';C=ROOT/'code/c143_quantum_walk_checker.py'
def repair(d):
    w=dict(d);w.pop('payload_sha256',None);d['payload_sha256']=sha256(json.dumps(w,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def setp(d,p,v):
    x=d
    for k in p[:-1]:x=x[k]
    x[p[-1]]=v
def rejected(d):
    with tempfile.TemporaryDirectory(prefix='c143-mut-') as tmp:
        p=Path(tmp)/'m.json';p.write_text(json.dumps(d,sort_keys=True,indent=2)+'\n');return subprocess.run([sys.executable,str(C),str(p)],capture_output=True,text=True).returncode!=0
def main():
    b=json.loads(E.read_text());cases=[
      (('schema',),'bad'),(('candidate_id',),'HCS-X'),(('scope_literal',),'BAD'),(('source_lock','basis_order'),'reversed'),(('source_lock','clock'),'shift-then-coin'),(('source_lock','determinant_convention'),'1/D'),(('source_lock','cutoff','path'),9),
      (('unitary_reversal_theorem','unitary'),False),(('unitary_reversal_theorem','theta_square'),'C'),(('unitary_reversal_theorem','reversal'),'Theta U Theta=U'),
      (('arrangement_control','dihedrally_equivalent'),True),(('arrangement_control','same_coin_population','0'),2),(('arrangement_control','determinant_polynomials_ascending','00011',2),'0'),(('arrangement_control','determinant_polynomials_ascending','00101',4),'0'),
      (('trace_ledgers','00011',1,'trace_Un'),'0'),(('trace_ledgers','00101',4,'trace_Un'),'0'),(('path_ledgers','00011',4,'rooted_closed_paths'),0),(('path_ledgers','00101',6,'signed_amplitude_sum'),'0'),
      (('population_average_negative_control','orthogonality_defect'),'0'),(('population_average_negative_control','determinant'),'-1'),(('population_average_negative_control','verdict'),'UNITARY'),(('raw_primitive_product_domain',),'entire'),
      (('route_a','tuple'),['A1_WEAK','A2_FAIL','A3_FAIL','A4_ROUTE_B_READY']),(('route_a','overall'),'ROUTE_A_SUCCESS_ROUTE_B_READY'),(('route_a','route_b_invocation_allowed'),True),
      (('claim_boundary','target_divisor_matching'),True),(('claim_boundary','euler_factors'),True),(('claim_boundary','root_numbers'),True),(('claim_boundary','self_adjoint_hilbert_polya'),True)]
    n=0
    for p,v in cases:
        d=deepcopy(b);setp(d,p,v);repair(d)
        if not rejected(d):raise SystemExit(f'mutant survived {p}')
        n+=1
    d=deepcopy(b);d['unitary_reversal_theorem']['unitary']=False
    if not rejected(d):raise SystemExit('stale survived')
    print(json.dumps({'status':'PASS','repaired_hash_rejections':n,'stale_hash_rejections':1,'total':n+1},sort_keys=True))
if __name__=='__main__':main()
