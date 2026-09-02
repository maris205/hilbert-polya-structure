#!/usr/bin/env python3
"""Focused exact audit for cyclic substitution-collapse dynamics.

The map is f(X) -> f(X^k) modulo X^m-1.  Path A performs repeated literal
coefficient substitution.  Path B independently rebuilds the t-th image by
solving each congruence k^t j = r (mod m).  Formula checks do not construct
either implementation.  Enumeration is bounded falsification evidence only.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
from math import gcd


class Audit:
    def __init__(self) -> None:
        self.assertions = 0
        self.boxes = 0

    def check(self, condition: bool, message: object = "") -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message or f"assertion {self.assertions} failed")

    def box(self) -> None:
        self.boxes += 1


A = Audit()
LINES: list[str] = []


def emit(line: str) -> None:
    LINES.append(line)


class ZnRing:
    def __init__(self, modulus: int) -> None:
        if modulus < 2:
            raise ValueError("the zero ring is outside the theorem contract")
        self.modulus = modulus
        self.name = f"Z{modulus}"
        self.elements = tuple(range(modulus))
        self.zero = 0

    def add(self, left: int, right: int) -> int:
        return (left + right) % self.modulus


class ProductRing:
    def __init__(self, moduli: tuple[int, ...]) -> None:
        if not moduli or any(modulus < 2 for modulus in moduli):
            raise ValueError("nontrivial factors are required")
        self.moduli = moduli
        self.name = "x".join(f"Z{modulus}" for modulus in moduli)
        self.elements = tuple(product(*(range(modulus) for modulus in moduli)))
        self.zero = tuple(0 for _ in moduli)

    def add(self, left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
        return tuple((x + y) % modulus
                     for x, y, modulus in zip(left, right, self.moduli))


def add_block(ring, values):
    answer = ring.zero
    for value in values:
        answer = ring.add(answer, value)
    return answer


def literal_once(coefficients, ring, m: int, k: int):
    """Path A: send each monomial independently, merging on arrival."""
    output = [ring.zero for _ in range(m)]
    for source, coefficient in enumerate(coefficients):
        target = (k * source) % m
        output[target] = ring.add(output[target], coefficient)
    return tuple(output)


def literal_iterate(coefficients, ring, m: int, k: int, t: int):
    for _ in range(t):
        coefficients = literal_once(coefficients, ring, m, k)
    return coefficients


def congruence_pushforward(coefficients, ring, m: int, k: int, t: int):
    """Path B: solve k^t*j=r mod m separately for each output coordinate."""
    multiplier = pow(k, t, m)
    output = []
    for target in range(m):
        block = (coefficients[source] for source in range(m)
                 if (multiplier * source - target) % m == 0)
        output.append(add_block(ring, block))
    return tuple(output)


def valuation(number: int, prime: int) -> int:
    exponent = 0
    while number % prime == 0:
        exponent += 1
        number //= prime
    return exponent


def prime_factorization(number: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            number //= divisor
        divisor += 1
    if number > 1:
        factors[number] = factors.get(number, 0) + 1
    return factors


def ceil_div(left: int, right: int) -> int:
    return (left + right - 1) // right


def parallel_part_and_height(m: int, k: int) -> tuple[int, int]:
    parallel = 1
    height = 0
    for prime, exponent in prime_factorization(m).items():
        if k % prime == 0:
            speed = valuation(k, prime)
            parallel *= prime ** exponent
            height = max(height, ceil_div(exponent, speed))
    return parallel, height


def divisors(number: int) -> tuple[int, ...]:
    return tuple(candidate for candidate in range(1, number + 1)
                 if number % candidate == 0)


def phi(number: int) -> int:
    answer = number
    for prime in prime_factorization(number):
        answer -= answer // prime
    return answer


def mobius(number: int) -> int:
    factors = prime_factorization(number)
    if any(exponent > 1 for exponent in factors.values()):
        return 0
    return -1 if len(factors) % 2 else 1


def multiplicative_order(multiplier: int, modulus: int) -> int:
    if modulus == 1:
        return 1
    A.check(gcd(multiplier, modulus) == 1,
            ("multiplicative order domain", multiplier, modulus))
    cursor = 1
    for order in range(1, phi(modulus) + 1):
        cursor = cursor * multiplier % modulus
        if cursor == 1:
            return order
    raise AssertionError(("missing order", multiplier, modulus))


def position_cycle_count_direct(n: int, multiplier: int) -> int:
    seen: set[int] = set()
    count = 0
    for start in range(n):
        if start in seen:
            continue
        count += 1
        cursor = start
        while cursor not in seen:
            seen.add(cursor)
            cursor = multiplier * cursor % n
    return count


def position_cycle_count_divisors(n: int, k: int, r: int) -> int:
    return sum(phi(order) // multiplicative_order(pow(k, r), order)
               for order in divisors(n))


def in_support_module(coefficients, ring, divisor: int) -> bool:
    return all(coefficient == ring.zero or index % divisor == 0
               for index, coefficient in enumerate(coefficients))


@dataclass(frozen=True)
class GraphSummary:
    fixed: int
    periodic: int
    components: int
    max_tail: int
    cycle_hist: tuple[tuple[int, int], ...]
    indegree_hist: tuple[tuple[int, int], ...]
    edge_sha16: str
    tail_cycle: dict


def graph_summary(states, successor) -> GraphSummary:
    successor_map = {state: successor(state) for state in states}
    state_set = set(states)
    A.check(len(state_set) == len(states), "duplicate states")
    for state, target in successor_map.items():
        A.check(target in state_set, ("closure", state, target))

    tail_cycle: dict[object, tuple[int, int]] = {}
    cycle_hist: Counter[int] = Counter()
    for start in states:
        if start in tail_cycle:
            continue
        path = []
        local_index = {}
        cursor = start
        while cursor not in local_index and cursor not in tail_cycle:
            local_index[cursor] = len(path)
            path.append(cursor)
            cursor = successor_map[cursor]
        if cursor in local_index:
            cycle_start = local_index[cursor]
            cycle_length = len(path) - cycle_start
            cycle_hist[cycle_length] += 1
            for state in path[cycle_start:]:
                tail_cycle[state] = (0, cycle_length)
            distance = 0
            for state in reversed(path[:cycle_start]):
                distance += 1
                tail_cycle[state] = (distance, cycle_length)
        else:
            distance, cycle_length = tail_cycle[cursor]
            for state in reversed(path):
                distance += 1
                tail_cycle[state] = (distance, cycle_length)

    indegrees = Counter(successor_map.values())
    indegree_hist = Counter(indegrees.get(state, 0) for state in states)
    fixed = sum(successor_map[state] == state for state in states)
    periodic = sum(distance == 0 for distance, _ in tail_cycle.values())
    max_tail = max(distance for distance, _ in tail_cycle.values())
    payload = "\n".join(f"{state!r}->{successor_map[state]!r}" for state in states)
    return GraphSummary(
        fixed=fixed,
        periodic=periodic,
        components=sum(cycle_hist.values()),
        max_tail=max_tail,
        cycle_hist=tuple(sorted(cycle_hist.items())),
        indegree_hist=tuple(sorted(indegree_hist.items())),
        edge_sha16=sha256(payload.encode("utf-8")).hexdigest()[:16],
        tail_cycle=tail_cycle,
    )


def format_hist(hist: tuple[tuple[int, int], ...]) -> str:
    return "{" + ",".join(f"{key}:{value}" for key, value in hist) + "}"


CASE_RESULTS: dict[tuple[str, int, int], GraphSummary] = {}


def run_case(ring, m: int, k: int) -> None:
    q = len(ring.elements)
    states = tuple(product(ring.elements, repeat=m))
    successor = lambda state: literal_once(state, ring, m, k)
    summary = graph_summary(states, successor)
    parallel, height = parallel_part_and_height(m, k)
    perpendicular = m // parallel

    A.check(summary.periodic == q ** perpendicular)
    A.check(summary.max_tail == height)
    recurrent_states = {state for state in states
                        if summary.tail_cycle[state][0] == 0}
    formula_core = {state for state in states
                    if in_support_module(state, ring, parallel)}
    A.check(recurrent_states == formula_core)

    gcd_sequence = []
    previous_cdf = 0
    for t in range(height + 3):
        g_t = gcd(pow(k, t), m)
        gcd_sequence.append(g_t)
        actual_fibres = Counter()
        for state in states:
            path_a = literal_iterate(state, ring, m, k, t)
            path_b = congruence_pushforward(state, ring, m, k, t)
            A.check(path_a == path_b, ("path disagreement", ring.name, m, k, t, state))
            actual_fibres[path_a] += 1

        expected_image = {target for target in states
                          if in_support_module(target, ring, g_t)}
        A.check(set(actual_fibres) == expected_image,
                ("image", ring.name, m, k, t))
        A.check(len(expected_image) == q ** (m // g_t))
        fibre_size = q ** (m - m // g_t)
        for target in states:
            expected_fibre = fibre_size if target in expected_image else 0
            A.check(actual_fibres.get(target, 0) == expected_fibre,
                    ("fibre", ring.name, m, k, t, target))

        actual_cdf = sum(distance <= t
                         for distance, _ in summary.tail_cycle.values())
        formula_cdf = q ** (m - m // g_t + perpendicular)
        A.check(actual_cdf == formula_cdf,
                ("depth CDF", ring.name, m, k, t, actual_cdf, formula_cdf))
        if t <= height:
            actual_layer = sum(distance == t
                               for distance, _ in summary.tail_cycle.values())
            A.check(actual_layer == formula_cdf - previous_cdf,
                    ("depth layer", ring.name, m, k, t))
            previous_cdf = formula_cdf

    A.check(gcd_sequence[height] == parallel)
    A.check(all(value == parallel for value in gcd_sequence[height:]))
    for t in range(height):
        A.check(gcd_sequence[t] < parallel,
                ("premature stabilization", ring.name, m, k, t))

    permutation_order = multiplicative_order(k, perpendicular)
    formula_cycle_hist: dict[int, int] = {}
    fixed_counts: dict[int, int] = {}
    for r in range(1, 2 * permutation_order + 1):
        multiplier = pow(k, r, perpendicular) if perpendicular > 1 else 0
        direct_position_cycles = position_cycle_count_direct(perpendicular, multiplier)
        divisor_position_cycles = position_cycle_count_divisors(perpendicular, k, r)
        A.check(direct_position_cycles == divisor_position_cycles,
                ("position cycles", ring.name, m, k, r))
        formula_fixed = q ** direct_position_cycles
        actual_fixed = sum(literal_iterate(state, ring, m, k, r) == state
                           for state in states)
        A.check(actual_fixed == formula_fixed,
                ("fixed count", ring.name, m, k, r, actual_fixed, formula_fixed))
        fixed_counts[r] = formula_fixed

    for period in divisors(permutation_order):
        least_period_points = sum(
            mobius(period // divisor) * fixed_counts[divisor]
            for divisor in divisors(period)
        )
        A.check(least_period_points % period == 0)
        formula_cycle_hist[period] = least_period_points // period
    formula_cycle_hist = {period: count for period, count in formula_cycle_hist.items()
                          if count}
    A.check(dict(summary.cycle_hist) == formula_cycle_hist,
            ("cycle histogram", ring.name, m, k,
             summary.cycle_hist, formula_cycle_hist))

    CASE_RESULTS[(ring.name, m, k)] = summary
    emit(
        f"SIG ring={ring.name} q={q} m={m} k={k} states={len(states)} "
        f"parallel={parallel} perpendicular={perpendicular} height={height} "
        f"fixed={summary.fixed} periodic={summary.periodic} "
        f"components={summary.components} max_tail={summary.max_tail} "
        f"cycles={format_hist(summary.cycle_hist)} "
        f"indegrees={format_hist(summary.indegree_hist)} "
        f"edge_sha16={summary.edge_sha16}"
    )
    A.box()


def boundary_and_counterexample_checks() -> None:
    # gcd(k,m) need not be the stable gcd: the first image can contain tails.
    parallel, height = parallel_part_and_height(12, 6)
    A.check((parallel, height) == (12, 2))
    A.check([gcd(pow(6, t), 12) for t in range(4)] == [1, 6, 12, 12])
    ring = ZnRing(2)
    basis_six = tuple(1 if index == 6 else 0 for index in range(12))
    A.check(in_support_module(basis_six, ring, 6))
    A.check(not in_support_module(basis_six, ring, 12))
    A.check(literal_once(basis_six, ring, 12, 6)[0] == 1)

    # A scalar logarithm is not the stabilization height.
    parallel_48, height_48 = parallel_part_and_height(48, 6)
    A.check((parallel_48, height_48) == (48, 4))
    A.check([gcd(pow(6, t), 48) for t in range(6)] == [1, 6, 12, 24, 48, 48])
    A.check(6 ** 3 >= 48 and height_48 != 3)

    # v_l(k) changes the clock: height is not max_l v_l(m).
    A.check(parallel_part_and_height(16, 4) == (16, 2))

    # Same cardinality, different nonfield additive groups: claimed counts agree.
    z4 = CASE_RESULTS[("Z4", 4, 2)]
    klein = CASE_RESULTS[("Z2xZ2", 4, 2)]
    A.check((z4.fixed, z4.periodic, z4.components, z4.max_tail,
             z4.cycle_hist, z4.indegree_hist) ==
            (klein.fixed, klein.periodic, klein.components, klein.max_tail,
             klein.cycle_hist, klein.indegree_hist))

    # Degenerate legal boundaries in the corrected contract.
    A.check(parallel_part_and_height(1, 37) == (1, 0))
    A.check(parallel_part_and_height(15, 2) == (1, 0))

    emit("COUNTEREXAMPLE gcd1_not_stable m=12 k=6 gcds=1,6,12,12 height=2")
    emit("COUNTEREXAMPLE scalar_log_height_false m=48 k=6 gcds=1,6,12,24,48,48 height=4")
    emit("COUNTEREXAMPLE max_prime_exponent_height_false m=16 k=4 height=2")
    emit("NONFIELD cardinality_only_counts Z4_vs_Z2xZ2 m=4 k=2 status=MATCH")


def main() -> None:
    emit("P157_P161_SCE_FOCUSED_EXACT_AUDIT")
    emit("external_status=HOLD_EXTERNAL")
    emit("research_verdict=KILL_INTERNAL_ENGINE_TRANSFER")
    emit("path_a=REPEATED_LITERAL_SUBSTITUTION")
    emit("path_b=DIRECT_CONGRUENCE_CLASS_PUSHFORWARD")
    emit("enumeration_role=COUNTEREXAMPLE_PRESSURE_ONLY")

    cases = (
        (ZnRing(2), 1, 1),
        (ZnRing(2), 5, 2),
        (ZnRing(2), 6, 2),
        (ZnRing(2), 8, 4),
        (ZnRing(2), 12, 6),
        (ZnRing(3), 6, 3),
        (ZnRing(4), 4, 2),
        (ProductRing((2, 2)), 4, 2),
        (ZnRing(4), 6, 2),
        (ZnRing(6), 4, 2),
        (ZnRing(4), 3, 3),
        (ZnRing(8), 4, 4),
    )
    for ring, m, k in cases:
        run_case(ring, m, k)
    boundary_and_counterexample_checks()

    emit(f"boxes={A.boxes}")
    emit(f"assertions={A.assertions}")
    emit("status=PASS")
    print("\n".join(LINES))


if __name__ == "__main__":
    main()
