#!/usr/bin/env python3
"""Exact falsifier for P151: unequal finite-spider first passage.

The checker uses only integers and fractions.Fraction.  It compares a literal
vertex-state Markov recursion with an independently assembled continuant
rational transform, then checks moments, extremizers, inverse boundaries, and
the owned equal-arm collapse.  Enumeration is counterexample pressure, not a
proof or novelty certificate.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb, gcd


ASSERTIONS = 0
SECTION_ASSERTIONS: dict[str, int] = defaultdict(int)


def check(section: str, condition: bool, message: str = "") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    SECTION_ASSERTIONS[section] += 1
    if not condition:
        raise AssertionError(f"{section}: {message}")


def trim(poly):
    poly = tuple(Fraction(value) for value in poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly = poly[:-1]
    return poly


def poly_add(left, right):
    size = max(len(left), len(right))
    return trim(
        tuple(
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
            for index in range(size)
        )
    )


def poly_scale(poly, scalar):
    return trim(tuple(Fraction(scalar) * coefficient for coefficient in poly))


def poly_shift(poly, amount):
    return trim((Fraction(0),) * amount + tuple(poly))


def poly_mul(left, right):
    output = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] += a * b
    return trim(tuple(output))


def poly_derivative_at_one(poly, order=0):
    if order == 0:
        return sum(poly, Fraction(0))
    if order == 1:
        return sum((Fraction(i) * value for i, value in enumerate(poly)), Fraction(0))
    if order == 2:
        return sum(
            (Fraction(i * (i - 1)) * value for i, value in enumerate(poly)),
            Fraction(0),
        )
    raise ValueError("only derivative orders 0, 1, and 2 are used")


def quotient_derivatives(numerator, denominator):
    d0 = poly_derivative_at_one(denominator, 0)
    d1 = poly_derivative_at_one(denominator, 1)
    d2 = poly_derivative_at_one(denominator, 2)
    n0 = poly_derivative_at_one(numerator, 0)
    n1 = poly_derivative_at_one(numerator, 1)
    n2 = poly_derivative_at_one(numerator, 2)
    f0 = n0 / d0
    f1 = (n1 - d1 * f0) / d0
    f2 = (n2 - 2 * d1 * f1 - d2 * f0) / d0
    return f0, f1, f2


def quotient_series(numerator, denominator, horizon):
    if denominator[0] == 0:
        raise ZeroDivisionError("formal denominator has zero constant term")
    coefficients = []
    for degree in range(horizon + 1):
        value = numerator[degree] if degree < len(numerator) else Fraction(0)
        for offset in range(1, min(degree, len(denominator) - 1) + 1):
            value -= denominator[offset] * coefficients[degree - offset]
        coefficients.append(value / denominator[0])
    return tuple(coefficients)


@lru_cache(None)
def continuant(length):
    if length == 0:
        return (Fraction(0),)
    if length == 1:
        return (Fraction(1),)
    if length == 2:
        return (Fraction(2),)
    return poly_add(
        poly_scale(continuant(length - 1), 2),
        poly_scale(poly_shift(continuant(length - 2), 2), -1),
    )


def continuant_closed(length):
    degree = length - 1
    output = [Fraction(0)] * (2 * (degree // 2) + 1)
    for index in range(degree // 2 + 1):
        output[2 * index] = (
            Fraction((-1) ** index)
            * comb(degree - index, index)
            * (2 ** (degree - 2 * index))
        )
    return trim(tuple(output))


def spider_transform(arms):
    number_of_arms = len(arms)
    factors = tuple(continuant(length) for length in arms)
    full_product = (Fraction(1),)
    for factor in factors:
        full_product = poly_mul(full_product, factor)
    denominator = poly_scale(full_product, number_of_arms)
    numerators = []
    for i, length in enumerate(arms):
        other_product = (Fraction(1),)
        for j, factor in enumerate(factors):
            if i != j:
                other_product = poly_mul(other_product, factor)
        numerators.append(poly_shift(other_product, length))
        return_term = poly_mul(continuant(length - 1), other_product)
        denominator = poly_add(denominator, poly_scale(poly_shift(return_term, 2), -1))
    return tuple(numerators), denominator


def literal_marked_coefficients(arms, horizon):
    number_of_arms = len(arms)
    live = {("centre", 0): Fraction(1)}
    absorbed = [[Fraction(0)] * (horizon + 1) for _ in arms]
    cumulative = Fraction(0)
    mass_checks = 0
    for time in range(1, horizon + 1):
        next_live = defaultdict(Fraction)
        for state, probability in live.items():
            if state[0] == "centre":
                for arm, length in enumerate(arms):
                    weight = probability / number_of_arms
                    if length == 1:
                        absorbed[arm][time] += weight
                        cumulative += weight
                    else:
                        next_live[(arm, 1)] += weight
            else:
                arm, position = state
                weight = probability / 2
                if position == 1:
                    next_live[("centre", 0)] += weight
                else:
                    next_live[(arm, position - 1)] += weight
                if position + 1 == arms[arm]:
                    absorbed[arm][time] += weight
                    cumulative += weight
                else:
                    next_live[(arm, position + 1)] += weight
        live = dict(next_live)
        check(
            "literal_transform",
            sum(live.values(), Fraction(0)) + cumulative == 1,
            f"mass profile={arms}, time={time}",
        )
        mass_checks += 1
    return tuple(tuple(row) for row in absorbed), mass_checks


def verify_continuants():
    for length in range(1, 101):
        polynomial = continuant(length)
        check(
            "continuants",
            polynomial == continuant_closed(length),
            f"closed continuant length={length}",
        )
        check(
            "continuants",
            poly_derivative_at_one(polynomial, 0) == length,
            f"P_l(1) length={length}",
        )
        check(
            "continuants",
            poly_derivative_at_one(polynomial, 1)
            == -Fraction(length * (length - 1) * (length - 2), 3),
            f"P_l'(1) length={length}",
        )
        check(
            "continuants",
            polynomial[0] == 2 ** (length - 1),
            f"P_l(0) length={length}",
        )


def verify_literal_transform():
    profiles = 0
    for number_of_arms in range(2, 6):
        for arms in product(range(1, 5), repeat=number_of_arms):
            profiles += 1
            horizon = 2 * sum(arms) + 12
            numerators, denominator = spider_transform(arms)
            check(
                "literal_transform",
                denominator[0] != 0,
                f"nonzero formal denominator profile={arms}",
            )
            literal, _ = literal_marked_coefficients(arms, horizon)
            total_numerator = (Fraction(0),)
            for arm, numerator in enumerate(numerators):
                total_numerator = poly_add(total_numerator, numerator)
                predicted = quotient_series(numerator, denominator, horizon)
                for time in range(horizon + 1):
                    check(
                        "literal_transform",
                        literal[arm][time] == predicted[time],
                        f"coefficient profile={arms}, arm={arm}, time={time}",
                    )
                    check(
                        "literal_transform",
                        (predicted[time] == 0) if (time - arms[arm]) % 2 else True,
                        f"parity profile={arms}, arm={arm}, time={time}",
                    )
                check(
                    "literal_transform",
                    literal[arm][arms[arm]] == Fraction(1, number_of_arms * 2 ** (arms[arm] - 1)),
                    f"first atom profile={arms}, arm={arm}",
                )

                endpoint, _, _ = quotient_derivatives(numerator, denominator)
                harmonic = Fraction(1, arms[arm]) / sum(
                    (Fraction(1, length) for length in arms), Fraction(0)
                )
                check(
                    "moments",
                    endpoint == harmonic,
                    f"endpoint profile={arms}, arm={arm}",
                )

            mass, mean, second_factorial = quotient_derivatives(total_numerator, denominator)
            reciprocal_sum = sum((Fraction(1, length) for length in arms), Fraction(0))
            total_length = sum(arms)
            cube_sum = sum(length**3 for length in arms)
            predicted_mean = Fraction(total_length) / reciprocal_sum
            predicted_variance = (
                Fraction(cube_sum - 2 * total_length, 3) / reciprocal_sum
                + Fraction(total_length**2, 3) / reciprocal_sum**2
            )
            variance = second_factorial + mean - mean**2
            check("moments", mass == 1, f"total transform mass profile={arms}")
            check("moments", mean == predicted_mean, f"mean profile={arms}")
            check("moments", variance == predicted_variance, f"variance profile={arms}")
    return profiles


def verify_excursion_moments():
    for length in range(1, 81):
        success_numerator = poly_shift((Fraction(1),), length)
        return_numerator = poly_shift(continuant(length - 1), 2)
        denominator = continuant(length)
        success = quotient_derivatives(success_numerator, denominator)
        returning = quotient_derivatives(return_numerator, denominator)
        attempt_numerator = poly_add(success_numerator, return_numerator)
        attempt = quotient_derivatives(attempt_numerator, denominator)
        check(
            "excursion_moments",
            success[0] == Fraction(1, length),
            f"success probability length={length}",
        )
        check(
            "excursion_moments",
            returning[0] == 1 - Fraction(1, length),
            f"return probability length={length}",
        )
        check(
            "excursion_moments",
            attempt[1] == length,
            f"attempt mean length={length}",
        )
        check(
            "excursion_moments",
            attempt[2] + attempt[1] == Fraction(length * (length**2 + 2), 3),
            f"attempt second moment length={length}",
        )
        check(
            "excursion_moments",
            returning[1] == Fraction(2 * (length**2 - 1), 3 * length),
            f"return-truncated duration length={length}",
        )


def positive_compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(1, total - parts + 2):
        for remainder in positive_compositions(total - first, parts - 1):
            yield (first,) + remainder


def verify_fixed_mass_extremizers():
    profiles = 0
    for number_of_arms in range(2, 7):
        for total_length in range(number_of_arms, 25):
            quotient, remainder = divmod(total_length, number_of_arms)
            lower_denominator = Fraction(number_of_arms - 1) + Fraction(
                1, total_length - number_of_arms + 1
            )
            upper_denominator = Fraction(number_of_arms - remainder, quotient)
            if remainder:
                upper_denominator += Fraction(remainder, quotient + 1)
            lower = Fraction(total_length) / lower_denominator
            upper = Fraction(total_length) / upper_denominator
            for arms in positive_compositions(total_length, number_of_arms):
                profiles += 1
                reciprocal_sum = sum((Fraction(1, length) for length in arms), Fraction(0))
                mean = Fraction(total_length) / reciprocal_sum
                extreme = sorted(arms) == [1] * (number_of_arms - 1) + [
                    total_length - number_of_arms + 1
                ]
                balanced = max(arms) - min(arms) <= 1
                check("fixed_mass_extrema", mean >= lower, f"lower bound profile={arms}")
                check(
                    "fixed_mass_extrema",
                    (mean == lower) == extreme,
                    f"lower equality profile={arms}",
                )
                check("fixed_mass_extrema", mean <= upper, f"upper bound profile={arms}")
                check(
                    "fixed_mass_extrema",
                    (mean == upper) == balanced,
                    f"upper equality profile={arms}",
                )
    return profiles


def lcm(left, right):
    return left // gcd(left, right) * right


def primitive_from_endpoint(endpoint):
    ratios = tuple(endpoint[0] / probability for probability in endpoint)
    common_denominator = 1
    for ratio in ratios:
        common_denominator = lcm(common_denominator, ratio.denominator)
    integers = [int(ratio * common_denominator) for ratio in ratios]
    common_divisor = 0
    for value in integers:
        common_divisor = gcd(common_divisor, value)
    return tuple(value // common_divisor for value in integers)


def verify_inverse_boundary():
    profiles = 0
    for number_of_arms in range(2, 6):
        for arms in product(range(1, 9), repeat=number_of_arms):
            profiles += 1
            reciprocal_sum = sum((Fraction(1, length) for length in arms), Fraction(0))
            endpoint = tuple(Fraction(1, length) / reciprocal_sum for length in arms)
            primitive = primitive_from_endpoint(endpoint)
            common_divisor = 0
            for length in arms:
                common_divisor = gcd(common_divisor, length)
            expected_primitive = tuple(length // common_divisor for length in arms)
            check(
                "inverse_boundary",
                primitive == expected_primitive,
                f"primitive recovery profile={arms}",
            )
            mean = Fraction(sum(arms)) / reciprocal_sum
            recovered_scale_squared = (
                mean
                * sum((Fraction(1, value) for value in primitive), Fraction(0))
                / sum(primitive)
            )
            check(
                "inverse_boundary",
                recovered_scale_squared == common_divisor**2,
                f"mean scale recovery profile={arms}",
            )
            dilated = tuple(2 * length for length in arms)
            dilated_reciprocal_sum = sum(
                (Fraction(1, length) for length in dilated), Fraction(0)
            )
            dilated_endpoint = tuple(
                Fraction(1, length) / dilated_reciprocal_sum for length in dilated
            )
            dilated_mean = Fraction(sum(dilated)) / dilated_reciprocal_sum
            check(
                "inverse_boundary",
                dilated_endpoint == endpoint,
                f"endpoint dilation blindness profile={arms}",
            )
            check(
                "inverse_boundary",
                dilated_mean == 4 * mean,
                f"quadratic mean scaling profile={arms}",
            )
    return profiles


def verify_equal_arm_owned_control():
    for number_of_arms in range(2, 9):
        for length in range(1, 13):
            arms = (length,) * number_of_arms
            numerators, denominator = spider_transform(arms)
            total_numerator = (Fraction(0),)
            for numerator in numerators:
                total_numerator = poly_add(total_numerator, numerator)
            radial_numerator = poly_shift((Fraction(1),), length)
            radial_denominator = poly_add(
                continuant(length),
                poly_scale(poly_shift(continuant(length - 1), 2), -1),
            )
            check(
                "equal_arm_owned_control",
                poly_mul(total_numerator, radial_denominator)
                == poly_mul(radial_numerator, denominator),
                f"equal-arm radial collapse r={number_of_arms}, length={length}",
            )
            for numerator in numerators:
                check(
                    "equal_arm_owned_control",
                    poly_scale(numerator, number_of_arms) == total_numerator,
                    f"equal-arm mark symmetry r={number_of_arms}, length={length}",
                )


def main():
    verify_continuants()
    literal_profiles = verify_literal_transform()
    verify_excursion_moments()
    extremal_profiles = verify_fixed_mass_extremizers()
    inverse_profiles = verify_inverse_boundary()
    verify_equal_arm_owned_control()
    print("P151 unequal-spider exact verifier")
    print(f"literal_profiles={literal_profiles}")
    print(f"fixed_mass_profiles={extremal_profiles}")
    print(f"inverse_profiles={inverse_profiles}")
    for section in sorted(SECTION_ASSERTIONS):
        print(f"{section}={SECTION_ASSERTIONS[section]}")
    print(f"assertions={ASSERTIONS}")
    print("arithmetic=integer_and_Fraction_only")
    print("enumeration_is_not_proof=1")
    print("external_status=HOLD_EXTERNAL")
    print("PASS")


if __name__ == "__main__":
    main()

