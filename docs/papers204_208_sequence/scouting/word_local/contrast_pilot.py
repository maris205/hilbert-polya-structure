#!/usr/bin/env python3
"""Four predeclared full ternary contrast/diversity probes, n=3..9."""
from itertools import product
import json
from pilot import profile


def evaluate(word, operation):
    n = len(word)
    return tuple(operation(word[(i - 1) % n], a, word[(i + 1) % n])
                 for i, a in enumerate(word))


def main():
    rules = (
        ("LDC", lambda a, b, c: len({a, b, c}) - 1),
        ("LRG", lambda a, b, c: max(a, b, c) - min(a, b, c)),
        ("MDE", lambda a, b, c: abs(b - sorted((a, b, c))[1])),
        ("MNC", lambda a, b, c: min(abs(b - a), abs(b - c))),
    )
    for name, operation in rules:
        for n in range(3, 10):
            result = profile(product(range(3), repeat=n),
                             lambda word: evaluate(word, operation))
            print(json.dumps({"candidate": name, "n": n, **result}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
