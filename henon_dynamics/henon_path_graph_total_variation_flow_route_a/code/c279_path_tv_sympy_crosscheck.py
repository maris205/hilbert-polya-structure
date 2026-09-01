#!/usr/bin/env python3
"""Independent symbolic reconstruction for HCS-C279."""
from __future__ import annotations

import itertools

import sympy as sp


def incidence(n: int) -> sp.Matrix:
    matrix = sp.zeros(max(0, n - 1), n)
    for edge in range(n - 1):
        matrix[edge, edge] = -1
        matrix[edge, edge + 1] = 1
    return matrix


def main() -> None:
    checks = 0

    # Translation nullspace, zero total subgradient, and exact recovery of an
    # arbitrary edge flux from D^T z by prefix sums.
    for n in range(1, 10):
        dmat = incidence(n)
        ones = sp.ones(n, 1)
        assert dmat * ones == sp.zeros(max(0, n - 1), 1)
        checks += 1
        if n > 1:
            z = sp.Matrix(sp.symbols(f"z0:{n - 1}"))
            gradient = dmat.T * z
            assert sp.simplify(sum(gradient)) == 0
            checks += 1
            for edge in range(n - 1):
                recovered = -sum(gradient[index] for index in range(edge + 1))
                assert sp.simplify(recovered - z[edge]) == 0
                checks += 1

    # On every possible plateau interval, interpolate its boundary signs.
    # The resulting D^T z is constant on the interval, proving the block-speed
    # formula.  Endpoint signs are fixed to zero.
    for n in range(1, 10):
        dmat = incidence(n)
        for lo in range(n):
            for hi in range(lo, n):
                left_choices = [0] if lo == 0 else [-1, 1]
                right_choices = [0] if hi == n - 1 else [-1, 1]
                for left, right in itertools.product(left_choices, right_choices):
                    if n == 1:
                        gradient = sp.zeros(1, 1)
                        expected = sp.Integer(0)
                    else:
                        flux = sp.zeros(n - 1, 1)
                        if lo > 0:
                            flux[lo - 1] = left
                        if hi < n - 1:
                            flux[hi] = right
                        size = hi - lo + 1
                        for edge in range(lo, hi):
                            flux[edge] = sp.Rational(left) + sp.Rational(edge - lo + 1, size) * (right - left)
                            assert abs(flux[edge]) <= 1
                            checks += 1
                        gradient = dmat.T * flux
                        expected = sp.Rational(left - right, size)
                    for coordinate in range(lo, hi + 1):
                        assert sp.simplify(gradient[coordinate] - expected) == 0
                        checks += 1

    # Euler's identity <D^T s,x>=J(x) and the two differential dissipation
    # identities in every open sign chamber up to n=8.
    for n in range(2, 9):
        dmat = incidence(n)
        amplitudes = sp.Matrix(sp.symbols(f"a0:{n - 1}", positive=True))
        for signs in itertools.product((-1, 1), repeat=n - 1):
            svec = sp.Matrix(signs)
            jumps = sp.Matrix([signs[index] * amplitudes[index] for index in range(n - 1)])
            coordinates = [sp.Integer(0)]
            for jump in jumps:
                coordinates.append(coordinates[-1] + jump)
            xvec = sp.Matrix(coordinates)
            gradient = dmat.T * svec
            velocity = -gradient
            total_variation = sum(amplitudes)
            assert sp.simplify((gradient.T * xvec)[0] - total_variation) == 0
            assert sp.simplify((svec.T * dmat * velocity)[0] + (velocity.T * velocity)[0]) == 0
            mean = sum(xvec) / n
            centred = xvec - mean * sp.ones(n, 1)
            assert sp.simplify((centred.T * velocity)[0] + total_variation) == 0
            checks += 3

    # Exact coefficient identity behind ||x-mean(x)1||_2 <= sqrt(n) J(x).
    for n in range(2, 13):
        jumps = sp.symbols(f"d0:{n - 1}", real=True)
        coordinates = [sp.Integer(0)]
        for jump in jumps:
            coordinates.append(coordinates[-1] + jump)
        mean = sum(coordinates) / n
        for coordinate in range(n):
            expansion = sp.Integer(0)
            for edge, jump in enumerate(jumps):
                coefficient = (1 if edge < coordinate else 0) - sp.Rational(n - edge - 1, n)
                assert abs(coefficient) <= 1
                expansion += coefficient * jump
                checks += 1
            assert sp.simplify(coordinates[coordinate] - mean - expansion) == 0
            checks += 1

    # A concrete simultaneous collision reconstructs the joint-merger rule.
    x = sp.Matrix([0, 2, 0, 2, 0])
    dmat = incidence(5)
    signs = sp.Matrix([1, -1, 1, -1])
    velocity = -(dmat.T * signs)
    assert velocity == sp.Matrix([1, -2, 2, -2, 1])
    collision_times = []
    for edge in range(4):
        denominator = velocity[edge] - velocity[edge + 1]
        if denominator:
            candidate = sp.Rational(x[edge + 1] - x[edge], denominator)
            if candidate > 0:
                collision_times.append(candidate)
    first = min(collision_times)
    state = x + first * velocity
    assert first == sp.Rational(1, 2)
    assert state == sp.Matrix([sp.Rational(1, 2), 1, 1, 1, sp.Rational(1, 2)])
    checks += 2

    print(f"C279_SYMPY_PASS ({checks} symbolic identities and inequalities)")


if __name__ == "__main__":
    main()
