#!/usr/bin/env python3
"""Producer-independent exact/numeric checker for HCS-C250."""
from __future__ import annotations
import argparse, json, re
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c250_ep_evidence.json"
SOURCE = "3ff451e904f8f063e88c40ef87f4697a6586b1a5"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"; EPOCH = 1788048000
mp.mp.dps = 95
NUM = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+|[eE][+-]?[0-9]+)$")
TOP = {"schema","candidate_id","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator","headline","frozen_object","theorem","regression","exact_identities","route_a","scope_flags","citations","nonclaims","payload_sha256"}
FLAGS = {"uses_target_zero_table","uses_prime_table","claims_arithmetic_local_data","claims_euler_factors","claims_root_numbers","claims_automorphy","claims_target_divisor_or_functional_equation","claims_hilbert_polya_operator","invokes_route_b"}
CASES = [("regular_1",F(1),F(1,4),F(1),F(0),F(1,7)),("regular_2",F(2),F(1),F(1),F(1,2),F(1,9)),("regular_3",F(3,2),F(2),F(2),F(-1,3),F(2,11)),("regular_4",F(1),F(4),F(1,2),F(2),F(1,5)),("regular_5",F(3),F(1,9),F(1,3),F(1,4),F(1,13)),("regular_6",F(5,2),F(3,2),F(3,2),F(-2,5),F(1,8)),("kappa_zero",F(1),F(0),F(2),F(1),F(1,6)),("equilibrium",F(2),F(1),F(1,2),F(0),F(1,10)),("equilibrium_2",F(3),F(4),F(2,3),F(0),F(1,12))]

def ph(d):
    b=dict(d); b.pop("payload_sha256",None)
    return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def q(s):
    n,d=(s.split("/",1)+["1"])[:2] if "/" in s else (s,"1")
    return F(int(n),int(d))
def mq(x): return mp.mpf(x.numerator)/x.denominator
def dstr(x): return mp.nstr(x,64,strip_zeros=False,min_fixed=-70,max_fixed=70)
def energy(w,k,x,v): return (v*v+w*w*x*x+k/(x*x))/2
def expected(w,k,x,v,t):
    a=x*x; b=x*v; c=v*v+k/(x*x); e=energy(w,k,x,v); disc=e*e-w*w*k
    wm,tm=mq(w),mq(t); u=mp.cos(wm*tm); z=mp.sin(wm*tm)/wm; up=-wm*mp.sin(wm*tm); zp=mp.cos(wm*tm)
    r=mq(a)*u*u+2*mq(b)*u*z+mq(c)*z*z; rp=2*mq(a)*u*up+2*mq(b)*(up*z+u*zp)+2*mq(c)*z*zp
    xx=mp.sqrt(r); vv=rp/(2*xx); ee=(vv*vv+wm*wm*xx*xx+mq(k)/(xx*xx))/2
    I=((u*vv-up*xx)**2+mq(k)*(u/xx)**2)/2
    sd=mp.sqrt(mq(disc)); xm=mp.sqrt((mq(e)-sd)/(wm*wm)); xp=mp.sqrt((mq(e)+sd)/(wm*wm)); act=mq(e)/(2*wm)-mp.sqrt(mq(k))/2
    return a,b,c,e,disc,xx,vv,ee,I,xm,xp,act

def close(actual, want, label, check, tol=mp.mpf("3e-40")):
    check(isinstance(actual,str) and NUM.fullmatch(actual) is not None,label+" syntax")
    if isinstance(actual,str) and NUM.fullmatch(actual): check(abs(mp.mpf(actual)-want)<=tol*max(1,abs(want)),label+" value")

def validate(data):
    n=0
    def ck(ok,label):
        nonlocal n; n+=1
        if not ok: raise AssertionError(label)
    ck(set(data)==TOP,"top closure"); ck(data["schema"]=="hcs-c250-ermakov-pinney-isotonic-v1","schema"); ck(data["candidate_id"]=="HCS-C250","candidate"); ck(data["source_commit"]==SOURCE,"source"); ck(data["fixed_epoch"]==EPOCH,"epoch"); ck(data["scope_literal"]==SCOPE,"scope"); ck(data["evaluator"]=={"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVAL},"evaluator"); ck(data["payload_sha256"]==ph(data),"payload hash")
    ck(data["route_a"]["tuple"]==["A0_FAIL","A1_PASS_ANALYTIC","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"],"tuple"); ck(data["route_a"]["overall"]=="ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False,"route verdict"); ck(set(data["scope_flags"])==FLAGS and all(v is False for v in data["scope_flags"].values()),"scope firewall")
    ck(data["regression"]["row_count"]==len(CASES)==9,"row count"); ck(len(data["regression"]["boundary_rows"])==4,"boundary count"); ck(len(data["exact_identities"])==10,"identity count")
    keys={"case_id","omega","kappa","x0","v0","time","a","b","c","energy","discriminant","ac_minus_b2","x_t","v_t","energy_t","turning_x_minus","turning_x_plus","period","action","ermakov_invariant","phase","regime"}
    for i,spec in enumerate(CASES):
        r=data["regression"]["rows"][i]; ck(set(r)==keys,f"row {i} keys"); cid,w,k,x,v,t=spec; ck(r["case_id"]==cid,f"row {i} id"); ck(r["omega"]==str(w) and r["kappa"]==str(k) and r["x0"]==str(x) and r["v0"]==str(v) and r["time"]==str(t),f"row {i} inputs")
        a,b,c,e,disc,xx,vv,ee,I,xm,xp,act=expected(w,k,x,v,t)
        ck(r["a"]==str(a) and r["b"]==str(b) and r["c"]==str(c) and r["energy"]==str(e),f"row {i} exact coefficients"); ck(r["discriminant"]==str(disc) and r["ac_minus_b2"]==str(a*c-b*b)==str(k),f"row {i} gram")
        close(r["x_t"],xx,f"row {i} x",ck); close(r["v_t"],vv,f"row {i} v",ck); close(r["energy_t"],ee,f"row {i} energy",ck); close(r["ermakov_invariant"],I,f"row {i} invariant",ck); close(r["turning_x_minus"],xm,f"row {i} xminus",ck); close(r["turning_x_plus"],xp,f"row {i} xplus",ck); close(r["action"],act,f"row {i} action",ck)
        if disc==0: ck(r["period"] is None and r["regime"]=="equilibrium",f"row {i} equilibrium")
        else: close(r["period"],mp.pi/mq(w),f"row {i} period",ck); ck(r["regime"]==("singular_kappa_zero" if k==0 else "oscillatory_positive"),f"row {i} regime")
    ck("quadratic_representation" in data["theorem"] and "no continuation" in data["theorem"]["boundaries"],"theorem scope")
    ck(len(data["citations"])==3 and all(set(c)>= {"key","claim","source"} for c in data["citations"]),"citation closure"); ck(len(data["nonclaims"])==5,"nonclaim closure")
    return n

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--evidence",type=Path,default=EVIDENCE); ap.add_argument("--quick",action="store_true"); a=ap.parse_args(); d=json.loads(a.evidence.read_text());
    if a.quick: assert d["payload_sha256"]==ph(d); print("C250 quick hostile preflight: PASS")
    else: print(f"C250 independent checker: PASS ({validate(d)} assertions; invariant, radial period/action, boundaries)")
if __name__=="__main__": main()
