#!/usr/bin/env python3
"""Exact certificates for the HCS-C16 quaternionic S-arithmetic clock.

The arithmetic is exact in Q(sqrt(3)).  Floating point is used only for
Archimedean logarithms and the lattice-point illustrations.  No zero or
prime data are read by this program.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


P = 13


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
    root3 = math.sqrt(3.0)
    real_unit = 2.0 * math.log(2.0 + root3)
    split_unit = math.log((4.0 + root3) / (4.0 - root3))
    return real_unit, split_unit


def element(m: int, n: int) -> Quad3:
    return (EPSILON**m) * (PI**n)


def joint_clock(m: int, n: int) -> tuple[float, int]:
    real_unit, split_unit = clock_constants()
    return m * real_unit + n * split_unit, n


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


def record_near_wall(limit: int) -> list[dict[str, object]]:
    """Primitive record approximants to the real Weyl wall."""
    real_unit, split_unit = clock_constants()
    best = math.inf
    records: list[dict[str, object]] = []
    for n in range(1, limit + 1):
        m = round(-n * split_unit / real_unit)
        if math.gcd(abs(m), n) != 1:
            continue
        signed = m * real_unit + n * split_unit
        length = abs(signed)
        if length < best:
            best = length
            unweighted_log_factor = -math.log(-math.expm1(-length))
            height = length + math.log(P) * n
            records.append(
                {
                    "m": m,
                    "n": n,
                    "real_signed": signed,
                    "real_length": length,
                    "tree_length": n,
                    "height": height,
                    "unweighted_log_local_factor_s1": unweighted_log_factor,
                    "height_weight_log10_s1": -height / math.log(10.0),
                }
            )
    return records


def primitive_box_count(real_bound: int, tree_bound: int) -> int:
    """Count primitive directions modulo +/- in a joint length rectangle."""
    real_unit, split_unit = clock_constants()
    answer = 0
    for n in range(tree_bound + 1):
        lower = math.ceil((-real_bound - split_unit * n) / real_unit - 1e-12)
        upper = math.floor((real_bound - split_unit * n) / real_unit + 1e-12)
        for m in range(lower, upper + 1):
            if canonical_primitive(m, n):
                answer += 1
    return answer


def box_count_rows(bounds: Iterable[int]) -> list[dict[str, object]]:
    real_unit, _ = clock_constants()
    rows = []
    for bound in bounds:
        observed = primitive_box_count(bound, bound)
        predicted = 12.0 * bound * bound / (math.pi**2 * real_unit)
        rows.append(
            {
                "real_bound": bound,
                "tree_bound": bound,
                "count_mod_inverse": observed,
                "primitive_lattice_prediction": predicted,
                "observed_over_prediction": observed / predicted,
            }
        )
    return rows


def primitive_height_count(height_bound: int) -> int:
    """Count primitive directions for H=ell_infinity+log(13)*ell_13."""
    real_unit, split_unit = clock_constants()
    log_p = math.log(P)
    answer = 0
    for n in range(math.floor(height_bound / log_p) + 1):
        remaining = height_bound - log_p * n
        lower = math.ceil((-remaining - split_unit * n) / real_unit - 1e-12)
        upper = math.floor((remaining - split_unit * n) / real_unit + 1e-12)
        for m in range(lower, upper + 1):
            if canonical_primitive(m, n):
                answer += 1
    return answer


def height_count_rows(bounds: Iterable[int]) -> list[dict[str, object]]:
    real_unit, _ = clock_constants()
    rows = []
    for bound in bounds:
        observed = primitive_height_count(bound)
        predicted = 6.0 * bound * bound / (math.pi**2 * real_unit * math.log(P))
        rows.append(
            {
                "height_bound": bound,
                "count_mod_inverse": observed,
                "primitive_height_prediction": predicted,
                "observed_over_prediction": observed / predicted,
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError("cannot write an empty table")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
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
            "floating_point_scope": "real logarithms and illustrative counts only",
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
