#!/usr/bin/env python3
"""Canonical finite regression ledger; infinite claims are proved separately."""
if not __debug__: raise RuntimeError("c396 producer refuses optimized Python")
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import mpmath as mp
import yaml
ROOT=Path(__file__).resolve().parents[1]
YAML=ROOT/"evaluations/route_a/HCS-C396/2026-09-05.yaml"
YSHA="b9f3ae12e0294002acf0aec9d499f42bb0b1537ae75b30b253e5b5a600a048d8"
BASE="697518b6db90458f86f7916fbf397b8ad5ef2372"
AUTH="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
FLAGS=("claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b")
TUPLE=["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"]
ETAS=(F(0),F(1,3),F(1,2),F(1),F(2),F(3),F(7))
TAUS=(F(1,2),F(1),F(2))
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()
def q(x):return [x.numerator,x.denominator]
def num(x):return mp.nstr(x,60)
def znum(x):return [num(mp.re(x)),num(mp.im(x))]
def real(x):return mp.mpf(x.numerator)/x.denominator
def build():
    raw=YAML.read_bytes();assert hashlib.sha256(raw).hexdigest()==YSHA
    ev=yaml.safe_load(raw);mp.mp.dps=100
    boundary=[];transport=[];spectrum=[];pseudo=[];green=[]
    for eta in ETAS:
      reflection=(eta-1)/(eta+1)
      boundary.append(dict(eta=q(eta),q=q(reflection),flux=q((reflection**2-1)/2),transparent=eta==1,conservative=eta==0))
      for tau in TAUS:
        for tr in (F(0),F(1,4),F(1),F(5,4),F(2),F(11,4),F(3)):
          for sr in (F(1,8),F(3,8),F(5,8),F(7,8)):
            t=tau*tr;s=tau*sr;k=int((s+t)//tau)
            transport.append(dict(eta=q(eta),tau=q(tau),t=q(t),s=q(s),crossings=k,remainder=q(s+t-k*tau),amplitude=q(reflection**k),operator_norm=q(abs(reflection)**int(t//tau)),extinct=reflection==0 and t>=tau))
        T=real(tau);Q=real(reflection)
        if reflection:
          for n in range(-3,4):
            lam=(mp.log(abs(Q))+1j*(2*mp.pi*n+(mp.pi if Q<0 else 0)))/T
            spectrum.append(dict(eta=q(eta),tau=q(tau),n=n,eigenvalue=znum(lam),similarity_condition=num(1/abs(Q))))
        z=mp.mpf(1)/2+1j
        def P(s):return (s*s+1)/z+2*s/z**2+2/z**3
        C=(Q*P(0)-P(T))/(mp.exp(z*T)-Q)
        def w(s):return P(s)+C*mp.exp(z*s)
        green.append(dict(eta=q(eta),tau=q(tau),z=["0.5","1.0"],w_zero=znum(w(0)),w_third=znum(w(T/3)),w_end=znum(w(T))))
    for tau in TAUS:
      T=real(tau)
      specs=[("trigonometric",F(j,6)) for j in (1,2,3,4,5)]+[("hyperbolic",x) for x in (F(1,2),F(1),F(2))]+[("critical",F(0))]
      for branch,param in specs:
        if branch=="trigonometric":
            v=mp.pi*real(param);X=-v*mp.cot(v)/T
            if param==F(1,2):X=mp.mpf(0)
            rho=T*mp.sin(v)/v
        elif branch=="hyperbolic":
            v=real(param);X=-v*mp.coth(v)/T;rho=T*mp.sinh(v)/v
        else:X=-1/T;rho=T
        hs=T*T/2 if not X else T/(2*X)-(1-mp.exp(-2*X*T))/(4*X*X)
        pseudo.append(dict(tau=q(tau),branch=branch,parameter=q(param),real_part=num(X),resolvent_norm=num(rho),least_mu=num(1/rho**2),hs_squared=num(hs)))
    d=dict(schema="hcs-c396-impedance-string-v1",candidate_id="HCS-C396",obstruction_id="HEN-O380",source_commit=BASE,fixed_epoch=1788566400,scope_literal="NO_BAD_EULER_OR_ROOT_NUMBER",scope_flags={k:False for k in FLAGS},evaluator=dict(authority="flow_systems/skills/route-a-evaluator.md",version="0.2.0",sha256=AUTH),route_a_yaml=dict(path=str(YAML.relative_to(ROOT)),raw_sha256=YSHA,semantic_sha256=hashlib.sha256(canon(ev)).hexdigest()),route_a=dict(tuple=TUPLE,overall_verdict="ROUTE_A_REJECTED",route_b_invocation_allowed=False),boundary_rows=boundary,transport_rows=transport,spectrum_rows=spectrum,pseudospectrum_rows=pseudo,green_rows=green,counts=dict(boundary=7,transport=588,spectrum=126,pseudospectrum=27,green=21),numerical_precision=dict(working_digits=100,stored_digits=60,interval_certified=False),theorem_boundary="Finite eta nonnegative; full physical time and spectrum proved analytically; exact pseudospectra only at eta one; no target arithmetic, ordinary trace or Route B")
    d["payload_sha256"]=hashlib.sha256(canon(d)).hexdigest();return d
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=ROOT/"results/c396_evidence.json");a=p.parse_args()
    d=build();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_bytes(json.dumps(d,sort_keys=True,indent=2).encode()+b"\n")
    print("C396 producer PASS",json.dumps(d["counts"],sort_keys=True),hashlib.sha256(a.output.read_bytes()).hexdigest())
if __name__=="__main__":main()
