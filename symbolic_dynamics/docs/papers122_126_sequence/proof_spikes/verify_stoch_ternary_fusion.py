#!/usr/bin/env python3
"""Independent exact verifier for oriented ternary fusion.

The rewrite search and the maximal-matching/composition model are implemented
separately and compared.  Redex occurrences, rather than distinct child words,
are counted as distinct unweighted history choices.
"""

from collections import Counter
from functools import lru_cache
from math import comb, factorial


ASSERTIONS = 0


def check(condition, context):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(context)


def successors(word):
    """Literal occurrences for i,(i+1) -> i+2 over Z/3Z."""
    out = []
    for position in range(len(word) - 1):
        left = int(word[position])
        right = int(word[position + 1])
        if right == (left + 1) % 3:
            parent = str((left + 2) % 3)
            out.append(word[:position] + parent + word[position + 2 :])
    return tuple(out)


@lru_cache(None)
def rewrite_support(word):
    children = set(successors(word))
    if not children:
        return frozenset((word,))
    answer = set()
    for child in children:
        answer.update(rewrite_support(child))
    return frozenset(answer)


@lru_cache(None)
def history_total(word):
    children = successors(word)
    if not children:
        return 1
    return sum(history_total(child) for child in children)


@lru_cache(None)
def history_fibres(word):
    """Terminal -> occurrence-distinguished history count."""
    children = successors(word)
    if not children:
        return ((word, 1),)
    counts = Counter()
    for child in children:  # keep repeated child states as different choices
        counts.update(dict(history_fibres(child)))
    return tuple(sorted(counts.items()))


@lru_cache(None)
def compositions(total, previous_one=False):
    """Compositions into 1 and 2 with no adjacent 1 parts."""
    if total == 0:
        return ((),)
    out = []
    if total >= 2:
        out.extend((2,) + rest for rest in compositions(total - 2, False))
    if total >= 1 and not previous_one:
        out.extend((1,) + rest for rest in compositions(total - 1, True))
    return tuple(out)


def terminal_from_composition(parts):
    position = 0
    output = []
    for part in parts:
        start = position % 3
        output.append(str(start if part == 1 else (start + 2) % 3))
        position += part
    return "".join(output)


def recover_composition(terminal, original_length):
    position = 0
    parts = []
    for symbol in terminal:
        value = int(symbol)
        if value == position % 3:
            part = 1
        elif value == (position + 2) % 3:
            part = 2
        else:
            return None
        parts.append(part)
        position += part
    if position != original_length:
        return None
    return tuple(parts)


@lru_cache(None)
def singleton_results(start, length):
    """All labels obtainable by fully fusing a periodic interval."""
    if length == 1:
        return frozenset((start,))
    out = set()
    for left_length in range(1, length):
        right_start = (start + left_length) % 3
        for left in singleton_results(start, left_length):
            for right in singleton_results(right_start, length - left_length):
                if right == (left + 1) % 3:
                    out.add((left + 2) % 3)
    return frozenset(out)


def support_formula(n):
    return sum(
        comb(m + 1, n - 2 * m)
        for m in range((n - 1 + 2) // 3, n // 2 + 1)
        if 0 <= n - 2 * m <= m + 1
    ) if n else 1


def history_formula(n):
    return sum(
        comb(m + 1, n - 2 * m) * factorial(m)
        for m in range((n - 1 + 2) // 3, n // 2 + 1)
        if 0 <= n - 2 * m <= m + 1
    ) if n else 1


def length_profile(n):
    profile = Counter()
    for m in range(0, n // 2 + 1):
        r = n - 2 * m
        if 0 <= r <= m + 1:
            profile[n - m] += comb(m + 1, r)
    return tuple(sorted(profile.items()))


def xor_value(word):
    values = (1, 2, 3)
    answer = 0
    for symbol in word:
        answer ^= values[int(symbol)]
    return answer


def main():
    # Independent bracketing control for the key no-large-block lemma.
    for start in range(3):
        for length in range(1, 31):
            expected = (
                frozenset((start,))
                if length == 1
                else frozenset(((start + 2) % 3,))
                if length == 2
                else frozenset()
            )
            check(singleton_results(start, length) == expected,
                  ("periodic interval", start, length))

    support_counts = []
    history_counts = []
    profiles = []

    # Literal rewrite DAG versus the independently generated grammar.
    for k in range(0, 10):
        n = 3 * k
        word = "012" * k
        grammar = {
            terminal_from_composition(parts): parts
            for parts in compositions(n, False)
        }
        check(len(grammar) == len(compositions(n, False)),
              ("injective grammar", k))
        literal = rewrite_support(word)
        check(literal == frozenset(grammar), ("support equality", k))
        check(len(literal) == support_formula(n), ("support formula", k))
        for terminal, parts in grammar.items():
            check(recover_composition(terminal, n) == parts,
                  ("inverse grammar", k, terminal))
            check(not successors(terminal), ("irreducible", k, terminal))
            check(xor_value(terminal) == xor_value(word),
                  ("xor", k, terminal))
        support_counts.append(len(literal))
        histories = history_total(word)
        check(histories == history_formula(n), ("history total", k))
        history_counts.append(histories)
        profiles.append(length_profile(n))

    # Direct terminal-fibre checks are more expensive; k<=6 still covers
    # every characteristic matching size and 114 distinct endpoints at k=6.
    for k in range(0, 7):
        n = 3 * k
        fibres = dict(history_fibres("012" * k))
        check(set(fibres) == set(rewrite_support("012" * k)),
              ("fibre support", k))
        for terminal, count in fibres.items():
            parts = recover_composition(terminal, n)
            dimers = parts.count(2)
            check(count == factorial(dimers),
                  ("factorial fibre", k, terminal, count, dimers))

    # Closed formulas, the b_n recurrence, and the 3-section recurrence.
    b = [support_formula(n) for n in range(91)]
    check(b[:7] == [1, 1, 1, 2, 2, 3, 4], "initial b_n")
    for n in range(3, len(b)):
        check(b[n] == b[n - 2] + b[n - 3], ("b recurrence", n))
    a = [b[3 * k] for k in range(31)]
    check(a[:10] == support_counts, "literal/formula support prefix")
    for k in range(3, len(a)):
        check(a[k] == 3 * a[k - 1] - 2 * a[k - 2] + a[k - 3],
              ("a recurrence", k))

    expected_histories = [
        2,
        12,
        144,
        2640,
        66240,
        2172240,
        88583040,
        4387582080,
        256987987200,
    ]
    check(history_counts[1:] == expected_histories, "history prefix")

    print("oriented ternary fusion verifier: PASS")
    print(f"assertions={ASSERTIONS}")
    print("literal_rewrite_support_k=0..9 " + ",".join(map(str, support_counts)))
    print("support_recurrence=a_k=3a_(k-1)-2a_(k-2)+a_(k-3)")
    print("support_gf=(1-z)/(1-3z+2z^2-z^3), a_0=1")
    print("composition_gf=(1+x)/(1-u*x^2-u*x^3)")
    print("history_counts_k=1..9 " + ",".join(map(str, history_counts[1:])))
    print("history_fibre=terminal_with_m_dimers_has_m!_histories checked_k<=6")
    print("periodic_singleton_blocks=only_lengths_1_and_2 checked_start=0,1,2_length<=30")
    print("length_profile_k=6 " + str(profiles[6]))


if __name__ == "__main__":
    main()
