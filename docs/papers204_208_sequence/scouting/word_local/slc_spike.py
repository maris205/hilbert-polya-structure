#!/usr/bin/env python3
"""Counterexample pressure on SLC; no enumeration is called a proof."""
from collections import Counter
from itertools import product
import json
import random


def step(w):
    return tuple(max(1, sum(w[j] >= a > w[j-1] for j in range(len(w))))
                 for a in w)


def orbit(w):
    path = []
    seen = {}
    while w not in seen:
        seen[w] = len(path)
        path.append(w)
        w = step(w)
        if len(path) > 5000:
            return None, path
    h = seen[w]
    return h, path


def main():
    initial = (1,2,1,2,1,3,1,3)
    h, path = orbit(initial)
    assert len(path) - h == 2
    rows = [{'type': 'fixed_only_counterexample', 'source': initial,
             'height': h, 'path': path, 'period': len(path)-h}]
    randomizer = random.Random(204206)
    for n in (8, 12, 20, 40):
        periods = Counter()
        maxheight = 0
        witness = None
        for _ in range(1500):
            w = tuple(randomizer.randint(1, min(n, 8)) for _ in range(n))
            h, path = orbit(w)
            if h is None:
                rows.append({'n': n, 'timeout_source': w, 'cutoff': len(path)})
                break
            p = len(path)-h
            periods[p] += 1
            maxheight = max(maxheight, h)
            if p > 2 and witness is None:
                witness = {'source': w, 'height': h, 'period': p, 'cycle': path[h:]}
        rows.append({'n': n, 'samples': sum(periods.values()),
                     'periods': dict(sorted(periods.items())),
                     'max_height_observed': maxheight, 'long_period_witness': witness})
    print(json.dumps(rows, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
