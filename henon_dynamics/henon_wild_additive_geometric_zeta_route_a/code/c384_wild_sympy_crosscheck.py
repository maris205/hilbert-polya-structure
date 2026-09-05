#!/usr/bin/env python3
"""Symbolic binomial, Euclidean and primitive-product checks, independent of producer."""
from pathlib import Path
import json
import sys
import sympy as s

ROOT=Path(__file__).resolve().parents[1]

def main():
    if sys.flags.optimize:raise RuntimeError('C384 SymPy refuses optimized Python')
    data=json.loads((ROOT/'results/c384_wild_evidence.json').read_text())['payload'];T=s.Symbol('T');checks=0
    table={(x['p'],x['n'],x['r']):x for x in data['extension_rows']}
    for p in [2,3,5]:
        for n in range(1,21):
            e=1;m=n
            while m%p==0:m//=p;e*=p
            H=sum(s.binomial(m,j)*T**(j-1) for j in range(1,m+1))
            if not s.Poly((1+T)**n-1-T**e*H**e,T,modulus=p).is_zero:raise ValueError('symbolic inseparability')
            checks+=1
        for n in range(1,13):
            for r in range(1,9):
                g=s.gcd(s.Poly((1+T)**n-1,T,modulus=p),s.Poly(T**r-1,T,modulus=p)).monic()
                coef=[int(g.nth(j))%p for j in range(g.degree()+1)]
                if coef!=table[p,n,r]['gcd']:raise ValueError('SymPy gcd')
                checks+=1
    period={(r['p'],r['n']):r for r in data['period_rows']}
    for p in data['grid']['primes']:
        coefficients=[s.Integer(1)]
        for n in range(1,17):
            coefficients.append(s.cancel(sum(period[p,j]['geometric']*coefficients[n-j] for j in range(1,n+1))/n))
        product=[s.Integer(1)]+[s.Integer(0)]*16
        for n in range(1,17):
            k=period[p,n]['primitive_cycles']
            if k:
                factor=[s.Integer(0)]*17
                for j in range(17//n+1):
                    if j*n<=16:factor[j*n]=s.binomial(k+j-1,j)
                product=[sum(product[j]*factor[i-j] for j in range(i+1)) for i in range(17)]
        if product!=coefficients:raise ValueError('primitive product coefficients')
        if any(not x.is_Integer or x<0 for x in product):raise ValueError('integral zeta coefficients')
        checks+=34
    w=s.Symbol('w')
    if s.simplify(w*s.diff(-s.log(1-w),w)-w/(1-w))!=0:raise ValueError('length log derivative')
    checks+=1
    print('C384_SYMPY_PASS exact_checks='+str(checks))

if __name__=='__main__':main()
