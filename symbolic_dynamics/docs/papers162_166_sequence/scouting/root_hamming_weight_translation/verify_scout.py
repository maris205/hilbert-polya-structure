#!/usr/bin/env python3
"""Independent exact controls for the Hamming-weight translation scout.

The script uses only the literal update.  It does not import any code from
another scout or paper.  Exhaustive checks cover the full state spaces
(Z/nZ)^n for 2 <= n <= 7 and all weak compositions of n into n parts for
2 <= n <= 10.  Larger deterministic random tests attack composite n as
well as prime n.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial, isqrt
import random


ASSERTIONS = 0


def check(condition: bool, message: object) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def weak_compositions(total: int, parts: int, prefix: tuple[int, ...] = ()):
    if parts == 1:
        yield prefix + (total,)
        return
    for first in range(total + 1):
        yield from weak_compositions(total - first, parts - 1, prefix + (first,))


def histogram(x: tuple[int, ...]) -> tuple[int, ...]:
    n = len(x)
    counts = [0] * n
    for value in x:
        counts[value] += 1
    return tuple(counts)


def literal_map(x: tuple[int, ...]) -> tuple[int, ...]:
    n = len(x)
    weight = sum(value != 0 for value in x)
    return tuple((value + weight) % n for value in x)


def phase_map(c: tuple[int, ...]) -> tuple[int, ...]:
    n = len(c)
    return tuple((i + c[i]) % n for i in range(n))


def tail_period(mapping: tuple[int, ...], start: int) -> tuple[int, int]:
    seen: dict[int, int] = {}
    point = start
    while point not in seen:
        seen[point] = len(seen)
        point = mapping[point]
    return seen[point], len(seen) - seen[point]


def cycles(mapping: tuple[int, ...]) -> list[tuple[int, ...]]:
    n = len(mapping)
    done: set[int] = set()
    answer: list[tuple[int, ...]] = []
    for start in range(n):
        if start in done:
            continue
        local: dict[int, int] = {}
        path: list[int] = []
        point = start
        while point not in local and point not in done:
            local[point] = len(path)
            path.append(point)
            point = mapping[point]
        if point in local:
            answer.append(tuple(path[local[point] :]))
        done.update(path)
    return answer


def is_gap_vector(c: tuple[int, ...]) -> bool:
    """Whether positive entries are clockwise gaps between their supports."""
    n = len(c)
    support = [i for i, value in enumerate(c) if value > 0]
    if not support:
        return False
    for position, point in enumerate(support):
        successor = support[(position + 1) % len(support)]
        gap = (successor - point) % n
        if gap == 0:
            gap = n
        if c[point] != gap:
            return False
    return True


def one_step_fibre_formula(y: tuple[int, ...]) -> int:
    n = len(y)
    counts = histogram(y)
    answer = int(counts[0] in (0, n))
    answer += sum(counts[k] == n - k for k in range(1, n))
    return answer


def max_fibre_formula(n: int) -> int:
    if n == 2:
        return 1
    r = (isqrt(8 * n + 1) - 1) // 2
    return 1 + r


def stirling_second(n: int, k: int) -> int:
    table = [[0] * (k + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for row in range(1, n + 1):
        for col in range(1, min(row, k) + 1):
            table[row][col] = table[row - 1][col - 1] + col * table[row - 1][col]
    return table[n][k]


def expected_period_points(n: int) -> dict[int, int]:
    answer = {1: 1 + (n - 1) ** n}
    for period in range(2, n + 1):
        answer[period] = factorial(period) * stirling_second(n, period)
    return answer


def encode(x: tuple[int, ...], base: int) -> int:
    answer = 0
    for value in x:
        answer = base * answer + value
    return answer


def polynomial_multiply(
    left: dict[tuple[int, int], Fraction],
    right: dict[tuple[int, int], Fraction],
    degree_cap: int,
) -> dict[tuple[int, int], Fraction]:
    answer: dict[tuple[int, int], Fraction] = {}
    for (du, dz), a in left.items():
        for (eu, ez), b in right.items():
            if du + eu <= degree_cap:
                key = (du + eu, dz + ez)
                answer[key] = answer.get(key, Fraction(0)) + a * b
    return answer


def fibre_polynomial(n: int) -> dict[int, int]:
    """Evaluate the claimed truncated exponential coefficient formula."""
    polynomial = {(0, 0): Fraction(1)}
    zero_factor = {
        (degree, int(degree in (0, n))): Fraction(1, factorial(degree))
        for degree in range(n + 1)
    }
    polynomial = polynomial_multiply(polynomial, zero_factor, n)
    for residue in range(1, n):
        marked_degree = n - residue
        factor = {
            (degree, int(degree == marked_degree)): Fraction(1, factorial(degree))
            for degree in range(n + 1)
        }
        polynomial = polynomial_multiply(polynomial, factor, n)
    answer: dict[int, int] = {}
    for (degree, fibre), coefficient in polynomial.items():
        if degree == n:
            scaled = coefficient * factorial(n)
            check(scaled.denominator == 1, ("fibre coefficient not integral", n, fibre, scaled))
            answer[fibre] = int(scaled)
    return answer


def self_avoiding_step_sequences(n: int, length: int):
    def recurse(
        steps: tuple[int, ...], ordinary_sum: int, residues: frozenset[int]
    ):
        if len(steps) == length:
            yield steps
            return
        for step in range(1, n):
            new_sum = ordinary_sum + step
            if new_sum > n:
                break
            residue = new_sum % n
            if residue not in residues:
                yield from recurse(steps + (step,), new_sum, residues | {residue})

    yield from recurse((), 0, frozenset({0}))


def tail_census_formula(n: int, tail: int) -> int:
    """Coefficient formula for points whose preperiod is exactly ``tail``."""
    total = Fraction(0)
    free_boxes = n - tail - 1
    for steps in self_avoiding_step_sequences(n, tail):
        used_mass = sum(steps)
        remaining_mass = n - used_mass
        denominator = factorial(remaining_mass)
        for step in steps:
            denominator *= factorial(step)
        total += Fraction(
            factorial(n) * (free_boxes**remaining_mass), denominator
        )
    check(total.denominator == 1, ("tail coefficient not integral", n, tail, total))
    return int(total)


def tail_census_closed(n: int, tail: int) -> int:
    """Stirling-number collapse of the self-avoiding path coefficient."""
    return factorial(tail) * sum(
        comb(n, mass)
        * stirling_second(mass, tail)
        * (n - tail - 1) ** (n - mass)
        for mass in range(tail, n)
    )


def exhaustive_composition_checks(n: int) -> tuple[int, int, int]:
    nontrivial_cycle_histograms = Counter()
    maximum_tail_histograms = 0
    maximum_tail_phase_pairs = 0
    composition_count = 0
    for c in weak_compositions(n, n):
        composition_count += 1
        mapping = phase_map(c)
        all_cycles = cycles(mapping)
        nontrivial = [cycle for cycle in all_cycles if len(cycle) > 1]
        check(len(nontrivial) <= 1, ("multiple nontrivial cycles", n, c, nontrivial))
        if nontrivial:
            cycle = nontrivial[0]
            check(sum(c[i] for i in cycle) == n, ("cycle mass", n, c, cycle))
            check(is_gap_vector(c), ("non-gap recurrent vector", n, c, cycle))
            check(set(cycle) == {i for i, value in enumerate(c) if value},
                  ("cycle support", n, c, cycle))
            nontrivial_cycle_histograms[len(cycle)] += 1
        elif is_gap_vector(c):
            support_size = sum(value > 0 for value in c)
            check(support_size == 1, ("missed gap cycle", n, c))
        tails = [tail_period(mapping, point)[0] for point in range(n)]
        check(max(tails) <= n - 2, ("tail bound", n, c, tails))
        if n >= 3:
            zero_sites = [i for i, value in enumerate(c) if value == 0]
            double_sites = [i for i, value in enumerate(c) if value == 2]
            equality_shape = (
                len(zero_sites) == 1
                and len(double_sites) == 1
                and all(value in (0, 1, 2) for value in c)
                and double_sites[0] != (zero_sites[0] - 1) % n
            )
            check((max(tails) == n - 2) == equality_shape,
                  ("tail equality shape", n, c, tails, equality_shape))
            if equality_shape:
                maximum_tail_histograms += 1
                actual_sharp_phases = {i for i, value in enumerate(tails) if value == n - 2}
                zero = zero_sites[0]
                double = double_sites[0]
                expected_sharp_phases = {(zero + 1) % n}
                if double == (zero + 1) % n:
                    expected_sharp_phases.add((zero + 2) % n)
                check(actual_sharp_phases == expected_sharp_phases,
                      ("sharp phases", n, c, actual_sharp_phases, expected_sharp_phases))
                maximum_tail_phase_pairs += len(actual_sharp_phases)
    for length in range(2, n + 1):
        check(nontrivial_cycle_histograms[length] == comb(n, length),
              ("cycle histogram census", n, length, nontrivial_cycle_histograms))
    if n >= 3:
        check(maximum_tail_histograms == n * (n - 2),
              ("max-tail histogram census", n, maximum_tail_histograms))
        check(maximum_tail_phase_pairs == n * (n - 1),
              ("max-tail phase census", n, maximum_tail_phase_pairs))
    return composition_count, maximum_tail_histograms, maximum_tail_phase_pairs


def exhaustive_state_checks(n: int) -> dict[str, object]:
    state_count = n**n
    indegree = [0] * state_count
    tail_counts: Counter[int] = Counter()
    period_counts: Counter[int] = Counter()
    recurrent_period_counts: Counter[int] = Counter()
    max_tail_histograms: Counter[tuple[int, ...]] = Counter()

    for x in product(range(n), repeat=n):
        c = histogram(x)
        target = literal_map(x)
        expected_target = tuple((value - c[0]) % n for value in x)
        check(target == expected_target, ("literal phase reduction", n, x, target, expected_target))
        indegree[encode(target, n)] += 1

        mapping = phase_map(c)
        tail, period = tail_period(mapping, 0)
        tail_counts[tail] += 1
        period_counts[period] += 1
        if tail == 0:
            recurrent_period_counts[period] += 1
        if n >= 3 and tail == n - 2:
            max_tail_histograms[c] += 1

    fibre_counts: Counter[int] = Counter()
    for y in product(range(n), repeat=n):
        index = encode(y, n)
        formula = one_step_fibre_formula(y)
        check(indegree[index] == formula, ("target fibre", n, y, indegree[index], formula))
        fibre_counts[formula] += 1

    check(sum(tail_counts.values()) == state_count, ("tail total", n))
    check(max(tail_counts) == n - 2, ("sharp tail", n, tail_counts))
    expected_periods = expected_period_points(n)
    check(dict(sorted(recurrent_period_counts.items())) == expected_periods,
          ("period spectrum", n, recurrent_period_counts, expected_periods))
    recurrent_formula = (n - 1) ** n + sum(
        factorial(length) * stirling_second(n, length) for length in range(1, n + 1)
    )
    check(tail_counts[0] == recurrent_formula,
          ("recurrent census", n, tail_counts[0], recurrent_formula))
    if n >= 3:
        check(tail_counts[n - 2] == (n - 1) * factorial(n) // 2,
              ("last transient shell", n, tail_counts[n - 2]))
        witness = [1] * n
        witness[n - 1] = 0
        witness[0] = 2
        check(tail_period(phase_map(tuple(witness)), 0)[0] == n - 2,
              ("tail witness", n, witness))

    expected_fibre_polynomial = fibre_polynomial(n)
    check(dict(sorted(fibre_counts.items())) == dict(sorted(expected_fibre_polynomial.items())),
          ("fibre polynomial", n, fibre_counts, expected_fibre_polynomial))
    check(max(fibre_counts) == max_fibre_formula(n),
          ("max fibre", n, fibre_counts, max_fibre_formula(n)))
    if n >= 3:
        r = (isqrt(8 * n + 1) - 1) // 2
        counts = [0] * n
        for mass in range(1, r + 1):
            counts[n - mass] = mass
        remainder = n - r * (r + 1) // 2
        if remainder:
            counts[1] += remainder
        witness = tuple(value for residue, count in enumerate(counts) for value in [residue] * count)
        check(len(witness) == n, ("fibre witness length", n, counts))
        check(one_step_fibre_formula(witness) == 1 + r,
              ("fibre witness", n, counts, one_step_fibre_formula(witness)))

    for tail in range(1, max(1, n - 1)):
        path_formula = tail_census_formula(n, tail)
        closed_formula = tail_census_closed(n, tail)
        check(path_formula == closed_formula,
              ("tail formulas disagree", n, tail, path_formula, closed_formula))
        check(tail_counts[tail] == closed_formula,
              ("tail census formula", n, tail, tail_counts[tail], closed_formula))

    return {
        "states": state_count,
        "image": state_count - fibre_counts.get(0, 0),
        "tails": dict(sorted(tail_counts.items())),
        "periods": dict(sorted(recurrent_period_counts.items())),
        "fibres": dict(sorted(fibre_counts.items())),
        "max_tail_histograms": len(max_tail_histograms),
    }


def randomized_extension_checks() -> int:
    generator = random.Random(0x48A66)
    tests = 0
    for n in (11, 12, 16, 20, 31, 48, 64, 80):
        for _ in range(400):
            c = [0] * n
            for _ball in range(n):
                c[generator.randrange(n)] += 1
            c_tuple = tuple(c)
            mapping = phase_map(c_tuple)
            nontrivial = [cycle for cycle in cycles(mapping) if len(cycle) > 1]
            check(len(nontrivial) <= 1, ("random cycle uniqueness", n, c_tuple, nontrivial))
            if nontrivial:
                cycle = nontrivial[0]
                check(sum(c_tuple[i] for i in cycle) == n,
                      ("random cycle mass", n, c_tuple, cycle))
                check(is_gap_vector(c_tuple), ("random gap vector", n, c_tuple, cycle))
            tails = [tail_period(mapping, i)[0] for i in range(n)]
            check(max(tails) <= n - 2, ("random tail bound", n, c_tuple, tails))
            check(one_step_fibre_formula(tuple(
                residue for residue, count in enumerate(c_tuple) for _ in range(count)
            )) <= max_fibre_formula(n), ("random fibre cap", n, c_tuple))
            tests += 1
    return tests


def format_counter(values: dict[int, int]) -> str:
    return ",".join(f"{key}:{values[key]}" for key in sorted(values))


def main() -> None:
    print("HWT_SCOUT_VERIFIER_V1")
    print("literal=T(x)=x+w(x)*1 mod n; phase convention=x-i*1")
    direct_results = {}
    for n in range(2, 8):
        result = exhaustive_state_checks(n)
        direct_results[n] = result
        print(
            f"n={n} states={result['states']} image={result['image']} "
            f"tails={format_counter(result['tails'])} "
            f"periods={format_counter(result['periods'])} "
            f"fibres={format_counter(result['fibres'])}"
        )
    for n in range(2, 11):
        count, sharp_histograms, sharp_pairs = exhaustive_composition_checks(n)
        print(
            f"compositions_n={n} count={count} "
            f"sharp_histograms={sharp_histograms} sharp_phase_pairs={sharp_pairs}"
        )
    random_tests = randomized_extension_checks()
    print(f"random_extensions={random_tests} moduli=11,12,16,20,31,48,64,80")
    print("BOUNDARIES n=2 permutation; t=0 recurrent; empty/full zero-support targets checked")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
