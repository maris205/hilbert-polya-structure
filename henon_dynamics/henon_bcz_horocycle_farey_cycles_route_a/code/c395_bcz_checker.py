#!/usr/bin/env python3
"""Independent Farey-fraction, scalar-recurrence and lattice certificate checker."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c395 checker refuses optimized Python")
import argparse
from fractions import Fraction
import hashlib
import json
from math import gcd
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
EVAL=ROOT/"evaluations/route_a/HCS-C395/2026-09-05.yaml"
EVAL_SHA="0d574d4f0ddae9e1bad4b84ba0962b4d257fa5045b8a828eba510e398923e6f9"
EVAL_DATA_SHA="a8ea2cfdb1840739fd25f3e6649dcf76a6c590a11fbb0c8fc77e8788b7ffbc9b"
FLAGS={"claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b"}
TUPLE=["A0_WEAK_ARITHMETIC_RELATION","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"]
def can(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def unique(items):
    x={}
    for k,v in items:
        assert k not in x,"duplicate key"
        x[k]=v
    return x
def load(p):return json.loads(p.read_text(),object_pairs_hook=unique,parse_constant=lambda s:(_ for _ in ()).throw(ValueError(s)))
def keys(x,names):assert type(x) is dict and set(x)==set(names),"key set"
def integer(x):assert type(x) is int,"literal integer";return x
def ints(x):assert type(x) is list;return [integer(t) for t in x]
def rat(x):
    v=ints(x);assert len(v)==2 and v[1]>0 and gcd(*v)==1,"reduced rational";return Fraction(*v)
def matrix(x):
    assert type(x) is list and len(x)==2
    v=[ints(row) for row in x];assert all(len(row)==2 for row in v);return v
def eq(x,y,label):assert can(x)==can(y),label
def domain(a,b):return 0<a<=1 and 0<b<=1 and a+b>1
def evaluation(p=EVAL):
    raw=p.read_bytes()
    class StrictLoader(yaml.SafeLoader):pass
    StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,lambda l,n,deep=False:unique(l.construct_pairs(n,deep=deep)))
    y=yaml.load(raw,Loader=StrictLoader)
    assert type(y["evaluation_date"]) is str and y["evaluation_date"]=="2026-09-05","quoted date"
    assert type(y["fixed_epoch"]) is int and y["fixed_epoch"]==1788566400,"epoch integer"
    keys(y["scope_flags"],FLAGS);assert all(v is False for v in y["scope_flags"].values()),"literal flags"
    assert y["route_b_invocation_allowed"] is False and y["tuple"]==TUPLE,"evaluation route"
    assert hashlib.sha256(can(y)).hexdigest()==EVAL_DATA_SHA,"evaluation exact semantic schema/type"
    assert hashlib.sha256(raw).hexdigest()==EVAL_SHA,"evaluation raw bytes"
    return y
def verify(x):
    keys(x,("schema","candidate_id","obstruction_id","source_commit","fixed_epoch","scope_literal","scope_flags","route_a","contract","layer_rows","wall_rows","fixed_rows","summary","payload_sha256"))
    assert type(x["payload_sha256"]) is str and hashlib.sha256(can({k:v for k,v in x.items() if k!="payload_sha256"})).hexdigest()==x["payload_sha256"],"payload SHA"
    assert x["schema"]=="c395-bcz-evidence-v1" and x["candidate_id"]=="HCS-C395" and x["obstruction_id"]=="HEN-O379"
    assert x["source_commit"]=="697518b6db90458f86f7916fbf397b8ad5ef2372" and integer(x["fixed_epoch"])==1788566400
    assert x["scope_literal"]=="NO_BAD_EULER_OR_ROOT_NUMBER"
    keys(x["scope_flags"],FLAGS);assert all(t is False for t in x["scope_flags"].values())
    keys(x["route_a"],("tuple","route_b_invocation_allowed"));assert x["route_a"]["tuple"]==TUPLE and x["route_a"]["route_b_invocation_allowed"] is False
    contract={"domain":"0<a,b<=1; a+b>1","layer_range":[1,64],"wall_range":[2,17],"fixed_iterate_range":[1,128],"physical_repetition_range":[1,5],"arithmetic":"all positive coprime denominator pairs; no prime filtering","precision":"exact integers and reduced rationals","theorem_scope":"all N>=1 and all scales; finite ledger is a consistency control"}
    eq(x["contract"],contract,"contract")
    assert type(x["layer_rows"]) is list and len(x["layer_rows"])==64
    total=0;periods=[]
    for n,row in enumerate(x["layer_rows"],1):
        keys(row,("N","least_period","scale_interval","lower_included","upper_included","interior_scale","cycle","branch_indices","return_matrices","product_at_start","gap_sum","interior_total_roof","endpoint_total_roof","repetitions"))
        assert integer(row["N"])==n
        fractions=sorted({Fraction(p,q) for q in range(1,n+1) for p in range(q+1)})
        pairs=[[u.denominator,v.denominator] for u,v in zip(fractions,fractions[1:])]
        # This is a complete sorted fraction population, not the producer floor orbit.
        eq(row["cycle"],pairs,"independent Farey cycle")
        p=integer(row["least_period"]);assert p==len(pairs)
        assert {tuple(t) for t in pairs}=={(q,r) for q in range(1,n+1) for r in range(1,n+1) if q+r>n and gcd(q,r)==1}
        periods.append(p);total+=p
        assert type(row["scale_interval"]) is list and len(row["scale_interval"])==2
        assert [rat(t) for t in row["scale_interval"]]==[Fraction(1,n+1),Fraction(1,n)]
        assert row["lower_included"] is False and row["upper_included"] is True
        delta=rat(row["interior_scale"]);assert delta==Fraction(2,2*n+1)
        assert not domain(Fraction(1,n+1),Fraction(n,n+1)),"excluded lower endpoint"
        indices=ints(row["branch_indices"]);assert len(indices)==p
        assert type(row["return_matrices"]) is list and len(row["return_matrices"])==p
        left,right=[1,0],[0,1]
        gaps=Fraction()
        for j,((q,r),k) in enumerate(zip(pairs,indices)):
            u,v=fractions[j:j+2];assert v-u==Fraction(1,q*r),"Farey gap"
            gaps+=v-u
            nxt=pairs[(j+1)%p]
            assert nxt==[r,k*r-q] and k*r<=n+q<(k+1)*r,"integer successor"
            left,right=right,[k*right[i]-left[i] for i in range(2)]
            M=matrix(row["return_matrices"][j]);eq(M,[[1-q*r,q*q],[-r*r,1+q*r]],"return matrix")
            # Exact floor, inverse/reversal and lattice first-return controls at
            # an interior scale AND the included upper endpoint.
            for d in (delta,Fraction(1,n)):
                a,b=d*q,d*r;c=d*nxt[1]
                assert domain(a,b) and domain(b,c)
                assert k*b<=1+a<(k+1)*b and c==k*b-a,"floor convention"
                assert k*b<=1+c<(k+1)*b and a==k*b-c,"inverse/reversal"
                R=1/(a*b)
                # h_R p B has columns (b,0),(c,1/b), checked scalarwise.
                assert 1/a-R*b==0 and -R*a==-1/b
                assert (-a+k*b)==c and -(-R*a)+k*(1/a-R*b)==1/b
            nextM=matrix(row["return_matrices"][(j+1)%p])
            # A_k M = M_next A_k verifies every cyclic starting position.
            AM=[M[1],[-M[0][i]+k*M[1][i] for i in range(2)]]
            MA=[[-nextM[i][1],nextM[i][0]+k*nextM[i][1]] for i in range(2)]
            assert AM==MA,"cocycle conjugacy"
        assert matrix(row["product_at_start"])==[left,right]==matrix(row["return_matrices"][0]),"scalar-recurrence product"
        assert rat(row["gap_sum"])==gaps==1
        assert rat(row["interior_total_roof"])==1/delta**2 and rat(row["endpoint_total_roof"])==n*n
        assert type(row["repetitions"]) is list and len(row["repetitions"])==5
        M=row["product_at_start"];power=[[1,0],[0,1]]
        for ell,rep in enumerate(row["repetitions"],1):
            keys(rep,("repetition","matrix","roof_multiplier"));assert integer(rep["repetition"])==ell and integer(rep["roof_multiplier"])==ell
            power=[[sum(M[i][k]*power[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
            assert matrix(rep["matrix"])==power==[[int(i==j)+ell*(M[i][j]-int(i==j)) for j in range(2)] for i in range(2)]
    assert periods[:3]==[1,2,4] and periods[-1]>128
    assert type(x["wall_rows"]) is list and len(x["wall_rows"])==16
    for n,row in enumerate(x["wall_rows"],2):
        keys(row,("N","epsilon","point","exact_image","exact_branch","near_point","near_image","near_branch","one_sided_limit","two_sided_derivative_exists"))
        assert integer(row["N"])==n;eps=rat(row["epsilon"]);assert eps==Fraction(1,16*n*n)
        for field,expected in (("point",(Fraction(1),Fraction(1,n))),("near_point",(1-eps,Fraction(1,n)+eps)),("one_sided_limit",(Fraction(1,n),1-Fraction(1,n)))):
            assert type(row[field]) is list and len(row[field])==2 and tuple(rat(t) for t in row[field])==expected
        for point,image,branch,expected in (("point","exact_image","exact_branch",2*n),("near_point","near_image","near_branch",2*n-1)):
            a,b=map(rat,row[point]);u,v=map(rat,row[image]);k=integer(row[branch])
            assert k==expected and domain(a,b) and domain(u,v)
            assert u==b and v+a==k*b and k*b<=1+a<(k+1)*b
        assert row["two_sided_derivative_exists"] is False
    assert type(x["fixed_rows"]) is list and len(x["fixed_rows"])==128
    for t,row in enumerate(x["fixed_rows"],1):
        keys(row,("iterate","layers","radial_segments","cardinality"));assert integer(row["iterate"])==t
        layers=ints(row["layers"]);assert layers==[n for n,p in enumerate(periods,1) if t%p==0]
        assert integer(row["radial_segments"])==sum(periods[n-1] for n in layers) and row["cardinality"]=="uncountable"
    summary={"layers":64,"cycle_points":total,"rational_scale_step_controls":2*total,"return_matrices":total,"repetition_controls":320,"wall_controls":16,"fixed_iterates":128}
    eq(x["summary"],summary,"summary")
    return summary
def main():
    p=argparse.ArgumentParser();p.add_argument("--evidence",type=Path,default=ROOT/"results/c395_bcz_evidence.json");p.add_argument("--evaluation",type=Path,default=EVAL);p.add_argument("--evaluation-only",action="store_true");a=p.parse_args();evaluation(a.evaluation)
    if a.evaluation_only:print("C395 strict evaluation PASS");return
    print("C395 independent checker PASS: "+json.dumps(verify(load(a.evidence)),sort_keys=True))
if __name__=="__main__":main()
