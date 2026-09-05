#!/usr/bin/env python3
"""Symbolic rational-map identities and direct angular periodic census."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c380 symbolic lane refuses optimized Python")
import argparse
import mpmath as mp
import sympy as s

def main():
    argparse.ArgumentParser().parse_args()
    a,z,u=s.symbols("a z u");B=z*(z-a)/(1-a*z);checks=0
    assert s.cancel(B.subs(z,1/z)-1/B)==0;checks+=1
    assert s.limit(B/z,z,0)==-a;checks+=1
    assert s.limit((1/B.subs(z,1/z))/z,z,0)==-a;checks+=1
    assert s.cancel(B.subs(a,1)+z)==0;checks+=1
    assert s.cancel(s.diff(B,z)-( -a*z**2+2*z-a)/(a*z-1)**2)==0;checks+=1
    assert s.simplify(s.diff(B,z).subs(z,1)-2/(1-a))==0;checks+=1
    assert s.simplify(s.diff(B,z).subs(z,-1)+2/(1+a))==0;checks+=1
    for av in (s.Rational(0),s.Rational(1,3),s.Rational(3,4)):
        P,Q=s.Poly(z,z),s.Poly(1,z)
        for n in range(1,6):
            P,Q=P*(P-av*Q),Q*(Q-av*P)
            assert s.gcd(P,Q).degree()==0;checks+=1
            circle=s.div(P-s.Poly(z,z)*Q,s.Poly(z,z))[0]
            assert circle.degree()==2**n-1;checks+=1
            assert s.gcd(circle,circle.diff()).degree()==0;checks+=1
    # Bisection of the monotone angular lift enumerates every fixed point,
    # independently of a polynomial root filter or matrix spectrum.
    mp.mp.dps=65;worst=mp.mpf(0);points=0
    for av in (mp.mpf(0),mp.mpf(1)/3,mp.mpf(3)/4):
        def step(x):return 2*x+2*mp.atan2(av*mp.sin(x),1-av*mp.cos(x))
        for n in range(1,6):
            total=mp.mpf(0)
            for j in range(2**n-1):
                lo,hi=mp.mpf(0),2*mp.pi
                if j==0:theta=lo
                else:
                    for _ in range(180):
                        mid=(lo+hi)/2;y=mid
                        for _ in range(n):y=step(y)
                        if y-mid<2*mp.pi*j:lo=mid
                        else:hi=mid
                    theta=(lo+hi)/2
                y=theta;mult=mp.mpf(1)
                for _ in range(n):
                    mult*=1+(1-av**2)/(1-2*av*mp.cos(y)+av**2)
                    y=step(y)
                residual=abs(y-theta-2*mp.pi*j)
                assert residual<mp.mpf("1e-48");checks+=1
                assert mult>1;checks+=1
                total+=1/(mult-1);points+=1
            expected=(1+(-av)**n)/(1-(-av)**n)
            worst=max(worst,abs(total-expected))
            assert abs(total-expected)<mp.mpf("1e-47");checks+=1
    print(f"C380 symbolic/direct-orbit PASS: checks={checks} direct_points={points} max_trace_residual={mp.nstr(worst,6)}")
if __name__=="__main__":main()
