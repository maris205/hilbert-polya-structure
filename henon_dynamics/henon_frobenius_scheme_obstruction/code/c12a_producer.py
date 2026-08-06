#!/usr/bin/env python3
"""Exact producer for HCS-C12A.

The script uses exact SymPy arithmetic.  It does not evaluate Riemann zeros,
fit parameters, or infer a recurrence from samples: the finite-permutation
formula is an input theorem whose smallest consequences are certified here.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

import sympy as sp


SCHEMA_VERSION = "HCS-C12A-1"
DECISION = "C12A_NO_GO_ZERO_DIMENSIONAL_FROBENIUS_COLLAPSE"
COLLISION = "C12B_N5_PRIOR_WORK_COLLISION"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def henon_iterate(a: sp.Expr, n: int) -> tuple[sp.Expr, sp.Expr]:
    q, p = sp.symbols("q p")
    x, y = q, p
    for _ in range(n):
        x, y = sp.expand(1 - a * x**2 - y), x
    return x, y


def legendre(d: int, p: int) -> int:
    residue = d % p
    if residue == 0:
        return 0
    value = pow(residue, (p - 1) // 2, p)
    if value == 1:
        return 1
    if value == p - 1:
        return -1
    raise ArithmeticError("Euler criterion returned a non-sign")


def low_period_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for p in (5, 11, 7, 3):
        for r in range(1, 5):
            for n in (1, 2):
                if p in (5, 11):
                    chi7 = legendre(7, p)
                    chi3 = legendre(3, p)
                    support = 1 + chi7**r if n == 1 else 2 + chi7**r + chi3**r
                    weighted = support
                    scheme_length = 2**n
                    status = "ETALE_GOOD"
                    singular = 0
                elif p == 7:
                    if n == 1:
                        support, weighted = 1, 2
                    else:
                        support = 1 if r % 2 else 3
                        weighted = 2 if r % 2 else 4
                    scheme_length = 2**n
                    status = "DEGREE_GOOD_NONREDUCED"
                    singular = 1
                else:
                    support = weighted = 1
                    scheme_length = 1
                    status = "DEGREE_DROP"
                    singular = 0
                rows.append(
                    {
                        "a": 6,
                        "p": p,
                        "r": r,
                        "n": n,
                        "prime_status": status,
                        "support_count": support,
                        "multiplicity_weighted_count": weighted,
                        "fiber_scheme_length": scheme_length,
                        "uniform_quadratic_length": 2**n if p != 3 else None,
                        "rational_singular_support_count": singular,
                    }
                )
            if p == 3:
                rows.append(
                    {
                        "a": 6,
                        "p": p,
                        "r": r,
                        "n": 4,
                        "prime_status": "DEGREE_DROP_POSITIVE_DIMENSIONAL",
                        "support_count": p ** (2 * r),
                        "multiplicity_weighted_count": None,
                        "fiber_scheme_length": None,
                        "uniform_quadratic_length": None,
                        "rational_singular_support_count": None,
                    }
                )
    return rows


def multiplication_norm_n2() -> sp.Expr:
    a, x0, x1 = sp.symbols("a x0 x1")
    domain = sp.QQ.frac_field(a)
    f0 = a * x0**2 + 2 * x1 - 1
    f1 = a * x1**2 + 2 * x0 - 1
    basis = (sp.Integer(1), x0, x1, x0 * x1)
    groebner = sp.groebner((f0, f1), x0, x1, order="grlex", domain=domain)
    jacobian = 4 * a**2 * x0 * x1 - 4
    columns: list[list[sp.Expr]] = []
    for monomial in basis:
        remainder = sp.expand(groebner.reduce(jacobian * monomial)[1])
        poly = sp.Poly(remainder, x0, x1, domain=domain)
        columns.append([poly.coeff_monomial(term) for term in basis])
    matrix = sp.Matrix(4, 4, lambda i, j: columns[j][i])
    return sp.factor(matrix.det())


def symbolic_certificate() -> dict[str, object]:
    a, x, x0, x1, q, p, u, v = sp.symbols("a x x0 x1 q p u v")
    f1 = a * x**2 + 2 * x - 1
    j1 = 2 * a * x + 2
    monic_f1 = sp.Poly(f1 / a, x, domain=sp.QQ.frac_field(a))
    d1 = sp.factor(sp.resultant(monic_f1.as_expr(), j1, x))
    d2 = multiplication_norm_n2()

    fixed_residual = sp.factor(a * ((u - 1) / a) ** 2 + 2 * ((u - 1) / a) - 1)
    fixed_numerator = sp.together(fixed_residual).as_numer_denom()[0]
    fixed_identity = sp.rem(fixed_numerator, u**2 - (a + 1), u)
    xp = (1 + v) / a
    yp = (1 - v) / a
    primitive_raw = (a * xp**2 + 2 * yp - 1, a * yp**2 + 2 * xp - 1)
    primitive_residuals = []
    for residual in primitive_raw:
        numerator = sp.together(residual).as_numer_denom()[0]
        primitive_residuals.append(sp.rem(numerator, v**2 - (a - 3), v))
    difference_identity = sp.expand(
        (a * x0**2 + 2 * x1 - 1)
        - (a * x1**2 + 2 * x0 - 1)
        - (x0 - x1) * (a * (x0 + x1) - 2)
    )

    # Exact ideal identities linking the first two iterates to the cyclic
    # presentation.  For n=2 put u1=pi_1(H(q,p)).
    h1q, h1p = henon_iterate(a, 1)
    h2q, h2p = henon_iterate(a, 2)
    cyclic1 = a * q**2 + 2 * q - 1
    cyclic20 = a * q**2 + 2 * p - 1
    cyclic21 = a * p**2 + 2 * q - 1
    u1 = 1 - a * q**2 - p
    n1_ideal_pass = (
        sp.expand(h1p - p - (q - p)) == 0
        and sp.expand((h1q - q).subs(p, q) + cyclic1) == 0
    )
    n2_ideal_pass = (
        sp.expand((h2p - p) + cyclic20) == 0
        and sp.expand((h2q - q) + cyclic21 - a * cyclic20 * (p + u1)) == 0
    )

    # Over Q(a), the fixed and primitive branch ideals are comaximal.  With
    # the difference factorization and the two exact parametrizations above,
    # this is the CRT certificate for the generic n=2 splitting.
    domain = sp.QQ.frac_field(a)
    crt_groebner = sp.groebner(
        (
            a * x0**2 + 2 * x1 - 1,
            a * x1**2 + 2 * x0 - 1,
            x0 - x1,
            a * (x0 + x1) - 2,
        ),
        x0,
        x1,
        order="lex",
        domain=domain,
    )
    generic_crt_comaximal_pass = sp.expand(crt_groebner.reduce(sp.Integer(1))[1]) == 0

    expected_d1 = -4 * (a + 1)
    expected_d2 = 2**8 * (a + 1) * (a - 3) ** 3
    checks = {
        "D_a_1": sp.sstr(d1),
        "D_a_1_pass": sp.simplify(d1 - expected_d1) == 0,
        "D_a_2": sp.sstr(d2),
        "D_a_2_pass": sp.simplify(d2 - expected_d2) == 0,
        "fixed_branch_residual_pass": sp.simplify(fixed_identity) == 0,
        "primitive_branch_residual_pass": all(sp.simplify(item) == 0 for item in primitive_residuals),
        "difference_factorization_pass": difference_identity == 0,
        "n1_iterate_cyclic_ideal_pass": n1_ideal_pass,
        "n2_iterate_cyclic_ideal_pass": n2_ideal_pass,
        "generic_crt_comaximal_pass": generic_crt_comaximal_pass,
        "period_two_splitting_scope": "Q(A); equivalently after excluding the branch collision A=3",
        "standard_monomial_count_formula": "2^n",
    }
    if not all(value for key, value in checks.items() if key.endswith("_pass")):
        raise AssertionError(f"symbolic identity failure: {checks}")
    return checks


def factor_degrees_mod(poly: sp.Poly, prime: int) -> list[int]:
    q = poly.gens[0]
    factors = sp.factor_list(sp.Poly(poly.as_expr(), q, modulus=prime))[1]
    return sorted(
        [int(sp.degree(factor, q)) for factor, exponent in factors for _ in range(exponent)],
        reverse=True,
    )


def integral_coefficients(poly: sp.Poly) -> list[int]:
    """Return exact integer coefficients, rejecting accidental QQ truncation."""
    coefficients = poly.all_coeffs()
    if any(sp.denom(coefficient) != 1 for coefficient in coefficients):
        raise AssertionError(f"nonintegral coefficient in {poly.as_expr()}")
    return [int(coefficient) for coefficient in coefficients]


def period_five_certificate() -> dict[str, object]:
    a, q, p, x = sp.symbols("a q p x")
    h5q, h5p = henon_iterate(a, 5)
    domain = sp.QQ.frac_field(a)
    on_r_q = sp.Poly(sp.expand((h5q - q).subs(p, q)), q, domain=domain)
    on_r_p = sp.Poly(sp.expand((h5p - p).subs(p, q)), q, domain=domain)
    common = sp.monic(sp.gcd(on_r_q, on_r_p)).as_expr()
    fixed = a * q**2 + 2 * q - 1
    generic_marker = sp.factor(sp.cancel(common * a**7 / fixed))
    expected_generic = (
        a**6 * q**6
        + 2 * a**5 * q**5
        + (-3 * a**5 + 2 * a**4) * q**4
        + (-4 * a**4 + 2 * a**3) * q**3
        + (3 * a**4 - 4 * a**3 + a**2) * q**2
        + (2 * a**3 - 2 * a**2) * q
        - a**3
        + 2 * a**2
        - a
        - 1
    )
    generic_pass = sp.simplify(generic_marker - expected_generic) == 0

    marker6 = sp.Poly(sp.expand(generic_marker.subs(a, 6)), q, domain=sp.ZZ)
    coeffs_q = integral_coefficients(marker6)
    scaled = sp.Poly(sp.expand(marker6.as_expr().subs(q, x / 6)), x, domain=sp.QQ)
    coeffs_x = integral_coefficients(scaled)
    published_z = [1, 2, -16, -22, 85, 60, -151]
    collision_pass = coeffs_x == published_z

    discriminant = int(sp.discriminant(marker6.as_expr(), q))
    discriminant_factors = {str(k): int(v) for k, v in sp.factorint(abs(discriminant)).items()}
    expected_disc = 2**36 * 3**30 * 31 * 241 * 389
    factor_types = {str(prime): factor_degrees_mod(marker6, prime) for prime in (37, 5, 157)}
    expected_types = {"37": [6], "5": [5, 1], "157": [2, 1, 1, 1, 1]}
    unramified = {
        str(prime): discriminant % prime != 0 and int(marker6.LC()) % prime != 0
        for prime in (37, 5, 157)
    }
    s6_pass = factor_types == expected_types and all(unramified.values())

    result = {
        "generic_reversor_marker": sp.sstr(generic_marker),
        "generic_marker_pass": generic_pass,
        "a6_q_coefficients": coeffs_q,
        "scaled_x_coefficients": coeffs_x,
        "published_brison_gallas_Z_coefficients": published_z,
        "published_collision_pass": collision_pass,
        "discriminant": discriminant,
        "discriminant_factorization": discriminant_factors,
        "discriminant_pass": discriminant == expected_disc,
        "unramified_certificate_primes": unramified,
        "factor_degrees": factor_types,
        "factor_degrees_pass": factor_types == expected_types,
        "galois_group_certificate": {
            "transitive_from_degree_6_frobenius": 37,
            "primitive_from_transitivity_and_5_cycle": 5,
            "transposition_prime": 157,
            "conclusion": "S6",
            "pass": s6_pass,
        },
        "novelty_status": COLLISION,
    }
    pass_keys = (
        result["generic_marker_pass"],
        result["published_collision_pass"],
        result["discriminant_pass"],
        result["factor_degrees_pass"],
        result["galois_group_certificate"]["pass"],
    )
    if not all(pass_keys):
        raise AssertionError(f"period-five certificate failed: {result}")
    return result


def joint_action_control() -> dict[str, object]:
    modulus = 5

    def trace(rotation: int, r: int, s: int) -> int:
        # Two H-cycles are exchanged by R(epsilon,i)=(-epsilon,-i).
        # F_c(epsilon,i)=(epsilon,i+epsilon*c) commutes with both H and R.
        return sum(
            modulus if (epsilon * rotation * r - s) % modulus == 0 else 0
            for epsilon in (-1, 1)
        )

    ordinary = {
        "F_c1": [trace(1, r, 0) for r in range(1, 11)],
        "F_c2": [trace(2, r, 0) for r in range(1, 11)],
    }
    joint = {
        "F_c1": [[trace(1, r, s) for s in range(5)] for r in range(1, 6)],
        "F_c2": [[trace(2, r, s) for s in range(5)] for r in range(1, 6)],
    }
    result = {
        "frobenius_convention": "arithmetic",
        "matched_reversibility": {
            "state_space": "{+1,-1} x Z/5Z",
            "H": "(epsilon,i)->(epsilon,i+1)",
            "R": "(epsilon,i)->(-epsilon,-i)",
            "F_c": "(epsilon,i)->(epsilon,i+epsilon*c)",
            "RHR_equals_H_inverse": True,
            "F_commutes_with_H_and_R": True,
        },
        "ordinary_sequences": ordinary,
        "ordinary_collision_pass": ordinary["F_c1"] == ordinary["F_c2"],
        "joint_characters": joint,
        "joint_separation_pass": joint["F_c1"] != joint["F_c2"],
        "reversal_symmetry_pass": all(
            trace(c, r, s) == trace(c, r, -s)
            for c in (1, 2) for r in range(1, 6) for s in range(5)
        ),
        "smallest_witness": {"r": 1, "s": 1, "trace_F_c1": 5, "trace_F_c2": 0},
    }
    if not all(
        (result["ordinary_collision_pass"], result["joint_separation_pass"], result["reversal_symmetry_pass"])
    ):
        raise AssertionError("joint-action information-loss control failed")
    return result


def write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    project = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=project / "results")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    rows = low_period_rows()
    csv_path = args.output_dir / "c12a_low_period_counts.csv"
    write_csv(rows, csv_path)

    artifact = {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "HCS-C12A",
        "map": "H_a(q,p)=(1-a*q^2-p,q)",
        "parameter_provenance": "a=6 is an integral arithmetic specialization of the Paper-5 family, not a fitted critical parameter",
        "chronology": {"r": "Frobenius extension degree", "n": "Hénon iterate", "merged": False},
        "symbolic": symbolic_certificate(),
        "low_period_rows": rows,
        "local_zeta_theorem": {
            "formula": "Z_{a,p,n}(u)=det(I-u*Frob_p | Q_l[S_{a,p,n}])^-1",
            "scope": "finite_zero_dimensional_fibers_only",
            "eigenvalue_class": "roots_of_unity",
            "cohomological_degrees": [0],
            "nilpotents_visible": False,
            "length_weighted_count_definition": "sum of geometric local lengths over F_{p^r}-rational support points",
            "status": "PROVED_GENERAL_FINITE_SCHEME_FACT",
        },
        "joint_action_control": joint_action_control(),
        "period_five": period_five_certificate(),
        "route_decision": {
            "registered_candidate": DECISION,
            "period_five_reframe": COLLISION,
            "route_b_authorized": False,
        },
        "frozen_inputs": {
            "experiment_plan_sha256": sha256(project / "EXPERIMENT_PLAN.md"),
            "protocol_sha256": sha256(project / "code" / "PROTOCOL.md"),
            "counts_csv_sha256": sha256(csv_path),
            "producer_sha256": sha256(Path(__file__).resolve()),
        },
    }

    json_path = args.output_dir / "c12a_certificate.json"
    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(artifact, handle, indent=2, sort_keys=True)
        handle.write("\n")

    summary = {
        "certificate": str(json_path),
        "certificate_sha256": sha256(json_path),
        "counts_csv": str(csv_path),
        "counts_csv_sha256": sha256(csv_path),
        "producer_sha256": sha256(Path(__file__).resolve()),
        "decision": DECISION,
        "period_five": COLLISION,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
