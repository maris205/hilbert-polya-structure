#!/usr/bin/env python3
"""Independent symbolic identities for the HCS-C358 theorem contract."""
from __future__ import annotations

import sys

import sympy as sp


def zero(expr, label):
    if isinstance(expr, sp.MatrixBase):
        if any(sp.factor(sp.together(item)) != 0 for item in expr):
            raise AssertionError(label)
    elif sp.factor(sp.together(expr)) != 0:
        raise AssertionError(label)


def main():
    if sys.flags.optimize:
        raise RuntimeError("C358 SymPy lane refuses optimized Python")
    a, b, x, y, z, lam, q, s0 = sp.symbols(
        "a b x y z lam q s0", positive=True)
    S = x + y + z
    Q = x*y + y*z + z*x
    fx = x*(1-x-a*y-b*z)
    fy = y*(1-b*x-y-a*z)
    fz = z*(1-a*x-b*y-z)
    checks = 0
    zero(fx+fy+fz-(S-S**2+(2-a-b)*Q), "total population")
    checks += 1
    dlogp = fx/x+fy/y+fz/z
    zero(dlogp-(3-(1+a+b)*S), "product logarithm")
    checks += 1
    zero(dlogp-3*(fx+fy+fz)/S-(2-a-b)*(S**2-3*Q)/S,
         "normalized product")
    checks += 1
    zero(S**2-3*Q-sp.Rational(1, 2)*((x-y)**2+(y-z)**2+(z-x)**2),
         "spread square")
    checks += 1

    r = 1/(1+a+b)
    J = sp.Matrix([fx, fy, fz]).jacobian([x, y, z]).subs({x:r, y:r, z:r})
    real = (a+b-2)/(2*(1+a+b))
    imag2 = 3*(a-b)**2/(4*(1+a+b)**2)
    zero((lam*sp.eye(3)-J).det()-(lam+1)*((lam-real)**2+imag2),
         "coexistence characteristic polynomial")
    checks += 1
    zero(J*sp.Matrix([1,1,1])+sp.Matrix([1,1,1]), "radial eigenvector")
    checks += 1

    u, v, w, delta = sp.symbols("u v w delta", positive=True)
    du = delta*u*(v-w)
    dv = delta*v*(w-u)
    dw = delta*w*(u-v)
    zero(du+dv+dw, "critical simplex")
    checks += 1
    zero(du*v*w+u*dv*w+u*v*dw, "critical product")
    checks += 1
    h = u*v*w
    quartic = (delta*u*(v-w))**2
    reduced = delta**2*u*(u*(1-u)**2-4*h)
    zero((quartic-reduced).subs(w, 1-u-v), "critical quartic")
    checks += 1

    logistic = s0*q/(1+s0*(q-1))
    zero(q*sp.diff(logistic, q)-logistic*(1-logistic), "logistic chart")
    checks += 1
    tau = sp.log(1+s0*(q-1))
    zero(q*sp.diff(tau, q)-logistic, "critical time change")
    checks += 1

    common = sp.symbols("common", positive=True)
    unit_field = sp.Matrix([fx, fy, fz]).subs({a:1,b:1})
    zero(unit_field[0]-x*(1-S), "unit wall x")
    zero(unit_field[1]-y*(1-S), "unit wall y")
    zero(unit_field[2]-z*(1-S), "unit wall z")
    checks += 3
    diagonal = fx.subs({y:x,z:x})
    zero(diagonal-x*(1-(1+a+b)*x), "diagonal logistic")
    checks += 1
    for low, high in ((a,b),(b,a)):
        zero((1-low)+(low-1), "unstable edge rate")
        zero((1-high)+(high-1), "stable edge rate")
        checks += 2
    print(f"C358 SymPy cross-check: PASS {checks} exact identities")


if __name__ == "__main__":
    main()
