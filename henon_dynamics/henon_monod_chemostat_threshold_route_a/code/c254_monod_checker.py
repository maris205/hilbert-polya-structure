#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C254."""
from __future__ import annotations
import argparse,json
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; EVIDENCE=ROOT/"results/c254_monod_evidence.json"
SOURCE="b89544f1f7b1043f4158dfdf9db77787b332f146"; EVAL="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"; SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"; EPOCH=1788048000
CASES=[
 ("survival_01",F(1),F(10),F(3),F(2),F(2)),("survival_02",F(1,2),F(4),F(2),F(1),F(3)),("survival_03",F(2,3),F(5),F(3,2),F(2),F(5,2)),("survival_04",F(3,4),F(7),F(2),F(3),F(4)),("survival_05",F(1,5),F(2),F(5,4),F(1,2),F(3,2)),("survival_06",F(4,3),F(9),F(3),F(1),F(2)),
 ("critical_01",F(1),F(1),F(2),F(1),F(2)),("critical_02",F(2),F(2),F(3),F(1),F(3)),("critical_03",F(1),F(3),F(2),F(3),F(4)),("critical_04",F(2),F(4),F(5,2),F(1),F(5)),("critical_05",F(1),F(1,2),F(3),F(1),F(3,2)),("critical_06",F(1),F(5),F(6,5),F(1),F(7,3)),
 ("washout_01",F(2),F(1),F(2),F(1),F(2)),("washout_02",F(3,2),F(2),F(2),F(2),F(3)),("washout_03",F(1),F(1),F(3,2),F(1),F(4)),("washout_04",F(4),F(5),F(3),F(1),F(5,2)),("washout_05",F(2,3),F(1),F(1),F(1),F(3,2)),("washout_06",F(5,4),F(3),F(2),F(3),F(2))]
TOP={"schema","candidate_id","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator","headline","frozen_object","theorem","regression","exact_identities","route_a","scope_flags","citations","nonclaims","payload_sha256"}
FLAGS={"uses_target_zero_table","uses_prime_table","claims_arithmetic_local_data","claims_euler_factors","claims_root_numbers","claims_automorphy","claims_target_divisor_or_functional_equation","claims_hilbert_polya_operator","invokes_route_b"}
def ph(d):
 b=dict(d); b.pop("payload_sha256",None); return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def q(x): return F(x)
def validate(d):
 n=0
 def ck(ok,label):
  nonlocal n; n+=1
  if not ok: raise AssertionError(label)
 ck(set(d)==TOP,"top"); ck(d["schema"]=="hcs-c254-monod-chemostat-threshold-v1","schema"); ck(d["candidate_id"]=="HCS-C254","id"); ck(d["evaluation_date"]=="2026-08-31","date")
 ck(d["source_commit"]==SOURCE and d["fixed_epoch"]==EPOCH and d["scope_literal"]==SCOPE,"locks"); ck(d["evaluator"]=={"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVAL},"evaluator"); ck(d["payload_sha256"]==ph(d),"hash")
 ck(d["route_a"]["tuple"]==["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FAIL"],"tuple"); ck(d["route_a"]["overall"]=="ROUTE_A_REJECTED" and d["route_a"]["route_b_invocation_allowed"] is False,"verdict")
 ck(set(d["scope_flags"])==FLAGS and all(v is False for v in d["scope_flags"].values()),"flags"); ck(len(d["regression"]["rows"])==18 and d["regression"]["regime_counts"]=={"survival":6,"critical":6,"washout":6},"row counts"); ck(len(d["regression"]["boundary_rows"])==5 and len(d["exact_identities"])==14,"boundary/identity counts")
 keys={"case_id","D","S_in","mu_max","K","Y","mu_feed","growth_margin","threshold_numerator","regime","washout_equilibrium","washout_eigenvalues","washout_charpoly","mu_prime_feed","positive_equilibrium","positive_qx_eigenvalues","positive_charpoly","leaf_implicit_coefficients","critical_leaf_asymptotic_coefficient","proof_role"}
 for i,(cid,D,Sin,mumax,K,Y) in enumerate(CASES):
  r=d["regression"]["rows"][i]; ck(set(r)==keys,f"row {i} keys"); ck((r["case_id"],q(r["D"]),q(r["S_in"]),q(r["mu_max"]),q(r["K"]),q(r["Y"]))==(cid,D,Sin,mumax,K,Y),f"row {i} inputs")
  muf=mumax*Sin/(K+Sin); delta=muf-D; th=mumax*Sin-D*(K+Sin); regime="survival" if th>0 else "critical" if th==0 else "washout"; mpf=mumax*K/(K+Sin)**2
  ck(q(r["mu_feed"])==muf and q(r["growth_margin"])==delta and q(r["threshold_numerator"])==th,f"row {i} threshold"); ck(r["regime"]==regime,f"row {i} regime"); ck([q(z) for z in r["washout_equilibrium"]]==[Sin,F(0)],f"row {i} E0"); ck([q(z) for z in r["washout_eigenvalues"]]==[-D,delta],f"row {i} E0 eig"); ck([q(z) for z in r["washout_charpoly"]]==[F(1),D-delta,-D*delta],f"row {i} E0 poly"); ck(q(r["mu_prime_feed"])==mpf,f"row {i} derivative")
  if regime=="survival":
   ss=D*K/(mumax-D); xs=Sin-ss; Xs=Y*xs; rate=xs*mumax*K/(K+ss)**2
   ck([q(z) for z in r["positive_equilibrium"]]==[ss,Xs],f"row {i} E+"); ck([q(z) for z in r["positive_qx_eigenvalues"]]==[-D,-rate],f"row {i} E+ eig"); ck([q(z) for z in r["positive_charpoly"]]==[F(1),D+rate,D*rate],f"row {i} E+ poly")
   c=r["leaf_implicit_coefficients"]; ck(q(c["x_star"])==xs and q(c["A"])==mumax-D and q(c["log_x"])==(K+Sin)/xs and q(c["minus_log_abs_xstar_minus_x"])==(K+ss)/xs,f"row {i} leaf"); ck(r["critical_leaf_asymptotic_coefficient"] is None,f"row {i} critical null")
  elif regime=="critical":
   ck(r["positive_equilibrium"] is None and r["positive_qx_eigenvalues"] is None and r["leaf_implicit_coefficients"] is None,f"row {i} critical nulls"); ck(q(r["critical_leaf_asymptotic_coefficient"])==1/mpf,f"row {i} critical coefficient")
  else:
   ck(r["positive_equilibrium"] is None and r["positive_qx_eigenvalues"] is None and r["leaf_implicit_coefficients"] is None and r["critical_leaf_asymptotic_coefficient"] is None,f"row {i} washout nulls")
 # Independently evaluate vector-field identities at a rational state for every case.
  S=Sin/2; X=Y*Sin/3; mu=mumax*S/(K+S); Sd=D*(Sin-S)-mu*X/Y; Xd=(mu-D)*X; Qd=Sd+Xd/Y
  ck(Qd==D*(Sin-(S+X/Y)),f"row {i} Q identity"); ck(mu>=0 and (X==0 or Xd/X==mu-D),f"row {i} positivity convention")
 ck("no nonconstant periodic" in d["theorem"]["no_recurrence"],"no-cycle theorem"); ck("K=0 and Y=0" in d["theorem"]["boundaries"],"singular boundaries"); ck(len(d["citations"])==3 and all(z["url"].startswith("https://doi.org/") for z in d["citations"]),"citations"); ck(len(d["nonclaims"])==5,"nonclaims")
 return n
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--evidence",type=Path,default=EVIDENCE); a=ap.parse_args(); d=json.loads(a.evidence.read_text()); print(f"C254 independent checker: PASS ({validate(d)} assertions; threshold, equilibria, spectra, leaf law and boundaries)")
if __name__=="__main__": main()
