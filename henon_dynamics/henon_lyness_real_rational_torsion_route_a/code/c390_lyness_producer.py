#!/usr/bin/env python3
"""Canonical finite source certificates; no finite-to-universal inference."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c390 producer refuses optimized Python")
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial,gcd
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FLAGS=("claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b")
TUPLE=["A0_WEAK_ARITHMETIC_RELATION","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"]
PARAMS=(F(1,4),F(1,2),F(1),F(2),F(7),F(11))
INTERVALS=((F(1,4),F(19,100),F(39,200)),(F(1,2),F(39,200),F(99,500)),(F(2),F(101,500),F(26,125)),(F(7),F(21,100),F(11,50)),(F(11),F(21,100),F(11,50)))
CONTRACT={"map":"F_a(x,y)=(y,(a+y)/x)","phase_space":"a,x,y>0; rational classification additionally a,x,y in Q","orbit_grid":"six rational a; r=a+2+t with t=1/2,1,2,4; twelve iterates","period_controls":"a=1 four-by-four seeds; a=7 GMX nine-cycle; five rational centers","angle_role":"certified intervals between classical rotation endpoints; not numerical energy reconstruction","denominator_range":[2,257],"external_dependencies":["BR2004:Propositions6-7","GMX2012:positive-rational-period-classification","Mazur1977:torsion-theorem"],"evidence_role":"finite exact source certificates; universal statements are analytic with declared classical inputs"}
def enc(x):return [x.numerator,x.denominator]
def matrix(A):return [[enc(v) for v in row] for row in A]
def can(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def step(a,p):x,y=p;return y,(a+y)/x
def H(a,p):x,y=p;return (x+1)*(y+1)*(x+y+a)/(x*y)
def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(2)),F()) for j in range(2)] for i in range(2)]
def monodromy(a,states):
    M=[[F(1),F(0)],[F(0),F(1)]]
    for x,y in states:M=mm([[F(0),F(1)],[-(a+y)/x**2,1/x]],M)
    return M
def orbit(a,p,n):
    points=[p]
    for _ in range(n):points.append(step(a,points[-1]))
    return points
def norm_cycle(points):return min(tuple(points[i:]+points[:i]) for i in range(len(points)))
def atan_bounds(d,n):
    s=sum((F((-1)**k,(2*k+1)*d**(2*k+1)) for k in range(n)),F())
    e=F(1,(2*n+1)*d**(2*n+1));return (s,s+e) if n%2==0 else (s-e,s)
def floor(x):return x.numerator//x.denominator
def ceil(x):return -floor(-x)
def pi_bounds():
    a,b=atan_bounds(5,32);c,d=atan_bounds(239,10);Q=2**128
    return F(floor((16*a-4*d)*Q)-1,Q),F(ceil((16*b-4*c)*Q)+1,Q)
def cos_poly(x,n):return sum(((-1)**k*x**(2*k)/factorial(2*k) for k in range(n+1)),F())
def cosine_bounds(q,pl,ph):
    Q=2**96;lo=cos_poly(2*q*ph,21);hi=cos_poly(2*q*pl,20)
    return F(floor(lo*Q)-2,Q),F(ceil(hi*Q)+2,Q)
def prime(n):return n>=2 and all(n%d for d in range(2,int(n**.5)+1))
def build():
    rows=[]
    for a in PARAMS:
        for t in (F(1,2),F(1),F(2),F(4)):
            r=a+2+t;pts=orbit(a,(r,r),12);M=monodromy(a,pts[:-1])
            rows.append({"a":enc(a),"r":enc(r),"energy":enc(H(a,pts[0])),"states":[[enc(x),enc(y)] for x,y in pts],"twelve_step_jacobian":matrix(M),"jacobian_determinant":enc(M[0][0]*M[1][1]-M[0][1]*M[1][0])})
    cycles=set()
    for x in (F(1,2),F(1),F(2),F(3)):
        for y in (F(1,2),F(1),F(2),F(3)):cycles.add(norm_cycle(orbit(F(1),(x,y),5)[:-1]))
    cr=[]
    controls=[(F(1),c) for c in sorted(cycles)]
    controls.append((F(7),norm_cycle(orbit(F(7),(F(3,2),F(5,7)),9)[:-1])))
    for a,c in controls:
        M=monodromy(a,c);cr.append({"a":enc(a),"least_period":len(c),"energy":enc(H(a,c[0])),"cycle":[[enc(x),enc(y)] for x,y in c],"return_matrix":matrix(M),"trace":enc(M[0][0]+M[1][1]),"determinant":enc(M[0][0]*M[1][1]-M[0][1]*M[1][0]),"identity_return":M==[[F(1),F(0)],[F(0),F(1)]]})
    fixed=[]
    for r in (F(3,2),F(2),F(3),F(4),F(5)):
        a=r*(r-1);fixed.append({"a":enc(a),"coordinate":enc(r),"energy":enc(H(a,(r,r))),"trace":enc(1/r),"determinant":enc(F(1))})
    pl,ph=pi_bounds();angle=[]
    for a,lo,hi in INTERVALS:
        bounds=[cosine_bounds(q,pl,ph) for q in (lo,hi)];periods=[]
        for n in range(2,258):
            ms=[m for m in range(1,n) if lo<F(m,n)<hi and gcd(m,n)==1]
            periods.append({"denominator":n,"prime_integer":prime(n),"numerators":ms})
        angle.append({"a":enc(a),"rotation_interval":[enc(lo),enc(hi)],"endpoint_cosine_bounds":[[enc(l),enc(u)] for l,u in bounds],"period_witnesses":periods})
    summary={"orbit_rows":len(rows),"exact_map_steps":12*len(rows),"cycle_controls":len(cr),"cycle_points":sum(r["least_period"] for r in cr),"fixed_controls":len(fixed),"endpoint_intervals":len(angle),"denominator_controls":256*len(angle),"sufficient_period_witnesses":sum(len(v["numerators"]) for r in angle for v in r["period_witnesses"])}
    out={"schema":"c390-lyness-evidence-v1","candidate_id":"HCS-C390","obstruction_id":"HEN-O374","source_commit":"0c877206d202f732e21ea0b194f9c7fdf30467ee","fixed_epoch":1788566400,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","scope_flags":{k:False for k in FLAGS},"route_a":{"tuple":TUPLE,"route_b_invocation_allowed":False},"contract":CONTRACT,"orbit_rows":rows,"cycle_rows":cr,"fixed_rows":fixed,"pi_bounds":[enc(pl),enc(ph)],"angle_rows":angle,"summary":summary}
    out["payload_sha256"]=hashlib.sha256(can(out)).hexdigest();return out
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=ROOT/"results/c390_lyness_evidence.json");a=p.parse_args();x=build();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+"\n");print("C390 producer PASS: "+json.dumps(x["summary"],sort_keys=True))
if __name__=="__main__":main()
