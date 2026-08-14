#!/usr/bin/env python3
"""Exact HCS-P49 cyclic-resultant and square-norm certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c49_certificate.json"
X = sp.symbols("X")

DEPENDENCIES = {
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
    "c48_readme": (
        TRACK / "henon_pressure_label_six_exponentials_obstruction" / "README.md",
        "5e292ff19c65d7878326c68cf937d86cbdb1bc5be1abd47e93c4e243c43fe108",
    ),
    "c48_certificate": (
        TRACK
        / "henon_pressure_label_six_exponentials_obstruction"
        / "results"
        / "c48_certificate.json",
        "7134167226aa6bd22596675bf21826b8303a2a731f087d6ad7405d7137a51234",
    ),
    "c48_code": (
        TRACK
        / "henon_pressure_label_six_exponentials_obstruction"
        / "code"
        / "c48_pressure_labels.py",
        "fd68c7af1e3dac6c555607bb29a796865069fc7d0dc7b9133ec46b8733d0a2a0",
    ),
    "c48_proof": (
        TRACK / "henon_pressure_label_six_exponentials_obstruction" / "PROOF_PACKAGE.md",
        "781b8f196b5444f480c7ccc321b23c4c0ff35db9514240ff6ea10c9d7cf3bbcd",
    ),
}

# The period-three return trace is negative.  Its actual unstable eigenvalue
# is -L3, so its polynomial is f_L3(-X), not the positive-modulus polynomial.
ORBIT_POLYNOMIALS = {
    "period_1": {
        "primitive_period": 1,
        "signed_unstable_branch": "+L1",
        "trace_sign": 1,
        "polynomial": sp.Poly(X**4 - 4 * X**3 - 22 * X**2 - 4 * X + 1, X),
    },
    "period_3": {
        "primitive_period": 3,
        "signed_unstable_branch": "-L3",
        "trace_sign": -1,
        "polynomial": sp.Poly(X**4 + 76 * X**3 - 7374 * X**2 + 76 * X + 1, X),
    },
    "period_4": {
        "primitive_period": 4,
        "signed_unstable_branch": "+L4",
        "trace_sign": 1,
        "polynomial": sp.Poly(X**2 - 578 * X + 1, X),
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def factorization(value: int) -> dict[str, int]:
    return {str(prime): int(exponent) for prime, exponent in sp.factorint(abs(value)).items()}


def dependency_locks() -> dict[str, dict[str, str]]:
    locks: dict[str, dict[str, str]] = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = sha256(path)
        if observed != expected:
            raise RuntimeError(f"dependency hash changed: {name}")
        locks[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return locks


def is_reciprocal(poly: sp.Poly) -> bool:
    coefficients = poly.all_coeffs()
    return coefficients == list(reversed(coefficients))


def resultant_abs(poly: sp.Poly, other: sp.Expr) -> int:
    return abs(int(sp.resultant(poly.as_expr(), other, X)))


def packet_rows(poly: sp.Poly, max_index: int) -> list[dict[str, Any]]:
    primitive_values: dict[int, int] = {}
    rows: list[dict[str, Any]] = []
    for index in range(1, max_index + 1):
        cyclotomic = sp.cyclotomic_poly(index, X)
        primitive = resultant_abs(poly, cyclotomic)
        cyclic = resultant_abs(poly, X**index - 1)
        primitive_values[index] = primitive
        divisor_product = 1
        for divisor in sp.divisors(index):
            divisor_product *= primitive_values[divisor]
        if divisor_product != cyclic:
            raise ArithmeticError(f"cyclotomic decomposition failed at index {index}")

        square_root, is_square = sp.integer_nthroot(primitive, 2)
        if index > 2 and not is_square:
            raise ArithmeticError(f"primitive norm is not square at index {index}")
        rows.append(
            {
                "index": index,
                "cyclic_resultant_abs": cyclic,
                "cyclic_resultant_factorization": factorization(cyclic),
                "cyclic_determinant_norm_abs": cyclic**2,
                "primitive_cyclotomic_norm_abs": primitive,
                "primitive_factorization": factorization(primitive),
                "divisor_product": divisor_product,
                "divisor_product_exact": divisor_product == cyclic,
                "square_theorem_applies": index > 2,
                "primitive_is_square": bool(is_square),
                "canonical_half_norm": int(square_root) if is_square else None,
                "half_norm_is_rational_prime": bool(sp.isprime(square_root)) if is_square else None,
            }
        )
    return rows


def symbolic_controls() -> dict[str, Any]:
    reciprocal_rows = []
    for index in range(3, 13):
        degree = int(sp.totient(index))
        phi = sp.cyclotomic_poly(index, X)
        reciprocal_residual = sp.cancel(X**degree * phi.subs(X, 1 / X) - phi)
        half = X ** (-degree // 2) * phi
        half_inversion_residual = sp.cancel(half.subs(X, 1 / X) - half)
        reciprocal_rows.append(
            {
                "index": index,
                "totient": degree,
                "totient_even": degree % 2 == 0,
                "reciprocal_residual": str(reciprocal_residual),
                "half_inversion_residual": str(half_inversion_residual),
            }
        )
        if degree % 2 or reciprocal_residual != 0 or half_inversion_residual != 0:
            raise ArithmeticError(f"symbolic inversion control failed at index {index}")

    nonreciprocal = sp.Poly(X**2 - 2 * X + 2, X)
    nonreciprocal_c3 = resultant_abs(nonreciprocal, sp.cyclotomic_poly(3, X))
    if nonreciprocal_c3 != 13 or sp.integer_nthroot(nonreciprocal_c3, 2)[1]:
        raise ArithmeticError("nonreciprocal negative control failed")
    return {
        "cyclotomic_reciprocity_rows": reciprocal_rows,
        "n_2_has_no_integer_half_exponent": True,
        "nonreciprocal_unit_hypothesis_control": {
            "polynomial": str(nonreciprocal.as_expr()),
            "primitive_norm_index_3": nonreciprocal_c3,
            "is_square": False,
        },
    }


def build_certificate(max_index: int = 12) -> dict[str, Any]:
    if max_index < 4:
        raise ValueError("max_index must be at least 4")

    orbits: dict[str, Any] = {}
    primitive_square_rows = 0
    prime_half_rows = 0
    for name, spec in ORBIT_POLYNOMIALS.items():
        poly = spec["polynomial"]
        if (
            not isinstance(poly, sp.Poly)
            or not poly.is_monic
            or not poly.is_irreducible
            or not is_reciprocal(poly)
        ):
            raise ArithmeticError(f"reciprocal monic polynomial failure: {name}")
        if int(poly.TC()) != 1:
            raise ArithmeticError(f"unit norm failure: {name}")
        rows = packet_rows(poly, max_index)
        if rows[1]["primitive_is_square"]:
            raise ArithmeticError(f"level-two sharpness control unexpectedly square: {name}")
        if rows[1]["cyclic_resultant_abs"] == rows[0]["cyclic_resultant_abs"] ** 2:
            raise ArithmeticError(f"false one-scalar repetition law passed: {name}")
        primitive_square_rows += sum(bool(row["primitive_is_square"]) for row in rows if row["index"] > 2)
        prime_half_rows += sum(bool(row["half_norm_is_rational_prime"]) for row in rows if row["index"] > 2)
        orbits[name] = {
            "primitive_period": spec["primitive_period"],
            "signed_unstable_branch": spec["signed_unstable_branch"],
            "trace_sign": spec["trace_sign"],
            "minimal_polynomial": str(poly.as_expr()),
            "degree": poly.degree(),
            "monic": bool(poly.is_monic),
            "irreducible": bool(poly.is_irreducible),
            "reciprocal": is_reciprocal(poly),
            "constant_term": int(poly.TC()),
            "rows": rows,
            "one_scalar_power_law_control": {
                "A_1": rows[0]["cyclic_resultant_abs"],
                "A_2": rows[1]["cyclic_resultant_abs"],
                "A_2_equals_A_1_squared": False,
            },
        }

    selected = {
        "period_1_index_3_prime_half": orbits["period_1"]["rows"][2]["canonical_half_norm"],
        "period_1_index_4_composite_half": orbits["period_1"]["rows"][3]["canonical_half_norm"],
        "period_3_index_3_prime_half": orbits["period_3"]["rows"][2]["canonical_half_norm"],
        "period_4_index_6_prime_half": orbits["period_4"]["rows"][5]["canonical_half_norm"],
    }
    expected_selected = {
        "period_1_index_3_prime_half": 19,
        "period_1_index_4_composite_half": 24,
        "period_3_index_3_prime_half": 7451,
        "period_4_index_6_prime_half": 577,
    }
    if selected != expected_selected:
        raise ArithmeticError("selected half-norm ledger changed")

    positive_modulus_period_3 = sp.Poly(X**4 - 76 * X**3 - 7374 * X**2 - 76 * X + 1, X)
    sign_transformed_period_3 = sp.Poly(positive_modulus_period_3.as_expr().subs(X, -X), X)
    if sign_transformed_period_3 != ORBIT_POLYNOMIALS["period_3"]["polynomial"]:
        raise ArithmeticError("period-three signed polynomial transform failed")
    positive_c3 = resultant_abs(positive_modulus_period_3, sp.cyclotomic_poly(3, X))
    signed_c3 = orbits["period_3"]["rows"][2]["primitive_cyclotomic_norm_abs"]
    if positive_c3 == signed_c3:
        raise ArithmeticError("period-three sign mutation was not detected")

    core = {
        "candidate_id": "HCS-P49",
        "obstruction_id": "HEN-O89",
        "claim_status": "PROVED",
        "scalar_route_status": "STOP_SCOPED_SQUARE_NORM",
        "ideal_packet_status": "OPEN_EXACT_STRUCTURE",
        "max_index": max_index,
        "orbits": orbits,
        "selected_half_norms": selected,
        "symbolic_controls": symbolic_controls(),
        "signed_period_3_control": {
            "actual_signed_cyclotomic_norm_index_3": signed_c3,
            "positive_modulus_mutation_index_3": positive_c3,
            "signed_polynomial_equals_positive_polynomial_at_minus_X": True,
            "mutation_detected": signed_c3 != positive_c3,
        },
        "theorem_ledger": {
            "ideal_canonical_under_inversion": True,
            "A_r_product_over_C_d": True,
            "determinant_ideal_equals_A_r_squared": True,
            "determinant_full_multiplier_field_norm_is_square": True,
            "minimal_trace_field_determinant_norm_is_forced_square": False,
            "lehmer_pierce_sequence_survives": True,
            "primitive_norm_is_square_for_index_gt_2": True,
            "primitive_norm_is_prime_for_index_gt_2": False,
            "half_norm_is_single_euler_label": False,
            "prime_ideal_packet_attachment": "OPEN",
        },
        "finite_summary": {
            "orbit_count": len(orbits),
            "primitive_row_count": len(orbits) * max_index,
            "square_theorem_row_count": len(orbits) * (max_index - 2),
            "square_theorem_rows_verified": primitive_square_rows,
            "prime_half_norm_rows": prime_half_rows,
            "level_two_nonsquare_controls": len(orbits),
            "one_scalar_power_law_rejections": len(orbits),
        },
        "claim_boundary": (
            "full multiplier-field norm-prime promotion is rejected; minimal trace-field norms "
            "and canonical principal-ideal packets survive, but no all-prime trace, continuation, "
            "functional equation, or operator is proved"
        ),
        "sources": {
            "cyclic_resultants": "Hillar, Journal of Symbolic Computation 39 (2005), 653-669",
            "cyclic_recurrences": "Hillar-Levine, arXiv:math/0411414",
            "quadratic_lehmer_pierce": "Flatters, arXiv:0708.2190",
            "primitive_ideal_divisors": "Postnikova-Schinzel, Math. USSR-Sb. 4 (1968), 153-159",
        },
    }
    return {
        **core,
        "core_sha256": canonical_sha(core),
        "dependency_locks": dependency_locks(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-index", type=int, default=12)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    certificate = build_certificate(args.max_index)
    if args.check:
        print(json.dumps({
            "check": True,
            "candidate_id": certificate["candidate_id"],
            "core_sha256": certificate["core_sha256"],
            "finite_summary": certificate["finite_summary"],
            "scalar_route_status": certificate["scalar_route_status"],
            "ideal_packet_status": certificate["ideal_packet_status"],
        }, sort_keys=True))
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
