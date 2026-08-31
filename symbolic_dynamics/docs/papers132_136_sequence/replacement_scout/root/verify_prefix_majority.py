#!/usr/bin/env python3
"""Exact falsification scout for synchronous prefix-majority dynamics."""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import groupby, product
from math import ceil, comb, log2


def step(word: tuple[int, ...]) -> tuple[int, ...]:
    balance = 0
    out = []
    for bit in word:
        balance += 1 if bit else -1
        out.append(int(balance >= 0))
    return tuple(out)


def runs(word: tuple[int, ...]) -> list[tuple[int, int]]:
    return [(bit, len(tuple(group))) for bit, group in groupby(word)]


def catalan(m: int) -> int:
    return comb(2 * m, m) // (m + 1)


def meander(m: int) -> int:
    return comb(m, m // 2)


def predicted_fibre(target: tuple[int, ...]) -> int:
    rr = runs(target)
    if len(rr) == 1:
        bit, length = rr[0]
        return meander(length if bit else length - 1)

    bit, length = rr[0]
    if bit:
        if length % 2:
            return 0
        answer = catalan(length // 2)
    else:
        if length % 2 == 0:
            return 0
        answer = catalan((length - 1) // 2)

    for _, length in rr[1:-1]:
        if length % 2 == 0:
            return 0
        answer *= catalan((length - 1) // 2)
    answer *= meander(rr[-1][1] - 1)
    return answer


def fixed_words(n: int) -> set[tuple[int, ...]]:
    answer = set()
    for r in range(n // 2 + 1):
        answer.add(tuple((0, 1) * r + (0,) * (n - 2 * r)))
    for r in range((n - 1) // 2 + 1):
        answer.add(tuple((0, 1) * r + (1,) * (n - 2 * r)))
    return answer


def tail(word: tuple[int, ...]) -> int:
    x = word
    t = 0
    while step(x) != x:
        x = step(x)
        t += 1
        assert t <= len(word) + 1
    return t


def fixed_prefix_length(word: tuple[int, ...]) -> int:
    image = step(word)
    for i, (left, right) in enumerate(zip(word, image)):
        if left != right:
            return i
    return len(word)


def locked_prefix_data(prefix: tuple[int, ...]) -> tuple[int, int, int]:
    """Return alternating-core length, locked bit, locked length."""
    r = 0
    while 2 * r + 1 < len(prefix) and prefix[2 * r : 2 * r + 2] == (0, 1):
        r += 1
    core = 2 * r
    assert core < len(prefix)
    bit = prefix[core]
    assert all(x == bit for x in prefix[core:])
    return core, bit, len(prefix) - core


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


ASSERTIONS = 0


def audit_length(n: int) -> str:
    global ASSERTIONS
    fibre: Counter[tuple[int, ...]] = Counter()
    depth: Counter[int] = Counter()
    fixed = fixed_words(n)
    maximum_tail = 0

    for word in product((0, 1), repeat=n):
        image = step(word)
        fibre[image] += 1
        tau = tail(word)
        depth[tau] += 1
        maximum_tail = max(maximum_tail, tau)

        assert (image == word) == (word in fixed)
        ASSERTIONS += 1

        prefix_length = fixed_prefix_length(word)
        if prefix_length < n:
            assert prefix_length >= (1 if word[0] else 2)
            core, bit, locked = locked_prefix_data(word[:prefix_length])
            if bit:
                lower = min(n, core + 2 * locked)
            else:
                assert locked >= 2
                lower = min(n, core + 2 * locked - 1)
            next_prefix = fixed_prefix_length(image)
            assert next_prefix >= lower
            ASSERTIONS += 3
            if next_prefix < n:
                next_core, next_bit, _ = locked_prefix_data(image[:next_prefix])
                assert (next_core, next_bit) == (core, bit)
                ASSERTIONS += 1

    assert len(fixed) == n + 1
    assert len(fibre) == fib(n + 2)
    assert maximum_tail == ceil(log2(n))
    ASSERTIONS += 3

    predicted_image = 0
    maximum_fibre = 0
    maximizers = []
    for target in product((0, 1), repeat=n):
        predicted = predicted_fibre(target)
        actual = fibre[target]
        assert actual == predicted
        ASSERTIONS += 1
        predicted_image += int(predicted > 0)
        if actual > maximum_fibre:
            maximum_fibre = actual
            maximizers = [target]
        elif actual == maximum_fibre:
            maximizers.append(target)

    assert predicted_image == fib(n + 2)
    assert maximum_fibre == comb(n, n // 2)
    assert n == 1 or maximizers == [(1,) * n]
    ASSERTIONS += 3

    return (
        f"n={n};states={2**n};image={len(fibre)};fixed={len(fixed)};"
        f"tail={maximum_tail};maxfibre={maximum_fibre};"
        f"depth={sorted(depth.items())}"
    )


def main() -> None:
    global ASSERTIONS
    signatures = [audit_length(n) for n in range(1, 20)]
    ASSERTIONS += 3
    assert sum(2**n for n in range(1, 20)) == 1_048_574
    assert signatures[-1].startswith("n=19;states=524288;")
    assert all("tail=" in line for line in signatures)
    digest = sha256("\n".join(signatures).encode()).hexdigest()

    print("SYNCHRONOUS PREFIX-MAJORITY DYNAMICS — EXACT SCOUT")
    print("lengths=1..19")
    print("states=1048574")
    print(f"assertions={ASSERTIONS}")
    print(f"signature_sha256={digest}")
    print("selected_lengths:")
    for n in (1, 5, 9, 16, 19):
        print(signatures[n - 1])
    print("RESULT: PASS")


if __name__ == "__main__":
    main()
