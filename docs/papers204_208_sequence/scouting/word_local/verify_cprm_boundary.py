#!/usr/bin/env python3
"""Standalone author pressure of CPRM's closed NO_PROMOTION deductions."""
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import json
from math import gcd

ASSERTIONS = 0


def check(condition, detail):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(detail)


def step(x):
    return tuple(1 + (a - 1) % x[(i + 1) % len(x)] for i, a in enumerate(x))


def quotients(x):
    return tuple((a - 1) // x[(i + 1) % len(x)] for i, a in enumerate(x))


def reconstruct(b, q):
    n = len(b)
    if 0 not in q:
        return None
    cut = q.index(0)
    x = [0] * n
    x[cut] = b[cut]
    for j in range(1, n):
        i = (cut - j) % n
        x[i] = b[i] + q[i] * x[(i + 1) % n]
    return tuple(x)


def return_polynomial(m):
    polys = [[0] * (m + 1), [1] + [0] * m]
    for a in range(2, m + 1):
        p = [0] * (m + 1)
        for b in range(1, a):
            if (a - 1) % b == 0:
                for k in range(m):
                    p[k + 1] += polys[b][k]
        polys.append(p)
    d = [1] + [0] * m
    for a in range(1, m + 1):
        for k in range(m):
            d[k + 1] -= polys[a][k]
    return d


def trace_coefficient(d, n):
    coeff = [0]
    for k in range(1, n + 1):
        dn = d[k] if k < len(d) else 0
        coeff.append(-k * dn - sum(d[j] * coeff[k-j]
                                  for j in range(1, min(k, len(d)-1) + 1)))
    return coeff[n]


def main():
    boxes, digest = [], sha256()
    for n in range(2, 7):
        for m in range(1, 7):
            states = list(product(range(1, m + 1), repeat=n))
            actual, fibre_q = defaultdict(set), defaultdict(set)
            heights = Counter()
            for x in states:
                y, q = step(x), quotients(x)
                check(0 in q and reconstruct(y, q) == x, ("source reconstruction", x))
                u = reconstruct((1,) * n, q)
                check(step(u) == (1,) * n and max(u) <= m, ("injected source", x, u))
                check(all(a <= b for a, b in zip(u, x)), ("coordinate domination", x, u))
                check(gcd(*x) == gcd(*y), ("gcd invariant", x, y))
                actual[y].add(x)
                fibre_q[y].add(q)
                row, h, g = x, 0, gcd(*x)
                bound = sum((a // g).bit_length() - 1 for a in x)
                while step(row) != row:
                    nxt = step(row)
                    check(all(b == a or 2*b <= a for a, b in zip(row, nxt)),
                          ("all strict changes halve", row, nxt))
                    row, h = nxt, h + 1
                    check(h <= bound, ("potential time bound", x, h))
                check(row == (g,) * n, ("exact endpoint", x, row))
                heights[h] += 1
                digest.update(json.dumps([x, y, q, h], separators=(",", ":")).encode() + b"\n")
            largest = len(actual[(1,) * n])
            for b in states:
                check(len(actual[b]) == len(fibre_q[b]), ("unique quotient code", n, m, b))
                check(fibre_q[b] <= fibre_q[(1,) * n], ("entire fibre injection", n, m, b))
                check((len(actual[b]) == largest) == (b == (1,) * n),
                      ("unique all-target maximizer", n, m, b))
            if n <= 4 and m <= 4:
                qwords = [q for q in product(range(m), repeat=n) if 0 in q]
                for b in states:
                    decoded = set()
                    for q in qwords:
                        x = reconstruct(b, q)
                        if max(x) <= m and all(b[i] <= x[(i+1) % n] for i in range(n)):
                            decoded.add(x)
                    check(decoded == actual[b], ("all target source sets", n, m, b))
            d = return_polynomial(m)
            check(trace_coefficient(d, n) == largest, ("evaluated return polynomial", n, m))
            boxes.append({"n": n, "m": m, "states": len(states),
                          "height_histogram": dict(sorted(heights.items())),
                          "image": sum(bool(actual[b]) for b in states),
                          "unique_maximum_target": [1] * n, "maximum_fibre": largest,
                          "divisor_return_denominator": d,
                          "full_inverse_sets_checked": n <= 4 and m <= 4})
    print(json.dumps({"status": "PASS", "disposition": "AUTHOR_NO_PROMOTION_NOT_A_GATE",
                      "assertions": ASSERTIONS, "boxes": boxes,
                      "ordered_record_sha256": digest.hexdigest(),
                      "runtime_repository_imports_or_data_reads": False}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
