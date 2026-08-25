#!/usr/bin/env python3
"""Independent SymPy reconstruction for HCS-C158."""
from __future__ import annotations

import json
from math import comb
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]

def read_qsi(row):
    a,b,c,d=map(sp.Rational,row);return a+b*sp.sqrt(3)+c*sp.I+d*sp.sqrt(3)*sp.I

def main():
    data=json.loads((ROOT/"results/c158_full_cycle_evidence.json").read_text());checks=0
    def check(condition,message):
        nonlocal checks;checks+=1
        if not condition:raise AssertionError(message)
    r=sp.sqrt(3);i=sp.I;w=(-1+i*r)/2
    F=sp.Matrix(3,3,lambda j,l:sp.expand_complex(w**(j*l)/r));P=sp.diag(1,0,1)
    A=sp.Matrix([[r/3,0,r/3],[r/3,0,-r/6+i/2],[r/3,0,-r/6-i/2]])
    check((F.conjugate().T*P-A).applyfunc(sp.simplify)==sp.zeros(3),"gate")
    lam,z=sp.symbols("lambda z")
    tau=r/6-i/2;q=-sp.Rational(1,2)-r*i/6;D=sp.expand(tau**2-4*q)
    check(sp.expand(A.charpoly(lam).as_expr()-lam*(lam**2-tau*lam+q))==0,"charpoly")
    check(sp.expand(D-(sp.Rational(11,6)+r*i/2))==0,"discriminant")
    check(q!=0 and D!=0,"distinct nonzero roots")
    psum=sp.simplify((sp.Abs(tau)**2+sp.Abs(D))/2)
    check(sp.simplify(psum-(1+sp.sqrt(37))/6)==0,"modulus square sum")
    check(sp.simplify(sp.Abs(q)**2-sp.Rational(1,3))==0,"modulus square product")
    check(sp.simplify(psum**2-sp.Rational(4,3)-(sp.sqrt(37)-5)/18)==0,"modulus discrimination")
    lp=(tau+sp.sqrt(D))/2;lm=(tau-sp.sqrt(D))/2
    for k in (1,2):
        C=sp.kronecker_product(*([A]*k))
        determinant=sp.Poly(sp.expand((sp.eye(3**k)-z*C).det(method="berkowitz")),z)
        factor=sp.Poly(sp.expand(sp.prod((1-z*lp**j*lm**(k-j))**comb(k,j) for j in range(k+1))),z)
        check(sp.simplify(determinant.as_expr()-factor.as_expr())==0,f"direct factorization {k}")
        frozen=[read_qsi(row) for row in data["field_trace_and_polynomial_ledgers"][str(k)]["coefficients_ascending"]]
        check(all(sp.simplify(determinant.nth(j)-frozen[j])==0 for j in range(2**k+1)),f"direct coefficients {k}")
        check(determinant.degree()==2**k,f"degree {k}")
    # A separate symbolic power path checks the k=3 tensor trace receipts.
    frozen3=data["direct_kronecker_determinant_checks"]["3"]["direct_matrix_power_traces"]
    for n,row in enumerate(frozen3,1):
        check(sp.simplify(sp.trace(A**n)**3-read_qsi(row))==0,f"symbolic C3 trace {n}")
    for k in range(1,13):
        total=sum(comb(k,j) for j in range(k+1));first=sum(j*comb(k,j) for j in range(k+1));center=sum((2*j-k)**2*comb(k,j) for j in range(k+1))
        check(total==2**k,f"mass {k}");check(first==k*2**(k-1),f"mean {k}");check(center==k*2**k,f"variance {k}")
    A0=F.conjugate().T*sp.diag(0,1,1)
    expected0=lam*(lam+i)*(3*lam+r)/3
    check(sp.simplify(A0.charpoly(lam).as_expr()-expected0)==0,"moved-hole polynomial")
    check(sp.simplify(sp.Abs((-i)*(-1/r))-1/r)==0,"moved product modulus")
    check(data["controls"]["moved_hole"]["mean_changes"] is False and data["controls"]["moved_hole"]["variance_changes"] is True,"moved boundary")
    check(data["surviving_log_modulus_theorem"]["phase_limit_claimed"] is False,"no phase limit")
    check(data["route_a"]["route_b_invocation_allowed"] is False,"Route B")
    print(json.dumps({"status":"C158_SYMPY_PASS","checks":checks},sort_keys=True))

if __name__=="__main__":main()
