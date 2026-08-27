#!/usr/bin/env python3
"""Finite hostile checks for the digit-weight automatic-shift contract.

The proof in the paper is an all-scale centered-limit argument.  This program
checks its two fragile finite shadows: centering at escaping base-q digits
really removes exactly those digits in a fixed observation window, and the
proposed lowering maps have the claimed truncated-addition composition law.
"""

from itertools import combinations


def digit_weight_support(q, d, largest_exponent):
    if d == 0:
        return {0}
    return {
        sum(q**exponent for exponent in chosen)
        for chosen in combinations(range(largest_exponent + 1), d)
    }


def check_centered_limits():
    checks = 0
    rows = []
    for q in (2, 3, 4):
        for d in (1, 2, 3, 4):
            for retained in range(d + 1):
                radius = 3 * q ** (retained + 2)
                first_high = 12
                escaping = tuple(range(first_high, first_high + d - retained))
                center = sum(q**exponent for exponent in escaping)
                largest = first_high + d + 2
                source = digit_weight_support(q, d, largest)
                target = digit_weight_support(q, retained, retained + 8)
                observed = {
                    offset
                    for offset in range(-radius, radius + 1)
                    if center + offset in source
                }
                expected = {offset for offset in target if -radius <= offset <= radius}
                assert observed == expected, (q, d, retained, observed ^ expected)
                checks += 1
                rows.append((q, d, retained, len(observed)))
    return checks, rows


def lowering(layer, amount):
    return layer - amount if layer >= amount else None


def check_lowering_monoid():
    checks = 0
    for d in range(1, 9):
        for layer in range(d + 1):
            for r in range(d + 1):
                for s in range(d + 1):
                    first = lowering(layer, s)
                    composed = None if first is None else lowering(first, r)
                    direct = lowering(layer, r + s)
                    assert composed == direct
                    checks += 1
    return checks


def check_return_scale_separation():
    """Finite witness for why different bases cannot share every return scale."""

    checks = 0
    witnesses = []
    for q in range(2, 7):
        for r in range(q + 1, 7):
            q_tail = {q**n for n in range(4, 13)}
            r_all = {r**n for n in range(1, 49)}
            missing = sorted(q_tail - r_all)
            direction = f"{q}->{r}"
            if not missing:
                # Perfect-power containment can occur in one direction (for
                # example 4^N=2^(2N)), but never in both directions unless
                # the integer bases agree.  The inverse conjugacy is what
                # supplies the second direction in the theorem proof.
                r_tail = {r**n for n in range(4, 13)}
                q_all = {q**n for n in range(1, 49)}
                missing = sorted(r_tail - q_all)
                direction = f"{r}->{q}"
            assert missing
            witnesses.append((direction, missing[0]))
            checks += 1
    return checks, witnesses


def main():
    limit_checks, rows = check_centered_limits()
    monoid_checks = check_lowering_monoid()
    rigidity_checks, witnesses = check_return_scale_separation()
    print(f"PASS centered-window checks: {limit_checks}")
    print(f"PASS lowering-composition checks: {monoid_checks}")
    print(f"PASS finite return-scale separations: {rigidity_checks}")
    print("sample centered rows (q,d,retained,visible ones):", rows[:8])
    print("sample bidirectional base-separation witnesses (direction,power):", witnesses[:8])


if __name__ == "__main__":
    main()
