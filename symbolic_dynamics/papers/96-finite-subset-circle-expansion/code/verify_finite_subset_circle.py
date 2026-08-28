#!/usr/bin/env python3
"""Exact controls for finite-subset dynamics induced by x -> d*x on S^1.

All evidence-bearing comparisons use integers.  The two principal routes are:

1. a truncated binary Euler product assembled from Moebius orbit counts;
2. literal cycle decompositions of multiplication by Q on a rational circle
   grid, followed in small cases by direct enumeration of every subset.
"""

from itertools import combinations
from math import comb, gcd, lcm


ASSERTIONS = 0
LITERAL_SUBSETS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    """Return the classical Moebius function by exact trial division."""
    if n == 1:
        return 1
    remaining = n
    prime_factors = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            prime_factors += 1
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        prime_factors += 1
    return -1 if prime_factors % 2 else 1


def base_orbit_counts(Q, cutoff):
    """Least-period orbit counts for x -> Q*x on R/Z."""
    answer = {}
    for ell in range(1, cutoff + 1):
        least_period_points = sum(
            mobius(ell // e) * (Q ** e - 1) for e in divisors(ell)
        )
        check(least_period_points % ell == 0,
              (Q, ell, "base orbit divisibility"))
        answer[ell] = least_period_points // ell
        check(answer[ell] >= 0, (Q, ell, "base orbit nonnegativity"))
    return answer


def binary_euler_coefficients(Q, cutoff):
    """Coefficients of product (1+u^ell)^O_ell through u^cutoff."""
    coefficients = [0] * (cutoff + 1)
    coefficients[0] = 1
    for ell, orbit_count in base_orbit_counts(Q, cutoff).items():
        updated = [0] * (cutoff + 1)
        for old_degree, old_value in enumerate(coefficients):
            if old_value == 0:
                continue
            max_chosen = min(orbit_count, (cutoff - old_degree) // ell)
            for chosen in range(max_chosen + 1):
                updated[old_degree + chosen * ell] += (
                    old_value * comb(orbit_count, chosen)
                )
        coefficients = updated
    return coefficients


def multiset_euler_coefficients(Q, cutoff):
    """Control coefficients of product (1-u^ell)^(-O_ell)."""
    coefficients = [0] * (cutoff + 1)
    coefficients[0] = 1
    for ell, orbit_count in base_orbit_counts(Q, cutoff).items():
        updated = [0] * (cutoff + 1)
        for old_degree, old_value in enumerate(coefficients):
            if old_value == 0:
                continue
            max_multiplicity = (cutoff - old_degree) // ell
            for multiplicity in range(max_multiplicity + 1):
                if multiplicity == 0:
                    ways = 1
                elif orbit_count == 0:
                    ways = 0
                else:
                    ways = comb(orbit_count + multiplicity - 1, multiplicity)
                updated[old_degree + multiplicity * ell] += old_value * ways
        coefficients = updated
    return coefficients


def exact_cardinality_formula(Q, j):
    numerator = (Q - 1) * (Q ** j - (-1) ** j)
    check(numerator % (Q + 1) == 0, (Q, j, "exact formula divisibility"))
    return numerator // (Q + 1)


def total_fixed_formula(Q, k):
    if k % 2 == 0:
        numerator = Q * (Q ** k - 1)
    else:
        numerator = Q ** (k + 1) - 1
    check(numerator % (Q + 1) == 0, (Q, k, "total formula divisibility"))
    return numerator // (Q + 1)


def alternating_fixed_polynomial(Q, k):
    lower = 1 if k % 2 == 0 else 0
    return sum((-1) ** (k - r) * Q ** r for r in range(lower, k + 1))


def zeta_factor_exponents(k):
    """Exponent of (1-d^r*z) in the claimed Artin--Mazur product."""
    lower = 1 if k % 2 == 0 else 0
    return {r: (-1) ** (k - r + 1) for r in range(lower, k + 1)}


def rational_grid_modulus(Q, cutoff):
    modulus = 1
    for ell in range(1, cutoff + 1):
        modulus = lcm(modulus, Q ** ell - 1)
    check(gcd(Q, modulus) == 1, (Q, cutoff, modulus, "grid permutation"))
    return modulus


def literal_grid_cycles(Q, cutoff):
    """Decompose multiplication by Q on Z/LZ and retain cycles <= cutoff."""
    modulus = rational_grid_modulus(Q, cutoff)
    seen = set()
    retained = []
    for start in range(modulus):
        if start in seen:
            continue
        cycle = []
        current = start
        while current not in seen:
            seen.add(current)
            cycle.append(current)
            current = (Q * current) % modulus
        check(current == start, (Q, cutoff, start, "permutation cycle closure"))
        if len(cycle) <= cutoff:
            retained.append(tuple(cycle))
    check(len(seen) == modulus, (Q, cutoff, "grid coverage"))
    return modulus, retained


def literal_cycle_selection_coefficients(cycles, cutoff):
    """0/1 subset-sum DP over actually enumerated rational-circle cycles."""
    coefficients = [0] * (cutoff + 1)
    coefficients[0] = 1
    for cycle in cycles:
        length = len(cycle)
        for degree in range(cutoff, length - 1, -1):
            coefficients[degree] += coefficients[degree - length]
    return coefficients


def direct_grid_subset_counts(Q, cutoff):
    """Enumerate every small grid subset and test Q*A=A literally."""
    global LITERAL_SUBSETS
    modulus = rational_grid_modulus(Q, cutoff)
    counts = [0] * (cutoff + 1)
    for size in range(1, cutoff + 1):
        for entries in combinations(range(modulus), size):
            LITERAL_SUBSETS += 1
            subset = frozenset(entries)
            image = frozenset((Q * entry) % modulus for entry in entries)
            if image == subset:
                counts[size] += 1
    return modulus, counts


def induced_primitive_orbits(d, k, period):
    numerator = sum(
        mobius(period // e) * total_fixed_formula(d ** e, k)
        for e in divisors(period)
    )
    check(numerator % period == 0,
          (d, k, period, numerator, "induced orbit divisibility"))
    answer = numerator // period
    check(answer >= 0, (d, k, period, answer, "induced orbit nonnegativity"))
    return answer


def coefficient_probe():
    for Q in range(2, 9):
        cutoff = 9
        binary = binary_euler_coefficients(Q, cutoff)
        multiset = multiset_euler_coefficients(Q, cutoff)
        for j in range(1, cutoff + 1):
            check(binary[j] == exact_cardinality_formula(Q, j),
                  (Q, j, binary[j], "binary coefficient"))
            check(multiset[j] == Q ** (j - 1) * (Q - 1),
                  (Q, j, multiset[j], "multiset control"))
        for k in range(1, cutoff + 1):
            total = sum(binary[1:k + 1])
            check(total == total_fixed_formula(Q, k),
                  (Q, k, total, "partial sum"))
            check(total == alternating_fixed_polynomial(Q, k),
                  (Q, k, total, "alternating polynomial"))


def zeta_and_rigidity_probe():
    """Check formal logarithmic coefficients and the outer-factor recovery."""
    for d in range(2, 8):
        for k in range(1, 10):
            exponents = zeta_factor_exponents(k)
            check(exponents[k] == -1, (d, k, "outer factor is a pole"))
            check(exponents[k - 1] == 1,
                  (d, k, "next outer factor is a zero"))
            pole_weight = d ** k
            zero_weight = d ** (k - 1)
            check(pole_weight // zero_weight == d,
                  (d, k, "pole/zero ratio recovers d"))
            recovered_k = 0
            residual = pole_weight
            while residual > 1:
                check(residual % d == 0,
                      (d, k, residual, "pole weight is a power of d"))
                residual //= d
                recovered_k += 1
            check(recovered_k == k,
                  (d, k, recovered_k, "outer pole recovers k after d"))
            for iterate in range(1, 16):
                from_factors = -sum(
                    exponent * d ** (r * iterate)
                    for r, exponent in exponents.items()
                )
                check(from_factors == total_fixed_formula(d ** iterate, k),
                      (d, k, iterate, from_factors, "zeta log coefficient"))


def literal_cycle_probe():
    cases = [(2, 5), (3, 4), (4, 4), (5, 3), (8, 3)]
    summaries = []
    for Q, cutoff in cases:
        modulus, cycles = literal_grid_cycles(Q, cutoff)
        observed_orbits = {ell: 0 for ell in range(1, cutoff + 1)}
        for cycle in cycles:
            observed_orbits[len(cycle)] += 1
        expected_orbits = base_orbit_counts(Q, cutoff)
        check(observed_orbits == expected_orbits,
              (Q, cutoff, observed_orbits, expected_orbits, "literal cycles"))

        coefficients = literal_cycle_selection_coefficients(cycles, cutoff)
        for j in range(1, cutoff + 1):
            check(coefficients[j] == exact_cardinality_formula(Q, j),
                  (Q, cutoff, j, coefficients[j], "literal cycle selection"))
        check(sum(coefficients[1:]) == total_fixed_formula(Q, cutoff),
              (Q, cutoff, "literal total"))
        summaries.append((Q, cutoff, modulus, observed_orbits,
                          coefficients[1:], sum(coefficients[1:])))
    return summaries


def direct_subset_probe():
    cases = [(2, 3), (3, 3), (4, 2)]
    summaries = []
    for Q, cutoff in cases:
        modulus, counts = direct_grid_subset_counts(Q, cutoff)
        for j in range(1, cutoff + 1):
            check(counts[j] == exact_cardinality_formula(Q, j),
                  (Q, cutoff, j, counts[j], "direct grid subsets"))
        check(sum(counts[1:]) == total_fixed_formula(Q, cutoff),
              (Q, cutoff, "direct grid total"))
        summaries.append((Q, cutoff, modulus, counts[1:], sum(counts[1:])))
    return summaries


def temporal_probe():
    for d in range(2, 6):
        for k in range(1, 8):
            primitive = {}
            for period in range(1, 13):
                primitive[period] = induced_primitive_orbits(d, k, period)
            for iterate in range(1, 13):
                reconstructed = sum(
                    period * primitive[period] for period in divisors(iterate)
                )
                check(reconstructed == total_fixed_formula(d ** iterate, k),
                      (d, k, iterate, reconstructed, "temporal reconstruction"))


def main():
    coefficient_probe()
    zeta_and_rigidity_probe()
    cycle_summaries = literal_cycle_probe()
    subset_summaries = direct_subset_probe()
    temporal_probe()

    sample = [induced_primitive_orbits(2, 3, period)
              for period in range(1, 9)]
    print("finite-subset circle exact control: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"literal_subsets={LITERAL_SUBSETS}")
    for Q, cutoff, modulus, orbits, exact, total in cycle_summaries:
        print(f"cycle Q={Q} k={cutoff} L={modulus} "
              f"orbits={orbits} exact={exact} total={total}")
    for Q, cutoff, modulus, exact, total in subset_summaries:
        print(f"subset Q={Q} k={cutoff} L={modulus} "
              f"exact={exact} total={total}")
    print(f"temporal d=2 k=3 P_1..P_8={sample}")


if __name__ == "__main__":
    main()
