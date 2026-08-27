#!/usr/bin/env python3
"""Exact incidence controls for horizontal-strip codings of a skew shift.

Coordinates are stored as rational pairs r+s*alpha.  Irrationality of alpha
makes equality modulo one an exact coefficient comparison, so the program
does not approximate the torus geometry numerically.
"""

from collections import defaultdict, deque
from fractions import Fraction


def choose2(value):
    return value * (value - 1) // 2


def frac(value):
    return value - value.numerator // value.denominator


def vertex_key(i, a, j, b, branch, q):
    assert i < j
    delta = j - i
    ci, cj = choose2(i), choose2(j)
    x_rat = (Fraction(b - a, q) + branch) / delta
    x_alpha = Fraction(-(cj - ci), delta)
    y_rat = Fraction(a, q) - i * x_rat
    y_alpha = -i * x_alpha - ci
    return (frac(x_rat), x_alpha, frac(y_rat), y_alpha)


def lies_on(key, time, level, q):
    x_rat, x_alpha, y_rat, y_alpha = key
    value_rat = y_rat + time * x_rat - Fraction(level, q)
    value_alpha = y_alpha + time * x_alpha + choose2(time)
    return value_alpha == 0 and value_rat.denominator == 1


def enumerate_arrangement(q, horizon):
    vertices = {}
    for i in range(horizon):
        for j in range(i + 1, horizon):
            for a in range(q):
                for b in range(q):
                    for branch in range(j - i):
                        key = vertex_key(i, a, j, b, branch, q)
                        vertices.setdefault(key, set()).update(((i, a), (j, b)))

    curves = [(time, level) for time in range(horizon) for level in range(q)]
    incidence = defaultdict(set)
    for key in vertices:
        exact_curves = {curve for curve in curves if lies_on(key, *curve, q)}
        assert len(exact_curves) == 2, (key, exact_curves)
        for curve in exact_curves:
            incidence[curve].add(key)

    if horizon >= 2:
        assert all(incidence[curve] for curve in curves)
        start = curves[0]
        seen_curves = {start}
        seen_vertices = set()
        queue = deque([("curve", start)])
        while queue:
            kind, item = queue.popleft()
            if kind == "curve":
                for key in incidence[item]:
                    if key not in seen_vertices:
                        seen_vertices.add(key)
                        queue.append(("vertex", key))
            else:
                for curve in curves:
                    if curve not in seen_curves and item in incidence[curve]:
                        seen_curves.add(curve)
                        queue.append(("curve", curve))
        assert len(seen_curves) == len(curves)
        assert len(seen_vertices) == len(vertices)

    return len(vertices), sum(len(points) for points in incidence.values())


def main():
    checks = 0
    rows = []
    for q in range(2, 7):
        for horizon in range(2, 9):
            vertices, edges = enumerate_arrangement(q, horizon)
            expected = q * q * (horizon + 1) * horizon * (horizon - 1) // 6
            assert vertices == expected
            assert edges == 2 * vertices
            faces = edges - vertices  # Euler characteristic of the torus is zero.
            assert faces == expected
            rows.append((q, horizon, vertices, edges, faces))
            checks += 1
    print(f"PASS exact irrational-coefficient arrangement checks: {checks}")
    print("sample rows (q,n,V,E,F):")
    for row in rows[:8]:
        print(row)


if __name__ == "__main__":
    main()
