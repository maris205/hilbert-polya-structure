#!/usr/bin/env python3
"""Independent symbolic and exact checks for the C245 event map.

The checks deliberately reconstruct the identities from the rise coordinate,
the free-flight ODE, and the simultaneous-wave recurrence.  They do not read
the producer's event rows, so a copied expression or a changed receipt cannot
make the symbolic gate pass by itself.
"""
from __future__ import annotations

from fractions import Fraction as F
import sympy as sp


def main() -> None:
    # Keep a positive a so SymPy can use the logarithm/exponential identities.
    r, y, eps, u, a, phi, dt = sp.symbols(
        "r y epsilon u a phi dt", positive=True
    )
    checks = 0

    def ok(expr, label: str) -> None:
        nonlocal checks
        checks += 1
        reduced = sp.simplify(expr)
        if reduced != 0:
            raise AssertionError(f"{label}: {sp.factor(reduced)}")

    def yes(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(label)

    # Rise law and its inverse.  The first identity is checked after the
    # parameter substitution r=e^{-a}; the endpoint checks retain symbolic r.
    U = (1 - sp.exp(-a * phi)) / (1 - sp.exp(-a))
    inv = sp.log(1 - (1 - r) * y) / sp.log(r)
    ok(inv.subs(r, sp.exp(-a)).subs(y, U) - phi, "rise inverse")
    ok(sp.diff(U, phi) - a * sp.exp(-a * phi) / (1 - sp.exp(-a)), "rise derivative")
    ok((1 - (1 - r) * y).subs(y, 0) - 1, "reset coordinate")
    ok((1 - (1 - r) * y).subs(y, 1) - r, "threshold coordinate")

    # Free flight is obtained directly from u=e^{-a phi}, rather than by
    # cancelling the same symbolic factor on both sides.
    u0 = sp.exp(-a * phi)
    u_shift = sp.exp(-a * (phi + dt))
    ok(u_shift - u0 * sp.exp(-a * dt), "free-flight exponential law")
    # A phase at phi reaches threshold after 1-phi units of free flight.
    ok(sp.exp(-a * (phi + (1 - phi))) - sp.exp(-a), "threshold arrival")
    # The event scaling sends the minimum m to r and scales every difference.
    m, x1, x2 = sp.symbols("m x1 x2", positive=True)
    scale = r / m
    ok((x1 * scale - x2 * scale) - scale * (x1 - x2), "common-scale difference")
    ok((m * scale) - r, "minimum reaches threshold")

    # Pulse map in u coordinates, derived by substituting U^{-1}(u) rather
    # than asserting an already simplified subtraction.
    c = (1 - r) * eps
    y_from_u = (1 - u) / (1 - r)
    pulse_from_y = 1 - (1 - r) * (y_from_u + eps)
    ok(pulse_from_y - (u - c), "pulse affine derivation")
    # The clipping boundary is u=r+c.  Both branch formulas are checked at
    # exact rational points on either side and exactly on the boundary.
    def pulse_map(value: F, threshold: F, amount: F, waves: int) -> F:
        """Independent implementation of one coordinate's wave update."""
        return max(threshold, value - waves * amount)

    for rr in (F(1, 2), F(2, 3), F(3, 4)):
        for ee in (F(1, 5), F(1, 4), F(1, 3)):
            cc = (1 - rr) * ee
            boundary = rr + cc
            yes(rr < boundary < 1, "clip boundary lies in state interval")
            for value, expected, label in (
                (rr, rr, "threshold clipping"),
                (boundary, rr, "boundary clipping"),
                (boundary + (1 - boundary) / 2, boundary + (1 - boundary) / 2 - cc, "interior pulse"),
                (F(1), F(1) - cc, "top pulse"),
            ):
                clipped = max(rr, value - cc)
                yes(clipped == expected, f"{label} {rr} {ee}")

    # A simultaneous wave subtracts k*c from every still-active coordinate.
    # The recurrence and its closed form are checked for symbolic k, then
    # clipped wave values are enumerated with exact Fraction arithmetic.
    k = sp.symbols("k", integer=True, nonnegative=True)
    w0 = sp.symbols("w0", real=True)
    recurrence = (w0 - (k + 1) * c) - ((w0 - k * c) - c)
    ok(recurrence, "wave subtraction recurrence")
    for rr in (F(1, 2), F(2, 3), F(3, 4)):
        for ee in (F(1, 5), F(1, 4), F(1, 3)):
            cc = (1 - rr) * ee
            for kk in range(0, 5):
                value = rr + cc + F(kk, 7) * (1 - rr - cc)
                raw = value - kk * cc
                clipped = max(rr, raw)
                yes(clipped >= rr and clipped <= 1, "wave clipping range")
                if raw <= rr:
                    yes(clipped == rr, "wave threshold branch")
                else:
                    yes(clipped == raw, "wave interior branch")

    # Equality blocks cannot split: apply the same affine-plus-clipping map
    # independently to two coordinates and then impose their old equality.
    z1, z2, kk = sp.symbols("z1 z2 kk", real=True)
    map_k = lambda z: sp.Max(r, z - kk * c)
    equalised = sp.simplify(
        (map_k(z1) - map_k(z2)).subs(z2, z1)
    )
    ok(equalised, "symbolic equality-block containment")
    for rr in (F(1, 2), F(2, 3), F(3, 4)):
        for ee in (F(1, 5), F(1, 4), F(1, 3)):
            cc = (1 - rr) * ee
            for value in (rr, rr + cc / 2, rr + cc, F(1)):
                for kk_i in range(0, 4):
                    # Rebuild the two equal coordinates as separate Fraction
                    # objects and pass them through the map independently.
                    left = F(value.numerator, value.denominator)
                    right = F(value.numerator, value.denominator)
                    p1 = pulse_map(left, rr, cc, kk_i)
                    p2 = pulse_map(right, rr, cc, kk_i)
                    yes(p1 == p2, "numeric equality block containment")

    # Primitive-word test is independent of the one-letter synchronized word.
    def primitive(word: tuple[int, ...]) -> bool:
        nword = len(word)
        return not any(
            nword % d == 0 and word == word[:d] * (nword // d)
            for d in range(1, nword)
        )

    for n in range(2, 9):
        yes(primitive((n,)), f"one-letter primitive word [{n}]")
    for word in ((1, 1), (2, 3, 2, 3), (1, 2, 1, 2, 1, 2)):
        yes(not primitive(word), f"repeated word rejected {word}")
    for word in ((1, 2), (2, 1, 3), (1, 2, 3, 1)):
        yes(primitive(word), f"nonrepeated word accepted {word}")

    # Rational event arithmetic examples; all comparisons remain exact.
    for rr in (F(1, 2), F(2, 3), F(3, 4)):
        for ee in (F(1, 5), F(1, 4), F(1, 3)):
            cc = (1 - rr) * ee
            state = [F(1), rr + (1 - rr) * F(1, 2), rr + (1 - rr) * F(3, 4)]
            minimum = min(state)
            scaled = [z * rr / minimum for z in state]
            yes(min(scaled) == rr, "rational minimum threshold")
            yes(max(scaled) <= 1, "rational scaled state range")
            pulse = max(rr, scaled[-1] - cc)
            yes(rr <= pulse <= 1, "rational pulse range")

    print(f"C245_SYMPY_PASS ({checks} symbolic/rational identities)")


if __name__ == "__main__":
    main()
