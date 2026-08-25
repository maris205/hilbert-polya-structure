#!/usr/bin/env python3
"""Symbolic Birkhoff-polynomial and Gauss sentinels for HCS-C161."""
import json
from math import gcd
import sympy as sp


def main():
    x, j, n, a, b = sp.symbols("x j n a b", integer=True, nonnegative=True)
    expression = sp.summation(a*(x+j)**2+b*(x+j), (j, 0, n-1))
    expected = (a*n*x**2+(a*n*(n-1)+b*n)*x+
                a*n*(n-1)*(2*n-1)/6+b*n*(n-1)/2)
    assert sp.simplify(expression-expected) == 0
    g=(a-b)*x**2
    phi=lambda z:a*z**2+b*z
    assert sp.expand(g-g.subs(x,x-1)-phi(-x)+phi(x-1))==0
    assert sp.expand(g-g.subs(x,-x))==0
    checks = 3
    for q in range(3, 20, 2):
        root = sp.exp(2*sp.pi*sp.I/q)
        for aa, bb, nn in ((1,0,1),(1,1,2),(2,3,q-1),(q//3 if q%3==0 else 3,1,q)):
            A = aa*nn; B = aa*nn*(nn-1)+bb*nn
            d = gcd(A,q)
            total = sum(complex(sp.N(root**((A*z*z+B*z) % q), 30)) for z in range(q))
            assert (abs(total)<1e-11) == (B%d != 0); checks += 1
    for p in (3,5,7,11,13,17,19):
        for A in range(p):
            for B in range(p):
                for C in range(p):
                    direct = sum((A*z*z+B*z+C)%p == 0 for z in range(p))
                    if A:
                        delta=(B*B-4*A*C)%p
                        symbol=0 if delta==0 else (1 if pow(delta,(p-1)//2,p)==1 else -1)
                        predicted=1+symbol
                    elif B: predicted=1
                    else: predicted=p if C==0 else 0
                    assert direct == predicted; checks += 1
    print(json.dumps({"status":"C161_SYMPY_PASS","checks":checks},sort_keys=True))


if __name__ == "__main__": main()
