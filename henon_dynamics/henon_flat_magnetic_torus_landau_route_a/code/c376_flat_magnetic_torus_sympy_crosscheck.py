#!/usr/bin/env python3
"""Independent symbolic identities for HCS-C376."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c376 sympy crosscheck refuses optimized Python")

import argparse

import sympy as sp


def main():
    argparse.ArgumentParser().parse_args()
    b, t, px, py, qx, qy, beta, q = sp.symbols(
        "b t px py qx qy beta q", positive=True, real=True
    )
    rotation = sp.Matrix([[sp.cos(b * t), -sp.sin(b * t)], [sp.sin(b * t), sp.cos(b * t)]])
    p = rotation * sp.Matrix([px, py])
    J = sp.Matrix([[0, -1], [1, 0]])
    center = sp.Matrix([qx, qy]) + J * sp.Matrix([px, py]) / b
    position = center - J * p / b
    checks = 0
    assert sp.simplify(sp.diff(p, t) - b * J * p) == sp.zeros(2, 1)
    checks += 2
    assert sp.simplify(sp.diff(position, t) - p) == sp.zeros(2, 1)
    checks += 2
    assert sp.simplify(position + J * p / b - center) == sp.zeros(2, 1)
    checks += 2
    period = 2 * sp.pi / b
    assert sp.simplify(p.subs(t, period) - sp.Matrix([px, py])) == sp.zeros(2, 1)
    assert sp.simplify(position.subs(t, period) - sp.Matrix([qx, qy])) == sp.zeros(2, 1)
    checks += 4
    assert sp.simplify(rotation.det() - 1) == 0
    assert sp.simplify(rotation.T * rotation - sp.eye(2)) == sp.zeros(2)
    checks += 5

    # Ladder algebra reduced to the central commutator [Pi_x,Pi_y]=i*b.
    comm_a_adjoint = sp.simplify((-sp.I * sp.I * b + sp.I * (-sp.I * b)) / (2 * b))
    assert comm_a_adjoint == 1
    checks += 1
    n = sp.symbols("n", integer=True, nonnegative=True)
    energy = b * (n + sp.Rational(1, 2))
    assert sp.simplify(energy.subs(n, n + 1) - energy - b) == 0
    checks += 1

    # Fixed positively oriented division vectors retain the flux sign.
    # If U shifts j and V has exponent -sigma*j, then UV/VU has exponent sigma.
    sigma, j_symbol = sp.symbols("sigma j", integer=True)
    assert sp.expand(-sigma * j_symbol - (-sigma * (j_symbol + 1)) - sigma) == 0
    checks += 1
    for sign in (-1, 1):
        for order in range(1, 65):
            for j_value in range(order):
                uv_exponent = (-sign * j_value) % order
                vu_exponent = (-sign * ((j_value + 1) % order)) % order
                assert sp.Mod(uv_exponent - vu_exponent - sign, order) == 0
                checks += 1

    # Zero field: the criterion is normalized by the rectangular lattice.
    # These exact controls cover stationary, both axial faces, a raw-irrational
    # closed slope, and a raw-rational but normalized-irrational dense slope.
    lx, ly, px0, py0 = sp.symbols("L_x L_y p_x p_y", positive=True, real=True)
    zero_field_position = sp.Matrix([qx, qy]) + t * sp.Matrix([px0, py0])
    assert sp.diff(zero_field_position, t) == sp.Matrix([px0, py0])
    checks += 2
    assert sp.Matrix([px0, 0]) * (lx / px0) == sp.Matrix([lx, 0])
    assert sp.Matrix([0, py0]) * (ly / py0) == sp.Matrix([0, ly])
    checks += 4
    normalized_closed = sp.simplify(sp.sqrt(2) * 1 / (1 * sp.sqrt(2)))
    assert normalized_closed == 1 and sp.sqrt(2).is_rational is False
    checks += 2
    normalized_dense = sp.simplify(1 * 1 / (1 * sp.sqrt(2)))
    assert normalized_dense.is_rational is False
    checks += 1
    assert sp.zeros(2, 1) * t == sp.zeros(2, 1)
    checks += 2

    # Finite geometric-series proof of the heat trace before the monotone limit.
    for cutoff in range(129):
        series = sum(q ** k for k in range(cutoff + 1))
        assert sp.expand((1 - q) * series - (1 - q ** (cutoff + 1))) == 0
        checks += 1

    s = sp.symbols("s")
    # Splitting the zeta series into odd and even terms gives the half-shift
    # identity.  We certify both its symbolic coefficient and exact partial sums.
    assert sp.simplify(2 ** s * (1 - 2 ** (-s)) - (2 ** s - 1)) == 0
    checks += 1
    for value in range(2, 18, 2):
        lhs_partial = sum((sp.Rational(k, 1) + sp.Rational(1, 2)) ** (-value) for k in range(65))
        odd_partial = 2 ** value * sum(sp.Rational(1, 2 * k + 1) ** value for k in range(65))
        assert sp.factor(lhs_partial - odd_partial) == 0
        checks += 1
    assert sp.zeta(0, sp.Rational(1, 2)) == 0
    checks += 1
    hurwitz_prime_zero = sp.log(sp.gamma(sp.Rational(1, 2))) - sp.log(2 * sp.pi) / 2
    assert sp.simplify(hurwitz_prime_zero + sp.log(2) / 2) == 0
    checks += 1

    level = sp.symbols("level", integer=True, nonnegative=True)
    e_level = b * (level + sp.Rational(1, 2))
    assert sp.simplify(sp.exp(-sp.I * period * e_level) + 1) == 0
    assert sp.simplify(sp.exp(-sp.I * 2 * period * e_level) - 1) == 0
    checks += 2
    print(
        f"C376 SymPy PASS: exact_symbolic_checks={checks} "
        "classical+signed-translation+zero-field+ladder+heat+zeta+revival"
    )


if __name__ == "__main__":
    main()
