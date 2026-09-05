#!/usr/bin/env python3
"""Exact rational complex producer; no target data and no sampled PDE definition."""
if not __debug__: raise RuntimeError("c386 producer refuses optimized Python")
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
YAML=ROOT/"evaluations/route_a/HCS-C386/2026-09-05.yaml"
YAML_SHA="f8c7b832fc5756a6e6adcaf7ad6369648e2fadf97d357347d4e762012649687e"
def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def q(x):
    x=F(x); return [x.numerator,x.denominator]
def z(a=0,b=0): return (F(a),F(b))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,k): return (a[0]*k,a[1]*k)
def conj(a): return (a[0],-a[1])
def norm(a): return a[0]*a[0]+a[1]*a[1]
def enc(a): return [q(a[0]),q(a[1])]
def velocity(a,b,c,p):
    B,C,d=norm(b),norm(c),1-norm(p)
    vb=add(scale(b,B+2*C/d+a),scale(mul(c,conj(p)),C/d**2))
    vc=add(scale(c,2*B+C/d**2),scale(mul(b,p),2*C/d))
    vp=add(mul(c,conj(b)),scale(p,C/d))
    return tuple(mul(z(0,-1),v) for v in (vb,vc,vp))
def row(a,b,c,p):
    B,C,P=norm(b),norm(c),norm(p);d=1-P;X=mul(mul(b,p),conj(c))
    Q=B+C/d;M=C/d**2
    E=(B*B+4*B*C/d+C*C*(1+P)/d**3+4*C*X[0]/d**2)/4+a*B/2
    delta=E-Q*Q/4-a*Q/2
    vb,vc,vp=velocity(a,b,c,p)
    d1=-2*mul(vp,conj(p))[0]
    X1=add(add(mul(mul(vb,p),conj(c)),mul(mul(b,vp),conj(c))),mul(mul(b,p),conj(vc)))
    d2=2*X1[1]
    k2=4*Q*M-(a-Q-M)**2
    kind="cascade" if a>0 and delta==0 else "inner_phase" if a==0 and delta==0 else "compact"
    lower=2*abs(delta)/(M*(2*(Q+M)+abs(a))) if delta else F(0)
    return dict(alpha=q(a),b=enc(b),c=enc(c),p=enc(p),d=q(d),Q=q(Q),M=q(M),energy=q(E),defect=q(delta),
                velocity=[enc(v) for v in (vb,vc,vp)],d_dot=q(d1),d_ddot=q(d2),
                kappa_squared=q(k2),d_star=q(k2/(4*a*M)) if kind=="cascade" else None,
                compact_lower_bound=q(lower),regime=kind,native_determinant_coefficients=[q(1),q(-M)])
def grids():
    alphas=[F(-2),F(-1),F(0),F(1,4),F(1),F(4)]
    bs=[z(),z(1),z(0,1),z(F(1,2),F(1,2))]
    cs=[z(F(1,2)),z(F(1,3),F(1,3))]
    ps=[z(),z(F(1,3)),z(0,F(1,2))]
    generic=[row(a,b,c,p) for a in alphas for b in bs for c in cs for p in ps]
    cascade=[]
    for a in (F(1,2),F(1),F(2)):
      for m in (F(1,2),F(1)):
       for eta in (z(1),z(0,1)):
        for phase in (z(1),z(F(3,5),F(4,5))):
         for p in ps:
            d=1-norm(p);c=scale(eta,m*d)
            b=sub(scale(phase,a),scale(mul(eta,conj(p)),m))
            cascade.append(row(a*a,b,c,p))
    inner=[]
    for m in (F(1,2),F(1)):
      for eta in (z(1),z(0,1)):
       for p in ps:
        A=scale(eta,m);d=1-norm(p)
        inner.append(row(F(0),neg(mul(A,conj(p))),scale(A,d),p))
    constants=[]
    for a in alphas:
      for b in bs:
        Q=norm(b);frequency=Q+a
        constants.append(dict(alpha=q(a),b=enc(b),Q=q(Q),energy=q(Q*Q/4+a*Q/2),
             defect=q(0),frequency=q(frequency),stationary=(Q==0 or frequency==0),
             rank=0,cascade=False))
    controls=[]
    for a in (F(1,4),F(1),F(4)):
        root={F(1,4):F(1,2),F(1):F(1),F(4):F(2)}[a]
        controls.append(dict(alpha=q(a),bounded=row(a,z(),z(1),z()),cascade=row(a,z(root),z(1),z())))
    return generic,cascade,inner,constants,controls
def build():
    raw=YAML.read_bytes();assert hashlib.sha256(raw).hexdigest()==YAML_SHA
    ev=yaml.safe_load(raw)
    generic,cascade,inner,constants,controls=grids()
    data=dict(schema="hcs-c386-szego-v1",candidate_id="HCS-C386",obstruction_id="HEN-O370",
       source_commit="3e692da6fa94362225c7534e9b66c83c15c7f284",fixed_epoch=1788566400,
       scope_literal="NO_BAD_EULER_OR_ROOT_NUMBER",scope_flags=ev["scope_flags"],
       evaluator=dict(authority="flow_systems/skills/route-a-evaluator.md",version="0.2.0",
         sha256="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"),
       route_a_yaml=dict(path="evaluations/route_a/HCS-C386/2026-09-05.yaml",raw_sha256=YAML_SHA,
                         semantic_sha256=hashlib.sha256(canon(ev)).hexdigest()),
       route_a=dict(tuple=ev["tuple"],overall_verdict="ROUTE_A_REJECTED",route_b_invocation_allowed=False),
       generic_rows=generic,cascade_rows=cascade,inner_rows=inner,constant_rows=constants,control_rows=controls,
       counts=dict(generic=len(generic),cascade=len(cascade),inner=len(inner),constants=len(constants),controls=len(controls)),
       theorem_boundary="Rank one only; constants separately; physical time unchanged; finite rational checks are regression, not all-mode proofs; auxiliary K squared determinant is not time evolution; no target arithmetic or Route B")
    data["payload_sha256"]=hashlib.sha256(canon(data)).hexdigest()
    return data
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=ROOT/"results/c386_szego_evidence.json");a=p.parse_args()
    data=build();a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_bytes(json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False,allow_nan=False).encode()+b"\n")
    print("C386 producer PASS",data["payload_sha256"],data["counts"])
if __name__=="__main__":main()
