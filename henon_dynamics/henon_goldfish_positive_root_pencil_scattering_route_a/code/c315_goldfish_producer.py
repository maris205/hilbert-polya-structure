#!/usr/bin/env python3
"""Produce exact-coefficient and high-precision HCS-C315 receipts."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/"results/c315_goldfish_evidence.json"
SOURCE="1938bae19e5a92f9ce2411aafdc68323bd641bd0"
EVALUATOR="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER";EPOCH=1788393600
mp.mp.dps=100

SPECS=[
 ("n2-basic",["0","1"],["1","2"]),("n2-skew",["-3/2","5/2"],["7/3","1/5"]),
 ("n3-basic",["-2","0","3"],["1","2","4"]),("n3-fractions",["-5/3","-1/4","7/5"],["2/7","5/4","3/2"]),
 ("n3-wide",["-7","1","9"],["5","1/3","2"]),("n4-basic",["-3","-1","2","5"],["1","3","2","4"]),
 ("n4-fractions",["-11/4","-2/3","5/4","13/3"],["3/8","7/5","2/9","11/6"]),
 ("n4-near",["0","1/5","2/5","1"],["1","2","3","4"]),("n5-basic",["-5","-2","0","3","8"],["2","1","4","3","5"]),
 ("n5-fractions",["-7/2","-4/3","1/6","9/5","17/4"],["1/2","5/3","7/4","2/5","9/7"]),
 ("n5-unit",["0","1","2","3","4"],["1","1","1","1","1"]),("n6-basic",["-6","-3","-1","2","5","9"],["1","2","3","4","5","6"]),
 ("n6-zigzag",["-8","-5/2","-1/3","4/5","7/3","6"],["7/4","1/6","5/2","2/3","9/5","4"]),
 ("n7-basic",["-9","-6","-3","-1","2","5","10"],["1","3","2","5","4","7","6"]),
]
TIMES=["-11","-3","-1/2","0","1/3","2","9"]
FLAGS={"claims_target_arithmetic_local_data":False,"claims_target_euler_factors":False,"claims_root_number":False,"claims_automorphy":False,"claims_target_divisor_or_counting_law":False,"claims_target_functional_equation":False,"claims_target_zero_match":False,"claims_hilbert_polya_operator":False,"invokes_route_b":False}

def mul(a,b):
 out=[Fraction(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def add(a,b):
 n=max(len(a),len(b));a=[Fraction(0)]*(n-len(a))+a;b=[Fraction(0)]*(n-len(b))+b
 return [x+y for x,y in zip(a,b)]
def scale(a,c):return [c*x for x in a]
def qs(x):return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def mf(x):return mp.mpf(x.numerator)/x.denominator
def dec(x):return mp.nstr(mp.re(x),76,strip_zeros=False)
def peval(co,z):
 v=mp.mpf("0")
 for c in co:v=v*z+mf(c)
 return v
def deriv(co):return [co[i]*Fraction(len(co)-1-i) for i in range(len(co)-1)]
def roots(co):
 z=sp.symbols("z");poly=sp.Poly(sum(sp.Rational(c.numerator,c.denominator)*z**(len(co)-1-i) for i,c in enumerate(co)),z)
 vals=sp.nroots(poly,n=90,maxsteps=300)
 out=[]
 for value in vals:
  re,im=value.as_real_imag()
  if abs(mp.mpf(str(sp.N(im,80))))>mp.mpf("1e-70"):raise AssertionError("nonreal root")
  out.append(mp.mpf(str(sp.N(re,90))))
 return sorted(out)
def polynomials(xs,vs):
 P=[Fraction(1)]
 for x in xs:P=mul(P,[Fraction(1),-x])
 Q=[Fraction(0)]*len(xs)
 for i,v in enumerate(vs):
  term=[Fraction(1)]
  for j,x in enumerate(xs):
   if i!=j:term=mul(term,[Fraction(1),-x])
  Q=add(Q,scale(term,v))
 return P,Q
def case_row(case_id,xraw,vraw):
 xs=list(map(Fraction,xraw));vs=list(map(Fraction,vraw));n=len(xs);P,Q=polynomials(xs,vs);yp=roots(Q)
 pd=deriv(P);pdd=deriv(pd);qd=deriv(Q)
 V=sum(vs,Fraction(0));M=sum((v*x for v,x in zip(vs,xs)),Fraction(0));c=M/V
 betas=[]
 for y in yp:betas.append(-peval(P,y)/peval(qd,y))
 if not all(b>0 for b in betas):raise AssertionError("beta sign")
 time_rows=[]
 for traw in TIMES:
  tt=Fraction(traw);co=[p-tt*q for p,q in zip(P,[Fraction(0)]+Q)];zr=roots(co);dp=deriv(co);ddp=deriv(dp)
  velocities=[]
  for z in zr:velocities.append(peval(Q,z)/peval(dp,z))
  implicit=[];gold=[]
  for i,z in enumerate(zr):
   vi=velocities[i]
   implicit.append(2*peval(qd,z)*vi/peval(dp,z)-peval(ddp,z)*vi*vi/peval(dp,z))
   gold.append(2*sum((vi*velocities[j]/(z-zr[j]) for j in range(n) if j!=i),mp.mpf("0")))
  time_rows.append({"time":traw,"roots":[dec(z) for z in zr],"velocities":[dec(v) for v in velocities],"sum_roots":dec(sum(zr)),"sum_velocities":dec(sum(velocities)),"max_ode_residual":dec(max(abs(a-b) for a,b in zip(implicit,gold)))})
 asym=[]
 for sign in (-1,1):
  tt=Fraction(sign*1000000);co=[p-tt*q for p,q in zip(P,[Fraction(0)]+Q)];zr=roots(co);tv=mf(tt)
  finite=zr[1:] if sign<0 else zr[:-1];ballistic=zr[0] if sign<0 else zr[-1]
  fpred=[y-b/tv for y,b in zip(yp,betas)];bpred=mf(V)*tv+mf(c)+sum(betas)/tv
  asym.append({"time":qs(tt),"finite_root_errors":[dec(z-p) for z,p in zip(finite,fpred)],"ballistic_root_error":dec(ballistic-bpred),"ballistic_velocity_limit":qs(V),"ballistic_intercept":qs(c)})
 return {"case_id":case_id,"dimension":n,"initial_positions":xraw,"initial_velocities":vraw,"P_coefficients":[qs(x) for x in P],"Q_coefficients":[qs(x) for x in Q],"total_velocity":qs(V),"velocity_weighted_position":qs(M),"ballistic_intercept":qs(c),"anchor_roots":[dec(y) for y in yp],"beta_coefficients":[dec(b) for b in betas],"time_rows":time_rows,"asymptotic_rows":asym}
def ph(d):
 b=dict(d);b.pop("payload_sha256",None);return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def leaves(v):
 if type(v)is dict:return sum(leaves(x) for x in v.values())
 if type(v)is list:return sum(leaves(x) for x in v)
 return 1
def main():
 if sys.flags.optimize:raise RuntimeError("C315 producer refuses optimized Python")
 p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=OUTPUT);a=p.parse_args();rows=[case_row(*s) for s in SPECS]
 d={"schema":"hcs-c315-positive-goldfish-v1","candidate_id":"HCS-C315","obstruction_id":"HEN-O299","evaluation_date":"2026-09-03","fixed_epoch":EPOCH,"source_commit":SOURCE,"scope_literal":SCOPE,"evaluator":{"version":"0.2.0","sha256":EVALUATOR},"model":{"dynamics":"zddot_i=2 sum_{j!=i} zdot_i zdot_j/(z_i-z_j)","domain":"N>=2, x_1<...<x_N real, and every initial velocity v_i>0","linearization":"roots of p(z,t)=P(z)-tQ(z)","invariant":"Q(z)=sum_i zdot_i(t) product_{j!=i}(z-z_j(t)) is time independent"},"theorem_contract":{"global":"the polynomial pencil is real rooted and simple for every real time, so the solution is complete and collision free","interlacing":"the moving roots have a strict signed-time interlacing with initial positions and invariant Q-roots","monotonicity":"every particle velocity stays strictly positive and their sum is constant","scattering":"one ballistic carrier transfers from the leftmost incoming rank to the rightmost outgoing rank while N-1 roots approach fixed interlacing anchors","asymptotics":"all finite roots and the ballistic root have explicit first inverse-time coefficients"},"cases":rows,"boundary_atlas":[{"face":"N=1","status":"free particle, listed only as a trivial boundary"},{"face":"one zero velocity","status":"global simplicity can fail; (x,v)=((0,1),(1,0)) collides at t=1"},{"face":"mixed velocity signs","status":"reality can fail; (x,v)=((0,1),(1,-1)) has a double root at t=1/4 and complex roots later"},{"face":"coincident initial positions","status":"excluded because the Newtonian vector field is singular"},{"face":"all negative velocities","status":"obtainable by time reversal but not merged into the positive-cone theorem"}],"collision_boundary":{"C196":"repulsive inverse-square Calogero--Moser uses a Hermitian eigenvalue pencil and N asymptotic free velocities; C315 uses a hyperbolic polynomial pencil and one-carrier scattering","C292":"sticky particles resolve physical mergers; C315 proves strict no-collision on a positive velocity cone","C296":"hard rods use event-driven elastic relabeling, not a smooth velocity-coupled root flow"},"route_a":{"tuple":["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},"scope_flags":FLAGS,"nonclaims":["Calogero retains ownership of the goldfish model and polynomial-root solution.","The positive-real interlacing closure is not presented as a literature-priority claim.","No canonical quantization, target determinant, target arithmetic data, Euler factors, root numbers, automorphy, target zero match, or Hilbert--Polya operator is asserted."],"references":[{"doi":"10.1016/S0167-2789(01)00160-9","role":"standard goldfish model ownership"},{"handle":"11573/11324","role":"Calogero polynomial-zero dynamics lineage"},{"doi":"10.1088/0305-4470/37/47/008","role":"free-particle linearization context"}]}
 d["enumeration"]={"case_count":len(rows),"time_rows":sum(len(x["time_rows"]) for x in rows),"root_time_cells":sum(sum(len(t["roots"]) for t in x["time_rows"]) for x in rows),"anchor_cells":sum(len(x["anchor_roots"]) for x in rows),"asymptotic_rows":2*len(rows)};d["enumeration"]["audited_leaf_count"]=leaves(d)+1;d["payload_sha256"]=ph(d);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n");print(f"C315_PRODUCER_PASS {d['payload_sha256']} {d['enumeration']['audited_leaf_count']}")
if __name__=="__main__":main()
