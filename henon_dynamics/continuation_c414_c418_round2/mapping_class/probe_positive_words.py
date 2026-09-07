#!/usr/bin/env python3
"""Bounded falsification probes, not a census or a proof."""
from itertools import product
import json


def step(p, letter):
    x, y, z = p
    return (x, z, x*z-y) if letter == 'A' else (z, y, y*z-x)


def invariant(p):
    x, y, z = p
    return x*x+y*y+z*z-x*y*z


def cover(p):
    if sum(abs(x) <= 1 for x in p) >= 2:
        return True
    for i, c in enumerate(p[:2]):
        if abs(c) == 1:
            u, v = (p[j] for j in range(3) if j != i)
            if abs(u-c*v) <= 1:
                return True
    return False


def tetrahedron(p):
    return all(abs(x) == 2 for x in p) and p[0]*p[1]*p[2] > 0


def escape_cone(p):
    a, b, c = map(abs, p)
    return a >= 2 and b >= 2 and c >= max(a, b) and c > 2 and p[0]*p[1]*p[2] > 0


def run():
    words = [''.join(w) for n in range(2, 8) for w in product('AB', repeat=n)
             if 'A' in w and 'B' in w]
    words += ['BBBBBBAAAAAA', 'BBBAAAA', 'BBAAAAAA', 'BBBBBBAAAA',
              'BBBBBBBBBBBBAAAAAAAAAAAA']
    tested = periodic = 0
    period_histogram = {}
    counterexamples = []
    for p in product(range(-4, 5), repeat=3):
        for word in words:
            tested += 1
            q = p
            for n in range(1, 97):
                escaped = False
                for letter in word:
                    q = step(q, letter)
                    if escape_cone(q):
                        escaped = True
                        break
                if escaped:
                    break
                if q == p:
                    periodic += 1
                    period_histogram[n] = period_histogram.get(n, 0) + 1
                    if not (cover(p) or tetrahedron(p)):
                        counterexamples.append({'point': p, 'word': word, 'period': n})
                    break
                if max(map(abs, q)) > 100000:
                    break
    fixed_line = []
    for m in range(-5, 9):
        p = (1, 1, m)
        q = p
        for letter in 'BBBBBBAAAAAA':
            q = step(q, letter)
        fixed_line.append({'m': m, 'fixed': q == p, 'K': invariant(p)})
    # Exact arithmetic exhaustively checks elementary one-step inequalities
    # on a small box; this is falsification only.
    cone_failures = []
    small_exit_failures = []
    for p in product(range(-8, 9), repeat=3):
        for letter in 'AB':
            q = step(p, letter)
            if invariant(q) != invariant(p):
                raise AssertionError((p, letter, q))
            if escape_cone(p) and not escape_cone(q):
                cone_failures.append((p, letter, q))
            if min(map(abs, p)) <= 1 and min(map(abs, q)) >= 2:
                if not escape_cone(q):
                    small_exit_failures.append((p, letter, q))
    print(json.dumps({'clock': 'letters listed in chronological application order',
                      'words': len(words), 'tested_point_word_pairs': tested,
                      'periodic_pairs_detected': periodic,
                      'period_histogram': period_histogram,
                      'cover_counterexamples': counterexamples,
                      'cone_failures': cone_failures,
                      'small_exit_failures': small_exit_failures,
                      'fixed_line_probe': fixed_line}, indent=2))


if __name__ == '__main__':
    run()
