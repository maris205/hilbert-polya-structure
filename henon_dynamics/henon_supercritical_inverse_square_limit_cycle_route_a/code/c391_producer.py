#!/usr/bin/env python3
"""Canonical exact identities and declared finite special-function receipts."""
if not __debug__: raise RuntimeError("c391 producer refuses optimized Python")
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp
import yaml
ROOT=Path(__file__).resolve().parents[1]
YAML=ROOT/"evaluations/route_a/HCS-C391/2026-09-05.yaml"
YAML_SHA="93de77babcb16fc698d687a35584124eb110a3fba10ce454c77abcd9b8197bbb"
BASE="0c877206d202f732e21ea0b194f9c7fdf30467ee"
AUTH="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def q(x):
    x=F(x);return [x.numerator,x.denominator]
def zz(a,b=0):return F(a),F(b)
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def div(a,b):
    z=mul(a,(b[0],-b[1]));n=b[0]**2+b[1]**2;return z[0]/n,z[1]/n
def enc(z):return [q(z[0]),q(z[1])]
def norm(z):return z[0]**2+z[1]**2
def dec(x):return mp.nstr(x,60,strip_zeros=False)
def cdec(z):return [dec(mp.re(z)),dec(mp.im(z))]
def exact_rows():
    sigmas=(F(1,2),F(1),F(2));units=(zz(1),zz(-1),zz(0,1),zz(0,-1),zz(F(3,5),F(4,5)))
    classical=[]
    for s in sigmas:
      for x in (F(1,2),F(1),F(2)):
       for p in map(F,(-2,-1,0,1,2)):
        g=s*s+F(1,4);e=p*p-g/(x*x);poly=(x*x,4*x*p,4*e)
        classical.append(dict(sigma=q(s),x=q(x),p=q(p),g=q(g),energy=q(e),y_coefficients=list(map(q,poly)),
          discriminant=q(poly[1]**2-4*poly[0]*poly[2]),finite_collision=True,periodic=False,
          clock_component="bounded_interval" if e<0 else "half_line"))
    boundary=[]
    for s in sigmas:
      for k in units+(zz(0),zz(F(1,2)),zz(2),zz(1,1)):
        boundary.append(dict(sigma=q(s),kappa=enc(k),flux_over_i=q(2*s*(1-norm(k))),self_adjoint=bool(norm(k)==1)))
    scattering=[]
    for h in (F(2),F(3),F(5)):
      for t in units:
        ratio=div((h-t[0],-t[1]),(1-h*t[0],-h*t[1]));R=mul(zz(0,-1),ratio)
        scattering.append(dict(exp_pi_sigma=q(h),t=enc(t),reflection=enc(R),relative_scattering=enc((-R[0],-R[1])),unitary=bool(norm(R)==1)))
    return classical,boundary,scattering
def numeric_rows():
    mp.mp.dps=100;levels=[];waves=[]
    for sq in ((1,2),(1,1),(2,1)):
      s=mp.mpf(sq[0])/sq[1]
      for phase in ((0,1),(1,3),(1,1),(5,3)):
        h=mp.mpf(phase[0])/phase[1];theta=mp.pi*h;vs=mp.exp(1j*theta)
        kappa=vs*mp.gamma(1j*s)/mp.gamma(-1j*s)
        for j in range(-2,3):
          logr=mp.log(2)-(theta+2*mp.pi*j)/(2*s);rho=mp.exp(logr)
          levels.append(dict(sigma=list(sq),phase_pi=list(phase),j=j,kappa=cdec(kappa),log_rho=dec(logr),energy=dec(-rho*rho),normalizer=dec(rho*mp.sqrt(2*mp.sinh(mp.pi*s)/(mp.pi*s)))))
        for kq in ((1,3),(1,1),(3,1)):
          k=mp.mpf(kq[0])/kq[1];t=vs*mp.exp(2j*s*mp.log(k/2));a=mp.exp(mp.pi*s/2);b=1/a
          R=-1j*(a-t*b)/(b-t*a);x=mp.mpf(7)/10
          phi=mp.exp(-1j*mp.pi/4)*mp.sqrt(k*x)*(mp.besselj(1j*s,k*x)-t*mp.besselj(-1j*s,k*x))/(b-t*a)
          waves.append(dict(sigma=list(sq),phase_pi=list(phase),momentum=list(kq),reflection=cdec(R),relative_scattering=cdec(-R),phi_at_7_over_10=cdec(phi),density=dec(abs(phi)**2)))
    return levels,waves
def build():
    raw=YAML.read_bytes();assert hashlib.sha256(raw).hexdigest()==YAML_SHA
    ev=yaml.safe_load(raw);cl,bd,sc=exact_rows();levels,waves=numeric_rows()
    d=dict(schema="hcs-c391-inverse-square-v1",candidate_id="HCS-C391",obstruction_id="HEN-O375",source_commit=BASE,fixed_epoch=1788566400,
      scope_literal="NO_BAD_EULER_OR_ROOT_NUMBER",scope_flags=ev["scope_flags"],
      evaluator=dict(authority="flow_systems/skills/route-a-evaluator.md",version="0.2.0",sha256=AUTH),
      route_a_yaml=dict(path=str(YAML.relative_to(ROOT)),raw_sha256=YAML_SHA,semantic_sha256=hashlib.sha256(canon(ev)).hexdigest()),
      route_a=dict(tuple=ev["tuple"],overall_verdict="ROUTE_A_REJECTED",route_b_invocation_allowed=False),
      classical_rows=cl,boundary_rows=bd,scattering_algebra_rows=sc,negative_levels=levels,continuum_rows=waves,
      counts=dict(classical=45,boundary=27,scattering_algebra=15,negative_levels=60,continuum=36),
      numerical_precision=dict(working_digits=100,stored_digits=60,interval_certified=False),
      theorem_boundary="All sigma positive and all unit boundary phases; finite evidence is regression, not completeness; no critical case, target arithmetic, regularized determinant, or Route B")
    d["payload_sha256"]=hashlib.sha256(canon(d)).hexdigest();return d
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=ROOT/"results/c391_evidence.json");a=p.parse_args()
    d=build();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_bytes(json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False,allow_nan=False).encode()+b"\n")
    print("C391 producer PASS",d["payload_sha256"],d["counts"])
if __name__=="__main__":main()
