#!/usr/bin/env python3
"""Exact controls for random adjacent product-plus-one coalescence.

Starting from n copies of 1, choose an active adjacent boundary uniformly and
replace its incident values x,y by x*y+1.  This standard-library verifier
compares:

* literal deletion histories and their Cartesian evaluation trees;
* the exact uniform-root-split law;
* raw moments and their triangular differential hierarchy;
* internal-node antichain polynomials and the marked Riccati equation; and
* the Euler linearization, minimum atom, and committed coefficient table.

All arithmetic is integer or fractions.Fraction.  Singularity arguments and
Sturm comparison belong to the manuscript and are not replaced by this code.
"""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import comb, factorial
from pathlib import Path


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def poly_add(left, right):
    answer = [Fraction(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        answer[index] += value
    for index, value in enumerate(right):
        answer[index] += value
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return tuple(answer)


def poly_scale(polynomial, scalar):
    return tuple(scalar * value for value in polynomial)


def poly_multiply(left, right):
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            answer[i + j] += left_value * right_value
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return tuple(answer)


def poly_value(polynomial, argument):
    answer = Fraction(0)
    for coefficient in reversed(polynomial):
        answer = answer * argument + coefficient
    return answer


def tree_value_from_boundary_order(order):
    """Evaluate the max-Cartesian tree of one original-boundary order."""

    rank = {boundary: time for time, boundary in enumerate(order)}

    def evaluate(left_leaf, right_leaf):
        if left_leaf == right_leaf:
            return 1
        root = max(range(left_leaf, right_leaf), key=rank.__getitem__)
        return 1 + evaluate(left_leaf, root) * evaluate(root + 1, right_leaf)

    return evaluate(0, len(order))


def literal_value_from_boundary_order(order):
    """Run literal adjacent mergers while deleting named old boundaries."""

    clusters = [(leaf, leaf, 1) for leaf in range(len(order) + 1)]
    for boundary in order:
        position = next(
            index
            for index in range(len(clusters) - 1)
            if clusters[index][1] == boundary
            and clusters[index + 1][0] == boundary + 1
        )
        left = clusters[position]
        right = clusters[position + 1]
        merged = (left[0], right[1], 1 + left[2] * right[2])
        clusters[position : position + 2] = [merged]
    check(len(clusters) == 1, (order, clusters))
    return clusters[0][2]


def antichain_poly_from_boundary_order(order):
    """Return the internal-node antichain polynomial of the tree."""

    rank = {boundary: time for time, boundary in enumerate(order)}

    def recurse(left_leaf, right_leaf):
        if left_leaf == right_leaf:
            return (Fraction(1),)
        root = max(range(left_leaf, right_leaf), key=rank.__getitem__)
        below = poly_multiply(
            recurse(left_leaf, root), recurse(root + 1, right_leaf)
        )
        return poly_add(below, (Fraction(0), Fraction(1)))

    return recurse(0, len(order))


def law_from_orders(size):
    if size == 1:
        return {1: Fraction(1)}
    counts = Counter()
    for order in permutations(range(size - 1)):
        tree_value = tree_value_from_boundary_order(order)
        literal_value = literal_value_from_boundary_order(order)
        check(tree_value == literal_value, (order, tree_value, literal_value))
        polynomial = antichain_poly_from_boundary_order(order)
        check(poly_value(polynomial, 1) == tree_value, (order, polynomial))
        counts[tree_value] += 1
    denominator = factorial(size - 1)
    return dict(
        sorted(
            (value, Fraction(count, denominator))
            for value, count in counts.items()
        )
    )


@lru_cache(maxsize=None)
def split_law(size):
    if size == 1:
        return {1: Fraction(1)}
    answer = Counter()
    root_weight = Fraction(1, size - 1)
    for left_size in range(1, size):
        for left_value, left_mass in split_law(left_size).items():
            for right_value, right_mass in split_law(size - left_size).items():
                answer[1 + left_value * right_value] += (
                    root_weight * left_mass * right_mass
                )
    return dict(sorted(answer.items()))


@lru_cache(maxsize=None)
def marked_expectation(size):
    if size == 1:
        return (Fraction(1),)
    total = (Fraction(0),)
    for left_size in range(1, size):
        total = poly_add(
            total,
            poly_multiply(
                marked_expectation(left_size),
                marked_expectation(size - left_size),
            ),
        )
    return poly_add(
        (Fraction(0), Fraction(1)),
        poly_scale(total, Fraction(1, size - 1)),
    )


def marked_expectation_from_orders(size):
    if size == 1:
        return (Fraction(1),)
    total = (Fraction(0),)
    for order in permutations(range(size - 1)):
        total = poly_add(total, antichain_poly_from_boundary_order(order))
    return poly_scale(total, Fraction(1, factorial(size - 1)))


def moment_table(max_order, max_size):
    moment = [
        [Fraction(0) for _ in range(max_size + 1)]
        for _ in range(max_order + 1)
    ]
    for order in range(max_order + 1):
        moment[order][1] = Fraction(1)
    for size in range(2, max_size + 1):
        for order in range(max_order + 1):
            total = Fraction(0)
            for left_size in range(1, size):
                total += sum(
                    comb(order, exponent)
                    * moment[exponent][left_size]
                    * moment[exponent][size - left_size]
                    for exponent in range(order + 1)
                )
            moment[order][size] = total / (size - 1)
    return moment


def truncated_square(coefficients, degree):
    return sum(
        coefficients[index] * coefficients[degree - index]
        for index in range(degree + 1)
    )


def verify_moment_ode(moment, max_order, max_size):
    """Check F_r'=sum_{k<=r} binom(r,k)F_k^2 coefficientwise."""

    for order in range(max_order + 1):
        for degree in range(max_size - 1):
            left = (degree + 1) * moment[order][degree + 2]
            right = sum(
                comb(order, exponent)
                * truncated_square(
                    [moment[exponent][size] for size in range(1, max_size + 1)],
                    degree,
                )
                for exponent in range(order + 1)
            )
            check(left == right, (order, degree, left, right))


def euler_solution_series(max_degree):
    """Solve U''+(1-z)^(-2)U=0, U(0)=1,U'(0)=-1 formally."""

    coefficient = [Fraction(0) for _ in range(max_degree + 2)]
    coefficient[0] = Fraction(1)
    coefficient[1] = Fraction(-1)
    for degree in range(max_degree):
        forcing = sum(
            (index + 1) * coefficient[degree - index]
            for index in range(degree + 1)
        )
        coefficient[degree + 2] = -forcing / (
            (degree + 2) * (degree + 1)
        )
    return coefficient


def negative_log_derivative(numerator, max_degree):
    answer = [Fraction(0) for _ in range(max_degree + 1)]
    for degree in range(max_degree + 1):
        target = -(degree + 1) * numerator[degree + 1]
        known = sum(
            answer[index] * numerator[degree - index]
            for index in range(degree)
        )
        answer[degree] = target - known
    return answer


def marked_linear_ode_series(max_degree):
    """Solve Y''+s(1-z)^(-2)Y=0 over Q[s][[z]]."""

    coefficient = [(Fraction(0),) for _ in range(max_degree + 2)]
    coefficient[0] = (Fraction(1),)
    coefficient[1] = (Fraction(-1),)
    marker = (Fraction(0), Fraction(1))
    for degree in range(max_degree):
        forcing = (Fraction(0),)
        for index in range(degree + 1):
            forcing = poly_add(
                forcing,
                poly_scale(coefficient[degree - index], index + 1),
            )
        coefficient[degree + 2] = poly_scale(
            poly_multiply(marker, forcing),
            Fraction(-1, (degree + 2) * (degree + 1)),
        )
    return coefficient


def marked_negative_log_derivative(numerator, max_degree):
    answer = [(Fraction(0),) for _ in range(max_degree + 1)]
    for degree in range(max_degree + 1):
        target = poly_scale(numerator[degree + 1], -(degree + 1))
        known = (Fraction(0),)
        for index in range(degree):
            known = poly_add(
                known,
                poly_multiply(answer[index], numerator[degree - index]),
            )
        answer[degree] = poly_add(target, poly_scale(known, -1))
    return answer


def parse_fraction(token):
    return Fraction(token)


def verify_committed_table(moment):
    table_path = Path(__file__).with_name("marked_antichain_coefficients.tsv")
    rows = table_path.read_text(encoding="utf-8").splitlines()
    check(
        rows[0]
        == "n\tantichain_coefficients_s0_up\tE_X\tE_X2\tmin_output\tmin_probability\tsupport_size",
        rows[0],
    )
    check(len(rows) == 13, len(rows))
    for expected_size, row in enumerate(rows[1:], start=1):
        fields = row.split("\t")
        check(len(fields) == 7, (expected_size, fields))
        size = int(fields[0])
        coefficients = tuple(parse_fraction(x) for x in fields[1].split(";"))
        check(size == expected_size, (size, expected_size))
        check(coefficients == marked_expectation(size), (size, coefficients))
        check(parse_fraction(fields[2]) == moment[1][size], size)
        check(parse_fraction(fields[3]) == moment[2][size], size)
        check(int(fields[4]) == size, fields[4])
        minimum_mass = (
            Fraction(1)
            if size == 1
            else Fraction(2 ** (size - 2), factorial(size - 1))
        )
        check(parse_fraction(fields[5]) == minimum_mass, size)
        check(int(fields[6]) == len(split_law(size)), size)


def run():
    # Exhaustive histories give literal/tree/antichain agreement and agree
    # with the independent split-law dynamic program through n=9.
    for size in range(1, 10):
        order_law = law_from_orders(size)
        recursive_law = split_law(size)
        check(order_law == recursive_law, (size, order_law, recursive_law))
        check(sum(recursive_law.values(), Fraction(0)) == 1, size)
        check(
            marked_expectation_from_orders(size) == marked_expectation(size),
            size,
        )

    max_order = 6
    max_size = 60
    moment = moment_table(max_order, max_size)
    verify_moment_ode(moment, max_order, max_size)

    # Full laws recover moments and the exact minimum atom through n=12.
    for size in range(1, 13):
        law = split_law(size)
        for order in range(max_order + 1):
            literal = sum(
                Fraction(value**order) * mass for value, mass in law.items()
            )
            check(literal == moment[order][size], (size, order, literal))
        check(min(law) == size, (size, min(law)))
        expected = (
            Fraction(1)
            if size == 1
            else Fraction(2 ** (size - 2), factorial(size - 1))
        )
        check(law[size] == expected, (size, law[size], expected))

    # The marked split recurrence and its bivariate linearization agree
    # coefficientwise through n=60 and specialize to the mean.
    marked_y = marked_linear_ode_series(max_size)
    marked_riccati = marked_negative_log_derivative(marked_y, max_size - 1)
    for size in range(1, max_size + 1):
        expected = marked_expectation(size)
        check(marked_riccati[size - 1] == expected, (size, expected))
        check(poly_value(expected, 1) == moment[1][size], size)
        singleton = expected[1] if len(expected) > 1 else Fraction(0)
        check(singleton == (0 if size == 1 else size - 1), (size, singleton))

    # Independent formal Euler equation -> Riccati mean coefficients.
    mean_u = euler_solution_series(max_size)
    mean_coefficients = negative_log_derivative(mean_u, max_size - 1)
    for size in range(1, max_size + 1):
        check(mean_coefficients[size - 1] == moment[1][size], size)

    verify_committed_table(moment)

    check(
        split_law(4) == {4: Fraction(2, 3), 5: Fraction(1, 3)},
        "order-four sentinel",
    )
    check(moment[1][10] == Fraction(9491, 270), "mean sentinel")
    check(
        moment[2][4] - moment[1][4] ** 2 == Fraction(2, 9),
        "variance sentinel",
    )
    check(len(split_law(12)) == 97, "support-size sentinel")

    print("product_plus_one verifier: PASS")
    print(f"exact assertions: {ASSERTIONS:,}")
    print("history enumeration: every boundary order through n <= 9")
    print("finite laws/moments/minimum atom: n <= 12, raw moments r <= 6")
    print("moment hierarchy: coefficientwise r <= 6, n <= 60")
    print("marked antichains: coefficientwise n <= 60, histories n <= 9")
    print("mean Euler linearization: coefficientwise n <= 60")
    print("coefficient artifact: byte-parsed and exactly matched through n <= 12")
    print("arithmetic: integers and fractions.Fraction only")
    print("scope sentinel: r>=3 pole/radius and all ownership claims are noncomputational")


if __name__ == "__main__":
    run()
