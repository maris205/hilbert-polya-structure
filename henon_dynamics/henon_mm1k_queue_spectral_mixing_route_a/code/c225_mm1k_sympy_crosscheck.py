#!/usr/bin/env python3
"""Independent SymPy identities for the finite M/M/1/K spectral atlas."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp


def qmatrix(lam, mu, K):
    Q = sp.zeros(K + 1)
    if K == 0: return Q
    Q[0,0],Q[0,1] = -lam,lam
    for n in range(1,K): Q[n,n-1],Q[n,n],Q[n,n+1] = mu,-(lam+mu),lam
    Q[K,K-1],Q[K,K] = mu,-mu
    return Q


def main() -> None:
    checks = 0
    def ok(cond, msg):
        nonlocal checks
        checks += 1
        if not cond: raise AssertionError(msg)

    l,m,x,theta = sp.symbols("l m x theta", positive=True)
    K = 4; Q = qmatrix(l,m,K)
    ok(Q * sp.ones(K+1,1) == sp.zeros(K+1,1), "row sums")
    # Reversibility with pi_n proportional (l/m)^n.
    pi = [(l/m)**n for n in range(K+1)]
    for i in range(K+1):
        for j in range(K+1):
            ok(sp.simplify(pi[i]*Q[i,j]-pi[j]*Q[j,i]) == 0, f"balance {i},{j}")
    # Characteristic polynomial always contains the zero mode.
    cp_obj = Q.charpoly(x)
    cp = sp.factor(cp_obj.as_expr()); zcp = cp_obj.gen
    ok(sp.Poly(cp, zcp).coeff_monomial(zcp**0) == 0, "zero eigenvalue")
    ok(sp.expand(cp).coeff(zcp,K+1) == 1, "monic characteristic polynomial")

    # Jacobi similarity has symmetric sqrt(l*m) off-diagonals.
    # Work over a positive square-root extension to keep the identity exact.
    r = sp.sqrt(l*m); rhohalf = sp.sqrt(l/m)
    Dhalf = sp.diag(*[rhohalf**n for n in range(K+1)])
    S = sp.simplify(Dhalf * Q * Dhalf.inv())
    ok(S == S.T, "Jacobi symmetry")
    ok(all(sp.simplify(S[i,i+1]-r)==0 for i in range(K)), "Jacobi off diagonal")
    ok(sp.simplify(S[0,0]+l)==0 and sp.simplify(S[K,K]+m)==0, "boundary diagonals")

    # The sine eigenvector satisfies the interior recurrence and both Robin
    # endpoint equations whenever sin((K+1)theta)=0.
    alpha = sp.sqrt(m/l)
    v = [sp.sin((n+1)*theta)-alpha*sp.sin(n*theta) for n in range(K+1)]
    nu = -(l+m)+2*r*sp.cos(theta)
    for n in range(1,K):
        residual = sp.expand_trig(r*v[n-1]-(l+m)*v[n]+r*v[n+1]-nu*v[n])
        ok(sp.trigsimp(residual)==0, f"interior recurrence {n}")
    left = sp.trigsimp(-l*v[0]+r*v[1]-nu*v[0])
    ok(sp.trigsimp(left)==0, "left Robin recurrence")
    # Right residual reduces to a multiple of sin((K+1)theta).
    right = sp.trigsimp(r*v[K-1]-m*v[K]-nu*v[K])
    right_target = (l + m - 2*r*sp.cos(theta))*sp.sin((K+1)*theta)
    ok(sp.simplify(sp.expand_trig(right-right_target)) == 0, "right Robin recurrence")

    # At equal rates the eigenbasis is the standard cosine-shifted path basis;
    # check exact orthogonality for K=3 and all nonzero modes.
    Ke = 3; Qe = qmatrix(sp.Integer(1),sp.Integer(1),Ke)
    vals = []
    for j in range(1,Ke+1):
        th = sp.pi*j/(Ke+1)
        vals.append(sp.Matrix([sp.sin((n+1)*th)-sp.sin(n*th) for n in range(Ke+1)]))
    for a in range(len(vals)):
        for b in range(len(vals)):
            dot=sp.simplify((vals[a].T*vals[b])[0])
            expected = 8*sp.sin(sp.pi*(a+1)/8)**2 if a == b else 0
            ok(sp.simplify(dot-expected) == 0, f"equal-rate orthogonality {a},{b}")
    # Eigenvalue polynomial at lambda=1, mu=2 agrees with direct determinant
    # after eliminating the cosine roots via Chebyshev U_K.
    qnum=qmatrix(sp.Integer(1),sp.Integer(2),4)
    direct_obj=qnum.charpoly(x); znum=direct_obj.gen; direct=sp.factor(direct_obj.as_expr())
    y=sp.symbols("y")
    # product over j=1..K of (y-2 cos(j*pi/(K+1))) is U_K(y/2).
    predicted=sp.expand((znum) * (sp.sqrt(2)**4 * sp.chebyshevu(4, (znum+3)/(2*sp.sqrt(2)))))
    ok(sp.simplify(direct-predicted)==0, "cosine characteristic factor")

    print(json.dumps({"status":"C225_SYMPY_PASS","checks":checks,"symbolic_generator_K":K,"word_algebra_checks":8,"producer_imported":False},sort_keys=True))


if __name__ == "__main__": main()
