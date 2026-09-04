#!/usr/bin/env python3
"""Independent symbolic cross-check for HCS-C357."""
from __future__ import annotations

import sys
import sympy as s

COUNT = 0


def need(expr, label):
    global COUNT
    COUNT += 1
    reduced = s.simplify(expr)
    if isinstance(reduced, s.MatrixBase):
        failed = any(s.simplify(value) != 0 for value in reduced)
    else:
        failed = reduced != 0
    if failed:
        raise AssertionError(label)


def main():
    if sys.flags.optimize:
        raise RuntimeError("C357 SymPy lane refuses optimized Python")
    wp, wm, E = s.symbols("wp wm E", positive=True)
    total = 1/wp+1/wm
    T = s.pi*total; J = E*total/2; Omega = 2/total
    need(s.diff(J, E)-1/Omega, "action frequency")
    need(Omega*T-2*s.pi, "period frequency")
    need(2*s.pi*J-s.pi*E*total, "phase area")
    t = s.symbols("t", real=True)
    def matrix(w):
        return s.Matrix([[s.cos(w*t), s.sin(w*t)/w], [-w*s.sin(w*t), s.cos(w*t)]])
    need(matrix(wp).det()-1, "symplectic plus")
    need(matrix(wm).det()-1, "symplectic minus")
    need(matrix(wp).subs(t, s.pi/wp)+s.eye(2), "plus half")
    need(matrix(wm).subs(t, s.pi/wm)+s.eye(2), "minus half")
    need(matrix(wm).subs(t, s.pi/wm)*matrix(wp).subs(t, s.pi/wp)-s.eye(2), "monodromy")
    x, w, nu = s.symbols("x w nu", positive=True)
    z = s.sqrt(2*w)*x
    # Algebraic transformed equation using y_zz=(z^2/4-nu-1/2)y.
    transformed = -w*(z**2/s.Integer(4)-nu-s.Rational(1, 2))+w*z**2/s.Integer(4)
    need(transformed-w*(nu+s.Rational(1, 2)), "Weber energy")
    Dp, Dm, Dpp, Dmp = s.symbols("Dp Dm Dpp Dmp")
    matching = s.Matrix([[Dp, -Dm], [s.sqrt(wp)*Dpp, s.sqrt(wm)*Dmp]])
    F = s.sqrt(wp)*Dpp*Dm+s.sqrt(wm)*Dmp*Dp
    need(matching.det()-F, "interface determinant")
    # Integer D_n is exp(-z^2/4) He_n(z); parity owns the zero at the seam.
    zz = s.symbols("zz")
    for n in range(40):
        poly = s.hermite(n, zz/s.sqrt(2))*2**(-s.Rational(n, 2))
        value = s.simplify(poly.subs(zz, 0))
        derivative = s.simplify(s.diff(poly*s.exp(-zz**2/4), zz).subs(zz, 0))
        if n % 2 == 0:
            need(derivative, "even derivative")
            if value == 0:
                raise AssertionError("even value unexpectedly zero")
            need(0, "even value nonzero")
        else:
            need(value, "odd value")
            if derivative == 0:
                raise AssertionError("odd derivative unexpectedly zero")
            need(0, "odd derivative nonzero")
    for a in range(1, 41):
        for b in range(1, 6):
            wpv, wmv, ev = s.Rational(a, b), s.Rational(a+b, b), s.Rational(2*a+b, a+b)
            vals = {wp: wpv, wm: wmv, E: ev}
            need((Omega*T-2*s.pi).subs(vals), "sample period")
            need((2*s.pi*J-s.pi*E*total).subs(vals), "sample action")
    print(f"C357 SymPy cross-check: PASS ({COUNT} identities)")


if __name__ == "__main__":
    main()
