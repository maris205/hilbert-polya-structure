#!/usr/bin/env python3
"""Exact pilot for odd-fringe mirroring on plane rooted trees.

At every vertex whose fringe subtree has odd order, reverse the child list;
perform these reversals simultaneously.  Fringe orders are invariant, hence
the map is an involution.  The script exhausts all plane rooted trees through
order 12 and independently checks the coupled fixed-point series.
"""

from functools import lru_cache


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(maxsize=None)
def forests(order):
    if order == 0:
        return ((),)
    answer = []
    for first_order in range(1, order + 1):
        for first in trees(first_order):
            for rest in forests(order - first_order):
                answer.append((first,) + rest)
    return tuple(answer)


@lru_cache(maxsize=None)
def trees(order):
    if order < 1:
        return ()
    return forests(order - 1)


@lru_cache(maxsize=None)
def size(tree):
    return 1 + sum(size(child) for child in tree)


@lru_cache(maxsize=None)
def odd_fringe_mirror(tree):
    children = tuple(odd_fringe_mirror(child) for child in tree)
    if size(tree) % 2:
        children = tuple(reversed(children))
    return children


@lru_cache(maxsize=None)
def global_mirror(tree):
    return tuple(reversed(tuple(global_mirror(child) for child in tree)))


def twisted_palindrome_criterion(tree):
    """Root-local criterion equivalent to being fixed by the full map."""
    images = tuple(odd_fringe_mirror(child) for child in tree)
    if size(tree) % 2:
        return tree == tuple(reversed(images))
    return tree == images


def add(left, right, cutoff):
    return [left[i] + right[i] for i in range(cutoff + 1)]


def subtract(left, right, cutoff):
    return [left[i] - right[i] for i in range(cutoff + 1)]


def multiply(left, right, cutoff):
    answer = [0] * (cutoff + 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j in range(cutoff + 1 - i):
            if right[j]:
                answer[i + j] += a * right[j]
    return answer


def inverse(series, cutoff):
    check(series[0] == 1, "series inverse requires constant coefficient one")
    answer = [0] * (cutoff + 1)
    answer[0] = 1
    for n in range(1, cutoff + 1):
        answer[n] = -sum(series[k] * answer[n - k] for k in range(1, n + 1))
    return answer


def shift(series, cutoff):
    return [0] + series[:cutoff]


def series_power(series, exponent, cutoff):
    answer = [0] * (cutoff + 1)
    answer[0] = 1
    for _ in range(exponent):
        answer = multiply(answer, series, cutoff)
    return answer


def algebraic_residual(fixed, cutoff):
    """Evaluate the eliminated polynomial P(x,F(x)) through ``cutoff``."""
    # Each triple is (power of F, power of x, integer coefficient).
    terms = (
        (6, 2, 2), (6, 1, -1),
        (5, 1, -2), (5, 0, 1),
        (4, 3, 4), (4, 2, 6), (4, 1, 4),
        (3, 3, 4), (3, 2, -12), (3, 1, -11), (3, 0, -6),
        (2, 4, 2), (2, 3, -11), (2, 2, 10), (2, 1, 26), (2, 0, 8),
        (1, 4, 4), (1, 3, -2), (1, 2, -20), (1, 1, -19), (1, 0, -3),
        (0, 4, 2), (0, 3, 9), (0, 2, 14), (0, 1, 3),
    )
    powers = {exponent: series_power(fixed, exponent, cutoff) for exponent in range(7)}
    answer = [0] * (cutoff + 1)
    for f_power, x_power, coefficient in terms:
        for degree in range(cutoff + 1 - x_power):
            answer[degree + x_power] += coefficient * powers[f_power][degree]
    return answer


def fixed_series(cutoff):
    """Solve E=x O/((1-E)^2-O^2), O=x(1+E)/(1-A(x^2))."""
    catalan_tree = [0] * (cutoff + 1)
    for n in range(1, cutoff + 1):
        catalan_tree[n] = len(trees(n))
    a_of_x2 = [0] * (cutoff + 1)
    for n in range(1, cutoff // 2 + 1):
        a_of_x2[2 * n] = catalan_tree[n]

    even = [0] * (cutoff + 1)
    odd = [0] * (cutoff + 1)
    one = [0] * (cutoff + 1)
    one[0] = 1
    denominator_odd = subtract(one, a_of_x2, cutoff)
    inverse_odd = inverse(denominator_odd, cutoff)

    for _ in range(cutoff + 2):
        one_minus_even = subtract(one, even, cutoff)
        denominator_even = subtract(
            multiply(one_minus_even, one_minus_even, cutoff),
            multiply(odd, odd, cutoff),
            cutoff,
        )
        new_even = shift(multiply(odd, inverse(denominator_even, cutoff), cutoff), cutoff)
        one_plus_even = add(one, even, cutoff)
        new_odd = shift(multiply(one_plus_even, inverse_odd, cutoff), cutoff)
        new_even = [value if degree % 2 == 0 else 0 for degree, value in enumerate(new_even)]
        new_odd = [value if degree % 2 == 1 else 0 for degree, value in enumerate(new_odd)]
        if new_even == even and new_odd == odd:
            break
        even, odd = new_even, new_odd
    else:
        raise AssertionError("formal fixed-point iteration did not settle")
    return add(even, odd, cutoff)


def main():
    cutoff = 12
    fixed_counts = [0] * (cutoff + 1)
    total_counts = [0] * (cutoff + 1)
    first_not_global = None
    first_global_not_fixed = None

    for order in range(1, cutoff + 1):
        for tree in trees(order):
            image = odd_fringe_mirror(tree)
            total_counts[order] += 1
            check(size(image) == order)
            check(odd_fringe_mirror(image) == tree, "map is not an involution")
            is_fixed = image == tree
            check(is_fixed == twisted_palindrome_criterion(tree))
            fixed_counts[order] += int(is_fixed)
            is_global = global_mirror(tree) == tree
            if is_fixed and not is_global and first_not_global is None:
                first_not_global = (order, tree)
            if is_global and not is_fixed and first_global_not_fixed is None:
                first_global_not_fixed = (order, tree)

        check((total_counts[order] - fixed_counts[order]) % 2 == 0)

    predicted = fixed_series(cutoff)
    for order in range(1, cutoff + 1):
        check(predicted[order] == fixed_counts[order], f"series mismatch at {order}")
    for degree, coefficient in enumerate(algebraic_residual(predicted, cutoff)):
        check(coefficient == 0, f"algebraic residual at degree {degree}")

    check(first_not_global is not None)
    check(first_global_not_fixed is not None)

    print("comb_phase2c_odd_fringe_mirror: PASS")
    print(f"assertions={ASSERTIONS}")
    print("exact_orders=1..12")
    print("total_counts=" + ",".join(map(str, total_counts[1:])))
    print("fixed_counts=" + ",".join(map(str, fixed_counts[1:])))
    print("two_cycle_counts=" + ",".join(
        str((total_counts[n] - fixed_counts[n]) // 2) for n in range(1, cutoff + 1)
    ))
    print(f"first_fixed_not_global_mirror_order={first_not_global[0]}")
    print("first_fixed_not_global_mirror_tree=" + repr(first_not_global[1]))
    print(f"first_global_mirror_not_fixed_order={first_global_not_fixed[0]}")
    print("first_global_mirror_not_fixed_tree=" + repr(first_global_not_fixed[1]))
    print("algebraic_equation=degree6_in_F_verified_through_x^12")
    print("theorem=involution_with_coupled_algebraic_fixed_series_and_exact_cycle_census")


if __name__ == "__main__":
    main()
