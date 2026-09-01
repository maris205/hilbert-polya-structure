#!/usr/bin/env python3
"""Exact controls for P141.

This deterministic program uses integers and fractions.Fraction only.  It has
no floating point, sampling, seed, network access, timestamp, or third-party
dependency.  Its stdout is frozen byte-for-byte in verification_output.txt.
"""

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product


ASSERTIONS = 0


def check(condition, payload=None):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(payload)


def adjacent(bits, left, right):
    if left == right:
        return False
    if left > right:
        left, right = right, left
    return bits[right] == 1


def exact_distribution(bits, weights):
    @lru_cache(maxsize=None)
    def recurse(active):
        if not active:
            return {(): Fraction(1)}
        total = sum(weights[vertex] for vertex in active)
        answer = defaultdict(Fraction)
        for vertex in active:
            residual = tuple(
                other for other in active
                if other != vertex and not adjacent(bits, other, vertex)
            )
            for endpoint, mass in recurse(residual).items():
                chosen = tuple(sorted((vertex,) + endpoint))
                answer[chosen] += Fraction(weights[vertex], total) * mass
        return dict(answer)

    return recurse(tuple(range(len(bits))))


def endpoint_for_dominant(bits, dominant):
    return tuple(
        [dominant]
        + [index for index in range(dominant + 1, len(bits)) if bits[index] == 0]
    )


def stick_distribution(bits, weights):
    prefix_weights = []
    running = 0
    for weight in weights:
        running += weight
        prefix_weights.append(running)
    dominant = [index for index, bit in enumerate(bits) if bit == 1]
    survival = Fraction(1)
    answer = {}
    for vertex in reversed(dominant):
        answer[endpoint_for_dominant(bits, vertex)] = (
            survival * Fraction(weights[vertex], prefix_weights[vertex])
        )
        survival *= Fraction(
            prefix_weights[vertex] - weights[vertex], prefix_weights[vertex]
        )
    zero_endpoint = tuple(index for index, bit in enumerate(bits) if bit == 0)
    answer[zero_endpoint] = survival
    return answer


def size_pgf(distribution):
    answer = defaultdict(Fraction)
    for endpoint, mass in distribution.items():
        answer[len(endpoint)] += mass
    return dict(answer)


def audit_inverse_marginals(bits, weights, distribution):
    n = len(bits)
    dominant = [index for index, bit in enumerate(bits) if bit == 1]
    zeros = [index for index, bit in enumerate(bits) if bit == 0]
    prefix_weights = []
    running = 0
    for weight in weights:
        running += weight
        prefix_weights.append(running)

    p_zero = distribution[tuple(zeros)]
    terminal_mass = {
        vertex: distribution.get(endpoint_for_dominant(bits, vertex), Fraction(0))
        for vertex in dominant
    }
    for vertex in dominant:
        reverse_survival = p_zero + sum(
            (terminal_mass[other] for other in dominant if other <= vertex),
            Fraction(0),
        )
        recovered = terminal_mass[vertex] / reverse_survival
        expected = Fraction(weights[vertex], prefix_weights[vertex])
        check(recovered == expected, (bits, weights, vertex, recovered, expected))

    marginals = {}
    for vertex in range(n):
        direct = sum(
            (mass for endpoint, mass in distribution.items() if vertex in endpoint),
            Fraction(0),
        )
        if bits[vertex] == 1:
            expected = terminal_mass[vertex]
        else:
            expected = Fraction(1)
            for later in dominant:
                if later > vertex:
                    expected *= Fraction(
                        prefix_weights[later] - weights[later],
                        prefix_weights[later],
                    )
        check(direct == expected, (bits, weights, vertex, direct, expected))
        marginals[vertex] = direct

    for position, left in enumerate(zeros):
        for right in zeros[position + 1:]:
            joint = sum(
                (
                    mass for endpoint, mass in distribution.items()
                    if left in endpoint and right in endpoint
                ),
                Fraction(0),
            )
            check(joint == marginals[left], (bits, weights, left, right, joint))


def audit_simplex(bits):
    dominant = [index for index, bit in enumerate(bits) if bit == 1]
    if not dominant:
        check(stick_distribution(bits, tuple(1 for _ in bits)) == {
            tuple(range(len(bits))): Fraction(1)
        })
        return

    raw = [1] + list(range(2, len(dominant) + 2))
    denominator = sum(raw)
    p_zero = Fraction(raw[0], denominator)
    p_dominant = {
        vertex: Fraction(raw[position + 1], denominator)
        for position, vertex in enumerate(dominant)
    }
    hazards = {}
    for vertex in dominant:
        survival = p_zero + sum(
            (p_dominant[other] for other in dominant if other <= vertex),
            Fraction(0),
        )
        hazards[vertex] = p_dominant[vertex] / survival
        check(0 < hazards[vertex] < 1, (bits, vertex, hazards[vertex]))

    weights = []
    prefix = Fraction(0)
    for vertex, bit in enumerate(bits):
        if bit == 0:
            weight = Fraction(1)
        else:
            hazard = hazards[vertex]
            weight = hazard * prefix / (1 - hazard)
        check(weight > 0, (bits, vertex, weight))
        weights.append(weight)
        prefix += weight

    realized = stick_distribution(bits, tuple(weights))
    check(realized[tuple(index for index, bit in enumerate(bits) if bit == 0)] == p_zero)
    for vertex in dominant:
        check(realized[endpoint_for_dominant(bits, vertex)] == p_dominant[vertex])


def ct_laplace(bits, weights, s):
    @lru_cache(maxsize=None)
    def recurse(active):
        if not active:
            return Fraction(1)
        total = sum(weights[vertex] for vertex in active)
        numerator = Fraction(0)
        for vertex in active:
            residual = tuple(
                other for other in active
                if other != vertex and not adjacent(bits, other, vertex)
            )
            numerator += weights[vertex] * recurse(residual)
        return numerator / (total + s)

    return recurse(tuple(range(len(bits))))


def permutation_ct_laplace(bits, weights, s):
    """Independent full-priority enumeration of max accepted absolute label."""
    n = len(bits)
    answer = Fraction(0)
    for order in permutations(range(n)):
        remaining = sum(weights)
        order_mass = Fraction(1)
        accepted = []
        last_accepted_position = -1
        rates_before = []
        for position, vertex in enumerate(order):
            rates_before.append(remaining)
            order_mass *= Fraction(weights[vertex], remaining)
            remaining -= weights[vertex]
            if all(not adjacent(bits, vertex, chosen) for chosen in accepted):
                accepted.append(vertex)
                last_accepted_position = position
        conditional_transform = Fraction(1)
        for rate in rates_before[:last_accepted_position + 1]:
            conditional_transform *= Fraction(rate, rate + s)
        answer += order_mass * conditional_transform
    return answer


def verify():
    parameter_inputs = 0
    endpoint_cells = 0
    pgf_cells = 0
    max_support = 0

    for n in range(1, 7):
        for tail in product((0, 1), repeat=n - 1):
            bits = (0,) + tail
            for weights in product((1, 2, 3), repeat=n):
                direct = exact_distribution(bits, weights)
                formula = stick_distribution(bits, weights)
                check(sum(direct.values()) == 1, (bits, weights, direct))
                check(sum(formula.values()) == 1, (bits, weights, formula))
                check(direct == formula, (bits, weights, direct, formula))
                check(size_pgf(direct) == size_pgf(formula), (bits, weights))
                audit_inverse_marginals(bits, weights, direct)
                for endpoint in set(direct) | set(formula):
                    check(direct.get(endpoint, 0) == formula.get(endpoint, 0))
                    endpoint_cells += 1
                for degree in set(size_pgf(direct)) | set(size_pgf(formula)):
                    check(
                        size_pgf(direct).get(degree, 0)
                        == size_pgf(formula).get(degree, 0)
                    )
                    pgf_cells += 1
                parameter_inputs += 1
                max_support = max(max_support, len(direct))

    for n in range(7, 11):
        profiles = (
            tuple(1 for _ in range(n)),
            tuple(index + 1 for index in range(n)),
            tuple(n - index for index in range(n)),
            tuple(1 + ((index * index + 2 * index + 3) % 7) for index in range(n)),
        )
        for tail in product((0, 1), repeat=n - 1):
            bits = (0,) + tail
            for weights in profiles:
                direct = exact_distribution(bits, weights)
                formula = stick_distribution(bits, weights)
                check(direct == formula, (bits, weights))
                check(sum(direct.values()) == 1, (bits, weights))
                check(size_pgf(direct) == size_pgf(formula), (bits, weights))
                audit_inverse_marginals(bits, weights, direct)
                parameter_inputs += 1
                endpoint_cells += len(set(direct) | set(formula))
                pgf_cells += len(set(size_pgf(direct)) | set(size_pgf(formula)))
                max_support = max(max_support, len(direct))

    simplex_inputs = 0
    for n in range(1, 11):
        for tail in product((0, 1), repeat=n - 1):
            audit_simplex((0,) + tail)
            simplex_inputs += 1

    clock_inputs = 0
    clock_profiles = lambda n: (
        tuple(1 for _ in range(n)),
        tuple(index + 1 for index in range(n)),
        tuple(1 + ((3 * index + 1) % 5) for index in range(n)),
    )
    for n in range(1, 7):
        for tail in product((0, 1), repeat=n - 1):
            bits = (0,) + tail
            for weights in clock_profiles(n):
                for s in (1, 2, 3):
                    check(
                        ct_laplace(bits, weights, s)
                        == permutation_ct_laplace(bits, weights, s),
                        (bits, weights, s),
                    )
                    clock_inputs += 1

    # Exact vocabulary firewall on a two-vertex clique with rates 1 and 2.
    tau_transform = ct_laplace((0, 1), (1, 2), 1)
    full_priority_span_transform = Fraction(1, 3) * Fraction(2, 3) + Fraction(2, 3) * Fraction(1, 2)
    accepted_count_pgf_half = Fraction(1, 2)
    check(tau_transform == Fraction(3, 4))
    check(full_priority_span_transform == Fraction(5, 9))
    check(len({tau_transform, full_priority_span_transform, accepted_count_pgf_half}) == 3)

    return (
        parameter_inputs,
        endpoint_cells,
        pgf_cells,
        simplex_inputs,
        clock_inputs,
        max_support,
    )


if __name__ == "__main__":
    report = verify()
    print("P141_WEIGHTED_THRESHOLD_GREEDY_MIS")
    print("arithmetic=fractions.Fraction; sampling=none; third_party=none")
    print(f"parameter_inputs={report[0]}")
    print(f"endpoint_cells={report[1]}")
    print(f"size_pgf_cells={report[2]}")
    print(f"simplex_realization_inputs={report[3]}")
    print(f"clock_transform_inputs={report[4]}")
    print(f"max_endpoint_support={report[5]}")
    print(f"exact_assertions={ASSERTIONS}")
    print("checks=endpoint,reverse_stick,hazard_inverse,simplex,size_pgf,marginals,nesting,clock_recursion,vocabulary_firewall")
    print("status=PASS")
