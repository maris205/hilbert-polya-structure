#!/usr/bin/env python3
"""Reviewer-owned exact control for P170 Hostile Review B.

No author, scouting, or Review-A module is imported.  Unlike the author
verifier's literal permutation tuples, dense bit masks, and dense coefficient
vectors, this control represents states as frozensets and polynomials as
sparse degree/coefficient pairs.  Its one-epoch atoms are derived from a
cycle-containing-the-smallest-label recurrence for derangements with a
prescribed exact fixed set.  Endpoint histories are then propagated through
that independently constructed exact-fixed-set inventory.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from functools import cache
from pathlib import Path


Sparse = tuple[tuple[int, int], ...]
ZERO: Sparse = ()
ONE: Sparse = ((0, 1),)


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)

    def equal(self, left, right, label: str) -> None:
        self.assertions += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")


A = Audit()


def normalize(terms) -> Sparse:
    coefficients = Counter()
    for degree, coefficient in terms:
        coefficients[degree] += coefficient
    return tuple(sorted((degree, coefficient) for degree, coefficient in coefficients.items()
                        if coefficient))


def add(left: Sparse, right: Sparse) -> Sparse:
    return normalize((*left, *right))


def scale(polynomial: Sparse, scalar: int) -> Sparse:
    if scalar == 0:
        return ZERO
    return tuple((degree, scalar * coefficient) for degree, coefficient in polynomial)


def multiply(left: Sparse, right: Sparse) -> Sparse:
    if not left or not right:
        return ZERO
    return normalize(
        (first_degree + second_degree, first * second)
        for first_degree, first in left
        for second_degree, second in right
    )


def shift(polynomial: Sparse, amount: int) -> Sparse:
    return tuple((degree + amount, coefficient) for degree, coefficient in polynomial)


@cache
def power(polynomial: Sparse, exponent: int) -> Sparse:
    answer = ONE
    base = polynomial
    while exponent:
        if exponent & 1:
            answer = multiply(answer, base)
        base = multiply(base, base)
        exponent //= 2
    return answer


def value(polynomial: Sparse, argument=1):
    return sum(coefficient * argument**degree for degree, coefficient in polynomial)


def derivative_at_one(polynomial: Sparse) -> int:
    return sum(degree * coefficient for degree, coefficient in polynomial)


def degrees(polynomial: Sparse):
    return tuple(degree for degree, _ in polynomial)


@cache
def ordinary_cycle_polynomial(size: int) -> Sparse:
    """Unsigned Stirling cycle polynomial, built by insertion recurrence."""
    polynomial = ONE
    for old_size in range(size):
        polynomial = multiply(polynomial, normalize(((0, old_size), (1, 1))))
    return polynomial


@cache
def derangement_cycle_polynomial(size: int) -> Sparse:
    """Cycle inventory of permutations with no fixed points.

    The cycle containing the smallest label has length ell>=2.  Choose and
    cyclically order its ell-1 companions, then derange the remainder.
    """
    if size == 0:
        return ONE
    total = ZERO
    for length in range(2, size + 1):
        multiplicity = math.comb(size - 1, length - 1) * math.factorial(length - 1)
        term = scale(shift(derangement_cycle_polynomial(size - length), 1), multiplicity)
        total = add(total, term)
    return total


@cache
def exact_fixed_set_polynomial(n: int, fixed_size: int) -> Sparse:
    return shift(derangement_cycle_polynomial(n - fixed_size), fixed_size)


@cache
def prescribed_fixed_polynomial(n: int, fixed_size: int) -> Sparse:
    return shift(ordinary_cycle_polynomial(n - fixed_size), fixed_size)


@cache
def transition_polynomial(n: int, current_size: int, target_size: int) -> Sparse:
    """One-step cycle inventory from a fixed current set to a fixed target."""
    total = ZERO
    outside = n - current_size
    for extra_fixed in range(outside + 1):
        exact_size = target_size + extra_fixed
        term = scale(
            exact_fixed_set_polynomial(n, exact_size),
            math.comb(outside, extra_fixed),
        )
        total = add(total, term)
    return total


@cache
def closed_marked(n: int, a: int, b: int, time: int) -> Sparse:
    total = ZERO
    for chosen in range(a - b + 1):
        term = power(prescribed_fixed_polynomial(n, b + chosen), time)
        total = add(total, scale(term, (-1) ** chosen * math.comb(a - b, chosen)))
    return total


def closed_count(n: int, a: int, b: int, time: int) -> int:
    return sum(
        (-1) ** chosen
        * math.comb(a - b, chosen)
        * math.factorial(n - b - chosen) ** time
        for chosen in range(a - b + 1)
    )


@cache
def harmonic(size: int) -> Fraction:
    return sum((Fraction(1, q) for q in range(1, size + 1)), Fraction())


def closed_derivative(n: int, a: int, b: int, time: int) -> Fraction:
    return sum(
        Fraction(
            (-1) ** chosen
            * math.comb(a - b, chosen)
            * math.factorial(n - b - chosen) ** time
            * time
        )
        * (b + chosen + harmonic(n - b - chosen))
        for chosen in range(a - b + 1)
    )


def supported(n: int, a: int, b: int) -> bool:
    return not (a == n and b == n - 1)


@cache
def subsets(state: frozenset[int]):
    ordered = tuple(sorted(state))
    return tuple(
        frozenset(choice)
        for size in range(len(ordered) + 1)
        for choice in itertools.combinations(ordered, size)
    )


def verify_cycle_inventories():
    before = A.assertions
    rows = {}
    for n in range(0, 33):
        ordinary = ordinary_cycle_polynomial(n)
        A.equal(value(ordinary), math.factorial(n), f"ordinary cycle mass n={n}")
        deranged = derangement_cycle_polynomial(n)
        rencontres = sum(
            (-1) ** chosen * math.comb(n, chosen) * math.factorial(n - chosen)
            for chosen in range(n + 1)
        )
        A.equal(value(deranged), rencontres, f"derangement mass n={n}")
        recombined = ZERO
        for fixed_size in range(n + 1):
            recombined = add(
                recombined,
                scale(exact_fixed_set_polynomial(n, fixed_size), math.comb(n, fixed_size)),
            )
        A.equal(recombined, ordinary, f"exact fixed sets partition S_n n={n}")
        for fixed_size in range(n + 1):
            prescribed = ZERO
            for extra in range(n - fixed_size + 1):
                prescribed = add(
                    prescribed,
                    scale(
                        exact_fixed_set_polynomial(n, fixed_size + extra),
                        math.comb(n - fixed_size, extra),
                    ),
                )
            A.equal(prescribed, prescribed_fixed_polynomial(n, fixed_size),
                    f"prescribed/exact fixed inventory n={n},s={fixed_size}")
        rows[str(n)] = {
            "cycle_coefficients": len(ordinary),
            "derangement_coefficients": len(deranged),
            "derangements": value(deranged),
        }
    return A.assertions - before, rows


def verify_endpoint_dynamic():
    """Propagate exact-fixed-set inventories on frozenset states."""
    before = A.assertions
    digest = hashlib.sha256()
    rows = {}
    for n in range(1, 9):
        ground = frozenset(range(n))
        states = subsets(ground)
        for current in states:
            direct_mass = sum(
                value(transition_polynomial(n, len(current), len(target)))
                for target in subsets(current)
            )
            A.equal(direct_mass, math.factorial(n), f"transition row mass n={n}")

        histories = {source: {source: ONE} for source in states}
        supported_pairs = 0
        for time in range(0, 5):
            for source in states:
                a = len(source)
                for target in states:
                    got = histories[source].get(target, ZERO)
                    expected = (
                        closed_marked(n, a, len(target), time)
                        if target <= source
                        else ZERO
                    )
                    A.equal(got, expected,
                            f"marked endpoint n={n},t={time},A={source},B={target}")
                    A.check(all(coefficient >= 0 for _, coefficient in got),
                            f"literal sparse coefficients nonnegative n={n},t={time}")
                    if target <= source:
                        A.equal(value(got), closed_count(n, a, len(target), time),
                                f"unmarked specialization n={n},t={time}")
                        if not target and source:
                            denominator = math.factorial(n) ** time
                            cdf = Fraction(value(got), denominator)
                            spectral_cdf = sum(
                                (-1) ** chosen
                                * math.comb(a, chosen)
                                * Fraction(math.factorial(n - chosen), math.factorial(n)) ** time
                                for chosen in range(a + 1)
                            )
                            A.equal(cdf, spectral_cdf,
                                    f"absorption CDF n={n},a={a},t={time}")
                        if time == 0:
                            A.equal(bool(got), source == target,
                                    f"zero-time Kronecker endpoint n={n}")
                        else:
                            positive = supported(n, a, len(target))
                            A.equal(bool(got), positive, f"positive-time support n={n}")
                            if positive:
                                supported_pairs += 1
                                endpoint_degrees = degrees(got)
                                A.equal(min(endpoint_degrees),
                                        time * (len(target) + (len(target) < n)),
                                        f"sharp low degree n={n},t={time}")
                                A.equal(max(endpoint_degrees),
                                        time * n - math.ceil((a - len(target)) / 2),
                                        f"sharp high degree n={n},t={time}")
                                A.equal(Fraction(derivative_at_one(got)),
                                        closed_derivative(n, a, len(target), time),
                                        f"marked derivative n={n},t={time}")
                                A.equal(
                                    Fraction(derivative_at_one(got), value(got)),
                                    closed_derivative(n, a, len(target), time)
                                    / closed_count(n, a, len(target), time),
                                    f"conditional cycle mean n={n},t={time}",
                                )
                    digest.update(
                        f"{n}|{time}|{tuple(sorted(source))}|{tuple(sorted(target))}|{got}\n".encode()
                    )
            if time < 4:
                following = {}
                for source, distribution in histories.items():
                    next_distribution = {}
                    for current, old_polynomial in distribution.items():
                        for target in subsets(current):
                            step = transition_polynomial(n, len(current), len(target))
                            product_polynomial = multiply(old_polynomial, step)
                            if product_polynomial:
                                next_distribution[target] = add(
                                    next_distribution.get(target, ZERO), product_polynomial
                                )
                    following[source] = next_distribution
                histories = following
        rows[str(n)] = {
            "states": len(states),
            "supported_checks": supported_pairs,
        }
    return A.assertions - before, rows, digest.hexdigest()


def verify_containment_spectrum():
    before = A.assertions
    rows = {}
    for n in range(1, 10):
        ground = frozenset(range(n))
        states = subsets(ground)
        factorial = math.factorial(n)
        for current in states:
            targets = subsets(current)
            counts = {
                target: value(transition_polynomial(n, len(current), len(target)))
                for target in targets
            }
            for eigen_set in states:
                action = sum(count for target, count in counts.items() if eigen_set <= target)
                expected = (
                    math.factorial(n - len(eigen_set)) if eigen_set <= current else 0
                )
                A.equal(action, expected,
                        f"containment eigenvector n={n},A={current},S={eigen_set}")

        # Explicit Boolean zeta/Mobius inverse in the paper's orientation.
        for row_state in states:
            for column_state in states:
                inverse_product = sum(
                    (-1) ** (len(intermediate) - len(column_state))
                    for intermediate in subsets(row_state)
                    if column_state <= intermediate
                )
                A.equal(inverse_product, int(row_state == column_state),
                        f"Boolean zeta/Mobius inverse n={n}")

        eigenvalues = [Fraction(math.factorial(n - rank), factorial) for rank in range(n + 1)]
        collisions = [
            (left, right)
            for left in range(n + 1)
            for right in range(left + 1, n + 1)
            if eigenvalues[left] == eigenvalues[right]
        ]
        A.equal(collisions, [(n - 1, n)], f"sole rank collision n={n}")
        rows[str(n)] = {
            "states": len(states),
            "eigenvalues": [str(x) for x in eigenvalues],
        }
    return A.assertions - before, rows


def closed_mean(n: int, size: int) -> Fraction:
    return sum(
        Fraction((-1) ** (chosen + 1) * math.comb(size, chosen), 1)
        / (1 - Fraction(math.factorial(n - chosen), math.factorial(n)))
        for chosen in range(1, size + 1)
    )


def closed_second(n: int, size: int) -> Fraction:
    total = Fraction()
    for chosen in range(1, size + 1):
        eigenvalue = Fraction(math.factorial(n - chosen), math.factorial(n))
        total += (
            (-1) ** (chosen + 1)
            * math.comb(size, chosen)
            * (1 + eigenvalue)
            / (1 - eigenvalue) ** 2
        )
    return total


def closed_pgf(n: int, size: int, argument: Fraction) -> Fraction:
    tail_transform = Fraction()
    for chosen in range(1, size + 1):
        eigenvalue = Fraction(math.factorial(n - chosen), math.factorial(n))
        tail_transform += Fraction((-1) ** (chosen + 1) * math.comb(size, chosen), 1) / (
            1 - argument * eigenvalue
        )
    return 1 - (1 - argument) * tail_transform


def verify_absorption_transforms():
    """Solve the full labelled triangular chain, not its size projection."""
    before = A.assertions
    rows = {}
    pgf_arguments = (Fraction(-1, 2), Fraction(1, 2), Fraction(3, 2))
    for n in range(2, 10):
        states = subsets(frozenset(range(n)))
        factorial = math.factorial(n)
        means = {frozenset(): Fraction()}
        seconds = {frozenset(): Fraction()}
        pgfs = {argument: {frozenset(): Fraction(1)} for argument in pgf_arguments}
        for state in sorted((state for state in states if state), key=lambda x: (len(x), tuple(x))):
            transitions = {
                target: Fraction(
                    value(transition_polynomial(n, len(state), len(target))), factorial
                )
                for target in subsets(state)
            }
            A.equal(sum(transitions.values()), 1, f"absorbing row stochastic n={n}")
            self_probability = transitions[state]
            proper = [target for target in subsets(state) if target != state]
            denominator = 1 - self_probability
            mean = (
                1 + sum(transitions[target] * means[target] for target in proper)
            ) / denominator
            means[state] = mean
            A.equal(mean, closed_mean(n, len(state)), f"full-lattice mean n={n}")

            second = (
                1
                + 2 * (mean - 1)
                + sum(transitions[target] * seconds[target] for target in proper)
            ) / denominator
            seconds[state] = second
            A.equal(second, closed_second(n, len(state)), f"full-lattice second moment n={n}")

            for argument in pgf_arguments:
                pgf = (
                    argument
                    * sum(transitions[target] * pgfs[argument][target] for target in proper)
                    / (1 - argument * self_probability)
                )
                pgfs[argument][state] = pgf
                A.equal(pgf, closed_pgf(n, len(state), argument),
                        f"full-lattice PGF n={n},s={argument}")
        full = frozenset(range(n))
        rows[str(n)] = {
            "full_mean": str(means[full]),
            "full_second_moment": str(seconds[full]),
            "full_pgf": {str(argument): str(pgfs[argument][full]) for argument in pgf_arguments},
        }
    return A.assertions - before, rows


def survival(n: int, size: int, time: int) -> Fraction:
    return sum(
        Fraction(
            (-1) ** (chosen + 1)
            * math.comb(size, chosen)
            * math.factorial(n - chosen) ** time,
            math.factorial(n) ** time,
        )
        for chosen in range(1, size + 1)
    )


def verify_low_dimensions_and_scales():
    before = A.assertions
    # n=1: the sole nonempty point is immortal.
    for time in range(0, 25):
        A.equal(survival(1, 1, time), 1, f"n=1 immortal t={time}")
    for time in range(0, 25):
        for size in (1, 2):
            A.equal(survival(2, size, time), Fraction(1, 2) ** time,
                    f"n=2 merged scale a={size},t={time}")
        for size in (1, 2, 3):
            expected = (
                size * Fraction(1, 3) ** time
                - (math.comb(size, 2) - math.comb(size, 3)) * Fraction(1, 6) ** time
            )
            A.equal(survival(3, size, time), expected,
                    f"n=3 terminal collision a={size},t={time}")

    bound_checks = 0
    for n in range(4, 41):
        lambdas = [Fraction(math.factorial(n - rank), math.factorial(n))
                   for rank in range(n + 1)]
        A.check(lambdas[1] > lambdas[2] > lambdas[3], f"n={n} two distinct leading scales")
        for size in range(1, n + 1):
            for time in range(0, 17):
                residual = (
                    survival(n, size, time)
                    - size * lambdas[1] ** time
                    + math.comb(size, 2) * lambdas[2] ** time
                )
                envelope = sum(math.comb(size, chosen) for chosen in range(3, size + 1)) * (
                    lambdas[3] ** time
                )
                A.check(abs(residual) <= envelope,
                        f"n={n} O(lambda_3^t) envelope a={size},t={time}")
                bound_checks += 1
    return A.assertions - before, {
        "n1_times": 25,
        "n2_n3_times": 25,
        "two_scale_n_range": [4, 40],
        "two_scale_exact_envelope_checks": bound_checks,
    }


def verify_uniform_marked_formulas():
    before = A.assertions
    parity = Counter()
    endpoint_checks = 0
    for n in range(1, 33):
        for a in range(n + 1):
            for b in range(a + 1):
                d = a - b
                parity["d=0" if d == 0 else "d=1" if d == 1 else "d-even" if d % 2 == 0 else "d-odd"] += 1
                for time in range(1, 6):
                    polynomial = closed_marked(n, a, b, time)
                    expected_positive = supported(n, a, b)
                    A.equal(bool(polynomial), expected_positive,
                            f"uniform marked support n={n},a={a},b={b},t={time}")
                    A.check(all(coefficient >= 0 for _, coefficient in polynomial),
                            f"uniform coefficient nonnegativity n={n},a={a},b={b},t={time}")
                    if expected_positive:
                        support_degrees = degrees(polynomial)
                        A.equal(min(support_degrees), time * (b + (b < n)),
                                f"uniform sharp low n={n},a={a},b={b},t={time}")
                        A.equal(max(support_degrees), time * n - math.ceil(d / 2),
                                f"uniform sharp high n={n},a={a},b={b},t={time}")
                        mass = value(polynomial)
                        A.equal(mass, closed_count(n, a, b, time),
                                f"uniform unmarked specialization n={n},a={a},b={b},t={time}")
                        derivative = derivative_at_one(polynomial)
                        A.equal(Fraction(derivative), closed_derivative(n, a, b, time),
                                f"uniform conditional numerator n={n},a={a},b={b},t={time}")
                        conditional_mean = Fraction(derivative, mass)
                        A.equal(
                            conditional_mean,
                            closed_derivative(n, a, b, time) / closed_count(n, a, b, time),
                            f"uniform conditional mean n={n},a={a},b={b},t={time}",
                        )
                        A.check(min(support_degrees) <= conditional_mean <= max(support_degrees),
                                f"uniform conditional mean range n={n},a={a},b={b},t={time}")
                    endpoint_checks += 1
    return A.assertions - before, {
        "n_range": [1, 32],
        "times": [1, 2, 3, 4, 5],
        "endpoint_time_checks": endpoint_checks,
        "degree_classes": dict(sorted(parity.items())),
    }


def cycle_deficit(cycles) -> int:
    return sum(len(cycle) - 1 for cycle in cycles)


def moved_support(cycles):
    return frozenset().union(*cycles) if cycles else frozenset()


def verify_sharp_witnesses():
    """Cycle-block witnesses, without constructing permutation tuples."""
    before = A.assertions
    classes = Counter()
    time = 4
    witness_count = 0
    for n in range(1, 101):
        ground = frozenset(range(n))
        for a in range(n + 1):
            source = frozenset(range(a))
            for b in range(a + 1):
                if not supported(n, a, b):
                    continue
                target = frozenset(range(b))
                lost = tuple(range(b, a))
                d = len(lost)
                complement = ground - target

                low_cycles = (complement,) if len(complement) >= 2 else ()
                low_endpoint = source - moved_support(low_cycles)
                A.equal(low_endpoint, target, f"low witness endpoint n={n},a={a},b={b}")
                low_total_cycles = time * (n - cycle_deficit(low_cycles))
                A.equal(low_total_cycles, time * (b + (b < n)),
                        f"low witness degree n={n},a={a},b={b}")

                if d == 0:
                    high_cycles = ()
                    classes["d=0"] += 1
                elif d == 1:
                    A.check(a < n, f"d=1 helper exists n={n},a={a},b={b}")
                    high_cycles = (frozenset((lost[0], a)),)
                    classes["d=1"] += 1
                elif d % 2 == 0:
                    high_cycles = tuple(frozenset(lost[q:q + 2]) for q in range(0, d, 2))
                    classes["d-even"] += 1
                else:
                    high_cycles = (frozenset(lost[:3]),) + tuple(
                        frozenset(lost[q:q + 2]) for q in range(3, d, 2)
                    )
                    classes["d-odd"] += 1
                A.check(all(cycle.isdisjoint(target) for cycle in high_cycles),
                        f"high witness fixes target n={n},a={a},b={b}")
                high_endpoint = source - moved_support(high_cycles)
                A.equal(high_endpoint, target, f"high witness endpoint n={n},a={a},b={b}")
                high_total_cycles = time * n - cycle_deficit(high_cycles)
                A.equal(high_total_cycles, time * n - math.ceil(d / 2),
                        f"high witness degree n={n},a={a},b={b}")
                witness_count += 1
    return A.assertions - before, {
        "n_range": [1, 100],
        "time": time,
        "witnesses": witness_count,
        "degree_classes": dict(sorted(classes.items())),
    }


def main():
    inventory_assertions, inventory_rows = verify_cycle_inventories()
    dynamic_assertions, dynamic_rows, dynamic_digest = verify_endpoint_dynamic()
    spectrum_assertions, spectrum_rows = verify_containment_spectrum()
    absorption_assertions, absorption_rows = verify_absorption_transforms()
    low_assertions, low_rows = verify_low_dimensions_and_scales()
    uniform_assertions, uniform_rows = verify_uniform_marked_formulas()
    witness_assertions, witness_rows = verify_sharp_witnesses()

    result = {
        "assertions": A.assertions,
        "decision": "REVIEW_B_INDEPENDENT_CONTROL_PASS",
        "external_status": "HOLD_EXTERNAL",
        "implementation": "frozenset states / sparse polynomials / derangement-cycle recurrence",
        "sections": {
            "cycle_inventories": {"assertions": inventory_assertions, "rows": inventory_rows},
            "endpoint_dynamic": {
                "assertions": dynamic_assertions,
                "rows": dynamic_rows,
                "payload_sha256": dynamic_digest,
            },
            "containment_spectrum": {"assertions": spectrum_assertions, "rows": spectrum_rows},
            "absorption_transforms": {"assertions": absorption_assertions, "rows": absorption_rows},
            "low_dimensions_and_scales": {"assertions": low_assertions, **low_rows},
            "uniform_marked_formulas": {"assertions": uniform_assertions, **uniform_rows},
            "sharp_witnesses": {"assertions": witness_assertions, **witness_rows},
        },
        "scope": {
            "literal_marked_endpoint_dynamic": "all frozenset pairs n=1..8, t=0..4",
            "containment_eigenbasis": "full Boolean lattices n=1..9",
            "labelled_absorption_recursion": "full Boolean lattices n=2..9",
            "cycle_inventory_and_uniform_marked": "inventory n<=32; endpoints n<=32,t<=5",
            "sharp_cycle_block_witnesses": "every supported size pair n<=100",
            "author_or_review_a_imports": 0,
        },
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
