#!/usr/bin/env python3
"""Symbolic cross-checks independent of the numerical producer."""
import sympy as sp


def main() -> None:
    f, c, kx, ky, lam, w, t = sp.symbols("f c kx ky lam w t", real=True)
    I = sp.I
    G = sp.Matrix([[0, f, -I*c*kx], [-f, 0, -I*c*ky],
                   [-I*c*kx, -I*c*ky, 0]])
    rho = kx**2 + ky**2
    checks = []
    checks.append(sp.simplify(G.conjugate().T + G) == sp.zeros(3))
    checks.append(sp.simplify((lam*sp.eye(3)-G).det() - lam*(lam**2 + f**2 + c**2*rho)) == 0)
    checks.append(sp.simplify(G**3 + (f**2+c**2*rho)*G) == sp.zeros(3))
    W = sp.sqrt(f**2+c**2*rho)
    P0 = sp.eye(3) + G**2/W**2
    Pp = (-G**2/W**2 - I*G/W)/2
    Pm = (-G**2/W**2 + I*G/W)/2
    for expr in (P0**2-P0, Pp**2-Pp, Pm**2-Pm, P0*Pp, Pp*Pm, P0+Pp+Pm-sp.eye(3)):
        checks.append(all(sp.simplify(entry) == 0 for entry in expr))
    checks.append(sp.simplify(sp.diff(sp.cos(w*t), t) + w*sp.sin(w*t)) == 0)
    expected = [1, 4, 4, 0, 4, 8, 0, 0, 4, 4]
    for q, value in enumerate(expected):
        count = sum(1 for i in range(-5, 6) for j in range(-5, 6) if i*i+j*j == q)
        checks.append(count == value)
    assert all(checks)
    print(f"C217 SymPy cross-check: PASS ({len(checks)} symbolic identities)")
    print("skew-Hermiticity, cubic, projector algebra, exponential derivative, and shell controls: PASS")


if __name__ == "__main__":
    main()
