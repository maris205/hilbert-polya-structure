#!/usr/bin/env python3
"""Deterministic exact verifier for P139.

Every binary functional graph is exhausted through length 18.  The ordered
Lyndon fibre formula is independently checked against literal fibres for every
target through length 14, and both closed special fibres are checked through
length 18.
"""

from bisect import bisect_left
from collections import Counter
from functools import lru_cache


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def bits(value, n):
    return tuple((value >> (n - 1 - i)) & 1 for i in range(n))


def integer(word):
    value = 0
    for bit in word:
        value = 2 * value + bit
    return value


def duval_start_mask(word):
    n = len(word)
    out = [0] * n
    i = 0
    while i < n:
        j = i + 1
        k = i
        while j < n and word[k] <= word[j]:
            if word[k] < word[j]:
                k = i
            else:
                k += 1
            j += 1
        period = j - k
        while i <= k:
            out[i] = 1
            i += period
    return tuple(out)


def suffix_record_mask(word):
    out = []
    best = None
    for i in range(len(word)):
        suffix = word[i:]
        record = best is None or suffix < best
        out.append(int(record))
        if record:
            best = suffix
    return tuple(out)


def step(value, n):
    return integer(duval_start_mask(bits(value, n)))


def leading_ones(word):
    count = 0
    for bit in word:
        if bit != 1:
            break
        count += 1
    return count


def classify(n):
    size = 1 << n
    nxt = [step(state, n) for state in range(size)]
    info = {}
    cycles = Counter()
    for start in range(size):
        if start in info:
            continue
        path = []
        position = {}
        state = start
        while state not in position and state not in info:
            position[state] = len(path)
            path.append(state)
            state = nxt[state]
        if state in position:
            split = position[state]
            period = len(path) - split
            cycles[period] += 1
            for i, vertex in enumerate(path):
                info[vertex] = (max(split - i, 0), period)
        else:
            old_tail, period = info[state]
            for i, vertex in enumerate(path):
                info[vertex] = (len(path) - i + old_tail, period)
    return nxt, info, cycles


def alternating_word(n):
    return tuple(i & 1 for i in range(n))


def mobius(n):
    value = n
    primes = 0
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            primes += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        primes += 1
    return -1 if primes % 2 else 1


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def binary_lyndon_count(n):
    return sum(mobius(d) * (2 ** (n // d)) for d in divisors(n)) // n


def is_lyndon(word):
    return all(word < word[i:] for i in range(1, len(word)))


@lru_cache(None)
def lyndon_words(length):
    return tuple(
        word for word in (bits(value, length) for value in range(1 << length))
        if is_lyndon(word)
    )


def factor_lengths(mask):
    if not mask or mask[0] != 1:
        return None
    starts = [i for i, bit in enumerate(mask) if bit]
    return tuple(
        (starts[i + 1] if i + 1 < len(starts) else len(mask)) - start
        for i, start in enumerate(starts)
    )


def ordered_lyndon_count(mask):
    """Rectangular comparison-matrix product, evaluated by suffix sums."""
    lengths = factor_lengths(mask)
    if lengths is None:
        return 0
    previous_words = lyndon_words(lengths[0])
    counts = [1] * len(previous_words)
    for length in lengths[1:]:
        current_words = lyndon_words(length)
        suffix_sums = [0] * (len(counts) + 1)
        for i in range(len(counts) - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + counts[i]
        next_counts = [
            suffix_sums[bisect_left(previous_words, word)]
            for word in current_words
        ]
        previous_words = current_words
        counts = next_counts
    return sum(counts)


def main():
    total_states = 0
    image_profile = []
    fibre_profile = []

    for n in range(1, 19):
        size = 1 << n
        total_states += size
        nxt, info, cycles = classify(n)
        fibres = Counter(nxt)
        all_ones = size - 1

        for state in range(size):
            word = bits(state, n)
            image = bits(nxt[state], n)
            check(duval_start_mask(word) == suffix_record_mask(word),
                  "CFL/suffix-record equivalence failed")
            check(image[0] == 1, "first factor start missing")
            check(info[state][1] == 1, "unexpected period")
            check(info[state][0] <= n, "clock bound failed")
            run = leading_ones(word)
            if run < n:
                check(leading_ones(image) >= run + 1,
                      "leading-one amplifier failed")

        max_tail = max(tail for tail, _ in info.values())
        deepest = [state for state, (tail, _) in info.items() if tail == max_tail]
        recurrent = {state for state, (tail, _) in info.items() if tail == 0}
        check(max_tail == n, "sharp clock failed")
        check(deepest == [integer(alternating_word(n))],
              "unique deepest source failed")
        check(recurrent == {all_ones}, "fixed/recurrent atlas failed")
        check(cycles == Counter({1: 1}), "cycle census failed")
        check(fibres[1 << (n - 1)] == binary_lyndon_count(n),
              "single-factor special fibre failed")
        check(fibres[all_ones] == n + 1,
              "all-starts special fibre failed")

        if n <= 14:
            check(len(lyndon_words(n)) == binary_lyndon_count(n),
                  "independent Lyndon census failed")
            for target in range(size):
                check(ordered_lyndon_count(bits(target, n)) == fibres[target],
                      "ordered-Lyndon fibre formula failed")

        image_profile.append(len(fibres))
        fibre_profile.append(max(fibres.values()))
        print(
            f"n={n:2d} states={size:6d} image={len(fibres):5d} "
            f"cycles={dict(cycles)} max_tail={max_tail:2d} "
            f"max_fibre={max(fibres.values()):5d} unique_deep=1"
        )

    print("IMAGE_PROFILE=" + ",".join(map(str, image_profile)))
    print("MAX_FIBRE_PROFILE=" + ",".join(map(str, fibre_profile)))
    print(f"TOTAL_EXHAUSTIVE_STATES={total_states}")
    print("ORDERED_FIBRES_EXHAUSTIVE_THROUGH=14")
    print("SPECIAL_FIBRES_CHECKED_THROUGH=18")
    print(f"EXACT_ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
