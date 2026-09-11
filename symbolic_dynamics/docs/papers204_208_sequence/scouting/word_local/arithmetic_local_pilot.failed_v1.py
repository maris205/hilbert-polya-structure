#!/usr/bin/env python3
"""Two predeclared small cyclic arithmetic scouts, not a theorem verifier."""
from itertools import product
import json
from math import gcd
from pilot import profile


def cprm(word):
    n = len(word)
    return tuple(1 + (a - 1) % word[(i + 1) % n] for i, a in enumerate(word))


def csgd(word):
    n = len(word)
    return tuple(a - gcd(a, word[(i + 1) % n]) for i, a in enumerate(word))


def main():
    for name, step, lower, upper in (("CPRM", cprm, 1, 6), ("CSGD", csgd, 0, 5)):
        for n in range(2, 7):
            for m in range(1, upper + 1):
                print(json.dumps({"candidate": name, "n": n, "m": m,
                                  **profile(product(range(lower, m + 1), repeat=n), step)},
                                 sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
