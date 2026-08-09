#!/usr/bin/env python3
"""Exact producer for the HCS-C22 T1--T3 certificate.

The producer uses exact ``Fraction`` arithmetic for the common geometry and
for every interval enclosure.  Square roots are enclosed by integer square
root bounds at a frozen decimal scale; floating point is never used to decide
any pass/fail gate.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Iterable, Sequence

import sympy as sp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "c22_certificate.json"

A_MIN = Fraction(59, 10)
A_MAX = Fraction(61, 10)
PARAMETERS = {"0": A_MIN, "1": A_MAX}
X_INTERVALS = {
    -1: (Fraction(-5, 8), Fraction(-1, 3)),
    1: (Fraction(1, 3), Fraction(5, 8)),
}
Y_INTERVALS = {
    -1: (Fraction(-81, 128), Fraction(-5, 16)),
    1: (Fraction(5, 16), Fraction(81, 128)),
}
STATE_NAMES = ("--", "-+", "+-", "++")
STATE_SIGNS = ((-1, -1), (-1, 1), (1, -1), (1, 1))
STATE_INDEX = {value: index for index, value in enumerate(STATE_SIGNS)}
ADJACENCY = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)
ALLOWED_EDGES = {
    (source, target)
    for source in range(4)
    for target in range(4)
    if ADJACENCY[source][target]
}
PRIMARY_PAIRS = (
    ("bigram", "0000101", "0001001"),
    ("trigram", "00101011", "00101101"),
)
SQRT_DIGITS = 90
CONTRACTION_UPPER = Fraction(49, 100)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--sqrt-digits", type=int, default=SQRT_DIGITS)
    parser.add_argument("--max-period", type=int, default=10)
    return parser.parse_args()


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def fraction_payload(value: Fraction) -> dict[str, object]:
    return {"fraction": fraction_text(value), "decimal": format(float(value), ".17g")}


@dataclass(frozen=True)
class QInterval:
    lower: Fraction
    upper: Fraction

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise ValueError((self.lower, self.upper))

    @classmethod
    def point(cls, value: Fraction | int) -> "QInterval":
        item = Fraction(value)
        return cls(item, item)

    def __add__(self, other: "QInterval") -> "QInterval":
        return QInterval(self.lower + other.lower, self.upper + other.upper)

    def __neg__(self) -> "QInterval":
        return QInterval(-self.upper, -self.lower)

    def __sub__(self, other: "QInterval") -> "QInterval":
        return self + (-other)

    def __mul__(self, other: "QInterval") -> "QInterval":
        values = (
            self.lower * other.lower,
            self.lower * other.upper,
            self.upper * other.lower,
            self.upper * other.upper,
        )
        return QInterval(min(values), max(values))

    def reciprocal(self) -> "QInterval":
        if self.lower <= 0 <= self.upper:
            raise ZeroDivisionError(self)
        return QInterval(Fraction(1, 1) / self.upper, Fraction(1, 1) / self.lower)

    def contains(self, value: Fraction | int) -> bool:
        item = Fraction(value)
        return self.lower <= item <= self.upper

    def width(self) -> Fraction:
        return self.upper - self.lower

    def payload(self) -> dict[str, object]:
        return {
            "lower": fraction_text(self.lower),
            "upper": fraction_text(self.upper),
            "lower_decimal": format(float(self.lower), ".17g"),
            "upper_decimal": format(float(self.upper), ".17g"),
        }


def sqrt_fraction_bounds(value: Fraction, digits: int) -> QInterval:
    """Return exact rational bounds of width at most 10**(-digits)."""

    if value < 0:
        raise ValueError("cannot enclose a negative square root")
    scale = 10**digits
    radicand_floor = value.numerator * scale * scale // value.denominator
    lower_integer = isqrt(radicand_floor)
    lower = Fraction(lower_integer, scale)
    if lower * lower == value:
        return QInterval.point(lower)
    return QInterval(lower, Fraction(lower_integer + 1, scale))


def interval_sqrt(value: QInterval, digits: int) -> QInterval:
    if value.lower < 0:
        raise ValueError(value)
    lower = sqrt_fraction_bounds(value.lower, digits).lower
    upper = sqrt_fraction_bounds(value.upper, digits).upper
    return QInterval(lower, upper)


def sum_intervals(values: Iterable[QInterval]) -> QInterval:
    result = QInterval.point(0)
    for value in values:
        result = result + value
    return result


def outward_decimal_interval(value: QInterval, digits: int) -> QInterval:
    """Round an interval outwards to a shared power-of-ten denominator."""

    if digits < 1:
        raise ValueError(digits)
    scale = 10**digits
    lower_integer = value.lower.numerator * scale // value.lower.denominator
    upper_integer = -(
        (-value.upper.numerator * scale) // value.upper.denominator
    )
    return QInterval(Fraction(lower_integer, scale), Fraction(upper_integer, scale))


def face_image(
    x_value: Fraction,
    y_interval: tuple[Fraction, Fraction],
) -> QInterval:
    square = x_value * x_value
    return QInterval(
        1 - A_MAX * square - y_interval[1],
        1 - A_MIN * square - y_interval[0],
    )


def t1_geometry_certificate() -> dict[str, object]:
    covering_records: list[dict[str, object]] = []
    forbidden_records: list[dict[str, object]] = []
    for source, target in sorted(ALLOWED_EDGES):
        source_x_sign, source_y_sign = STATE_SIGNS[source]
        target_x_sign, target_y_sign = STATE_SIGNS[target]
        source_x = X_INTERVALS[source_x_sign]
        source_y = Y_INTERVALS[source_y_sign]
        target_x = X_INTERVALS[target_x_sign]
        target_y = Y_INTERVALS[target_y_sign]
        left = face_image(source_x[0], source_y)
        right = face_image(source_x[1], source_y)
        entry_margin = min(source_x[0] - target_y[0], target_y[1] - source_x[1])
        increasing = left.upper < target_x[0] and right.lower > target_x[1]
        decreasing = right.upper < target_x[0] and left.lower > target_x[1]
        if increasing:
            crossing_margin = min(target_x[0] - left.upper, right.lower - target_x[1])
            degree = 1
        elif decreasing:
            crossing_margin = min(target_x[0] - right.upper, left.lower - target_x[1])
            degree = -1
        else:
            crossing_margin = Fraction(0)
            degree = 0
        covering_records.append(
            {
                "source": STATE_NAMES[source],
                "target": STATE_NAMES[target],
                "left_face_image": left.payload(),
                "right_face_image": right.payload(),
                "entry_margin": fraction_payload(entry_margin),
                "crossing_margin": fraction_payload(crossing_margin),
                "degree": degree,
                "pass": target_y_sign == source_x_sign
                and entry_margin > 0
                and crossing_margin > 0
                and degree != 0,
            }
        )

    for source in range(4):
        for target in range(4):
            if (source, target) in ALLOWED_EDGES:
                continue
            source_x_sign, source_y_sign = STATE_SIGNS[source]
            target_x_sign, target_y_sign = STATE_SIGNS[target]
            if target_y_sign != source_x_sign:
                source_x = X_INTERVALS[source_x_sign]
                target_y = Y_INTERVALS[target_y_sign]
                gap = (
                    target_y[0] - source_x[1]
                    if source_x[1] < target_y[0]
                    else source_x[0] - target_y[1]
                )
                reason = "entry_sign_mismatch"
                passed = gap > 0
            else:
                source_x = X_INTERVALS[source_x_sign]
                source_y = Y_INTERVALS[source_y_sign]
                maximum = max(
                    face_image(source_x[0], source_y).upper,
                    face_image(source_x[1], source_y).upper,
                )
                gap = X_INTERVALS[target_x_sign][0] - maximum
                reason = "positive_entry_source_misses_positive_exit"
                passed = source_y_sign == 1 and target_x_sign == 1 and gap > 0
            forbidden_records.append(
                {
                    "source": STATE_NAMES[source],
                    "target": STATE_NAMES[target],
                    "reason": reason,
                    "gap": fraction_payload(gap),
                    "pass": passed,
                }
            )

    x_half_width = Fraction(7, 48)
    y_half_width = Fraction(41, 256)
    kappa = Fraction(1, 2)
    xy_ratio = y_half_width / x_half_width
    yx_ratio = x_half_width / y_half_width
    forward_denominator = 2 * A_MIN * Fraction(1, 3) - xy_ratio * kappa
    backward_denominator = 2 * A_MIN * Fraction(5, 16) - yx_ratio * kappa
    forward_slope = yx_ratio / forward_denominator
    backward_slope = xy_ratio / backward_denominator
    input_norm_sq = 1 + kappa * kappa
    forward_expansion_sq = forward_denominator * forward_denominator / input_norm_sq
    backward_expansion_sq = backward_denominator * backward_denominator / input_norm_sq

    numerator_ranges = {
        "negative_negative": QInterval(Fraction(5, 3), Fraction(9, 4)),
        "mixed": QInterval(Fraction(17, 24), Fraction(31, 24)),
    }
    radicand_ranges = {
        name: QInterval(value.lower / A_MAX, value.upper / A_MIN)
        for name, value in numerator_ranges.items()
    }
    lower_square = Fraction(1, 9)
    upper_square = Fraction(25, 64)
    self_map_margins = {
        name: {
            "lower_square_margin": fraction_payload(value.lower - lower_square),
            "upper_square_margin": fraction_payload(upper_square - value.upper),
            "pass": value.lower > lower_square and value.upper < upper_square,
        }
        for name, value in radicand_ranges.items()
    }
    contraction_squared = Fraction(240, 1003)
    contraction_decimal_squared = Fraction(49, 100) ** 2

    all_coverings = all(bool(item["pass"]) for item in covering_records)
    all_forbidden = all(bool(item["pass"]) for item in forbidden_records)
    all_self_map = all(bool(item["pass"]) for item in self_map_margins.values())
    cone_pass = (
        forward_slope < kappa
        and backward_slope < kappa
        and forward_expansion_sq > 1
        and backward_expansion_sq > 1
    )
    return {
        "map": "H_a(q,p)=(1-a*q^2-p,q)",
        "parameter_interval": [fraction_text(A_MIN), fraction_text(A_MAX)],
        "maximal_self_map_window_from_frozen_boxes": ["144/25", "51/8"],
        "covering_window_from_frozen_boxes": ["289/50", "99/16"],
        "state_order": list(STATE_NAMES),
        "adjacency": [list(row) for row in ADJACENCY],
        "covering_records": covering_records,
        "forbidden_records": forbidden_records,
        "minimum_covering_margin": fraction_payload(
            min(Fraction(item["crossing_margin"]["fraction"]) for item in covering_records)
        ),
        "minimum_forbidden_gap": fraction_payload(
            min(Fraction(item["gap"]["fraction"]) for item in forbidden_records)
        ),
        "entry_margin": fraction_payload(Fraction(1, 128)),
        "signed_root": {
            "numerator_ranges": {
                name: value.payload() for name, value in numerator_ranges.items()
            },
            "radicand_ranges": {
                name: value.payload() for name, value in radicand_ranges.items()
            },
            "self_map_margins": self_map_margins,
            "contraction_squared": fraction_payload(contraction_squared),
            "contraction_upper": fraction_payload(CONTRACTION_UPPER),
            "contraction_vs_upper_squared_margin": fraction_payload(
                contraction_decimal_squared - contraction_squared
            ),
            "pass": all_self_map
            and contraction_squared < contraction_decimal_squared,
        },
        "cone": {
            "kappa": fraction_payload(kappa),
            "forward_denominator": fraction_payload(forward_denominator),
            "forward_slope": fraction_payload(forward_slope),
            "forward_expansion_squared": fraction_payload(forward_expansion_sq),
            "backward_denominator": fraction_payload(backward_denominator),
            "backward_slope": fraction_payload(backward_slope),
            "backward_expansion_squared": fraction_payload(backward_expansion_sq),
            "pass": cone_pass,
        },
        "decisions": {
            "six_coverings": len(covering_records) == 6 and all_coverings,
            "ten_forbidden": len(forbidden_records) == 10 and all_forbidden,
            "uniform_signed_root_contraction": all_self_map
            and contraction_squared < contraction_decimal_squared,
            "uniform_two_sided_cones": cone_pass,
            "t1_pass": all_coverings and all_forbidden and all_self_map and cone_pass,
        },
    }


def admissible_sign_word(signs: Sequence[int]) -> bool:
    n = len(signs)
    return all(
        not (signs[(index - 1) % n] == 1 and signs[(index + 1) % n] == 1)
        for index in range(n)
    )


def rotations(word: Sequence[object]) -> list[tuple[object, ...]]:
    values = tuple(word)
    return [values[index:] + values[:index] for index in range(len(values))]


def primitive_word(word: Sequence[object]) -> bool:
    values = tuple(word)
    n = len(values)
    return all(values != values[:d] * (n // d) for d in range(1, n) if n % d == 0)


def least_period(word: Sequence[object]) -> int:
    values = tuple(word)
    n = len(values)
    for d in range(1, n + 1):
        if n % d == 0 and values == values[:d] * (n // d):
            return d
    raise AssertionError(values)


def joint_canonical(
    parameter_word: Sequence[int], signs: Sequence[int]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    pairs = tuple(zip(parameter_word, signs, strict=True))
    canonical = min(rotations(pairs))
    return tuple(item[0] for item in canonical), tuple(item[1] for item in canonical)


def joint_primitive(parameter_word: Sequence[int], signs: Sequence[int]) -> bool:
    pairs = tuple(zip(parameter_word, signs, strict=True))
    return primitive_word(pairs)


def state_word(signs: Sequence[int]) -> tuple[int, ...]:
    result = tuple(
        STATE_INDEX[(signs[index], signs[(index - 1) % len(signs)])]
        for index in range(len(signs))
    )
    if not all(ADJACENCY[result[i]][result[(i + 1) % len(result)]] for i in range(len(result))):
        raise AssertionError((signs, result))
    return result


def divisors(value: int) -> list[int]:
    return [item for item in range(1, value + 1) if value % item == 0]


def mobius(value: int) -> int:
    factors = 0
    remaining = value
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            factors += 1
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        factors += 1
    return -1 if factors % 2 else 1


def joint_combinatorics(max_period: int) -> dict[str, object]:
    matrix = sp.Matrix(ADJACENCY)
    rows: list[dict[str, object]] = []
    for n in range(1, max_period + 1):
        sign_words = [
            tuple(values)
            for values in itertools.product((-1, 1), repeat=n)
            if admissible_sign_word(values)
        ]
        fixed_joint = (2**n) * len(sign_words)
        canonical: set[tuple[tuple[int, int], ...]] = set()
        for parameter_word in itertools.product((0, 1), repeat=n):
            for signs in sign_words:
                pairs = tuple(zip(parameter_word, signs, strict=True))
                if primitive_word(pairs):
                    canonical.add(min(rotations(pairs)))
        expected_orbits = sum(
            mobius(d) * ((2 ** (n // d)) * int(sp.trace(matrix ** (n // d))))
            for d in divisors(n)
        ) // n
        identifiers = [
            "".join(str(item[0]) for item in word)
            + "|"
            + "".join("+" if item[1] > 0 else "-" for item in word)
            for word in sorted(canonical)
        ]
        digest = hashlib.sha256("\n".join(identifiers).encode("ascii")).hexdigest()
        base_period_distribution: dict[int, int] = {}
        for joint_word in canonical:
            base_period = least_period(tuple(item[0] for item in joint_word))
            base_period_distribution[base_period] = (
                base_period_distribution.get(base_period, 0) + 1
            )
        all_base_necklaces = {
            min(rotations(word)) for word in itertools.product((0, 1), repeat=n)
        }
        primitive_base_necklaces = {
            word for word in all_base_necklaces if primitive_word(word)
        }
        achiral_primitive = sum(
            min(rotations(word[::-1])) == word for word in primitive_base_necklaces
        )
        primitive_chiral_pairs = (len(primitive_base_necklaces) - achiral_primitive) // 2
        all_base_bracelets = {
            min(word, min(rotations(word[::-1]))) for word in all_base_necklaces
        }
        rows.append(
            {
                "period": n,
                "state_fixed_words": len(sign_words),
                "trace_A_power": int(sp.trace(matrix**n)),
                "joint_fixed_points": fixed_joint,
                "primitive_joint_necklaces": len(canonical),
                "mobius_expected": expected_orbits,
                "canonical_ids_sha256": digest,
                "joint_orbits_by_base_least_period": {
                    str(key): value for key, value in sorted(base_period_distribution.items())
                },
                "parameter_classes": {
                    "all_cyclic_necklaces": len(all_base_necklaces),
                    "primitive_cyclic_necklaces": len(primitive_base_necklaces),
                    "achiral_primitive_necklaces": achiral_primitive,
                    "primitive_chiral_pairs": primitive_chiral_pairs,
                    "primitive_dihedral_classes": achiral_primitive
                    + primitive_chiral_pairs,
                    "all_dihedral_bracelets": len(all_base_bracelets),
                },
                "pass": len(sign_words) == int(sp.trace(matrix**n))
                and len(canonical) == expected_orbits,
            }
        )
    return {"period_rows": rows, "pass": all(bool(row["pass"]) for row in rows)}


def cyclic_ngram_counts(word: str, width: int) -> tuple[tuple[str, int], ...]:
    n = len(word)
    counts: dict[str, int] = {}
    for index in range(n):
        token = "".join(word[(index + offset) % n] for offset in range(width))
        counts[token] = counts.get(token, 0) + 1
    return tuple(sorted(counts.items()))


def dihedral_orbit(word: str) -> set[str]:
    direct = {word[index:] + word[:index] for index in range(len(word))}
    reverse = word[::-1]
    return direct | {reverse[index:] + reverse[:index] for index in range(len(word))}


def minimal_matched_pair(width: int, max_period: int = 10) -> dict[str, object]:
    for n in range(1, max_period + 1):
        representatives: list[str] = []
        seen: set[str] = set()
        for values in itertools.product("01", repeat=n):
            word = "".join(values)
            if not primitive_word(word) or word in seen:
                continue
            orbit = dihedral_orbit(word)
            seen.update(orbit)
            representatives.append(word)
        for left, right in itertools.combinations(representatives, 2):
            if cyclic_ngram_counts(left, width) == cyclic_ngram_counts(right, width):
                return {
                    "width": width,
                    "period": n,
                    "left": left,
                    "right": right,
                    "counts": list(cyclic_ngram_counts(left, width)),
                }
    raise RuntimeError(width)


def signed_sqrt_midpoint(value: Fraction, sign: int, digits: int) -> Fraction:
    bounds = sqrt_fraction_bounds(value, digits)
    midpoint = (bounds.lower + bounds.upper) / 2
    return midpoint if sign > 0 else -midpoint


def absolute_difference(value: Fraction) -> Fraction:
    return value if value >= 0 else -value


def certify_branch(word: str, signs: tuple[int, ...], digits: int) -> dict[str, object]:
    n = len(word)
    parameters = tuple(PARAMETERS[item] for item in word)
    coordinates = tuple(Fraction(sign, 2) for sign in signs)
    threshold = Fraction(1, 10 ** (digits - 12))
    for iteration in range(1, 2001):
        updated = tuple(
            signed_sqrt_midpoint(
                (1 - coordinates[(index - 1) % n] - coordinates[(index + 1) % n])
                / parameters[index],
                signs[index],
                digits,
            )
            for index in range(n)
        )
        delta = max(
            absolute_difference(new - old)
            for new, old in zip(updated, coordinates, strict=True)
        )
        coordinates = updated
        if delta < threshold:
            break
    else:
        raise RuntimeError((word, signs))

    image_intervals: list[QInterval] = []
    residual_upper = Fraction(0)
    for index, sign in enumerate(signs):
        radicand = (
            1 - coordinates[(index - 1) % n] - coordinates[(index + 1) % n]
        ) / parameters[index]
        root = sqrt_fraction_bounds(radicand, digits)
        image = root if sign > 0 else QInterval(-root.upper, -root.lower)
        image_intervals.append(image)
        residual_upper = max(
            residual_upper,
            absolute_difference(image.lower - coordinates[index]),
            absolute_difference(image.upper - coordinates[index]),
        )
    error = residual_upper / (1 - CONTRACTION_UPPER)
    coordinate_intervals = tuple(
        QInterval(value - error, value + error) for value in coordinates
    )
    if not all(
        X_INTERVALS[sign][0] < interval.lower <= interval.upper < X_INTERVALS[sign][1]
        for sign, interval in zip(signs, coordinate_intervals, strict=True)
    ):
        raise AssertionError("certified coordinate left its sign box")

    matrix = (
        (QInterval.point(1), QInterval.point(0)),
        (QInterval.point(0), QInterval.point(1)),
    )
    for parameter, coordinate in zip(parameters, coordinate_intervals, strict=True):
        jacobian = (
            (QInterval.point(-2 * parameter) * coordinate, QInterval.point(-1)),
            (QInterval.point(1), QInterval.point(0)),
        )
        matrix = interval_matrix_product(jacobian, matrix)
    trace = matrix[0][0] + matrix[1][1]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if not determinant.contains(1):
        raise AssertionError("interval monodromy determinant misses one")
    if trace.lower > 2:
        absolute_trace = trace
    elif trace.upper < -2:
        absolute_trace = QInterval(-trace.upper, -trace.lower)
    else:
        raise AssertionError("branch hyperbolicity was not certified")
    discriminant = absolute_trace * absolute_trace - QInterval.point(4)
    report_digits = digits - 20
    weight_digits = digits - 25
    trace_report = outward_decimal_interval(trace, report_digits)
    determinant_report = outward_decimal_interval(determinant, report_digits)
    unstable = outward_decimal_interval(
        (absolute_trace + interval_sqrt(discriminant, digits))
        * QInterval.point(Fraction(1, 2)),
        report_digits,
    )
    inverse_unstable = outward_decimal_interval(
        unstable.reciprocal(), weight_digits
    )
    flat_denominator = QInterval.point(2) - trace
    signed_flat = outward_decimal_interval(
        flat_denominator.reciprocal(), weight_digits
    )
    absolute_flat_denominator = (
        flat_denominator
        if flat_denominator.lower > 0
        else QInterval(-flat_denominator.upper, -flat_denominator.lower)
    )
    absolute_flat = outward_decimal_interval(
        absolute_flat_denominator.reciprocal(), weight_digits
    )

    return {
        "sign_word": "".join("+" if item > 0 else "-" for item in signs),
        "state_word": [STATE_NAMES[index] for index in state_word(signs)],
        "iterations": iteration,
        "center": [fraction_text(item) for item in coordinates],
        "residual_upper": fraction_text(residual_upper),
        "banach_error_upper": fraction_text(error),
        "coordinate_intervals": [item.payload() for item in coordinate_intervals],
        "monodromy_trace": trace_report.payload(),
        "monodromy_determinant": determinant_report.payload(),
        "unstable_modulus": unstable.payload(),
        "inverse_unstable": inverse_unstable.payload(),
        "signed_flat": signed_flat.payload(),
        "absolute_flat": absolute_flat.payload(),
        "pass": True,
    }


def interval_matrix_product(
    left: tuple[tuple[QInterval, QInterval], tuple[QInterval, QInterval]],
    right: tuple[tuple[QInterval, QInterval], tuple[QInterval, QInterval]],
) -> tuple[tuple[QInterval, QInterval], tuple[QInterval, QInterval]]:
    return tuple(
        tuple(
            sum_intervals(left[i][k] * right[k][j] for k in range(2))
            for j in range(2)
        )
        for i in range(2)
    )  # type: ignore[return-value]


def all_admissible_sign_words(period: int) -> list[tuple[int, ...]]:
    return [
        tuple(values)
        for values in itertools.product((-1, 1), repeat=period)
        if admissible_sign_word(values)
    ]


def sector_certificate(word: str, digits: int, keep_branches: bool = True) -> dict[str, object]:
    branches = [certify_branch(word, signs, digits) for signs in all_admissible_sign_words(len(word))]
    aggregates: dict[str, QInterval] = {}
    for key in ("inverse_unstable", "absolute_flat", "signed_flat", "monodromy_trace"):
        aggregates[key] = sum_intervals(
            QInterval(
                Fraction(branch[key]["lower"]),
                Fraction(branch[key]["upper"]),
            )
            for branch in branches
        )
    canonical_rotation = min(word[index:] + word[:index] for index in range(len(word)))
    reversed_word = word[::-1]
    reversal_canonical = min(
        reversed_word[index:] + reversed_word[:index] for index in range(len(word))
    )
    return {
        "protocol": word,
        "period": len(word),
        "oriented_sector": True,
        "reversal_is_metadata_not_quotient": True,
        "canonical_rotation": canonical_rotation,
        "reversal_sector_id": reversal_canonical,
        "reversal_same_necklace": canonical_rotation == reversal_canonical,
        "parameter_counts": {"0": word.count("0"), "1": word.count("1")},
        "state_branch_count": len(branches),
        "expected_trace_A_power": int(sp.trace(sp.Matrix(ADJACENCY) ** len(word))),
        "base_primitive_implies_all_joint_branches_primitive": primitive_word(word),
        "aggregates": {key: value.payload() for key, value in aggregates.items()},
        "branches": branches if keep_branches else [],
        "pass": len(branches) == int(sp.trace(sp.Matrix(ADJACENCY) ** len(word)))
        and all(bool(branch["pass"]) for branch in branches),
    }


def interval_from_payload(payload: dict[str, object]) -> QInterval:
    return QInterval(Fraction(str(payload["lower"])), Fraction(str(payload["upper"])))


def compare_sectors(left: dict[str, object], right: dict[str, object]) -> dict[str, object]:
    comparisons: dict[str, object] = {}
    for key in ("inverse_unstable", "absolute_flat", "signed_flat", "monodromy_trace"):
        left_interval = interval_from_payload(left["aggregates"][key])
        right_interval = interval_from_payload(right["aggregates"][key])
        difference = left_interval - right_interval
        disjoint = difference.upper < 0 or difference.lower > 0
        separation = (
            right_interval.lower - left_interval.upper
            if left_interval.upper < right_interval.lower
            else left_interval.lower - right_interval.upper
            if right_interval.upper < left_interval.lower
            else Fraction(0)
        )
        comparisons[key] = {
            "difference": difference.payload(),
            "intervals_disjoint": disjoint,
            "separation_margin": fraction_payload(separation),
        }
    return {
        "left": left["protocol"],
        "right": right["protocol"],
        "comparisons": comparisons,
        "intrinsic_aggregate_separation_pass": bool(
            comparisons["inverse_unstable"]["intervals_disjoint"]
        ),
        "absolute_flat_separation_pass": bool(
            comparisons["absolute_flat"]["intervals_disjoint"]
        ),
        "all_reported_aggregate_separations_pass": all(
            bool(item["intervals_disjoint"]) for item in comparisons.values()
        ),
    }


def intervals_overlap(left: QInterval, right: QInterval) -> bool:
    return not (left.upper < right.lower or right.upper < left.lower)


def symmetry_control(
    reference: dict[str, object], transformed: dict[str, object], kind: str
) -> dict[str, object]:
    checks = {}
    for key in ("inverse_unstable", "absolute_flat", "signed_flat"):
        first = interval_from_payload(reference["aggregates"][key])
        second = interval_from_payload(transformed["aggregates"][key])
        checks[key] = intervals_overlap(first, second)
    transformed_by_sign = {
        branch["sign_word"]: branch for branch in transformed["branches"]
    }
    branch_rows = []
    mapping_ids = []
    for branch in reference["branches"]:
        reference_sign = branch["sign_word"]
        if kind == "cyclic_rotation":
            transformed_sign = reference_sign[1:] + reference_sign[:1]
        elif kind == "reversal":
            transformed_sign = reference_sign[::-1]
        else:
            raise ValueError(kind)
        partner = transformed_by_sign.get(transformed_sign)
        branch_checks = {}
        if partner is not None:
            for key in (
                "monodromy_trace",
                "inverse_unstable",
                "absolute_flat",
                "signed_flat",
            ):
                branch_checks[key] = intervals_overlap(
                    interval_from_payload(branch[key]),
                    interval_from_payload(partner[key]),
                )
        mapping_ids.append(f"{reference_sign}>{transformed_sign}")
        branch_rows.append(
            {
                "reference_sign": reference_sign,
                "transformed_sign": transformed_sign,
                "partner_present": partner is not None,
                "checks": branch_checks,
                "pass": partner is not None and all(branch_checks.values()),
            }
        )
    mapping_sha256 = hashlib.sha256(
        "\n".join(mapping_ids).encode("ascii")
    ).hexdigest()
    return {
        "kind": kind,
        "reference": reference["protocol"],
        "transformed": transformed["protocol"],
        "aggregate_checks": checks,
        "branch_count": len(branch_rows),
        "branch_mapping_sha256": mapping_sha256,
        "branch_rows": branch_rows,
        "pass": all(checks.values()) and all(bool(row["pass"]) for row in branch_rows),
    }


def finite_field_witness() -> dict[str, object]:
    prime = 43
    parameters = {"0": 36, "1": 19}
    cases = (("0000101", (29, 23)), ("0001001", (37, 27)))

    def multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
        return [
            [sum(left[i][k] * right[k][j] for k in range(2)) % prime for j in range(2)]
            for i in range(2)
        ]

    records = []
    for word, start in cases:
        q, p = start
        matrix = [[1, 0], [0, 1]]
        for symbol in word:
            parameter = parameters[symbol]
            derivative = [[-2 * parameter * q % prime, -1 % prime], [1, 0]]
            matrix = multiply(derivative, matrix)
            q, p = (1 - parameter * q * q - p) % prime, q
        trace = (matrix[0][0] + matrix[1][1]) % prime
        determinant_i_minus = (
            (1 - matrix[0][0]) * (1 - matrix[1][1]) - matrix[0][1] * matrix[1][0]
        ) % prime
        records.append(
            {
                "protocol": word,
                "fixed_point": list(start),
                "return_point": [q, p],
                "monodromy": matrix,
                "trace": trace,
                "determinant_I_minus_M": determinant_i_minus,
                "inverse_flat_weight": pow(determinant_i_minus, -1, prime),
                "pass": (q, p) == start,
            }
        )
    return {
        "prime": prime,
        "parameter_residues": parameters,
        "records": records,
        "traces_distinct": records[0]["trace"] != records[1]["trace"],
        "pass": all(bool(item["pass"]) for item in records)
        and records[0]["trace"] != records[1]["trace"],
    }


def t3_symbolic_certificate(max_period: int = 8) -> dict[str, object]:
    hill_rows = []
    for n in range(1, max_period + 1):
        symbols = sp.symbols(f"b0:{n}")
        monodromy = sp.eye(2)
        for symbol in symbols:
            monodromy = sp.Matrix([[-symbol, -1], [1, 0]]) * monodromy
        if n == 1:
            cyclic_jacobian = sp.Matrix([[symbols[0] + 2]])
        elif n == 2:
            cyclic_jacobian = sp.Matrix([[symbols[0], 2], [2, symbols[1]]])
        else:
            cyclic_jacobian = sp.zeros(n)
            for index, symbol in enumerate(symbols):
                cyclic_jacobian[index, index] = symbol
                cyclic_jacobian[index, (index - 1) % n] += 1
                cyclic_jacobian[index, (index + 1) % n] += 1
        det_i_minus = sp.expand(2 - sp.trace(monodromy))
        difference = sp.expand(
            cyclic_jacobian.det() - ((-1) ** (n + 1)) * det_i_minus
        )
        leading_product = sp.prod(symbols)
        trace_leading = sp.expand(sp.trace(monodromy)).coeff(leading_product)
        hill_rows.append(
            {
                "period": n,
                "hill_identity_pass": difference == 0,
                "trace_top_product_coefficient": int(trace_leading),
                "expected_trace_top_product_coefficient": (-1) ** n,
                "quotient_basis_length": 2**n,
                "pass": difference == 0 and trace_leading == (-1) ** n,
            }
        )
    z = sp.symbols("z")
    adjacency = sp.kronecker_product(sp.ones(2, 2), sp.Matrix(ADJACENCY))
    local_bare_denominator = sp.factor((sp.eye(8) - z * adjacency).det())
    return {
        "hypotheses": [
            "all protocol parameters are nonzero",
            "cyclic-orbit scheme or saturated projective closure",
            "pointwise trace sums require a reduced/nondegenerate fixed scheme",
            "pointwise determinant identification requires nondegeneracy at every repetition",
        ],
        "fixed_scheme_length": "2^n with scheme multiplicity",
        "global_unit_numerator_residue_sum": "0",
        "global_trace_inserted_residue_sum": "-2^n",
        "global_unit_numerator_residue_determinant": "1",
        "pointwise_flat_identification": (
            "equals the residue determinant only when every repeated fixed "
            "scheme is reduced/nondegenerate"
        ),
        "full_shift_global_bare_zeta": "1/(1-4*z)",
        "local_symbolic_bare_denominator": str(local_bare_denominator),
        "hill_rows": hill_rows,
        "naive_P2_compactification_warning": True,
        "zero_parameter_counterexample": "H_0^4=identity",
        "pass": all(bool(row["pass"]) for row in hill_rows)
        and sp.expand(local_bare_denominator - (1 - 2 * z - 8 * z**3 - 16 * z**4)) == 0,
    }


def main() -> None:
    args = parse_args()
    if args.sqrt_digits < 40:
        raise SystemExit("sqrt-digits must be at least 40")
    if args.max_period < 8:
        raise SystemExit("max-period must be at least 8")

    t1 = t1_geometry_certificate()
    combinatorics = joint_combinatorics(args.max_period)
    minimal_pairs = {
        "bigram": minimal_matched_pair(2),
        "trigram": minimal_matched_pair(3),
    }
    sectors: dict[str, dict[str, object]] = {}
    comparisons = []
    controls = []
    for label, left_word, right_word in PRIMARY_PAIRS:
        left = sector_certificate(left_word, args.sqrt_digits)
        right = sector_certificate(right_word, args.sqrt_digits)
        sectors[left_word] = left
        sectors[right_word] = right
        comparisons.append({"label": label, **compare_sectors(left, right)})

        for reference in (left, right):
            reference_word = str(reference["protocol"])
            rotation_word = reference_word[1:] + reference_word[:1]
            reverse_word = reference_word[::-1]
            rotation_sector = sector_certificate(
                rotation_word, args.sqrt_digits, keep_branches=True
            )
            reverse_sector = sector_certificate(
                reverse_word, args.sqrt_digits, keep_branches=True
            )
            controls.append(
                symmetry_control(reference, rotation_sector, "cyclic_rotation")
            )
            controls.append(symmetry_control(reference, reverse_sector, "reversal"))

    t2_pass = (
        combinatorics["pass"]
        and all(bool(item["pass"]) for item in sectors.values())
        and all(bool(item["intrinsic_aggregate_separation_pass"]) for item in comparisons)
        and all(bool(item["all_reported_aggregate_separations_pass"]) for item in comparisons)
        and all(bool(item["pass"]) for item in controls)
    )
    t3 = t3_symbolic_certificate()
    output = {
        "material_passport": {
            "id": "HCS-C22-T1-T3",
            "type": "exact_computer_assisted_certificate",
            "status": "VERIFIED_BY_PRODUCER_PENDING_INDEPENDENT_CHECK",
            "determinism": "deterministic_exact_rational",
        },
        "run_id": "HCS_C22_T1_T3_PRODUCER_V1",
        "coordinate_and_clock": {
            "state": "z_i=(q_i,q_{i-1})",
            "chronology": "later protocol symbols act on the left",
            "primitive_object": "joint parameter-state necklace",
            "clock": "one skew-product microstep",
        },
        "numerical_policy": {
            "sqrt_enclosure_decimal_digits": args.sqrt_digits,
            "sqrt_rounding_mode": "integer-isqrt lower bound and one-unit rational upper bound",
            "all_gate_decisions_exact_rational": True,
            "contraction_upper_used": fraction_text(CONTRACTION_UPPER),
            "python_version": platform.python_version(),
            "sympy_version": sp.__version__,
        },
        "t1_common_survivor": t1,
        "t2_joint_chronology": {
            "combinatorics": combinatorics,
            "minimal_matched_pairs": minimal_pairs,
            "sectors": sectors,
            "comparisons": comparisons,
            "symmetry_controls": controls,
            "finite_field_control": finite_field_witness(),
            "pass": t2_pass,
        },
        "t3_global_collapse": t3,
        "decisions": {
            "t1_pass": bool(t1["decisions"]["t1_pass"]),
            "t2_pass": bool(t2_pass),
            "t3_pass": bool(t3["pass"]),
            "positive_result": (
                "tested local intrinsic instability aggregates differ despite matching "
                "cyclic parameter bigram and trigram ledgers, modulo cyclic/reversal symmetry"
            ),
            "negative_result": (
                "the unit-numerator all-complex signed residue determinant "
                "collapses identically to one"
            ),
            "operator_gate_authorized": bool(t1["decisions"]["t1_pass"] and t2_pass and t3["pass"]),
        },
        "scope": {
            "certified": [
                "common local real h-set geometry and fibre cones",
                "uniform signed-root coding for the frozen two-letter interval",
                "joint primitive combinatorics through the frozen cutoff",
                "complete local real branch aggregation for two matched-ledger protocol pairs",
                "global cyclic-scheme and signed-residue collapse theorem controls",
            ],
            "not_certified": [
                "common complex pinning domain",
                "nuclear transfer operator or Fredholm determinant",
                "arithmetic primitive mechanism",
                "Hilbert-Polya spectral realization",
            ],
        },
    }
    if not all(
        (
            output["decisions"]["t1_pass"],
            output["decisions"]["t2_pass"],
            output["decisions"]["t3_pass"],
        )
    ):
        raise SystemExit("at least one T1--T3 producer gate failed")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "t1_pass": output["decisions"]["t1_pass"],
                "t2_pass": output["decisions"]["t2_pass"],
                "t3_pass": output["decisions"]["t3_pass"],
                "operator_gate_authorized": output["decisions"]["operator_gate_authorized"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
