#!/usr/bin/env python3
"""Deterministic exact controls for A -> A+A on nonempty subsets of F_p.

The proof in the manuscript is uniform in the odd prime p.  This program is
only a finite falsification layer.  It uses two deliberately different
routes:

1. literal enumeration of the power set and its functional graph;
2. direct h-fold sumset construction, arithmetic-progression extremizers,
   and Moebius reconstruction of the temporal cycle census.

Every evidence-bearing operation is exact integer/set arithmetic.  There is
no randomness, floating-point comparison, CAS, or optimization solver.
"""

from collections import Counter
from itertools import combinations


ASSERTIONS = 0
LITERAL_SUBSETS = 0
LITERAL_PAIRS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    if n == 1:
        return 1
    remaining = n
    factors = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            factors += 1
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        factors += 1
    return -1 if factors % 2 else 1


def primes_through(limit):
    answer = []
    for candidate in range(2, limit + 1):
        if all(candidate % q for q in range(2, int(candidate ** 0.5) + 1)):
            answer.append(candidate)
    return answer


def order_of_two(p):
    value = 1
    for order in range(1, p):
        value = (2 * value) % p
        if value == 1:
            return order
    raise AssertionError((p, "2 has no multiplicative order"))


def all_subsets(p, nonempty=True):
    start = 1 if nonempty else 0
    for mask in range(start, 1 << p):
        yield frozenset(i for i in range(p) if (mask >> i) & 1)


def sumset(A, B, p):
    return frozenset((a + b) % p for a in A for b in B)


def phi(A, p):
    return sumset(A, A, p)


def iterate_phi(A, p, time):
    current = A
    for _ in range(time):
        current = phi(current, p)
    return current


def hfold_sumset(A, p, copies):
    check(copies >= 1, (p, copies, "positive number of summands"))
    current = frozenset({0})
    for _ in range(copies):
        current = sumset(current, A, p)
    return current


def ceiling_log_two_ratio(numerator, denominator):
    """Smallest t >= 0 with 2^t * denominator >= numerator."""
    check(numerator >= denominator >= 1,
          (numerator, denominator, "ratio endpoint"))
    time = 0
    scale = denominator
    while scale < numerator:
        scale *= 2
        time += 1
    return time


def absorption_time(A, p):
    check(len(A) >= 2, (p, A, "absorption is for nonsingletons"))
    full = frozenset(range(p))
    current = A
    time = 0
    while current != full:
        current = phi(current, p)
        time += 1
        check(time <= p, (p, A, "failed to absorb"))
    return time


def fixed_formula(p, order, iterate):
    return 2 + (p - 1 if iterate % order == 0 else 0)


def fixed_from_zeta_cycle_product(p, order, iterate):
    """Recover n[z^n] log zeta from its two registered cycle factors."""
    singleton_cycles = (p - 1) // order
    return 2 + (singleton_cycles * order
                if iterate % order == 0 else 0)


def temporal_orbit_from_fixed(p, order, period):
    numerator = sum(
        mobius(period // d) * fixed_formula(p, order, d)
        for d in divisors(period)
    )
    check(numerator % period == 0,
          (p, order, period, numerator, "temporal divisibility"))
    answer = numerator // period
    check(answer >= 0, (p, order, period, answer, "temporal nonnegativity"))
    return answer


def arithmetic_progression_differences(A, p):
    """All oriented nonzero differences realizing A as a modular AP."""
    size = len(A)
    differences = set()
    for start in A:
        for difference in range(1, p):
            candidate = frozenset(
                (start + j * difference) % p for j in range(size)
            )
            if len(candidate) == size and candidate == A:
                differences.add(difference)
    return differences


def functional_orbit(A, p):
    positions = {}
    history = []
    current = A
    while current not in positions:
        positions[current] = len(history)
        history.append(current)
        current = phi(current, p)
    return history, positions[current]


def identity_probe():
    """Compare repeated squaring with an independently built 2^t-fold sumset."""
    cases = []
    for p, max_time in [(3, 5), (5, 5), (7, 4)]:
        tested = 0
        for A in all_subsets(p):
            for time in range(max_time + 1):
                left = iterate_phi(A, p, time)
                right = hfold_sumset(A, p, 1 << time)
                check(left == right, (p, A, time, left, right, "iterate identity"))
                tested += 1
        cases.append((p, max_time, tested))
    return cases


def cauchy_davenport_and_vosper_probe():
    """Literal pairwise checks of Cauchy--Davenport and Vosper's safe range."""
    global LITERAL_PAIRS
    summaries = []
    for p in [3, 5, 7]:
        subsets = list(all_subsets(p))
        critical = 0
        for A in subsets:
            for B in subsets:
                LITERAL_PAIRS += 1
                C = sumset(A, B, p)
                check(len(C) >= min(p, len(A) + len(B) - 1),
                      (p, A, B, C, "Cauchy--Davenport"))
                if (len(A) >= 2 and len(B) >= 2
                        and len(C) == len(A) + len(B) - 1
                        and len(C) <= p - 2):
                    differences_A = arithmetic_progression_differences(A, p)
                    differences_B = arithmetic_progression_differences(B, p)
                    check(differences_A & differences_B,
                          (p, A, B, "Vosper common difference"))
                    critical += 1
        summaries.append((p, len(subsets) ** 2, critical))

    # A larger self-sum probe attacks exactly the rigidity statement used in
    # the manuscript without paying for every ordered pair at p=11,13.
    self_critical = {}
    for p in [11, 13]:
        count = 0
        for A in all_subsets(p):
            if len(A) < 2:
                continue
            doubled = phi(A, p)
            if len(doubled) == 2 * len(A) - 1 and len(doubled) <= p - 2:
                check(arithmetic_progression_differences(A, p),
                      (p, A, "self-Vosper AP"))
                count += 1
        self_critical[p] = count
    return summaries, self_critical


def full_power_set_probe():
    """Enumerate every state for five primes and reconstruct the phase portrait."""
    global LITERAL_SUBSETS
    summaries = []
    for p in [3, 5, 7, 11, 13]:
        order = order_of_two(p)
        full = frozenset(range(p))
        fixed_counts = [0] * (2 * order + 1)
        layer_max = {m: -1 for m in range(2, p + 1)}
        recurrent_cycles = set()

        for A in all_subsets(p):
            LITERAL_SUBSETS += 1
            doubled = phi(A, p)
            check(len(doubled) >= min(p, 2 * len(A) - 1),
                  (p, A, doubled, "self Cauchy--Davenport"))

            history, cycle_start = functional_orbit(A, p)
            recurrent = cycle_start == 0
            predicted_recurrent = (A == full or len(A) == 1)
            check(recurrent == predicted_recurrent,
                  (p, A, recurrent, cycle_start, "recurrent classification"))
            if recurrent:
                cycle = frozenset(history)
                recurrent_cycles.add(cycle)
                expected_length = 1 if A in (full, frozenset({0})) else order
                check(len(cycle) == expected_length,
                      (p, A, len(cycle), expected_length, "cycle length"))

            if len(A) >= 2:
                time = absorption_time(A, p)
                bound = ceiling_log_two_ratio(p - 1, len(A) - 1)
                check(time <= bound, (p, A, time, bound, "absorption bound"))
                layer_max[len(A)] = max(layer_max[len(A)], time)

            current = A
            for iterate in range(1, 2 * order + 1):
                current = phi(current, p)
                if current == A:
                    fixed_counts[iterate] += 1

        for iterate in range(1, 2 * order + 1):
            check(fixed_counts[iterate] == fixed_formula(p, order, iterate),
                  (p, iterate, fixed_counts[iterate], "fixed count"))

        expected_cycle_histogram = Counter({1: 2, order: (p - 1) // order})
        observed_cycle_histogram = Counter(len(cycle) for cycle in recurrent_cycles)
        check(observed_cycle_histogram == expected_cycle_histogram,
              (p, observed_cycle_histogram, expected_cycle_histogram,
               "recurrent cycle histogram"))

        expected_layers = {
            m: ceiling_log_two_ratio(p - 1, m - 1)
            for m in range(2, p + 1)
        }
        check(layer_max == expected_layers,
              (p, layer_max, expected_layers, "exact layer maxima"))
        summaries.append((p, order, fixed_counts[1:], layer_max,
                          dict(sorted(observed_cycle_histogram.items()))))
    return summaries


def arithmetic_progression_extremizer_probe():
    summaries = []
    total_cases = 0
    for p in [q for q in primes_through(43) if q % 2 == 1]:
        order = order_of_two(p)
        # The fixed sequence itself recovers the first anomaly and its height.
        fixed = [fixed_formula(p, order, n) for n in range(1, order + 1)]
        anomaly = next(n for n, value in enumerate(fixed, start=1) if value != 2)
        recovered_p = fixed[anomaly - 1] - 1
        check((recovered_p, anomaly) == (p, order),
              (p, order, recovered_p, anomaly, "first anomaly recovery"))

        for m in range(2, p + 1):
            total_cases += 1
            expected = ceiling_log_two_ratio(p - 1, m - 1)
            A = frozenset(range(m))
            observed = absorption_time(A, p)
            check(observed == expected,
                  (p, m, observed, expected, "AP extremizer depth"))
            for time in range(expected):
                observed_size = len(iterate_phi(A, p, time))
                expected_size = (1 << time) * (m - 1) + 1
                check(observed_size == expected_size,
                      (p, m, time, observed_size, expected_size,
                       "AP pre-absorption size"))
            check(iterate_phi(A, p, expected) == frozenset(range(p)),
                  (p, m, expected, "AP endpoint absorption"))

        # Moebius inversion of the fixed sequence must leave only the two
        # fixed cycles and the order-length singleton cycles.
        for period in range(1, 3 * order + 1):
            zeta_fixed = fixed_from_zeta_cycle_product(p, order, period)
            check(zeta_fixed == fixed_formula(p, order, period),
                  (p, order, period, zeta_fixed, "zeta log coefficient"))
            observed = temporal_orbit_from_fixed(p, order, period)
            if period == 1:
                expected = 2
            elif period == order:
                expected = (p - 1) // order
            else:
                expected = 0
            check(observed == expected,
                  (p, order, period, observed, expected, "temporal census"))
        summaries.append((p, order))
    return total_cases, summaries


def endpoint_probe():
    # Empty-set convention: adjoining it adds one fixed cycle.
    empty = frozenset()
    check(phi(empty, 5) == empty, "empty subset endpoint")

    # At p=2, doubling is not invertible on singletons; this is why the main
    # theorem assumes an odd prime.
    p = 2
    states = list(all_subsets(p))
    fixed_counts = []
    recurrent = 0
    for A in states:
        history, cycle_start = functional_orbit(A, p)
        if cycle_start == 0:
            recurrent += 1
        check(len(history) <= 2, (A, history, "p=2 phase portrait"))
    for iterate in range(1, 5):
        fixed_counts.append(sum(iterate_phi(A, p, iterate) == A for A in states))
    check(fixed_counts == [2, 2, 2, 2], (fixed_counts, "p=2 fixed endpoint"))
    check(recurrent == 2, (recurrent, "p=2 recurrent endpoint"))
    return fixed_counts, recurrent


def main():
    identity = identity_probe()
    pair_summaries, self_critical = cauchy_davenport_and_vosper_probe()
    phase_summaries = full_power_set_probe()
    ap_cases, orders = arithmetic_progression_extremizer_probe()
    endpoint_fixed, endpoint_recurrent = endpoint_probe()

    print("sumset-squaring exact control: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"literal_subsets={LITERAL_SUBSETS}")
    print(f"literal_ordered_pairs={LITERAL_PAIRS}")
    print(f"iterate_identity_cases={identity}")
    print(f"pairwise_cd_vosper={pair_summaries}")
    print(f"self_vosper_critical={self_critical}")
    for p, order, fixed, layers, cycles in phase_summaries:
        print(f"phase p={p} ord2={order} fixed_1..2h={fixed} "
              f"layer_max={layers} recurrent_cycles={cycles}")
    print(f"ap_extremizer_cases={ap_cases} prime_orders={orders}")
    print(f"endpoint_p2 fixed_1..4={endpoint_fixed} "
          f"recurrent_points={endpoint_recurrent}")


if __name__ == "__main__":
    main()
