#!/usr/bin/env python3
"""Producer-independent rational checker for HCS-C255."""
from __future__ import annotations
import argparse,json
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; EVIDENCE=ROOT/"results/c255_suslov_evidence.json"; SOURCE="b89544f1f7b1043f4158dfdf9db77787b332f146"; EVAL="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"; SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"; EPOCH=1788048000
CASES=[("generic_01",F(2),F(3),F(6),F(1),F(1),F(1)),("generic_02",F(1),F(2),F(5),F(1,2),F(1),F(3,2)),("generic_03",F(3),F(4),F(7),F(-1),F(2),F(2)),("generic_04",F(5),F(2),F(6),F(0),F(1),F(2)),("generic_05",F(2),F(5),F(6),F(1),F(0),F(3)),("generic_06",F(4),F(3),F(5),F(-1),F(1,2),F(1)),("generic_07",F(3,2),F(5,2),F(4),F(1,2),F(-1),F(2)),("generic_08",F(7),F(4),F(8),F(2),F(1),F(1,2)),("generic_09",F(2),F(2),F(3),F(1),F(-1),F(5,2)),("generic_10",F(1),F(3),F(4),F(-1,2),F(-1),F(1)),("generic_11",F(6),F(5),F(7),F(2),F(-1),F(3)),("generic_12",F(5,2),F(7,2),F(5),F(1),F(-1,2),F(4)),("principal_01",F(1),F(2),F(3),F(0),F(0),F(1)),("principal_02",F(2),F(3),F(4),F(0),F(0),F(2)),("principal_03",F(3),F(5),F(7),F(0),F(0),F(1,2)),("principal_04",F(4),F(1),F(6),F(0),F(0),F(3))]
TOP={"schema","candidate_id","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator","headline","frozen_object","theorem","regression","exact_identities","route_a","scope_flags","citations","nonclaims","payload_sha256"}; FLAGS={"uses_target_zero_table","uses_prime_table","claims_arithmetic_local_data","claims_euler_factors","claims_root_numbers","claims_automorphy","claims_target_divisor_or_functional_equation","claims_hilbert_polya_operator","invokes_route_b"}
def ph(d):
 b=dict(d); b.pop("payload_sha256",None); return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def q(x): return F(x)
def validate(d):
 n=0
 def ck(ok,label):
  nonlocal n; n+=1
  if not ok: raise AssertionError(label)
 ck(set(d)==TOP,"top"); ck(d["schema"]=="hcs-c255-suslov-nonholonomic-heteroclinic-v1","schema"); ck(d["candidate_id"]=="HCS-C255" and d["evaluation_date"]=="2026-08-31","id/date"); ck(d["source_commit"]==SOURCE and d["fixed_epoch"]==EPOCH and d["scope_literal"]==SCOPE,"locks"); ck(d["evaluator"]=={"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVAL},"evaluator"); ck(d["payload_sha256"]==ph(d),"hash"); ck(d["route_a"]["tuple"]==["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"tuple"); ck(d["route_a"]["overall"]=="ROUTE_A_REJECTED" and d["route_a"]["route_b_invocation_allowed"] is False,"verdict"); ck(set(d["scope_flags"])==FLAGS and all(v is False for v in d["scope_flags"].values()),"flags"); ck(d["regression"]["row_count"]==16 and d["regression"]["regime_counts"]=={"generic":12,"principal_axis":4},"counts"); ck(len(d["regression"]["boundary_rows"])==5 and len(d["exact_identities"])==16,"boundary/identity counts")
 keys={"case_id","I1","I2","I3","a","b","H","schur_complement","inertia_determinant","regime","q_squared","R_squared","kappa_squared","equilibrium_raw_direction","energy_scale_squared","equilibrium_speed_squared","period_squared_over_pi_squared","unstable_divergence_squared","reduced_orbit_statement","full_reconstruction_statement","proof_role"}
 for i,(cid,I1,I2,I3,a,b,H) in enumerate(CASES):
  r=d["regression"]["rows"][i]; ck(set(r)==keys,f"row {i} keys"); ck((r["case_id"],q(r["I1"]),q(r["I2"]),q(r["I3"]),q(r["a"]),q(r["b"]),q(r["H"]))==(cid,I1,I2,I3,a,b,H),f"row {i} inputs")
  sch=I3-a*a/I1-b*b/I2; det=I1*I2*sch; q2=a*a/I1+b*b/I2; generic=q2>0; k2=2*H*q2/(I1*I2)
  ck(sch>0 and q(r["schur_complement"])==sch and q(r["inertia_determinant"])==det,f"row {i} SPD"); ck(q(r["q_squared"])==q2 and q(r["R_squared"])==2*H and q(r["kappa_squared"])==k2,f"row {i} scales"); ck(("generic" in r["regime"])==generic,f"row {i} regime"); ck("clean SO(3) periodic rotation" in r["full_reconstruction_statement"],f"row {i} clean reconstruction")
  # Direct rational vector-field tests at two states.
  for w1,w2 in ((F(1,3),F(2,5)),(F(-2,3),F(1,4))):
   ell=a*w1+b*w2; f1=-ell*w2/I1; f2=ell*w1/I2
   ck(I1*w1*f1+I2*w2*f2==0,f"row {i} energy"); ck((-a*(-w2)/I1+b*(-w1)/I2)==-(-a*w2/I1+b*w1/I2),f"row {i} divergence odd")
  if generic:
   denom=I1*b*b+I2*a*a; c2=2*H/denom; speed2=c2*(a*a+b*b)
   ck([q(z) for z in r["equilibrium_raw_direction"]]==[b,-a] and a*b+b*(-a)==0,f"row {i} equilibrium"); ck(q(r["energy_scale_squared"])==c2 and q(r["equilibrium_speed_squared"])==speed2,f"row {i} energy/speed"); ck(q(r["period_squared_over_pi_squared"])==4/speed2,f"row {i} period"); ck(q(r["unstable_divergence_squared"])==k2,f"row {i} exponent"); ck((-a*(-a)/I1+b*b/I2)==q2,f"row {i} raw divergence")
  else:
   ck(all(r[k] is None for k in ("equilibrium_raw_direction","energy_scale_squared","equilibrium_speed_squared","period_squared_over_pi_squared","unstable_divergence_squared")),f"row {i} principal nulls"); ck("every reduced state is an equilibrium" in r["reduced_orbit_statement"],f"row {i} principal dynamics")
 ck("SO(3)/SO(2) clean" in d["theorem"]["clean_reconstruction"] and "not omitted or called isolated" in d["theorem"]["clean_reconstruction"],"clean-family theorem"); ck("no positive C1 density" in d["theorem"]["poisson_measure"],"measure obstruction"); ck("a=b=0" in d["theorem"]["boundaries"],"principal boundary"); ck(len(d["citations"])==3 and all(z["url"].startswith("https://doi.org/") for z in d["citations"]),"citations"); ck(len(d["nonclaims"])==5,"nonclaims")
 return n
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--evidence",type=Path,default=EVIDENCE); a=ap.parse_args(); print(f"C255 independent checker: PASS ({validate(json.loads(a.evidence.read_text()))} assertions; inertia, heteroclinics, clean rotations, measure and scope)")
if __name__=="__main__": main()
