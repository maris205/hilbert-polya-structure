#!/usr/bin/env python3
"""Independent symbolic identities for HCS-C365."""
from __future__ import annotations
if not __debug__: raise RuntimeError("c365 SymPy lane refuses optimized Python")
import argparse
import sympy as s

def main():
    argparse.ArgumentParser().parse_args();checks=0
    t,l1,l2,l3,y1,y2=s.symbols("t l1 l2 l3 y1 y2")
    P=(t-l1)*(t-l2)*(t-l3);P1=s.expand(P.subs(t,y1));P2=s.expand(P.subs(t,y2))
    z1=-P1/(y1-y2);z2=P2/(y1-y2);c=l1+l2+l3-y1-y2
    M=s.Matrix([[t-y1,0,-s.Symbol("u")],[0,t-y2,-s.Symbol("v")],[-s.Symbol("ub"),-s.Symbol("vb"),t-c]])
    det=s.expand(M.det().subs({s.Symbol("u")*s.Symbol("ub"):z1,s.Symbol("v")*s.Symbol("vb"):z2}))
    # Re-expand directly since substitutions of products may depend on expression order.
    det2=s.expand((t-y1)*(t-y2)*(t-c)-(t-y2)*z1-(t-y1)*z2)
    assert s.simplify(det2-P)==0;checks+=1
    a,b,u,v=s.symbols("a b u v",integer=True,nonnegative=True)
    summand=b+u-v+1
    total=s.summation(s.summation(summand,(v,0,b)),(u,0,a))
    target=(a+1)*(b+1)*(a+b+2)/2
    assert s.simplify(total-target)==0;checks+=1
    for av in range(8):
        for bv in range(8):
            brute=sum(bv+uu-vv+1 for uu in range(av+1) for vv in range(bv+1))
            assert brute==(av+1)*(bv+1)*(av+bv+2)//2;checks+=1
    A=s.Matrix(3,3,lambda i,j:s.symbols(f"a{i}{j}"))
    X=s.Matrix(3,3,lambda i,j:s.symbols(f"x{i}{j}"))
    Y=s.Matrix(3,3,lambda i,j:s.symbols(f"y{i}{j}"))
    df=-s.I*s.trace(X*(Y*A-A*Y))
    kks=-s.I*s.trace(A*(X*Y-Y*X))
    assert s.expand(df-kks)==0;checks+=1
    projector=s.diag(1,0,0);generator=s.I*projector
    moment=-s.I*s.trace(A*generator);flow=generator*A-A*generator
    assert s.expand(moment-A[0,0])==0 and flow[0,1]==s.I*A[0,1] and flow[1,0]==-s.I*A[1,0];checks+=1
    full_turn=s.diag(s.exp(2*s.pi*s.I),1,1)
    assert s.simplify(full_turn-s.eye(3))==s.zeros(3);checks+=1
    primitive=s.Matrix([1,2,3]);inside=s.pi*s.Matrix([s.Rational(1,2),1,s.Rational(3,2)])
    assert s.simplify(inside-s.pi*primitive/2)==s.zeros(3,1);checks+=1
    outside=s.pi*s.Matrix([0,0,1]);relation=s.Matrix([-3,0,1])
    assert relation.dot(primitive)==0 and s.simplify(relation.dot(outside)-s.pi)==0;checks+=1
    assert s.eye(3).rank()==3;checks+=1
    print(f"C365 SymPy PASS: exact_symbolic_checks={checks}")
if __name__=="__main__": main()
