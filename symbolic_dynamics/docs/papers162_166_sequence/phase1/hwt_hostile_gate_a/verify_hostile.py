#!/usr/bin/env python3
"""Independent hostile verifier for Hamming-weight translation dynamics.

No author or other reviewer code is imported.  The literal state map, the
occupancy-composition phase map, and the exponential-coefficient indegree
enumerator are implemented by separate routines using only the standard
library.
"""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import factorial, isqrt


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def decode_state(index, n):
    values = [0] * n
    for position in range(n - 1, -1, -1):
        values[position] = index % n
        index //= n
    return tuple(values)


def encode_state(state, n):
    value = 0
    for coordinate in state:
        value = value * n + coordinate
    return value


def literal_step(state, n):
    weight = sum(coordinate != 0 for coordinate in state)
    return tuple((coordinate + weight) % n for coordinate in state)


def multiplicities(state, n):
    counts = [0] * n
    for coordinate in state:
        counts[coordinate] += 1
    return tuple(counts)


def phase_step(profile, phase):
    return (phase + profile[phase]) % len(profile)


def phase_rho(profile, start):
    seen = {}
    phase = start
    time = 0
    while phase not in seen:
        seen[phase] = time
        phase = phase_step(profile, phase)
        time += 1
    return seen[phase], time - seen[phase]


def mapping_rho(mapping, start):
    seen = {}
    point = start
    time = 0
    while point not in seen:
        seen[point] = time
        point = mapping[point]
        time += 1
    return seen[point], time - seen[point]


@lru_cache(None)
def stirling_second(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    return stirling_second(n - 1, k - 1) + k * stirling_second(n - 1, k)


def expected_exact_period_points(n):
    answer = {1: 1 + (n - 1) ** n}
    for period in range(2, n + 1):
        answer[period] = factorial(period) * stirling_second(n, period)
    return answer


def ordered_bell(n):
    return sum(factorial(k) * stirling_second(n, k) for k in range(1, n + 1))


def target_fibre_from_profile(profile):
    n = len(profile)
    zero_branch = int(profile[0] == n)
    full_support_branch = int(profile[0] == 0)
    middle_branches = sum(profile[k] == n - k for k in range(1, n))
    return zero_branch + full_support_branch + middle_branches


def triangular_hit_number(n):
    # Largest h with h(h+1)/2 <= n.
    return (isqrt(8 * n + 1) - 1) // 2


def expected_max_fibre(n):
    return 1 if n == 2 else 1 + triangular_hit_number(n)


def target_oracle(profile, time):
    """Number of j with g_profile^time(j)=0."""
    n = len(profile)
    answer = 0
    for start in range(n):
        phase = start
        for _ in range(time):
            phase = phase_step(profile, phase)
        answer += phase == 0
    return answer


def weak_compositions(total, length, prefix=()):
    if length == 1:
        yield prefix + (total,)
        return
    for first in range(total + 1):
        yield from weak_compositions(total - first, length - 1, prefix + (first,))


def multinomial(profile):
    answer = factorial(sum(profile))
    for entry in profile:
        answer //= factorial(entry)
    return answer


def symbolic_indegree_enumerator(n):
    """Return coefficients of the formal EGF product in the gate report."""
    # Keys are (z-degree, u-degree), values are rational coefficients.
    polynomial = {(0, 1): Fraction(1)}
    for degree in range(1, n + 1):
        polynomial[(degree, 0)] = Fraction(1, factorial(degree))

    for required in range(1, n):
        factor = {
            (degree, 0): Fraction(1, factorial(degree))
            for degree in range(n + 1)
            if degree != required
        }
        factor[(required, 1)] = Fraction(1, factorial(required))
        product = {}
        for (z_left, u_left), left in polynomial.items():
            for (z_right, u_right), right in factor.items():
                if z_left + z_right <= n:
                    key = (z_left + z_right, u_left + u_right)
                    product[key] = product.get(key, Fraction(0)) + left * right
        polynomial = product

    answer = Counter()
    for (z_degree, u_degree), coefficient in polynomial.items():
        if z_degree == n:
            scaled = coefficient * factorial(n)
            check(scaled.denominator == 1)
            answer[u_degree] += scaled.numerator

    # The all-zero target was unmarked by the generic product; its special
    # k=0 branch replaces one u^0 contribution by u^1.
    answer[0] -= 1
    answer[1] += 1
    return +answer


def audit_cycle_geometry(profile):
    n = len(profile)
    support = {i for i, entry in enumerate(profile) if entry > 0}
    for start in range(n):
        depth, period = phase_rho(profile, start)
        check(depth <= max(0, n - 2), (profile, start, depth, period))
        if depth != 0:
            continue
        if period == 1:
            check(profile[start] in (0, n), (profile, start))
            continue
        cycle = []
        phase = start
        for _ in range(period):
            cycle.append(phase)
            phase = phase_step(profile, phase)
        check(phase == start)
        check(set(cycle) == support, (profile, start, cycle, support))
        check(sum(profile[i] for i in cycle) == n)
        ordered = sorted(support)
        for index in support:
            place = ordered.index(index)
            successor = ordered[(place + 1) % len(ordered)]
            gap = (successor - index) % n
            check(profile[index] == gap, (profile, index, successor))


def audit_literal_spaces():
    rows = []
    for n in range(2, 8):
        size = n ** n
        mapping = [0] * size
        profiles = [None] * size
        for index in range(size):
            state = decode_state(index, n)
            check(encode_state(state, n) == index)
            profile = multiplicities(state, n)
            profiles[index] = profile
            target = literal_step(state, n)
            mapping[index] = encode_state(target, n)

            # At the state anchored as phase zero, g(0)=m_0 and
            # X_j=state-j*1.
            reduced_target = tuple((coordinate - profile[0]) % n for coordinate in state)
            check(target == reduced_target, (n, state, target, reduced_target))

            # Coordinate differences are the strict diagonal-orbit invariant.
            for i in range(1, n):
                check(
                    (target[i] - target[0]) % n == (state[i] - state[0]) % n
                )

        indegrees = [0] * size
        for target in mapping:
            indegrees[target] += 1

        depth_histogram = Counter()
        exact_period = Counter()
        for index in range(size):
            depth, period = mapping_rho(mapping, index)
            check(depth <= max(0, n - 2))
            depth_histogram[depth] += 1
            if depth == 0:
                exact_period[period] += 1
            check(indegrees[index] == target_fibre_from_profile(profiles[index]))

        expected_periods = expected_exact_period_points(n)
        check(dict(sorted(exact_period.items())) == expected_periods)
        for period, point_count in expected_periods.items():
            check(point_count % period == 0)
        check(sum(exact_period.values()) == (n - 1) ** n + ordered_bell(n))
        check(max(depth_histogram) == max(0, n - 2))

        indegree_histogram = Counter(indegrees)
        check(indegree_histogram == symbolic_indegree_enumerator(n))
        check(max(indegrees) == expected_max_fibre(n))
        check(sum(degree * count for degree, count in indegree_histogram.items()) == size)

        # Compare every t-step target fibre with the independent n-phase oracle.
        iterated_targets = list(range(size))
        oracle_cache = {}
        for time in range(0, 2 * n + 1):
            target_counts = [0] * size
            for target in iterated_targets:
                target_counts[target] += 1
            for index in range(size):
                key = (profiles[index], time)
                if key not in oracle_cache:
                    oracle_cache[key] = target_oracle(*key)
                check(target_counts[index] == oracle_cache[key], (n, time, index))
            iterated_targets = [mapping[target] for target in iterated_targets]

        rows.append(
            "n={}:states={};period-points={};depths={};indegrees={};max={}".format(
                n,
                size,
                ",".join(f"{p}:{exact_period[p]}" for p in sorted(exact_period)),
                ",".join(f"{d}:{depth_histogram[d]}" for d in sorted(depth_histogram)),
                ",".join(f"{d}:{indegree_histogram[d]}" for d in sorted(indegree_histogram)),
                max(indegrees),
            )
        )
    return rows


def audit_compositions_and_symbolic_extension():
    rows = []
    composition_cells = 0
    phase_cells = 0
    for n in range(2, 12):
        weighted_periods = Counter()
        weighted_depths = Counter()
        weighted_indegrees = Counter()
        maximum_depth = 0
        for profile in weak_compositions(n, n):
            composition_cells += 1
            check(sum(profile) == n)
            weight = multinomial(profile)
            depth, period = phase_rho(profile, 0)
            weighted_depths[depth] += weight
            weighted_indegrees[target_fibre_from_profile(profile)] += weight
            maximum_depth = max(maximum_depth, depth)
            if depth == 0:
                weighted_periods[period] += weight
            for start in range(n):
                phase_cells += 1
                start_depth, _ = phase_rho(profile, start)
                check(start_depth <= max(0, n - 2))
            audit_cycle_geometry(profile)

        check(sum(weighted_depths.values()) == n ** n)
        check(dict(sorted(weighted_periods.items())) == expected_exact_period_points(n))
        check(maximum_depth == max(0, n - 2))
        check(weighted_indegrees == symbolic_indegree_enumerator(n))
        check(max(weighted_indegrees) == expected_max_fibre(n))
        if n in (8, 9, 10, 11):
            rows.append(
                f"n={n}:compositions={sum(1 for _ in weak_compositions(n,n))};"
                f"recurrent={(n-1)**n+ordered_bell(n)};tail={maximum_depth};"
                f"max-fibre={expected_max_fibre(n)}"
            )

    symbolic_rows = []
    for n in range(2, 31):
        enumerator = symbolic_indegree_enumerator(n)
        check(sum(enumerator.values()) == n ** n)
        check(sum(degree * count for degree, count in enumerator.items()) == n ** n)
        check(max(enumerator) == expected_max_fibre(n))
        if n in (12, 16, 20, 24, 30):
            symbolic_rows.append(
                f"n={n}:support={','.join(map(str,sorted(enumerator)))};"
                f"max-fibre={max(enumerator)};max-targets={enumerator[max(enumerator)]}"
            )
    return composition_cells, phase_cells, rows, symbolic_rows


def audit_boundary_witnesses():
    # n=2 is entirely recurrent and has maximum fibre one.
    mapping = [encode_state(literal_step(decode_state(i, 2), 2), 2) for i in range(4)]
    check(all(mapping_rho(mapping, i)[0] == 0 for i in range(4)))
    check(expected_max_fibre(2) == 1)

    # Sharp tail witness for every 3 <= n <= 64: profile
    # (1,...,1,2,1,0) with the 2 in position n-3.
    for n in range(3, 65):
        profile = [1] * n
        profile[n - 3] = 2
        profile[n - 1] = 0
        check(sum(profile) == n)
        check(phase_rho(tuple(profile), 0) == (n - 2, 1), (n, profile))

    # The maximum-fibre construction: hits r=1,...,h, no zero coordinate,
    # and places the leftover in symbol 1 without creating an extra hit.
    for n in range(3, 65):
        h = triangular_hit_number(n)
        profile = [0] * n
        for required in range(1, h + 1):
            profile[n - required] = required
        leftover = n - h * (h + 1) // 2
        if leftover:
            check(profile[1] == 0)
            profile[1] = leftover
        check(sum(profile) == n)
        check(profile[0] == 0)
        check(target_fibre_from_profile(tuple(profile)) == 1 + h)


def main():
    print("HAMMING-WEIGHT DIAGONAL TRANSLATION -- INDEPENDENT HOSTILE GATE A")
    print("[literal full spaces n=2..7]")
    for row in audit_literal_spaces():
        print(row)
    print("[composition extension n=2..11]")
    composition_cells, phase_cells, rows, symbolic_rows = audit_compositions_and_symbolic_extension()
    for row in rows:
        print(row)
    print(f"composition-cells={composition_cells};phase-cells={phase_cells}")
    print("[symbolic indegree EGF extension n=2..30]")
    for row in symbolic_rows:
        print(row)
    audit_boundary_witnesses()
    print("boundary-witnesses=n2 and n=3..64 PASS")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("RESULT=PASS")
    print("GATE_DECISION=GREEN_WITH_ALL_TIME_ORACLE_SUPPORT_ONLY")
    print("EXTERNAL_STATUS=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
