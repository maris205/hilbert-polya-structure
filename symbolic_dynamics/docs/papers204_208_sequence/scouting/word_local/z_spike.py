#!/usr/bin/env python3
"""Targeted recurrence/mask pressure; imports the literal scout Z update."""
from itertools import product
from random import Random
import json
from pilot import z_array


def orbit(w):
    seen, path = {}, []
    while w not in seen:
        seen[w] = len(path)
        path.append(w)
        w = z_array(w)
    return seen[w], len(path)-seen[w], path


def main():
    for n in range(2, 15):
        height, witness = -1, None
        for bits in product(range(2), repeat=n-1):
            w = (0,)+bits
            h, p, path = orbit(w)
            assert p == 2
            if h > height:
                height, witness = h, w
        print(json.dumps(dict(test='binary_sources', n=n, height=height,
                              witness=witness), sort_keys=True))
    rng = Random(204)
    for n in (16, 32, 64, 128, 256):
        height, witness = -1, None
        endpoints = {}
        for trial in range(2000):
            mask = tuple(rng.randrange(2) for _ in range(n-1))
            w = (0,)+tuple(rng.randrange(1, n-i+1) if mask[i-1] else 0
                          for i in range(1, n))
            h, p, path = orbit(w)
            assert p == 2
            b = (0,)+mask
            bh, bp, bpath = orbit(b)
            assert bp == 2
            aend = path[h + h % 2]
            bend = bpath[bh + bh % 2]
            assert aend == bend, (w, aend, bend)
            if h > height:
                height, witness = h, w
        print(json.dumps(dict(test='random_sources_same_mask', n=n,
                              trials=2000, seed=204, height=height,
                              witness=witness), sort_keys=True))


if __name__ == '__main__':
    main()
