#!/usr/bin/env python3
"""Author corroboration of the evaluated distance decoder; no imports/data."""
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import json


def distances(x):
    return tuple(abs(a - x[(i + 1) % len(x)]) for i, a in enumerate(x))


def minimums(d):
    return tuple(min(d[i - 1], a) for i, a in enumerate(d))


def weight(d):
    w = tuple(a for a in d if a)
    a, b = w.count(1), w.count(2)
    if not w:
        return 3
    if not b:
        return 0 if a % 2 else 2 ** (a // 2 + 1)
    if not a:
        return 0 if b % 2 else 2
    j = w.index(2)
    run = 0
    for c in w[j + 1:] + w[:j + 1]:
        if c == 1:
            run += 1
        else:
            if run % 2:
                return 0
            run = 0
    return 2 ** (a // 2)


def reconstruct(d):
    result = set()
    for first in range(3):
        paths = [(first,)]
        for edge in d[:-1]:
            paths = [p + (a,) for p in paths for a in range(3)
                     if abs(p[-1] - a) == edge]
        result.update(p for p in paths if abs(p[-1] - first) == d[-1])
    return result


def main():
    records = []
    assertions = 0
    for n in range(3, 10):
        states = list(product(range(3), repeat=n))
        buckets = defaultdict(set)
        direct = Counter()
        for x in states:
            d = distances(x)
            buckets[d].add(x)
            target = tuple(min(abs(a-x[i-1]), abs(a-x[(i+1)%n]))
                           for i, a in enumerate(x))
            assert target == minimums(d)
            assertions += 1
            direct[target] += 1
        summed = Counter()
        histogram = Counter()
        for d in states:
            expected = buckets.get(d, set())
            decoded = reconstruct(d)
            assert decoded == expected
            assert weight(d) == len(expected)
            assertions += 2
            summed[minimums(d)] += weight(d)
            histogram[weight(d)] += 1
        for y in states:
            assert summed[y] == direct[y]
            assertions += 1
        vector = [summed[y] for y in states]
        records.append({"n": n, "states": len(states),
                        "realizable_distances": len(buckets),
                        "distance_fibre_histogram": dict(sorted(histogram.items())),
                        "target_count_vector_sha256": sha256(json.dumps(
                            vector, separators=(",", ":")).encode()).hexdigest()})
    print(json.dumps({"status": "PASS", "assertions": assertions,
                      "records": records}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
