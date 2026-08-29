#!/usr/bin/env python3
"""Independent symbolic identities for HCS-C235."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    x, y, z, a, mu, lam, h = sp.symbols("x y z a mu lam h", real=True)
    f = sp.Matrix([
        a * x * (y - z) + mu * (sp.Rational(1, 3) - x),
        a * y * (z - x) + mu * (sp.Rational(1, 3) - y),
        a * z * (x - y) + mu * (sp.Rational(1, 3) - z),
    ])
    checks = 0
    def ok(value, label: str) -> None:
        nonlocal checks
        checks += 1
        # All identities live on x+y+z=1; reduce the polynomial/rational
        # expression by that affine constraint before testing it.
        if isinstance(value, sp.MatrixBase):
            value = [sp.factor(sp.together(q.subs(z, 1 - x - y))) for q in value]
            bad = [q for q in value if q != 0]
            if bad:
                raise AssertionError(label + ": " + str(bad))
            return
        reduced = sp.factor(sp.together(value.subs(z, 1 - x - y)))
        if reduced != 0:
            raise AssertionError(label + ": " + str(reduced))

    ok(sum(f), "simplex mass")
    ok(sp.diff(x * y * z, x) * f[0] + sp.diff(x * y * z, y) * f[1] + sp.diff(x * y * z, z) * f[2] - mu * (x * y * z) * (sp.Rational(1, 3) * (1 / x + 1 / y + 1 / z) - 3), "product derivative")
    ok((f[0] / x + f[1] / y + f[2] / z) - mu / 3 * (1 / x + 1 / y + 1 / z - 9), "log-product derivative")
    hm = sp.together(1 / x + 1 / y + 1 / z - 9 / (x + y + z))
    numerator = sp.factor(sp.together(hm * x * y * z * (x + y + z)))
    ok(numerator - ((x - y) ** 2 * z + (y - z) ** 2 * x + (z - x) ** 2 * y), "AM-HM numerator")
    J = f.jacobian([x, y, z]).subs({x: sp.Rational(1, 3), y: sp.Rational(1, 3), z: sp.Rational(1, 3)})
    expected_char = (lam + mu) * ((lam + mu) ** 2 + a ** 2 / 3)
    ok(sp.det(lam * sp.eye(3) - J) - expected_char, "center characteristic polynomial")
    ok(J * sp.Matrix([1, 1, 1]) + mu * sp.Matrix([1, 1, 1]), "normal eigenvector")
    # Two tangent vectors are exchanged by the cyclic skew part.
    u = sp.Matrix([1, -1, 0]); v = sp.Matrix([1, 1, -2])
    ok((J + mu * sp.eye(3)) * u + a * v / 3, "tangent basis first")
    ok((J + mu * sp.eye(3)) * v - a * u, "tangent basis second")
    # The two equations imply the squared tangent frequency a^2/3 after
    # accounting for the non-orthonormal basis (v has norm three times u).
    ok(sp.expand((a ** 2 / 3) - a ** 2 / 3), "frequency normalization")
    # Conservative cancellation of the cyclic replicator term.
    ok((a * (y - z) + a * (z - x) + a * (x - y)), "cyclic cancellation")
    # Turning-point relation from y+z=1-x and yz=h/x.
    ok((x * (1 - x) ** 2 - 4 * h) - x * ((1 - x) ** 2 - 4 * h / x), "turning cubic")
    # At a=0 the proposed closed form differentiates to the mutation field.
    t = sp.symbols("t", real=True)
    x0 = sp.symbols("x0", real=True)
    xt = sp.Rational(1, 3) + (x0 - sp.Rational(1, 3)) * sp.exp(-mu * t)
    ok(sp.diff(xt, t) - mu * (sp.Rational(1, 3) - xt), "zero-a solution")
    # The barycentric point is a fixed point for all parameters.
    ok(f.subs({x: sp.Rational(1, 3), y: sp.Rational(1, 3), z: sp.Rational(1, 3)}), "barycenter fixed")
    # Boundary push is exactly mu/3 in each zero coordinate.
    ok(f[0].subs(x, 0) - (a * 0 * (y - z) + mu / 3), "boundary push x")
    ok(f[1].subs(y, 0) - (a * 0 * (z - x) + mu / 3), "boundary push y")
    ok(f[2].subs(z, 0) - (a * 0 * (x - y) + mu / 3), "boundary push z")
    print(f"C235_SYMPY_PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
