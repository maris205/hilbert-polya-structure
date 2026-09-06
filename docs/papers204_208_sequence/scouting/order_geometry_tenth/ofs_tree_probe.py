#!/usr/bin/env python3
"""Original-box author comparison to a structurally different tree recursion."""
import importlib.util
import itertools
import json
from collections import Counter
from functools import lru_cache
from pathlib import Path

base = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("literal_pilot", base/"pilot.py")
literal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(literal)
CHECKS = 0


def require(condition, detail=None):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError((CHECKS, detail))


@lru_cache(None)
def trees(m):
    if m == 0:
        return ((),)
    return tuple((l, r) for k in range(m) for l in trees(k) for r in trees(m-1-k))


def ls(t):
    branches = []
    while t:
        t, b = t
        branches.append(b)
    return tuple(reversed(branches))


def first(t, replacement):
    if not t:
        return replacement
    return (first(t[0], replacement), t[1])


@lru_cache(None)
def product(bs):
    if len(bs) == 2:
        return f((bs[0], bs[1]))
    return first(f(((), bs[-1])), product(bs[:-1]))


@lru_cache(None)
def f(t):
    if not t or t == ((), ()):
        return t
    bs = ls(t)
    if len(bs) >= 2:
        return ((), product(bs))
    cs = ls(bs[0])
    if len(cs) == 1:
        return first(f(((), cs[0])), ((), ()))
    return (((), ()), product(cs))


def diagonals(t):
    edges = []
    def visit(s, start, root=False):
        if not s:
            return start+1
        middle = visit(s[0], start)
        end = visit(s[1], middle)
        if not root:
            edges.append((start, end))
        return end
    visit(t, 0, True)
    return tuple(sorted(edges))


def word(t):
    return "U"+word(t[0])+"D"+word(t[1]) if t else ""


def exponent(t, on_spine=True):
    if not t:
        return 0
    own = int(bool(t[0]) and not on_spine)
    return own+exponent(t[0], on_spine)+exponent(t[1], False)


def main():
    rows = []
    for n in range(3, 11):
        carrier = trees(n-2)
        require({diagonals(t) for t in carrier} == set(literal.triangulations(tuple(range(n)))))
        counts = Counter(f(t) for t in carrier)
        wrong_word, wrong_exponent = [], []
        for t in carrier:
            d, out = diagonals(t), diagonals(f(t))
            require(out == literal.ofs(d, n), (n, d, out, literal.ofs(d, n)))
            if n >= 4:
                require(((1, n-1) in out) != ((1, n-1) in d))
                require((1, n-1) in out or (0, 2) in out)
            if (t in counts) != ("UUDU" not in word(t)):
                wrong_word.append({"target": d, "word": word(t), "actual_fibre": counts[t]})
            if counts[t] and counts[t] != 2**exponent(t):
                wrong_exponent.append({"target": d, "word": word(t),
                                       "actual_fibre": counts[t], "guessed": 2**exponent(t)})
        rows.append({"n": n, "states": len(carrier), "recursion_matches": True,
                     "standard_UUDU_image_mismatches": len(wrong_word),
                     "standard_UUDU_first_counterexample": wrong_word[:1],
                     "guessed_exponent_mismatches": len(wrong_exponent),
                     "guessed_exponent_first_counterexample": wrong_exponent[:1]})
    print(json.dumps({"role": "author_tree_dictionary_and_falsification_probe",
                      "assertions": CHECKS, "literal_flip_assertions": literal.CHECKS,
                      "rows": rows}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
