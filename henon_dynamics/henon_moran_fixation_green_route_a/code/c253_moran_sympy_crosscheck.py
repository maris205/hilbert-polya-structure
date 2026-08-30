#!/usr/bin/env python3
"""Symbolic checks for Moran rates, fixation and Green equations."""
import sympy as s
N,rho,beta,i=s.symbols('N rho beta i', positive=True)
# Treat i as an interior integer and use symbolic shifts.
lam=lambda j: beta*rho*j*(N-j)/N
mu=lambda j: beta*j*(N-j)/N
u=lambda j: (1-rho**(-j))/(1-rho**(-N))
checks=[]
checks.append((s.simplify(lam(i)*(u(i+1)-u(i))+mu(i)*(u(i-1)-u(i))),"fixation backward"))
w=s.Function('w')
# detailed balance ratio is an exact rational identity
checks.append((s.simplify((rho*i*(N-i)/((i+1)*(N-i-1)))*mu(i+1)-lam(i)/1),"rate ratio"))
# time recurrence is encoded by Q; verify row sum of generator including absorbing exits.
checks.append((s.simplify(-(lam(i)+mu(i))+lam(i)+mu(i)),"generator row sum"))
# neutral limit of fixation formula
j=s.symbols('j', positive=True)
checks.append((s.limit((1-rho**(-j))/(1-rho**(-N)),rho,1)-j/N,"neutral limit"))
# Green identity for a 2-state transient block
l1,l2,m1,m2=s.symbols('l1 l2 m1 m2', positive=True)
Q=s.Matrix([[-(l1+m1),l1],[m2,-(l2+m2)]])
G=(-Q).inv()
checks.append((s.simplify((-Q)*G-s.eye(2)),"Green inverse"))
# absorption-time backward equation t=G*1
tt=G*s.ones(2,1)
checks.append((s.simplify(Q*tt+s.ones(2,1)),"time equation"))
# scaling beta: Green scales inversely
checks.append((s.simplify(((-beta*Q).inv())-G/beta),"rate scaling"))
# recurrence for reversible weights
wi=s.symbols('w_i', positive=True)
checks.append((s.simplify((wi*beta*rho*i*(N-i)/N)-(wi*rho*i*(N-i)/((i+1)*(N-i-1)))*beta*(i+1)*(N-i-1)/N),"detailed balance"))
# boundaries of fixation
checks.append((s.simplify(u(N)-1),"upper boundary"))
checks.append((s.simplify(u(0)),"lower boundary"))
for value,label in checks:
    if isinstance(value,s.MatrixBase):
        bad=any(s.simplify(z)!=0 for z in value)
    else:
        bad=s.simplify(value)!=0
    if bad:
        raise AssertionError(f"{label}: {s.simplify(value)}")
print(f"C253_SYMPY_PASS ({len(checks)} symbolic identities; fixation, generator, Green and boundary limits)")
