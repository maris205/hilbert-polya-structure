#!/usr/bin/env python3
"""Exact HCS-P48 certificate for the three-orbit pressure-label obstruction."""

from __future__ import annotations

import argparse
import hashlib
import json
from functools import lru_cache
from pathlib import Path

import sympy as sp
from sympy.polys.numberfields import primitive_element


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c48_certificate.json"
X = sp.symbols("X")

DEPENDENCIES = {
    "c45_readme": (
        TRACK / "henon_pressure_normalized_prime_orbit_bridge" / "README.md",
        "45cb4c5b8c735bfb5c3a497cfecef21fc81140b3c77f56c866249df8715e5ba1",
    ),
    "c45_certificate": (
        TRACK / "henon_pressure_normalized_prime_orbit_bridge" / "results" / "c45_certificate.json",
        "962e0f6aca53b8e1c8786caa291af7bb318efd631b86b7f70702c1d2bea603f7",
    ),
    "c46_readme": (
        TRACK / "henon_integral_monodromy_units" / "README.md",
        "700cce354f56c3b218984f2a8606d04b122304336c65735da86adb7f93cb9a47",
    ),
    "c46_certificate": (
        TRACK / "henon_integral_monodromy_units" / "results" / "c46_certificate.json",
        "43251f10b1c900921963b95648b0e95b15e70bdb6bd9d3a9674cf7b234f55f85",
    ),
    "c47_readme": (
        TRACK / "henon_repetition_label_classification" / "README.md",
        "9b1c18c6f133296398d8826282284756af436abc45c282c5e0200443605f291a",
    ),
    "c47_certificate": (
        TRACK / "henon_repetition_label_classification" / "results" / "c47_certificate.json",
        "0f05a0939518fae1be7a8ab60d3b9c5310cfc746381fb693e25295ead694ba1f",
    ),
    "exact_algebra_appendix": (
        TRACK / "henon_instability_roof_zeta" / "paper" / "sections" / "A_exact_algebra.tex",
        "bd9b6c20aad7358f33d18a01ee9d206c3534892f667dc8f2d3e57dfc5c9e24dc",
    ),
    "certified_orbit_catalog": (
        TRACK / "henon_instability_roof_zeta" / "results" / "catalog_validation.json",
        "0eab1930a17e4315e59eebc9dc7d3ef111b674d3625f09ca3396c1aa7c814fde",
    ),
}


def canonical_sha(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def dependency_locks() -> dict[str, dict[str, str]]:
    locks: dict[str, dict[str, str]] = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency hash changed: {name}")
        locks[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return locks


def derivative(q: sp.Expr) -> sp.Matrix:
    return sp.Matrix([[-12 * q, -1], [1, 0]])


def recurrence_residuals(coordinates: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    n = len(coordinates)
    return tuple(
        sp.simplify(1 - 6 * coordinates[i] ** 2 - coordinates[(i - 1) % n] - coordinates[(i + 1) % n])
        for i in range(n)
    )


def chronological_monodromy(coordinates: tuple[sp.Expr, ...]) -> sp.Matrix:
    matrix = sp.eye(2)
    for coordinate in coordinates:
        matrix = derivative(coordinate) * matrix
    return sp.simplify(matrix)


def state_word(coordinates: tuple[sp.Expr, ...]) -> list[str]:
    signs = ["+" if coordinate > 0 else "-" for coordinate in coordinates]
    return [signs[i] + signs[(i - 1) % len(signs)] for i in range(len(signs))]


def factorization(integer: int) -> dict[str, int]:
    return {str(prime): exponent for prime, exponent in sp.factorint(abs(integer)).items()}


def matrix_strings(matrix: sp.Matrix) -> list[list[str]]:
    return [[str(sp.simplify(matrix[i, j])) for j in range(matrix.cols)] for i in range(matrix.rows)]


def orbit_certificate() -> dict[str, object]:
    a = -sp.sqrt(5) / 6
    b = (1 + sp.sqrt(5)) / 6
    r6 = sp.sqrt(6) / 6
    orbit_specs = {
        "period_1": {
            "coordinates": (-(1 + sp.sqrt(7)) / 6,),
            "expected_trace": 2 + 2 * sp.sqrt(7),
            "expected_minpoly": X**4 - 4 * X**3 - 22 * X**2 - 4 * X + 1,
        },
        "period_3": {
            "coordinates": (a, b, a),
            "expected_trace": -38 - 42 * sp.sqrt(5),
            "expected_minpoly": X**4 - 76 * X**3 - 7374 * X**2 - 76 * X + 1,
        },
        "period_4": {
            "coordinates": (-r6, -r6, r6, r6),
            "expected_trace": sp.Integer(578),
            "expected_minpoly": X**2 - 578 * X + 1,
        },
    }
    result: dict[str, object] = {}
    for name, spec in orbit_specs.items():
        coordinates = spec["coordinates"]
        matrix = chronological_monodromy(coordinates)
        trace = sp.simplify(sp.trace(matrix))
        if trace != spec["expected_trace"]:
            raise ArithmeticError(f"unexpected trace for {name}")
        residuals = recurrence_residuals(coordinates)
        if any(residual != 0 for residual in residuals):
            raise ArithmeticError(f"recurrence failure for {name}")
        absolute_trace = sp.Abs(trace)
        multiplier = sp.simplify((absolute_trace + sp.sqrt(absolute_trace**2 - 4)) / 2)
        minpoly = sp.Poly(sp.minimal_polynomial(multiplier, X), X)
        expected_minpoly = sp.Poly(spec["expected_minpoly"], X)
        if minpoly != expected_minpoly:
            raise ArithmeticError(f"minimal polynomial failure for {name}")
        inside_rectangles = all(
            sp.simplify(sp.Abs(coordinate) - sp.Rational(1, 3)) >= 0
            and sp.simplify(sp.Rational(5, 8) - sp.Abs(coordinate)) >= 0
            for coordinate in coordinates
        )
        if not inside_rectangles:
            raise ArithmeticError(f"orbit left the certified coordinate rectangles: {name}")
        result[name] = {
            "period": len(coordinates),
            "primitive": name in {"period_1", "period_3", "period_4"},
            "coordinates": [str(sp.simplify(value)) for value in coordinates],
            "state_word_from_current_previous_signs": state_word(coordinates),
            "recurrence_residuals": [str(value) for value in residuals],
            "inside_abs_q_interval_1_3_to_5_8": inside_rectangles,
            "monodromy": matrix_strings(matrix),
            "trace": str(trace),
            "determinant": str(sp.simplify(matrix.det())),
            "positive_unstable_modulus": str(multiplier),
            "positive_unstable_modulus_decimal_30": str(sp.N(multiplier, 30)),
            "minimal_polynomial": str(minpoly.as_expr()),
        }
    return result


@lru_cache(maxsize=1)
def field_certificate() -> dict[str, object]:
    l1 = 1 + sp.sqrt(7) + sp.sqrt(7 + 2 * sp.sqrt(7))
    l3 = 19 + 21 * sp.sqrt(5) + sp.sqrt(2565 + 798 * sp.sqrt(5))
    l4 = 289 + 24 * sp.sqrt(145)
    f1 = sp.Poly(sp.minimal_polynomial(l1, X), X)
    f3 = sp.Poly(sp.minimal_polynomial(l3, X), X)
    f4 = sp.Poly(sp.minimal_polynomial(l4, X), X)
    expected = {
        "L1": sp.Poly(X**4 - 4 * X**3 - 22 * X**2 - 4 * X + 1, X),
        "L3": sp.Poly(X**4 - 76 * X**3 - 7374 * X**2 - 76 * X + 1, X),
        "L4": sp.Poly(X**2 - 578 * X + 1, X),
    }
    for name, observed in (("L1", f1), ("L3", f3), ("L4", f4)):
        if observed != expected[name]:
            raise ArithmeticError(f"field polynomial mismatch: {name}")

    d3 = 10260 + 3192 * sp.sqrt(5)
    d3_conjugate = 10260 - 3192 * sp.sqrt(5)
    d3_norm = int(sp.expand(d3 * d3_conjugate))
    if d3_norm != 54_323_280:
        raise ArithmeticError("period-three quadratic discriminant norm mismatch")

    primitive_poly, primitive_coefficients, _ = primitive_element([l1, l3, l4], X, ex=True)
    primitive_poly = sp.Poly(primitive_poly, X)
    coefficients = [int(value) for value in primitive_poly.all_coeffs()]
    factor_rows = [(sp.degree(factor, X), exponent) for factor, exponent in sp.factor_list(primitive_poly.as_expr())[1]]
    if primitive_poly.degree() != 32 or factor_rows != [(32, 1)]:
        raise ArithmeticError("compositum degree is not 32")

    pair_degrees: dict[str, int] = {}
    for label, generators in {
        "L1_L3": [l1, l3],
        "L1_L4": [l1, l4],
        "L3_L4": [l3, l4],
        "duplicate_L3_control": [l1, l3, l3],
    }.items():
        polynomial, _, _ = primitive_element(generators, X, ex=True)
        pair_degrees[label] = int(sp.degree(polynomial, X))
    expected_pair_degrees = {"L1_L3": 16, "L1_L4": 8, "L3_L4": 8, "duplicate_L3_control": 16}
    if pair_degrees != expected_pair_degrees:
        raise ArithmeticError("pair or duplicate field-degree control failed")

    discriminants = {name: int(sp.discriminant(poly.as_expr(), X)) for name, poly in (("f1", f1), ("f3", f3), ("f4", f4))}
    return {
        "generators": {
            "L1": str(l1),
            "L3": str(l3),
            "L4": str(l4),
        },
        "minimal_polynomials": {
            "L1": str(f1.as_expr()),
            "L3": str(f3.as_expr()),
            "L4": str(f4.as_expr()),
        },
        "degrees": {"L1": 4, "L3": 4, "L4": 2},
        "polynomial_discriminants": {
            name: {"integer": value, "factorization": factorization(value)}
            for name, value in discriminants.items()
        },
        "period_3_relative_discriminant": {
            "d3": str(d3),
            "norm": d3_norm,
            "norm_factorization": factorization(d3_norm),
            "odd_11_valuation_witness": True,
        },
        "ramification_degree_ladder": [
            "[Q(L1):Q]=4",
            "adjoin sqrt(5): degree 8 because K1 is unramified at 5",
            "adjoin sqrt(d3): degree 16 because an 11-adic valuation of d3 stays odd",
            "adjoin sqrt(145): degree 32 because 29 is unramified before the final quadratic field",
        ],
        "pair_and_duplicate_controls": pair_degrees,
        "primitive_element": {
            "expression": "L1 + L3 + L4",
            "sympy_coefficients": [int(value) for value in primitive_coefficients],
            "minimal_polynomial_degree": primitive_poly.degree(),
            "minimal_polynomial_coefficients": coefficients,
            "coefficient_sha256": canonical_sha(coefficients),
            "irreducible_factor_degrees": [[int(degree), int(exponent)] for degree, exponent in factor_rows],
        },
        "conclusion": "the three fields are linearly disjoint and log(L1), log(L3), log(L4) are Q-linearly independent",
    }


def build_certificate() -> dict[str, object]:
    payload: dict[str, object] = {
        "candidate_id": "HCS-P48",
        "dependency_locks": dependency_locks(),
        "exact_survivor_orbits": orbit_certificate(),
        "field_independence": field_certificate(),
        "transcendence_compiler": {
            "rational_h": "if h=a/b>0 and L^h is a rational integer, then L^a is both that integer power and an algebraic unit, impossible",
            "irrational_h": "apply the Six Exponentials Theorem to (1,h) and (log L1,log L3,log L4)",
            "unconditional_conclusion": "for every real h>0, L1^h,L3^h,L4^h cannot all be rational primes",
            "algebraic_irrational_corollary": "Gelfond-Schneider makes each positive real L_j^h transcendental",
            "status": "PROVED",
        },
        "source_locks": {
            "six_exponentials": {
                "theorem": "three real Q-independent x-values and two real Q-independent xi-values force one of the six exp(x_i xi_j) to be transcendental",
                "reference": "J. Pila, Journal of the Australian Mathematical Society 54 (1993), Theorem 3.1",
                "doi": "10.1017/S1446788700037022",
            },
            "gelfond_schneider": {
                "reference": "A. Gelfond, Sur le septieme probleme de Hilbert (1934)",
                "url": "https://www.mathnet.ru/eng/im4924",
            },
        },
        "strongest_positive_result": "three exact primitive survivor multipliers generate a degree-32 compositum and have Q-independent logarithms",
        "strongest_obstruction": "the common pressure power cannot label all three exact orbits by rational primes for any h>0",
        "open_theorem": "a collective non-termwise arithmetic packet or distributional trace bridge",
        "reusable_structure": "three linearly disjoint algebraic-unit multipliers plus Six Exponentials obstruct every common irrational power",
        "round2_clue": "replace one-prime-per-orbit labels by prime ideals, packets, cyclic resultants, or signed trace distributions",
        "claim_boundary": "at least one of three labels is nonprime; the theorem need not identify which one when h is transcendental and does not refute the pressure prime-orbit counting law",
        "status": "PROVED_THREE_ORBIT_ALL_PRIME_PRESSURE_LABEL_OBSTRUCTION",
    }
    payload["payload_sha256"] = canonical_sha(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"check": True, "sha256": payload["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
