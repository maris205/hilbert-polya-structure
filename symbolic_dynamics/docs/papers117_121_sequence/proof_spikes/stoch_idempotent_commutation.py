#!/usr/bin/env python3
"""Exact pilot for the random-redex system BA->AB, AA->A.

Only the Python standard library is used.  Every probability is a Fraction.
The program is a falsification control, not evidence of novelty.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def redex_successors(word):
    """One successor per redex occurrence; duplicates retain multiplicity."""
    out = []
    for i in range(len(word) - 1):
        pair = word[i : i + 2]
        if pair == "BA":
            out.append(("swap", i, word[:i] + "AB" + word[i + 2 :]))
        if pair == "AA":
            out.append(("delete", i, word[:i] + "A" + word[i + 2 :]))
    return tuple(out)


def expected_normal_form(word):
    suffix = "B" * word.count("B")
    return ("A" + suffix) if "A" in word else suffix


@lru_cache(maxsize=None)
def terminal_forms(word):
    moves = redex_successors(word)
    if not moves:
        return frozenset((word,))
    answer = set()
    for _, _, nxt in moves:
        answer.update(terminal_forms(nxt))
    return frozenset(answer)


@lru_cache(maxsize=None)
def absorption_law(word):
    moves = redex_successors(word)
    if not moves:
        return {0: Fraction(1)}
    answer = {}
    weight = Fraction(1, len(moves))
    for _, _, nxt in moves:
        for time, probability in absorption_law(nxt).items():
            answer[time + 1] = answer.get(time + 1, Fraction(0)) + weight * probability
    return dict(sorted(answer.items()))


def all_words(length):
    return ("".join(bits) for bits in product("AB", repeat=length))


def run():
    # Exhaustive termination/confluence/orientation gate.
    for length in range(9):
        for word in all_words(length):
            forms = terminal_forms(word)
            check(forms == frozenset((expected_normal_form(word),)), (word, forms))
            law = absorption_law(word)
            check(sum(law.values(), Fraction(0)) == 1, (word, law))
            check(all(time >= 0 and mass > 0 for time, mass in law.items()), (word, law))

    # Fixed-content fibres among all input words of length at most N.
    for bound in range(1, 10):
        words = [word for length in range(bound + 1) for word in all_words(length)]
        for b_count in range(bound):
            target = "A" + "B" * b_count
            actual = sum(expected_normal_form(word) == target for word in words)
            expected = comb(bound + 1, b_count + 1) - 1
            check(actual == expected, (bound, b_count, actual, expected))

    # The block family B^b A^a has an interval of attainable times.
    for a_count in range(1, 6):
        for b_count in range(7):
            word = "B" * b_count + "A" * a_count
            law = absorption_law(word)
            lower = a_count - 1 + b_count
            upper = a_count - 1 + a_count * b_count
            check(tuple(law) == tuple(range(lower, upper + 1)), (a_count, b_count, law))
            check(sum(law.values(), Fraction(0)) == 1, (a_count, b_count, law))
            if b_count:
                check(law[lower] == Fraction(1, a_count), (a_count, b_count, law[lower]))
            else:
                check(law == {a_count - 1: Fraction(1)}, (a_count, law))

    # Exact sentinels and deliberately falsified tempting simplifications.
    check(absorption_law("BAA") == {2: Fraction(1, 2), 3: Fraction(1, 2)}, "BAA")
    check(
        absorption_law("BBAA")
        == {3: Fraction(1, 2), 4: Fraction(1, 8), 5: Fraction(3, 8)},
        "BBAA",
    )
    check(len(absorption_law("BAA")) > 1, "time is not determined by content")
    check(
        len(set(absorption_law("BBAA").values())) > 1,
        "the interval law is not uniform",
    )

    print("stoch_idempotent_commutation: PASS")
    print(f"assertions={ASSERTIONS}")
    print("normal_form(A-present)=A B^#B")
    print("fibre_leq_N(A B^b)=binom(N+1,b+1)-1")
    print("block_support=[a+b-1, ab+a-1]")
    print("minimum_mass(b>0)=1/a")
    print("killed=time_determined_by_content, uniform_interval_law")


if __name__ == "__main__":
    run()
