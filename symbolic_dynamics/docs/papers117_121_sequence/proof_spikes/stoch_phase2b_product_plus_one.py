#!/usr/bin/env python3
"""Exact Phase-2b pilot: adjacent coalescence under x star y = x*y+1."""

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


@lru_cache(maxsize=None)
def output_law(state):
    if len(state) == 1:
        return {state[0]: Fraction(1)}
    weight = Fraction(1, len(state) - 1)
    answer = {}
    for index in range(len(state) - 1):
        merged = state[index] * state[index + 1] + 1
        nxt = state[:index] + (merged,) + state[index + 2 :]
        for value, mass in output_law(nxt).items():
            answer[value] = answer.get(value, Fraction(0)) + weight * mass
    return dict(sorted(answer.items()))


def exact_moments(max_order, bound):
    """m[order][size] for the complete polynomial moment hierarchy."""
    moments = [[Fraction(0)] * (bound + 1) for _ in range(max_order + 1)]
    for size in range(1, bound + 1):
        moments[0][size] = Fraction(1)
    for order in range(1, max_order + 1):
        moments[order][1] = Fraction(1)

    for size in range(2, bound + 1):
        for order in range(1, max_order + 1):
            total = Fraction(0)
            for split in range(1, size):
                total += sum(
                    comb(order, power)
                    * moments[power][split]
                    * moments[power][size - split]
                    for power in range(order + 1)
                )
            moments[order][size] = total / (size - 1)
    return moments


def cartesian_value(boundary_order, leaf_count):
    """Evaluate the Cartesian tree of a fixed original-boundary deletion order."""
    priority = {boundary: rank for rank, boundary in enumerate(boundary_order)}

    def evaluate(left_leaf, right_leaf):
        if left_leaf == right_leaf:
            return 1
        root_boundary = max(range(left_leaf, right_leaf), key=priority.__getitem__)
        return (
            evaluate(left_leaf, root_boundary)
            * evaluate(root_boundary + 1, right_leaf)
            + 1
        )

    return evaluate(0, leaf_count - 1)


def permutation_law(leaf_count):
    if leaf_count == 1:
        return {1: Fraction(1)}
    counts = {}
    for order in permutations(range(leaf_count - 1)):
        value = cartesian_value(order, leaf_count)
        counts[value] = counts.get(value, 0) + 1
    denominator = factorial(leaf_count - 1)
    return {value: Fraction(count, denominator) for value, count in sorted(counts.items())}


def poly_add(left, right):
    degree = max(len(left), len(right))
    answer = [Fraction(0)] * degree
    for index, value in enumerate(left):
        answer[index] += value
    for index, value in enumerate(right):
        answer[index] += value
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return tuple(answer)


def poly_mul(left, right):
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x_value in enumerate(left):
        for j, y_value in enumerate(right):
            answer[i + j] += x_value * y_value
    return tuple(answer)


def poly_scale(poly, scalar):
    return tuple(scalar * value for value in poly)


def poly_eval_one(poly):
    return sum(poly, Fraction(0))


def cartesian_antichain_poly(boundary_order, leaf_count):
    """Antichain-size polynomial of the internal-node Cartesian-tree poset."""
    priority = {boundary: rank for rank, boundary in enumerate(boundary_order)}

    def evaluate(left_leaf, right_leaf):
        if left_leaf == right_leaf:
            return (Fraction(1),)
        root_boundary = max(range(left_leaf, right_leaf), key=priority.__getitem__)
        below = poly_mul(
            evaluate(left_leaf, root_boundary),
            evaluate(root_boundary + 1, right_leaf),
        )
        return poly_add(below, (Fraction(0), Fraction(1)))

    return evaluate(0, leaf_count - 1)


def marked_antichain_expectations(bound):
    """a_n(u)=E sum_{antichains A}u^|A| under the random-BST split law."""
    answer = [()] * (bound + 1)
    answer[1] = (Fraction(1),)
    root_term = (Fraction(0), Fraction(1))
    for size in range(2, bound + 1):
        total = (Fraction(0),)
        for split in range(1, size):
            total = poly_add(total, poly_mul(answer[split], answer[size - split]))
        answer[size] = poly_add(root_term, poly_scale(total, Fraction(1, size - 1)))
    return answer


def linear_ode_series(bound):
    """Coefficients of u''+u/(1-z)^2=0, u(0)=1,u'(0)=-1."""
    coefficients = [Fraction(0)] * (bound + 2)
    coefficients[0] = Fraction(1)
    coefficients[1] = Fraction(-1)
    for degree in range(bound):
        convolution = sum(
            Fraction(index + 1) * coefficients[degree - index]
            for index in range(degree + 1)
        )
        coefficients[degree + 2] = -convolution / ((degree + 2) * (degree + 1))
    return coefficients


def quotient_minus_derivative(numerator, bound):
    """Return coefficients of -u'/u through the requested degree."""
    answer = [Fraction(0)] * (bound + 1)
    for degree in range(bound + 1):
        target = -(degree + 1) * numerator[degree + 1]
        known = sum(answer[index] * numerator[degree - index] for index in range(degree))
        answer[degree] = target - known  # numerator[0]=1
    return answer


def run():
    moments = exact_moments(6, 60)
    marked = marked_antichain_expectations(60)
    mean = moments[1]
    second = moments[2]

    # Literal adjacent-pair dynamics agrees with the uniform-root-split
    # recurrence and its second-moment refinement.
    for size in range(1, 13):
        law = output_law((1,) * size)
        check(sum(law.values(), Fraction(0)) == 1, (size, law))
        for order in range(7):
            literal_moment = sum(value**order * mass for value, mass in law.items())
            check(
                literal_moment == moments[order][size],
                (size, order, literal_moment, moments[order][size]),
            )

        check(min(law) == size, (size, min(law)))
        minimum_mass = Fraction(1) if size == 1 else Fraction(2 ** (size - 2), factorial(size - 1))
        check(law[size] == minimum_mass, (size, law[size], minimum_mass))

    # A current adjacent boundary is exactly an original boundary that has not
    # yet been removed.  Thus its successive uniform choices form a uniform
    # permutation, whose max-Cartesian tree has the random-BST split law.
    for size in range(1, 10):
        check(permutation_law(size) == output_law((1,) * size), size)

        if size == 1:
            enumerated_marked = (Fraction(1),)
        else:
            total = (Fraction(0),)
            for order in permutations(range(size - 1)):
                total = poly_add(total, cartesian_antichain_poly(order, size))
            enumerated_marked = poly_scale(total, Fraction(1, factorial(size - 1)))
        check(enumerated_marked == marked[size], (size, enumerated_marked, marked[size]))

    # Coefficient form of M_r' = sum_{k=0}^r binom(r,k) M_k^2,
    # including M_0=(1-z)^(-1).
    for order in range(7):
        for size in range(2, 61):
            rhs = sum(
                comb(order, power)
                * sum(
                    moments[power][left] * moments[power][size - left]
                    for left in range(1, size)
                )
                for power in range(order + 1)
            )
            check((size - 1) * moments[order][size] == rhs, (order, size))

    # Coefficient form of A_z=A^2+u/(1-z)^2 for the expected marked-antichain
    # polynomial.  Evaluation at u=1 recovers the product-plus-one mean.
    root_term = (Fraction(0), Fraction(1))
    for size in range(1, 61):
        check(poly_eval_one(marked[size]) == mean[size], (size, marked[size], mean[size]))
        expected_singletons = Fraction(0) if size == 1 else Fraction(size - 1)
        singleton_coefficient = marked[size][1] if len(marked[size]) > 1 else Fraction(0)
        check(singleton_coefficient == expected_singletons, (size, singleton_coefficient))
        if size >= 2:
            convolution = (Fraction(0),)
            for split in range(1, size):
                convolution = poly_add(
                    convolution,
                    poly_mul(marked[split], marked[size - split]),
                )
            rhs_poly = poly_add(convolution, poly_scale(root_term, size - 1))
            lhs_poly = poly_scale(marked[size], size - 1)
            degree = max(len(lhs_poly), len(rhs_poly))
            for coefficient in range(degree):
                lhs_value = lhs_poly[coefficient] if coefficient < len(lhs_poly) else 0
                rhs_value = rhs_poly[coefficient] if coefficient < len(rhs_poly) else 0
                check(lhs_value == rhs_value, (size, coefficient, lhs_value, rhs_value))

    # The Riccati equation M'=M^2+(1-z)^(-2) linearizes to the displayed
    # Euler equation.  Verify its formal coefficients independently.
    ode_u = linear_ode_series(60)
    riccati_coefficients = quotient_minus_derivative(ode_u, 59)
    for size in range(1, 61):
        check(riccati_coefficients[size - 1] == mean[size], (size, riccati_coefficients[size - 1]))

    check(
        output_law((1, 1, 1, 1)) == {4: Fraction(2, 3), 5: Fraction(1, 3)},
        output_law((1, 1, 1, 1)),
    )
    check(mean[10] == Fraction(9491, 270), mean[10])
    check(second[4] - mean[4] ** 2 == Fraction(2, 9), "variance sentinel")
    check(len(output_law((1,) * 12)) == 97, "support-size sentinel")

    print("stoch_phase2b_product_plus_one: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"states={output_law.cache_info().currsize}")
    print("bst_equivalence=uniform original-boundary order checked_n<=9")
    print("moment_hierarchy=M_r'=sum_{k=0}^r binom(r,k) M_k^2 checked_r<=6,n<=60")
    print("marked_antichains=A_z=A^2+u/(1-z)^2 checked_n<=60,permutations_n<=9")
    print("mean_ode=M'=M^2+(1-z)^(-2), M(0)=1")
    print("linearization=u''+u/(1-z)^2=0, M=-u'/u")
    print("dominant_candidate=rho=1-exp(-2*pi/(3*sqrt(3)))")
    print("minimum_atom=P(X_n=n)=2^(n-2)/(n-1)! checked_n<=12")
    print("killed_guess=deterministic_output_for_n>=4")


if __name__ == "__main__":
    run()
