#!/usr/bin/env python3
"""Exact finite controls for the monomial-toggle contraction cocycle.

The script uses only the Python standard library.  Every probability and
matrix entry is a ``Fraction``; no pseudorandom or floating-point lane is
used.  Finite enumeration is a falsification control, not a proof of the
paper's limit theorems.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import product


ASSERTIONS = 0
LANE_ASSERTIONS = Counter()
CASES = Counter()


def check(condition, lane, message):
    global ASSERTIONS
    if not condition:
        raise AssertionError(f"{lane}: {message}")
    ASSERTIONS += 1
    LANE_ASSERTIONS[lane] += 1


def matmul(left, right):
    """Multiply two row-major 2-by-2 matrices."""
    return (
        left[0] * right[0] + left[1] * right[2],
        left[0] * right[1] + left[1] * right[3],
        left[2] * right[0] + left[3] * right[2],
        left[2] * right[1] + left[3] * right[3],
    )


def determinant(matrix):
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]


def literal_word_state(word, a):
    """Return literal product and independently recorded normal-form data."""
    identity = (F(1), F(0), F(0), F(1))
    stay = (a, F(0), F(0), F(1))
    toggle = (F(0), F(1), a, F(0))
    matrix = identity
    orientation = 0
    visits_zero = 0
    signed_occupation = 0
    toggles = 0
    for letter in word:
        visits_zero += int(orientation == 0)
        signed_occupation += 1 if orientation == 0 else -1
        matrix = matmul(toggle if letter else stay, matrix)
        if letter:
            orientation ^= 1
            toggles += 1
    return matrix, orientation, visits_zero, signed_occupation, toggles


def normal_matrix(a, n, orientation, visits_zero):
    visits_one = n - visits_zero
    if orientation == 0:
        return (a**visits_zero, F(0), F(0), a**visits_one)
    return (F(0), a**visits_one, a**visits_zero, F(0))


def occupation_dp(n, q):
    """Distribution of (orientation, pre-update visits to orientation zero)."""
    stay = 1 - q
    distribution = {(0, 0): F(1)}
    for _ in range(n):
        nxt = {}
        for (orientation, visits_zero), mass in distribution.items():
            new_visits = visits_zero + int(orientation == 0)
            same = (orientation, new_visits)
            flipped = (orientation ^ 1, new_visits)
            nxt[same] = nxt.get(same, F(0)) + stay * mass
            nxt[flipped] = nxt.get(flipped, F(0)) + q * mass
        distribution = nxt
    return distribution


def normal_form_lane():
    """Literal matrices versus normal form, Gram spectrum, and occupation DP."""
    for a in (F(1, 2), F(2, 3), F(3, 4)):
        for q in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
            stay = 1 - q
            for n in range(13):
                literal_distribution = {}
                literal_moments = {s: F(0) for s in (1, 2, 3)}
                for word in product((0, 1), repeat=n):
                    matrix, orientation, visits_zero, signed_sum, toggles = (
                        literal_word_state(word, a)
                    )
                    normal = normal_matrix(a, n, orientation, visits_zero)
                    visits_one = n - visits_zero
                    expected_signed = 2 * visits_zero - n
                    check(matrix == normal, "normal_form", "literal word mismatch")
                    check(
                        orientation == (sum(word) % 2),
                        "normal_form",
                        "orientation parity mismatch",
                    )
                    check(
                        signed_sum == expected_signed,
                        "normal_form",
                        "signed occupation mismatch",
                    )
                    check(
                        determinant(matrix) == (-1) ** toggles * a**n,
                        "normal_form",
                        "signed determinant mismatch",
                    )

                    # M^T M is computed from the literal matrix, independently
                    # of the asserted normal form.
                    gram_11 = matrix[0] ** 2 + matrix[2] ** 2
                    gram_22 = matrix[1] ** 2 + matrix[3] ** 2
                    gram_12 = matrix[0] * matrix[1] + matrix[2] * matrix[3]
                    check(gram_12 == 0, "normal_form", "literal columns not orthogonal")
                    check(
                        sorted((gram_11, gram_22))
                        == sorted((a ** (2 * visits_zero), a ** (2 * visits_one))),
                        "normal_form",
                        "literal Gram spectrum mismatch",
                    )

                    weight = q**toggles * stay ** (n - toggles)
                    state = (orientation, visits_zero)
                    literal_distribution[state] = (
                        literal_distribution.get(state, F(0)) + weight
                    )
                    for s in literal_moments:
                        literal_moments[s] += (
                            weight * a ** (s * min(visits_zero, visits_one))
                        )
                    CASES["normal_form_words"] += 1

                dynamic = occupation_dp(n, q)
                check(
                    dynamic == literal_distribution,
                    "occupation_dp",
                    "word law and Markov DP differ",
                )
                check(
                    sum(dynamic.values(), F(0)) == 1,
                    "occupation_dp",
                    "occupation law not normalized",
                )
                for s in (1, 2, 3):
                    dynamic_moment = sum(
                        mass * a ** (s * min(visits_zero, n - visits_zero))
                        for (_, visits_zero), mass in dynamic.items()
                    )
                    check(
                        dynamic_moment == literal_moments[s],
                        "occupation_dp",
                        f"order-{s} singular moment mismatch",
                    )
                CASES["occupation_distributions"] += 1


def signed_transfer(n, q, t, direction=1):
    """Exact row-vector evaluation of e_+^T (E_{+/-} P)^n 1."""
    stay = 1 - q
    state_zero = F(1)
    state_one = F(0)
    for _ in range(n):
        weight_zero = t if direction == 1 else 1 / t
        weight_one = 1 / t if direction == 1 else t
        weighted_zero = state_zero * weight_zero
        weighted_one = state_one * weight_one
        state_zero, state_one = (
            stay * weighted_zero + q * weighted_one,
            q * weighted_zero + stay * weighted_one,
        )
    return state_zero + state_one


def signed_sum_dp(n, q):
    """Independent DP for the joint law of terminal orientation and Z_n."""
    stay = 1 - q
    distribution = {(0, 0): F(1)}
    for _ in range(n):
        nxt = {}
        for (orientation, signed_sum), mass in distribution.items():
            new_sum = signed_sum + (1 if orientation == 0 else -1)
            same = (orientation, new_sum)
            flipped = (orientation ^ 1, new_sum)
            nxt[same] = nxt.get(same, F(0)) + stay * mass
            nxt[flipped] = nxt.get(flipped, F(0)) + q * mass
        distribution = nxt
    return distribution


def transfer_lane():
    """Literal signed transforms versus transfer matrices and absolute DP."""
    for q in (F(0), F(1, 5), F(1, 2), F(4, 5), F(1)):
        stay = 1 - q
        for t in (F(3, 2), F(2), F(5, 2)):
            for n in range(12):
                literal_plus = F(0)
                literal_minus = F(0)
                literal_absolute = F(0)
                for word in product((0, 1), repeat=n):
                    _, _, _, signed_sum, toggles = literal_word_state(word, F(1, 2))
                    weight = q**toggles * stay ** (n - toggles)
                    literal_plus += weight * t**signed_sum
                    literal_minus += weight * t ** (-signed_sum)
                    literal_absolute += weight * t ** abs(signed_sum)
                    CASES["signed_transform_words"] += 1

                transfer_plus = signed_transfer(n, q, t, 1)
                transfer_minus = signed_transfer(n, q, t, -1)
                distribution = signed_sum_dp(n, q)
                dynamic_absolute = sum(
                    mass * t ** abs(signed_sum)
                    for (_, signed_sum), mass in distribution.items()
                )
                check(
                    literal_plus == transfer_plus,
                    "signed_transfer",
                    "positive signed transform mismatch",
                )
                check(
                    literal_minus == transfer_minus,
                    "signed_transfer",
                    "negative signed transform mismatch",
                )
                check(
                    literal_absolute == dynamic_absolute,
                    "signed_transfer",
                    "absolute transform DP mismatch",
                )
                check(
                    literal_absolute <= literal_plus + literal_minus,
                    "signed_transfer",
                    "lower absolute-transform bound failed",
                )
                check(
                    literal_plus + literal_minus <= 2 * literal_absolute,
                    "signed_transfer",
                    "upper absolute-transform bound failed",
                )
                check(
                    sum(distribution.values(), F(0)) == 1,
                    "signed_transfer",
                    "signed-sum distribution not normalized",
                )
                CASES["signed_transfer_parameters"] += 1


def recurrence_lane():
    """Cayley--Hamilton recurrence, strict-root sentinel, and endpoints."""
    for q in (F(0), F(1, 5), F(1, 2), F(4, 5), F(1)):
        stay = 1 - q
        for t in (F(3, 2), F(2), F(5, 2)):
            trace = stay * (t + 1 / t)
            determinant_k = stay - q
            values = [signed_transfer(n, q, t, 1) for n in range(27)]
            check(values[0] == 1, "recurrence", "m_0 mismatch")
            check(values[1] == t, "recurrence", "m_1 mismatch")
            for n in range(25):
                check(
                    values[n + 2]
                    == trace * values[n + 1] - determinant_k * values[n],
                    "recurrence",
                    "Cayley--Hamilton recurrence mismatch",
                )
                CASES["signed_recurrences"] += 1
            at_one = 1 - trace + determinant_k
            check(
                at_one == stay * (2 - t - 1 / t),
                "recurrence",
                "characteristic polynomial at one mismatch",
            )
            if 0 < q < 1:
                check(at_one < 0, "recurrence", "strict Perron-root sentinel failed")
            for n in range(27):
                absolute = sum(
                    mass * t ** abs(signed_sum)
                    for (_, signed_sum), mass in signed_sum_dp(n, q).items()
                )
                if q == 0:
                    check(
                        absolute == t**n,
                        "endpoint",
                        "q=0 absolute transform mismatch",
                    )
                elif q == 1:
                    check(
                        absolute == t ** (n % 2),
                        "endpoint",
                        "q=1 parity transform mismatch",
                    )
                CASES["endpoint_times"] += int(q in (0, 1))


def occupation_moment_lane():
    """Finite exact moments and the martingale CLT variance coefficient."""
    for q in (F(1, 5), F(1, 3), F(1, 2), F(2, 3), F(4, 5)):
        stay = 1 - q
        rho = 1 - 2 * q
        variance_rate = (1 - q) / q
        check(
            variance_rate == (1 + rho) / (1 - rho),
            "clt_variance",
            "correlation-sum variance identity failed",
        )
        check(
            variance_rate == (1 - rho * rho) / (1 - rho) ** 2,
            "clt_variance",
            "martingale variance identity failed",
        )
        for y in (F(-1), F(1)):
            xi_same = y - rho * y
            xi_flip = -y - rho * y
            check(
                stay * xi_same + q * xi_flip == 0,
                "clt_variance",
                "conditional martingale mean failed",
            )
            check(
                stay * xi_same**2 + q * xi_flip**2 == 1 - rho**2,
                "clt_variance",
                "conditional martingale variance failed",
            )

        for n in range(81):
            distribution = signed_sum_dp(n, q)
            mean = sum(mass * signed_sum for (_, signed_sum), mass in distribution.items())
            second = sum(
                mass * signed_sum**2
                for (_, signed_sum), mass in distribution.items()
            )
            expected_mean = (
                F(0) if n == 0 else (1 - rho**n) / (1 - rho)
            )
            expected_second = F(n) + 2 * sum(
                F(n - lag) * rho**lag for lag in range(1, n)
            )
            check(
                sum(distribution.values(), F(0)) == 1,
                "occupation_moments",
                "signed-sum law not normalized",
            )
            check(mean == expected_mean, "occupation_moments", "mean mismatch")
            check(second == expected_second, "occupation_moments", "second moment mismatch")
            check(second - mean**2 >= 0, "occupation_moments", "negative variance")
            CASES["occupation_moment_times"] += 1


def main():
    normal_form_lane()
    transfer_lane()
    recurrence_lane()
    occupation_moment_lane()
    print("monomial-toggle exact control: PASS")
    print(f"assertions={ASSERTIONS}")
    print(f"normal_form_words={CASES['normal_form_words']}")
    print(f"signed_transform_words={CASES['signed_transform_words']}")
    print(f"occupation_distributions={CASES['occupation_distributions']}")
    print(f"signed_transfer_parameter_cases={CASES['signed_transfer_parameters']}")
    print(f"signed_recurrence_steps={CASES['signed_recurrences']}")
    print(f"occupation_moment_times={CASES['occupation_moment_times']}")
    print(f"endpoint_times={CASES['endpoint_times']}")
    print(
        "lane_assertions="
        + ",".join(f"{name}:{LANE_ASSERTIONS[name]}" for name in sorted(LANE_ASSERTIONS))
    )


if __name__ == "__main__":
    main()
