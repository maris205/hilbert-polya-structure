#!/usr/bin/env python3
"""Independent exact verifier: no producer import and no symbolic algebra."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c388 checker refuses optimized Python")
import argparse
from fractions import Fraction
import hashlib
import json
from math import gcd,prod
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
EVAL=ROOT/"evaluations/route_a/HCS-C388/2026-09-05.yaml"
EVAL_SHA="37803e9b1d795598c95a84ab557521b40df29f96d574c5ed3b507caa921dcd44"
EVAL_DATA_SHA="143d37185c4509ba238947c93bcebae572bbda7f7911e961779838e17ad842f0"
FLAGS={"claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b"}
TUPLE=["A0_WEAK_ARITHMETIC_RELATION","A1_WEAK","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"]
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def pairs(items):
    out={}
    for k,v in items:
        assert k not in out,"duplicate key";out[k]=v
    return out
def load(path):return json.loads(path.read_text(),object_pairs_hook=pairs,parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))
def keys(x,names):assert type(x) is dict and set(x)==set(names),"key set"
def ints(xs):assert type(xs) is list and all(type(x) is int for x in xs),"integer type"
def mat(x,n):assert type(x) is list and len(x)==n;[ints(r) for r in x];assert all(len(r)==n for r in x)
def mul(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def determinant(A):
    n=len(A);m=[r[:] for r in A];sign=1;prev=1
    for k in range(n-1):
        p=next((i for i in range(k,n) if m[i][k]),None)
        if p is None:return 0
        if p!=k:m[p],m[k]=m[k],m[p];sign=-sign
        pivot=m[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                q=m[i][j]*pivot-m[i][k]*m[k][j];assert q%prev==0;m[i][j]=q//prev
            m[i][k]=0
        prev=pivot
    return sign*m[-1][-1] if n else 1
def charpoly(A):
    n=len(A);B=eye(n);out=[1]
    for k in range(1,n+1):
        B=mul(A,B);t=sum(B[i][i] for i in range(n));assert t%k==0
        c=-t//k;out.append(c)
        for i in range(n):B[i][i]+=c
    assert all(v==0 for row in B for v in row)
    return out
def expected_matrix(a,b,c):
    n=a*c;A=[[0]*n for _ in range(n)]
    # Generate quotient addition by the two HNF relations, independently.
    reps=[(i,j) for i in range(a) for j in range(c)]
    where={p:k for k,p in enumerate(reps)}
    for k,(i,j) in enumerate(reps):
        A[k][k]+=1;A[k][where[((i+1)%a,j)]]+=1
        dest=(i,j+1) if j+1<c else ((i-b)%a,0)
        A[k][where[dest]]+=1
    return A
def expected_grid():
    out=[]
    for n in range(1,37):
        for a in range(1,n+1):
            if n%a:continue
            c=n//a
            if n<=12 or (a,c) in ((3,6),(6,3),(6,6)):
                out.extend((a,b,c) for b in range(a))
    return sorted(out,key=lambda v:(v[0]*v[2],v))
def evaluation(path=EVAL):
    raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==EVAL_SHA,"evaluation raw hash"
    class UniqueLoader(yaml.SafeLoader):pass
    def mapping(loader,node,deep=False):return pairs(loader.construct_pairs(node,deep=deep))
    UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,mapping)
    x=yaml.load(raw,Loader=UniqueLoader)
    assert hashlib.sha256(canonical(x)).hexdigest()==EVAL_DATA_SHA,"evaluation structure/type hash"
    assert type(x["evaluation_date"]) is str and x["evaluation_date"]=="2026-09-05"
    assert type(x["fixed_epoch"]) is int and x["fixed_epoch"]==1788566400
    assert x["tuple"]==TUPLE and x["route_b_invocation_allowed"] is False
    assert set(x["scope_flags"])==FLAGS and all(v is False for v in x["scope_flags"].values())
    return x
def verify(x):
    keys(x,("schema","candidate_id","obstruction_id","source_commit","fixed_epoch","scope_literal","scope_flags","route_a","contract","lattice_rows","torus_rows","dirichlet_rows","summary","payload_sha256"))
    claimed=x["payload_sha256"];payload={k:v for k,v in x.items() if k!="payload_sha256"};assert type(claimed) is str and hashlib.sha256(canonical(payload)).hexdigest()==claimed,"payload digest"
    assert x["schema"]=="c388-connected-algebraic-evidence-v1" and x["candidate_id"]=="HCS-C388" and x["obstruction_id"]=="HEN-O372"
    assert x["source_commit"]=="3e692da6fa94362225c7534e9b66c83c15c7f284" and type(x["fixed_epoch"]) is int and x["fixed_epoch"]==1788566400
    assert x["scope_literal"]=="NO_BAD_EULER_OR_ROOT_NUMBER";keys(x["scope_flags"],FLAGS);assert all(v is False for v in x["scope_flags"].values())
    keys(x["route_a"],("tuple","route_b_invocation_allowed"));assert x["route_a"]["tuple"]==TUPLE and x["route_a"]["route_b_invocation_allowed"] is False
    assert canonical(x["contract"])==canonical({"source_polynomial":"1+u+v","hnf":"columns (a,0),(b,c); a,c>0; 0<=b<a","grid":"all HNF index <=12 plus (a,c)=(3,6),(6,3),(6,6)","rational_torus_denominators":[1,24],"evidence_role":"finite exact certificates; not proof of universal claims"})
    assert type(x["lattice_rows"]) is list and [tuple(r["hnf"]) for r in x["lattice_rows"]]==expected_grid(),"complete ordered lattice grid"
    for row in x["lattice_rows"]:
        keys(row,("hnf","index","resonant","matrix","smith_diagonal","left_unimodular","right_unimodular","rank","torus_dimension","component_count","characteristic_polynomial","nonzero_eigenvalue_product_abs","kernel_gram","kernel_gram_determinant"))
        ints(row["hnf"]);a,b,c=row["hnf"];n=a*c
        for k in ("index","rank","torus_dimension","component_count","nonzero_eigenvalue_product_abs","kernel_gram_determinant"):assert type(row[k]) is int
        assert row["index"]==n and type(row["resonant"]) is bool
        resonance=(a%3==0 and (b-c)%3==0);null=2 if resonance else 0
        assert row["resonant"] is resonance and row["torus_dimension"]==null and row["rank"]==n-null
        A=row["matrix"];U=row["left_unimodular"];V=row["right_unimodular"]
        for M in (A,U,V):mat(M,n)
        assert A==expected_matrix(a,b,c),"quotient matrix"
        assert abs(determinant(U))==abs(determinant(V))==1,"unimodular witnesses"
        d=row["smith_diagonal"];ints(d);assert len(d)==n and all(v>0 for v in d[:n-null]) and all(v==0 for v in d[n-null:])
        assert all(d[i+1]%d[i]==0 for i in range(n-null-1)),"Smith divisibility"
        assert mul(mul(U,A),V)==[[d[i] if i==j else 0 for j in range(n)] for i in range(n)],"Smith factorization"
        cp=row["characteristic_polynomial"];ints(cp);assert cp==charpoly(A),"characteristic polynomial"
        pdet=abs(cp[n-null]);assert row["nonzero_eigenvalue_product_abs"]==pdet
        assert row["component_count"]==prod(d[:n-null])
        if resonance:
            assert 3*pdet==n*n*row["component_count"],"covolume correction"
            mat(row["kernel_gram"],2)
            basis=[[((1,0,-1),(0,1,-1))[k][(i-j)%3] for i in range(a) for j in range(c)] for k in range(2)]
            assert all(v==0 for r in mul(A,list(map(list,zip(*basis)))) for v in r)
            gram=mul(basis,list(map(list,zip(*basis))))
            assert row["kernel_gram"]==gram and row["kernel_gram_determinant"]==determinant(gram)==n*n//3
        else:assert row["kernel_gram"]==[] and row["kernel_gram_determinant"]==1 and row["component_count"]==pdet
    assert type(x["torus_rows"]) is list and len(x["torus_rows"])==24
    for q,row in enumerate(x["torus_rows"],1):
        keys(row,("denominator","state_count","fixed_count","period_three_cycles","cycles"))
        for k in ("denominator","state_count","fixed_count","period_three_cycles"):assert type(row[k]) is int
        assert row["denominator"]==q and row["state_count"]==q*q
        assert row["fixed_count"]==gcd(q,3) and row["period_three_cycles"]==(q*q-gcd(q,3))//3
        seen=set();lengths=[];starts=[]
        for cycle in row["cycles"]:
            assert type(cycle) is list and len(cycle) in (1,3)
            pts=[]
            for p in cycle:ints(p);assert len(p)==2 and all(0<=v<q for v in p);pts.append(tuple(p))
            assert len(set(pts))==len(pts) and pts[0]==min(pts)
            for p,t in zip(pts,pts[1:]+pts[:1]):assert t==(p[1],(-p[0]-p[1])%q)
            assert not (seen&set(pts));seen.update(pts);lengths.append(len(pts));starts.append(pts[0])
        assert starts==sorted(starts) and len(seen)==q*q and lengths.count(1)==gcd(q,3)
    assert len(x["dirichlet_rows"])==8
    for h,row in zip((1,2,4,8,16,32,64,128),x["dirichlet_rows"]):
        keys(row,("paired_terms","partial_sum","tail_upper"));assert type(row["paired_terms"]) is int and row["paired_terms"]==h
        for k in ("partial_sum","tail_upper"):ints(row[k]);assert len(row[k])==2 and row[k][1]>0 and gcd(*row[k])==1
        direct=sum((Fraction((1 if n%3==1 else -1),n*n) for n in range(1,3*h) if n%3),Fraction())
        assert Fraction(*row["partial_sum"])==direct
        assert Fraction(*row["tail_upper"])==Fraction(2,(3*h+1)**3)+Fraction(1,3*(3*h+1)**2)
    summary={"lattice_count":len(x["lattice_rows"]),"resonant_count":sum(r["resonant"] for r in x["lattice_rows"]),"nonresonant_count":sum(not r["resonant"] for r in x["lattice_rows"]),"torus_state_count":sum(q*q for q in range(1,25)),"dirichlet_bound_count":8}
    keys(x["summary"],summary);assert all(type(v) is int for v in x["summary"].values()) and x["summary"]==summary
    return summary
def main():
    p=argparse.ArgumentParser();p.add_argument("--evidence",type=Path,default=ROOT/"results/c388_algebraic_evidence.json");p.add_argument("--evaluation",type=Path,default=EVAL);p.add_argument("--evaluation-only",action="store_true");a=p.parse_args()
    evaluation(a.evaluation)
    if a.evaluation_only:print("C388 strict evaluation PASS");return
    print("C388 independent checker PASS: "+json.dumps(verify(load(a.evidence)),sort_keys=True))
if __name__=="__main__":main()
