#!/usr/bin/env python3
"""Exact symbolic/rational cross-check lane for HCS-C332."""
import sys

import sympy as s

if sys.flags.optimize:
    raise RuntimeError("C332 SymPy lane refuses optimized Python")


def clamp(x,low,high): return min(high,max(low,x))
def P(z,m,M,r): return min(max(z,M-r),m+r)
def solve(levels,z,r):
    out=[z]
    for u in levels[1:]: out.append(clamp(out[-1],u-r,u+r))
    return out
def variation(values): return sum(abs(b-a) for a,b in zip(values,values[1:]))

checks=0
for m0 in range(-3,4):
    m=s.Rational(m0)
    for D0 in range(0,9):
        D=s.Rational(D0); M=m+D
        for r0 in range(0,6):
            r=s.Rational(r0)
            zs=[m] if r==0 else [m-r,m-r/2,m,m+r/2,m+r]
            outputs=[P(z,m,M,r) for z in zs]
            for z,p in zip(zs,outputs):
                if P(p,m,M,r)!=p: raise AssertionError("idempotence")
                checks+=1
            if outputs!=sorted(outputs): raise AssertionError("order")
            checks+=1
            for i in range(len(zs)-1):
                if abs(outputs[i+1]-outputs[i])>abs(zs[i+1]-zs[i]): raise AssertionError("nonexpansion")
                checks+=1
            rep=P(m,m,M,r); mid=(m+M)/2
            levels=[m,mid,M,M,mid,m]; y=solve(levels,rep,r); stop=[u-v for u,v in zip(levels,y)]
            if variation(y)!=2*max(D-2*r,0): raise AssertionError("play variation")
            if variation(levels)!=variation(y)+variation(stop): raise AssertionError("variation split")
            if any(abs(u-v)>r for u,v in zip(levels,y)): raise AssertionError("feasibility")
            stretched=[m,m,mid,mid,M,M,M,mid,mid,m,m]
            ys=solve(stretched,rep,r)
            if [ys[i] for i in (0,2,4,6,8,10)]!=y: raise AssertionError("reparameterization")
            checks+=4

print(f"C332 SymPy cross-check: PASS ({checks} exact identities)")
