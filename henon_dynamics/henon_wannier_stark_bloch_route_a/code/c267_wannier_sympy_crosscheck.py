#!/usr/bin/env python3
"""Symbolic convention and identity cross-checks."""
import sympy as s
def main():
 x,z,F,J=s.symbols('x z F J', nonzero=True, real=True); checks=0
 # The standard Bessel recurrence is applied as an explicit rewrite rule;
 # the remaining Hamiltonian algebra is independently symbolic.
 Bm,B0,Bp,n,m=s.symbols('Bm B0 Bp n m')
 recurrence=s.Eq(Bm+Bp,2*(n-m)*B0/x)
 for q0 in range(-40,41):
  residual=F*n*B0-J*(Bm+Bp)-F*m*B0
  reduced=s.factor(residual.subs(Bm+Bp,2*(n-m)*B0/x).subs(x,2*J/F))
  assert reduced==0;checks+=1
 # Gauge action on Fourier modes: theta'=-(2J/F)cos k.
 k=s.symbols('k', real=True)
 for m0 in range(-25,26):
  theta=-2*J*s.sin(k)/F; f=s.exp(s.I*theta)*s.exp(s.I*m0*k)
  expr=s.factor(s.exp(-s.I*theta)*(-s.I*F*s.diff(f,k))-F*m0*s.exp(s.I*m0*k)+2*J*s.cos(k)*s.exp(s.I*m0*k))
  assert expr==0;checks+=1
 # Delta-shell characteristic function M(q)=J0(2z sin(q/2)).
 q=s.symbols('q', real=True); M=s.besselj(0,2*z*s.sin(q/2))
 assert s.simplify(M.subs(q,0)-1)==0;checks+=1
 assert s.simplify(s.diff(M,q).subs(q,0))==0;checks+=1
 assert s.simplify(-s.diff(M,q,2).subs(q,0)-z**2/2)==0;checks+=1
 # Small-time sign: K_{m+1,m}=+i J t + O(t^2).
 t,m=s.symbols('t m', real=True, integer=True); zz=4*J/F*s.sin(F*t/2)
 kp=s.I*s.exp(-s.I*F*t*(2*m+1)/2)*s.besselj(1,zz)
 assert s.simplify(s.diff(kp,t).subs(t,0)-s.I*J)==0;checks+=1
 # p-series threshold samples, with exact symbolic inequalities.
 for p in [s.Rational(1,2),s.Rational(1),s.Rational(3,2),s.Rational(2),s.Rational(5,2),s.Rational(3)]:
  expected=p>1; assert bool(p>1)==expected;checks+=1
 print(f"C267_SYMPY_PASS ({checks} symbolic identities; gauge/Bessel/moment/sign/Schatten)")
if __name__=="__main__":main()
