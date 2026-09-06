#!/usr/bin/env python3
"""Finite local-order and visibility feedback probes; small full boxes."""
from itertools import product
import json
from pilot import profile


def neighbour_rank(w, reverse=False):
    n = len(w)
    if reverse:
        return tuple(int(w[(i-1) % n] > a) + int(w[(i+1) % n] > a)
                     for i, a in enumerate(w))
    return tuple(int(w[(i-1) % n] < a) + int(w[(i+1) % n] < a)
                 for i, a in enumerate(w))


def extrema(w):
    n = len(w)
    return tuple(2 if a < min(w[(i-1) % n], w[(i+1) % n]) else
                 0 if a > max(w[(i-1) % n], w[(i+1) % n]) else 1
                 for i, a in enumerate(w))


def visibility(w, natural=False):
    n = len(w)
    degrees = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if natural:
                visible = all((j-i)*w[k] < (j-k)*w[i] + (k-i)*w[j]
                              for k in range(i+1, j))
            else:
                visible = all(w[k] < min(w[i], w[j]) for k in range(i+1, j))
            if visible:
                degrees[i] += 1
                degrees[j] += 1
    return tuple(degrees)


def bidirectional_records(w):
    result = []
    for i, a in enumerate(w):
        count = 0
        for tail in (w[i+1:], tuple(reversed(w[:i]))):
            maximum = a
            for b in tail:
                if b > maximum:
                    maximum = b
                    count += 1
        result.append(count)
    return tuple(result)


def main():
    for name, step in [('LNR', neighbour_rank),
                       ('UGR', lambda w: neighbour_rank(w, True)),
                       ('ETR', extrema)]:
        for n in range(3, 11):
            print(json.dumps(dict(candidate=name, n=n,
                                  **profile(product(range(3), repeat=n), step)),
                             sort_keys=True), flush=True)
    for name, step in [('HVD', visibility),
                       ('NVD', lambda w: visibility(w, True)),
                       ('BRD', bidirectional_records)]:
        for n in range(1, 7):
            print(json.dumps(dict(candidate=name, n=n,
                                  **profile(product(range(n), repeat=n), step)),
                             sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
