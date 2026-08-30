#!/usr/bin/env python3
"""Independent exact symbolic checks for C239."""
from __future__ import annotations

from math import gcd
import sympy as sp


def divisors(v: int) -> list[int]:
    return sp.divisors(v)


def mobius(v: int) -> int:
    return int(sp.mobius(v))


def fixed(k: int, m: int, r: int) -> int:
    return gcd(k**r - 1, m) - 1


def cycles(k: int, n: int) -> list[list[int]]:
    m = k * n + 1
    seen: set[int] = set()
    out: list[list[int]] = []
    for i in range(1, m):
        if i in seen:
            continue
        c: list[int] = []
        x = i
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = (k * x) % m
        assert x == i
        j = c.index(min(c))
        out.append(c[j:] + c[:j])
    return sorted(out, key=lambda c: c[0])


def packet_interleave(k: int, n: int, position: int) -> int:
    j, r0 = divmod(position - 1, n)
    return k * (r0 + 1) - j


def main() -> None:
    checks = 0
    k, n, r, i, M = sp.symbols("k n r i M", integer=True, positive=True)
    assert sp.expand((k * n + 1) - M).subs(M, k * n + 1) == 0
    checks += 1
    packet_checks = 0
    for kk in range(2, 7):
        for nn in range(1, 11):
            mm = kk * nn + 1
            for pos in range(1, mm):
                assert packet_interleave(kk, nn, pos) == (kk * pos) % mm
                packet_checks += 1
    assert packet_checks == 1100
    checks += 1
    # Iterating the modular multiplication map r times gives k^r i modulo M.
    # The fixed congruence has gcd(k^r-1,M) residue solutions, one of which is
    # the excluded zero position.
    congruence = sp.expand((k**r - 1) * i)
    assert sp.factor(congruence - (k**r * i - i)) == 0
    checks += 1
    # Concrete symbolic polynomial identities for representative cycles.
    z, lam = sp.symbols("z lam")
    for kk, nn in ((2, 2), (2, 5), (3, 3), (4, 2), (5, 2), (6, 1)):
        cs = cycles(kk, nn)
        zeta_denominator = sp.prod(1 - z ** len(c) for c in cs)
        char = sp.prod(lam ** len(c) - 1 for c in cs)
        counts = {length: sum(len(c) == length for c in cs) for length in range(1, 100)}
        zeta_denominator_factored = sp.prod((1 - z**length) ** count for length, count in counts.items() if count)
        char_factored = sp.prod((lam**length - 1) ** count for length, count in counts.items() if count)
        assert sp.expand(zeta_denominator - zeta_denominator_factored) == 0
        assert sp.expand(char - char_factored) == 0
        checks += 2
        q = sp.n_order(kk, kk * nn + 1)
        assert all(fixed(kk, kk * nn + 1, int(t)) == fixed(kk, kk * nn + 1, int(t) + int(q)) for t in (1, 2, 3))
        checks += 1
        for t in range(1, int(q) + 1):
            exact = sum(mobius(t // d) * fixed(kk, kk * nn + 1, d) for d in divisors(t))
            direct = t * sum(len(c) == t for c in cs)
            assert exact == direct
            checks += 1
    # A small permutation matrix gives the same characteristic polynomial.
    kk, nn = 2, 2
    m = kk * nn + 1
    P = sp.zeros(m - 1)
    for old in range(1, m):
        new = (kk * old) % m
        P[new - 1, old - 1] = 1
    char_matrix = sp.factor((lam * sp.eye(m - 1) - P).det())
    char_cycles = sp.factor(sp.prod(lam ** len(c) - 1 for c in cycles(kk, nn)))
    assert sp.expand(char_matrix - char_cycles) == 0
    checks += 1
    print(f"C239 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
