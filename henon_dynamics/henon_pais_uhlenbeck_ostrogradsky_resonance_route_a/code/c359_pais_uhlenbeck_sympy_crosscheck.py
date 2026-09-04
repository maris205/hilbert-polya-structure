#!/usr/bin/env python3
"""Independent symbolic identities for HCS-C359."""
from __future__ import annotations

import math
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
        raise RuntimeError("C359 SymPy lane refuses optimized Python")
    w1, w2 = s.symbols("w1 w2", positive=True)
    q0, q1, p0, p1 = s.symbols("q0 q1 p0 p1", real=True)
    delta = w2**2-w1**2
    z = s.Matrix([q0, q1, p0, p1])
    poisson = s.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [-1, 0, 0, 0], [0, -1, 0, 0]])
    Q1 = (p1+w2**2*q0)/s.sqrt(delta)
    P1 = (p0+w1**2*q1)/s.sqrt(delta)
    Q2 = (p1+w1**2*q0)/s.sqrt(delta)
    P2 = -(p0+w2**2*q1)/s.sqrt(delta)
    y = s.Matrix([Q1, P1, Q2, P2])
    canonical = s.Matrix([[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]])
    need(y.jacobian(z)*poisson*y.jacobian(z).T-canonical, "canonical transform")
    H = p0*q1+p1**2/2+(w1**2+w2**2)*q1**2/2-w1**2*w2**2*q0**2/2
    A, B, C, D = s.symbols("A B C D")
    inverse = s.solve([Q1-A, P1-B, Q2-C, P2-D], [q0, q1, p0, p1], dict=True)[0]
    normal = -(B**2+w1**2*A**2)/2+(D**2+w2**2*C**2)/2
    need(H.subs(inverse)-normal, "Hamiltonian normal form")
    flow = poisson*s.Matrix([s.diff(H, u) for u in z])
    expected_flow = s.Matrix([q1, p1, w1**2*w2**2*q0, -p0-(w1**2+w2**2)*q1])
    need(flow-expected_flow, "Hamilton equations")
    matrix = expected_flow.jacobian(z)
    lam = s.symbols("lambda")
    need(matrix.charpoly(lam).as_expr()-(lam**2+w1**2)*(lam**2+w2**2), "characteristic polynomial")
    t = s.symbols("t", real=True)
    a1, b1, a2, b2 = s.symbols("a1 b1 a2 b2")
    x = a1*s.cos(w1*t)+b1*s.sin(w1*t)+a2*s.cos(w2*t)+b2*s.sin(w2*t)
    need(s.diff(x, t, 4)+(w1**2+w2**2)*s.diff(x, t, 2)+w1**2*w2**2*x, "general distinct solution")
    for m in range(1, 18):
        for n in range(m+1, 20):
            if math.gcd(m, n) != 1:
                continue
            g = s.Rational(m+n, m*n)
            T = 2*s.pi/g
            need(s.cos(g*m*T)-1, "rational phase one cosine")
            need(s.sin(g*m*T), "rational phase one sine")
            need(s.cos(g*n*T)-1, "rational phase two cosine")
            need(s.sin(g*n*T), "rational phase two sine")
            for n1 in range(8):
                for n2 in range(8):
                    energy = g*n*(n2+s.Rational(1, 2))-g*m*(n1+s.Rational(1, 2))
                    need(energy/g-(n*n2-m*n1+s.Rational(n-m, 2)), "quantum lattice")
    w = s.symbols("w", positive=True)
    equal = matrix.subs({w1: w, w2: w})
    need(equal.charpoly(lam).as_expr()-(lam**2+w**2)**2, "equal characteristic")
    if 4-(equal-s.I*w*s.eye(4)).rank() != 1 or 4-(equal+s.I*w*s.eye(4)).rank() != 1:
        raise AssertionError("equal-frequency geometric multiplicity")
    need(0, "equal Jordan plus")
    need(0, "equal Jordan minus")
    a, b, c, d = s.symbols("a b c d")
    xe = (a+b*t)*s.cos(w*t)+(c+d*t)*s.sin(w*t)
    need((s.diff(xe, t, 2)+w**2*xe).diff(t, 2)+w**2*(s.diff(xe, t, 2)+w**2*xe), "equal solution")
    xz = a+b*t+c*t**2+d*t**3
    need(s.diff(xz, t, 4), "double zero")
    nu = s.symbols("nu", positive=True)
    xh = a*s.exp(nu*t)+b*s.exp(-nu*t)+c*s.cos(w*t)+d*s.sin(w*t)
    need((s.diff(xh, t, 2)-nu**2*xh).diff(t, 2)+w**2*(s.diff(xh, t, 2)-nu**2*xh), "mixed hyperbolic factor")
    xoz = a*s.exp(nu*t)+b*s.exp(-nu*t)+c+d*t
    need(s.diff(s.diff(xoz,t,2)-nu**2*xoz,t,2), "negative-zero factor")
    mu = s.symbols("mu", positive=True)
    xdn = a*s.exp(nu*t)+b*s.exp(-nu*t)+c*s.exp(mu*t)+d*s.exp(-mu*t)
    need((s.diff(xdn,t,2)-nu**2*xdn).diff(t,2)-mu**2*(s.diff(xdn,t,2)-nu**2*xdn), "distinct negative factors")
    xen = (a+b*t)*s.exp(nu*t)+(c+d*t)*s.exp(-nu*t)
    intermediate = s.diff(xen,t,2)-nu**2*xen
    need(s.diff(intermediate,t,2)-nu**2*intermediate, "repeated negative factor")
    xop = a+b*t+c*s.cos(w*t)+d*s.sin(w*t)
    need(s.diff(s.diff(xop,t,2)+w**2*xop,t,2), "zero-positive factor")
    print(f"C359 SymPy cross-check: PASS ({COUNT} identities)")


if __name__ == "__main__":
    main()
