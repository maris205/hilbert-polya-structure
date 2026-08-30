#!/usr/bin/env python3
"""Negative control: a two-generator Rees pair collapses to an XY motif count."""

from fractions import Fraction
from itertools import product
from math import comb


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def elements(modulus):
    return tuple((i_index, group, lam) for i_index in (0, 1) for group in range(modulus) for lam in (0, 1))


def multiply(left, right, modulus):
    i_index, group, lam = left
    j_index, other_group, mu = right
    sandwich = lam * j_index
    return (i_index, (group + sandwich + other_group) % modulus, mu)


def generators(modulus):
    del modulus
    return {"X": (0, 0, 1), "Y": (1, 0, 0)}


def word_product(word, modulus):
    gens = generators(modulus)
    answer = gens[word[0]]
    for letter in word[1:]:
        answer = multiply(answer, gens[letter], modulus)
    return answer


def xy_count(word):
    return sum(word[i : i + 2] == "XY" for i in range(len(word) - 1))


def expected_product(word, modulus):
    first_index = 0 if word[0] == "X" else 1
    last_lambda = 1 if word[-1] == "X" else 0
    return (first_index, xy_count(word) % modulus, last_lambda)


def phase_dp(length, modulus):
    if length == 1:
        return {("X", 0): 1, ("Y", 0): 1}
    states = {("X", 0): 1, ("Y", 0): 1}
    for _ in range(1, length):
        nxt = {}
        for (last, phase), count in states.items():
            for letter in "XY":
                new_phase = (phase + (last == "X" and letter == "Y")) % modulus
                key = (letter, new_phase)
                nxt[key] = nxt.get(key, 0) + count
        states = nxt
    return states


def run():
    # The displayed sandwich matrix really defines an associative Rees semigroup.
    for modulus in range(2, 7):
        carrier = elements(modulus)
        for left in carrier:
            for middle in carrier:
                for right in carrier:
                    check(
                        multiply(multiply(left, middle, modulus), right, modulus)
                        == multiply(left, multiply(middle, right, modulus), modulus),
                        (modulus, left, middle, right),
                    )

    # Literal products equal endpoint data plus the adjacent XY count.
    for modulus in range(2, 8):
        for length in range(1, 13):
            exhaustive_phase = {}
            for letters in product("XY", repeat=length):
                word = "".join(letters)
                actual = word_product(word, modulus)
                expected = expected_product(word, modulus)
                check(actual == expected, (modulus, word, actual, expected))
                phase = actual[1]
                exhaustive_phase[phase] = exhaustive_phase.get(phase, 0) + 1

            dp_phase = {}
            for (_, phase), count in phase_dp(length, modulus).items():
                dp_phase[phase] = dp_phase.get(phase, 0) + count
            check(exhaustive_phase == dp_phase, (modulus, length, exhaustive_phase, dp_phase))

    # The unwrapped motif law is a single binomial coefficient.
    for length in range(1, 18):
        histogram = {}
        for letters in product("XY", repeat=length):
            word = "".join(letters)
            count = xy_count(word)
            histogram[count] = histogram.get(count, 0) + 1
        expected = {
            count: comb(length + 1, 2 * count + 1)
            for count in range(length // 2 + 1)
        }
        check(histogram == expected, (length, histogram, expected))
        total = 2**length
        mean = sum(count * multiplicity for count, multiplicity in histogram.items()) / Fraction(total)
        check(mean == Fraction(max(0, length - 1), 4), (length, mean))
        variance = sum(
            (count - mean) ** 2 * multiplicity for count, multiplicity in histogram.items()
        ) / Fraction(total)
        expected_variance = Fraction(0) if length == 1 else Fraction(length + 1, 16)
        check(variance == expected_variance, (length, variance))

    check("XYXY".count("X") == "XXYY".count("X"), "same X count")
    check("XYXY".count("Y") == "XXYY".count("Y"), "same Y count")
    check(xy_count("XYXY") != xy_count("XXYY"), "phase is not a letter-count statistic")
    check(
        word_product("XYXY", 7)[1] == 2 and word_product("XXYY", 7)[1] == 1,
        "orientation sentinel",
    )

    print("stoch_rees_motif_kill: PASS")
    print(f"assertions={ASSERTIONS}")
    print("group_phase=#XY mod m")
    print("count_n(k)=binom(n+1,2k+1)")
    print("fair_mean=(n-1)/4; fair_variance=(n+1)/16 for n>=2")
    print("killed=nonlocal_Green_phase; reason=adjacent_motif_finite_memory")


if __name__ == "__main__":
    run()
