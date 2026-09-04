#!/usr/bin/env python3
"""Independent symbolic lane for HCS-C368."""
from __future__ import annotations
import sys
import sympy as s

def main():
    if sys.flags.optimize: raise RuntimeError('C368 SymPy lane refuses optimized Python')
    a,br,bi,q=s.symbols('a br bi q', real=True, nonzero=True)
    D=a**2-4*(br**2+bi**2); ad=a*q/D; bdr=-2*q*br/D; bdi=-2*q*bi/D; checks=0
    assert s.simplify(a*bdr+2*ad*br)==0; checks+=1
    assert s.simplify(a*bdi+2*ad*bi)==0; checks+=1
    assert s.simplify(a*ad+2*(br*bdr+bi*bdi)-q)==0; checks+=1
    assert s.simplify(2*a*ad*br+a**2*bdr)==0; checks+=1
    assert s.simplify(2*a*ad*bi+a**2*bdi)==0; checks+=1
    assert s.simplify(2*a*ad+4*(br*bdr+bi*bdi)-2*q)==0; checks+=1
    assert s.simplify(2*a*ad-2*a**2*q/D)==0; checks+=1
    u,K2,uc=s.symbols('u K2 uc', positive=True)
    FF=u+2*K2/u**2
    assert s.diff(FF,u)==1-4*K2/u**3; checks+=1
    assert s.simplify(FF.subs({u:uc,K2:uc**3/4})-3*uc/2)==0; checks+=1
    assert s.simplify((1-4*K2/u**3).subs(K2,uc**3/4)-(1-(uc/u)**3))==0; checks+=1
    t,M00,T=s.symbols('t M00 T', real=True)
    assert s.diff(M00+2*q*t,t)==2*q; checks+=1
    assert s.simplify(s.solve(s.Eq(M00+2*q*T,3*uc/2),T)[0]-(M00-3*uc/2)/(-2*q))==0; checks+=1
    z1,z2,b=s.symbols('z1 z2 b')
    assert s.factor((a*z1+b*z1**2)-(a*z2+b*z2**2))==(z1-z2)*(a+b*z1+b*z2); checks+=1
    B,h=s.symbols('B h', positive=True, real=True); phi=s.symbols('phi', real=True)
    bc=B*s.exp(s.I*phi); zetac=-s.exp(-s.I*phi)
    assert s.simplify(2*B*zetac+bc*zetac**2+s.conjugate(bc))==0; checks+=1
    w=s.expand_complex(B*(-2*s.exp(s.I*h)+s.exp(2*s.I*h)+1))
    re=s.series(s.re(w),h,0,5).removeO(); im=s.series(s.im(w),h,0,5).removeO()
    assert s.simplify(re-(-B*h**2+s.Rational(7,12)*B*h**4))==0; checks+=1
    assert s.simplify(im-(-B*h**3))==0; checks+=1
    X=-re; Y=-im
    assert s.limit(Y**2/X**3,h,0)==1/B; checks+=1
    th=s.symbols('th', real=True)
    bc=br+s.I*bi; z=a*s.exp(s.I*th)+bc*s.exp(2*s.I*th); zth=s.diff(z,th)
    integrand=s.simplify(s.im(s.conjugate(z)*zth)/2)
    area=s.integrate(s.expand_trig(integrand),(th,0,2*s.pi))
    assert s.simplify(area-s.pi*(a**2+2*(br**2+bi**2)))==0; checks+=1
    # On the circular face the scalar radius equation closes exactly.
    ac=s.symbols('ac', positive=True)
    assert s.simplify((ac*q/ac**2)-q/ac)==0; checks+=1
    assert s.integrate(2*q,t)==2*q*t; checks+=1
    print(f'C368 SymPy cross-check: PASS ({checks} exact checks)')
if __name__=='__main__': main()
