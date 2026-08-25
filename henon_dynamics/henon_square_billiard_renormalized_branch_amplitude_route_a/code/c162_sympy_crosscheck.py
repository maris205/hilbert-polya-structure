#!/usr/bin/env python3
"""SymPy branch-limit crosscheck for HCS-C162."""
import json
import sympy as sp

def main():
    eps,t=sp.symbols("eps t",positive=True,real=True)
    # Principal-branch algebra: eps^2-2*i*t*eps=eps*(eps-2*i*t).
    reduced=(eps-sp.I*t)/(2*sp.pi)*(eps-2*sp.I*t)**(-sp.Rational(3,2))
    limit=sp.limit(reduced,eps,0,dir="+")
    expected=sp.exp(sp.I*sp.pi/4)/(2**sp.Rational(5,2)*sp.pi*sp.sqrt(t))
    assert sp.simplify(sp.expand_complex(limit-expected))==0
    checks=1
    N,r=sp.symbols("N r",positive=True,real=True)
    substituted=sp.simplify(expected.subs(t,2*sp.sqrt(N))*r)
    target=r*sp.exp(sp.I*sp.pi/4)/(8*sp.pi*N**sp.Rational(1,4))
    assert sp.simplify(substituted-target)==0;checks+=1
    # A coincident simple pole is killed by eps^(3/2).
    assert sp.limit(eps**sp.Rational(3,2)/eps,eps,0,dir="+")==0;checks+=1
    for value in (1,2,5,13,65,325):
        symbolic=target.subs({N:value,r:8})
        numeric=complex(sp.N(symbolic,50))
        assert abs(numeric.real-numeric.imag)<1e-45;checks+=1
    print(json.dumps({"status":"C162_SYMPY_PASS","checks":checks},sort_keys=True))
if __name__=="__main__":main()
