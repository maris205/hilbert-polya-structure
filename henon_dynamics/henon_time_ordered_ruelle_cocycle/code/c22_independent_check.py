#!/usr/bin/env python3
"""Nonimporting checker for the HCS-C22 T1--T3 producer artifact.

This file deliberately imports neither ``c22_producer`` nor any earlier Hénon
project.  It reconstructs the rational geometry, contraction audit, joint
necklaces, Banach residual bounds, interval monodromies, finite-field control,
and symbolic Hill identities from the serialized certificate.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Iterable, Sequence

import sympy as sp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = PROJECT_ROOT / "results" / "c22_certificate.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "results" / "c22_independent_check.json"

LOWER_A = Fraction(59, 10)
UPPER_A = Fraction(61, 10)
LETTER_A = {"0": LOWER_A, "1": UPPER_A}
X_BOX = {
    -1: (Fraction(-5, 8), Fraction(-1, 3)),
    1: (Fraction(1, 3), Fraction(5, 8)),
}
Y_BOX = {
    -1: (Fraction(-81, 128), Fraction(-5, 16)),
    1: (Fraction(5, 16), Fraction(81, 128)),
}
NAMES = ("--", "-+", "+-", "++")
SIGNS = ((-1, -1), (-1, 1), (1, -1), (1, 1))
GRAPH = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


@dataclass(frozen=True)
class Box:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError(self)

    @classmethod
    def scalar(cls, value: Fraction | int) -> "Box":
        item = Fraction(value)
        return cls(item, item)

    def __add__(self, other: "Box") -> "Box":
        return Box(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self) -> "Box":
        return Box(-self.hi, -self.lo)

    def __sub__(self, other: "Box") -> "Box":
        return self + (-other)

    def __mul__(self, other: "Box") -> "Box":
        candidates = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return Box(min(candidates), max(candidates))

    def inverse(self) -> "Box":
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError(self)
        return Box(1 / self.hi, 1 / self.lo)

    def subset_of(self, other: "Box") -> bool:
        return other.lo <= self.lo and self.hi <= other.hi

    def contains(self, value: Fraction | int) -> bool:
        item = Fraction(value)
        return self.lo <= item <= self.hi


def add_boxes(items: Iterable[Box]) -> Box:
    answer = Box.scalar(0)
    for item in items:
        answer = answer + item
    return answer


def parse_box(payload: dict[str, object]) -> Box:
    return Box(Fraction(str(payload["lower"])), Fraction(str(payload["upper"])))


def rational_sqrt_box(value: Fraction, digits: int) -> Box:
    if value < 0:
        raise ValueError(value)
    scale = 10**digits
    integer = isqrt(value.numerator * scale * scale // value.denominator)
    lower = Fraction(integer, scale)
    upper = lower if lower * lower == value else Fraction(integer + 1, scale)
    return Box(lower, upper)


def sqrt_box(value: Box, digits: int) -> Box:
    return Box(
        rational_sqrt_box(value.lo, digits).lo,
        rational_sqrt_box(value.hi, digits).hi,
    )


def product_matrix(
    left: tuple[tuple[Box, Box], tuple[Box, Box]],
    right: tuple[tuple[Box, Box], tuple[Box, Box]],
) -> tuple[tuple[Box, Box], tuple[Box, Box]]:
    return tuple(
        tuple(add_boxes(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def check_t1(payload: dict[str, object]) -> dict[str, bool]:
    checks: dict[str, bool] = {}
    parameter_interval = tuple(Fraction(value) for value in payload["parameter_interval"])
    derived_self_window = (
        Fraction(64, 25) * Fraction(9, 4),
        9 * Fraction(17, 24),
    )
    derived_covering_window = (
        max(Fraction(289, 50), Fraction(499, 150), Fraction(84, 25)),
        min(Fraction(237, 16), Fraction(99, 16), Fraction(807, 128)),
    )
    checks["parameter_interval"] = parameter_interval == (LOWER_A, UPPER_A)
    checks["parameter_inside_derived_windows"] = (
        derived_self_window[0] < parameter_interval[0]
        <= parameter_interval[1] < derived_self_window[1]
        and derived_covering_window[0] < parameter_interval[0]
        <= parameter_interval[1] < derived_covering_window[1]
    )
    checks["self_map_window"] = tuple(
        Fraction(value) for value in payload["maximal_self_map_window_from_frozen_boxes"]
    ) == derived_self_window
    checks["covering_window"] = tuple(
        Fraction(value) for value in payload["covering_window_from_frozen_boxes"]
    ) == derived_covering_window

    entry_margins = []
    for sign in (-1, 1):
        x_interval = X_BOX[sign]
        y_interval = Y_BOX[sign]
        entry_margins.extend(
            (x_interval[0] - y_interval[0], y_interval[1] - x_interval[1])
        )
    checks["entry_containment"] = (
        min(entry_margins) == Fraction(1, 128)
        and Fraction(payload["entry_margin"]["fraction"]) == Fraction(1, 128)
    )

    square_lower = Fraction(17, 24) / UPPER_A
    square_upper = Fraction(9, 4) / LOWER_A
    checks["self_map_exact"] = (
        square_lower == Fraction(85, 732)
        and square_upper == Fraction(45, 118)
        and square_lower - Fraction(1, 9) == Fraction(11, 2196)
        and Fraction(25, 64) - square_upper == Fraction(35, 3776)
    )
    theta_squared = 1 / (LOWER_A * Fraction(17, 24))
    checks["contraction_exact"] = (
        theta_squared == Fraction(240, 1003)
        and Fraction(1, 4) - theta_squared == Fraction(43, 4012)
    )

    allowed = {(i, j) for i in range(4) for j in range(4) if GRAPH[i][j]}
    crossing_margins = []
    forbidden_gaps = []
    for source, target in allowed:
        sx, sy = SIGNS[source]
        tx, ty = SIGNS[target]
        x_interval = X_BOX[sx]
        y_interval = Y_BOX[sy]
        target_x = X_BOX[tx]

        def face(x: Fraction) -> Box:
            return Box(
                1 - UPPER_A * x * x - y_interval[1],
                1 - LOWER_A * x * x - y_interval[0],
            )

        left = face(x_interval[0])
        right = face(x_interval[1])
        if left.hi < target_x[0] and right.lo > target_x[1]:
            margin = min(target_x[0] - left.hi, right.lo - target_x[1])
        elif right.hi < target_x[0] and left.lo > target_x[1]:
            margin = min(target_x[0] - right.hi, left.lo - target_x[1])
        else:
            margin = Fraction(0)
        crossing_margins.append(margin)
        checks[f"cover_{NAMES[source]}_{NAMES[target]}"] = ty == sx and margin > 0

    for source in range(4):
        for target in range(4):
            if (source, target) in allowed:
                continue
            sx, sy = SIGNS[source]
            tx, ty = SIGNS[target]
            if ty != sx:
                source_x = X_BOX[sx]
                target_y = Y_BOX[ty]
                gap = (
                    target_y[0] - source_x[1]
                    if source_x[1] < target_y[0]
                    else source_x[0] - target_y[1]
                )
            else:
                inner_max = 1 - LOWER_A * Fraction(1, 9) - Y_BOX[sy][0]
                gap = X_BOX[tx][0] - inner_max
            forbidden_gaps.append(gap)
            checks[f"forbid_{NAMES[source]}_{NAMES[target]}"] = gap > 0

    checks["minimum_crossing"] = min(crossing_margins) == Fraction(7, 720)
    checks["minimum_forbidden"] = min(forbidden_gaps) == Fraction(217, 720)

    rx = Fraction(7, 48)
    ry = Fraction(41, 256)
    kappa = Fraction(1, 2)
    forward_denom = 2 * LOWER_A / 3 - (ry / rx) * kappa
    backward_denom = 2 * LOWER_A * Fraction(5, 16) - (rx / ry) * kappa
    forward_slope = (rx / ry) / forward_denom
    backward_slope = (ry / rx) / backward_denom
    checks["cone_exact"] = (
        forward_denom == Fraction(11371, 3360)
        and backward_denom == Fraction(6361, 1968)
        and forward_slope == Fraction(125440, 466211)
        and backward_slope == Fraction(15129, 44527)
        and forward_denom**2 / (1 + kappa**2) == Fraction(129299641, 14112000)
        and backward_denom**2 / (1 + kappa**2) == Fraction(40462321, 4841280)
        and forward_slope < kappa
        and backward_slope < kappa
    )
    checks["producer_decision"] = all(bool(value) for value in payload["decisions"].values())
    return checks


def admissible(values: Sequence[int]) -> bool:
    n = len(values)
    return all(not (values[(i - 1) % n] == 1 and values[(i + 1) % n] == 1) for i in range(n))


def all_rotations(values: Sequence[object]) -> list[tuple[object, ...]]:
    word = tuple(values)
    return [word[i:] + word[:i] for i in range(len(word))]


def primitive(values: Sequence[object]) -> bool:
    word = tuple(values)
    n = len(word)
    return all(word != word[:d] * (n // d) for d in range(1, n) if n % d == 0)


def minimum_period(values: Sequence[object]) -> int:
    word = tuple(values)
    for d in range(1, len(word) + 1):
        if len(word) % d == 0 and word == word[:d] * (len(word) // d):
            return d
    raise AssertionError(word)


def check_joint_combinatorics(payload: dict[str, object]) -> dict[str, bool]:
    checks = {}
    rows = payload["period_rows"]
    matrix = sp.Matrix(GRAPH)
    for row in rows:
        n = int(row["period"])
        state_words = [word for word in itertools.product((-1, 1), repeat=n) if admissible(word)]
        canonical = set()
        for base in itertools.product((0, 1), repeat=n):
            for signs in state_words:
                pairs = tuple(zip(base, signs, strict=True))
                if primitive(pairs):
                    canonical.add(min(all_rotations(pairs)))
        ids = [
            "".join(str(item[0]) for item in word)
            + "|"
            + "".join("+" if item[1] > 0 else "-" for item in word)
            for word in sorted(canonical)
        ]
        digest = hashlib.sha256("\n".join(ids).encode("ascii")).hexdigest()
        base_distribution: dict[str, int] = {}
        for joint_word in canonical:
            period = str(minimum_period(tuple(item[0] for item in joint_word)))
            base_distribution[period] = base_distribution.get(period, 0) + 1
        all_necklaces = {
            min(all_rotations(word)) for word in itertools.product((0, 1), repeat=n)
        }
        primitive_necklaces = {word for word in all_necklaces if primitive(word)}
        achiral = sum(
            min(all_rotations(word[::-1])) == word for word in primitive_necklaces
        )
        chiral_pairs = (len(primitive_necklaces) - achiral) // 2
        bracelets = {
            min(word, min(all_rotations(word[::-1]))) for word in all_necklaces
        }
        parameter_classes = row["parameter_classes"]
        checks[f"period_{n}"] = (
            len(state_words) == int(sp.trace(matrix**n)) == int(row["state_fixed_words"])
            and len(canonical) == int(row["primitive_joint_necklaces"])
            and digest == row["canonical_ids_sha256"]
            and int(row["joint_fixed_points"]) == (2**n) * len(state_words)
            and base_distribution == row["joint_orbits_by_base_least_period"]
            and int(parameter_classes["all_cyclic_necklaces"]) == len(all_necklaces)
            and int(parameter_classes["primitive_cyclic_necklaces"]) == len(primitive_necklaces)
            and int(parameter_classes["achiral_primitive_necklaces"]) == achiral
            and int(parameter_classes["primitive_chiral_pairs"]) == chiral_pairs
            and int(parameter_classes["primitive_dihedral_classes"]) == achiral + chiral_pairs
            and int(parameter_classes["all_dihedral_bracelets"]) == len(bracelets)
        )
    return checks


def cyclic_word_profile(word: str, width: int) -> tuple[tuple[str, int], ...]:
    counts: dict[str, int] = {}
    for start in range(len(word)):
        token = "".join(word[(start + offset) % len(word)] for offset in range(width))
        counts[token] = counts.get(token, 0) + 1
    return tuple(sorted(counts.items()))


def dihedral_words(word: str) -> set[str]:
    rotations = {word[index:] + word[:index] for index in range(len(word))}
    reverse = word[::-1]
    return rotations | {
        reverse[index:] + reverse[:index] for index in range(len(word))
    }


def reconstruct_minimal_pair(width: int, max_period: int) -> tuple[int, str, str, tuple[tuple[str, int], ...]]:
    for period in range(1, max_period + 1):
        representatives: list[str] = []
        consumed: set[str] = set()
        for values in itertools.product("01", repeat=period):
            word = "".join(values)
            if not primitive(tuple(word)) or word in consumed:
                continue
            orbit = dihedral_words(word)
            consumed.update(orbit)
            representatives.append(word)
        for left_index, left in enumerate(representatives):
            for right in representatives[left_index + 1 :]:
                profile = cyclic_word_profile(left, width)
                if profile == cyclic_word_profile(right, width):
                    return period, left, right, profile
    raise AssertionError((width, max_period))


def check_minimal_matched_pairs(payload: dict[str, object]) -> dict[str, bool]:
    checks: dict[str, bool] = {}
    for label, width in (("bigram", 2), ("trigram", 3)):
        declared = payload[label]
        period, left, right, profile = reconstruct_minimal_pair(width, 10)
        declared_profile = tuple((str(token), int(count)) for token, count in declared["counts"])
        checks[label] = (
            int(declared["width"]) == width
            and int(declared["period"]) == period
            and str(declared["left"]) == left
            and str(declared["right"]) == right
            and declared_profile == profile
            and right not in dihedral_words(left)
        )
    return checks


def verify_branch(word: str, branch: dict[str, object], digits: int) -> dict[str, bool]:
    signs = tuple(1 if value == "+" else -1 for value in branch["sign_word"])
    center = tuple(Fraction(value) for value in branch["center"])
    n = len(word)
    parameters = tuple(LETTER_A[value] for value in word)
    residual = Fraction(0)
    for i, sign in enumerate(signs):
        radicand = (1 - center[(i - 1) % n] - center[(i + 1) % n]) / parameters[i]
        root = rational_sqrt_box(radicand, digits)
        image = root if sign > 0 else Box(-root.hi, -root.lo)
        residual = max(residual, abs(image.lo - center[i]), abs(image.hi - center[i]))
    declared_residual = Fraction(branch["residual_upper"])
    error = Fraction(branch["banach_error_upper"])
    coordinates = tuple(parse_box(value) for value in branch["coordinate_intervals"])
    checks = {
        "residual": residual <= declared_residual,
        "banach": error >= residual / (1 - Fraction(49, 100)),
        "coordinate_formula": all(
            interval.lo <= value - error and interval.hi >= value + error
            for interval, value in zip(coordinates, center, strict=True)
        ),
        "inside_sign_box": all(
            X_BOX[sign][0] < interval.lo <= interval.hi < X_BOX[sign][1]
            for sign, interval in zip(signs, coordinates, strict=True)
        ),
    }

    monodromy = (
        (Box.scalar(1), Box.scalar(0)),
        (Box.scalar(0), Box.scalar(1)),
    )
    for parameter, coordinate in zip(parameters, coordinates, strict=True):
        jacobian = (
            (Box.scalar(-2 * parameter) * coordinate, Box.scalar(-1)),
            (Box.scalar(1), Box.scalar(0)),
        )
        monodromy = product_matrix(jacobian, monodromy)
    trace = monodromy[0][0] + monodromy[1][1]
    determinant = monodromy[0][0] * monodromy[1][1] - monodromy[0][1] * monodromy[1][0]
    trace_declared = parse_box(branch["monodromy_trace"])
    determinant_declared = parse_box(branch["monodromy_determinant"])
    checks["trace_enclosure"] = trace.subset_of(trace_declared)
    checks["determinant_enclosure"] = determinant.subset_of(determinant_declared) and determinant_declared.contains(1)
    checks["hyperbolic"] = trace.hi < -2 or trace.lo > 2

    abs_trace = trace if trace.lo > 2 else Box(-trace.hi, -trace.lo)
    unstable = (abs_trace + sqrt_box(abs_trace * abs_trace - Box.scalar(4), digits)) * Box.scalar(Fraction(1, 2))
    unstable_declared = parse_box(branch["unstable_modulus"])
    inv_declared = parse_box(branch["inverse_unstable"])
    flat_denom = Box.scalar(2) - trace
    signed_flat = flat_denom.inverse()
    abs_denom = flat_denom if flat_denom.lo > 0 else Box(-flat_denom.hi, -flat_denom.lo)
    abs_flat = abs_denom.inverse()
    checks["unstable_enclosure"] = unstable.subset_of(unstable_declared)
    checks["inverse_unstable_enclosure"] = unstable.inverse().subset_of(inv_declared)
    checks["signed_flat_enclosure"] = signed_flat.subset_of(parse_box(branch["signed_flat"]))
    checks["absolute_flat_enclosure"] = abs_flat.subset_of(parse_box(branch["absolute_flat"]))
    return checks


def check_sectors(payload: dict[str, object], digits: int) -> dict[str, object]:
    branch_failures: list[str] = []
    aggregate_checks: dict[str, bool] = {}
    sectors = payload["sectors"]
    for word, sector in sectors.items():
        if len(sector["branches"]) != int(sp.trace(sp.Matrix(GRAPH) ** len(word))):
            branch_failures.append(f"{word}:branch_count")
        for branch in sector["branches"]:
            checks = verify_branch(word, branch, digits)
            for name, passed in checks.items():
                if not passed:
                    branch_failures.append(f"{word}:{branch['sign_word']}:{name}")
        for key in ("inverse_unstable", "absolute_flat", "signed_flat", "monodromy_trace"):
            reconstructed = add_boxes(parse_box(branch[key]) for branch in sector["branches"])
            declared = parse_box(sector["aggregates"][key])
            aggregate_checks[f"{word}:{key}"] = reconstructed == declared

    comparison_checks = {}
    for comparison in payload["comparisons"]:
        left = sectors[comparison["left"]]
        right = sectors[comparison["right"]]
        for key in ("inverse_unstable", "absolute_flat", "signed_flat", "monodromy_trace"):
            difference = parse_box(left["aggregates"][key]) - parse_box(right["aggregates"][key])
            comparison_checks[f"{comparison['label']}:{key}"] = difference.hi < 0 or difference.lo > 0
    return {
        "branch_failure_count": len(branch_failures),
        "branch_failures": branch_failures[:20],
        "aggregate_checks": aggregate_checks,
        "comparison_checks": comparison_checks,
        "pass": not branch_failures
        and all(aggregate_checks.values())
        and all(comparison_checks.values()),
    }


def check_finite_field(payload: dict[str, object]) -> dict[str, bool]:
    prime = 43
    parameter = {"0": 36, "1": 19}
    checks = {}
    for record in payload["records"]:
        q, p = record["fixed_point"]
        matrix = [[1, 0], [0, 1]]
        for letter in record["protocol"]:
            derivative = [[-2 * parameter[letter] * q % prime, -1 % prime], [1, 0]]
            matrix = [
                [sum(derivative[i][k] * matrix[k][j] for k in range(2)) % prime for j in range(2)]
                for i in range(2)
            ]
            q, p = (1 - parameter[letter] * q * q - p) % prime, q
        trace = (matrix[0][0] + matrix[1][1]) % prime
        det_i_minus = ((1 - matrix[0][0]) * (1 - matrix[1][1]) - matrix[0][1] * matrix[1][0]) % prime
        checks[record["protocol"]] = (
            [q, p] == record["fixed_point"]
            and matrix == record["monodromy"]
            and trace == record["trace"]
            and det_i_minus == record["determinant_I_minus_M"]
            and pow(det_i_minus, -1, prime) == record["inverse_flat_weight"]
        )
    checks["distinct"] = payload["records"][0]["trace"] != payload["records"][1]["trace"]
    return checks


def interval_trace(word: str, coordinates: Sequence[Box]) -> Box:
    monodromy = (
        (Box.scalar(1), Box.scalar(0)),
        (Box.scalar(0), Box.scalar(1)),
    )
    for letter, coordinate in zip(word, coordinates, strict=True):
        jacobian = (
            (Box.scalar(-2 * LETTER_A[letter]) * coordinate, Box.scalar(-1)),
            (Box.scalar(1), Box.scalar(0)),
        )
        monodromy = product_matrix(jacobian, monodromy)
    return monodromy[0][0] + monodromy[1][1]


def boxes_overlap(left: Box, right: Box) -> bool:
    return not (left.hi < right.lo or right.hi < left.lo)


def check_symmetry_exact(payload: dict[str, object]) -> dict[str, bool]:
    checks: dict[str, bool] = {}
    sectors = payload["sectors"]
    for control in payload["symmetry_controls"]:
        reference_word = str(control["reference"])
        kind = str(control["kind"])
        expected_word = (
            reference_word[1:] + reference_word[:1]
            if kind == "cyclic_rotation"
            else reference_word[::-1]
        )
        reference = sectors[reference_word]
        rows = {str(row["reference_sign"]): row for row in control["branch_rows"]}
        mapping_ids: list[str] = []
        branch_pass = True
        for branch in reference["branches"]:
            sign_text = str(branch["sign_word"])
            partner_sign = (
                sign_text[1:] + sign_text[:1]
                if kind == "cyclic_rotation"
                else sign_text[::-1]
            )
            mapping_ids.append(f"{sign_text}>{partner_sign}")
            row = rows.get(sign_text)
            coordinates = [parse_box(item) for item in branch["coordinate_intervals"]]
            transformed_coordinates = (
                coordinates[1:] + coordinates[:1]
                if kind == "cyclic_rotation"
                else list(reversed(coordinates))
            )
            transformed_trace = interval_trace(expected_word, transformed_coordinates)
            original_trace = parse_box(branch["monodromy_trace"])
            branch_pass = branch_pass and (
                row is not None
                and str(row["transformed_sign"]) == partner_sign
                and boxes_overlap(original_trace, transformed_trace)
            )
        digest = hashlib.sha256("\n".join(mapping_ids).encode("ascii")).hexdigest()
        checks[f"{kind}:{reference_word}"] = (
            kind in {"cyclic_rotation", "reversal"}
            and str(control["transformed"]) == expected_word
            and len(reference["branches"]) == int(control["branch_count"])
            and len(rows) == int(control["branch_count"])
            and digest == control["branch_mapping_sha256"]
            and branch_pass
        )
    checks["control_family_count"] = len(payload["symmetry_controls"]) == 8
    return checks


def check_t3(payload: dict[str, object]) -> dict[str, bool]:
    checks = {}
    for row in payload["hill_rows"]:
        n = int(row["period"])
        b = sp.symbols(f"b0:{n}")
        matrix = sp.eye(2)
        for value in b:
            matrix = sp.Matrix([[-value, -1], [1, 0]]) * matrix
        if n == 1:
            cyclic = sp.Matrix([[b[0] + 2]])
        elif n == 2:
            cyclic = sp.Matrix([[b[0], 2], [2, b[1]]])
        else:
            cyclic = sp.zeros(n)
            for i in range(n):
                cyclic[i, i] = b[i]
                cyclic[i, (i - 1) % n] += 1
                cyclic[i, (i + 1) % n] += 1
        checks[f"hill_{n}"] = sp.expand(cyclic.det() - (-1) ** (n + 1) * (2 - sp.trace(matrix))) == 0
    z = sp.symbols("z")
    extended = sp.kronecker_product(sp.ones(2, 2), sp.Matrix(GRAPH))
    checks["local_bare"] = sp.expand((sp.eye(8) - z * extended).det() - (1 - 2 * z - 8 * z**3 - 16 * z**4)) == 0
    checks["scope_guards"] = (
        payload["global_unit_numerator_residue_determinant"] == "1"
        and payload["global_unit_numerator_residue_sum"] == "0"
        and payload["global_trace_inserted_residue_sum"] == "-2^n"
        and "every repeated fixed scheme" in payload["pointwise_flat_identification"]
        and payload["naive_P2_compactification_warning"] is True
        and payload["zero_parameter_counterexample"] == "H_0^4=identity"
    )
    return checks


def main() -> None:
    args = parse_args()
    certificate = json.loads(args.input.read_text(encoding="utf-8"))
    digits = int(certificate["numerical_policy"]["sqrt_enclosure_decimal_digits"])
    t1_checks = check_t1(certificate["t1_common_survivor"])
    combinatorics_checks = check_joint_combinatorics(
        certificate["t2_joint_chronology"]["combinatorics"]
    )
    minimal_pair_checks = check_minimal_matched_pairs(
        certificate["t2_joint_chronology"]["minimal_matched_pairs"]
    )
    sector_checks = check_sectors(certificate["t2_joint_chronology"], digits)
    finite_field_checks = check_finite_field(
        certificate["t2_joint_chronology"]["finite_field_control"]
    )
    symmetry_checks = check_symmetry_exact(certificate["t2_joint_chronology"])
    t3_checks = check_t3(certificate["t3_global_collapse"])
    groups = {
        "t1_exact_checks": t1_checks,
        "joint_combinatorics_checks": combinatorics_checks,
        "minimal_pair_checks": minimal_pair_checks,
        "sector_interval_checks": sector_checks,
        "finite_field_checks": finite_field_checks,
        "symmetry_checks": symmetry_checks,
        "t3_symbolic_checks": t3_checks,
    }
    passed = (
        all(t1_checks.values())
        and all(combinatorics_checks.values())
        and all(minimal_pair_checks.values())
        and bool(sector_checks["pass"])
        and all(finite_field_checks.values())
        and all(symmetry_checks.values())
        and all(t3_checks.values())
    )
    output = {
        "material_passport": {
            "id": "HCS-C22-T1-T3-INDEPENDENT-CHECK",
            "type": "nonimporting_reproducibility_check",
            "status": "VERIFIED" if passed else "FAILED",
        },
        "run_id": "HCS_C22_T1_T3_INDEPENDENT_CHECK_V1",
        "producer_artifact": (
            str(args.input.resolve().relative_to(PROJECT_ROOT))
            if args.input.resolve().is_relative_to(PROJECT_ROOT)
            else args.input.name
        ),
        "producer_sha256": sha256_file(args.input),
        "checker_imports_producer": False,
        "groups": groups,
        "pass": passed,
    }
    if not passed:
        raise SystemExit(json.dumps(output, indent=2))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "producer_sha256": output["producer_sha256"],
                "pass": passed,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
