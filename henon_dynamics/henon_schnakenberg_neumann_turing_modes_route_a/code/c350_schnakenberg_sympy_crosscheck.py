#!/usr/bin/env python3
"""Independent symbolic lane for the HCS-C350 theorem algebra."""
import sys

import sympy as sp


def main():
    if sys.flags.optimize:
        raise RuntimeError("C350 SymPy lane refuses optimized Python")
    a, b, du, dv, mu, lam = sp.symbols("a b d_u d_v mu lambda", positive=True)
    s = a + b
    u, v = sp.symbols("u v", positive=True)
    f = a - u + u**2 * v
    g = b - u**2 * v
    J = sp.Matrix([f, g]).jacobian([u, v]).subs({u: s, v: b / s**2})
    expected = sp.Matrix([[(b-a)/s, s**2], [-2*b/s, -s**2]])
    checks = 0
    assert sp.simplify(J - expected) == sp.zeros(2); checks += 4
    assert sp.simplify(J.trace() - ((b-a)/s-s**2)) == 0; checks += 1
    assert sp.simplify(J.det() - s**2) == 0; checks += 1
    M = J - sp.diag(du*mu, dv*mu)
    B = dv*(b-a)/s - du*s**2
    D = du*dv*mu**2 - B*mu + s**2
    assert sp.simplify(M.det()-D) == 0; checks += 1
    assert sp.simplify(M.trace()-((b-a)/s-s**2-(du+dv)*mu)) == 0; checks += 1
    assert sp.simplify((lam*sp.eye(2)-M).det() - (lam**2-M.trace()*lam+D)) == 0; checks += 1
    d = sp.symbols("d", positive=True)
    assert sp.simplify(B.subs({du:d,dv:d}) - d*J.trace()) == 0; checks += 1
    # Designed exact lower endpoint and double-wall controls.
    controls = [
        (sp.Rational(1,10),sp.Rational(9,10),1,sp.Rational(100,11),sp.Rational(1,4),0),
        (sp.Rational(1,10),sp.Rational(9,10),1,sp.Rational(100,11),sp.Rational(11,25),0),
        (sp.Rational(1,9),sp.Rational(8,9),1,9,sp.Rational(1,3),0),
    ]
    for aa,bb,duu,dvv,muu,target in controls:
        assert sp.simplify(D.subs({a:aa,b:bb,du:duu,dv:dvv,mu:muu})-target)==0
        checks += 1
    Q = sp.expand(B**2-4*du*dv*s**2)
    assert sp.simplify(Q.subs({a:sp.Rational(1,9),b:sp.Rational(8,9),du:1,dv:9}))==0; checks += 1
    print(f"C350 SymPy cross-check: PASS {checks} exact identities")


if __name__ == "__main__":
    main()
