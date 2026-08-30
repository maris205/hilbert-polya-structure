#!/usr/bin/env python3
"""Independent symbolic and numerical checks for the C243 formulas."""
from __future__ import annotations

import mpmath as mp
import sympy as sp


def main() -> None:
    z, phi, H = sp.symbols("z phi H", real=True)
    Lam = sp.symbols("Lambda", positive=True)
    r = sp.sqrt(1 - z**2)
    ham = Lam*z**2/2 - r*sp.cos(phi)
    checks = 0

    def ok(expr, label: str) -> None:
        nonlocal checks
        checks += 1
        if sp.simplify(expr) != 0:
            raise AssertionError(label + ": " + str(sp.factor(expr)))

    zdot = -r*sp.sin(phi)
    phidot = Lam*z + z*sp.cos(phi)/r
    ok(zdot + sp.diff(ham, phi), "Hamilton z equation")
    ok(phidot - sp.diff(ham, z), "Hamilton phi equation")
    x = r*sp.cos(phi)
    y = r*sp.sin(phi)
    xdot = sp.diff(x, z)*zdot + sp.diff(x, phi)*phidot
    ydot = sp.diff(y, z)*zdot + sp.diff(y, phi)*phidot
    ok(xdot + Lam*z*y, "Bloch x equation")
    ok(ydot - z*(1 + Lam*x), "Bloch y equation")
    ok(zdot + y, "Bloch z equation")
    ok(x**2 + y**2 + z**2 - 1, "Bloch sphere constraint")
    # Eliminate phi from the conserved energy.
    cosphi = (Lam*z**2/2 - H)/r
    poly = sp.expand((1-z**2) - (Lam*z**2/2 - H)**2)
    ok(poly - (-Lam**2*z**4/4 + (Lam*H-1)*z**2 + 1-H**2), "energy polynomial")
    yp = 2*(Lam*H-1 + sp.sqrt(Lam**2-2*Lam*H+1))/Lam**2
    ym = 2*(Lam*H-1 - sp.sqrt(Lam**2-2*Lam*H+1))/Lam**2
    ok(sp.simplify(yp + ym - 4*(Lam*H-1)/Lam**2), "root sum")
    ok(sp.simplify(yp*ym - 4*(H**2-1)/Lam**2), "root product")
    # Fixed-point energies and pitchfork algebra.
    ok((Lam*0**2/2 - sp.sqrt(1-0**2)*sp.cos(0)) + 1, "zero-phase energy")
    ok((Lam*0**2/2 - sp.sqrt(1-0**2)*sp.cos(sp.pi)) - 1, "pi-phase energy")
    zb = sp.sqrt(1-Lam**-2)
    ok(sp.simplify((Lam*zb**2/2 + sp.sqrt(1-zb**2)) - (Lam + 1/Lam)/2), "broken energy")
    # Homoclinic profile: use u=sech^2 and tanh^2=1-u.
    u = sp.symbols("u", nonnegative=True)
    A = 2*sp.sqrt(Lam-1)/Lam
    w = sp.sqrt(Lam-1)
    lhs = A**2*w**2*u*(1-u)
    rhs = (Lam-1)*A**2*u - Lam**2*A**4*u**2/4
    ok(sp.factor(lhs-rhs), "separatrix profile")
    # Numerical quadrature independently reproduces both complete-K periods.
    mp.mp.dps = 70
    numeric = 0
    for L, h, mode in [(mp.mpf(2), mp.mpf("0.5"), "cross"), (mp.mpf(2), mp.mpf("1.1"), "self"), (mp.mpf(3), mp.mpf("1.2"), "self")]:
        d = mp.sqrt(L*L - 2*L*h + 1)
        ymn = 2*(L*h-1-d)/(L*L); ypn = 2*(L*h-1+d)/(L*L)
        if mode == "cross":
            integral = mp.quad(lambda th: 1/mp.sqrt(ypn*mp.sin(th)**2-ymn), [0, mp.pi/2])
            direct = 8*integral/L
            formula = 8/(L*mp.sqrt(ypn-ymn))*mp.ellipk(ypn/(ypn-ymn))
        else:
            integral = mp.quad(lambda th: 1/mp.sqrt(ypn-(ypn-ymn)*mp.sin(th)**2), [0, mp.pi/2])
            direct = 4*integral/L
            formula = 4/(L*mp.sqrt(ypn))*mp.ellipk(1-ymn/ypn)
        if abs(direct-formula) > mp.mpf("1e-45")*max(1, abs(formula)):
            raise AssertionError(f"elliptic period mismatch {L} {h}")
        numeric += 1
    print(f"C243_SYMPY_PASS ({checks} symbolic identities; {numeric} independent elliptic quadratures)")


if __name__ == "__main__":
    main()
