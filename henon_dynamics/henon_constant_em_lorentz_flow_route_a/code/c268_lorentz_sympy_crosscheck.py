#!/usr/bin/env python3
"""Symbolic E/B sign, characteristic, projector, flow, and null checks."""
import sympy as s
def main():
 e1,e2,e3,b1,b2,b3,k=s.symbols('e1 e2 e3 b1 b2 b3 k',real=True);z=s.symbols('z');checks=0
 A=k*s.Matrix([[0,e1,e2,e3],[e1,0,b3,-b2],[e2,-b3,0,b1],[e3,b2,-b1,0]]);eta=s.diag(1,-1,-1,-1)
 assert A.T*eta+eta*A==s.zeros(4);checks+=16
 E2=e1**2+e2**2+e3**2;B2=b1**2+b2**2+b3**2;EB=e1*b1+e2*b2+e3*b3
 expected=z**4+k**2*(B2-E2)*z**2-k**4*EB**2
 assert s.expand(A.charpoly(z).as_expr()-expected)==0;checks+=1
 assert s.simplify(s.trace(A**2)-2*k**2*(E2-B2))==0;checks+=1
 assert s.simplify(A.det()+k**4*EB**2)==0;checks+=1
 # Abstract projector algebra modulo X^2-(a2-b2)X-a2*b2 for X=A^2.
 X,alpha2,beta2=s.symbols('X alpha2 beta2',nonnegative=True);D=alpha2+beta2;rel=X**2-(alpha2-beta2)*X-alpha2*beta2
 rem=lambda p:s.rem(s.together(p*D**2).as_numer_denom()[0],rel,X)
 Ph=(X+beta2)/D;Pr=(-X+alpha2)/D
 for expr in (Ph+Pr-1,Ph**2-Ph,Pr**2-Pr,Ph*Pr):assert s.factor(rem(expr))==0;checks+=1
 # Coefficient-wise differential equation for the closed exponential.
 t,a,b=s.symbols('t a b',positive=True,real=True)
 ch=s.cosh(a*t);sh=s.sinh(a*t)/a;co=s.cos(b*t);si=s.sin(b*t)/b
 assert s.diff(ch,t)==a**2*sh;checks+=1
 assert s.diff(sh,t)==ch;checks+=1
 assert s.diff(co,t)==-b**2*si;checks+=1
 assert s.diff(si,t)==co;checks+=1
 # The chosen mixed tensor gives gamma*(E+v cross B) spatial force.
 g,v1,v2,v3=s.symbols('g v1 v2 v3');u=s.Matrix([g,g*v1,g*v2,g*v3]);f=s.expand(A*u/k)
 target=s.Matrix([g*(e1*v1+e2*v2+e3*v3),g*(e1+v2*b3-v3*b2),g*(e2-v1*b3+v3*b1),g*(e3+v1*b2-v2*b1)])
 assert s.simplify(f-target)==s.zeros(4,1);checks+=4
 # Concrete nonzero null field E=(1,0,0), B=(0,1,0).
 N=A.subs({k:1,e1:1,e2:0,e3:0,b1:0,b2:1,b3:0})
 assert N**3==s.zeros(4);checks+=16
 assert N**2!=s.zeros(4);checks+=1
 tau=s.symbols('tau',real=True);U=s.eye(4)+tau*N+tau**2*N**2/2;Phi=tau*s.eye(4)+tau**2*N/2+tau**3*N**2/6
 assert s.diff(U,tau)==N*U;checks+=16
 assert s.diff(Phi,tau)==U;checks+=16
 assert s.simplify(U.T*eta*U-eta)==s.zeros(4);checks+=16
 # Exact rational specializations recheck Cayley-Hamilton without producer data.
 vals=(-2,-1,0,1,2)
 for j in range(32):
  sub={e1:vals[j%5],e2:vals[(j+1)%5],e3:vals[(j+2)%5],b1:vals[(2*j)%5],b2:vals[(2*j+1)%5],b3:vals[(2*j+2)%5],k:s.Rational((j%4)+1,(j%3)+1)}
  Q=A.subs(sub);poly=s.expand(expected.subs(sub));assert Q.charpoly(z).as_expr().expand()==poly;checks+=1
 print(f"C268_SYMPY_PASS ({checks} symbolic identities; convention/characteristic/projectors/null/flow)")
if __name__=="__main__":main()
