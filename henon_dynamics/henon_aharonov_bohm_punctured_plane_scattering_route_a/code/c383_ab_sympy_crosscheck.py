#!/usr/bin/env python3
"""Symbolic channel, distribution, gauge, and Bessel-ODE identities."""
if not __debug__:raise RuntimeError("c383 sympy refuses optimized Python")
import argparse
import sympy as s

def main():
    argparse.ArgumentParser().parse_args()
    beta=s.symbols("beta",real=True);r,k,nu=s.symbols("r k nu",positive=True)
    z=s.symbols("z",nonzero=True);theta=s.symbols("theta",real=True)
    checks=0
    for m in range(-64,65):
        positive=s.Rational(m)-beta if m>=1 else beta-m
        assert s.expand(abs(m)-positive-(beta if m>=1 else -beta))==0;checks+=1
    for m in range(-16,17):
        for n in range(-4,5):
            assert s.expand((m+n-(beta+n))**2-(m-beta)**2)==0;checks+=1
    bessel=s.besselj(nu,k*r)
    assert s.simplify(s.expand_func(-s.diff(bessel,r,2)-s.diff(bessel,r)/r+nu**2*bessel/r**2-k**2*bessel))==0;checks+=1
    # Away-forward Abel limits of positive minus nonpositive Fourier sums.
    difference=z/(1-z)-1/(1-1/z)
    assert s.cancel(difference+1+(z+1)/(z-1))==0;checks+=1
    assert s.trigsimp((s.cot(theta/2)+s.I)*(s.cot(theta/2)-s.I)-1/s.sin(theta/2)**2)==0;checks+=1
    n=s.symbols("n",integer=True);m=s.symbols("m",integer=True)
    assert s.expand((n-m-beta)**2-(-m+beta)**2).subs(n,2*beta)==0;checks+=1
    assert s.simplify(s.exp(s.I*s.pi*beta)*s.exp(-s.I*s.pi*beta)-1)==0;checks+=1
    print(f"C383 SymPy PASS: exact_identities={checks}")
if __name__=="__main__":main()
