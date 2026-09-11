#!/usr/bin/env python3
"""Six literal circular statistic recomputations; bounded author scout only."""
from itertools import product
import json
from pilot import profile


def next_equal(w):
    n = len(w)
    return tuple(next(d for d in range(1, n + 1) if w[(i + d) % n] == w[i])
                 for i in range(n))


def nearest_equal(w):
    n = len(w)
    return tuple(next((d for d in range(1, n) if
                       w[(i + d) % n] == w[i] or w[(i - d) % n] == w[i]), n)
                 for i in range(n))


def class_size(w):
    return tuple(w.count(v) for v in w)


def distinct_window(w):
    n = len(w)
    out = []
    for i in range(n):
        seen = set()
        for d in range(n):
            v = w[(i + d) % n]
            if v in seen:
                break
            seen.add(v)
        out.append(len(seen))
    return tuple(out)


def unequal_window(w):
    n = len(w)
    return tuple(next((d for d in range(1, n) if
                       w[(i + d - 1) % n] == w[(i + d) % n]), n)
                 for i in range(n))


def record_count(w):
    n = len(w)
    out = []
    for i in range(n):
        high, count = 0, 0
        for d in range(n):
            v = w[(i + d) % n]
            if v > high:
                high = v
                count += 1
        out.append(count)
    return tuple(out)


def main():
    for name, step in (("CNE", next_equal), ("CNM", nearest_equal),
                       ("CCS", class_size), ("CDW", distinct_window),
                       ("CUW", unequal_window), ("CRC", record_count)):
        for n in range(1, 7):
            states = product(range(1, n + 1), repeat=n)
            print(json.dumps(dict(candidate=name, n=n,
                                  **profile(states, step)), sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
