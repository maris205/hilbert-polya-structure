#!/usr/bin/env python3
"""Independent symbolic lane for HCS-C354."""
from __future__ import annotations

import sys
from fractions import Fraction as Q

import sympy as s

COUNT = 0


def need(expr, label):
    global COUNT
    COUNT += 1
    if s.simplify(expr) != 0:
        raise AssertionError(label)


def main():
    if sys.flags.optimize:
        raise RuntimeError("C354 SymPy lane refuses optimized Python")
    A, C, gamma, L, G, E, u = s.symbols("A C gamma L G E u", nonzero=True)
    veff = G**2/(2*C)+gamma*u+(L-G*u)**2/(2*A*(1-u**2))
    P = s.expand(2*A*(1-u**2)*(E-veff))
    target = s.expand(2*A*(E-G**2/(2*C)-gamma*u)*(1-u**2)-(L-G*u)**2)
    need(P-target, "energy reduction")
    cs = [2*A*E-A*G**2/C-L**2, 2*(L*G-A*gamma), A*G**2/C-2*A*E-G**2, 2*A*gamma]
    need(P-sum(cs[i]*u**i for i in range(4)), "coefficient expansion")
    need(target.subs(u, 1)+(L-G)**2, "north pole")
    need(target.subs(u, -1)+(L+G)**2, "south pole")
    phi = (L-G*u)/(A*(1-u**2)); psi = G/C-u*phi
    need(A*(1-u**2)*phi+G*u-L, "vertical momentum")
    need(C*(psi+u*phi)-G, "axial momentum")
    need((L-G*u)/(1-u**2)-(L-G)/(2*(1-u))-(L+G)/(2*(1+u)), "phi partial fractions")
    need((G-L*u)/(1-u**2)-(G-L)/(2*(1-u))-(G+L)/(2*(1+u)), "psi partial fractions")
    a, b, c, d = s.symbols("a b c d")
    cubic_disc = s.discriminant(a*u**3+b*u**2+c*u+d, u)
    need(cubic_disc-(b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d), "cubic discriminant")
    z = s.symbols("z")
    samples = [
        (Q(1), Q(1), Q(-3, 4), Q(1, 4), Q(3, 2)),
        (Q(2), Q(3), Q(-2, 3), Q(1, 3), Q(5, 3)),
        (Q(3), Q(2), Q(-1, 2), Q(1, 2), Q(2)),
        (Q(5, 2), Q(4), Q(-4, 5), Q(1, 5), Q(6, 5)),
    ]
    for av, gv, r1, r2, r3 in samples:
        vals = [s.Rational(x.numerator, x.denominator) for x in (av, gv, r1, r2, r3)]
        avs, gvs, x1, x2, x3 = vals
        gap, outer = x2-x1, x3-x1
        k2, nu2 = gap/outer, gvs*outer/(2*avs)
        uu = x1+gap*z
        lhs = 4*avs**2*gap**2*nu2*z*(1-z)*(1-k2*z)
        rhs = 2*avs*gvs*(uu-x1)*(uu-x2)*(uu-x3)
        need(lhs-rhs, "Jacobi substitution")
        need(k2-gap/outer, "modulus")
        need(4*nu2-2*gvs*outer/avs, "frequency")
        need((1-uu)-(1-x1)*(1-gap/(1-x1)*z), "north Pi transform")
        need((1+uu)-(1+x1)*(1+gap/(1+x1)*z), "south Pi transform")
    steady = {A: 1, C: 1, gamma: 8, L: 3, G: 0, E: 2}
    need(target.subs(steady).subs(u, -s.Rational(1, 2)), "steady P")
    need(s.diff(target, u).subs(steady).subs(u, -s.Rational(1, 2)), "steady P prime")
    # Repeated exact specializations protect signs and denominator factors.
    for n in range(1, 65):
        values = {A: s.Rational(n+1, n), C: s.Rational(n+2, n+1), gamma: s.Rational(n+3, n+2), L: s.Rational(n-2, n+1), G: s.Rational(2-n, n+2), E: s.Rational(n+4, n+3), u: s.Rational((n % 5)-2, 5)}
        need((P-target).subs(values), "specialized reduction")
        need((A*(1-u**2)*phi+G*u-L).subs(values), "specialized L")
        need((C*(psi+u*phi)-G).subs(values), "specialized G")
    print(f"C354 SymPy cross-check: PASS ({COUNT} identities)")


if __name__ == "__main__":
    main()
