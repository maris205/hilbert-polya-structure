#!/usr/bin/env python3
"""Independent exact checker for C143; imports no producer module."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


def canonical_hash(data):
    work = dict(data)
    work.pop("payload_sha256", None)
    return sha256(json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def zmat(n): return [[Fraction(0) for _ in range(n)] for _ in range(n)]
def eye(n):
    a = zmat(n)
    for i in range(n): a[i][i] = 1
    return a
def trans(a): return [list(x) for x in zip(*a)]
def mul(a,b):
    out=[[Fraction(0) for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for k in range(len(b)):
            for j in range(len(b[0])): out[i][j]+=a[i][k]*b[k][j]
    return out
def tr(a): return sum(a[i][i] for i in range(len(a)))


def construct(word):
    coins={
        '0': ((Fraction(3,5),Fraction(4,5)),(Fraction(4,5),Fraction(-3,5))),
        '1': ((Fraction(5,13),Fraction(12,13)),(Fraction(12,13),Fraction(-5,13))),
    }
    d=2*len(word); s=zmat(d); c=zmat(d)
    for x,ch in enumerate(word):
        for i in range(2):
            for j in range(2): c[2*x+i][2*x+j]=coins[ch][i][j]
        s[2*((x+1)%len(word))+1][2*x]=1
        s[2*((x-1)%len(word))][2*x+1]=1
    return s,c,mul(s,c)


def coeff_from_traces(vals,dim):
    d=[Fraction(1)]
    for k in range(1,dim+1):d.append(-sum(d[k-j]*vals[j-1] for j in range(1,k+1))/k)
    return d


def fmt(x):
    x=Fraction(x);return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'


def rots(w): return [w[i:]+w[:i] for i in range(len(w))]
def primitive(w): return all(len(w)%d or w!=w[:d]*(len(w)//d) for d in range(1,len(w)))


def paths(u,cutoff):
    dim=len(u); adj=[[(r,u[r][c]) for r in range(dim) if u[r][c]] for c in range(dim)]; ans=[]
    for n in range(1,cutoff+1):
        count=0;amp=Fraction(0);cycles={}
        def rec(start,current,vertices,weight,left):
            nonlocal count,amp
            if left==0:
                if current==start:
                    count+=1;amp+=weight
                    w=tuple(vertices)
                    if primitive(w):cycles.setdefault(min(rots(w)),weight)
                return
            for target,value in adj[current]:
                rec(start,target,vertices if left==1 else vertices+[target],weight*value,left-1)
        for start in range(dim):rec(start,start,[start],Fraction(1),n)
        ans.append({'n':n,'rooted_closed_paths':count,'signed_amplitude_sum':fmt(amp),'primitive_cycle_count':len(cycles),'primitive_signed_weight_sum':fmt(sum(cycles.values(),Fraction(0)))})
    return ans


def main():
    parser=argparse.ArgumentParser();parser.add_argument('evidence',nargs='?',type=Path,default=Path(__file__).resolve().parents[1]/'results/c143_quantum_walk_evidence.json');args=parser.parse_args()
    data=json.loads(args.evidence.read_text());checks=0
    def check(cond,msg):
        nonlocal checks;checks+=1
        if not cond:raise AssertionError(msg)
    check(data['schema']=='hcs-c143-coined-walk-evidence-v1','schema')
    check(data['candidate_id']=='HCS-C143','candidate')
    check(data['scope_literal']=='NO_BAD_EULER_OR_ROOT_NUMBER','scope')
    check(data['payload_sha256']==canonical_hash(data),'hash')
    lock=data['source_lock']
    check(lock['basis_order']=='(0,+),(0,-),(1,+),(1,-),...,(4,+),(4,-)','basis')
    check(lock['clock']=='one coin-then-flip-flop-shift step','clock')
    check(lock['determinant_convention']=='D_w(z)=det(I_10-zU_w)','det')
    check(lock['cutoff']=={'matrix_dimension':10,'path':10,'trace':12},'cutoff')
    polys={};trace_ledgers={};max_absolute_column_sums=[]
    for word in ('00011','00101'):
        s,c,u=construct(word)
        check(mul(s,s)==eye(10),f'S2 {word}')
        check(mul(c,c)==eye(10),f'C2 {word}')
        check(mul(trans(u),u)==eye(10),f'unitary {word}')
        check(mul(mul(c,u),c)==mul(c,s),f'reversal {word}')
        power=[row[:] for row in u];vals=[]
        for n in range(1,13):
            vals.append(tr(power));power=mul(power,u)
            check(data['trace_ledgers'][word][n-1]=={'n':n,'trace_Un':fmt(vals[-1])},f'trace {word} {n}')
        coeff=coeff_from_traces(vals,10);polys[word]=coeff;trace_ledgers[word]=vals
        check(data['arrangement_control']['determinant_polynomials_ascending'][word]==[fmt(x) for x in coeff],f'poly {word}')
        check(coeff==list(reversed(coeff)),f'palindrome {word}')
        check(coeff[-1]==1,f'det U {word}')
        check(data['path_ledgers'][word]==paths(u,10),f'paths {word}')
        max_absolute_column_sums.append(max(sum(abs(u[row][column]) for row in range(10)) for column in range(10)))
    expected=[Fraction(0)]*11
    expected[2]=Fraction(196,4225);expected[4]=Fraction(-196,4225);expected[6]=Fraction(-196,4225);expected[8]=Fraction(196,4225)
    check([polys['00011'][i]-polys['00101'][i] for i in range(11)]==expected,'difference factor')
    check(data['arrangement_control']['dihedrally_equivalent'] is False,'dihedral')
    check(data['arrangement_control']['same_coin_population']=={'0':3,'1':2},'population')
    th=data['unitary_reversal_theorem'];check(th['unitary'] is True,'unitary flag');check(th['theta_square']=='I','theta2');check(th['reversal']=='Theta_w U_w Theta_w^(-1)=U_w^(-1)','theta reversal')
    neg=data['population_average_negative_control'];check(neg['orthogonality_defect']=='Cbar^T Cbar-I=-(24/1625)I','average defect');check(neg['determinant']=='-1601/1625','average determinant');check(neg['verdict']=='POPULATION_AVERAGING_DESTROYS_UNITARITY_AND_ORDER_INFORMATION','average verdict')
    check(data['raw_primitive_product_domain']=='absolute for |z|<5/7 by the maximum absolute column sum' and max_absolute_column_sums==[Fraction(7,5),Fraction(7,5)],'product domain and exact absolute-column majorant')
    check(data['route_a']['tuple']==['A1_WEAK','A2_FAIL','A3_FAIL','A4_UNITARY_OR_SCATTERING_CANDIDATE'],'tuple')
    check(data['route_a']['overall']=='ROUTE_A_EXPLORATORY','overall');check(data['route_a']['route_b_invocation_allowed'] is False,'routeb');check(all(v is False for v in data['claim_boundary'].values()),'boundary')
    print(json.dumps({'status':'PASS','assertions':checks},sort_keys=True))


if __name__=='__main__':main()
