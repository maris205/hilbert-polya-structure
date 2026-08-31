#!/usr/bin/env python3
"""Exact scout for complementary power--gcd divisor dynamics.

The script is deliberately dependency-free and deterministic.  Finite
enumeration is used only as falsification evidence for the formulas recorded
in SCOUT.md; it is not presented as a proof or a novelty claim.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import product
from math import ceil, gcd, prod


PRIMES = (2, 3, 5, 7)


def scalar_step(e: int, k: int, a: int) -> int:
    return max(e - k * a, 0)


def vector_step(es: tuple[int, ...], k: int, state: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(scalar_step(e, k, a) for e, a in zip(es, state))


def literal_step(es: tuple[int, ...], k: int, state: tuple[int, ...]) -> int:
    n = prod(p**e for p, e in zip(PRIMES, es))
    d = prod(p**a for p, a in zip(PRIMES, state))
    return n // gcd(n, d**k)


def decode(es: tuple[int, ...], value: int) -> tuple[int, ...]:
    ans = []
    for p, e in zip(PRIMES, es):
        a = 0
        while value % p == 0:
            value //= p
            a += 1
        assert a <= e
        ans.append(a)
    assert value == 1
    return tuple(ans)


def tail_period(es: tuple[int, ...], k: int, state: tuple[int, ...]) -> tuple[int, int]:
    seen: dict[tuple[int, ...], int] = {}
    x = state
    while x not in seen:
        seen[x] = len(seen)
        x = vector_step(es, k, x)
    return seen[x], len(seen) - seen[x]


def scalar_depth(e: int, k: int, a: int) -> int:
    """Exact entrance time into the scalar recurrent set."""
    if a == 0 or a == e or ((k + 1) * a == e):
        return 0
    delta = (k + 1) * a - e
    if delta > 0:
        t = 1
        while k**t * delta < e:
            t += 2
        return t
    delta = -delta
    t = 2
    while k**t * delta < e:
        t += 2
    return t


def scalar_tail_cumulative(e: int, k: int, t: int) -> int:
    """Closed count of scalar states with recurrent depth at most t."""
    total = 2 + int(e % (k + 1) == 0)
    if t >= 1:
        odd = t if t % 2 else t - 1
        threshold = ceil(e / (k**odd))
        lower = ceil((e + threshold) / (k + 1))
        total += max(0, e - max(lower, 1))
    if t >= 2:
        even = t if t % 2 == 0 else t - 1
        threshold = ceil(e / (k**even))
        upper = (e - threshold) // (k + 1)
        total += max(0, upper)
    return total


def scalar_fibre(e: int, k: int, target: int) -> int:
    if target == 0:
        return e - ceil(e / k) + 1
    return int((e - target) % k == 0)


def states(es: tuple[int, ...]):
    return product(*(range(e + 1) for e in es))


def audit_box(es: tuple[int, ...], k: int) -> tuple[int, int, int, int, str]:
    global ASSERTIONS
    all_states = list(states(es))
    image_counts: Counter[tuple[int, ...]] = Counter()
    tail_counts: Counter[int] = Counter()
    period_counts: Counter[int] = Counter()
    max_tail = 0

    for a in all_states:
        nxt = vector_step(es, k, a)
        literal = decode(es, literal_step(es, k, a))
        assert literal == nxt
        ASSERTIONS += 1

        tail, period = tail_period(es, k, a)
        predicted_tail = max(scalar_depth(e, k, x) for e, x in zip(es, a))
        assert tail == predicted_tail
        ASSERTIONS += 1
        assert period in (1, 2)
        ASSERTIONS += 1

        for e, x in zip(es, a):
            tau = scalar_depth(e, k, x)
            if tau:
                for t in range(tau):
                    numerator = e + (-k) ** t * ((k + 1) * x - e)
                    assert numerator % (k + 1) == 0
                    y = x
                    for _ in range(t):
                        y = scalar_step(e, k, y)
                    assert y == numerator // (k + 1) > 0
                    ASSERTIONS += 2
                y = x
                for _ in range(tau):
                    y = scalar_step(e, k, y)
                assert y == 0
                assert scalar_step(e, k, y) == e
                ASSERTIONS += 2

        image_counts[nxt] += 1
        tail_counts[tail] += 1
        period_counts[period] += 1
        max_tail = max(max_tail, tail)

    deltas = tuple(int(e % (k + 1) == 0) for e in es)
    recurrent = prod(2 + delta for delta in deltas)
    fixed = int(all(deltas))
    assert tail_counts[0] == recurrent
    assert period_counts[1] == fixed
    assert period_counts[2] == len(all_states) - fixed
    ASSERTIONS += 3

    for target in all_states:
        predicted = prod(scalar_fibre(e, k, b) for e, b in zip(es, target))
        assert image_counts[target] == predicted
        ASSERTIONS += 1

    running = 0
    for t in range(max_tail + 1):
        running += tail_counts[t]
        predicted = prod(scalar_tail_cumulative(e, k, t) for e in es)
        assert running == predicted
        ASSERTIONS += 1
    assert running == len(all_states)
    ASSERTIONS += 1

    cycles = (recurrent + fixed) // 2
    signature = (
        f"e={','.join(map(str, es))};k={k};states={len(all_states)};"
        f"tail={max_tail};rec={recurrent};fix={fixed};cycles={cycles};"
        f"image={len(image_counts)};tails={sorted(tail_counts.items())}"
    )
    return len(all_states), max_tail, recurrent, fixed, signature


ASSERTIONS = 0


def main() -> None:
    global ASSERTIONS
    boxes: list[tuple[tuple[int, ...], int]] = []
    boxes.extend(((e,), k) for k in range(2, 8) for e in range(1, 81))
    boxes.extend(((e1, e2), k) for k in range(2, 6) for e1 in range(1, 13) for e2 in range(1, 11))
    boxes.extend(
        ((e1, e2, e3), k)
        for k in range(2, 5)
        for e1 in range(1, 8)
        for e2 in range(1, 7)
        for e3 in range(1, 6)
    )
    boxes.extend(
        [
            ((3, 4, 5, 6), 2),
            ((6, 6, 6, 6), 2),
            ((7, 8, 9, 10), 2),
            ((4, 5, 6, 7), 3),
            ((8, 8, 8, 8), 3),
            ((3, 7, 11, 15), 3),
            ((5, 6, 7, 8), 4),
            ((10, 10, 10, 10), 4),
            ((4, 9, 14, 19), 5),
            ((6, 13, 20, 27), 6),
        ]
    )

    total_states = 0
    maximum_tail = 0
    signatures: list[str] = []
    selected: list[str] = []
    for es, k in boxes:
        count, tail, _, _, signature = audit_box(es, k)
        total_states += count
        maximum_tail = max(maximum_tail, tail)
        signatures.append(signature)
        if (es, k) in {
            ((80,), 2),
            ((12, 10), 5),
            ((7, 6, 5), 4),
            ((7, 8, 9, 10), 2),
            ((6, 13, 20, 27), 6),
        }:
            selected.append(signature)

    digest = sha256("\n".join(signatures).encode()).hexdigest()
    ASSERTIONS += 4
    assert len(boxes) == 1600
    assert total_states > 100_000
    assert maximum_tail >= 7
    assert len(selected) == 5

    print("COMPLEMENTARY POWER-GCD DIVISOR DYNAMICS — EXACT SCOUT")
    print(f"boxes={len(boxes)}")
    print(f"states={total_states}")
    print(f"assertions={ASSERTIONS}")
    print(f"maximum_tail={maximum_tail}")
    print(f"signature_sha256={digest}")
    print("selected_boxes:")
    for line in selected:
        print(line)
    print("RESULT: PASS")


if __name__ == "__main__":
    main()
