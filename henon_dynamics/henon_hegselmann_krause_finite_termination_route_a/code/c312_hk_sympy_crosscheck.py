#!/usr/bin/env python3
"""Exact rational/matrix identities for HCS-C312."""
import sympy as sp
def update(state,eps):return sp.Matrix([sum(state[j] for j in range(len(state)) if bool(abs(state[j]-state[i])<=eps))/sum(1 for j in range(len(state)) if bool(abs(state[j]-state[i])<=eps)) for i in range(len(state))])
def main():
 checks=0
 def eq(x,y,label):
  nonlocal checks
  vals=list(x-y) if isinstance(x,sp.MatrixBase) else [x-y]
  if any(sp.simplify(v)!=0 for v in vals):raise AssertionError(label)
  checks+=1
 s=[sp.Rational(0),sp.Rational(1,2),sp.Rational(7,5)];u=update(s,sp.Integer(1));eq(u,sp.Matrix([sp.Rational(1,4),sp.Rational(19,30),sp.Rational(19,20)]),"mean example update");eq(sum(s)/3,sp.Rational(19,30),"initial mean");eq(sum(u)/3,sp.Rational(11,18),"updated mean");eq(sum(u)/3-sum(s)/3,-sp.Rational(1,45),"mean drift")
 A=sp.Matrix([[sp.Rational(1,2),sp.Rational(1,2),0],[sp.Rational(1,3)]*3,[0,sp.Rational(1,2),sp.Rational(1,2)]]);one=sp.ones(3,1);eq(A*one,one,"row stochastic");eq((one.T*A)[0,0],sp.Rational(5,6),"not column stochastic first")
 a,b,c=sp.symbols("a b c",real=True);complete=sp.ones(3,3)/3;eq(complete*sp.Matrix([a,b,c]),sp.ones(3,1)*(a+b+c)/3,"complete consensus")
 for k in range(-5,6):
  state=[sp.Rational(0),sp.Rational(1,2),sp.Rational(7,5)];shift=sp.Rational(k,3);scaled=[2*x+shift for x in state];eq(update(scaled,sp.Integer(2)),2*update(state,sp.Integer(1))+sp.ones(3,1)*shift,f"affine covariance {k}")
 for n in range(1,11):
  J=sp.ones(n,n)/n;eq(J*J,J,f"consensus idempotent {n}");eq(J*sp.ones(n,1),sp.ones(n,1),f"consensus row sum {n}")
 print(f"C312 SymPy cross-check: PASS ({checks} exact identities)")
if __name__=="__main__":main()
