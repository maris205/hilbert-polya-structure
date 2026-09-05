#!/usr/bin/env python3
"""Integer matrix/minor evidence; the all-period proof is separate."""
if not __debug__:
    raise RuntimeError("c397 producer refuses optimized Python")
import argparse, hashlib, json
from pathlib import Path
from itertools import combinations, permutations
from math import gcd
ROOT=Path(__file__).resolve().parents[1]
FLAGS=['claims_target_arithmetic_local_data','claims_target_euler_factors','claims_root_number','claims_automorphy','claims_target_divisor_or_counting_law','claims_target_functional_equation','claims_target_zero_match','claims_hilbert_polya_operator','invokes_route_b']
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def metadata():return {'schema':'hcs-exact-evidence-v1','candidate_id':'HCS-C397','source_commit':'697518b6db90458f86f7916fbf397b8ad5ef2372','fixed_epoch':1788566400,'scope_literal':'NO_BAD_EULER_OR_ROOT_NUMBER','scope_flags':{k:False for k in FLAGS},'route_a':{'tuple':['A0_WEAK_ARITHMETIC_RELATION','A1_WEAK','A2_FAIL','A3_FAIL','A4_FORMAL_HINT'],'overall_verdict':'ROUTE_A_REJECTED','route_b_invocation_allowed':False},'evidence_role':'finite exact regression; not an infinite theorem or target match'}
def det(M):
    n=len(M);total=0
    for p in permutations(range(n)):
        v=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        for i in range(n):v*=M[i][p[i]]
        total+=v
    return total
def mul(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def pmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def smith(M):
    divisors=[1]
    for k in range(1,5):
        g=0
        for i in combinations(range(4),k):
            for j in combinations(range(4),k):g=gcd(g,det([[M[r][s] for s in j] for r in i]))
        divisors.append(g)
    return [divisors[i+1]//divisors[i] for i in range(4)]
def build():
    d=metadata();d['families']=[]
    for a in (1,3,4,5,8):
        A=[[0,0,0,-1],[1,0,0,a],[0,1,0,1],[0,0,1,a]]
        power=[[int(i==j) for j in range(4)] for i in range(4)];periods=[];primitive={}
        for n in range(1,25):
            power=mul(power,A);B=[[power[i][j]-int(i==j) for j in range(4)] for i in range(4)]
            signed=det(B);fixed=abs(signed);least=fixed-sum(j*v for j,v in primitive.items() if n%j==0)
            assert least%n==0;primitive[n]=least//n
            periods.append({'n':n,'return_matrix':B,'signed_determinant':signed,'fixed':fixed,'smith':smith(B),'primitive_cycles':primitive[n]})
        P=[1,-a,-1,-a,1];Q=[1,3,a*a+4,3,1]
        d['families'].append({'a':a,'matrix':A,'polynomial':P,'zeta_numerator':pmul([1,-4,6,-4,1],Q),'zeta_denominator':pmul(P,P),'periods':periods})
    d['boundary']=[];A=[[0,0,0,-1],[1,0,0,2],[0,1,0,1],[0,0,1,2]];power=[[int(i==j) for j in range(4)] for i in range(4)]
    for n in range(1,13):
        power=mul(power,A);B=[[power[i][j]-int(i==j) for j in range(4)] for i in range(4)]
        d['boundary'].append({'a':2,'n':n,'signed_determinant':det(B),'identity_component_dimension':2 if n%3==0 else 0,'cardinality':'infinite' if n%3==0 else str(abs(det(B)))})
    d['controls']={'primitive_limit_mean':[2,1],'primitive_limit_variance':[2,1],'primitive_cluster_endpoints':[[0,1],[4,1]],'homoclinic_group':'trivial for all a>=1,a!=2','clock':'integer iteration, not log-prime','zeta_not_koopman_determinant':'unitary infinite-dimensional Koopman is noncompact'}
    return d
def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=ROOT/'results/c397_salem_evidence.json');a=p.parse_args();d=build();d['payload_sha256']=hashlib.sha256(canonical(d)).hexdigest();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,sort_keys=True,indent=2)+'\n');print('C397 producer PASS: '+d['payload_sha256'])
if __name__=='__main__':main()
