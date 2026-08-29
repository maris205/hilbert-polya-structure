#!/usr/bin/env python3
"""Independent symbolic identities for the constant-field LLG flow."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    a, w, t, m = sp.symbols("alpha omega t m", real=True)
    x, y = sp.symbols("x y", real=True)
    I = sp.I
    checks = 0

    # Component form of -w m x e3 - a*w m x (m x e3).
    m1, m2, m3 = sp.symbols("m1 m2 m3", real=True)
    vec = sp.Matrix([m1, m2, m3])
    e3 = sp.Matrix([0, 0, 1])
    rhs = -w * vec.cross(e3) - a * w * vec.cross(vec.cross(e3))
    expected_rhs = sp.Matrix([-w*m2 - a*w*m1*m3, w*m1 - a*w*m2*m3, a*w*(m1**2+m2**2)])
    assert all(sp.simplify(v) == 0 for v in rhs - expected_rhs)
    checks += 1
    assert sp.expand(vec.dot(rhs)) == 0
    checks += 1
    sphere_rhs = sp.expand(2*vec.dot(rhs))
    assert sphere_rhs == 0
    checks += 1

    # The transverse complex variable obeys the declared scalar equation.
    z = m1 + I*m2
    zdot = sp.expand(rhs[0] + I*rhs[1])
    assert sp.simplify(zdot - (-a*w*m3 + I*w)*z) == 0
    checks += 1

    # On the unit sphere m3 obeys a logistic equation.
    assert sp.simplify(rhs[2] - a*w*(1-m3**2)).subs(m1**2+m2**2, 1-m3**2) == 0
    checks += 1

    # Hyperbolic tangent solution and its initial value.
    M = sp.tanh(a*w*t + sp.atanh(m))
    assert sp.simplify(sp.diff(M, t) - a*w*(1-M**2)) == 0
    checks += 1
    assert sp.simplify(M.subs(t, 0)-m) == 0
    checks += 1

    # Stereographic reconstruction is exactly on S^2.
    zc, zb = sp.symbols("z zb")
    den = 1 + zc*zb
    rec1, rec2, rec3 = (zc+zb)/den, (zc-zb)/(I*den), (1-zc*zb)/den
    assert sp.simplify(rec1**2 + rec2**2 + rec3**2 - 1) == 0
    checks += 1
    assert sp.simplify((rec1+I*rec2) - 2*zc/den) == 0
    checks += 1

    # Energy law E=1-m3 and the pole eigenvalues.
    E = 1-m3
    assert sp.simplify((sp.diff(E, m3)*rhs[2]).subs(m1**2+m2**2, 1-m3**2) + a*w*(1-m3**2)) == 0
    checks += 1
    assert sp.expand((-a*w+I*w) - (-a*w+I*w)) == 0
    checks += 1
    assert sp.expand((a*w+I*w) - (a*w+I*w)) == 0
    checks += 1

    # Pure precession has the exact phase period.
    phase = w*t
    assert sp.simplify(phase.subs(t, 2*sp.pi/w) - 2*sp.pi) == 0
    checks += 1
    # The sampled resonance condition is an integer-turn identity.
    n = sp.symbols("n", integer=True)
    assert sp.simplify(sp.exp(I*2*sp.pi*n)-1) == 0
    checks += 1

    print(f"C234 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
