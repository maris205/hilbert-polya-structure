#!/usr/bin/env python3
"""Independent symbolic reconstruction of C229 identities."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    checks = 0
    t, u, k, th, s, x, z, a = sp.symbols("t u k th s x z a", positive=True)
    e = sp.exp(-k*t)
    h = s**2/(2*k)*(1-e)
    psi = u*e/(1+h*u)
    phi = 2*k*th/s**2*sp.log(1+h*u)
    checks += 1; assert sp.simplify(sp.diff(psi,t) + k*psi + s**2*psi**2/2) == 0
    checks += 1; assert sp.simplify(sp.diff(phi,t) - k*th*psi) == 0
    F = sp.exp(-phi-psi*x)
    # backward Kolmogorov equation for the affine transform
    lhs = sp.diff(F,t)
    rhs = k*(th-x)*sp.diff(F,x) + s**2*x*sp.diff(F,x,2)/2
    checks += 1; assert sp.simplify(lhs-rhs) == 0
    # deterministic and squared-Bessel branches
    checks += 1; assert sp.simplify(sp.limit(psi, s, 0) - u*e) == 0
    checks += 1; assert sp.simplify(sp.limit(phi, s, 0) - th*u*(1-e)) == 0
    psi0 = u/(1+s**2*u*t/2)
    checks += 1; assert sp.simplify(sp.limit(psi, k, 0) - psi0) == 0
    checks += 1; assert sp.simplify(sp.limit(phi, k, 0)) == 0
    # Laguerre eigen-equation under the CIR generator.
    for n in range(8):
        Ln = sp.assoc_laguerre(n, a-1, z)
        checks += 1; assert sp.simplify(z*sp.diff(Ln,z,2)+(a-z)*sp.diff(Ln,z)+n*Ln) == 0
    # Gamma stationary flux is zero for every smooth compactly supported f.
    beta = sp.symbols("beta", positive=True)
    density = z**(a-1)*sp.exp(-z)
    # Formal adjoint acting on density after scaling z=x/beta.
    flux = z*density
    checks += 1; assert sp.simplify(sp.diff((a-z)*density,z) - sp.diff(flux,z,2)) == 0
    # First Laguerre mode gives exact gap eigenvalue.
    L1 = sp.assoc_laguerre(1, a-1, z)
    checks += 1; assert sp.simplify(z*sp.diff(L1,z,2)+(a-z)*sp.diff(L1,z)+L1) == 0
    # Feller index algebra: delta>=2 iff 2*k*th>=s^2 (s>0).
    delta = 4*k*th/s**2
    checks += 1; assert sp.simplify(delta-2 - 2*(2*k*th-s**2)/s**2) == 0
    print(f"C229 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__": main()
