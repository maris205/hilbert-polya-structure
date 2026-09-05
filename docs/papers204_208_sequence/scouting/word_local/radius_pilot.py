#!/usr/bin/env python3
"""Literal palindrome-radius feedback pilots; finite evidence only.

The generic graph census is reused from this lane's pilot.py, not from a
manuscript or independent verifier. This is author exploratory code.
"""
from itertools import product
import json
from pilot import profile


def odd_radius(w):
    out = []
    for i in range(len(w)):
        r = 0
        while i-r-1 >= 0 and i+r+1 < len(w) and w[i-r-1] == w[i+r+1]:
            r += 1
        out.append(r)
    return tuple(out)


def even_radius(w):
    out = []
    for i in range(len(w)):
        r = 0
        while i-r-1 >= 0 and i+r < len(w) and w[i-r-1] == w[i+r]:
            r += 1
        out.append(r)
    return tuple(out)


def circular_radius(w):
    n, out = len(w), []
    for i in range(n):
        r = 0
        while r < (n-1)//2 and w[(i-r-1) % n] == w[(i+r+1) % n]:
            r += 1
        out.append(r)
    return tuple(out)


def main():
    for name, step, cap, max_n in [
        ('OPR', odd_radius, lambda i, n: min(i, n-1-i), 10),
        ('EPR', even_radius, lambda i, n: min(i, n-i), 9),
        ('CPR', circular_radius, lambda i, n: (n-1)//2, 8),
    ]:
        for n in range(1, max_n+1):
            states = product(*(range(cap(i, n)+1) for i in range(n)))
            print(json.dumps(dict(candidate=name, n=n, **profile(states, step)),
                             sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
