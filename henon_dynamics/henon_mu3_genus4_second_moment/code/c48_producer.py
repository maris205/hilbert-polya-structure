#!/usr/bin/env python3
"""Produce the exact HCS-C48 genus-four second-moment certificate.

The finite controls keep the four chronological variables in their original
order.  The separate projective computation counts the explicit (3,3) curve
on P1 x P1 and checks the direction-count identity prime by prime.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


SCHEMA = "hcs-c48-certificate-v1"
CONTROL_BOUND = 199
DIRECT_P3_CONTROL_PRIMES = (7, 13, 19, 31, 37, 43, 61)
EXPECTED_A = (
    -4, -4, -4, 8, -16, 20, -16, -28, 8, -28, 8,
    8, 44, -28, 56, 56, 8, -16, -16, -28, 32,
)


def canonical_json(obj: Any) -> bytes:
    return json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def fraction_record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def is_prime(n: int) -> bool:
    if type(n) is not int or n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def prime_divisors(n: int) -> list[int]:
    answer: list[int] = []
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            answer.append(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor += 1
    if n > 1:
        answer.append(n)
    return answer


def primitive_root(p: int) -> int:
    factors = prime_divisors(p - 1)
    for candidate in range(2, p):
        if all(pow(candidate, (p - 1) // q, p) != 1 for q in factors):
            return candidate
    raise AssertionError("primitive root not found")


def split_primes_through(bound: int) -> tuple[int, ...]:
    return tuple(p for p in range(5, bound + 1) if p % 3 == 1 and is_prime(p))


def p1_points(p: int) -> tuple[tuple[int, int], ...]:
    """Canonical representatives (v:1), followed by (1:0)."""
    return tuple((value, 1) for value in range(p)) + ((1, 0),)


def curve_value(
    p: int, rho: int, r: int, s: int, t: int, u: int
) -> int:
    return (
        rho * pow(r, 3, p) * (pow(t, 3, p) + pow(u, 3, p))
        + pow(rho, 2, p) * pow(s, 3, p) * pow(t, 2, p) * u
        - pow(s, 3, p) * t * pow(u, 2, p)
    ) % p


def count_curve_p1xp1(p: int, rho: int) -> int:
    total = 0
    points = p1_points(p)
    for r, s in points:
        for t, u in points:
            total += curve_value(p, rho, r, s, t, u) == 0
    return total


def boundary_root_profile(p: int, rho: int) -> dict[str, Any]:
    a_roots: list[list[int]] = []
    b_roots: list[list[int]] = []
    a_multiple: list[list[int]] = []
    b_multiple: list[list[int]] = []
    for t, u in p1_points(p):
        a = rho * (pow(t, 3, p) + pow(u, 3, p)) % p
        b = t * u * (rho * rho * t - u) % p
        da_t = 3 * rho * t * t % p
        da_u = 3 * rho * u * u % p
        db_t = u * (2 * rho * rho * t - u) % p
        db_u = t * (rho * rho * t - 2 * u) % p
        if a == 0:
            a_roots.append([t, u])
            if da_t == 0 and da_u == 0:
                a_multiple.append([t, u])
        if b == 0:
            b_roots.append([t, u])
            if db_t == 0 and db_u == 0:
                b_multiple.append([t, u])
    common = [point for point in a_roots if point in b_roots]
    interior_witness = 2 * rho % p
    assert len(a_roots) == len(b_roots) == 3
    assert not a_multiple and not b_multiple and not common
    assert interior_witness != 0
    return {
        "A_projective_roots": a_roots,
        "B_projective_roots": b_roots,
        "A_multiple_roots": a_multiple,
        "B_multiple_roots": b_multiple,
        "common_A_B_roots": common,
        "A_at_interior_B_root_divided_by_t_cubed": interior_witness,
        "two_and_three_nonzero": 2 % p != 0 and 3 % p != 0,
    }


def four_chart_singular_counts(p: int, rho: int) -> list[int]:
    """Exhaust the four standard affine charts of P1 x P1 over F_p."""
    rho2 = rho * rho % p
    counts = [0, 0, 0, 0]
    for x in range(p):
        x2 = x * x % p
        x3 = x2 * x % p
        for y in range(p):
            y2 = y * y % p
            y3 = y2 * y % p
            triples = (
                (
                    rho * (1 + y3) + x3 * y * (rho2 - y),
                    3 * x2 * y * (rho2 - y),
                    3 * rho * y2 + x3 * (rho2 - 2 * y),
                ),
                (
                    rho * (y3 + 1) + x3 * y * (rho2 * y - 1),
                    3 * x2 * y * (rho2 * y - 1),
                    3 * rho * y2 + x3 * (2 * rho2 * y - 1),
                ),
                (
                    rho * x3 * (1 + y3) + y * (rho2 - y),
                    3 * rho * x2 * (1 + y3),
                    3 * rho * x3 * y2 + rho2 - 2 * y,
                ),
                (
                    rho * x3 * (y3 + 1) + y * (rho2 * y - 1),
                    3 * rho * x2 * (y3 + 1),
                    3 * rho * x3 * y2 + 2 * rho2 * y - 1,
                ),
            )
            for chart, (value, dx, dy) in enumerate(triples):
                if value % p == dx % p == dy % p == 0:
                    counts[chart] += 1
    assert counts == [0, 0, 0, 0]
    return counts


def direct_p3_intersection_count(p: int, rho: int) -> int:
    """Count S cap R using first-nonzero-coordinate P3 representatives."""
    total = 0
    for first in range(4):
        prefix = [0] * first + [1]
        suffix_length = 3 - first
        number = p**suffix_length
        for encoded in range(number):
            suffix: list[int] = []
            value = encoded
            for _ in range(suffix_length):
                suffix.append(value % p)
                value //= p
            x0, x1, x2, x3 = prefix + suffix
            cubic = (x0**3 + x1**3 + x2**3 + x3**3) % p
            quadric = (x0 * x1 + x1 * x2 + x2 * x3 + rho * x3 * x0) % p
            total += cubic == 0 and quadric == 0
    return total


def chronological_zero_count(p: int, rho: int) -> int:
    """Count Phi=0 using a last-variable root table, without reordering Phi."""
    cubic = [2 * pow(x, 3, p) % p for x in range(p)]
    # roots[linear][target] counts x with 2*x^3+linear*x=target.
    roots = [[0] * p for _ in range(p)]
    for linear in range(p):
        row = roots[linear]
        for x in range(p):
            row[(cubic[x] + linear * x) % p] += 1

    total = 0
    for x0 in range(p):
        c0 = cubic[x0]
        for x1 in range(p):
            partial01 = (c0 + cubic[x1] + x0 * x1) % p
            for x2 in range(p):
                partial = (partial01 + cubic[x2] + x1 * x2) % p
                linear = (x2 + rho * x0) % p
                total += roots[linear][(-partial) % p]
    return total


def build_control(p: int, expected_a: int) -> dict[str, Any]:
    assert is_prime(p) and p % 3 == 1 and p > 3
    generator = primitive_root(p)
    rho = pow(generator, (p - 1) // 3, p)
    assert rho != 1 and pow(rho, 3, p) == 1

    curve_count = count_curve_p1xp1(p, rho)
    a_p = p + 1 - curve_count
    assert a_p == expected_a

    zero_count = chronological_zero_count(p, rho)
    projective_3 = p**3 + p**2 + p + 1
    fermat_surface = p**2 + 7 * p + 1
    split_quadric = (p + 1) ** 2
    direction_zero_count = (
        1 + projective_3 - fermat_surface - split_quadric + p * curve_count
    )
    simplified_zero_count = p**3 - p**2 - 8 * p + p * curve_count
    assert zero_count == direction_zero_count == simplified_zero_count

    traced = Fraction(2 * zero_count, p) - 2 * p**2
    d_p = (p - 1) // 2
    normalized = traced / d_p
    assert traced.denominator == 1
    assert traced == -14 - 2 * a_p
    assert normalized == Fraction(-28 - 4 * a_p, p - 1)
    assert a_p * a_p <= 64 * p

    return {
        "prime": p,
        "least_primitive_root": generator,
        "rho_order_3": rho,
        "rho_order_exactly_3": rho != 1 and pow(rho, 3, p) == 1,
        "real_cyclotomic_degree_d_p": d_p,
        "chronological_zero_count_Z_p": zero_count,
        "projective_counts": {
            "P3": projective_3,
            "split_Fermat_cubic_surface_S": fermat_surface,
            "split_quadric_R": split_quadric,
            "curve_X": curve_count,
        },
        "direction_formula_zero_count": direction_zero_count,
        "direction_formula_matches_chronological_count": True,
        "frobenius_trace_a_p": a_p,
        "galois_traced_second_moment_C_p_2": traced.numerator,
        "normalized_second_moment_c_p_2": fraction_record(normalized),
        "moment_formula_matches_minus_14_minus_2a": True,
        "integer_Weil_gate": {
            "a_p_squared": a_p * a_p,
            "64p": 64 * p,
            "passes": True,
        },
        "smoothness_finite_control": boundary_root_profile(p, rho),
        "four_affine_chart_singular_counts_over_F_p": four_chart_singular_counts(
            p, rho
        ),
    }


def source_lock(project_root: Path) -> list[dict[str, str]]:
    root = project_root.parent
    relatives = (
        "henon_mu3_galois_norm_rank_obstruction/results/c45_certificate.json",
        "henon_mu3_normalized_trace_operator_gate/results/c47_certificate.json",
    )
    answer: list[dict[str, str]] = []
    for relative in relatives:
        source = root / relative
        if not source.is_file():
            raise FileNotFoundError(source)
        answer.append(
            {"path": f"henon_dynamics/{relative}", "sha256": sha256_file(source)}
        )
    return answer


def build_payload(project_root: Path) -> dict[str, Any]:
    primes = split_primes_through(CONTROL_BOUND)
    assert len(primes) == len(EXPECTED_A)
    controls = [
        build_control(p, expected_a) for p, expected_a in zip(primes, EXPECTED_A)
    ]
    direct_p3_controls = []
    for p in DIRECT_P3_CONTROL_PRIMES:
        row = controls[primes.index(p)]
        count = direct_p3_intersection_count(p, row["rho_order_3"])
        assert count == row["projective_counts"]["curve_X"]
        direct_p3_controls.append(
            {
                "prime": p,
                "direct_S_intersection_R_count_in_P3": count,
                "P1xP1_curve_count": row["projective_counts"]["curve_X"],
                "counts_match": True,
            }
        )
    return {
        "material_passport": {
            "candidate_id": "HCS-C48",
            "project": "henon_mu3_genus4_second_moment",
            "ai_assistance_disclosed": True,
            "evidence_policy": "all-prime algebraic proof plus exact chronological and projective controls; no Riemann-zero data",
        },
        "source_lock": source_lock(project_root),
        "finite_field_model": {
            "prime_scope": "p>3 prime and p=1 mod 3",
            "rho_convention": "rho is the nontrivial cube root obtained from the least primitive root",
            "norm_clock": "z_p=p^(-s)",
            "chronological_phase": "Phi=2*(x0^3+x1^3+x2^3+x3^3)+x0*x1+x1*x2+x2*x3+rho*x3*x0",
            "chronological_control_algorithm": "exact terminal-step dynamic program with cubic-linear root kernel; x0,x1,x2 remain ordered and x3 closes the rho-twisted edge",
            "chronology_preserved": True,
            "averaged_transition_matrix_used": False,
        },
        "projective_direction_theorem": {
            "homogeneous_parts": "C=sum_i x_i^3 and Q=x0*x1+x1*x2+x2*x3+rho*x3*x0",
            "radial_identity": "Phi(lambda*v)=lambda^2*(2*lambda*C(v)+Q(v))",
            "exact_count": "Z_p=1+#P3-#S-#R+p*#X",
            "P3_count": "p^3+p^2+p+1",
            "split_Fermat_surface_count": "#S=p^2+7p+1",
            "split_quadric_count": "#R=(p+1)^2",
            "simplified_count": "Z_p=p^3-p^2-8p+p*#X",
            "quadric_split_change": "y=x1+rho*x3, w=x1+x3 gives Q=x0*y+x2*w",
            "status": "PROVED_FOR_EVERY_SPLIT_PRIME_P_GREATER_THAN_3",
        },
        "genus4_curve_theorem": {
            "quadric_parametrization": "x0=r*t, x2=r*u, x1=s*(rho*t+u)/(rho-1), x3=-s*(t+u)/(rho-1)",
            "curve_equation": "F=rho*r^3*(t^3+u^3)+rho^2*s^3*t^2*u-s^3*t*u^2",
            "ambient": "P1_(r:s) x P1_(t:u)",
            "bidegree": [3, 3],
            "decomposition": "F=A*r^3+B*s^3 with A=rho*(t^3+u^3), B=t*u*(rho^2*t-u)",
            "smoothness_cases": [
                "r*s!=0: radial derivatives force A=B=0; coordinate roots of B make A nonzero, while the remaining root u=rho^2*t gives A/t^3=2*rho!=0",
                "r=0: a singular point would be a multiple projective root of B, whose roots t=0,u=0,u=rho^2*t are distinct",
                "s=0: a singular point would be a multiple projective root of the separable binary cubic A",
            ],
            "excluded_characteristics": [2, 3],
            "smooth_over_algebraic_closure": True,
            "smoothness_status": "DIRECT_ALL_PRIME_THEOREM_NOT_AN_INFERENCE_FROM_FINITE_CONTROLS",
            "four_affine_chart_polynomials": [
                "rho*(1+y^3)+x^3*y*(rho^2-y)",
                "rho*(y^3+1)+x^3*y*(rho^2*y-1)",
                "rho*x^3*(1+y^3)+y*(rho^2-y)",
                "rho*x^3*(y^3+1)+y*(rho^2*y-1)",
            ],
            "geometrically_connected_reason": "smooth ample divisor of bidegree (3,3) on P1xP1",
            "geometrically_irreducible": True,
            "genus_by_adjunction": 4,
        },
        "second_moment_theorem": {
            "definitions": "a_p=p+1-#X(F_p), C_p,2=2*Z_p/p-2*p^2, c_p,2=C_p,2/d_p, d_p=(p-1)/2",
            "exact_traced_identity": "C_p,2=-14-2*a_p",
            "exact_normalized_identity": "c_p,2=-(28+4*a_p)/(p-1)",
            "hasse_Weil_trace_bound": "|a_p|<=8*sqrt(p)",
            "integer_Weil_certificate": "a_p^2<=64*p",
            "normalized_bound": "|c_p,2|<=(28+32*sqrt(p))/(p-1)",
            "interpretation": "the non-Tate residue of the second chronological moment is a genus-four Frobenius trace",
            "status": "PROVED_FOR_EVERY_SPLIT_PRIME_P_GREATER_THAN_3",
        },
        "analytic_upgrade": {
            "first_moment": "c_p,1=-12/(p-1)",
            "higher_moment_bound": "|c_p,n|<=4*4^n for n>=3",
            "absolute_convergence_abscissae": {
                "n_equals_1": fraction_record(Fraction(0)),
                "n_equals_2": fraction_record(Fraction(1, 4)),
                "n_at_least_3_uniform_wall": fraction_record(Fraction(1, 3)),
                "combined_log_Euler_germ": fraction_record(Fraction(1, 3)),
            },
            "normal_convergence": "sum_p sum_n |c_p,n|*p^(-n*Re(s))/n converges locally uniformly for Re(s)>1/3",
            "Euler_germ": "canonical normalized Euler product is holomorphic and nonzero for Re(s)>1/3",
            "first_active_unresolved_wall": "n=3",
            "continuation_through_one_third": "NOT_PROVED",
        },
        "sixth_order_regularized_determinant": {
            "inherited_semifinite_ideal_criterion": "X_s in L^q(M,tau) iff q*Re(s)>2",
            "tau_L6_domain": "Re(s)>1/3",
            "tau_L5_domain": "Re(s)>2/5",
            "counterterms": "ell_n(s)=sum_p c_p,n*p^(-n*s), n=1,2,3,4,5",
            "det6_definition": "det6_tau_gr(I-X_s)=exp(-sum_(n>=6) str_tau(X_s^n)/n)",
            "exact_factorization": "G(s)=exp(-sum_(n=1)^5 ell_n(s)/n)*det6_tau_gr(I-X_s)",
            "minimal_fixed_tau_Lq_order_on_full_domain": 6,
            "unregularized_tau_trace_class_domain": "Re(s)>2",
            "classical_Hilbert_trace_identity": "Tr_H(|X_s|^q)=sum_(p=1 mod 3) d_p*((8p+4)/3)*p^(-q*Re(s))",
            "classical_Schatten_criterion": "X_s in classical S^q(H) iff q*Re(s)>3",
            "classical_trace_class_domain": "Re(s)>3",
            "classical_determinant_warning": "the classical Hilbert trace does not implement the field-degree-normalized root G",
            "determinant_category": "semifinite tau-associated graded regularization, not a classical Fredholm determinant",
            "counterterm_status": "five source-native chronological Galois-supertrace moments, not fitted prefactors",
            "gain_mechanism": "arithmetic cancellation in the second signed moment, not improved positive-ideal membership",
        },
        "exact_controls": controls,
        "exact_direct_P3_intersection_controls": direct_p3_controls,
        "aggregate_control": {
            "control_bound_inclusive": CONTROL_BOUND,
            "control_primes": list(primes),
            "number_of_controls": len(controls),
            "frobenius_trace_ledger": list(EXPECTED_A),
            "traced_second_moment_ledger": [-14 - 2 * a for a in EXPECTED_A],
            "all_direction_counts_match_chronological_counts": all(
                row["direction_formula_matches_chronological_count"] for row in controls
            ),
            "all_exact_moment_identities_hold": all(
                row["moment_formula_matches_minus_14_minus_2a"] for row in controls
            ),
            "all_integer_Weil_gates_pass": all(
                row["integer_Weil_gate"]["passes"] for row in controls
            ),
            "all_boundary_smoothness_controls_pass": all(
                not row["smoothness_finite_control"]["A_multiple_roots"]
                and not row["smoothness_finite_control"]["B_multiple_roots"]
                and not row["smoothness_finite_control"]["common_A_B_roots"]
                for row in controls
            ),
            "all_four_chart_singular_loci_empty_over_control_fields": all(
                row["four_affine_chart_singular_counts_over_F_p"] == [0, 0, 0, 0]
                for row in controls
            ),
            "direct_P3_control_primes": list(DIRECT_P3_CONTROL_PRIMES),
            "all_direct_P3_intersection_counts_match_curve_counts": all(
                row["counts_match"] for row in direct_p3_controls
            ),
        },
        "decisions": {
            "second_moment_arithmetic_structure": "EXPLICIT_SMOOTH_GENUS4_FROBENIUS_TRACE",
            "all_prime_smoothness": "PROVED_DIRECTLY_OUTSIDE_CHARACTERISTICS_2_AND_3",
            "normalized_Euler_germ_domain": "IMPROVED_FROM_RE_S_GT_ONE_HALF_TO_RE_S_GT_ONE_THIRD",
            "sixth_order_regularized_graded_determinant": "CONSTRUCTED_IN_SEMIFINITE_TAU_CATEGORY_ON_RE_S_GT_ONE_THIRD",
            "ordinary_trace_class_determinant_on_that_domain": "NOT_CLAIMED",
            "next_large_gate": "THIRD_CHRONOLOGICAL_MOMENT_ARITHMETIC_STRUCTURE_AT_THE_ONE_THIRD_WALL",
        },
        "route_a": {
            "A1": "A1_WEAK",
            "A2": "A2_ANALYTIC_DETERMINANT",
            "A2_reason": "the exact genus-four second-moment cancellation yields a canonical Det6 graded realization in L6(M,tau) and a nonzero Euler germ on Re(s)>1/3",
            "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "A3_reason": "the arithmetic Frobenius structure improves the analytic half-plane, but no continuation, functional equation, Gamma factor, or Riemann divisor is proved",
            "A4": "A4_NATURAL_QUANTIZATION",
            "overall": "ROUTE_A_EXPLORATORY",
            "scoped_status": "ROUTE_A_EXPLORATORY_GENUS4_THIRD_ABSCISSA",
            "route_b_invocation_allowed": False,
        },
        "scope": {
            "rh_proved": False,
            "hilbert_polya_self_adjoint_operator_constructed": False,
            "global_meromorphic_continuation_claimed": False,
            "functional_equation_claimed": False,
            "gamma_factor_claimed": False,
            "riemann_divisor_claimed": False,
            "riemann_zero_data_used": False,
            "finite_controls_used_as_proof_of_all_prime_smoothness": False,
            "unregularized_tau_L1_determinant_claimed_on_Re_s_gt_one_third": False,
            "classical_Fredholm_determinant_claimed_on_Re_s_gt_one_third": False,
            "classical_Schatten_criterion_claimed_qRe_s_gt_2": False,
        },
    }


def build_certificate(project_root: Path) -> dict[str, Any]:
    payload = build_payload(project_root)
    return {
        "schema": SCHEMA,
        "payload": payload,
        "payload_sha256": hashlib.sha256(canonical_json(payload)).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()
    project_root = Path(__file__).resolve().parents[1]
    certificate = build_certificate(project_root)
    output = Path(arguments.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"wrote {output}")
    print(f"payload_sha256={certificate['payload_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
