#!/usr/bin/env python3
"""Exact controls for odd-fringe mirror dynamics on plane rooted trees.

A nonempty plane rooted tree is a tuple of its root's children; ``()`` is a
leaf.  At every vertex whose old fringe subtree has odd order, reverse its
child tuple, simultaneously.  The verifier is deterministic and uses only
the Python standard library.
"""

from csv import DictReader
from functools import lru_cache
from math import comb
from pathlib import Path


ASSERTIONS = 0
STATES_ENUMERATED = 0
EMPTY = None


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(maxsize=None)
def forests(order):
    """All ordered forests having ``order`` vertices in total."""
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
def update(tree):
    children = tuple(update(child) for child in tree)
    return tuple(reversed(children)) if size(tree) % 2 else children


def update_state(state):
    return EMPTY if state is EMPTY else update(state)


@lru_cache(maxsize=None)
def trigger_snapshot(tree):
    """Store every trigger before making any child-order change."""
    return (size(tree) % 2, tuple(trigger_snapshot(child) for child in tree))


@lru_cache(maxsize=None)
def apply_snapshot(snapshot):
    odd, child_snapshots = snapshot
    children = tuple(apply_snapshot(child) for child in child_snapshots)
    return tuple(reversed(children)) if odd else children


@lru_cache(maxsize=None)
def global_mirror(tree):
    return tuple(reversed(tuple(global_mirror(child) for child in tree)))


@lru_cache(maxsize=None)
def unordered_key(tree):
    return tuple(sorted(unordered_key(child) for child in tree))


@lru_cache(maxsize=None)
def fringe_orders(tree):
    answer = [size(tree)]
    for child in tree:
        answer.extend(fringe_orders(child))
    return tuple(sorted(answer))


@lru_cache(maxsize=None)
def pointwise_fringe_preserved(source, target):
    """Check the recursively induced source-to-image vertex transport."""
    if size(source) != size(target) or len(source) != len(target):
        return False
    width = len(source)
    for index, child in enumerate(source):
        target_index = width - 1 - index if size(source) % 2 else index
        image_child = target[target_index]
        if size(child) != size(image_child):
            return False
        if not pointwise_fringe_preserved(child, image_child):
            return False
    return True


@lru_cache(maxsize=None)
def fixed_criterion(tree):
    images = tuple(update(child) for child in tree)
    if size(tree) % 2:
        return tree == tuple(reversed(images))
    return tree == images


def iterate(tree, time):
    for _ in range(time):
        tree = update(tree)
    return tree


def catalan(index):
    return comb(2 * index, index) // (index + 1)


def parity_coefficients(maximum):
    """Return e(z)=E(sqrt(z)) and o(z)=O(sqrt(z))/sqrt(z).

    With C(z)=1/(1-A(z)), the coupled system becomes
      o=(1+e)C,
      e*((1-e)^2-z*o^2)=z*o.
    Coefficient n of the second equation determines e[n], then the first
    determines o[n].
    """
    catalans = [catalan(index) for index in range(maximum + 1)]
    even = [0] * (maximum + 1)
    odd = [0] * (maximum + 1)
    odd[0] = 1

    for degree in range(1, maximum + 1):
        denominator = []
        for index in range(degree):
            even_square = sum(
                even[left] * even[index - left] for left in range(index + 1)
            )
            shifted_odd_square = (
                sum(odd[left] * odd[index - 1 - left] for left in range(index))
                if index
                else 0
            )
            denominator.append(
                int(index == 0) - 2 * even[index] + even_square - shifted_odd_square
            )
        check(denominator[0] == 1, "parity recurrence lost its unit denominator")
        even[degree] = odd[degree - 1] - sum(
            even[index] * denominator[degree - index]
            for index in range(1, degree)
        )
        odd[degree] = catalans[degree] + sum(
            even[index] * catalans[degree - index]
            for index in range(1, degree + 1)
        )
    return even, odd


def multiply(left, right, cutoff):
    answer = [0] * (cutoff + 1)
    for i, left_value in enumerate(left[: cutoff + 1]):
        if not left_value:
            continue
        for j, right_value in enumerate(right[: cutoff + 1 - i]):
            if right_value:
                answer[i + j] += left_value * right_value
    return answer


def add(left, right, cutoff):
    return [left[index] + right[index] for index in range(cutoff + 1)]


def subtract(left, right, cutoff):
    return [left[index] - right[index] for index in range(cutoff + 1)]


def shift(series, amount, cutoff):
    return [0] * amount + series[: cutoff + 1 - amount]


def series_power(series, exponent, cutoff):
    answer = [0] * (cutoff + 1)
    answer[0] = 1
    for _ in range(exponent):
        answer = multiply(answer, series, cutoff)
    return answer


def polynomial_residual(fixed, cutoff):
    """Evaluate the displayed degree-six P(x,F(x))."""
    terms = (
        (6, 2, 2), (6, 1, -1),
        (5, 1, -2), (5, 0, 1),
        (4, 3, 4), (4, 2, 6), (4, 1, 4),
        (3, 3, 4), (3, 2, -12), (3, 1, -11), (3, 0, -6),
        (2, 4, 2), (2, 3, -11), (2, 2, 10), (2, 1, 26), (2, 0, 8),
        (1, 4, 4), (1, 3, -2), (1, 2, -20), (1, 1, -19), (1, 0, -3),
        (0, 4, 2), (0, 3, 9), (0, 2, 14), (0, 1, 3),
    )
    powers = {
        exponent: series_power(fixed, exponent, cutoff) for exponent in range(7)
    }
    answer = [0] * (cutoff + 1)
    for f_power, x_power, coefficient in terms:
        for degree in range(cutoff + 1 - x_power):
            answer[degree + x_power] += coefficient * powers[f_power][degree]
    return answer


def parity_elimination_residual(even, cutoff):
    """Evaluate Q(z,e) obtained by separating even and odd orders."""
    terms = (
        (6, 1, 4), (6, 0, -1),
        (4, 1, 8), (4, 0, 2),
        (3, 1, 4),
        (2, 2, 1), (2, 1, 8), (2, 0, -1),
        (1, 2, 2),
        (0, 2, 1),
    )
    powers = {
        exponent: series_power(even, exponent, cutoff) for exponent in range(7)
    }
    answer = [0] * (cutoff + 1)
    for e_power, z_power, coefficient in terms:
        for degree in range(cutoff + 1 - z_power):
            answer[degree + z_power] += coefficient * powers[e_power][degree]
    return answer


# Sparse multivariate integer polynomials for the exact resultant audit.
# Exponent tuples are ordered as (B,G,x,F).
def mp_clean(poly):
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def mp_add(left, right):
    answer = dict(left)
    for monomial, coefficient in right.items():
        answer[monomial] = answer.get(monomial, 0) + coefficient
    return mp_clean(answer)


def mp_scale(poly, scalar):
    return mp_clean({monomial: scalar * coefficient for monomial, coefficient in poly.items()})


def mp_subtract(left, right):
    return mp_add(left, mp_scale(right, -1))


def mp_multiply(left, right):
    answer = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(a + b for a, b in zip(left_monomial, right_monomial))
            answer[monomial] = answer.get(monomial, 0) + left_coefficient * right_coefficient
    return mp_clean(answer)


def mp_variable(index):
    exponent = [0, 0, 0, 0]
    exponent[index] = 1
    return {tuple(exponent): 1}


def mp_g_coefficient(poly, degree):
    answer = {}
    for (b_power, g_power, x_power, f_power), coefficient in poly.items():
        if g_power == degree:
            answer[(b_power, 0, x_power, f_power)] = coefficient
    return answer


def reduce_b_quadratic(poly):
    """Reduce modulo B^2-B+x^2, returning U,V with poly=U*B+V."""
    # U and V use exponent pairs (x,F).
    answer_u = {}
    answer_v = {}
    b_reductions = {
        0: ({}, {(0, 0): 1}),
        1: ({(0, 0): 1}, {}),
    }
    maximum_b = max((monomial[0] for monomial in poly), default=0)
    for degree in range(2, maximum_b + 1):
        previous_u, previous_v = b_reductions[degree - 1]
        current_u = dict(previous_u)
        for key, value in previous_v.items():
            current_u[key] = current_u.get(key, 0) + value
        current_v = {(x_power + 2, f_power): -value
                     for (x_power, f_power), value in previous_u.items()}
        b_reductions[degree] = (
            {key: value for key, value in current_u.items() if value},
            {key: value for key, value in current_v.items() if value},
        )

    for (b_power, g_power, x_power, f_power), coefficient in poly.items():
        check(g_power == 0, "G survived first resultant")
        for destination, reduced in ((answer_u, b_reductions[b_power][0]),
                                     (answer_v, b_reductions[b_power][1])):
            for (extra_x, extra_f), value in reduced.items():
                key = (x_power + extra_x, f_power + extra_f)
                destination[key] = destination.get(key, 0) + coefficient * value
    return (
        {key: value for key, value in answer_u.items() if value},
        {key: value for key, value in answer_v.items() if value},
    )


def xf_add(left, right):
    answer = dict(left)
    for key, value in right.items():
        answer[key] = answer.get(key, 0) + value
    return {key: value for key, value in answer.items() if value}


def xf_multiply(left, right):
    answer = {}
    for (lx, lf), lc in left.items():
        for (rx, rf), rc in right.items():
            key = (lx + rx, lf + rf)
            answer[key] = answer.get(key, 0) + lc * rc
    return {key: value for key, value in answer.items() if value}


def exact_resultant_audit():
    """Reconstruct Res_B(Res_G(H1,H2),H3)=4*x^2*P exactly."""
    one = {(0, 0, 0, 0): 1}
    b_var = mp_variable(0)
    g_var = mp_variable(1)
    x_var = mp_variable(2)
    f_var = mp_variable(3)
    h1 = mp_subtract(
        mp_multiply(mp_multiply(mp_add(f_var, g_var), mp_subtract(one, f_var)),
                    mp_subtract(one, g_var)),
        mp_multiply(x_var, mp_subtract(f_var, g_var)),
    )
    h2 = mp_add(
        mp_multiply(mp_add(mp_subtract(one, b_var), x_var), g_var),
        mp_add(
            mp_scale(mp_multiply(mp_subtract(mp_subtract(one, b_var), x_var), f_var), -1),
            mp_scale(x_var, 2),
        ),
    )
    h0, h1_coefficient, h2_coefficient = (
        mp_g_coefficient(h1, degree) for degree in range(3)
    )
    b0 = mp_g_coefficient(h2, 0)
    a1 = mp_g_coefficient(h2, 1)
    first_resultant = mp_add(
        mp_subtract(mp_multiply(h2_coefficient, mp_multiply(b0, b0)),
                    mp_multiply(h1_coefficient, mp_multiply(a1, b0))),
        mp_multiply(h0, mp_multiply(a1, a1)),
    )
    u_poly, v_poly = reduce_b_quadratic(first_resultant)
    norm = xf_add(
        {(x_power + 2, f_power): value
         for (x_power, f_power), value in xf_multiply(u_poly, u_poly).items()},
        xf_add(xf_multiply(u_poly, v_poly), xf_multiply(v_poly, v_poly)),
    )
    p_terms = (
        (6, 2, 2), (6, 1, -1),
        (5, 1, -2), (5, 0, 1),
        (4, 3, 4), (4, 2, 6), (4, 1, 4),
        (3, 3, 4), (3, 2, -12), (3, 1, -11), (3, 0, -6),
        (2, 4, 2), (2, 3, -11), (2, 2, 10), (2, 1, 26), (2, 0, 8),
        (1, 4, 4), (1, 3, -2), (1, 2, -20), (1, 1, -19), (1, 0, -3),
        (0, 4, 2), (0, 3, 9), (0, 2, 14), (0, 1, 3),
    )
    expected = {(x_power + 2, f_power): 4 * coefficient
                for f_power, x_power, coefficient in p_terms}
    keys = sorted(set(norm) | set(expected))
    for key in keys:
        check(norm.get(key, 0) == expected.get(key, 0), f"resultant coefficient {key}")
    return len(keys)


def coefficient_data(cutoff):
    even, odd = parity_coefficients(cutoff // 2)
    rows = []
    for order in range(cutoff + 1):
        carrier = 1 if order == 0 else catalan(order - 1)
        if order == 0:
            fixed = 1
        elif order % 2:
            fixed = odd[(order - 1) // 2]
        else:
            fixed = even[order // 2]
        check((carrier - fixed) % 2 == 0, f"odd nonfixed count at order {order}")
        rows.append((order, carrier, fixed, (carrier - fixed) // 2))
    return rows, even, odd


def check_coupled_series(rows, cutoff):
    fixed = [0] + [rows[order][2] for order in range(1, cutoff + 1)]
    even = [value if degree % 2 == 0 else 0 for degree, value in enumerate(fixed)]
    odd = [value if degree % 2 else 0 for degree, value in enumerate(fixed)]
    one = [0] * (cutoff + 1)
    one[0] = 1
    a_x2 = [0] * (cutoff + 1)
    for order in range(1, cutoff // 2 + 1):
        a_x2[2 * order] = catalan(order - 1)

    one_minus_even = subtract(one, even, cutoff)
    first_left = multiply(
        even,
        subtract(
            multiply(one_minus_even, one_minus_even, cutoff),
            multiply(odd, odd, cutoff),
            cutoff,
        ),
        cutoff,
    )
    first_right = shift(odd, 1, cutoff)
    second_left = multiply(odd, subtract(one, a_x2, cutoff), cutoff)
    second_right = shift(add(one, even, cutoff), 1, cutoff)
    for degree in range(cutoff + 1):
        check(first_left[degree] == first_right[degree], f"E equation at {degree}")
        check(second_left[degree] == second_right[degree], f"O equation at {degree}")

    for degree, coefficient in enumerate(polynomial_residual(fixed, cutoff)):
        check(coefficient == 0, f"P(x,F) residual at {degree}")


def check_table(rows):
    table_path = Path(__file__).with_name("coefficient_table.csv")
    with table_path.open(newline="", encoding="utf-8") as handle:
        records = list(DictReader(handle))
    check(len(records) == len(rows), "coefficient table row count")
    check(
        tuple(records[0].keys()) == ("n", "total", "fixed", "two_cycles"),
        "coefficient table header",
    )
    for expected, record in zip(rows, records):
        observed = tuple(int(record[key]) for key in record)
        check(observed == expected, f"coefficient table mismatch at {expected[0]}")


def main():
    global STATES_ENUMERATED
    exhaustive_cutoff = 12
    series_cutoff = 30
    totals = [1] + [0] * exhaustive_cutoff
    fixed_counts = [1] + [0] * exhaustive_cutoff
    first_fixed_not_global = None
    first_global_not_fixed = None

    check(update_state(EMPTY) is EMPTY, "empty state is not fixed")
    STATES_ENUMERATED = 1

    for order in range(1, exhaustive_cutoff + 1):
        states = trees(order)
        check(len(states) == catalan(order - 1), f"Catalan count at order {order}")
        for tree in states:
            STATES_ENUMERATED += 1
            totals[order] += 1
            image = update(tree)
            check(apply_snapshot(trigger_snapshot(tree)) == image, "snapshot update")
            check(size(image) == order, "order changed")
            check(unordered_key(image) == unordered_key(tree), "underlying tree changed")
            check(fringe_orders(image) == fringe_orders(tree), "fringe orders changed")
            check(pointwise_fringe_preserved(tree, image), "pointwise fringe transport")
            check(update(image) == tree, "map is not an involution")
            is_fixed = image == tree
            check(is_fixed == fixed_criterion(tree), "root-local fixed criterion")
            fixed_counts[order] += int(is_fixed)

            is_global = global_mirror(tree) == tree
            check(global_mirror(global_mirror(tree)) == tree, "global mirror regression")
            if is_fixed and not is_global and first_fixed_not_global is None:
                first_fixed_not_global = (order, tree)
            if is_global and not is_fixed and first_global_not_fixed is None:
                first_global_not_fixed = (order, tree)

            for time in range(1, 7):
                expected = is_fixed or time % 2 == 0
                check((iterate(tree, time) == tree) == expected, "iterate-fixed parity")

    rows, parity_even, _ = coefficient_data(series_cutoff)
    for order in range(exhaustive_cutoff + 1):
        check(totals[order] == rows[order][1], f"carrier recurrence at {order}")
        check(fixed_counts[order] == rows[order][2], f"fixed recurrence at {order}")

    check(first_fixed_not_global == (4, ((), ((),))), "first M-not-J witness")
    check(
        first_global_not_fixed == (9, (((), ((),)), (((),), ()))),
        "first J-not-M witness",
    )

    check_coupled_series(rows, series_cutoff)
    resultant_terms = exact_resultant_audit()
    for degree, coefficient in enumerate(
        parity_elimination_residual(parity_even, series_cutoff // 2)
    ):
        check(coefficient == 0, f"Q(z,e) residual at {degree}")
    check_table(rows)

    print("odd-fringe mirror plane-tree controls: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"states_enumerated={STATES_ENUMERATED}")
    print("exhaustive_orders=0..12")
    print("series_orders=0..30")
    print("carrier_counts_0_12=" + ",".join(map(str, totals)))
    print("fixed_counts_0_12=" + ",".join(map(str, fixed_counts)))
    print(
        "two_cycle_counts_0_12="
        + ",".join(str(rows[order][3]) for order in range(exhaustive_cutoff + 1))
    )
    print("first_fixed_not_global_mirror=(4,((), ((),)))")
    print("first_global_mirror_not_fixed=(9,(((), ((),)), (((),), ())))")
    print("coupled_residual=zero_through_x^30")
    print("degree_six_residual=zero_through_x^30")
    print(f"exact_resultant=4*x^2*P ({resultant_terms}_coefficients)")
    print("parity_elimination_residual=zero_through_z^15")
    print("coefficient_table=31_rows_match")


if __name__ == "__main__":
    main()
