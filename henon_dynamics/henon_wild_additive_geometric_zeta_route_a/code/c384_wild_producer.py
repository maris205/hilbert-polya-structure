#!/usr/bin/env python3
"""Exact source data, polynomial Euclid and direct finite-field recounts."""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import comb, isqrt
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
SOURCE='3e692da6fa94362225c7534e9b66c83c15c7f284'
PRIMES=[2,3,5,7,11,13,17,19,23,29,31,37,41,43]
ROUTE=['A0_STRUCTURAL_ARITHMETIC_RELATION','A1_WEAK','A2_FAIL','A3_FAIL','A4_FAIL']
FLAGS=['claims_target_arithmetic_local_data','claims_target_euler_factors','claims_root_number',
 'claims_automorphy','claims_target_divisor_or_counting_law','claims_target_functional_equation',
 'claims_target_zero_match','claims_hilbert_polya_operator','invokes_route_b']

def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def rem(a,b,p):
    a=trim([x%p for x in a]);b=trim([x%p for x in b])
    while a!=[0] and len(a)>=len(b):
        j=len(a)-len(b);c=a[-1]*pow(b[-1],-1,p)%p
        for k,x in enumerate(b):a[j+k]=(a[j+k]-c*x)%p
        trim(a)
    return a

def gcd(a,b,p):
    while b!=[0]:a,b=b,rem(a,b,p)
    inv=pow(a[-1],-1,p)
    return [x*inv%p for x in a]

def orderpart(n,p):
    e=1
    while n%p==0:n//=p;e*=p
    return e

def divisors(n):return [d for d in range(1,n+1) if n%d==0]

def mobius(n):
    sign=1
    for p in range(2,isqrt(n)+1):
        if n%p==0:
            n//=p;sign=-sign
            if n%p==0:return 0
    return -sign if n>1 else sign

def fraction(x):return [x.numerator,x.denominator]

def digits(x,p,r):
    out=[]
    for _ in range(r):out.append(x%p);x//=p
    return out

def modulus(p,r):
    if r==1:return [0,1]
    for num in range(1,p**r):
        a=digits(num,p,r)+[1]
        if a[0]==0:continue
        if all(rem(a,[-x%p,1],p)!=[0] for x in range(p)):
            return a
    raise ValueError('no small irreducible')

def field_product(x,y,p,mod):
    r=len(mod)-1;a=digits(x,p,r);b=digits(y,p,r);c=[0]*(2*r-1)
    for j,u in enumerate(a):
        for k,v in enumerate(b):c[j+k]=(c[j+k]+u*v)%p
    c=rem(c,mod,p)+[0]*r
    return sum(c[i]*p**i for i in range(r))

def field_power(x,k,p,mod):
    y=1
    while k:
        if k&1:y=field_product(y,x,p,mod)
        x=field_product(x,x,p,mod);k//=2
    return y

def evidence():
    periods=[]
    for p in PRIMES:
        counts={n:p**(n-orderpart(n,p)) for n in range(1,97)}
        for n in range(1,97):
            e=orderpart(n,p)
            periods.append(dict(p=p,n=n,valuation_power=e,geometric=counts[n],
              multiplicity=p**e,scheme_length=p**n,
              primitive_cycles=sum(mobius(n//d)*counts[d] for d in divisors(n))//n))
    extensions=[];lookup={}
    for p in PRIMES[:5]:
        for n in range(1,49):
            a=[comb(n,j)%p for j in range(n+1)];a[0]=(a[0]-1)%p
            for r in range(1,25):
                b=[p-1]+[0]*(r-1)+[1];g=gcd(a,b,p)
                lookup[p,n,r]=p**(len(g)-1)
                extensions.append(dict(p=p,n=n,r=r,gcd=g,count=lookup[p,n,r]))
    for row in extensions:
        p,n,r=row['p'],row['n'],row['r']
        exact=sum(mobius(n//a)*mobius(r//b)*lookup[p,a,b]
                  for a in divisors(n) for b in divisors(r))
        row.update(exact_period_degree_points=exact,exact_degree_cycles=exact//n)
    controls=[]
    for p in PRIMES[:5]:
        for a in range(p):
            order=0
            if a:
                order=1
                while pow(a,order,p)!=1:order+=1
            for n in range(1,33):
                e=orderpart(n,p) if a and n%order==0 else 0
                controls.append(dict(p=p,a=a,n=n,unit_order=order,geometric=p**(n-e)))
    recounts=[]
    for p in [2,3,5]:
        for r in [1,2,3]:
            mod=modulus(p,r);q=p**r;mapping=[]
            for x in range(q):
                y=field_power(x,p,p,mod)
                mapping.append(sum(((x//p**j+y//p**j)%p)*p**j for j in range(r)))
            it=list(range(q));counts=[]
            for n in range(1,13):
                it=[mapping[x] for x in it]
                counts.append(sum(y==x for x,y in enumerate(it)))
            recounts.append(dict(p=p,r=r,modulus=mod,counts=counts))
    residues=[];tails=[]
    for p in [2,3,5]:
        c=[Fraction(1,p)]+[Fraction(1,p**(p**k))-Fraction(1,p**(p**(k-1))) for k in range(1,5)]
        for k in [1,2,3]:
            partial=sum(c[j]/p**j for j in range(k,5))
            tail=Fraction(1,p**(5+p**4))
            residues.append(dict(p=p,K=k,J=4,residue_lower=fraction(-partial),
                residue_upper=fraction(-partial+tail),universal_upper=fraction(Fraction(1,p**(k+p**(k-1))))))
        for k in range(3):
            for rho in [Fraction(1,2),Fraction(3,4)]:
                t=rho**(p**(k+1));bound=Fraction(1,p**(p**k))*t/(1-t)
                tails.append(dict(p=p,K=k,rho=fraction(rho),bound=fraction(bound)))
    payload=dict(schema='hcs-c384-wild-v1',candidate_id='HCS-C384',source_commit=SOURCE,
      scope_literal='NO_BAD_EULER_OR_ROOT_NUMBER',route_tuple=ROUTE,
      scope_flags={k:False for k in FLAGS},route_b_invocation_allowed=False,
      source=dict(map='x+x^p',space='A1(Fbar_p)',clock='iterate n',arithmetic_clock='extension r',
       geometric_zeta='exp(sum N_n z^n/n)',length_zeta='1/(1-p*z)',boundary='abs(z)=1/p'),
      grid=dict(primes=PRIMES,period_n_max=96,extension_primes=PRIMES[:5],extension_n_max=48,
       extension_r_max=24,period_rows=len(periods),extension_rows=len(extensions),control_rows=len(controls)),
      period_rows=periods,extension_rows=extensions,neighbor_controls=controls,
      direct_field_recounts=recounts,residue_intervals=residues,interior_tail_bounds=tails,
      composite_characteristic_controls=[dict(label=c,admissible=False) for c in [6,10,12,14,15,18,20,21,22,24]],
      proof_scope='all primes p, n>=1 and r>=1; finite grid is regression only')
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    return dict(payload=payload,payload_sha256=sha256(raw).hexdigest())

def main():
    if sys.flags.optimize:raise RuntimeError('C384 producer refuses optimized Python')
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=ROOT/'results/c384_wild_evidence.json')
    args=ap.parse_args();data=evidence();args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    print('C384_PRODUCER_PASS payload_sha256='+data['payload_sha256'])

if __name__=='__main__':main()
