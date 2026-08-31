#!/usr/bin/env python3
"""Paper-local exact verifier for rootward active-pile coalescence.

All probabilities and expectations use fractions.Fraction.  The program has
no randomness, floating point, timestamp, network access, or third-party
dependency.  The maximum-time endpoint check is deliberately labelled
PILOT_ONLY and is not part of the manuscript theorem contract.
"""

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial


ASSERTIONS = 0


def check(condition, message="exact check failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def potential(mask, n):
    return sum(v for v in range(n) if (mask >> v) & 1)


def maximum(mask):
    return mask.bit_length() - 1


def successors(mask, n):
    out = []
    for v in range(1, n):
        if (mask >> v) & 1:
            out.append((mask & ~(1 << v)) | (1 << (v - 1)))
    return tuple(out)


@lru_cache(None)
def expected_steps(n, mask):
    if mask == 1:
        return Fraction(0)
    out = successors(mask, n)
    return Fraction(1) + sum(
        (expected_steps(n, target) for target in out), Fraction()
    ) / len(out)


@lru_cache(None)
def hitting_distribution(n, mask):
    if mask == 1:
        return ((0, Fraction(1)),)
    out = successors(mask, n)
    law = defaultdict(Fraction)
    for target in out:
        for time, probability in hitting_distribution(n, target):
            law[time + 1] += probability / len(out)
    return tuple(sorted(law.items()))


@lru_cache(None)
def pair_mean(a, b):
    if a == b:
        return Fraction(0)
    if a == 0:
        return Fraction(b)
    return Fraction(1, 2) + (
        pair_mean(a - 1, b) + pair_mean(a, b - 1)
    ) / 2


def double_factorial(value):
    answer = 1
    while value > 1:
        answer *= value
        value -= 2
    return answer


def interface_sum(mask, n):
    positions = [v for v in range(n) if (mask >> v) & 1]
    return sum(
        (pair_mean(a, b) for a, b in zip(positions, positions[1:])),
        Fraction(),
    )


def catalan(j):
    return comb(2 * j, j) // (j + 1)


def ballot_adjacent_mean(m):
    """Independent stopped-event ballot sum for h(m-1,m)."""
    if m == 1:
        return Fraction(1)
    p = m - 1
    meeting = sum(
        (
            Fraction(catalan(j), 2 ** (2 * j + 1))
            * Fraction(2 * j + 1, 2)
            for j in range(p)
        ),
        Fraction(),
    )
    root_exit = Fraction()
    for q in range(p):
        reflected = comb(p + q - 1, q)
        if q:
            reflected -= comb(p + q - 1, q - 1)
        probability = Fraction(reflected, 2 ** (p + q))
        elapsed = Fraction(p + q, 2)
        residual = p + 1 - q
        root_exit += probability * (elapsed + residual)
    return meeting + root_exit


def verify_transition_and_mean_range():
    rooted_states = 0
    transitions = 0
    for n in range(1, 15):
        for mask in range(1, 1 << n, 2):
            rooted_states += 1
            out = successors(mask, n)
            check(bool(out) == (mask != 1))
            if mask == 1:
                check(expected_steps(n, mask) == 0)
                check(interface_sum(mask, n) == 0)
                continue

            active = mask.bit_count() - 1
            check(len(out) == active)
            check(len(set(out)) == len(out))
            check(sum((Fraction(1, active) for _ in out), Fraction()) == 1)
            source_potential = potential(mask, n)
            source_maximum = maximum(mask)
            for target in out:
                transitions += 1
                check(target & 1)
                check(potential(target, n) < source_potential)
                check(maximum(target) >= source_maximum - 1)
                check(maximum(target) <= source_maximum)

            bellman = Fraction(1) + sum(
                (expected_steps(n, target) for target in out), Fraction()
            ) / active
            check(expected_steps(n, mask) == bellman)
            check(expected_steps(n, mask) == interface_sum(mask, n))

    check(rooted_states == (1 << 14) - 1)
    return rooted_states, transitions


def verify_pair_triangle():
    pair_states = 0
    for b in range(0, 81):
        for a in range(0, b + 1):
            pair_states += 1
            value = pair_mean(a, b)
            check(value >= 0)
            if a == b:
                check(value == 0)
            elif a == 0:
                check(value == b)
            else:
                check(
                    value
                    == Fraction(1, 2)
                    + (pair_mean(a - 1, b) + pair_mean(a, b - 1)) / 2
                )

    for m in range(1, 81):
        predicted = Fraction(
            double_factorial(2 * m - 1),
            double_factorial(2 * m - 2),
        )
        central = Fraction(2 * m * comb(2 * m, m), 4**m)
        check(pair_mean(m - 1, m) == predicted)
        check(predicted == central)
        check(ballot_adjacent_mean(m) == predicted)
        if m < 80:
            check(2 * m * pair_mean(m, m + 1) == (2 * m + 1) * predicted)
    return pair_states


def verify_all_rooted_distributions():
    distribution_states = 0
    for n in range(1, 12):
        for mask in range(1, 1 << n, 2):
            distribution_states += 1
            law = dict(hitting_distribution(n, mask))
            check(sum(law.values(), Fraction()) == 1)
            mean = sum(
                (time * probability for time, probability in law.items()),
                Fraction(),
            )
            check(mean == expected_steps(n, mask))
            if mask == 1:
                check(law == {0: Fraction(1)})
            else:
                check(
                    set(law)
                    == set(range(maximum(mask), potential(mask, n) + 1))
                )
                check(all(probability > 0 for probability in law.values()))
    check(distribution_states == (1 << 11) - 1)
    return distribution_states


def verify_full_start_laws():
    for n in range(1, 12):
        mask = (1 << n) - 1
        law = dict(hitting_distribution(n, mask))
        predicted_mean = sum(
            (
                Fraction(
                    double_factorial(2 * m - 1),
                    double_factorial(2 * m - 2),
                )
                for m in range(1, n)
            ),
            Fraction(),
        )
        actual_mean = sum(
            (time * probability for time, probability in law.items()),
            Fraction(),
        )
        check(actual_mean == predicted_mean)
        check(actual_mean == interface_sum(mask, n))
        if n == 1:
            check(law == {0: Fraction(1)})
        else:
            check(law[n - 1] == Fraction(1, factorial(n - 1)))
            # This upper-endpoint pattern remains pilot-only and is not a
            # manuscript theorem or a contributor to the GO decision.
            check(
                law[comb(n, 2)]
                == Fraction(1, 2 ** comb(n - 1, 2))
            )


def main():
    rooted_states, transitions = verify_transition_and_mean_range()
    pair_states = verify_pair_triangle()
    distribution_states = verify_all_rooted_distributions()
    verify_full_start_laws()

    # Fixed ledger assertions make accidental range drift visible.
    check(rooted_states == 16383)
    check(distribution_states == 2047)
    check(pair_states == 3321)
    check(transitions == 98305)

    print("P129 rootward active-pile exact verifier: PASS")
    print("arithmetic=integer+Fraction; randomness=none; floating_point=none")
    print(
        f"rooted_mean_range=n=1..14; rooted_states={rooted_states}; "
        f"transitions={transitions}"
    )
    print(
        f"rooted_distribution_range=n=1..11; "
        f"rooted_states={distribution_states}"
    )
    print(f"pair_recurrence_range=0<=a<=b<=80; pair_states={pair_states}")
    print("adjacent_ballot_range=m=1..80")
    print("full_start_exact_law_range=n=1..11")
    print("pilot_only_maximum_endpoint=n=2..11; MANUSCRIPT_CLAIM=NO")
    print("claims=C1,C2,C3,C4,C5,C6,C7,C8")
    print(f"assertions={ASSERTIONS}")
    print("external_status=HOLD")


if __name__ == "__main__":
    main()
