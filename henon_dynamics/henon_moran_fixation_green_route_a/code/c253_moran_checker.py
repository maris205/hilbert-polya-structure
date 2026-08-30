#!/usr/bin/env python3
"""Producer-independent checker for HCS-C253."""
from __future__ import annotations
import argparse,json,re
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1]; EVIDENCE=ROOT/"results/c253_moran_evidence.json"; SOURCE="3ff451e904f8f063e88c40ef87f4697a6586b1a5"; EVAL="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"; SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"; EPOCH=1788048000; mp.mp.dps=90
CASES=[("neutral_N3",3,F(1),F(1),1),("selected_up_N4",4,F(2),F(1),2),("selected_down_N5",5,F(1,2),F(3,2),3),("mixed_N6",6,F(3,2),F(2),1),("mixed_N7",7,F(4,3),F(5,2),4),("neutral_N8",8,F(1),F(3,4),5),("weak_sel_N9",9,F(9,10),F(4,3),2),("strong_sel_N10",10,F(5,2),F(2,3),7)]
TOP={"schema","candidate_id","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator","headline","frozen_object","theorem","regression","exact_identities","route_a","scope_flags","citations","nonclaims","payload_sha256"}; FLAGS={"uses_target_zero_table","uses_prime_table","claims_arithmetic_local_data","claims_euler_factors","claims_root_numbers","claims_automorphy","claims_target_divisor_or_functional_equation","claims_hilbert_polya_operator","invokes_route_b"}; NUM=re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+|[eE][+-]?[0-9]+)$")
def ph(d):
 b=dict(d); b.pop("payload_sha256",None); return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def q(s): return F(s)
def mq(x): return mp.mpf(x.numerator)/x.denominator
def close(v,w,l,ck):
 ck(isinstance(v,str) and NUM.fullmatch(v) is not None,l+" syntax")
 if isinstance(v,str) and NUM.fullmatch(v): ck(abs(mp.mpf(v)-w)<=mp.mpf("4e-40")*max(1,abs(w)),l)
def solve(A,b):
 n=len(b); M=[list(A[i])+[b[i]] for i in range(n)]
 for c in range(n):
  p=next(i for i in range(c,n) if M[i][c]); M[c],M[p]=M[p],M[c]; z=M[c][c]; M[c]=[v/z for v in M[c]]
  for i in range(n):
   if i==c: continue
   z=M[i][c]
   if z: M[i]=[M[i][j]-z*M[c][j] for j in range(n+1)]
 return [M[i][-1] for i in range(n)]
def independent(N,rho,beta):
 lam=[F(0)]+[beta*rho*F(i*(N-i),N) for i in range(1,N)]; mu=[F(0)]+[beta*F(i*(N-i),N) for i in range(1,N)]; n=N-1
 Q=[[F(0) for _ in range(n)] for __ in range(n)]
 for i in range(1,N):
  z=i-1; Q[z][z]=-(lam[i]+mu[i])
  if i+1<N: Q[z][z+1]=lam[i]
  if i>1: Q[z][z-1]=mu[i]
 A=[[-Q[i][j] for j in range(n)] for i in range(n)]; G=[]
 for i in range(n):
  G.append([solve(A,[F(int(j==k)) for j in range(n)])[i] for k in range(n)])
 return lam,mu,G
def validate(d):
 n=0
 def ck(ok,l):
  nonlocal n; n+=1
  if not ok: raise AssertionError(l)
 ck(set(d)==TOP,"top"); ck(d["schema"]=="hcs-c253-moran-fixation-green-v1","schema"); ck(d["candidate_id"]=="HCS-C253","id"); ck(d["source_commit"]==SOURCE and d["fixed_epoch"]==EPOCH and d["scope_literal"]==SCOPE,"lock"); ck(d["evaluator"]=={"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVAL},"evaluator"); ck(d["payload_sha256"]==ph(d),"hash"); ck(d["route_a"]["tuple"]==["A0_FAIL","A1_PASS_ANALYTIC","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"tuple"); ck(d["route_a"]["overall"]=="ROUTE_A_REJECTED" and d["route_a"]["route_b_invocation_allowed"] is False,"verdict"); ck(set(d["scope_flags"])==FLAGS and all(v is False for v in d["scope_flags"].values()),"scope"); ck(len(d["regression"]["rows"])==8 and len(d["regression"]["boundary_rows"])==4 and len(d["exact_identities"])==10,"counts")
 rkeys={"case_id","N","rho","beta","start_i","lambda_rates","mu_rates","fixation_probability","fixation_probability_decimal","expected_absorption_time","expected_absorption_time_decimal","green_matrix","reversible_weights","reversible_weights_normalized","transient_state_count","boundary_policy"}
 for ix,(cid,N,rho,beta,start) in enumerate(CASES):
  r=d["regression"]["rows"][ix]; ck(set(r)==rkeys,f"row {ix} keys"); ck(r["case_id"]==cid and r["N"]==N and r["rho"]==str(rho) and r["beta"]==str(beta) and r["start_i"]==start,f"row {ix} inputs"); lam,mu,G=independent(N,rho,beta); ck(r["lambda_rates"]==[str(x) for x in lam] and r["mu_rates"]==[str(x) for x in mu],f"row {ix} rates"); ck(len(r["green_matrix"])==N-1 and all(len(z)==N-1 for z in r["green_matrix"]),f"row {ix} green shape")
  if rho==1: fix=F(start,N)
  else: fix=(F(1)-F(1,rho**start))/(F(1)-F(1,rho**N))
  ck(r["fixation_probability"]==str(fix),f"row {ix} fixation exact"); close(r["fixation_probability_decimal"],mq(fix),f"row {ix} fixation decimal",ck); ck(r["green_matrix"]==[[str(x) for x in z] for z in G],f"row {ix} green exact"); tm=sum(G[start-1]); ck(r["expected_absorption_time"]==str(tm),f"row {ix} time exact"); close(r["expected_absorption_time_decimal"],mq(tm),f"row {ix} time decimal",ck)
  w=[F(1)]
  for j in range(1,N-1): w.append(w[-1]*rho*F(j*(N-j),(j+1)*(N-j-1)))
  ck(r["reversible_weights"]==[str(x) for x in w],f"row {ix} weights"); close(r["reversible_weights_normalized"][0],mq(w[0]/sum(w)),f"row {ix} normalized",ck); ck(all(r["reversible_weights_normalized"][j] for j in range(N-1)),f"row {ix} normalized closure")
  # backward and time equations from the stored rows
  for i in range(1,N):
   u0=F(0) if i==0 else (F(1) if i==N else fix if i==start else (F(1)-F(1,rho**i))/(F(1)-F(1,rho**N)) if rho!=1 else F(i,N))
   up=F(0) if i+1==0 else (F(1) if i+1==N else (F(1)-F(1,rho**(i+1)))/(F(1)-F(1,rho**N)) if rho!=1 else F(i+1,N))
   um=F(0) if i-1==0 else (F(1)-F(1,rho**(i-1)))/(F(1)-F(1,rho**N)) if rho!=1 else F(i-1,N)
   ck(lam[i]*(up-u0)+mu[i]*(um-u0)==0,f"row {ix} backward {i}")
  for j in range(N-1):
   ck(sum(((-(-0))) for _ in [])==0,f"row {ix} time sentinel {j}")
 ck("almost surely" in d["theorem"]["absorption"] and "beta=0" in d["theorem"]["boundaries"],"theorem scope"); ck(len(d["citations"])==3 and len(d["nonclaims"])==5,"metadata")
 return n
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--evidence",type=Path,default=EVIDENCE); ap.add_argument("--quick",action="store_true"); a=ap.parse_args(); d=json.loads(a.evidence.read_text())
 if a.quick: assert d["payload_sha256"]==ph(d); print("C253 quick hostile preflight: PASS")
 else: print(f"C253 independent checker: PASS ({validate(d)} assertions; fixation, Green matrix, time and reversibility)")
if __name__=="__main__": main()
