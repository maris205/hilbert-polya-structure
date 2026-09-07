#!/usr/bin/env python3
"""Exact finite audit of the *proved* universal eight-state graph.

This is not a parameter census or a proof of rational-to-polynomial rigidity.
It independently enumerates every simple graph cycle, derives its polynomial
labels, and checks literal Hénon reconstruction for the sharp F_3(t) example.
Only Python's standard library is used. Nothing is written by this script.
"""

from collections import Counter
from fractions import Fraction
from itertools import product


def simple_cycles(vertices, successors):
    """Each directed simple cycle occurs once, starting at its least vertex."""
    answer = []
    for start in vertices:
        def extend(path):
            for nxt in successors(path[-1]):
                if nxt == start:
                    answer.append(tuple(path))
                elif nxt > start and nxt not in path:
                    extend(path + [nxt])
        extend([start])
    return answer


VERTICES = tuple(product((0, 1), repeat=3))


def label(state, bit):
    u, v, w = state
    return bit, 2 * v * w, u  # constant, a, a^2 coefficients


def symbolic_cycles():
    cycles = simple_cycles(VERTICES,
                           lambda v: (v[1:] + (bit,) for bit in (0, 1)))
    rows = []
    for cycle in cycles:
        word = ''.join(str(v[0]) for v in cycle)
        labels = tuple(dict.fromkeys(label(v, cycle[(j + 1) % len(cycle)][2])
                                      for j, v in enumerate(cycle)))
        rows.append((word, labels, sum(v[0] for v in cycle) % 2))
    return rows


def value(poly, a, modulus=None):
    out = poly[0] + poly[1] * a + poly[2] * a * a
    return out if modulus is None else out % modulus


def numerical_cycles(a, lam, modulus=None):
    def successors(v):
        for bit in (0, 1):
            if value(label(v, bit), a, modulus) == lam:
                yield v[1:] + (bit,)
    for v in VERTICES:
        assert len(list(successors(v))) <= 1
        incoming = [u for u in VERTICES if v in list(successors(u))]
        assert len(incoming) <= 1
    return simple_cycles(VERTICES, successors)


def lift_counts(cycles):
    counts = Counter()
    for cycle in cycles:
        odd = sum(v[0] for v in cycle) % 2
        counts[(1 + odd) * len(cycle)] += 1 if odd else 2
    return dict(sorted(counts.items()))


def add(poly, other, p):
    n = max(len(poly), len(other))
    return trim(tuple(((poly[i] if i < len(poly) else 0) +
                       (other[i] if i < len(other) else 0)) % p
                      for i in range(n)))


def scale(poly, factor, p):
    return trim(tuple(c * factor % p for c in poly))


def multiply(poly, other, p):
    result = [0] * (len(poly) + len(other) - 1)
    for i, x in enumerate(poly):
        for j, y in enumerate(other):
            result[i + j] = (result[i + j] + x * y) % p
    return trim(tuple(result))


def trim(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly = poly[:-1]
    return poly


def embed(sign, state, a, p):
    u, v, w = state
    inv2 = pow(2, -1, p)
    x = ((((-1) ** v + a * (-1) ** u) * inv2) % p, sign % p)
    y = ((((-1) ** w + a * (-1) ** v) * inv2) % p,
         (sign * (-1) ** v) % p)
    return x, y


def literal_henon(point, a, constant, p):
    # P=t, c=-t^2+constant. Work in F_p[t], not its values on F_p.
    x, y = point
    c = (constant % p, 0, -1 % p)
    return y, add(add(multiply(y, y, p), c, p), scale(x, -a, p), p)


def sharp_example():
    p, a, constant = 3, 2, 2  # characteristic 3, a=-1, C=-1
    lam = (((a + 1) ** 2) * pow(4, -1, p) - constant) % p
    cycles = numerical_cycles(a, lam, p)
    counts = lift_counts(cycles)
    points = {embed(sign, v, a, p)
              for cyc in cycles for v in cyc for sign in (-1, 1)}
    assert len(points) == 14
    assert counts == {4: 1, 5: 2}
    assert {literal_henon(P, a, constant, p) for P in points} == points
    observed = simple_cycles(sorted(points),
                             lambda P: (literal_henon(P, a, constant, p),))
    assert dict(sorted(Counter(map(len, observed)).items())) == counts
    all_labels = {embed(sign, v, a, p): (sign, v)
                  for v in VERTICES for sign in (-1, 1)}
    assert len(all_labels) == 16
    for point, (sign, state) in all_labels.items():
        image = literal_henon(point, a, constant, p)
        permitted = [bit for bit in (0, 1)
                     if value(label(state, bit), a, p) == lam]
        if permitted:
            expected = embed(sign * (-1) ** state[1],
                             state[1:] + (permitted[0],), a, p)
            assert image == expected
        else:
            assert image not in all_labels
    return counts, sorted(points)


def reconstruction_identity():
    """Compare polynomial coefficients in a over Q for all 16 bit windows."""
    for u, v, w, z in product((0, 1), repeat=4):
        bx = (Fraction((-1) ** v, 2), Fraction((-1) ** u, 2))
        by = (Fraction((-1) ** w, 2), Fraction((-1) ** v, 2))
        bz = (Fraction((-1) ** z, 2), Fraction((-1) ** w, 2))
        # C=K-lambda and K=(a+1)^2/4.
        K = (Fraction(1, 4), Fraction(1, 2), Fraction(1, 4))
        lam = label((u, v, w), z)
        C = tuple(K[i] - lam[i] for i in range(3))
        by2 = (by[0] ** 2, 2 * by[0] * by[1], by[1] ** 2)
        difference = (by2[0] + C[0] - bz[0],
                      by2[1] + C[1] - bx[0] - bz[1],
                      by2[2] + C[2] - bx[1])
        assert difference == (0, 0, 0)
    return 16


def main():
    rows = symbolic_cycles()
    print('ALL_DIRECTED_SIMPLE_CYCLES', len(rows))
    print('word | distinct lambda polynomials (constant,a,a^2) | odd sign lift')
    for row in rows:
        print(*row, sep=' | ')
    print('LITERAL_RECONSTRUCTION_IDENTITIES', reconstruction_identity())
    counts, points = sharp_example()
    print('SHARP_F3_T_ORDINARY_CYCLES', counts)
    print('SHARP_F3_T_DISTINCT_POLYNOMIAL_POINTS', len(points))
    print('SHARP_POINT_LABELS_COEFFICIENTS_LOW_TO_HIGH', points)
    print('FINITE_SYMBOLIC_AND_LITERAL_CHECKS_PASS')


if __name__ == '__main__':
    main()
