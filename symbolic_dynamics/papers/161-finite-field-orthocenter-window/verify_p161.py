#!/usr/bin/env python3
"""Exact falsifier for P161 finite-field orthocenter-window dynamics.

The script exhausts the anisotropic affine planes for p=3 and p=7.  It checks
the literal transition graph, oriented right-angle depths, reverse-window
fibres, one-step and stable images, and the p=3 empty-core boundary.  Bounded
enumeration is counterexample pressure, not an all-prime proof or a source,
novelty, priority, or release certificate.
"""

from __future__ import annotations

from collections import Counter
from itertools import product


SINK = ("SINK",)
ASSERTIONS = 0


def check(condition: bool, message: object = "assertion failed") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def sub(left: tuple[int, int], right: tuple[int, int], p: int) -> tuple[int, int]:
    return ((left[0] - right[0]) % p, (left[1] - right[1]) % p)


def dot(left: tuple[int, int], right: tuple[int, int], p: int) -> int:
    return (left[0] * right[0] + left[1] * right[1]) % p


def area(left, middle, right, p: int) -> int:
    u = sub(middle, left, p)
    v = sub(right, left, p)
    return (u[0] * v[1] - u[1] * v[0]) % p


def right_coordinate(triangle, p: int) -> int | None:
    left, middle, right = triangle
    tests = (
        dot(sub(middle, left, p), sub(right, left, p), p),
        dot(sub(left, middle, p), sub(right, middle, p), p),
        dot(sub(left, right, p), sub(middle, right, p), p),
    )
    zeros = [index for index, value in enumerate(tests) if value == 0]
    check(len(zeros) <= 1, ("multiple right coordinates", p, triangle, tests))
    return zeros[0] if zeros else None


def orthocenter(left, middle, right, p: int) -> tuple[int, int]:
    """Solve the altitudes through left and middle by exact field arithmetic."""
    side_bc = sub(middle, right, p)
    side_ac = sub(left, right, p)
    rhs_left = dot(left, side_bc, p)
    rhs_middle = dot(middle, side_ac, p)
    determinant = (
        side_bc[0] * side_ac[1] - side_bc[1] * side_ac[0]
    ) % p
    check(determinant != 0, ("singular altitude system", p, left, middle, right))
    inverse = pow(determinant, -1, p)
    height = (
        (rhs_left * side_ac[1] - side_bc[1] * rhs_middle) * inverse % p,
        (side_bc[0] * rhs_middle - rhs_left * side_ac[0]) * inverse % p,
    )
    check(dot(sub(height, left, p), side_bc, p) == 0,
          ("first altitude", p, left, middle, right, height))
    check(dot(sub(height, middle, p), side_ac, p) == 0,
          ("second altitude", p, left, middle, right, height))
    return height


def verify_prime(p: int) -> str:
    check(p % 4 == 3, ("wrong prime class", p))
    points = tuple(product(range(p), repeat=2))

    # Anisotropy is the boundary that prevents isotropic right-angle failures.
    for vector in points:
        check((dot(vector, vector, p) == 0) == (vector == (0, 0)),
              ("anisotropy", p, vector))

    triangles = tuple(
        (left, middle, right)
        for left in points
        for middle in points
        for right in points
        if area(left, middle, right, p) != 0
    )
    states = triangles + (SINK,)
    total = p * p * (p * p - 1) * (p * p - p)
    right_each = p * p * (p * p - 1) * (p - 1)
    nonright = p * p * (p * p - 1) * (p - 1) * (p - 3)
    check(len(triangles) == total, ("triangle count", p))
    check(nonright == total - 3 * right_each, ("count decomposition", p))
    check(nonright % 4 == 0, ("four-cycle divisibility", p))

    heights = {}
    successors = {SINK: SINK}
    indegrees = Counter({SINK: 1})
    kinds = Counter()
    for triangle in triangles:
        kind = right_coordinate(triangle, p)
        kinds[kind] += 1
        left, middle, right = triangle
        height = orthocenter(left, middle, right, p)
        heights[triangle] = height
        check((height == left) == (kind == 0), ("height=first", p, triangle))
        check((height == middle) == (kind == 1), ("height=second", p, triangle))
        check((height == right) == (kind == 2), ("height=third", p, triangle))
        target = (middle, right, height)
        if area(*target, p) == 0:
            target = SINK
        successors[triangle] = target
        indegrees[target] += 1

    check(kinds[0] == right_each, ("right-first count", p, kinds))
    check(kinds[1] == right_each, ("right-second count", p, kinds))
    check(kinds[2] == right_each, ("right-third count", p, kinds))
    check(kinds[None] == nonright, ("nonright count", p, kinds))
    check(indegrees[SINK] == 1 + 2 * right_each, ("sink fibre", p))

    cycles = set()
    depth_hist = Counter({0: 1})
    for triangle in triangles:
        kind = right_coordinate(triangle, p)
        target = successors[triangle]

        if kind is None:
            orbit = [triangle]
            for _ in range(4):
                orbit.append(successors[orbit[-1]])
            check(SINK not in orbit, ("nonright hit sink", p, triangle))
            check(orbit[4] == triangle, ("fourth iterate", p, triangle))
            check(len(set(orbit[:4])) == 4, ("short nonright period", p, triangle))
            cycles.add(frozenset(orbit[:4]))
            expected_depth = 0
        elif kind == 0:
            check(target != SINK, ("right-first premature sink", p, triangle))
            check(right_coordinate(target, p) == 2,
                  ("right-first rotation", p, triangle, target))
            check(successors[target] == SINK, ("right-first depth", p, triangle))
            expected_depth = 2
        else:
            check(target == SINK, ("right-second/third depth", p, triangle))
            expected_depth = 1
        depth_hist[expected_depth] += 1

        expected_fibre = 0 if kind in (0, 1) else 1
        check(indegrees.get(triangle, 0) == expected_fibre,
              ("target fibre", p, triangle, kind))

        left, middle, right = triangle
        reverse = (heights[triangle], left, middle)
        reverse_valid = area(*reverse, p) != 0
        check(reverse_valid == (kind not in (0, 1)),
              ("reverse validity", p, triangle, kind, reverse))
        if reverse_valid:
            check(successors[reverse] == triangle,
                  ("reverse candidate", p, triangle, reverse))

    check(len(cycles) == nonright // 4, ("cycle count", p, len(cycles)))
    check(depth_hist[0] == 1 + nonright, ("depth zero", p, depth_hist))
    check(depth_hist[1] == 2 * right_each, ("depth one", p, depth_hist))
    check(depth_hist[2] == right_each, ("depth two", p, depth_hist))
    check(max(depth_hist) == 2, ("sharp height", p, depth_hist))

    image_one = set(successors.values())
    image_two = {successors[target] for target in image_one}
    image_three = {successors[target] for target in image_two}
    check(len(image_one) == 1 + total - 2 * right_each, ("image one", p))
    check(len(image_two) == 1 + nonright, ("image two", p))
    check(image_three == image_two, ("stable image", p))
    check(sum(indegrees.values()) == len(states), ("fibre mass", p))
    check(sum(state == successors[state] for state in states) == 1,
          ("fixed set", p))

    if p == 3:
        check(nonright == 0, "p=3 core must be empty")
        check(image_two == {SINK}, "p=3 stable image must be sink")
        check(depth_hist[2] > 0, "p=3 height-two shell must survive")

    return (
        f"p={p}:states={len(states)},T={total},R={right_each},Q={nonright},"
        f"cycles4={nonright // 4},image1={len(image_one)},"
        f"stable_image={len(image_two)},sink_fibre={indegrees[SINK]},"
        f"depths=0:{depth_hist[0]},1:{depth_hist[1]},2:{depth_hist[2]}"
    )


def main() -> None:
    signatures = [verify_prime(p) for p in (3, 7)]
    print("P161_ORT_EXACT_V1")
    for signature in signatures:
        print("ORT", signature)
    print("BOUNDARY p=3_empty_periodic_triangle_core_height_two")
    print("INVERSE unique_reverse_window_and_sink_fibre")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
