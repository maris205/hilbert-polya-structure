#!/usr/bin/env python3
"""Independent fail-closed checker for the HCS-C48 certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable


SCHEMA = "hcs-c48-certificate-v1"
CONTROL_BOUND = 199
DIRECT_P3_CONTROL_PRIMES = (7, 13, 19, 31, 37, 43, 61)
EXPECTED_A = (
    -4, -4, -4, 8, -16, 20, -16, -28, 8, -28, 8,
    8, 44, -28, 56, 56, 8, -16, -16, -28, 32,
)


class GateFailure(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GateFailure(message)


def canonical_json(obj: Any) -> bytes:
    return json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def strict_equal(left: Any, right: Any) -> bool:
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return set(left) == set(right) and all(
            strict_equal(left[key], right[key]) for key in left
        )
    if isinstance(left, list):
        return len(left) == len(right) and all(
            strict_equal(a, b) for a, b in zip(left, right)
        )
    return left == right


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def is_prime(n: int) -> bool:
    if type(n) is not int or n < 2:
        return False
    for divisor in range(2, n):
        if divisor * divisor > n:
            break
        if n % divisor == 0:
            return False
    return True


def multiplicative_order(value: int, p: int) -> int:
    running = 1
    for exponent in range(1, p):
        running = running * value % p
        if running == 1:
            return exponent
    raise GateFailure("multiplicative order not found")


def least_primitive_root(p: int) -> int:
    for candidate in range(2, p):
        if multiplicative_order(candidate, p) == p - 1:
            return candidate
    raise GateFailure("primitive root not found")


def split_primes_through(bound: int) -> list[int]:
    return [p for p in range(5, bound + 1) if p % 3 == 1 and is_prime(p)]


def curve_value(
    p: int, rho: int, r: int, s: int, t: int, u: int
) -> int:
    return (
        rho * r**3 * (t**3 + u**3)
        + rho**2 * s**3 * t**2 * u
        - s**3 * t * u**2
    ) % p


@lru_cache(maxsize=None)
def count_curve_by_disjoint_charts(p: int, rho: int) -> int:
    """Independently partition each P1 into its affine line and infinity."""
    total = 0
    # s=u=1: p^2 points.
    for r in range(p):
        for t in range(p):
            total += curve_value(p, rho, r, 1, t, 1) == 0
    # s=1 and (t:u)=(1:0): p points.
    for r in range(p):
        total += curve_value(p, rho, r, 1, 1, 0) == 0
    # (r:s)=(1:0) and u=1: p points.
    for t in range(p):
        total += curve_value(p, rho, 1, 0, t, 1) == 0
    # Both infinity points.
    total += curve_value(p, rho, 1, 0, 1, 0) == 0
    return total


@lru_cache(maxsize=None)
def count_phase_by_eliminating_x1(p: int, rho: int) -> int:
    """Independent exact count of the ordered phase, eliminating x1.

    The producer eliminates x3.  Here the original phase is regrouped around
    x1, so agreement is a useful implementation cross-check and no transition
    matrix is averaged.
    """
    cubic = [2 * x**3 % p for x in range(p)]
    root_histogram = [[0] * p for _ in range(p)]
    for linear in range(p):
        for x1 in range(p):
            root_histogram[linear][(cubic[x1] + linear * x1) % p] += 1

    total = 0
    for x0 in range(p):
        for x2 in range(p):
            linear = (x0 + x2) % p
            for x3 in range(p):
                fixed = (
                    cubic[x0]
                    + cubic[x2]
                    + cubic[x3]
                    + x2 * x3
                    + rho * x3 * x0
                ) % p
                total += root_histogram[linear][(-fixed) % p]
    return total


def canonical_p1(p: int) -> list[tuple[int, int]]:
    return [(value, 1) for value in range(p)] + [(1, 0)]


def rebuild_boundary_profile(p: int, rho: int) -> dict[str, Any]:
    a_roots: list[list[int]] = []
    b_roots: list[list[int]] = []
    a_multiple: list[list[int]] = []
    b_multiple: list[list[int]] = []
    for t, u in canonical_p1(p):
        a = rho * (t**3 + u**3) % p
        b = t * u * (rho**2 * t - u) % p
        a_gradient = (3 * rho * t**2 % p, 3 * rho * u**2 % p)
        b_gradient = (
            u * (2 * rho**2 * t - u) % p,
            t * (rho**2 * t - 2 * u) % p,
        )
        point = [t, u]
        if a == 0:
            a_roots.append(point)
            if a_gradient == (0, 0):
                a_multiple.append(point)
        if b == 0:
            b_roots.append(point)
            if b_gradient == (0, 0):
                b_multiple.append(point)
    common = [point for point in a_roots if point in b_roots]
    require(len(a_roots) == len(b_roots) == 3, "boundary cubic root count")
    require(not a_multiple and not b_multiple and not common, "boundary roots")
    return {
        "A_projective_roots": a_roots,
        "B_projective_roots": b_roots,
        "A_multiple_roots": a_multiple,
        "B_multiple_roots": b_multiple,
        "common_A_B_roots": common,
        "A_at_interior_B_root_divided_by_t_cubed": 2 * rho % p,
        "two_and_three_nonzero": 2 % p != 0 and 3 % p != 0,
    }


def chart_polynomial_and_gradient(
    chart: int, p: int, rho: int, x: int, y: int
) -> tuple[int, int, int]:
    rho2 = rho * rho % p
    x2, x3 = x * x % p, x**3 % p
    y2, y3 = y * y % p, y**3 % p
    if chart == 0:
        return (
            (rho * (1 + y3) + x3 * y * (rho2 - y)) % p,
            (3 * x2 * y * (rho2 - y)) % p,
            (3 * rho * y2 + x3 * (rho2 - 2 * y)) % p,
        )
    if chart == 1:
        return (
            (rho * (y3 + 1) + x3 * y * (rho2 * y - 1)) % p,
            (3 * x2 * y * (rho2 * y - 1)) % p,
            (3 * rho * y2 + x3 * (2 * rho2 * y - 1)) % p,
        )
    if chart == 2:
        return (
            (rho * x3 * (1 + y3) + y * (rho2 - y)) % p,
            (3 * rho * x2 * (1 + y3)) % p,
            (3 * rho * x3 * y2 + rho2 - 2 * y) % p,
        )
    require(chart == 3, "invalid chart")
    return (
        (rho * x3 * (y3 + 1) + y * (rho2 * y - 1)) % p,
        (3 * rho * x2 * (y3 + 1)) % p,
        (3 * rho * x3 * y2 + 2 * rho2 * y - 1) % p,
    )


@lru_cache(maxsize=None)
def rebuild_chart_singular_counts(p: int, rho: int) -> list[int]:
    counts = []
    for chart in range(4):
        singular = 0
        for x in range(p):
            for y in range(p):
                singular += chart_polynomial_and_gradient(
                    chart, p, rho, x, y
                ) == (0, 0, 0)
        counts.append(singular)
    require(counts == [0, 0, 0, 0], "finite chart singularity")
    return counts


@lru_cache(maxsize=None)
def direct_p3_count_last_nonzero_normalization(p: int, rho: int) -> int:
    """Independent P3 enumeration with the last nonzero coordinate set to 1."""
    total = 0
    for last in range(3, -1, -1):
        number = p**last
        for encoded in range(number):
            prefix: list[int] = []
            value = encoded
            for _ in range(last):
                prefix.append(value % p)
                value //= p
            coordinates = prefix + [1] + [0] * (3 - last)
            x0, x1, x2, x3 = coordinates
            cubic = (x0**3 + x1**3 + x2**3 + x3**3) % p
            quadric = (x0 * x1 + x1 * x2 + x2 * x3 + rho * x3 * x0) % p
            total += cubic == 0 and quadric == 0
    return total


@lru_cache(maxsize=None)
def rebuild_control(p: int, expected_a: int) -> dict[str, Any]:
    require(type(p) is int and is_prime(p) and p % 3 == 1 and p > 3, "prime")
    generator = least_primitive_root(p)
    rho = pow(generator, (p - 1) // 3, p)
    require(multiplicative_order(rho, p) == 3, "rho order")
    curve_count = count_curve_by_disjoint_charts(p, rho)
    a_p = p + 1 - curve_count
    require(a_p == expected_a, "Frobenius ledger")
    zero_count = count_phase_by_eliminating_x1(p, rho)
    p3 = p**3 + p**2 + p + 1
    surface = p**2 + 7 * p + 1
    quadric = (p + 1) ** 2
    direction = 1 + p3 - surface - quadric + p * curve_count
    simplified = p**3 - p**2 - 8 * p + p * curve_count
    require(zero_count == direction == simplified, "direction count")
    traced = Fraction(2 * zero_count, p) - 2 * p**2
    normalized = traced / ((p - 1) // 2)
    require(traced.denominator == 1, "integrality")
    require(traced == -14 - 2 * a_p, "moment identity")
    require(a_p * a_p <= 64 * p, "integer Weil gate")
    return {
        "prime": p,
        "least_primitive_root": generator,
        "rho_order_3": rho,
        "rho_order_exactly_3": True,
        "real_cyclotomic_degree_d_p": (p - 1) // 2,
        "chronological_zero_count_Z_p": zero_count,
        "projective_counts": {
            "P3": p3,
            "split_Fermat_cubic_surface_S": surface,
            "split_quadric_R": quadric,
            "curve_X": curve_count,
        },
        "direction_formula_zero_count": direction,
        "direction_formula_matches_chronological_count": True,
        "frobenius_trace_a_p": a_p,
        "galois_traced_second_moment_C_p_2": traced.numerator,
        "normalized_second_moment_c_p_2": record(normalized),
        "moment_formula_matches_minus_14_minus_2a": True,
        "integer_Weil_gate": {
            "a_p_squared": a_p * a_p,
            "64p": 64 * p,
            "passes": True,
        },
        "smoothness_finite_control": rebuild_boundary_profile(p, rho),
        "four_affine_chart_singular_counts_over_F_p": rebuild_chart_singular_counts(
            p, rho
        ),
    }


def expected_source_lock(project_root: Path) -> list[dict[str, str]]:
    root = project_root.parent
    relatives = (
        "henon_mu3_galois_norm_rank_obstruction/results/c45_certificate.json",
        "henon_mu3_normalized_trace_operator_gate/results/c47_certificate.json",
    )
    return [
        {"path": f"henon_dynamics/{relative}", "sha256": sha256_file(root / relative)}
        for relative in relatives
    ]


@lru_cache(maxsize=None)
def expected_payload(project_root: Path) -> dict[str, Any]:
    primes = split_primes_through(CONTROL_BOUND)
    require(len(primes) == len(EXPECTED_A), "control ledger length")
    controls = [
        rebuild_control(p, a_p) for p, a_p in zip(primes, EXPECTED_A)
    ]
    direct_controls = []
    for p in DIRECT_P3_CONTROL_PRIMES:
        row = controls[primes.index(p)]
        count = direct_p3_count_last_nonzero_normalization(
            p, row["rho_order_3"]
        )
        require(count == row["projective_counts"]["curve_X"], "P3 intersection")
        direct_controls.append(
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
        "source_lock": expected_source_lock(project_root),
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
                "n_equals_1": record(Fraction(0)),
                "n_equals_2": record(Fraction(1, 4)),
                "n_at_least_3_uniform_wall": record(Fraction(1, 3)),
                "combined_log_Euler_germ": record(Fraction(1, 3)),
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
        "exact_direct_P3_intersection_controls": direct_controls,
        "aggregate_control": {
            "control_bound_inclusive": CONTROL_BOUND,
            "control_primes": primes,
            "number_of_controls": len(controls),
            "frobenius_trace_ledger": list(EXPECTED_A),
            "traced_second_moment_ledger": [-14 - 2 * a for a in EXPECTED_A],
            "all_direction_counts_match_chronological_counts": True,
            "all_exact_moment_identities_hold": True,
            "all_integer_Weil_gates_pass": True,
            "all_boundary_smoothness_controls_pass": True,
            "all_four_chart_singular_loci_empty_over_control_fields": True,
            "direct_P3_control_primes": list(DIRECT_P3_CONTROL_PRIMES),
            "all_direct_P3_intersection_counts_match_curve_counts": True,
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


def audit_certificate(
    certificate: Any, project_root: Path
) -> tuple[list[dict[str, str]], bool]:
    gates: list[dict[str, str]] = []

    def run(name: str, check: Callable[[], None]) -> None:
        try:
            check()
        except GateFailure as exc:
            gates.append({"gate": name, "status": "FAIL", "detail": str(exc)})
        except Exception as exc:
            gates.append(
                {
                    "gate": name,
                    "status": "ERROR",
                    "detail": f"{type(exc).__name__}: {exc}",
                }
            )
        else:
            gates.append({"gate": name, "status": "PASS", "detail": "verified"})

    def schema_gate() -> None:
        require(type(certificate) is dict, "certificate must be dictionary")
        require(
            set(certificate) == {"schema", "payload", "payload_sha256"},
            "top-level keys",
        )
        require(certificate["schema"] == SCHEMA, "schema")
        require(type(certificate["payload"]) is dict, "payload type")

    def digest_gate() -> None:
        expected = hashlib.sha256(canonical_json(certificate["payload"])).hexdigest()
        require(certificate["payload_sha256"] == expected, "payload digest")

    def source_gate() -> None:
        require(
            strict_equal(
                certificate["payload"]["source_lock"],
                expected_source_lock(project_root),
            ),
            "source lock",
        )

    def prime_scope_gate() -> None:
        aggregate = certificate["payload"]["aggregate_control"]
        require(
            type(aggregate["control_bound_inclusive"]) is int
            and aggregate["control_bound_inclusive"] == CONTROL_BOUND,
            "control bound",
        )
        primes = split_primes_through(CONTROL_BOUND)
        require(aggregate["control_primes"] == primes, "complete prime ledger")
        actual = [row["prime"] for row in certificate["payload"]["exact_controls"]]
        require(all(type(p) is int for p in actual) and actual == primes, "control rows")

    def chronological_gate() -> None:
        for row, a_p in zip(
            certificate["payload"]["exact_controls"], EXPECTED_A
        ):
            expected = rebuild_control(row["prime"], a_p)
            require(
                type(row["least_primitive_root"]) is int
                and row["least_primitive_root"] == expected["least_primitive_root"]
                and type(row["rho_order_3"]) is int
                and row["rho_order_3"] == expected["rho_order_3"]
                and row["rho_order_exactly_3"] is True,
                f"order-three convention p={row['prime']}",
            )
            require(
                row["chronological_zero_count_Z_p"]
                == expected["chronological_zero_count_Z_p"],
                f"chronological count p={row['prime']}",
            )
        model = certificate["payload"]["finite_field_model"]
        require(model["chronology_preserved"] is True, "chronology flag")
        require(model["averaged_transition_matrix_used"] is False, "averaging flag")
        require(model["norm_clock"] == "z_p=p^(-s)", "norm clock")
        require(model["chronological_control_algorithm"].startswith("exact terminal-step dynamic program"), "chronological algorithm")

    def projective_gate() -> None:
        theorem = certificate["payload"]["projective_direction_theorem"]
        require(theorem["exact_count"] == "Z_p=1+#P3-#S-#R+p*#X", "direction theorem")
        require(theorem["split_Fermat_surface_count"] == "#S=p^2+7p+1", "surface")
        require(theorem["split_quadric_count"] == "#R=(p+1)^2", "quadric")
        for row, a_p in zip(certificate["payload"]["exact_controls"], EXPECTED_A):
            expected = rebuild_control(row["prime"], a_p)
            keys = (
                "projective_counts", "direction_formula_zero_count",
                "direction_formula_matches_chronological_count",
            )
            require(
                all(strict_equal(row[key], expected[key]) for key in keys),
                f"projective direction data p={row['prime']}",
            )

    def direct_p3_gate() -> None:
        rows = certificate["payload"]["exact_direct_P3_intersection_controls"]
        require([row["prime"] for row in rows] == list(DIRECT_P3_CONTROL_PRIMES), "P3 primes")
        for row in rows:
            p = row["prime"]
            rho = pow(least_primitive_root(p), (p - 1) // 3, p)
            expected = direct_p3_count_last_nonzero_normalization(p, rho)
            require(
                row == {
                    "prime": p,
                    "direct_S_intersection_R_count_in_P3": expected,
                    "P1xP1_curve_count": expected,
                    "counts_match": True,
                },
                f"direct P3 intersection p={p}",
            )

    def smoothness_gate() -> None:
        theorem = certificate["payload"]["genus4_curve_theorem"]
        require(
            theorem["curve_equation"]
            == "F=rho*r^3*(t^3+u^3)+rho^2*s^3*t^2*u-s^3*t*u^2",
            "curve equation",
        )
        require(theorem["bidegree"] == [3, 3], "bidegree")
        require(theorem["excluded_characteristics"] == [2, 3], "characteristics")
        require(theorem["smooth_over_algebraic_closure"] is True, "geometric smoothness")
        require(
            theorem["smoothness_status"]
            == "DIRECT_ALL_PRIME_THEOREM_NOT_AN_INFERENCE_FROM_FINITE_CONTROLS",
            "all-prime proof status",
        )
        require(
            theorem["smoothness_cases"]
            == [
                "r*s!=0: radial derivatives force A=B=0; coordinate roots of B make A nonzero, while the remaining root u=rho^2*t gives A/t^3=2*rho!=0",
                "r=0: a singular point would be a multiple projective root of B, whose roots t=0,u=0,u=rho^2*t are distinct",
                "s=0: a singular point would be a multiple projective root of the separable binary cubic A",
            ],
            "smoothness cases",
        )
        require(
            theorem["four_affine_chart_polynomials"]
            == [
                "rho*(1+y^3)+x^3*y*(rho^2-y)",
                "rho*(y^3+1)+x^3*y*(rho^2*y-1)",
                "rho*x^3*(1+y^3)+y*(rho^2-y)",
                "rho*x^3*(y^3+1)+y*(rho^2*y-1)",
            ],
            "chart cover",
        )
        require(theorem["geometrically_irreducible"] is True, "irreducibility")
        require(type(theorem["genus_by_adjunction"]) is int and theorem["genus_by_adjunction"] == 4, "genus")
        for row, a_p in zip(certificate["payload"]["exact_controls"], EXPECTED_A):
            expected = rebuild_control(row["prime"], a_p)
            require(
                strict_equal(
                    row["smoothness_finite_control"],
                    expected["smoothness_finite_control"],
                ),
                f"boundary roots p={row['prime']}",
            )
            require(
                strict_equal(
                    row["four_affine_chart_singular_counts_over_F_p"],
                    [0, 0, 0, 0],
                ),
                f"chart singularity p={row['prime']}",
            )

    def moment_Weil_gate() -> None:
        theorem = certificate["payload"]["second_moment_theorem"]
        require(theorem["exact_traced_identity"] == "C_p,2=-14-2*a_p", "traced identity")
        require(theorem["exact_normalized_identity"] == "c_p,2=-(28+4*a_p)/(p-1)", "normalized identity")
        require(theorem["integer_Weil_certificate"] == "a_p^2<=64*p", "Weil theorem")
        for row, a_p in zip(certificate["payload"]["exact_controls"], EXPECTED_A):
            expected = rebuild_control(row["prime"], a_p)
            keys = (
                "frobenius_trace_a_p", "galois_traced_second_moment_C_p_2",
                "normalized_second_moment_c_p_2",
                "moment_formula_matches_minus_14_minus_2a", "integer_Weil_gate",
            )
            require(
                all(strict_equal(row[key], expected[key]) for key in keys),
                f"moment/Weil p={row['prime']}",
            )

    def analytic_gate() -> None:
        data = certificate["payload"]["analytic_upgrade"]
        require(data["first_moment"] == "c_p,1=-12/(p-1)", "first moment")
        require(
            strict_equal(data["absolute_convergence_abscissae"], {
                "n_equals_1": record(Fraction(0)),
                "n_equals_2": record(Fraction(1, 4)),
                "n_at_least_3_uniform_wall": record(Fraction(1, 3)),
                "combined_log_Euler_germ": record(Fraction(1, 3)),
            }),
            "abscissae",
        )
        require(data["first_active_unresolved_wall"] == "n=3", "active wall")
        require(data["continuation_through_one_third"] == "NOT_PROVED", "continuation scope")

    def det6_gate() -> None:
        data = certificate["payload"]["sixth_order_regularized_determinant"]
        require(data["inherited_semifinite_ideal_criterion"] == "X_s in L^q(M,tau) iff q*Re(s)>2", "semifinite ideal")
        require(data["tau_L6_domain"] == "Re(s)>1/3", "tau L6")
        require(data["tau_L5_domain"] == "Re(s)>2/5", "tau L5 obstruction")
        require(type(data["minimal_fixed_tau_Lq_order_on_full_domain"]) is int and data["minimal_fixed_tau_Lq_order_on_full_domain"] == 6, "minimal tau order")
        require(data["exact_factorization"] == "G(s)=exp(-sum_(n=1)^5 ell_n(s)/n)*det6_tau_gr(I-X_s)", "factorization")
        require(data["unregularized_tau_trace_class_domain"] == "Re(s)>2", "unregularized tau trace class")
        require(data["classical_Hilbert_trace_identity"] == "Tr_H(|X_s|^q)=sum_(p=1 mod 3) d_p*((8p+4)/3)*p^(-q*Re(s))", "classical trace identity")
        require(data["classical_Schatten_criterion"] == "X_s in classical S^q(H) iff q*Re(s)>3", "classical Schatten")
        require(data["classical_trace_class_domain"] == "Re(s)>3", "classical trace class")
        require(data["classical_determinant_warning"].endswith("field-degree-normalized root G"), "classical determinant warning")
        require(data["determinant_category"] == "semifinite tau-associated graded regularization, not a classical Fredholm determinant", "determinant category")
        require(data["counterterm_status"].startswith("five source-native"), "counterterms")

    def decision_gate() -> None:
        decisions = certificate["payload"]["decisions"]
        require(decisions["second_moment_arithmetic_structure"] == "EXPLICIT_SMOOTH_GENUS4_FROBENIUS_TRACE", "structure")
        require(decisions["all_prime_smoothness"] == "PROVED_DIRECTLY_OUTSIDE_CHARACTERISTICS_2_AND_3", "smoothness")
        require(decisions["normalized_Euler_germ_domain"] == "IMPROVED_FROM_RE_S_GT_ONE_HALF_TO_RE_S_GT_ONE_THIRD", "Euler domain")
        require(decisions["sixth_order_regularized_graded_determinant"] == "CONSTRUCTED_IN_SEMIFINITE_TAU_CATEGORY_ON_RE_S_GT_ONE_THIRD", "Det6")
        require(decisions["ordinary_trace_class_determinant_on_that_domain"] == "NOT_CLAIMED", "L1 scope")

    def route_scope_gate() -> None:
        route = certificate["payload"]["route_a"]
        require(route["A1"] == "A1_WEAK", "A1")
        require(route["A2"] == "A2_ANALYTIC_DETERMINANT", "A2")
        require(route["A3"] == "A3_PARTIAL_ANALYTIC_STRUCTURE", "A3")
        require(route["A4"] == "A4_NATURAL_QUANTIZATION", "A4")
        require(route["overall"] == "ROUTE_A_EXPLORATORY", "overall")
        require(route["route_b_invocation_allowed"] is False, "Route B")
        scope = certificate["payload"]["scope"]
        require(all(type(value) is bool for value in scope.values()), "scope types")
        require(not any(scope.values()), "scope overclaim")

    def aggregate_gate() -> None:
        aggregate = certificate["payload"]["aggregate_control"]
        expected = expected_payload(project_root)["aggregate_control"]
        require(strict_equal(aggregate, expected), "aggregate ledger")

    def replay_gate() -> None:
        require(
            strict_equal(certificate["payload"], expected_payload(project_root)),
            "full payload replay",
        )

    run("G01_SCHEMA_AND_TYPES", schema_gate)
    run("G02_PAYLOAD_DIGEST", digest_gate)
    run("G03_SOURCE_LOCK", source_gate)
    run("G04_COMPLETE_SPLIT_PRIME_SCOPE", prime_scope_gate)
    run("G05_CHRONOLOGICAL_PHASE_COUNTS", chronological_gate)
    run("G06_PROJECTIVE_DIRECTION_COUNTS", projective_gate)
    run("G07_DIRECT_P3_INTERSECTION_CONTROLS", direct_p3_gate)
    run("G08_ALL_PRIME_SMOOTH_GENUS4_THEOREM", smoothness_gate)
    run("G09_SECOND_MOMENT_AND_INTEGER_WEIL", moment_Weil_gate)
    run("G10_ONE_THIRD_ANALYTIC_UPGRADE", analytic_gate)
    run("G11_MINIMAL_DET6_FACTORIZATION", det6_gate)
    run("G12_DECISIONS", decision_gate)
    run("G13_ROUTE_A_AND_SCOPE", route_scope_gate)
    run("G14_AGGREGATE_CONTROL", aggregate_gate)
    run("G15_FULL_PAYLOAD_REPLAY", replay_gate)
    return gates, all(row["status"] == "PASS" for row in gates)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate")
    parser.add_argument("--output")
    args = parser.parse_args()
    path = Path(args.certificate)
    project_root = Path(__file__).resolve().parents[1]
    certificate = json.loads(path.read_text(encoding="utf-8"))
    gates, passed = audit_certificate(certificate, project_root)
    report = {
        "schema": "hcs-c48-independent-check-v1",
        "certificate_sha256": sha256_file(path),
        "gates": gates,
        "passed": passed,
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
