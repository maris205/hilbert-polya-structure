#!/usr/bin/env python3
"""Exact scout for random translation-intersection dynamics on F_2^d."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product
from math import comb, log2
from hashlib import sha256


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def translate(A: int, v: int, d: int) -> int:
    out = 0
    for x in range(1 << d):
        if A >> x & 1:
            out |= 1 << (x ^ v)
    return out


def step(A: int, v: int, d: int) -> int:
    return A & translate(A, v, d)


def vector_span(vectors: tuple[int, ...]) -> int:
    elements = {0}
    for v in vectors:
        elements |= {x ^ v for x in tuple(elements)}
    return sum(1 << x for x in elements)


def core(A: int, H: int, d: int) -> int:
    out = A
    for h in range(1 << d):
        if H >> h & 1:
            out &= translate(A, h, d)
    return out


def run(A: int, history: tuple[int, ...], d: int) -> int:
    for v in history:
        A = step(A, v, d)
    return A


def all_subspaces(d: int) -> tuple[int, ...]:
    seen = {1}
    todo = [1]
    while todo:
        H = todo.pop()
        for v in range(1, 1 << d):
            if not (H >> v & 1):
                K = vector_span(tuple(x for x in range(1 << d) if H >> x & 1) + (v,))
                if K not in seen:
                    seen.add(K)
                    todo.append(K)
    return tuple(sorted(seen))


def dim(H: int) -> int:
    size = H.bit_count()
    check(size > 0 and size & (size - 1) == 0, "subspace cardinality")
    return size.bit_length() - 1


def spanning_history_count(t: int, r: int) -> int:
    if r > t:
        return 0
    answer = 1
    for i in range(r):
        answer *= (1 << t) - (1 << i)
    return answer


def stabilizer(B: int, d: int) -> int:
    return sum(1 << v for v in range(1 << d) if translate(B, v, d) == B)


def poly_mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_pow(base: list[int], exponent: int) -> list[int]:
    out = [1]
    while exponent:
        if exponent & 1:
            out = poly_mul(out, base)
        base = poly_mul(base, base)
        exponent //= 2
    return out


def predicted_target_poly(B: int, d: int, t: int, subspaces: tuple[int, ...]) -> Counter[int]:
    b = B.bit_count()
    stab = stabilizer(B, d)
    answer: Counter[int] = Counter()
    for H in subspaces:
        if H & ~stab:
            continue
        r = dim(H)
        histories = spanning_history_count(t, r)
        if not histories:
            continue
        hsize = 1 << r
        check(b % hsize == 0, "stabilized target is a union of cosets")
        outside = (1 << (d - r)) - b // hsize
        # One outside H-coset may be any proper subset.
        base = [comb(hsize, k) for k in range(hsize)]
        choices = poly_pow(base, outside)
        for degree, coefficient in enumerate(choices):
            answer[b + degree] += histories * coefficient
    return +answer


def exhaustive_target_atlas(d: int, max_t: int) -> list[str]:
    N = 1 << d
    phase = 1 << N
    subspaces = all_subspaces(d)
    rows = []
    for t in range(max_t + 1):
        actual: dict[int, Counter[int]] = defaultdict(Counter)
        for history in product(range(N), repeat=t):
            H = vector_span(tuple(history))
            for A in range(phase):
                target = run(A, tuple(history), d)
                check(target == core(A, H, d), "history-span semigroup law")
                actual[target][A.bit_count()] += 1
        total = 0
        for B in range(phase):
            expected = predicted_target_poly(B, d, t, subspaces)
            check(actual[B] == expected, f"weighted target fibre d={d},t={t},B={B}")
            total += sum(expected.values())
        check(total == phase * N**t, "history/source mass")
        rows.append(f"d={d},t={t},targets={phase},mass={total}")
    return rows


def temporal_and_recovery_checks() -> list[str]:
    rows = []
    for d in range(1, 7):
        N = 1 << d
        subspaces = all_subspaces(d)
        gaussian_mass = 0
        for H in subspaces:
            r = dim(H)
            gaussian_mass += 1
            for t in range(0, d + 4):
                histories = spanning_history_count(t, r)
                brute = 0
                if d <= 4 and t <= 4:
                    for history in product(range(N), repeat=t):
                        brute += vector_span(tuple(history)) == H
                    check(brute == histories, "fixed-subspace history count")
        for t in range(0, d + 5):
            full = spanning_history_count(t, d)
            if d <= 4 and t <= 5:
                brute_full = sum(
                    vector_span(tuple(history)).bit_count() == N
                    for history in product(range(N), repeat=t)
                )
                check(brute_full == full, "full-rank history count")
            if t < d:
                check(full == 0, "rank cannot exceed history length")
            else:
                product_form = 1
                for i in range(d):
                    product_form *= (1 << t) - (1 << i)
                check(full == product_form, "sharp synchronization numerator")
        worst = ((1 << N) - 1) ^ 1  # V minus {0}
        for H in subspaces:
            check((core(worst, H, d) == 0) == (dim(H) == d), "sharp worst-state clock")

        # At t=1 and fixed |B|, the unweighted target fibre strictly recovers
        # the stabilizer dimension wherever that dimension can occur.
        by_size: dict[int, dict[int, int]] = defaultdict(dict)
        if d <= 4:
            phase = 1 << N
            for B in range(phase):
                s = dim(stabilizer(B, d))
                value = sum(predicted_target_poly(B, d, 1, subspaces).values())
                old = by_size[B.bit_count()].setdefault(s, value)
                check(old == value, "fibre depends only on size and stabilizer dimension")
            for b, values in by_size.items():
                ordered = sorted(values.items())
                for (_, left), (_, right) in zip(ordered, ordered[1:]):
                    check(left < right, f"stabilizer recovery b={b}")
        rows.append(f"d={d},subspaces={gaussian_mass},sharp_rank_clock=PASS")
    return rows


def main() -> None:
    rows = exhaustive_target_atlas(1, 5)
    rows += exhaustive_target_atlas(2, 5)
    rows += exhaustive_target_atlas(3, 4)
    rows += temporal_and_recovery_checks()
    digest = sha256("\n".join(rows).encode()).hexdigest()
    print("RANDOM_TRANSLATION_INTERSECTION_SCOUT_V1")
    print(f"boxes={len(rows)}")
    print(f"row_sha256={digest}")
    print(f"assertions={ASSERTIONS}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
