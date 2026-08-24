#!/usr/bin/env python3
"""Separate symbolic reconstruction of the C137 analytic identities."""
from itertools import product
import sympy as sp


def main() -> None:
    a, b, t, s, r = sp.symbols("a b t s r", positive=True)
    Ma = sp.Matrix([[0, 1], [1, a]])
    Mb = sp.Matrix([[0, 1], [1, b]])
    checks = 0
    center = t/(t**2-1)
    radius = 1/(t**2-1)
    assert sp.factor(center+radius-1/(t-1)) == 0
    checks += 1
    assert sp.Rational(1, sp.Rational(7,2)+1)-sp.Rational(1, 6-1) == sp.Rational(1,45)
    assert sp.Rational(1,4+1)-sp.Rational(1,6-1) == 0
    checks += 2
    assert sp.summation((r+1)*sp.Rational(1,2)**r, (r,0,sp.oo)) == 4
    assert sp.summation((r+1)*sp.Rational(1,5)**r, (r,0,sp.oo)) == sp.Rational(25,16)
    assert sp.summation((r+1)*r*sp.Rational(1,2)**(r-1)*sp.Rational(1,4), (r,1,sp.oo)) == 4
    assert sp.summation((r+1)*r*sp.Rational(1,5)**(r-1)*sp.Rational(1,25), (r,1,sp.oo)) == sp.Rational(5,32)
    checks += 4
    M1 = Ma**3*Mb**2
    M2 = Ma**2*Mb*Ma*Mb
    trace1, trace2 = sp.expand(sp.trace(M1)), sp.expand(sp.trace(M2))
    expected1 = a**3*b**2+a**3+2*a**2*b+2*a*b**2+3*a+2*b
    expected2 = a**3*b**2+4*a**2*b+a*b**2+3*a+2*b
    assert sp.expand(trace1-expected1) == 0
    assert sp.expand(trace2-expected2) == 0
    assert sp.factor(trace1-trace2) == a*(a-b)**2
    checks += 3
    values_a = [sp.Integer(3), sp.Rational(13,4), sp.Rational(7,2)]
    values_b = [sp.Integer(6), sp.Rational(13,2), sp.Integer(7)]
    for av, bv in product(values_a, values_b):
        assert sp.expand((trace1-trace2).subs({a:av,b:bv})) == av*(bv-av)**2
        checks += 1
        for n in range(1, 9):
            for word in product((0,1), repeat=n):
                M = sp.eye(2)
                for letter in word:
                    M *= (Ma if letter == 0 else Mb).subs({a:av,b:bv})
                tr = sp.trace(M)
                det = M.det()
                disc = tr**2-4*det
                A,B,C,D = M[0,0],M[0,1],M[1,0],M[1,1]
                fixed = (A-D+s)/(2*C)
                numerator = sp.together(C*fixed**2+(D-A)*fixed-B).as_numer_denom()[0]
                assert det == (-1)**n
                assert sp.rem(sp.Poly(numerator,s),sp.Poly(s**2-disc,s)).is_zero
                assert sp.expand(disc-((D-A)**2+4*B*C)) == 0
                multiplier = (tr-s)/(tr+s)
                assert sp.cancel(1/(1-multiplier)-(sp.Rational(1,2)+tr/(2*s))) == 0
                checks += 4
    print(f"C137 SymPy cross-check: PASS ({checks} exact checks)")


if __name__ == "__main__":
    main()
