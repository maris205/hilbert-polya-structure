#!/usr/bin/env python3
"""Deterministic exact controls for the random cap--floor paper.

All theorem-bearing checks use integers or fractions.  The two exhaustive
lanes enumerate rank permutations, so they are independent of a particular
floating-point threshold sample.
"""

from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial


ASSERTIONS = 0


def check(condition, message="exact assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def update_state(state, kind, threshold):
    """Left-compose one cap/floor with an interval-or-constant state."""
    tag = state[0]
    if tag == "constant":
        value = state[1]
        return ("constant", max(value, threshold) if kind == "floor"
                else min(value, threshold))
    _, lower, upper = state
    if kind == "floor":
        if threshold < upper:
            return ("interval", max(lower, threshold), upper)
        return ("constant", threshold)
    if threshold > lower:
        return ("interval", lower, min(upper, threshold))
    return ("constant", threshold)


def direct_value(word, x):
    """Apply g_1 first and g_n last, exactly as in the manuscript."""
    value = x
    for kind, threshold in word:
        value = (max(value, threshold) if kind == "floor"
                 else min(value, threshold))
    return value


def state_value(state, x):
    if state[0] == "constant":
        return state[1]
    _, lower, upper = state
    return max(lower, min(x, upper))


def survival_sum(n, p):
    q = 1 - p
    return sum((p ** j) * (q ** (n - j)) for j in range(n + 1))


def composition_sentinel_lane():
    """A noncommuting two-map sentinel catches a reversed cocycle loop."""
    floor_then_cap = [("floor", 3), ("cap", 1)]
    cap_then_floor = [("cap", 1), ("floor", 3)]
    state_fc = ("interval", 0, 4)
    state_cf = ("interval", 0, 4)
    for kind, threshold in floor_then_cap:
        state_fc = update_state(state_fc, kind, threshold)
    for kind, threshold in cap_then_floor:
        state_cf = update_state(state_cf, kind, threshold)
    check(state_fc == ("constant", 1), "floor-then-cap sentinel failed")
    check(state_cf == ("constant", 3), "cap-then-floor sentinel failed")
    for x in range(5):
        check(direct_value(floor_then_cap, x) == 1,
              "floor-then-cap direct sentinel failed")
        check(direct_value(cap_then_floor, x) == 3,
              "cap-then-floor direct sentinel failed")
    check(state_fc != state_cf, "composition-order sentinel failed")
    return 13


def exhaustive_normal_form(max_n=7):
    environments = 0
    evaluations = 0
    summaries = {}
    for n in range(1, max_n + 1):
        scale = n + 1
        by_floors = {
            j: {"total": 0, "survivors": 0, "gap_sum": 0}
            for j in range(n + 1)
        }
        for bits in product((0, 1), repeat=n):  # 0=cap, 1=floor
            floor_count = sum(bits)
            for ranks in permutations(range(1, n + 1)):
                word = [
                    ("floor" if bit else "cap", rank)
                    for bit, rank in zip(bits, ranks)
                ]
                state = ("interval", 0, scale)
                for kind, rank in word:
                    state = update_state(state, kind, rank)

                lower_record = max(
                    [rank for (kind, rank) in word if kind == "floor"] or [0]
                )
                upper_record = min(
                    [rank for (kind, rank) in word if kind == "cap"] or [scale]
                )
                survives = lower_record < upper_record
                check((state[0] == "interval") == survives,
                      "crossing criterion mismatch")
                if survives:
                    check(state == ("interval", lower_record, upper_record),
                          "record endpoints mismatch")

                # Thresholds and endpoints contain all breakpoints of the word.
                for x in range(scale + 1):
                    check(direct_value(word, x) == state_value(state, x),
                          "chronological composition mismatch")
                    evaluations += 1

                bucket = by_floors[floor_count]
                bucket["total"] += 1
                if survives:
                    bucket["survivors"] += 1
                    bucket["gap_sum"] += upper_record - lower_record
                environments += 1

        for j, bucket in by_floors.items():
            check(bucket["total"] == comb(n, j) * factorial(n),
                  "type/rank total mismatch")
            check(bucket["survivors"] == factorial(n),
                  "aggregate survival count mismatch")
            check(bucket["gap_sum"] == factorial(n),
                  "aggregate spacing sum mismatch")

        for p in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
            q = 1 - p
            enumerated_survival = sum(
                Fraction(by_floors[j]["survivors"], factorial(n))
                * p ** j * q ** (n - j)
                for j in range(n + 1)
            )
            enumerated_diameter = sum(
                Fraction(by_floors[j]["gap_sum"], scale * factorial(n))
                * p ** j * q ** (n - j)
                for j in range(n + 1)
            )
            exact_survival = survival_sum(n, p)
            check(enumerated_survival == exact_survival,
                  "weighted survival mismatch")
            check(enumerated_diameter == exact_survival / scale,
                  "weighted diameter mismatch")
        summaries[n] = by_floors
    return environments, evaluations, summaries


def fixed_type_order_lane(max_n=8):
    permutation_cases = 0
    for n in range(1, max_n + 1):
        scale = n + 1
        total = factorial(n)
        for floor_count in range(n + 1):
            favorable = 0
            gap_sum = 0
            bits = (1,) * floor_count + (0,) * (n - floor_count)
            for ranks in permutations(range(1, n + 1)):
                floors = [rank for bit, rank in zip(bits, ranks) if bit]
                caps = [rank for bit, rank in zip(bits, ranks) if not bit]
                lower = max(floors or [0])
                upper = min(caps or [scale])
                if lower < upper:
                    favorable += 1
                    gap_sum += upper - lower
                permutation_cases += 1
            expected = factorial(floor_count) * factorial(n - floor_count)
            check(favorable == expected, "conditional favorable count mismatch")
            check(Fraction(favorable, total) == Fraction(1, comb(n, floor_count)),
                  "conditional survival probability mismatch")
            check(Fraction(gap_sum, scale * total)
                  == Fraction(1, scale * comb(n, floor_count)),
                  "conditional mean diameter mismatch")
    return permutation_cases


def law_lane():
    cases = 0
    parameters = (
        Fraction(1, 5), Fraction(1, 3), Fraction(1, 2),
        Fraction(2, 3), Fraction(4, 5),
    )
    for p in parameters:
        q = 1 - p
        for n in range(0, 61):
            s = survival_sum(n, p)
            check(s == q * (survival_sum(n - 1, p) if n else 0) + p ** n,
                  "survival recurrence mismatch")
            if p == q:
                check(s == Fraction(n + 1, 2 ** n),
                      "critical survival mismatch")
            else:
                check(s == (p ** (n + 1) - q ** (n + 1)) / (p - q),
                      "closed survival mismatch")
                r, a = max(p, q), min(p, q)
                check(s == r ** (n + 1) * (1 - (a / r) ** (n + 1)) / (r - a),
                      "off-critical form mismatch")
            cases += 1

        for m in range(2, 62):
            pmf_from_tail = survival_sum(m - 1, p) - survival_sum(m, p)
            convolution = p * q * sum(
                q ** i * p ** (m - 2 - i) for i in range(m - 1)
            )
            check(pmf_from_tail == convolution,
                  "geometric convolution mismatch")
            cases += 1

        for cutoff in range(2, 62):
            accumulated = sum(
                p * q * sum(q ** i * p ** (m - 2 - i)
                            for i in range(m - 1))
                for m in range(2, cutoff + 1)
            )
            check(accumulated + survival_sum(cutoff, p) == 1,
                  "convolution mass plus survival tail mismatch")

        check(Fraction(1, 1) / p + Fraction(1, 1) / q
              == Fraction(1, 1) / (p * q), "mean identity mismatch")
        check(q / (p * p) + p / (q * q)
              == (1 - 3 * p * q) / (p * p * q * q),
              "variance identity mismatch")

        # Coefficients of the rational survival generating function.
        coeffs = [survival_sum(n, p) for n in range(63)]
        for n in range(2, 63):
            check(coeffs[n] - coeffs[n - 1] + p * q * coeffs[n - 2] == 0,
                  "survival generating-function coefficient mismatch")
    return cases


def endpoint_lane():
    cases = 0
    for p in (Fraction(0), Fraction(1)):
        for n in range(0, 101):
            check(survival_sum(n, p) == 1, "endpoint survival mismatch")
            check(survival_sum(n, p) / (n + 1) == Fraction(1, n + 1),
                  "endpoint diameter mismatch")
            cases += 1
    return cases


def main():
    sentinel_cases = composition_sentinel_lane()
    environments, evaluations, _ = exhaustive_normal_form()
    conditional = fixed_type_order_lane()
    law_cases = law_lane()
    endpoint_cases = endpoint_lane()
    print("random cap-floor exact control: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"composition_sentinel_cases={sentinel_cases}")
    print(f"normal_form_environments={environments}")
    print(f"normal_form_evaluations={evaluations}")
    print(f"conditional_order_permutations={conditional}")
    print(f"law_cases={law_cases}")
    print(f"endpoint_cases={endpoint_cases}")


if __name__ == "__main__":
    main()
