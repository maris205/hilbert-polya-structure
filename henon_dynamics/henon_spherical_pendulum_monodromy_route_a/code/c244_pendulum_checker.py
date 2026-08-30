#!/usr/bin/env python3
"""Independent schema and numerical checker for HCS-C244.

This file intentionally duplicates the short algebraic/numerical derivations
instead of importing the producer.  It is therefore useful as a hostile
receipt checker as well as a regression test.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c244_pendulum_evidence.json"
SOURCE = "5f357e2d2b78604f6c286bfbd05da922e1d6791f"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000
mp.mp.dps = 100
NUM = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+|[eE][+-]?[0-9]+)$")
TOP = {"schema","candidate_id","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator","headline","frozen_object","theorem","regression","exact_identities","route_a","scope_flags","citations","nonclaims","payload_sha256"}
FLAGS = {"uses_target_zero_table","uses_prime_table","claims_arithmetic_local_data","claims_euler_factors","claims_root_numbers","claims_automorphy","claims_target_divisor_or_functional_equation","claims_hilbert_polya_operator","invokes_route_b"}
CASES = [("R01",F(-1,2),F(1,4)),("R02",F(0),F(1,10)),("R03",F(0),F(1,4)),("R04",F(1,4),F(1,10)),("R05",F(1,2),F(1,10)),("R06",F(3,4),F(1,20)),("R07",F(9,10),F(1,20)),("R08",F(1),F(1,100))]
CRIT_S = [F(-1,2),F(-1,3),F(-2,3),F(-3,4),F(-4,5)]
CRIT_KEYS = {"face_id","s","h","j_squared","discriminant","type","boundary_note"}
REG_KEYS = {"case_id","h","j","j_squared","root_count","roots","physical_interval","root_order","period_T","angle_increment_Delta_phi","action_I","quadrature_parameterization","regularity"}

def ph(data: dict) -> str:
    body=dict(data); body.pop("payload_sha256",None)
    return sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def qmp(q:F)->mp.mpf: return mp.mpf(q.numerator)/q.denominator
def qtxt(q:F)->str: return str(q.numerator) if q.denominator==1 else f"{q.numerator}/{q.denominator}"
def close(v, x, label, check, tol="2e-35"):
    check(isinstance(v,str) and NUM.fullmatch(v) is not None, label+" syntax")
    if isinstance(v,str) and NUM.fullmatch(v): check(abs(mp.mpf(v)-x)<=mp.mpf(tol)*max(1,abs(x)),label+" numeric")

def roots(h:mp.mpf,j:mp.mpf)->list[mp.mpf]:
    z=mp.polyroots([2,-2*h,-2,2*h-j*j],maxsteps=1200,error=False)
    r=sorted(mp.re(x) for x in z if abs(mp.im(x))<mp.mpf("1e-60"))
    if len(r)!=3: raise AssertionError("three real roots")
    return r

def quad(h:F,j:F):
    hh,jj=qmp(h),qmp(j); r1,r2,r3=roots(hh,jj); m=(r1+r2)/2; d=(r2-r1)/2
    def u(t): return m+d*mp.cos(t)
    def den(t): return mp.sqrt(2*(r3-u(t)))
    T=2*mp.quad(lambda t:1/den(t),[0,mp.pi])
    D=2*jj*mp.quad(lambda t:1/((1-u(t)**2)*den(t)),[0,mp.pi])
    I=mp.quad(lambda t:d*d*mp.sin(t)**2*den(t)/(1-u(t)**2),[0,mp.pi])/mp.pi
    return r1,r2,r3,T,D,I

def validate(data:dict)->int:
    n=0
    def ck(ok,label):
        nonlocal n; n+=1
        if not ok: raise AssertionError(label)
    def ex(a,b,label): ck(type(a) is type(b) and a==b,label)
    ck(set(data)==TOP,"top-level closure")
    for key,val in (("schema","hcs-c244-spherical-pendulum-monodromy-v1"),("candidate_id","HCS-C244"),("evaluation_date","2026-08-30"),("source_commit",SOURCE),("scope_literal",SCOPE)): ex(data[key],val,key)
    ex(data["fixed_epoch"],EPOCH,"epoch"); ex(data["evaluator"],{"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVAL},"evaluator")
    ex(data["payload_sha256"],ph(data),"payload hash")
    ex(data["route_a"]["tuple"],["A0_FAIL","A1_PASS_ANALYTIC","A2_FAIL","A3_FAIL","A4_NATURAL_QUANTIZATION"],"route tuple")
    ex(data["route_a"]["overall"],"ROUTE_A_REJECTED","route verdict"); ex(data["route_a"]["route_b_invocation_allowed"],False,"route B")
    ck(set(data["scope_flags"])==FLAGS,"scope key closure"); ck(all(v is False for v in data["scope_flags"].values()),"scope all false")
    for phrase in ("physical interval","focus-focus","Liouville","Delta_phi/(2*pi)=p/q","No elementary closed form"):
        ck(phrase in json.dumps(data["theorem"],ensure_ascii=False),"theorem phrase "+phrase)
    ex(data["theorem"]["monodromy"],"With the declared oriented basis and a positive loop around the isolated focus-focus value, M=[[1,1],[0,1]].","theorem monodromy")
    ex(data["regression"]["working_digits"],90,"working precision"); ex(data["regression"]["serialized_digits"],64,"serialized precision")
    fixed=data["regression"]["fixed_rows"]; ex(len(fixed),2,"fixed count")
    fk={"point_id","theta","u","j","h","singularity_type","chart"}
    expected=[("bottom","pi","-1","0","-1","elliptic-elliptic"),("top","0","1","0","1","focus-focus")]
    for i,(pid,th,u,j,h,typ) in enumerate(expected):
        ck(set(fixed[i])==fk,f"fixed {i} keys")
        for k,v in (("point_id",pid),("theta",th),("u",u),("j",j),("h",h),("singularity_type",typ),("chart","global_vector")): ex(fixed[i][k],v,f"fixed {i} {k}")
    crit=data["regression"]["critical_rows"]; ex(len(crit),7,"critical count")
    ck(crit[0]["face_id"]=="bottom_elliptic_endpoint" and crit[1]["face_id"]=="top_focus_focus_endpoint","endpoint order")
    for i,s in enumerate(CRIT_S,2):
        row=crit[i]; ck(set(row)==CRIT_KEYS,f"critical {i} keys"); ex(row["face_id"],"interior_double_root",f"critical {i} id"); ex(row["s"],qtxt(s),f"critical {i} s"); h=(3*s*s-1)/(2*s); q=(1-s*s)**2/(-s); ex(row["h"],qtxt(h),f"critical {i} h"); ex(row["j_squared"],qtxt(q),f"critical {i} j2"); ex(row["discriminant"],"0",f"critical {i} disc"); ex(row["type"],"elliptic critical circle",f"critical {i} type"); ck("P(s)=P'(s)=0" in row["boundary_note"],f"critical {i} note")
    reg=data["regression"]["regular_rows"]; ex(len(reg),len(CASES),"regular count")
    for i,(cid,h,j) in enumerate(CASES):
        row=reg[i]; ck(set(row)==REG_KEYS,f"regular {i} keys"); ex(row["case_id"],cid,f"regular {i} id"); ex(row["h"],qtxt(h),f"regular {i} h"); ex(row["j"],qtxt(j),f"regular {i} j"); ex(row["j_squared"],qtxt(j*j),f"regular {i} j2"); ex(row["root_count"],3,f"regular {i} root count"); ck(row["roots"] and len(row["roots"])==3,f"regular {i} root list")
        rr1,rr2,rr3,tval,dval,ival=quad(h,j); rr=(rr1,rr2,rr3); vals=row["roots"]
        for k,x in enumerate(rr): close(vals[k],x,f"regular {i} root{k}",ck,"2e-35")
        ck(rr[0]<rr[1]<1<rr[2] and rr[0]>-1,f"regular {i} root order")
        for k,x in enumerate(rr): ck(abs(2*(1-x*x)*(qmp(h)-x)-qmp(j*j))<mp.mpf("2e-35"),f"regular {i} residual{k}")
        close(row["period_T"],tval,f"regular {i} T",ck); close(row["angle_increment_Delta_phi"],dval,f"regular {i} Delta",ck); close(row["action_I"],ival,f"regular {i} action",ck)
        for k,v in (("physical_interval","(r1,r2) subset (-1,1); r3>1"),("root_order","r1<r2<1<r3"),("quadrature_parameterization","u=(r1+r2)/2+(r2-r1)cos(theta)/2, theta in [0,pi]"),("regularity","discriminant nonzero; j!=0")): ex(row[k],v,f"regular {i} {k}")
    ex(data["regression"]["critical_row_count"],7,"critical summary"); ex(data["regression"]["regular_row_count"],8,"regular summary"); ex(data["regression"]["fixed_row_count"],2,"fixed summary")
    mon=data["regression"]["monodromy"]; ex(mon,{"matrix":[[1,1],[0,1]],"loop_orientation":"positive counterclockwise around (h,j)=(1,0)","basis":"alpha=vanishing cycle, beta=transported complementary cycle","matrix_convention":"columns_are_transported_basis_vectors_in_initial_basis","transport_receipt":"beta_final=beta_initial+alpha_initial","determinant":1},"monodromy")
    ck(len(data["exact_identities"])==10,"identity count"); ck(any(x.get("identity_id")=="torus_closure" for x in data["exact_identities"]),"closure identity"); ck(len(data["citations"])==2,"citation count"); ck(data["citations"][0]["url"]=="https://doi.org/10.1090/S0273-0979-1988-15705-9","citation 0 DOI"); ck(data["citations"][1]["url"]=="https://doi.org/10.1016/j.jde.2013.01.018","citation 1 DOI"); ck(len(data["nonclaims"])==5,"nonclaim count")
    return n

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--evidence",type=Path,default=DEFAULT); ap.add_argument("--quick",action="store_true"); a=ap.parse_args(); d=json.loads(a.evidence.read_text())
    if a.quick:
        assert set(d)==TOP and d["candidate_id"]=="HCS-C244" and d["payload_sha256"]==ph(d); print("C244 quick hostile preflight: PASS")
    else: print(f"C244 independent checker: PASS ({validate(d)} assertions; cubic, chambers, quadratures, monodromy)")
if __name__=="__main__": main()
