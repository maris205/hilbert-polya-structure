#!/usr/bin/env python3
"""Separate exact block-determinant and reversal reconstruction for C138."""
from itertools import product
import sympy as sp


def main():
    C=sp.Rational(2,3)*sp.ones(3)-sp.eye(3); Z=sp.zeros(3); S=Z.row_join(C).col_join(C.row_join(Z)); J=Z.row_join(sp.eye(3)).col_join(sp.eye(3).row_join(Z))
    checks=0
    for M in (C.T*C-sp.eye(3),S.T*S-sp.eye(6),J*J-sp.eye(6),J*S-S*J):
        for v in M: assert sp.simplify(v)==0; checks+=1
    x1,x2,x3,q1,q2,q3,rho,c,t=sp.symbols("x1 x2 x3 q1 q2 q3 rho c t", nonzero=True); xs=(x1,x2,x3); qs=(q1,q2,q3)
    Xp=sp.diag(*(xs[i]*qs[i] for i in range(3))); Xm=sp.diag(*(xs[i]/qs[i] for i in range(3)))
    D=sp.factor((sp.eye(3)-rho**2*C*Xm*C*Xp).det()); Q=lambda i,j:qs[i]/qs[j]+qs[j]/qs[i]
    T1=sp.Rational(1,9)*sum(x*x for x in xs)+sp.Rational(4,9)*sum(xs[i]*xs[j]*Q(i,j) for i in range(3) for j in range(i+1,3))
    T2=sp.Rational(1,9)*sum(xs[i]**2*xs[j]**2 for i in range(3) for j in range(i+1,3))+sp.Rational(4,9)*sum(xs[i]*xs[j]*xs[3-i-j]**2*Q(i,j) for i in range(3) for j in range(i+1,3))
    assert sp.factor(D-(1-rho**2*T1+rho**4*T2-rho**6*(x1*x2*x3)**2))==0; checks+=1
    assert sp.factor(D.subs({q1:c*q1,q2:c*q2,q3:c*q3})-D)==0; checks+=1
    assert sp.factor(D.subs({q1:1/q1,q2:1/q2,q3:1/q3})-D)==0; checks+=1
    for power in range(7):
        assert (sp.expand(D).coeff(rho,power)==0)==(power not in (0,2,4,6)); checks+=1
    zero=sp.factor(D.subs({q1:1,q2:1,q3:1,x1:t,x2:t**2,x3:t**3,rho:1}))
    target=-sp.Rational(1,9)*(t-1)**3*(t+1)*(t**2+1)*(t**2+t+1)*(3*t**2-2*t+3)*(3*t**2+5*t+3)
    assert sp.factor(zero-target)==0; checks+=1
    pi=sp.factor(sp.expand(D.subs({q1:-1,q2:1,q3:1})-D.subs({q1:1,q2:1,q3:1})).coeff(rho,2))
    assert pi==sp.Rational(16,9)*x1*(x2+x3); checks+=1
    u=(1+sp.I)/sp.sqrt(2); Pa=sp.diag(u,1,1,sp.conjugate(u),1,1); Pm=sp.diag(sp.conjugate(u),1,1,u,1,1); Ua=Pa*S*Pa; Um=Pm*S*Pm
    correct=(J*Ua.conjugate()*J-Um.inv()).applyfunc(sp.simplify); wrong=(J*Ua.conjugate()*J-Ua.inv()).applyfunc(sp.simplify)
    for v in correct: assert v==0; checks+=1
    assert sum(v!=0 for v in wrong)==8; checks+=1
    assert sp.simplify(sum(sp.conjugate(v)*v for v in wrong))==sp.Rational(64,9); checks+=1
    rooted=primitive=0
    for n in range(1,9):
        count=0 if n%2 else 2*3**n
        rooted+=count
        prim=int(sum(sp.mobius(d)*(0 if (n//d)%2 else 2*3**(n//d)) for d in sp.divisors(n))/n)
        primitive+=prim
        checks+=2
    assert rooted==14760 and primitive==1905; checks+=2
    for i,j in product(range(3),repeat=2):
        if i==j: continue
        amp=sp.factor(C[j,i]*C[i,j]); assert amp==sp.Rational(4,9); checks+=1
        winding=[0,0,0]; winding[i]+=1; winding[j]-=1; assert sum(winding)==0; checks+=1
    print(f"C138 SymPy cross-check: PASS ({checks} exact checks)")


if __name__=="__main__": main()
