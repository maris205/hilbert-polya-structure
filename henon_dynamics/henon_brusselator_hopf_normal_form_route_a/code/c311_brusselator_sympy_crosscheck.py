#!/usr/bin/env python3
"""Derive the C311 Hopf coefficient from the vector field in SymPy."""
import sympy as sp
def main():
 A=sp.symbols("A",positive=True,real=True);u,v=sp.symbols("u v",real=True);I=sp.I;B0=1+A**2;x=A+u;y=B0/A+v
 f=sp.Matrix([A-(B0+1)*x+x**2*y,B0*x-x**2*y]);z=[u,v];J=f.jacobian(z).subs({u:0,v:0});checks=0
 def zero(e,label):
  nonlocal checks
  values=list(e) if isinstance(e,sp.MatrixBase) else [e]
  if any(sp.simplify(value)!=0 for value in values):raise AssertionError(label)
  checks+=1
 zero(sp.trace(J),"trace");zero(J.det()-A**2,"det");zero((J**2+A**2*sp.eye(2))[0,0],"Cayley 00");zero((J**2+A**2*sp.eye(2))[1,1],"Cayley 11")
 q=sp.Matrix([1,-1+I/A]);p=sp.Matrix([(1+I*A)/2,I*A/2]);zero((J-I*A*sp.eye(2))*q,"right eigenvector");zero((J.T+I*A*sp.eye(2))*p,"left eigenvector");zero(sp.conjugate(p).dot(q)-1,"normalization")
 def Q(a,b):return sp.Matrix([sum(sp.diff(f[k],z[i],z[j]).subs({u:0,v:0})*a[i]*b[j] for i in range(2) for j in range(2)) for k in range(2)])
 def C(a,b,c):return sp.Matrix([sum(sp.diff(f[k],z[i],z[j],z[l]).subs({u:0,v:0})*a[i]*b[j]*c[l] for i in range(2) for j in range(2) for l in range(2)) for k in range(2)])
 qb=sp.conjugate(q);term=C(q,q,qb)+Q(qb,(2*I*A*sp.eye(2)-J).inv()*Q(q,q))-2*Q(q,J.inv()*Q(q,qb));G=sp.simplify(sp.conjugate(p).dot(term));target=-(1+2/A**2)-I*(4*A**4-7*A**2+4)/(3*A**3)
 zero(G-target,"G21");zero(sp.re(G)/(2*A)+(A**2+2)/(2*A**3),"Kuznetsov l1");zero(sp.re(G)/2+(A**2+2)/(2*A**2),"physical cubic");zero(-1/sp.re(G)-A**2/(A**2+2),"radius coefficient")
 mu=sp.symbols("mu",real=True);trace=mu;disc=trace**2-4*A**2;zero(sp.diff(trace/2,mu)-sp.Rational(1,2),"transversality");zero(sp.diff(sp.sqrt(A**2-mu**2/4),mu).subs(mu,0),"no linear frequency detuning")
 print(f"C311 SymPy cross-check: PASS ({checks} identities; G21 derived)")
if __name__=="__main__":main()
