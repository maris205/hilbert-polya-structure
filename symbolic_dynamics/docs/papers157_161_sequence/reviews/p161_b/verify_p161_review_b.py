#!/usr/bin/env python3
"""Independent normalized exact controls for P161 Hostile Review B.

This reviewer-owned program imports no author or Review-A code.  Translation
equivariance lets it enumerate ordered affine bases (u,v), representing the
triangle (0,u,v), rather than repeat the same calculation at every basepoint.
For p=3,7,11,19 it solves each orthocenter from the two altitude equations,
checks the literal four windows or the directed singular transition, and
checks the forced reverse candidate target by target.  It also verifies
translation equivariance exhaustively at p=3,7 and records p=5 as an
isotropic negative control.

The computation is bounded counterexample pressure, not an all-prime proof
and not a novelty, ownership, or external-release certificate.
"""

from __future__ import annotations

from collections import Counter
from itertools import product


ASSERTIONS = 0
SINK = None


def require(condition: bool, label: object) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def add(a, b, p: int):
    return ((a[0] + b[0]) % p, (a[1] + b[1]) % p)


def neg(a, p: int):
    return ((-a[0]) % p, (-a[1]) % p)


def sub(a, b, p: int):
    return add(a, neg(b, p), p)


def dot(a, b, p: int) -> int:
    return (a[0] * b[0] + a[1] * b[1]) % p


def det(a, b, p: int) -> int:
    return (a[0] * b[1] - a[1] * b[0]) % p


def is_triangle(triangle, p: int) -> bool:
    a, b, c = triangle
    return det(sub(b, a, p), sub(c, a, p), p) != 0


def solve_rows(r1, rhs1: int, r2, rhs2: int, p: int):
    determinant = det(r1, r2, p)
    require(determinant != 0, ("independent altitude rows", p, r1, r2))
    inverse = pow(determinant, -1, p)
    return (
        (rhs1 * r2[1] - r1[1] * rhs2) * inverse % p,
        (r1[0] * rhs2 - rhs1 * r2[0]) * inverse % p,
    )


def orthocenter(triangle, p: int):
    """Solve the displayed altitude predicates as a two-row system."""
    a, b, c = triangle
    r1 = sub(b, c, p)
    r2 = sub(a, c, p)
    h = solve_rows(r1, dot(a, r1, p), r2, dot(b, r2, p), p)
    require(dot(sub(h, a, p), r1, p) == 0, ("altitude A", p, triangle, h))
    require(dot(sub(h, b, p), r2, p) == 0, ("altitude B", p, triangle, h))
    require(
        dot(sub(h, c, p), sub(a, b, p), p) == 0,
        ("altitude C", p, triangle, h),
    )
    return h


def right_slots(triangle, p: int):
    a, b, c = triangle
    tests = (
        dot(sub(b, a, p), sub(c, a, p), p),
        dot(sub(a, b, p), sub(c, b, p), p),
        dot(sub(a, c, p), sub(b, c, p), p),
    )
    return tuple(index for index, value in enumerate(tests) if value == 0)


def transition(triangle, p: int):
    if triangle is SINK:
        return SINK
    a, b, c = triangle
    candidate = (b, c, orthocenter(triangle, p))
    return candidate if is_triangle(candidate, p) else SINK


def translate(triangle, shift, p: int):
    if triangle is SINK:
        return SINK
    return tuple(add(point, shift, p) for point in triangle)


def normalized_triangles(p: int):
    zero = (0, 0)
    vectors = tuple(product(range(p), repeat=2))
    return tuple(
        (zero, u, v)
        for u in vectors
        for v in vectors
        if det(u, v, p) != 0
    )


def verify_prime(p: int) -> str:
    require(p % 4 == 3, ("anisotropic congruence", p))
    vectors = tuple(product(range(p), repeat=2))
    for vector in vectors:
        require(
            (dot(vector, vector, p) == 0) == (vector == (0, 0)),
            ("anisotropy", p, vector),
        )

    triangles = normalized_triangles(p)
    t0 = (p * p - 1) * (p * p - p)
    r0 = (p * p - 1) * (p - 1)
    q0 = (p * p - 1) * (p - 1) * (p - 3)
    require(len(triangles) == t0, ("normalized T", p, len(triangles), t0))
    require(t0 == q0 + 3 * r0, ("normalized partition", p))
    require((p * p * q0) % 4 == 0, ("four-cycle divisibility", p))

    kinds = Counter()
    degenerate_next = 0
    valid_reverse = 0
    for triangle in triangles:
        zero, u, v = triangle
        slots = right_slots(triangle, p)
        require(len(slots) <= 1, ("right strata disjoint", p, triangle, slots))
        kind = slots[0] if slots else None
        kinds[kind] += 1

        h = orthocenter(triangle, p)
        require((h == zero) == (kind == 0), ("H=A", p, triangle, h, kind))
        require((h == u) == (kind == 1), ("H=B", p, triangle, h, kind))
        require((h == v) == (kind == 2), ("H=C", p, triangle, h, kind))

        next_state = transition(triangle, p)
        require(
            (next_state is SINK) == (kind in (1, 2)),
            ("sink source classification", p, triangle, kind),
        )
        degenerate_next += next_state is SINK

        if kind is None:
            orbit = [triangle]
            for _ in range(4):
                orbit.append(transition(orbit[-1], p))
            require(SINK not in orbit, ("nonright carrier closure", p, triangle))
            require(orbit[4] == triangle, ("fourth return", p, triangle, orbit))
            require(len(set(orbit[:4])) == 4, ("exact period four", p, triangle))
            quartet = (zero, u, v, h)
            for omit in range(4):
                window = tuple(quartet[index] for index in range(4) if index != omit)
                require(is_triangle(window, p), ("no collinear triple", p, quartet))
        elif kind == 0:
            rotated = (u, v, zero)
            require(next_state == rotated, ("right-first rotation", p, triangle))
            require(right_slots(rotated, p) == (2,), ("right-first to third", p, triangle))
            require(transition(rotated, p) is SINK, ("right-first depth two", p, triangle))
        else:
            require(next_state is SINK, ("right-second/third depth one", p, triangle))

        # A target (A,B,C) can only have the nonsink predecessor (H,A,B).
        reverse = (h, zero, u)
        reverse_is_valid = is_triangle(reverse, p)
        require(
            reverse_is_valid == (kind not in (0, 1)),
            ("reverse candidate validity", p, triangle, kind, reverse),
        )
        if reverse_is_valid:
            valid_reverse += 1
            require(transition(reverse, p) == triangle, ("reverse edge", p, triangle))

    require(kinds[0] == r0, ("R0", p, kinds))
    require(kinds[1] == r0, ("R1", p, kinds))
    require(kinds[2] == r0, ("R2", p, kinds))
    require(kinds[None] == q0, ("Q0", p, kinds))
    require(degenerate_next == 2 * r0, ("normalized sink sources", p))
    require(valid_reverse == q0 + r0, ("positive normalized fibres", p))

    # Translation equivariance turns the normalized census into the full one.
    if p in (3, 7):
        for triangle in triangles:
            base_h = orthocenter(triangle, p)
            base_next = transition(triangle, p)
            for shift in vectors:
                shifted = translate(triangle, shift, p)
                require(
                    orthocenter(shifted, p) == add(base_h, shift, p),
                    ("orthocenter translation", p, triangle, shift),
                )
                require(
                    transition(shifted, p) == translate(base_next, shift, p),
                    ("transition translation", p, triangle, shift),
                )

    t = p * p * t0
    r = p * p * r0
    q = p * p * q0
    image1 = 1 + p * p * valid_reverse
    stable = 1 + q
    sink_fibre = 1 + p * p * degenerate_next
    require(image1 == 1 + t - 2 * r, ("image-one formula", p))
    require(stable == 1 + t - 3 * r, ("stable-image formula", p))
    require(sink_fibre == 1 + 2 * r, ("sink-fibre formula", p))
    require((1 + 2 * r) + r + q == 1 + t, ("fibre mass", p))

    if p == 3:
        require((t, r, q) == (432, 144, 0), ("p=3 counts", t, r, q))
        require((image1, stable, sink_fibre) == (145, 1, 289), "p=3 boundary")

    return (
        f"p={p}:normalized={t0},T={t},R={r},Q={q},"
        f"image1={image1},stable={stable},sink_fibre={sink_fibre},"
        f"depths=0:{1+q},1:{2*r},2:{r}"
    )


def isotropic_negative_control() -> str:
    p = 5
    vectors = tuple(product(range(p), repeat=2))
    null = tuple(v for v in vectors if v != (0, 0) and dot(v, v, p) == 0)
    triangles = normalized_triangles(p)
    right_first = sum(0 in right_slots(triangle, p) for triangle in triangles)
    anisotropic_r0 = (p * p - 1) * (p - 1)
    require(len(null) == 8, ("p=5 null census", len(null)))
    require(right_first == 64, ("p=5 actual right-first", right_first))
    require(right_first != anisotropic_r0, ("p=5 scope separation", right_first))
    return (
        f"p=5:null_nonzero={len(null)},normalized_right_first={right_first},"
        f"anisotropic_formula={anisotropic_r0}"
    )


def main() -> None:
    signatures = tuple(verify_prime(p) for p in (3, 7, 11, 19))
    negative = isotropic_negative_control()
    print("P161_REVIEW_B_NORMALIZED_V1")
    for signature in signatures:
        print("EXACT", signature)
    print("SCOPE_CONTROL", negative)
    print("WINDOWS literal_four_window_or_oriented_sink_transition")
    print("FIBRES forced_reverse_candidate_checked_target_by_target")
    print("TRANSLATIONS exhaustive_p=3,7")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
