#!/usr/bin/env python3
"""Symbolic classical-flow and completed-square checks for HCS-C313."""
import math,sympy as sp
def main():
 t,s,R=sp.symbols("t s R",positive=True,real=True);ell,d=sp.symbols("ell d",integer=True,nonnegative=True);checks=0
 def zero(x,label):
  nonlocal checks
  if sp.simplify(sp.trigsimp(x).rewrite(sp.exp))!=0:raise AssertionError(label)
  checks+=1
 c=sp.cos(t/R);z=sp.sin(t/R);X2,V2,XV=sp.symbols("X2 V2 XV",real=True)
 xn=c*c*X2+R**2*z*z*V2+2*R*c*z*XV;vn=z*z*X2/R**2+c*c*V2-2*c*z*XV;dot=-c*z*X2/R+R*c*z*V2+(c*c-z*z)*XV
 zero(xn.subs({X2:R**2,V2:1,XV:0})-R**2,"sphere");zero(vn.subs({X2:R**2,V2:1,XV:0})-1,"speed");zero(dot.subs({X2:R**2,V2:1,XV:0}),"tangent")
 zero(ell*(ell+d-1)+(d-1)**2/sp.Integer(4)-(ell+(d-1)/2)**2,"completed square")
 for dim in range(2,21):
  total=0
  for l in range(0,31):
   m=(2*l+dim-1)*math.factorial(l+dim-2)//(math.factorial(l)*math.factorial(dim-1));total+=m
   zero(m-(math.comb(l+dim,dim)-(math.comb(l+dim-2,dim) if l>=2 else 0)),"multiplicity")
   zero(total-(math.comb(l+dim,dim)+(math.comb(l+dim-1,dim) if l>=1 else 0)),"cumulative")
  zero(sp.exp(-sp.I*2*sp.pi*(ell+sp.Rational(dim-1,2)))-(-1)**(dim-1),"2pi revival")
  zero(sp.exp(-sp.I*4*sp.pi*(ell+sp.Rational(dim-1,2)))-1,"4pi revival")
 print(f"C313 SymPy cross-check: PASS ({checks} identities)")
if __name__=="__main__":main()
