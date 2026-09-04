#!/usr/bin/env python3
"""Exact finite controls for cyclic Goedel-implication dynamics.

The computation is deliberately standard-library only.  Exhaustion is a
regression oracle for the paper's proofs, never evidence of novelty.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import product
from math import comb, gcd


def step(x: tuple[int, ...], q: int) -> tuple[int, ...]:
    top = q - 1
    m = len(x)
    return tuple(top if x[i] <= x[(i + 1) % m] else x[(i + 1) % m]
                 for i in range(m))


def shift(x: tuple[int, ...], r: int = 1) -> tuple[int, ...]:
    r %= len(x)
    return x[r:] + x[:r]


def in_core(y: tuple[int, ...], q: int) -> bool:
    top = q - 1
    m = len(y)
    return all(y[(i + 1) % m] == top or y[i] > y[(i + 1) % m]
               for i in range(m))


def fibre_formula(y: tuple[int, ...], q: int) -> int:
    top = q - 1
    m = len(y)
    sites = [i for i, a in enumerate(y) if a < top]
    if not sites:
        return q
    ans = 1
    for j, p in enumerate(sites):
        nxt = sites[(j + 1) % len(sites)]
        d = (nxt - p) % m
        if d == 0:
            d = m
        a, b = y[p], y[nxt]
        factor = comb(top - a + d - 1, d - 1)
        if b >= a:
            factor -= comb(b - a + d - 1, d - 1)
        ans *= factor
    return ans


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def matpow(a: list[list[int]], e: int) -> list[list[int]]:
    n = len(a)
    out = [[int(i == j) for j in range(n)] for i in range(n)]
    while e:
        if e & 1:
            out = matmul(out, a)
        a = matmul(a, a)
        e //= 2
    return out


def trace_power(q: int, e: int) -> int:
    top = q - 1
    a = [[int(b == top or x > b) for b in range(q)] for x in range(q)]
    p = matpow(a, e)
    return sum(p[i][i] for i in range(q))


def char_recurrence_ok(q: int, length: int = 20) -> bool:
    # chi_A(L)=L^q-(L+1)^(q-1).
    vals = [trace_power(q, m) for m in range(length + 1)]
    for m in range(q, length + 1):
        rhs = sum(comb(q - 1, j) * vals[m - q + j]
                  for j in range(q))
        if vals[m] != rhs:
            return False
    return True


def main() -> None:
    assertions = 0
    transitions = 0
    records: list[str] = []
    for q in range(2, 6):
        for m in range(1, 8):
            states = list(product(range(q), repeat=m))
            images = [step(x, q) for x in states]
            fibres = Counter(images)
            transitions += len(states)

            core = {y for y in states if in_core(y, q)}
            image_set = set(images)
            assert image_set == core
            assertions += 1
            assert len(core) == trace_power(q, m)
            assertions += 1

            for x, y in zip(states, images):
                assert in_core(y, q)
                assert step(y, q) == shift(y)
                assert (x in core) == (step(x, q) == shift(x))
                assertions += 3

            for y in states:
                expected = fibre_formula(y, q) if y in core else 0
                assert fibres.get(y, 0) == expected
                assertions += 1
            assert sum(fibres.values()) == q**m
            assertions += 1

            x = states[-1]
            for r in range(1, m + 2):
                fixed = 0
                for x in states:
                    z = x
                    for _ in range(r):
                        z = step(z, q)
                    fixed += z == x
                assert fixed == trace_power(q, gcd(m, r))
                assertions += 1

            max_fibre = max(fibres.values())
            records.append(
                f"q={q} m={m} states={q**m} core={len(core)} "
                f"transient={q**m-len(core)} max_fibre={max_fibre}"
            )

        assert char_recurrence_ok(q)
        assertions += 1

    digest = sha256("\n".join(records).encode()).hexdigest()
    print("cyclic Goedel-implication exact controls")
    for line in records:
        print(line)
    print(f"transitions={transitions}")
    print(f"assertions={assertions}")
    print(f"record_digest={digest}")
    print("status=PASS")


if __name__ == "__main__":
    main()
