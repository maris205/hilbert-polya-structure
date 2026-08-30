#!/usr/bin/env python3
"""Independent checker for the frozen hysteretic relay certificate."""
from __future__ import annotations
import argparse,json,re
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1]
EVIDENCE=ROOT/"results/c252_relay_evidence.json"
SOURCE="3ff451e904f8f063e88c40ef87f4697a6586b1a5"
EVAL="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"; EPOCH=1788048000; mp.mp.dps=95
CASES=[("contracting_a",F(1,2),F(1),F(3,2)),("contracting_b",F(2),F(3,4),F(-2)),("neutral",F(3,2),F(0),F(5,3)),("small_h",F(1,5),F(7,3),F(1,7)),("large_h",F(5,2),F(1,5),F(-3,2)),("zero_y",F(1),F(2),F(0)),("rational_decay",F(3,4),F(2),F(4,3)),("boundary_grazing",F(1),F(1),F(1))]
TOP={"schema","candidate_id","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator","headline","frozen_object","theorem","regression","exact_identities","route_a","scope_flags","citations","nonclaims","payload_sha256"}
FLAGS={"uses_target_zero_table","uses_prime_table","claims_arithmetic_local_data","claims_euler_factors","claims_root_numbers","claims_automorphy","claims_target_divisor_or_functional_equation","claims_hilbert_polya_operator","invokes_route_b"}; NUM=re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+|[eE][+-]?[0-9]+)$")
def ph(d):
 b=dict(d); b.pop("payload_sha256",None); return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def mq(x):
 q=x if isinstance(x,F) else F(x); return mp.mpf(q.numerator)/q.denominator
def close(v,w,label,ck):
 ck(isinstance(v,str) and NUM.fullmatch(v) is not None,label+" syntax")
 if isinstance(v,str) and NUM.fullmatch(v): ck(abs(mp.mpf(v)-w)<=mp.mpf("4e-40")*max(1,abs(w)),label)
def validate(d):
 n=0
 def ck(ok,l):
  nonlocal n; n+=1
  if not ok: raise AssertionError(l)
 ck(set(d)==TOP,"top"); ck(d["schema"]=="hcs-c252-hysteretic-relay-v1","schema"); ck(d["candidate_id"]=="HCS-C252","id"); ck(d["source_commit"]==SOURCE and d["fixed_epoch"]==EPOCH and d["scope_literal"]==SCOPE,"lock"); ck(d["evaluator"]=={"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVAL},"evaluator"); ck(d["payload_sha256"]==ph(d),"hash")
 ck(d["route_a"]["tuple"]==["A0_FAIL","A1_PASS_ANALYTIC","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"tuple"); ck(d["route_a"]["overall"]=="ROUTE_A_REJECTED" and d["route_a"]["route_b_invocation_allowed"] is False,"verdict"); ck(set(d["scope_flags"])==FLAGS and all(v is False for v in d["scope_flags"].values()),"scope")
 ck(len(d["regression"]["rows"])==8 and len(d["regression"]["boundary_rows"])==4,"counts"); ck(len(d["exact_identities"])==10,"identities")
 rkeys={"case_id","h","gamma","y0","left_section","right_section","leg_time","full_period","leg_rows","cycle","half_multiplier","full_multiplier","guard_policy","grazing"}; lkeys={"leg","start_theta","end_theta","sigma","duration","y_start","y_end","decay_factor","guard"}; ckeys={"h","gamma","y0","full_period","return_theta","return_sigma","y_return","poincare_multiplier","fixed_periodic_y","nonzero_contraction"}
 for i,(cid,h,g,y) in enumerate(CASES):
  r=d["regression"]["rows"][i]; ck(set(r)==rkeys,f"row {i} keys"); ck(r["case_id"]==cid and r["h"]==str(h) and r["gamma"]==str(g) and r["y0"]==str(y),f"row {i} inputs"); ck(r["left_section"]==str(-h) and r["right_section"]==str(h) and r["leg_time"]==str(2*h) and r["full_period"]==str(4*h),f"row {i} geometry"); ck(set(r["cycle"])==ckeys,f"row {i} cycle keys"); close(r["half_multiplier"],mp.e**(-mq(g)*mq(2*h)),f"row {i} half",ck); close(r["full_multiplier"],mp.e**(-mq(g)*mq(4*h)),f"row {i} full",ck); close(r["cycle"]["y_return"],mq(y)*mp.e**(-mq(g)*mq(4*h)),f"row {i} return",ck); close(r["cycle"]["poincare_multiplier"],mp.e**(-mq(g)*mq(4*h)),f"row {i} multiplier",ck); ck(r["cycle"]["full_period"]==str(4*h) and r["cycle"]["return_theta"]==str(-h) and r["cycle"]["return_sigma"]==1,f"row {i} cycle geometry"); ck(r["grazing"]==(y==0),f"row {i} grazing")
  legs=r["leg_rows"]; ck(len(legs)==2 and all(set(z)==lkeys for z in legs),f"row {i} leg closure"); ck(legs[0]["sigma"]==1 and legs[1]["sigma"]==-1,f"row {i} signs"); ck(legs[0]["start_theta"]==str(-h) and legs[0]["end_theta"]==str(h) and legs[1]["start_theta"]==str(h) and legs[1]["end_theta"]==str(-h),f"row {i} guards"); ck(legs[0]["duration"]==str(2*h) and legs[1]["duration"]==str(2*h),f"row {i} durations"); close(legs[0]["y_end"],mq(y)*mp.e**(-mq(g)*mq(2*h)),f"row {i} leg0 y",ck); close(legs[1]["y_end"],mq(y)*mp.e**(-mq(g)*mq(4*h)),f"row {i} leg1 y",ck)
 ck("unique forward" in d["theorem"]["wellposedness"] and "Zeno" in d["theorem"]["no_zeno"],"theorem boundary"); ck(len(d["citations"])==3 and len(d["nonclaims"])==5,"metadata")
 return n
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--evidence",type=Path,default=EVIDENCE); ap.add_argument("--quick",action="store_true"); a=ap.parse_args(); d=json.loads(a.evidence.read_text())
 if a.quick: assert d["payload_sha256"]==ph(d); print("C252 quick hostile preflight: PASS")
 else: print(f"C252 independent checker: PASS ({validate(d)} assertions; exact relay map and no-Zeno bound)")
if __name__=="__main__": main()
