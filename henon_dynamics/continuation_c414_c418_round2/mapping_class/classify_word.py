#!/usr/bin/env python3
"""Exact <=40-state ordinary integer-period classifier for positive A/B words.

The mathematical global-completeness argument is in PROOF_PACKAGE.md.  Letters
in CLI strings are applied chronologically, so AB means B composed with A.
No search radius or trial-period cutoff is used by the classifier.
"""
import argparse
import json
from itertools import product
from math import isqrt
from line_automaton import lines, quadratic


def invariant(p):
    x, y, z = p
    return x*x+y*y+z*z-x*y*z


def step(p, letter):
    x, y, z = p
    return (x, z, x*z-y) if letter == 'A' else (z, y, y*z-x)


def in_cover(p):
    x, y, z = p
    return (sum(abs(a) <= 1 for a in p) >= 2
            or (abs(x) == 1 and abs(y-x*z) <= 1)
            or (abs(y) == 1 and abs(x-y*z) <= 1))


def candidates(k):
    answer = set()
    for v, w in lines()[:39]:
        a, b, c = quadratic((v, w))
        assert a == 1
        disc = b*b-4*(c-k)
        if disc < 0:
            continue
        d = isqrt(disc)
        if d*d != disc:
            continue
        for numerator in (-b+d, -b-d):
            if numerator % 2 == 0:
                t = numerator//2
                answer.add(tuple(v[i]*t+w[i] for i in range(3)))
    if k == 4:
        answer |= {(2*a, 2*b, 2*a*b) for a, b in product((-1, 1), repeat=2)}
    assert len(answer) <= 40
    assert all(invariant(p) == k for p in answer)
    return sorted(answer)


def classify(k, word):
    if not word or set(word) != {'A', 'B'}:
        raise ValueError('word must use A and B, with no other letters')
    points = candidates(k)
    pool = set(points)
    action = {}
    for p in points:
        q = p
        for letter in word:
            q = step(q, letter)
            if q not in pool:
                q = None
                break
        action[p] = q
    cycles, used = [], set()
    for start in points:
        if start in used:
            continue
        path, q = [], start
        while q is not None and q not in path and q not in used:
            path.append(q)
            q = action[q]
        if q == start:
            cycles.append(path)
        elif q is not None and q in path:
            raise AssertionError('partial injective map cannot have a tail into a cycle')
        used.update(path)
    return {'K': k, 'word_chronological': word, 'candidate_count': len(points),
            'periodic_point_count': sum(map(len, cycles)),
            'cycles': cycles, 'periods': sorted({len(c) for c in cycles}),
            'cycle_count_by_period': {str(n): sum(len(c) == n for c in cycles)
                                     for n in sorted({len(c) for c in cycles})}}


def self_test():
    expected = {0: 1, 1: 6, 2: 16, 3: 0, 4: 26, 5: 32, 8: 40, 9: 6, 14: 40}
    for k, count in expected.items():
        assert len(candidates(k)) == count, (k, count, len(candidates(k)))
    # Independent direct membership comparison in a small box is diagnostic.
    box = range(-8, 9)
    grouped = {}
    for p in product(box, repeat=3):
        if in_cover(p) or (all(abs(a) == 2 for a in p) and p[0]*p[1]*p[2] > 0):
            grouped.setdefault(invariant(p), set()).add(p)
    for k, observed in grouped.items():
        calculated = {p for p in candidates(k) if max(map(abs, p)) <= 8}
        assert observed == calculated, (k, observed ^ calculated)
    for k in range(-20, 101):
        for word in ('AB', 'ABB', 'AABB', 'AAABBB', 'AAAAAABBBBBB', 'AABABABBBA'):
            result = classify(k, word)
            for cycle in result['cycles']:
                for i, p in enumerate(cycle):
                    q = p
                    for letter in word:
                        q = step(q, letter)
                    assert q == cycle[(i+1) % len(cycle)]
    return {'self_test': 'PASS', 'low_level_candidate_counts': expected,
            'sample_new_level': classify(101, 'ABB'),
            'sample_fixed_line_level': classify(14, 'BBBBBBAAAAAA')}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--K', type=int)
    parser.add_argument('--word')
    args = parser.parse_args()
    if args.K is None and args.word is None:
        result = self_test()
    elif args.K is not None and args.word is not None:
        result = classify(args.K, args.word)
    else:
        parser.error('--K and --word are required together')
    print(json.dumps(result, indent=2))
