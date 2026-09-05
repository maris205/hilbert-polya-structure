#!/usr/bin/env python3
"""Independent standard-library arithmetic verifier; never imports producer."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c390 checker refuses optimized Python")
import argparse
from fractions import Fraction
import hashlib
import json
from math import factorial,gcd,isqrt
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
EVAL=ROOT/"evaluations/route_a/HCS-C390/2026-09-05.yaml"
EVAL_SHA="dbf5817ff1799f271ea0c9cb2220fd7b1b8bd447b1b8ae93255148f8d1754023"
EVAL_DATA_SHA="6fb5cb72f865af8cb7edf7eac34bdc2e7d518cb0a3897939424d53493bacde25"
FLAGS={"claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b"}
TUPLE=["A0_WEAK_ARITHMETIC_RELATION","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"]
def can(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def pairs(items):
    d={}
    for k,v in items:assert k not in d,"duplicate key";d[k]=v
    return d
def load(path):return json.loads(path.read_text(),object_pairs_hook=pairs,parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))
def keys(x,ks):assert type(x) is dict and set(x)==set(ks),"key set"
def rat(x):
    assert type(x) is list and len(x)==2 and all(type(v) is int for v in x),"rational type"
    n,d=x;assert d>0 and gcd(n,d)==1,"reduced rational";return Fraction(n,d)
def point(x):assert type(x) is list and len(x)==2;v=tuple(rat(t) for t in x);assert all(t>0 for t in v),"positive point";return v
def mat(A):assert type(A) is list and len(A)==2 and all(type(r) is list and len(r)==2 for r in A);return [[rat(x) for x in r] for r in A]
def ints(x):assert type(x) is list and all(type(v) is int for v in x),"integer list"
def integral(a,p):x,y=p;return x+y+x/y+y/x+(a+1)/x+(a+1)/y+a/(x*y)+a+2
def verify_chain(a,pts):
    for (x,y),(u,v) in zip(pts,pts[1:]):assert u==y and x*v==a+y,"recurrence"
    energy=integral(a,pts[0]);assert all(integral(a,p)==energy for p in pts),"energy preservation"
    # Reversal is checked by a backwards scalar recurrence, not the producer map.
    rev=list(reversed([(y,x) for x,y in pts]))
    for (x,y),(u,v) in zip(rev,rev[1:]):assert u==y and x*v==a+y,"reversed recurrence"
    return energy
def derivative(a,pts):
    # Differentiate the scalar second-order recurrence using two dual directions.
    columns=[]
    for j in range(2):
        dx,dy=Fraction(j==0),Fraction(j==1)
        for x,y in pts:dx,dy=dy,(dy*x-(a+y)*dx)/(x*x)
        columns.append((dx,dy))
    return [[columns[j][i] for j in range(2)] for i in range(2)]
def determinant(M):return M[0][0]*M[1][1]-M[0][1]*M[1][0]
def evaluation(path=EVAL):
    raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==EVAL_SHA,"evaluation raw hash"
    class UniqueLoader(yaml.SafeLoader):pass
    def mapping(loader,node,deep=False):return pairs(loader.construct_pairs(node,deep=deep))
    UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,mapping)
    x=yaml.load(raw,Loader=UniqueLoader)
    assert hashlib.sha256(can(x)).hexdigest()==EVAL_DATA_SHA,"evaluation structure/type hash"
    assert type(x["evaluation_date"]) is str and x["evaluation_date"]=="2026-09-05"
    assert type(x["fixed_epoch"]) is int and x["fixed_epoch"]==1788566400
    assert x["tuple"]==TUPLE and x["route_b_invocation_allowed"] is False
    assert set(x["scope_flags"])==FLAGS and all(v is False for v in x["scope_flags"].values())
    return x
def arc_bounds(d,n):
    terms=[Fraction((-1)**k,(2*k+1)*d**(2*k+1)) for k in range(n+1)]
    s=sum(terms[:-1]);return min(s,s+terms[-1]),max(s,s+terms[-1])
def cos_bounds(t0,t1):
    def series(t,n):return sum((Fraction((-1)**k,factorial(2*k))*t**(2*k) for k in range(n+1)),Fraction())
    return series(t1,19),series(t0,18)
def verify(x):
    keys(x,("schema","candidate_id","obstruction_id","source_commit","fixed_epoch","scope_literal","scope_flags","route_a","contract","orbit_rows","cycle_rows","fixed_rows","pi_bounds","angle_rows","summary","payload_sha256"))
    claimed=x["payload_sha256"];payload={k:v for k,v in x.items() if k!="payload_sha256"};assert type(claimed) is str and hashlib.sha256(can(payload)).hexdigest()==claimed,"payload digest"
    assert x["schema"]=="c390-lyness-evidence-v1" and x["candidate_id"]=="HCS-C390" and x["obstruction_id"]=="HEN-O374"
    assert x["source_commit"]=="0c877206d202f732e21ea0b194f9c7fdf30467ee" and type(x["fixed_epoch"]) is int and x["fixed_epoch"]==1788566400
    assert x["scope_literal"]=="NO_BAD_EULER_OR_ROOT_NUMBER";keys(x["scope_flags"],FLAGS);assert all(v is False for v in x["scope_flags"].values())
    keys(x["route_a"],("tuple","route_b_invocation_allowed"));assert x["route_a"]["tuple"]==TUPLE and x["route_a"]["route_b_invocation_allowed"] is False
    contract={"map":"F_a(x,y)=(y,(a+y)/x)","phase_space":"a,x,y>0; rational classification additionally a,x,y in Q","orbit_grid":"six rational a; r=a+2+t with t=1/2,1,2,4; twelve iterates","period_controls":"a=1 four-by-four seeds; a=7 GMX nine-cycle; five rational centers","angle_role":"certified intervals between classical rotation endpoints; not numerical energy reconstruction","denominator_range":[2,257],"external_dependencies":["BR2004:Propositions6-7","GMX2012:positive-rational-period-classification","Mazur1977:torsion-theorem"],"evidence_role":"finite exact source certificates; universal statements are analytic with declared classical inputs"}
    assert can(x["contract"])==can(contract),"frozen contract"
    params=[Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(2),Fraction(7),Fraction(11)]
    grid=[(a,a+2+t) for a in params for t in (Fraction(1,2),Fraction(1),Fraction(2),Fraction(4))]
    assert type(x["orbit_rows"]) is list and len(x["orbit_rows"])==24
    for row,(a,r) in zip(x["orbit_rows"],grid):
        keys(row,("a","r","energy","states","twelve_step_jacobian","jacobian_determinant"));assert rat(row["a"])==a and rat(row["r"])==r
        assert r*r-r-a>0,"upper diagonal branch"
        assert type(row["states"]) is list and len(row["states"])==13
        pts=[point(p) for p in row["states"]];assert pts[0]==(r,r)
        assert rat(row["energy"])==verify_chain(a,pts)
        M=mat(row["twelve_step_jacobian"]);assert M==derivative(a,pts[:-1]),"dual Jacobian"
        assert rat(row["jacobian_determinant"])==determinant(M)==pts[-1][0]*pts[-1][1]/(r*r),"weighted symplectic determinant"
    # Independently reconstruct the exact cycle support of the frozen seed grid.
    support=set()
    for u in (Fraction(1,2),Fraction(1),Fraction(2),Fraction(3)):
        for v in (Fraction(1,2),Fraction(1),Fraction(2),Fraction(3)):
            seq=[u,v]
            for _ in range(4):seq.append((1+seq[-1])/seq[-2])
            support.update((seq[k],seq[k+1]) for k in range(5))
    seen=set();starts=[];assert type(x["cycle_rows"]) is list and len(x["cycle_rows"])==11
    for i,row in enumerate(x["cycle_rows"]):
        keys(row,("a","least_period","energy","cycle","return_matrix","trace","determinant","identity_return"))
        a=rat(row["a"]);n=row["least_period"];assert type(n) is int and n==(5 if i<10 else 9) and a==(1 if i<10 else 7)
        assert type(row["cycle"]) is list and len(row["cycle"])==n
        pts=[point(p) for p in row["cycle"]];assert len(set(pts))==n and pts[0]==min(pts),"primitive canonical cycle"
        assert rat(row["energy"])==verify_chain(a,pts+[pts[0]])
        M=mat(row["return_matrix"]);assert M==derivative(a,pts),"return derivative"
        assert rat(row["trace"])==M[0][0]+M[1][1]==2 and rat(row["determinant"])==determinant(M)==1
        N=[[M[i][j]-int(i==j) for j in range(2)] for i in range(2)]
        assert all(sum(N[i][k]*N[k][j] for k in range(2))==0 for i in range(2) for j in range(2)),"return nilpotence"
        identity=M==[[1,0],[0,1]];assert type(row["identity_return"]) is bool and row["identity_return"] is identity
        if i<10:assert identity and not (seen&set(pts));seen.update(pts);starts.append(pts[0])
        else:
            seq=list(map(Fraction,("3/2","5/7","36/7","17","14/3","35/51","28/17","63/5","119/10")))
            assert set(pts)=={(seq[j],seq[(j+1)%9]) for j in range(9)} and not identity
            assert rat(row["energy"])==Fraction(258,7)
    assert seen==support and starts==sorted(starts),"complete seed-induced five-cycle grid"
    assert type(x["fixed_rows"]) is list and len(x["fixed_rows"])==5
    for row,r in zip(x["fixed_rows"],map(Fraction,("3/2","2","3","4","5"))):
        keys(row,("a","coordinate","energy","trace","determinant"));a=rat(row["a"])
        assert a==r*r-r and rat(row["coordinate"])==r
        assert rat(row["energy"])==(r+1)**3/r and rat(row["trace"])==1/r and rat(row["determinant"])==1
    assert type(x["pi_bounds"]) is list and len(x["pi_bounds"])==2
    pl,ph=map(rat,x["pi_bounds"]);l5,u5=arc_bounds(5,31);l239,u239=arc_bounds(239,11)
    assert 3<pl<=16*l5-4*u239<=16*u5-4*l239<=ph<4 and ph-pl<=Fraction(4,2**128),"tight independent Machin enclosure"
    intervals=[(Fraction(1,4),Fraction(19,100),Fraction(39,200)),(Fraction(1,2),Fraction(39,200),Fraction(99,500)),(Fraction(2),Fraction(101,500),Fraction(26,125)),(Fraction(7),Fraction(21,100),Fraction(11,50)),(Fraction(11),Fraction(21,100),Fraction(11,50))]
    assert type(x["angle_rows"]) is list and len(x["angle_rows"])==5
    for row,(a,lo,hi) in zip(x["angle_rows"],intervals):
        keys(row,("a","rotation_interval","endpoint_cosine_bounds","period_witnesses"));assert rat(row["a"])==a
        assert type(row["rotation_interval"]) is list and len(row["rotation_interval"])==2 and list(map(rat,row["rotation_interval"]))==[lo,hi]
        assert type(row["endpoint_cosine_bounds"]) is list and len(row["endpoint_cosine_bounds"])==2
        for q,bounds in zip((lo,hi),row["endpoint_cosine_bounds"]):
            assert type(bounds) is list and len(bounds)==2;l,u=map(rat,bounds);cl,cu=cos_bounds(2*q*pl,2*q*ph)
            assert 0<l<=cl<=cu<=u<1 and u-l<=Fraction(8,2**96),"tight independent cosine enclosure"
            if a<1:assert q<Fraction(1,5) and 4*a*u*u+2*u-1<0,"interval above center endpoint"
            else:assert q>Fraction(1,5) and 4*a*l*l+2*l-1>0,"interval below center endpoint"
        assert type(row["period_witnesses"]) is list and len(row["period_witnesses"])==256
        for n,w in enumerate(row["period_witnesses"],2):
            keys(w,("denominator","prime_integer","numerators"));assert type(w["denominator"]) is int and w["denominator"]==n
            isprime=all(n%d for d in range(2,isqrt(n)+1));assert type(w["prime_integer"]) is bool and w["prime_integer"] is isprime
            ints(w["numerators"]);assert w["numerators"]==[m for m in range(1,n) if m>n*lo and m<n*hi and gcd(m,n)==1],"complete reduced denominator witnesses"
            if isprime and n*(hi-lo)>1:assert w["numerators"],"large-prime existence bound"
    summary={"orbit_rows":24,"exact_map_steps":288,"cycle_controls":11,"cycle_points":59,"fixed_controls":5,"endpoint_intervals":5,"denominator_controls":1280,"sufficient_period_witnesses":690}
    keys(x["summary"],summary);assert all(type(v) is int for v in x["summary"].values()) and x["summary"]==summary
    return summary
def main():
    p=argparse.ArgumentParser();p.add_argument("--evidence",type=Path,default=ROOT/"results/c390_lyness_evidence.json");p.add_argument("--evaluation",type=Path,default=EVAL);p.add_argument("--evaluation-only",action="store_true");a=p.parse_args();evaluation(a.evaluation)
    if a.evaluation_only:print("C390 strict evaluation PASS");return
    print("C390 independent checker PASS: "+json.dumps(verify(load(a.evidence)),sort_keys=True))
if __name__=="__main__":main()
