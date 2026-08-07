#!/usr/bin/env python3
"""Exact certificates for the HCS-C16 quaternionic S-arithmetic clock.

The arithmetic is exact in Q(sqrt(3)).  Archimedean logarithms and all
boundary decisions use high-precision Decimal arithmetic; binary floats are
used only when serializing compact diagnostics.  No zero or prime data are
read by this program.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable, TypeVar


P = 13
DECIMAL_PRECISION = 80
T = TypeVar("T")


def at_decimal_precision(function: Callable[..., T]) -> Callable[..., T]:
    """Run a numeric helper under the producer's private Decimal context."""
    def wrapped(*args: object, **kwargs: object) -> T:
        with localcontext() as context:
            context.prec = DECIMAL_PRECISION
            return function(*args, **kwargs)

    return wrapped


def decimal_pi(precision: int = DECIMAL_PRECISION) -> Decimal:
    """Compute pi with Gauss--Legendre iteration at the requested precision."""
    with localcontext() as context:
        context.prec = precision + 12
        one = Decimal(1)
        a = one
        b = one / Decimal(2).sqrt()
        t = Decimal(1) / 4
        multiplier = one
        for _ in range(max(6, math.ceil(math.log2(precision)) + 1)):
            next_a = (a + b) / 2
            b = (a * b).sqrt()
            t -= multiplier * (a - next_a) ** 2
            a = next_a
            multiplier *= 2
        value = (a + b) ** 2 / (4 * t)
        context.prec = precision
        return +value


def decimal_clock_constants(
    precision: int = DECIMAL_PRECISION,
) -> tuple[Decimal, Decimal, Decimal]:
    """Return A, C, and log(13) using deterministic Decimal arithmetic."""
    with localcontext() as context:
        context.prec = precision
        root3 = Decimal(3).sqrt()
        real_unit = Decimal(2) * (Decimal(2) + root3).ln()
        split_unit = ((Decimal(4) + root3) / (Decimal(4) - root3)).ln()
        log_p = Decimal(P).ln()
        return +real_unit, +split_unit, +log_p


def decimal_ceil(value: Decimal) -> int:
    return int(value.to_integral_value(rounding=ROUND_CEILING))


def decimal_floor(value: Decimal) -> int:
    return int(value.to_integral_value(rounding=ROUND_FLOOR))


def qstr(value: Fraction) -> str:
    """Return a stable string for a rational number."""
    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def valuation(value: Fraction, prime: int) -> int:
    """The additive prime-adic valuation of a nonzero rational."""
    value = Fraction(value)
    if value == 0:
        raise ValueError("valuation(0) is infinite")
    numerator = abs(value.numerator)
    denominator = value.denominator
    answer = 0
    while numerator % prime == 0:
        numerator //= prime
        answer += 1
    while denominator % prime == 0:
        denominator //= prime
        answer -= 1
    return answer


def legendre_symbol(value: int, prime: int) -> int:
    value %= prime
    if value == 0:
        return 0
    residue = pow(value, (prime - 1) // 2, prime)
    return -1 if residue == prime - 1 else residue


def hilbert_symbol_odd(a: int, b: int, prime: int) -> int:
    """Hilbert symbol (a,b)_p for an odd prime and nonzero integers."""
    alpha = valuation(Fraction(a), prime)
    beta = valuation(Fraction(b), prime)
    u = a // (prime**alpha)
    v = b // (prime**beta)
    sign = -1 if (alpha * beta * ((prime - 1) // 2)) % 2 else 1
    if beta % 2:
        sign *= legendre_symbol(u, prime)
    if alpha % 2:
        sign *= legendre_symbol(v, prime)
    return sign


def hilbert_symbol_two(a: int, b: int) -> int:
    """Hilbert symbol (a,b)_2 for nonzero odd integers a,b."""
    if a % 2 == 0 or b % 2 == 0:
        raise ValueError("this certificate only needs odd a and b")
    exponent = ((a - 1) // 2) * ((b - 1) // 2)
    return -1 if exponent % 2 else 1


@dataclass(frozen=True)
class Quad3:
    """An exact element a+b*sqrt(3)."""

    a: Fraction
    b: Fraction

    def __init__(self, a: int | Fraction, b: int | Fraction = 0):
        object.__setattr__(self, "a", Fraction(a))
        object.__setattr__(self, "b", Fraction(b))

    def __mul__(self, other: "Quad3") -> "Quad3":
        return Quad3(
            self.a * other.a + 3 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    def conjugate(self) -> "Quad3":
        return Quad3(self.a, -self.b)

    def norm(self) -> Fraction:
        return self.a * self.a - 3 * self.b * self.b

    def inverse(self) -> "Quad3":
        norm = self.norm()
        if norm == 0:
            raise ZeroDivisionError
        conjugate = self.conjugate()
        return Quad3(conjugate.a / norm, conjugate.b / norm)

    def __pow__(self, exponent: int) -> "Quad3":
        if exponent < 0:
            return self.inverse() ** (-exponent)
        answer = Quad3(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                answer = answer * base
            base = base * base
            power //= 2
        return answer

    def trace(self) -> Fraction:
        return 2 * self.a

    def discriminant(self) -> Fraction:
        return self.trace() ** 2 - 4 * self.norm()

    def matrix(self) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
        return ((self.a, 3 * self.b), (self.b, self.a))

    def as_dict(self) -> dict[str, str]:
        return {"a": qstr(self.a), "b": qstr(self.b)}


EPSILON = Quad3(2, 1)
PI = Quad3(4, 1)


def clock_constants() -> tuple[float, float]:
    real_unit, split_unit, _ = decimal_clock_constants()
    return float(real_unit), float(split_unit)


def element(m: int, n: int) -> Quad3:
    return (EPSILON**m) * (PI**n)


def joint_clock(m: int, n: int) -> tuple[float, int]:
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        real_unit, split_unit, _ = decimal_clock_constants()
        signed = Decimal(m) * real_unit + Decimal(n) * split_unit
        return float(signed), n


def element_certificate(m: int, n: int) -> dict[str, object]:
    alpha = element(m, n)
    norm = alpha.norm()
    discriminant = alpha.discriminant()
    signed_real, signed_tree = joint_clock(m, n)
    predicted_norm = Fraction(P) ** n
    tree_from_invariants = max(
        0, valuation(norm, P) - valuation(discriminant, P)
    )
    matrix = alpha.matrix()
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return {
        "m": m,
        "n": n,
        "element": alpha.as_dict(),
        "matrix": [[qstr(entry) for entry in row] for row in matrix],
        "trace": qstr(alpha.trace()),
        "norm": qstr(norm),
        "predicted_norm": qstr(predicted_norm),
        "discriminant": qstr(discriminant),
        "v13_norm": valuation(norm, P),
        "v13_discriminant": valuation(discriminant, P),
        "real_signed": signed_real,
        "real_length": abs(signed_real),
        "tree_signed": signed_tree,
        "tree_length": abs(signed_tree),
        "tree_length_from_trace_norm": tree_from_invariants,
        "primitive": math.gcd(abs(m), abs(n)) == 1,
        "matrix_determinant_matches_norm": determinant == norm,
        "norm_matches_13_power": norm == predicted_norm,
    }


def canonical_primitive(m: int, n: int) -> bool:
    """One representative of (m,n) modulo the Weyl involution +/-1."""
    if m == 0 and n == 0:
        return False
    if math.gcd(abs(m), abs(n)) != 1:
        return False
    return n > 0 or (n == 0 and m > 0)


@at_decimal_precision
def record_near_wall(limit: int) -> list[dict[str, object]]:
    """Primitive record approximants to the real Weyl wall."""
    if limit < 1:
        raise ValueError("near-wall limit must be positive")
    real_unit, split_unit, log_p = decimal_clock_constants()
    best = Decimal("Infinity")
    records: list[dict[str, object]] = []
    for n in range(1, limit + 1):
        m = int(
            (-Decimal(n) * split_unit / real_unit).to_integral_value(
                rounding=ROUND_HALF_EVEN
            )
        )
        if math.gcd(abs(m), n) != 1:
            continue
        signed = Decimal(m) * real_unit + Decimal(n) * split_unit
        length = abs(signed)
        if length < best:
            best = length
            unweighted_log_factor = -(Decimal(1) - (-length).exp()).ln()
            height = length + log_p * n
            records.append(
                {
                    "m": m,
                    "n": n,
                    "real_signed": float(signed),
                    "real_length": float(length),
                    "tree_length": n,
                    "height": float(height),
                    "unweighted_log_local_factor_s1": float(unweighted_log_factor),
                    "height_weight_log10_s1": float(-height / Decimal(10).ln()),
                }
            )
    return records


@at_decimal_precision
def primitive_box_count_details(
    real_bound: int, tree_bound: int
) -> tuple[int, Decimal]:
    """Count a box and return a conservative Decimal cutoff margin."""
    if real_bound < 0 or tree_bound < 0:
        raise ValueError("box bounds must be nonnegative")
    real_unit, split_unit, _ = decimal_clock_constants()
    bound = Decimal(real_bound)
    answer = 0
    minimum_gap = Decimal("Infinity")
    for n in range(tree_bound + 1):
        shift = split_unit * n
        lower_value = (-bound - shift) / real_unit
        upper_value = (bound - shift) / real_unit
        lower = decimal_ceil(lower_value)
        upper = decimal_floor(upper_value)
        for m in range(lower, upper + 1):
            if canonical_primitive(m, n):
                answer += 1
        # Include nonprimitive lattice points to make the reported separation
        # a conservative lower bound for every counted primitive direction.
        candidates = set(range(lower - 2, lower + 3)) | set(
            range(upper - 2, upper + 3)
        )
        for m in candidates:
            if m == 0 and n == 0:
                continue
            gap = abs(abs(Decimal(m) * real_unit + shift) - bound)
            minimum_gap = min(minimum_gap, gap)
    return answer, minimum_gap


def primitive_box_count(real_bound: int, tree_bound: int) -> int:
    """Count primitive directions modulo +/- in a joint length rectangle."""
    return primitive_box_count_details(real_bound, tree_bound)[0]


@at_decimal_precision
def box_count_rows(bounds: Iterable[int]) -> list[dict[str, object]]:
    real_unit, _, _ = decimal_clock_constants()
    pi = decimal_pi()
    rows = []
    for bound in bounds:
        observed, minimum_gap = primitive_box_count_details(bound, bound)
        predicted = Decimal(12) * bound * bound / (pi**2 * real_unit)
        rows.append(
            {
                "real_bound": bound,
                "tree_bound": bound,
                "count_mod_inverse": observed,
                "primitive_lattice_prediction": float(predicted),
                "observed_over_prediction": float(Decimal(observed) / predicted),
                "minimum_boundary_gap": float(minimum_gap),
                "decimal_precision_digits": DECIMAL_PRECISION,
            }
        )
    return rows


@at_decimal_precision
def primitive_height_count_details(height_bound: int) -> tuple[int, Decimal]:
    """Count a height ball and return a conservative Decimal cutoff margin."""
    if height_bound < 0:
        raise ValueError("height bound must be nonnegative")
    real_unit, split_unit, log_p = decimal_clock_constants()
    bound = Decimal(height_bound)
    answer = 0
    minimum_gap = Decimal("Infinity")
    max_n = decimal_floor(bound / log_p)
    for n in range(max_n + 1):
        remaining = bound - log_p * n
        shift = split_unit * n
        lower = decimal_ceil((-remaining - shift) / real_unit)
        upper = decimal_floor((remaining - shift) / real_unit)
        for m in range(lower, upper + 1):
            if canonical_primitive(m, n):
                answer += 1
        candidates = set(range(lower - 2, lower + 3)) | set(
            range(upper - 2, upper + 3)
        )
        for m in candidates:
            if m == 0 and n == 0:
                continue
            value = abs(Decimal(m) * real_unit + shift) + log_p * n
            minimum_gap = min(minimum_gap, abs(value - bound))
    return answer, minimum_gap


def primitive_height_count(height_bound: int) -> int:
    """Count primitive directions for H=ell_infinity+log(13)*ell_13."""
    return primitive_height_count_details(height_bound)[0]


@at_decimal_precision
def height_count_rows(bounds: Iterable[int]) -> list[dict[str, object]]:
    real_unit, _, log_p = decimal_clock_constants()
    pi = decimal_pi()
    rows = []
    for bound in bounds:
        observed, minimum_gap = primitive_height_count_details(bound)
        predicted = Decimal(6) * bound * bound / (pi**2 * real_unit * log_p)
        rows.append(
            {
                "height_bound": bound,
                "count_mod_inverse": observed,
                "primitive_height_prediction": float(predicted),
                "observed_over_prediction": float(Decimal(observed) / predicted),
                "minimum_boundary_gap": float(minimum_gap),
                "decimal_precision_digits": DECIMAL_PRECISION,
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError("cannot write an empty table")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def produce(output: Path, near_wall_limit: int) -> None:
    output.mkdir(parents=True, exist_ok=True)
    real_unit, split_unit = clock_constants()
    near_wall = record_near_wall(near_wall_limit)
    boxes = box_count_rows([10, 20, 40, 80, 160, 320])
    heights = height_count_rows([10, 20, 40, 80, 160, 320, 640])
    samples = [
        element_certificate(1, 0),
        element_certificate(0, 1),
        element_certificate(1, 1),
        element_certificate(1, -1),
        element_certificate(-1, 2),
        element_certificate(-6, 17),
    ]

    certificate = {
        "candidate_id": "HCS-C16",
        "arithmetic_model": {
            "quaternion_algebra": "(-1,3)_Q",
            "order": "Z[1,i,j,ij]",
            "localized_prime": P,
            "hilbert_symbols": {
                "at_2": hilbert_symbol_two(-1, 3),
                "at_3": hilbert_symbol_odd(-1, 3, 3),
                "at_13": hilbert_symbol_odd(-1, 3, 13),
                "at_infinity": 1,
            },
            "ramified_finite_places": [2, 3],
            "sqrt3_roots_mod_13": [4, 9],
        },
        "generators": {
            "epsilon": {
                **EPSILON.as_dict(),
                "norm": qstr(EPSILON.norm()),
                "signed_clock": [real_unit, 0],
            },
            "pi": {
                **PI.as_dict(),
                "norm": qstr(PI.norm()),
                "signed_clock": [split_unit, 1],
            },
        },
        "joint_clock": {
            "A": real_unit,
            "C": split_unit,
            "formula": "(m,n) -> (m*A+n*C,n)",
            "basis_determinant": real_unit,
            "rank": 2,
            "height_formula": "H=abs(m*A+n*C)+log(13)*abs(n)=2*h(r)",
        },
        "sample_elements": samples,
        "near_wall_records": near_wall,
        "primitive_box_counts": boxes,
        "primitive_height_counts": heights,
        "data_boundary": {
            "prime_table_used": False,
            "zero_table_used": False,
            "fitted_parameters": [],
            "floating_point_scope": "serialization of Decimal logarithms and count diagnostics only",
            "decimal_precision_digits": DECIMAL_PRECISION,
            "boundary_method": "Decimal comparisons without epsilon; positive cutoff margins recorded",
            "near_wall_limit": near_wall_limit,
        },
    }

    json_path = output / "exact_certificates.json"
    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(certificate, handle, indent=2, sort_keys=True)
        handle.write("\n")
    write_csv(output / "near_wall.csv", near_wall)
    write_csv(output / "primitive_box_counts.csv", boxes)
    write_csv(output / "primitive_height_counts.csv", heights)

    artifacts = [
        json_path,
        output / "near_wall.csv",
        output / "primitive_box_counts.csv",
        output / "primitive_height_counts.csv",
    ]
    hashes = {path.name: sha256(path) for path in artifacts}
    with (output / "artifact_hashes.json").open("w", encoding="utf-8") as handle:
        json.dump(hashes, handle, indent=2, sort_keys=True)
        handle.write("\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("results"))
    parser.add_argument("--near-wall-limit", type=int, default=1000)
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    produce(arguments.output, arguments.near_wall_limit)
