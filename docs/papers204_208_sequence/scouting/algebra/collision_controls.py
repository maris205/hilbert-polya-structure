#!/usr/bin/env python3
"""Cheap negative controls against blanket transfer claims; no author imports."""
import json
from itertools import product


def polarity_control():
    checked = 0
    for n in range(1, 5):
        edges = [(i, j) for i in range(n) for j in range(i, n)]
        size = 1 << n
        for bits in range(1 << len(edges)):
            rows = [0]*n
            for k, (i, j) in enumerate(edges):
                if bits >> k & 1:
                    rows[i] |= 1 << j
                    rows[j] |= 1 << i
            polar = [sum(1 << i for i in range(n) if s & rows[i] == s) for s in range(size)]
            assert all(polar[polar[polar[s]]] == polar[s] for s in range(size))
            for a, b in product(range(size), repeat=2):
                checked += 1
                seq = [(a, b)]
                for _ in range(6):
                    a, b = b, polar[a | b]
                    seq.append((a, b))
                if seq[6] != seq[3]:
                    return {"control": "arbitrary_symmetric_polarity", "checked_pairs": checked,
                            "n": n, "relation_rows": rows, "trace": seq,
                            "conclusion": "P^3=P does not imply two-register F^6=F^3"}
    return {"control": "arbitrary_symmetric_polarity", "checked_pairs": checked,
            "conclusion": "NO_COUNTEREXAMPLE_THROUGH_N4_NOT_A_PROOF"}


def cs_characteristic_control():
    # Literal GF(3) matrix arithmetic; find first failure of characteristic-2 F^2 law.
    q = 3
    mats = list(product(range(q), repeat=4))
    def add(a, b):
        return tuple((x+y) % q for x, y in zip(a, b))
    def mul(a, b):
        return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % q for i in range(2) for j in range(2))
    def comm(a, b):
        return tuple((x-y) % q for x, y in zip(mul(a, b), mul(b, a)))
    for a, b in product(mats, repeat=2):
        c, s = comm(a, b), add(a, b)
        trace = (s[0]+s[3]) % q
        actual = comm(c, s)
        expected = tuple(trace*x % q for x in c)
        if actual != expected:
            return {"control": "CS_odd_characteristic", "q": q, "A": a, "B": b,
                    "C": c, "S": s, "actual_first_coordinate_F2": actual,
                    "char2_formula_first_coordinate_F2": expected,
                    "conclusion": "characteristic-two hypothesis essential"}
    raise AssertionError("expected odd-characteristic obstruction missing")


if __name__ == "__main__":
    for row in (polarity_control(), cs_characteristic_control()):
        print(json.dumps(row, sort_keys=True, separators=(",", ":")))
