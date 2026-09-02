#!/usr/bin/env python3
"""Independent hostile verifier for P161 Review A.

This implementation deliberately does not import the paper-local verifier and
does not use its 2-by-2 orthocenter formula.  For every carrier triangle over
F_3^2 and F_7^2 it finds the orthocenter by scanning the affine plane against
the two altitude predicates, then constructs the literal totalized functional
graph and reads its fibres, images, depths, and cycles directly.

The p=5 lane is a negative scope control: it confirms that the displayed
right-angle count is not silently valid when the standard dot product is
isotropic.  Finite enumeration is falsification pressure, not an all-prime
proof and not an ownership or novelty certificate.
"""

from __future__ import annotations

from collections import Counter
from itertools import product


SINK = ("SINK",)
ASSERTIONS = 0


def require(condition: bool, label: object) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def minus(a: tuple[int, int], b: tuple[int, int], p: int) -> tuple[int, int]:
    return ((a[0] - b[0]) % p, (a[1] - b[1]) % p)


def scalar(a: tuple[int, int], b: tuple[int, int], p: int) -> int:
    return (a[0] * b[0] + a[1] * b[1]) % p


def wedge(a: tuple[int, int], b: tuple[int, int], p: int) -> int:
    return (a[0] * b[1] - a[1] * b[0]) % p


def is_triangle(state, p: int) -> bool:
    a, b, c = state
    return wedge(minus(b, a, p), minus(c, a, p), p) != 0


def right_slot(state, p: int) -> int | None:
    a, b, c = state
    tests = (
        scalar(minus(b, a, p), minus(c, a, p), p),
        scalar(minus(a, b, p), minus(c, b, p), p),
        scalar(minus(a, c, p), minus(b, c, p), p),
    )
    slots = tuple(i for i, value in enumerate(tests) if value == 0)
    require(len(slots) <= 1, ("two right slots", p, state, tests))
    return slots[0] if slots else None


def orthocenter_by_predicate(state, points, p: int) -> tuple[int, int]:
    """Find H by exhaustive satisfaction of the two altitude equations."""
    a, b, c = state
    solutions = tuple(
        h
        for h in points
        if scalar(minus(h, a, p), minus(b, c, p), p) == 0
        and scalar(minus(h, b, p), minus(a, c, p), p) == 0
    )
    require(len(solutions) == 1, ("orthocenter uniqueness", p, state, solutions))
    return solutions[0]


def iterate(successor, state, steps: int):
    for _ in range(steps):
        state = successor[state]
    return state


def verify_anisotropic_prime(p: int) -> str:
    require(p in (3, 7), ("review lane", p))
    points = tuple(product(range(p), repeat=2))
    for vector in points:
        require(
            (scalar(vector, vector, p) == 0) == (vector == (0, 0)),
            ("anisotropy", p, vector),
        )

    triangles = tuple(
        state
        for state in product(points, repeat=3)
        if is_triangle(state, p)
    )
    states = triangles + (SINK,)
    expected_t = p**2 * (p**2 - 1) * (p**2 - p)
    expected_r = p**2 * (p**2 - 1) * (p - 1)
    expected_q = p**2 * (p**2 - 1) * (p - 1) * (p - 3)
    require(len(triangles) == expected_t, ("T", p, len(triangles), expected_t))
    require(expected_t - 3 * expected_r == expected_q, ("Q algebra", p))

    heights = {}
    kinds = Counter()
    for state in triangles:
        height = orthocenter_by_predicate(state, points, p)
        heights[state] = height
        kind = right_slot(state, p)
        kinds[kind] += 1
        a, b, c = state
        require(
            scalar(minus(height, c, p), minus(a, b, p), p) == 0,
            ("third altitude", p, state, height),
        )
        require((height == a) == (kind == 0), ("H=A", p, state, height, kind))
        require((height == b) == (kind == 1), ("H=B", p, state, height, kind))
        require((height == c) == (kind == 2), ("H=C", p, state, height, kind))

    require(kinds[0] == expected_r, ("R0", p, kinds))
    require(kinds[1] == expected_r, ("R1", p, kinds))
    require(kinds[2] == expected_r, ("R2", p, kinds))
    require(kinds[None] == expected_q, ("Q", p, kinds))

    successor = {SINK: SINK}
    indegree = Counter({SINK: 1})
    for state in triangles:
        _, b, c = state
        proposed = (b, c, heights[state])
        target = proposed if is_triangle(proposed, p) else SINK
        successor[state] = target
        indegree[target] += 1

    cycles = set()
    depth_counts = Counter({0: 1})
    for state in triangles:
        a, b, c = state
        h = heights[state]
        kind = right_slot(state, p)
        reverse = (h, a, b)
        reverse_is_valid = is_triangle(reverse, p)

        require(
            reverse_is_valid == (kind not in (0, 1)),
            ("reverse validity", p, state, kind, reverse),
        )
        if reverse_is_valid:
            require(successor[reverse] == state, ("reverse edge", p, state, reverse))
            require(indegree[state] == 1, ("unit fibre", p, state, kind))
        else:
            require(indegree.get(state, 0) == 0, ("zero fibre", p, state, kind))

        if kind is None:
            quartet = (
                (a, b, c),
                (b, c, h),
                (c, h, a),
                (h, a, b),
            )
            for window in quartet:
                require(is_triangle(window, p), ("quartet carrier", p, state, window))
            require(len(set(quartet)) == 4, ("quartet distinct", p, state, quartet))
            require(successor[quartet[0]] == quartet[1], ("window 1", p, state))
            require(successor[quartet[1]] == quartet[2], ("window 2", p, state))
            require(successor[quartet[2]] == quartet[3], ("window 3", p, state))
            require(successor[quartet[3]] == quartet[0], ("window 4", p, state))
            cycles.add(frozenset(quartet))
            depth_counts[0] += 1
        elif kind == 0:
            rotated = (b, c, a)
            require(successor[state] == rotated, ("right-0 first edge", p, state))
            require(right_slot(rotated, p) == 2, ("right-0 to right-2", p, state))
            require(successor[rotated] == SINK, ("right-0 second edge", p, state))
            depth_counts[2] += 1
        else:
            require(successor[state] == SINK, ("right-1/2 edge", p, state, kind))
            depth_counts[1] += 1

    require(len(cycles) == expected_q // 4, ("4-cycle census", p, len(cycles)))
    require(indegree[SINK] == 1 + 2 * expected_r, ("sink fibre", p, indegree[SINK]))
    require(sum(indegree.values()) == len(states), ("fibre mass", p))

    expected_image_one = {
        SINK,
        *(state for state in triangles if right_slot(state, p) in (None, 2)),
    }
    expected_stable = {
        SINK,
        *(state for state in triangles if right_slot(state, p) is None),
    }
    image_one = set(successor.values())
    image_two = {successor[state] for state in image_one}
    image_three = {successor[state] for state in image_two}
    require(image_one == expected_image_one, ("one-step image set", p))
    require(image_two == expected_stable, ("two-step image set", p))
    require(image_three == image_two, ("stable image", p))
    require(len(image_one) == 1 + expected_t - 2 * expected_r, ("image1 size", p))
    require(len(image_two) == 1 + expected_q, ("image2 size", p))

    require(depth_counts[0] == 1 + expected_q, ("depth 0", p, depth_counts))
    require(depth_counts[1] == 2 * expected_r, ("depth 1", p, depth_counts))
    require(depth_counts[2] == expected_r, ("depth 2", p, depth_counts))
    require(sum(depth_counts.values()) == len(states), ("depth partition", p))

    # Direct fixed-iterate counts independently pressure the claimed zeta product.
    for time in range(1, 9):
        actual_fixed = sum(iterate(successor, state, time) == state for state in states)
        expected_fixed = 1 + (expected_q if time % 4 == 0 else 0)
        require(actual_fixed == expected_fixed, ("Fix(F^t)", p, time, actual_fixed))

    if p == 3:
        require(expected_t == 432, ("p=3 T", expected_t))
        require(expected_r == 144, ("p=3 R", expected_r))
        require(expected_q == 0, ("p=3 Q", expected_q))
        require(image_two == {SINK}, ("p=3 stable core", image_two))
        require(depth_counts == Counter({1: 288, 2: 144, 0: 1}), ("p=3 depths", depth_counts))
        require(indegree[SINK] == 289, ("p=3 sink fibre", indegree[SINK]))

    return (
        f"p={p}:states={len(states)},T={expected_t},R={expected_r},Q={expected_q},"
        f"cycles4={len(cycles)},image1={len(image_one)},stable={len(image_two)},"
        f"sink_fibre={indegree[SINK]},depths=0:{depth_counts[0]},"
        f"1:{depth_counts[1]},2:{depth_counts[2]}"
    )


def verify_isotropic_scope_control() -> str:
    p = 5
    points = tuple(product(range(p), repeat=2))
    nonzero_null = tuple(
        v for v in points if v != (0, 0) and scalar(v, v, p) == 0
    )
    require(nonzero_null, "p=5 must have nonzero null vectors")
    triangles = tuple(
        state
        for state in product(points, repeat=3)
        if is_triangle(state, p)
    )
    right_first = sum(right_slot(state, p) == 0 for state in triangles)
    anisotropic_formula = p**2 * (p**2 - 1) * (p - 1)
    require(right_first != anisotropic_formula, ("scope leak", right_first, anisotropic_formula))
    return (
        f"p=5:null_vectors={len(nonzero_null)},right_first={right_first},"
        f"anisotropic_formula={anisotropic_formula}"
    )


def main() -> None:
    signatures = tuple(verify_anisotropic_prime(p) for p in (3, 7))
    scope = verify_isotropic_scope_control()
    print("P161_REVIEW_A_INDEPENDENT_V1")
    for signature in signatures:
        print("EXACT", signature)
    print("SCOPE_CONTROL", scope)
    print("FOUR_WINDOWS exact_4_cycle_or_oriented_sink_boundary")
    print("FIBRES every_target_checked_from_literal_indegree")
    print("IMAGES literal_support_and_stabilization_checked")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
