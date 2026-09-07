#!/usr/bin/env python3
"""Exact symbolic construction of the 45-line partial action.

This file constructs finite data from the displayed line definitions.  It does
not certify the global escape lemma or make a novelty claim.
"""
from itertools import product
import json


def lines():
    answer = []
    for i in range(3):
        for a, b in product((-1, 0, 1), repeat=2):
            v, w = [0]*3, [0]*3
            v[i] = 1
            others = [j for j in range(3) if j != i]
            w[others[0]], w[others[1]] = a, b
            answer.append((tuple(v), tuple(w)))
    for i in range(3):
        for c, b in product((-1, 1), (-1, 0, 1)):
            v, w = [0]*3, [0]*3
            others = [j for j in range(3) if j != i]
            w[i] = c
            v[others[0]], v[others[1]] = 1, c
            w[others[1]] = b
            answer.append((tuple(v), tuple(w)))
    return answer


def polynomial_product(a, b):
    return (a[0]*b[0], a[0]*b[1]+a[1]*b[0], a[1]*b[1])


def image(line, letter):
    v, w = line
    x, y, z = [(w[i], v[i], 0) for i in range(3)]
    u, subtract = (x, y) if letter == 'A' else (y, x)
    poly = tuple(a-b for a, b in zip(polynomial_product(u, z), subtract))
    out = (x, z, poly) if letter == 'A' else (z, y, poly)
    if any(p[2] for p in out):
        return None
    vnew = tuple(p[1] for p in out)
    wnew = tuple(p[0] for p in out)
    first = next(i for i, a in enumerate(vnew) if a)
    a, b = vnew[first], wnew[first]
    if abs(a) != 1:
        return None
    normalized_v = tuple(u*a for u in vnew)
    normalized_w = tuple(wnew[i]-normalized_v[i]*b for i in range(3))
    candidate = (normalized_v, normalized_w)
    return candidate, a, b


def invariant(point):
    x, y, z = point
    return x*x+y*y+z*z-x*y*z


def quadratic(line):
    v, w = line
    vals = [invariant(tuple(v[i]*t+w[i] for i in range(3))) for t in (0, 1, -1)]
    return (vals[1]+vals[2]-2*vals[0])//2, (vals[1]-vals[2])//2, vals[0]


def graph():
    all_lines = lines()
    index = {line: i for i, line in enumerate(all_lines)}
    edges = {}
    for letter in 'AB':
        edges[letter] = []
        for line in all_lines:
            result = image(line, letter)
            edges[letter].append(None if result is None or result[0] not in index
                                 else (index[result[0]], result[1], result[2]))
    return all_lines, edges


def word_cycles(word, edges):
    action = []
    for start in range(45):
        current, a, b = start, 1, 0
        for letter in word:
            edge = edges[letter][current]
            if edge is None:
                current = None
                break
            current, c, d = edge
            a, b = c*a, c*b+d
        action.append(None if current is None else (current, a, b))
    cycles, used = [], set()
    for start in range(45):
        if start in used:
            continue
        path, current, a, b = [], start, 1, 0
        while current is not None and current not in path and current not in used:
            path.append(current)
            edge = action[current]
            if edge is None:
                current = None
                break
            current, c, d = edge
            a, b = c*a, c*b+d
        if current == start:
            cycles.append({'lines': path, 'return_a': a, 'return_b': b,
                           'generic_period': len(path)*(2 if a == -1 else 1)})
        used.update(path)
    return cycles


def main():
    all_lines, edges = graph()
    assert len(set(all_lines)) == 45
    words = ['AB', 'ABB', 'AABB', 'AAABBB', 'AAAAAABBBBBB', 'AAAAAAABBBBBBB']
    hist = {}
    for n in range(2, 13):
        for letters in product('AB', repeat=n):
            if len(set(letters)) != 2:
                continue
            for cycle in word_cycles(''.join(letters), edges):
                d = cycle['generic_period']
                hist[d] = hist.get(d, 0)+1
    print(json.dumps({'lines': [{'id': i, 'v': v, 'w': w, 'K_coefficients': quadratic((v, w))}
                               for i, (v, w) in enumerate(all_lines)],
                      'edges': edges, 'generic_period_histogram_words_le_12': hist,
                      'sample_word_cycles': {word: word_cycles(word, edges) for word in words}}, indent=2))


if __name__ == '__main__':
    main()
