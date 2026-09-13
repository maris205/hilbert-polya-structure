#!/usr/bin/env python3
"""Exact finite identities for the first cyclotomic jet; no data files or fits.

The universal-prime claims require the separate matrix/Cartier/geometric
proofs. This script checks only the displayed rational polynomial identities.
"""
import sympy as sp


def main():
    x, y, t, z, u, v, h = sp.symbols("x y t z u v h")
    J = y + x / y - x - t / x
    b = x * (y - 1)
    A0 = sp.Matrix([[t - b, -x], [-(y - 1) * (t - b), b]])
    A1 = sp.Matrix([[J - 1, 1], [J - 1 + b, 1]])
    A2 = sp.diag(1, 0)
    A = A0 + z * A1 + z**2 * A2
    assert sp.cancel(A.det() - z**3) == 0
    assert sp.cancel(sp.trace(A) - (t + J * z + z**2)) == 0
    I2 = sp.trace(A0 * A2 + A2 * A0 - A1 * A1)
    assert sp.cancel(I2 - (2 * t - 4 * b - J**2)) == 0
    W2 = x * y * (sp.diff(b, x) * sp.diff(J, y)
                  - sp.diff(b, y) * sp.diff(J, x))
    # Equality in the localized characteristic-two energy-zero curve.
    n2 = sp.fraction(sp.together(W2 - t))[0]
    curve2 = sp.expand(x * y * J)
    assert sp.groebner([curve2], t, y, x, modulus=2).reduce(sp.expand(n2))[1] == 0

    W = 1 + u * v
    Ju = W - v / W - t * u
    G = sp.diag(u, 1)
    Ag = G * A.subs({x: 1 / u, y: W}, simultaneous=True) * G.inv()
    Ahat = (sp.Matrix([[t - v, -1], [-v * (t - v), v]])
            + z * sp.Matrix([[Ju - 1, u], [v - t + v**2 / W, 1]])
            + z**2 * A2)
    assert all(sp.cancel(c) == 0 for c in Ag - Ahat)
    assert sp.cancel(Ahat.det() - z**3) == 0

    endpoint = Ahat.subs(u, 0)
    duA = Ahat.diff(u).subs(u, 0)
    dvA = Ahat.diff(v).subs(u, 0)
    tangentJ = v + v**2 - t
    B = z * endpoint.diff(z)
    commutator = endpoint * B - B * endpoint
    R = sp.expand(sp.trace((duA + tangentJ * dvA) * commutator).subs(v, 1 - h))
    R_expected = ((h**2 - 3*h - t + 2) * z**4
                  + (-2*h**3 + 14*h**2 + 6*h*t - 24*h - 8*t + 12) * z**3
                  + (-h**4 + 3*h**3 - 2*h**2 + 5*h*t + 3*t**2 - 4*t) * z**2
                  + (-h**3*t + 3*h**2*t + h*t**2 - 2*h*t) * z)
    assert sp.expand(R - R_expected) == 0
    print("PASS: original trace/determinant, exact I2, char-2 tangent identity")
    print("PASS: first-endpoint regular gauge, all four coefficients of R")
    print("R =", sp.collect(R, z))


if __name__ == "__main__":
    main()
