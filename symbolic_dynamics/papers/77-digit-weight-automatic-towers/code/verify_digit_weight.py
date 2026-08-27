#!/usr/bin/env python3
"""Deterministic finite controls for the digit-weight tower paper.

The proofs are all-scale arguments.  This script checks four finite shadows:

1. centering at several phased, nonconsecutive escaping digit sets removes
   exactly those digits in a fixed observation window;
2. the lowering maps obey truncated addition with an absorbing zero;
3. the divisibility step in bounded-difference rigidity has no small
   counterexample; and
4. unequal bases have a finite return-scale mismatch in at least one
   direction, including perfect-power containment cases.
"""

from itertools import combinations


def power_sum(q, exponents):
    return sum(q**exponent for exponent in exponents)


def digit_weight_support(q, d, largest_exponent):
    if d == 0:
        return {0}
    return {
        power_sum(q, chosen)
        for chosen in combinations(range(largest_exponent + 1), d)
    }


def escaping_patterns(first_high, count):
    if count == 0:
        return [()]
    pools = (
        tuple(range(first_high, first_high + 2 * count + 2)),
        tuple(range(first_high, first_high + 3 * count + 3, 2)),
    )
    patterns = []
    for pool in pools:
        patterns.extend(combinations(pool, count))
    return sorted(set(patterns))[:8]


def check_centered_limits():
    checks = 0
    rows = []
    for q in (2, 3, 4):
        for d in (1, 2, 3, 4):
            for retained in range(d + 1):
                radius = 2 * q ** (retained + 2)
                first_high = 11
                for escaping in escaping_patterns(first_high, d - retained):
                    largest = max(escaping, default=first_high) + 2
                    source = digit_weight_support(q, d, largest)
                    target = digit_weight_support(q, retained, retained + 9)
                    for phase in (-3, -1, 0, 2, 4):
                        center = power_sum(q, escaping) + phase
                        observed = {
                            offset
                            for offset in range(-radius, radius + 1)
                            if center + offset in source
                        }
                        expected = {
                            offset
                            for offset in range(-radius, radius + 1)
                            if phase + offset in target
                        }
                        assert observed == expected, (
                            q,
                            d,
                            retained,
                            escaping,
                            phase,
                            observed ^ expected,
                        )
                        checks += 1
                        rows.append(
                            (q, d, retained, len(escaping), phase, len(observed))
                        )
    return checks, rows


def lowering(layer, amount):
    return layer - amount if layer >= amount else None


def check_lowering_monoid():
    checks = 0
    for d in range(1, 10):
        for layer in range(d + 1):
            for first in range(d + 2):
                for second in range(d + 2):
                    intermediate = lowering(layer, second)
                    composed = (
                        None
                        if intermediate is None
                        else lowering(intermediate, first)
                    )
                    direct = lowering(layer, first + second)
                    assert composed == direct
                    checks += 1
    return checks


def check_bounded_difference_divisibility():
    """Check the finite divisibility core of Lemma 3.1.

    If all exponents in the symmetric difference are at least r, the
    difference is divisible by q**r.  If its absolute value is smaller than
    q**r, it must vanish, and injectivity then forces equal sets.
    """

    checks = 0
    for q in (2, 3, 4, 5):
        universe = range(9)
        subsets = [
            frozenset(chosen)
            for size in range(5)
            for chosen in combinations(universe, size)
        ]
        for left in subsets:
            for right in subsets:
                symmetric = left ^ right
                if not symmetric:
                    continue
                least = min(symmetric)
                difference = power_sum(q, left) - power_sum(q, right)
                assert difference % (q**least) == 0
                assert abs(difference) >= q**least
                checks += 1
    return checks


def check_return_scale_separation():
    checks = 0
    witnesses = []
    for q in range(2, 9):
        for p in range(q + 1, 9):
            q_tail = {q**n for n in range(4, 14)}
            p_all = {p**n for n in range(1, 64)}
            missing = sorted(q_tail - p_all)
            direction = f"{q}->{p}"
            if not missing:
                p_tail = {p**n for n in range(4, 14)}
                q_all = {q**n for n in range(1, 64)}
                missing = sorted(p_tail - q_all)
                direction = f"{p}->{q}"
            assert missing
            witnesses.append((direction, missing[0]))
            checks += 1
    return checks, witnesses


def main():
    centered_checks, rows = check_centered_limits()
    monoid_checks = check_lowering_monoid()
    divisibility_checks = check_bounded_difference_divisibility()
    rigidity_checks, witnesses = check_return_scale_separation()
    print(f"PASS phased centered-window checks: {centered_checks}")
    print(f"PASS lowering-composition checks: {monoid_checks}")
    print(f"PASS bounded-difference divisibility checks: {divisibility_checks}")
    print(f"PASS finite return-scale separations: {rigidity_checks}")
    print("sample centered rows:", rows[:8])
    print("sample base-separation witnesses:", witnesses[:8])


if __name__ == "__main__":
    main()
