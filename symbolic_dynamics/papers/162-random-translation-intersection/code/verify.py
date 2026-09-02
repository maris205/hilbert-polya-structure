#!/usr/bin/env python3
"""Independent exact checks for P162 random translation intersections.

Standard library only.  This file imports neither scout nor hostile-gate code.
Enumeration is counterexample pressure, not a proof.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb


ASSERTIONS = 0


def check(condition: bool, message: str = "assertion failed") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def translate(mask: int, v: int, n: int) -> int:
    out = 0
    for x in range(n):
        if (mask >> x) & 1:
            out |= 1 << (x ^ v)
    return out


def update(mask: int, v: int, n: int) -> int:
    return mask & translate(mask, v, n)


def literal(mask: int, history: tuple[int, ...], n: int) -> int:
    for v in history:
        mask = update(mask, v, n)
    return mask


def span_elements(vectors: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    span = {0}
    for v in vectors:
        span |= {x ^ v for x in tuple(span)}
    return tuple(sorted(span))


def erosion(mask: int, span: tuple[int, ...], n: int) -> int:
    out = (1 << n) - 1
    for h in span:
        out &= translate(mask, h, n)
    return out


def stabilizer(mask: int, n: int) -> tuple[int, ...]:
    return tuple(v for v in range(n) if translate(mask, v, n) == mask)


def gauss2(n: int, r: int) -> int:
    if r < 0 or r > n:
        return 0
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= 2 ** (n - i) - 1
        denominator *= 2 ** (r - i) - 1
    check(numerator % denominator == 0, "Gaussian binomial integrality")
    return numerator // denominator


def spanning_histories(t: int, r: int) -> int:
    if r > t:
        return 0
    ans = 1
    for i in range(r):
        ans *= 2**t - 2**i
    return ans


def poly_mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_pow(base: list[int], exponent: int) -> list[int]:
    out = [1]
    for _ in range(exponent):
        out = poly_mul(out, base)
    return out


def predicted_fibre(d: int, target: int, t: int) -> list[int]:
    n = 2**d
    b = target.bit_count()
    stab = stabilizer(target, n)
    s = len(stab).bit_length() - 1
    out = [0] * (n + 1)
    for r in range(s + 1):
        q = 2**r
        check(b % q == 0, "target must be a union of H-cosets")
        outside = 2 ** (d - r) - b // q
        base = [comb(q, k) for k in range(q)]
        poly = poly_pow(base, outside)
        factor = gauss2(s, r) * spanning_histories(t, r)
        for k, value in enumerate(poly):
            out[b + k] += factor * value
    return out


def all_subspaces(d: int) -> tuple[tuple[int, ...], ...]:
    n = 2**d
    spaces = {span_elements(())}
    changed = True
    while changed:
        changed = False
        for h in tuple(spaces):
            hs = set(h)
            for v in range(n):
                if v not in hs:
                    k = span_elements(list(h) + [v])
                    if k not in spaces:
                        spaces.add(k)
                        changed = True
    return tuple(sorted(spaces, key=lambda h: (len(h), h)))


def exact_literal_atlas() -> list[str]:
    rows: list[str] = []
    boxes = {0: 6, 1: 8, 2: 6, 3: 4}
    for d, tmax in boxes.items():
        n = 2**d
        phase = 1 << n
        for t in range(tmax + 1):
            observed = [[0] * (n + 1) for _ in range(phase)]
            history_count = 0
            for history in product(range(n), repeat=t):
                history_count += 1
                h = span_elements(history)
                for source in range(phase):
                    direct = literal(source, history, n)
                    collapsed = erosion(source, h, n)
                    check(direct == collapsed, "history-span identity")
                    observed[direct][source.bit_count()] += 1
            check(history_count == n**t, "history census")
            total = 0
            for target in range(phase):
                predicted = predicted_fibre(d, target, t)
                for k in range(n + 1):
                    check(observed[target][k] == predicted[k],
                          "weighted target fibre")
                    total += observed[target][k]
                if t == 0:
                    expected = [0] * (n + 1)
                    expected[target.bit_count()] = 1
                    check(predicted == expected, "time-zero identity")
                if target == phase - 1:
                    expected = [0] * (n + 1)
                    expected[n] = n**t
                    check(predicted == expected, "full target boundary")
            check(total == phase * n**t, "atlas mass")
            rows.append(
                f"atlas d={d} t={t} histories={history_count} "
                f"pairs={phase * history_count} mass={total}"
            )
    return rows


def rank_and_clock_checks() -> list[str]:
    rows: list[str] = []
    for d in range(5):
        n = 2**d
        for t in range(6):
            counts = [0] * (d + 1)
            for history in product(range(n), repeat=t):
                r = len(span_elements(history)).bit_length() - 1
                counts[r] += 1
            predicted = [gauss2(d, r) * spanning_histories(t, r)
                         for r in range(d + 1)]
            for r in range(d + 1):
                check(counts[r] == predicted[r], "rank census")
            check(sum(counts) == n**t, "rank mass")
            if t < d:
                check(counts[d] == 0, "pre-d full-rank hole")
            else:
                product_numerator = 1
                for i in range(d):
                    product_numerator *= 2**t - 2**i
                check(counts[d] == product_numerator,
                      "full-rank product")
        expected = sum((Fraction(1, 1 - Fraction(2**r, 2**d))
                        for r in range(d)), Fraction(0))
        recurrence = Fraction(0)
        for r in reversed(range(d)):
            p = Fraction(2**d - 2**r, 2**d)
            recurrence += 1 / p
        check(expected == recurrence, "mean clock recurrence")
        rows.append(f"rank d={d} t=0..5 mean={expected}")
    return rows


def structural_boundaries() -> list[str]:
    rows: list[str] = []
    for d in range(7):
        n = 2**d
        phase = 1 << n
        witness = phase - 2
        spaces = all_subspaces(d)
        for h in spaces:
            hmask = sum(1 << x for x in h)
            check(erosion(witness, h, n) == (phase - 1) ^ hmask,
                  "sharp witness identity")
        check(len(spaces) == sum(gauss2(d, r) for r in range(d + 1)),
              "subspace census")
        rows.append(f"witness d={d} subspaces={len(spaces)}")

    for d in range(5):
        n = 2**d
        phase = 1 << n
        fixed = []
        for source in range(phase):
            is_fixed = all(update(source, v, n) == source for v in range(n))
            check(is_fixed == (source in (0, phase - 1)),
                  "universal fixed state")
            if is_fixed:
                fixed.append(source)
        check(fixed == [0, phase - 1], "fixed-state list")
        rows.append(f"fixed d={d} phase={phase} count={len(fixed)}")
    return rows


def one_step_and_recovery() -> list[str]:
    rows: list[str] = []
    odd_trivial = 0
    for d in range(5):
        n = 2**d
        phase = 1 << n
        groups: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for target in range(phase):
            b = target.bit_count()
            stab = stabilizer(target, n)
            check(len(stab) & (len(stab) - 1) == 0, "stabilizer power of two")
            s = len(stab).bit_length() - 1
            poly = predicted_fibre(d, target, 1)
            value = sum(poly)
            if s == 0:
                expected = 1
                if b % 2:
                    odd_trivial += 1
            else:
                check(b % 2 == 0, "nontrivial stabilizer forces even size")
                expected = 1 + (2**s - 1) * 3 ** (2 ** (d - 1) - b // 2)
            check(value == expected, "one-step boundary formula")
            groups[b].append((s, value))
        for b, pairs in groups.items():
            by_s: dict[int, int] = {}
            for s, value in pairs:
                if s in by_s:
                    check(by_s[s] == value, "fibre depends on d,b,s")
                else:
                    by_s[s] = value
            ordered = sorted(by_s.items())
            for (s0, v0), (s1, v1) in zip(ordered, ordered[1:]):
                check(s0 < s1 and v0 < v1, "strict stabilizer recovery")
            for s, value in ordered:
                check((value == 1) == (s == 0), "trivial stabilizer recovery")
        recovered_d = (phase.bit_length() - 1).bit_length() - 1
        check(recovered_d == d, "phase-size recovery")
        rows.append(f"recovery d={d} targets={phase} sizes={len(groups)}")
    check(odd_trivial > 0, "odd trivial-stabilizer targets exercised")
    rows.append(f"boundary odd_targets_with_s0={odd_trivial}")
    return rows


def main() -> None:
    rows = []
    rows.extend(exact_literal_atlas())
    rows.extend(rank_and_clock_checks())
    rows.extend(structural_boundaries())
    rows.extend(one_step_and_recovery())
    row_blob = "\n".join(rows).encode("utf-8")
    print("P162 RTI independent exact verifier")
    for row in rows:
        print(row)
    print(f"ASSERTIONS {ASSERTIONS}")
    print(f"ROW_SHA256 {sha256(row_blob).hexdigest()}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
