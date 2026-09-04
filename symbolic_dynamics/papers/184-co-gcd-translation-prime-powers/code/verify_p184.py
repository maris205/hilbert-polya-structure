#!/usr/bin/env python3
"""Exact author-side regression control for P184.

The implementation uses only the Python standard library, writes no files,
and emits deterministic stdout for bytewise comparison with CANONICAL.txt.
"""

from __future__ import annotations

from collections import Counter
from math import gcd


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def equal(self, got, expected, label: str) -> None:
        self.assertions += 1
        if got != expected:
            raise AssertionError(f"{label}: got={got!r}, expected={expected!r}")

    def true(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)


AUDIT = Audit()


def valuation(x: int, p: int, a: int) -> int:
    if x == 0:
        return a
    result = 0
    while x % p == 0:
        x //= p
        result += 1
    return result


def step(x: int, modulus: int) -> int:
    return (x + modulus // gcd(x, modulus)) % modulus


def literal_tail_period(start: int, modulus: int) -> tuple[int, int]:
    first: dict[int, int] = {}
    x = start
    time = 0
    while x not in first:
        first[x] = time
        x = step(x, modulus)
        time += 1
    return first[x], time - first[x]


def predicted_tail_period(x: int, p: int, a: int) -> tuple[int, int]:
    value = valuation(x, p, a)
    if 2 * value < a:
        return 0, p**value
    if 2 * value > a:
        return 1, p ** (a - value)
    h = a // 2
    unit = x // (p**h)
    run = p - unit % p
    landed = unit + run
    extra = valuation(landed, p, h)
    return run + 1, p ** (h - extra)


def double_targets(p: int, a: int) -> set[int]:
    result = {1}
    for value in range(1, (a - 1) // 2 + 1):
        for unit in range(1, p**value):
            if unit % p:
                result.add(p**value * (1 + p ** (a - 2 * value) * unit))
    return result


def empty_targets(p: int, a: int) -> set[int]:
    modulus = p**a
    h = a // 2
    if a % 2:
        return {y for y in range(modulus) if valuation(y, p, a) > h}
    return {p**h * z for z in range(p**h) if z % p == 1}


def predicted_cycle_census(p: int, a: int) -> Counter:
    return Counter(
        {
            p**value: (p - 1) * p ** (a - 2 * value - 1)
            for value in range((a - 1) // 2 + 1)
        }
    )


def predicted_tail_census(p: int, a: int) -> Counter:
    modulus = p**a
    recurrent = modulus - p ** (a // 2)
    result = Counter({0: recurrent})
    if a % 2:
        result[1] = p ** (a // 2)
    else:
        h = a // 2
        for depth in range(1, p + 1):
            result[depth] = p ** (h - 1)
    return result


def actual_cycle_census(recurrent: set[int], modulus: int) -> Counter:
    unseen = set(recurrent)
    result = Counter()
    while unseen:
        start = min(unseen)
        orbit: list[int] = []
        x = start
        while x not in orbit:
            orbit.append(x)
            x = step(x, modulus)
        AUDIT.equal(x, start, f"recurrent orbit closes at start N={modulus} x={start}")
        result[len(orbit)] += 1
        unseen.difference_update(orbit)
    return result


def verify_case(p: int, a: int) -> str:
    modulus = p**a
    tails = Counter()
    periods = Counter()
    recurrent: set[int] = set()
    preimages: dict[int, list[int]] = {y: [] for y in range(modulus)}

    for x in range(modulus):
        actual = literal_tail_period(x, modulus)
        predicted = predicted_tail_period(x, p, a)
        AUDIT.equal(actual, predicted, f"orbit p={p} a={a} x={x}")
        tail, period = actual
        tails[tail] += 1
        periods[period] += 1
        if tail == 0:
            recurrent.add(x)
        target = step(x, modulus)
        preimages[target].append(x)
        for translate in (-2, -1, 0, 1, 2):
            AUDIT.equal(
                gcd(x + translate * modulus, modulus),
                gcd(x, modulus),
                f"representative gcd p={p} a={a} x={x} k={translate}",
            )

    expected_tails = predicted_tail_census(p, a)
    AUDIT.equal(tails, expected_tails, f"tail census p={p} a={a}")
    expected_recurrent = modulus - p ** (a // 2)
    AUDIT.equal(len(recurrent), expected_recurrent, f"recurrent count p={p} a={a}")
    cycles = actual_cycle_census(recurrent, modulus)
    AUDIT.equal(cycles, predicted_cycle_census(p, a), f"cycle census p={p} a={a}")

    doubles = double_targets(p, a)
    empties = empty_targets(p, a)
    defect = p ** ((a - 1) // 2)
    AUDIT.equal(len(doubles), defect, f"double target count p={p} a={a}")
    AUDIT.equal(len(empties), defect, f"empty target count p={p} a={a}")
    AUDIT.true(doubles.isdisjoint(empties), f"target sets disjoint p={p} a={a}")

    for y in range(modulus):
        incoming = preimages[y]
        predicted_size = 0 if y in empties else 2 if y in doubles else 1
        AUDIT.equal(len(incoming), predicted_size, f"fibre atlas p={p} a={a} y={y}")
        AUDIT.true(len(incoming) <= 2, f"fibre cap p={p} a={a} y={y}")
        for source in incoming:
            AUDIT.equal(step(source, modulus), y, f"listed predecessor p={p} a={a} x={source} y={y}")

    histogram = Counter(len(preimages[y]) for y in range(modulus))
    AUDIT.equal(
        histogram,
        Counter({0: defect, 1: modulus - 2 * defect, 2: defect}),
        f"fibre histogram p={p} a={a}",
    )
    image = {step(x, modulus) for x in range(modulus)}
    AUDIT.equal(image, set(range(modulus)) - empties, f"image set p={p} a={a}")
    AUDIT.equal(len(image), modulus - defect, f"image size p={p} a={a}")

    # The last middle unit lands at zero, then at the fixed unit 1.
    if a % 2 == 0:
        h = a // 2
        boundary = p**h * (p**h - 1)
        AUDIT.equal(step(boundary, modulus), 0, f"middle zero landing p={p} a={a}")
        AUDIT.equal(literal_tail_period(boundary, modulus), (2, 1), f"middle zero orbit p={p} a={a}")
        if p == 2:
            for unit in range(1, p**h, 2):
                x = p**h * unit
                AUDIT.equal(literal_tail_period(x, modulus)[0], 2, f"binary middle tail a={a} u={unit}")

    tail_text = ",".join(f"{depth}:{tails[depth]}" for depth in sorted(tails))
    cycle_text = ",".join(f"{length}:{cycles[length]}" for length in sorted(cycles))
    return (
        f"p={p} a={a} N={modulus} recurrent={len(recurrent)} image={len(image)} "
        f"fibres_0_1_2={defect}/{modulus - 2 * defect}/{defect} "
        f"tails={tail_text} cycles={cycle_text}"
    )


def main() -> None:
    print("P184_EXACT_AUTHOR_CONTROL")
    cases = (
        *((2, a) for a in range(1, 10)),
        *((3, a) for a in range(1, 8)),
        *((5, a) for a in range(1, 6)),
        *((7, a) for a in range(1, 5)),
        *((11, a) for a in range(1, 3)),
    )
    AUDIT.equal(len(cases), 27, "published carrier count")
    for p, a in cases:
        print(verify_case(p, a))
    print(f"ASSERTIONS={AUDIT.assertions}")
    print("STATUS=HOLD_EXTERNAL")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()

