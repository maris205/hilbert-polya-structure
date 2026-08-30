#!/usr/bin/env python3
"""Independent exact control for adjacent ``x*y+1`` coalescence.

Starting from n copies of 1, choose one of the currently active adjacent
boundaries uniformly and replace the two incident blocks by ``x*y+1``.
The script compares three descriptions:

* literal uniform deletion orders of the original boundaries;
* the uniform-root-split recursion of the induced planar binary tree; and
* the differential hierarchy for every raw moment.

It also marks antichains by cardinality.  If ``P_T(u)`` is the antichain
polynomial of the internal-node poset of the evaluation tree, then the
terminal value is ``P_T(1)``.  We independently compare boundary orders,
the marked split recursion, and the bivariate Riccati linearization.

All probabilities and moments are rational.  The closed trigonometric
solution and singularity argument are mathematical proofs in the companion
report; here we verify their formal-power-series linearization exactly.
"""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import comb, factorial


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def value_from_boundary_order(order):
    """Evaluate the tree encoded by a boundary-deletion permutation."""

    rank = {boundary: time for time, boundary in enumerate(order)}

    def evaluate(left_leaf, right_leaf):
        if left_leaf == right_leaf:
            return 1
        root_boundary = max(
            range(left_leaf, right_leaf), key=lambda boundary: rank[boundary]
        )
        return 1 + evaluate(left_leaf, root_boundary) * evaluate(
            root_boundary + 1, right_leaf
        )

    return evaluate(0, len(order))


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


def antichain_poly_from_boundary_order(order):
    """Return P_T(u)=sum_A u^|A| for the Cartesian evaluation tree."""

    rank = {boundary: time for time, boundary in enumerate(order)}

    def recurse(left_leaf, right_leaf):
        if left_leaf == right_leaf:
            return (Fraction(1),)
        root_boundary = max(
            range(left_leaf, right_leaf), key=lambda boundary: rank[boundary]
        )
        product = poly_multiply(
            recurse(left_leaf, root_boundary),
            recurse(root_boundary + 1, right_leaf),
        )
        return poly_add(product, (Fraction(0), Fraction(1)))

    return recurse(0, len(order))


@lru_cache(maxsize=None)
def marked_expectation(size):
    """Expected internal-node antichain polynomial under uniform splitting."""

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
    total = poly_scale(total, Fraction(1, size - 1))
    return poly_add(total, (Fraction(0), Fraction(1)))


def marked_expectation_from_orders(size):
    if size == 1:
        return (Fraction(1),)
    total = (Fraction(0),)
    for order in permutations(range(size - 1)):
        polynomial = antichain_poly_from_boundary_order(order)
        check(poly_value(polynomial, 1) == value_from_boundary_order(order), order)
        total = poly_add(total, polynomial)
    return poly_scale(total, Fraction(1, factorial(size - 1)))


def literal_value_from_boundary_order(order):
    """Run the adjacent tuple process while deleting the named old gaps."""

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


def law_from_orders(size):
    if size == 1:
        return {1: Fraction(1)}
    counts = Counter()
    for order in permutations(range(size - 1)):
        tree_value = value_from_boundary_order(order)
        literal_value = literal_value_from_boundary_order(order)
        check(tree_value == literal_value, (order, tree_value, literal_value))
        counts[tree_value] += 1
    denominator = factorial(size - 1)
    return dict(sorted((value, Fraction(count, denominator)) for value, count in counts.items()))


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
    """Check F_r'=sum_{k<=r} binom(r,k) F_k^2 coefficientwise."""

    # F_r[z^d] = m_r(d+1).
    for order in range(max_order + 1):
        coefficients = [moment[order][size] for size in range(1, max_size + 1)]
        for degree in range(max_size - 1):
            left = (degree + 1) * coefficients[degree + 1]
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
    """Solve u''+(1-z)^(-2)u=0, u(0)=1, u'(0)=-1 formally."""

    coefficient = [Fraction(0) for _ in range(max_degree + 2)]
    coefficient[0] = Fraction(1)
    coefficient[1] = Fraction(-1)
    for degree in range(max_degree):
        forcing = sum(
            (index + 1) * coefficient[degree - index]
            for index in range(degree + 1)
        )
        coefficient[degree + 2] = -forcing / ((degree + 2) * (degree + 1))
    return coefficient


def negative_log_derivative(numerator, max_degree):
    """Return the first coefficients of -u'/u when u(0)=1."""

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
    """Solve y''+u(1-z)^(-2)y=0 over Q[u][[z]]."""

    coefficient = [(Fraction(0),) for _ in range(max_degree + 2)]
    coefficient[0] = (Fraction(1),)
    coefficient[1] = (Fraction(-1),)
    u_polynomial = (Fraction(0), Fraction(1))
    for degree in range(max_degree):
        forcing = (Fraction(0),)
        for index in range(degree + 1):
            forcing = poly_add(
                forcing,
                poly_scale(coefficient[degree - index], index + 1),
            )
        forcing = poly_multiply(u_polynomial, forcing)
        coefficient[degree + 2] = poly_scale(
            forcing, Fraction(-1, (degree + 2) * (degree + 1))
        )
    return coefficient


def marked_negative_log_derivative(numerator, max_degree):
    """Return -y_z/y in Q[u][[z]] when y(0)=1."""

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


def run():
    # Deletion histories and recursive split laws are independent exact routes.
    for size in range(1, 10):
        order_law = law_from_orders(size)
        recursive_law = split_law(size)
        check(order_law == recursive_law, (size, order_law, recursive_law))
        check(sum(recursive_law.values(), Fraction(0)) == 1, size)
        check(
            marked_expectation_from_orders(size) == marked_expectation(size),
            (size, marked_expectation_from_orders(size), marked_expectation(size)),
        )

    # Literal laws validate the full raw-moment hierarchy.
    max_order = 4
    max_size = 36
    moment = moment_table(max_order, max_size)
    verify_moment_ode(moment, max_order, max_size)
    for size in range(1, 13):
        law = split_law(size)
        for order in range(max_order + 1):
            literal = sum(
                Fraction(value**order) * mass for value, mass in law.items()
            )
            check(literal == moment[order][size], (size, order, literal))

    # The minimum output and its exact atom are checked separately.
    for size in range(1, 13):
        law = split_law(size)
        check(min(law) == size, (size, min(law)))
        expected = (
            Fraction(1)
            if size == 1
            else Fraction(2 ** (size - 2), factorial(size - 1))
        )
        check(law[size] == expected, (size, law[size], expected))

    # Independent formal Euler equation -> Riccati coefficient comparison.
    u = euler_solution_series(max_size)
    mean_coefficients = negative_log_derivative(u, max_size - 1)
    for size in range(1, max_size + 1):
        check(mean_coefficients[size - 1] == moment[1][size], size)

    # Marking antichains by cardinality gives
    # A_z=A^2+u/(1-z)^2.  Its Q[u][[z]] linearization agrees with the
    # independently averaged Cartesian-tree antichain polynomials.
    marked_u = marked_linear_ode_series(max_size)
    marked_riccati = marked_negative_log_derivative(marked_u, max_size - 1)
    for size in range(1, max_size + 1):
        expected = marked_expectation(size)
        check(marked_riccati[size - 1] == expected, (size, marked_riccati[size - 1], expected))
        check(poly_value(expected, 1) == moment[1][size], (size, expected))

    check(
        split_law(4) == {4: Fraction(2, 3), 5: Fraction(1, 3)},
        "order-four sentinel",
    )
    check(moment[1][10] == Fraction(9491, 270), "mean sentinel")

    print("root_product_plus_one_verify: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"cached_split_sizes={split_law.cache_info().currsize}")
    print("history_model=uniform_permutation_of_original_boundaries")
    print("moment_hierarchy=F_r'=sum_{k=0}^r binom(r,k) F_k^2")
    print("minimum_atom=2^(n-2)/(n-1)! for n>=2")
    print("mean_linearization=u''+(1-z)^(-2)u=0")
    print("marked_antichains=A_z=A^2+u/(1-z)^2 checked_n<=36")


if __name__ == "__main__":
    run()
