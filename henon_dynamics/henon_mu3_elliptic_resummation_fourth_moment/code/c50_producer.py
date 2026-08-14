#!/usr/bin/env python3
"""Produce the exact HCS-C50 elliptic-resummation/fourth-moment certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp


SCHEMA = "hcs-c50-certificate-v1"
SOURCE_HASHES = {
    "henon_dynamics/henon_mu3_genus4_second_moment/results/c48_certificate.json":
        "92cd5c1079ebbaeaa27fc32e617852ae5d5989500ff3a816dd9fe306c32a32a8",
    "henon_dynamics/henon_mu3_fano_threefold_third_moment/results/c49_certificate.json":
        "b3ec1bf12ea0f05469054fda37bd34ee4b6748030813c8c6407752035a3c25d2",
}
FACTOR_ROWS = (
    (7, 2, -4, 2), (13, 3, -1, -1), (19, 7, -4, 2),
    (31, 25, -4, 8), (37, 26, -1, -7), (43, 36, 8, 2),
    (61, 47, -1, -7), (67, 37, -4, -10), (73, 8, 11, -7),
    (79, 23, -16, 2), (97, 35, 2, 2), (103, 56, -4, 8),
    (109, 63, 11, 11), (127, 107, -16, 2), (139, 96, 20, 8),
    (151, 32, 8, 20), (157, 12, -13, 17), (163, 104, 8, -16),
    (181, 48, -10, 2), (193, 84, -13, -1), (199, 106, -4, 20),
)
EXTENSION_COUNTS = {
    7: (12, 66, 372, 2586), 13: (18, 270, 2046, 27414),
    19: (24, 474, 6744, 129930), 31: (24, 1050, 29640, 926970),
}
# p,rho,Z,S,Q,X,alpha,beta,Cnum,Cden,cnum,cden
N4_ROWS = (
    (7, 2, 823690, 156171, 137600, 22380, 18914, -2772, 6, 7, 2, 7),
    (13, 3, 62719618, 5381481, 5231240, 411906, 152438, -9672, -342, 13, -57, 13),
    (19, 7, 893976790, 50171439, 49666400, 2646492, 511898, -32832, 582, 19, 194, 57),
    (31, 25, 27512444014, 918818859, 917116928, 29634792, 1731722, -51336, -354, 31, -118, 155),
    (37, 26, 94932973702, 2641057041, 2637047240, 71410926, 4060454, -140748, 1602, 37, 89, 37),
    (43, 36, 271817751322, 6477111759, 6471951200, 150612360, 5240066, -103716, -930, 43, -310, 301),
    (61, 47, 3142759524706, 52391334009, 52379274248, 859151634, 12286742, -478728, 8970, 61, 299, 61),
    (67, 37, 6060711080110, 91846102719, 91829264480, 1370834004, 17139002, -252456, -234, 67, -78, 737),
    (73, 8, 11047394090698, 153459186429, 153436479560, 2102125302, 23095886, -261048, -1662, 73, -277, 438),
    (79, 23, 19203877100890, 246245014659, 246204454400, 3116628132, 41053298, -122292, -10218, 79, -262, 79),
    (97, 35, 80798279594842, 841725254181, 841649709320, 8677539006, 76457534, -747288, -1038, 97, -173, 776),
)


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def record(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def reduce_rho(expression: Any, rho: Any) -> Any:
    numerator, denominator = sp.cancel(expression).as_numer_denom()
    numerator = sp.rem(numerator, rho**2 + rho + 1, rho, domain="QQ(x)")
    denominator = sp.rem(denominator, rho**2 + rho + 1, rho, domain="QQ(x)")
    return sp.factor(numerator / denominator)


def group_identities() -> dict[str, bool]:
    rho, x = sp.symbols("rho x")
    f = -x * (rho**2 * x - 1) / (rho * (x**3 + 1))
    t1 = rho**2 / x
    t2 = -rho**2 * (x + 1) / (x + rho**2)
    h = (rho - 1) / 3
    result = {
        "T1_squared_identity": reduce_rho(t1.subs(x, t1) - x, rho) == 0,
        "T2_squared_identity": reduce_rho(t2.subs(x, t2) - x, rho) == 0,
        "T1_T2_commute": reduce_rho(t1.subs(x, t2) - t2.subs(x, t1), rho) == 0,
        "f_T1_equals_minus_f": reduce_rho(f.subs(x, t1) / f + 1, rho) == 0,
        "f_T2_times_f_equals_h_cubed": reduce_rho(f.subs(x, t2) * f - h**3, rho) == 0,
    }
    if not all(result.values()):
        raise AssertionError("group identity failed")
    return result


def rational_matrix(matrix: sp.Matrix) -> list[list[dict[str, int]]]:
    return [[record(Fraction(int(value.p), int(value.q))) for value in row] for row in matrix.tolist()]


def idempotent_matrix_certificate() -> dict[str, Any]:
    identity2 = sp.eye(2)
    delta = sp.Matrix([[0, -1], [1, -1]])
    reflection = sp.Matrix([[0, 1], [1, 0]])
    e_std = (2 * identity2 - delta - delta**2) / 3
    e_j = (identity2 + reflection) / 2
    identity4 = sp.eye(4)
    central_i = sp.diag(1, 1, -1, -1)
    e_plus, e_minus = (identity4 + central_i) / 2, (identity4 - central_i) / 2
    e_std_j_4 = sp.diag(e_std * e_j, e_std * e_j)
    primitive_plus, primitive_minus = e_plus * e_std_j_4, e_minus * e_std_j_4
    assertions = [
        delta**3 == identity2, reflection**2 == identity2,
        reflection * delta * reflection == delta**2,
        e_std**2 == e_std, e_j**2 == e_j,
        e_plus**2 == e_plus, e_minus**2 == e_minus,
        primitive_plus**2 == primitive_plus,
        primitive_minus**2 == primitive_minus,
    ]
    if not all(assertions):
        raise AssertionError("standard-representation idempotent failure")
    return {
        "standard_delta_matrix": rational_matrix(delta),
        "standard_reflection_j_matrix": rational_matrix(reflection),
        "e_std_matrix": rational_matrix(e_std),
        "e_j_matrix": rational_matrix(e_j),
        "e_std_rank": e_std.rank(), "e_j_rank": e_j.rank(),
        "e_plus_rank_in_two_blocks": e_plus.rank(),
        "e_minus_rank_in_two_blocks": e_minus.rank(),
        "primitive_plus_rank": primitive_plus.rank(),
        "primitive_minus_rank": primitive_minus.rank(),
        "all_projectors_idempotent": True,
        "two_standard_blocks": True,
    }


def truncated_series_division(numerator: list[int], denominator: list[int], degree: int) -> list[int]:
    answer = [0] * (degree + 1)
    for n in range(degree + 1):
        source = numerator[n] if n < len(numerator) else 0
        answer[n] = source - sum(denominator[j] * answer[n-j] for j in range(1, min(n, len(denominator)-1)+1))
    return answer


def chern_certificate() -> dict[str, int]:
    numerator = [int(sp.binomial(8, k)) for k in range(9)]
    cubic = truncated_series_division(numerator, [1, 3], 6)
    complete = truncated_series_division(numerator, [1, 5, 6], 5)
    cubic_coefficient, complete_coefficient = cubic[6], complete[5]
    cubic_euler, complete_euler = 3 * cubic_coefficient, 6 * complete_coefficient
    primitive_b6 = cubic_euler - 7
    b5 = 6 - complete_euler
    if (cubic_coefficient, complete_coefficient, cubic_euler, complete_euler, primitive_b6, b5) != (31, -27, 93, -162, 86, 168):
        raise AssertionError("Chern/Betti calculation failed")
    return {
        "cubic_top_chern_coefficient": cubic_coefficient,
        "cubic_degree": 3, "cubic_Euler_characteristic": cubic_euler,
        "cubic_primitive_middle_b6": primitive_b6,
        "complete_intersection_top_chern_coefficient": complete_coefficient,
        "complete_intersection_degree": 6,
        "complete_intersection_Euler_characteristic": complete_euler,
        "complete_intersection_middle_b5": b5,
    }


def singular_groebner_basis() -> list[str]:
    if shutil.which("Singular") is None:
        raise RuntimeError("Singular is required for the characteristic-zero smoothness gate")
    script = """ring R=0,(x0,x1,x2,x3,x4,x5,x6,x7,r),dp;
poly Q=x0*x1+x1*x2+x2*x3+x3*x4+x4*x5+x5*x6+x6*x7+r*x7*x0;
ideal I=x0^2-x1-r*x7,x1^2-x0-x2,x2^2-x1-x3,x3^2-x2-x4,x4^2-x3-x5,x5^2-x4-x6,x6^2-x5-x7,x7^2-x6-r*x0,Q,r^2+r+1;
option(redSB); ideal G=std(I); G;
"""
    run = subprocess.run(["Singular", "-q"], input=script, text=True,
                         capture_output=True, check=True, timeout=60)
    rows = [line.split("=", 1)[1].strip() for line in run.stdout.splitlines() if line.startswith("G[")]
    expected = ["x7", "x6", "x5", "x4", "x3", "x2", "x1", "x0", "r^2+r+1"]
    if rows != expected:
        raise AssertionError(f"unexpected reduced singular basis: {rows}")
    return rows


def p1_points(p: int) -> list[tuple[int, int]]:
    return [(1, value) for value in range(p)] + [(0, 1)]


def curve_count(p: int, rho: int) -> int:
    total = 0
    for r, s in p1_points(p):
        r3, s3 = r**3 % p, s**3 % p
        for t, u in p1_points(p):
            value = rho * r3 * (t**3 + u**3) + s3 * t * u * (rho * rho * t - u)
            total += value % p == 0
    return total


def elliptic_trace(p: int) -> int:
    character_sum = 0
    for x in range(p):
        value = (x**3 + 69 * x + 22) % p
        if value:
            character_sum += 1 if pow(value, (p - 1) // 2, p) == 1 else -1
    return -character_sum


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return answer


def local_polynomial(p: int, a_plus: int, a_minus: int) -> list[int]:
    plus, minus = [1, -a_plus, p], [1, -a_minus, p]
    return multiply(multiply(plus, plus), multiply(minus, minus))


def newton_polynomial(p: int, counts: tuple[int, ...]) -> list[int]:
    traces = [p**degree + 1 - count for degree, count in enumerate(counts, 1)]
    coefficients = [1]
    for degree in range(1, 5):
        numerator = -sum(traces[j - 1] * coefficients[degree - j] for j in range(1, degree + 1))
        if numerator % degree:
            raise AssertionError("Newton coefficient not integral")
        coefficients.append(numerator // degree)
    return coefficients + [p ** (4 - degree) * coefficients[degree] for degree in range(3, -1, -1)]


def factor_controls() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rows, extensions = [], []
    for p, rho, expected_plus, expected_minus in FACTOR_ROWS:
        count = curve_count(p, rho)
        a_curve = p + 1 - count
        a_plus = elliptic_trace(p)
        if a_plus != expected_plus or a_curve != 2 * (expected_plus + expected_minus):
            raise AssertionError(f"factor trace mismatch at p={p}")
        polynomial = local_polynomial(p, expected_plus, expected_minus)
        rows.append({
            "p": p, "rho": rho, "curve_count": count,
            "curve_trace": a_curve, "E_plus_trace": a_plus,
            "E_minus_trace": expected_minus,
            "L_polynomial_coefficients_low_to_high": polynomial,
            "factorization_status": "THEOREM_DERIVED_FROM_GROUP_ISOGENY",
            "finite_degree_one_control_pass": True,
        })
        if p in EXTENSION_COUNTS:
            newton = newton_polynomial(p, EXTENSION_COUNTS[p])
            if newton != polynomial:
                raise AssertionError(f"extension Newton mismatch at p={p}")
            extensions.append({
                "p": p, "curve_counts_degrees_1_to_4": list(EXTENSION_COUNTS[p]),
                "Newton_polynomial_coefficients_low_to_high": newton,
                "matches_group_factorization": True,
            })
    return rows, extensions


def projective_space(p: int, dimension: int) -> int:
    return sum(p**j for j in range(dimension + 1))


def fermat_count(p: int, variables: int = 8) -> int:
    histogram = [0] * p
    for x in range(p):
        histogram[pow(x, 3, p)] += 1
    state = [0] * p
    state[0] = 1
    support = [(r, n) for r, n in enumerate(histogram) if n]
    for _ in range(variables):
        following = [0] * p
        for left, multiplicity in enumerate(state):
            if multiplicity:
                for right, other in support:
                    following[(left + right) % p] += multiplicity * other
        state = following
    return (state[0] - 1) // (p - 1)


def chronological_zero_count(p: int, rho: int) -> int:
    """Literal eight-step DP retaining start, endpoint, and phase residue."""
    cubes = [2 * pow(x, 3, p) % p for x in range(p)]
    total = 0
    for start in range(p):
        states = [[0] * p for _ in range(p)]
        states[start][cubes[start]] = 1
        for _ in range(1, 8):
            following = [[0] * p for _ in range(p)]
            for previous in range(p):
                shifts = [(previous * current + cubes[current]) % p for current in range(p)]
                for residue, multiplicity in enumerate(states[previous]):
                    if multiplicity:
                        for current, shift in enumerate(shifts):
                            following[current][(residue + shift) % p] += multiplicity
            states = following
        for endpoint in range(p):
            total += states[endpoint][(-rho * endpoint * start) % p]
    return total


def direct_affine_intersection_count(p: int, rho: int) -> int:
    """Independent C=Q=0 DP, used only for the two smallest controls."""
    cubes = [pow(x, 3, p) for x in range(p)]
    total = 0
    for start in range(p):
        states: dict[tuple[int, int, int], int] = {(start, cubes[start], 0): 1}
        for _ in range(1, 8):
            following: dict[tuple[int, int, int], int] = {}
            for (previous, cubic, quadric), multiplicity in states.items():
                for current in range(p):
                    key = (current, (cubic + cubes[current]) % p,
                           (quadric + previous * current) % p)
                    following[key] = following.get(key, 0) + multiplicity
            states = following
        for (endpoint, cubic, quadric), multiplicity in states.items():
            if cubic == 0 and (quadric + rho * endpoint * start) % p == 0:
                total += multiplicity
    return (total - 1) // (p - 1)


def n4_controls() -> list[dict[str, Any]]:
    answer = []
    for values in N4_ROWS:
        p, rho, zero, surface, quadric, intersection, alpha, beta, cn, cd, nn, nd = values
        if surface != fermat_count(p):
            raise AssertionError(f"Fermat count mismatch at p={p}")
        if quadric != (p**3 + 1) * (p**3 + p**2 + p + 1):
            raise AssertionError("split quadric mismatch")
        if zero != 1 + projective_space(p, 7) - surface - quadric + p * intersection:
            raise AssertionError("direction identity mismatch")
        if alpha != surface - projective_space(p, 6) or beta != projective_space(p, 5) - intersection:
            raise AssertionError("alpha/beta mismatch")
        traced = Fraction(2 * zero, p**3) - 2 * p**4
        formula = -2 - Fraction(2 * alpha, p**3) - Fraction(2 * beta, p**2)
        normalized = traced / ((p - 1) // 2)
        if traced != formula or record(traced) != {"numerator": cn, "denominator": cd} or record(normalized) != {"numerator": nn, "denominator": nd}:
            raise AssertionError("fourth moment mismatch")
        chronology_recomputed = p <= 31
        if chronology_recomputed and chronological_zero_count(p, rho) != zero:
            raise AssertionError(f"literal chronology mismatch at p={p}")
        direct_intersection = direct_affine_intersection_count(p, rho) if p <= 13 else None
        if direct_intersection is not None and direct_intersection != intersection:
            raise AssertionError(f"direct C=Q mismatch at p={p}")
        answer.append({
            "p": p, "rho": rho, "Z_p_4": zero,
            "S_cubic_sixfold": surface, "Q_split_sixfold": quadric,
            "X_complete_intersection_fivefold": intersection,
            "alpha_p": alpha, "beta_p": beta,
            "C_p_4": record(traced), "c_p_4": record(normalized),
            "literal_eight_step_chronology_recomputed": chronology_recomputed,
            "X_direct_affine_CQ_control": direct_intersection,
            "Weil_integer_bounds_pass": alpha * alpha <= 86**2 * p**6 and beta * beta <= 168**2 * p**5,
        })
    return answer


def p181_singular_points() -> list[dict[str, Any]]:
    p, rho = 181, 48
    points: list[dict[str, Any]] = []
    for x0 in range(p):
        for x1 in range(p):
            xs = [x0, x1]
            for index in range(1, 7):
                xs.append((xs[index] ** 2 - xs[index - 1]) % p)
            if (x1 + rho * xs[7] - x0 * x0) % p:
                continue
            if (xs[6] + rho * x0 - xs[7] * xs[7]) % p:
                continue
            if sum(pow(x, 3, p) for x in xs) % p:
                continue
            q_value = (sum(xs[index] * xs[index + 1] for index in range(7)) + rho * xs[7] * xs[0]) % p
            if q_value:
                continue
            if any(xs):
                points.append({"coordinates": xs, "C_mod_p": 0, "Q_mod_p": 0,
                               "normalized_gradient_recurrence_pass": True})
    if len(points) != 12:
        raise AssertionError(f"expected 12 p=181 singular tuples, got {len(points)}")
    return sorted(points, key=lambda row: row["coordinates"])


def build_payload(project: Path) -> dict[str, Any]:
    locks = []
    for relative, expected in SOURCE_HASHES.items():
        actual = sha256_file(project / relative)
        if actual != expected:
            raise AssertionError(f"source lock mismatch: {relative}")
        locks.append({"path": relative, "sha256": actual})
    factors, extensions = factor_controls()
    groebner = singular_groebner_basis()
    return {
        "material_passport": {
            "candidate_id": "HCS-C50",
            "project_slug": "henon_mu3_elliptic_resummation_fourth_moment",
            "artifact_status": "RELEASE_CANDIDATE",
        },
        "source_lock": locks,
        "curve_and_group": {
            "base_field": "K=Q(rho), rho^2+rho+1=0",
            "curve": "y^3=-x*(rho^2*x-1)/(rho*(x^3+1))",
            "exact_identities": group_identities(),
            "generators": {
                "delta": "(x,y)->(x,rho*y)",
                "i": "(x,y)->(rho^2/x,-y)",
                "j": "(x,y)->(-rho^2*(x+1)/(x+rho^2),((rho-1)/3)/y)",
            },
            "group": "C2 x S3",
        },
        "jacobian_decomposition": {
            "genus_C": 4, "delta_quotient_genus": 0,
            "C3_invariant_differentials": 0, "i_fixed_points": 2,
            "i_quotient_genus": 2, "i_plus_dimension": 2, "i_minus_dimension": 2,
            "H0_representation": "Std_+ direct_sum Std_-",
            "idempotents": "e_+/-=(1+/-i)/2; e_std=(2-delta-delta^2)/3; e_j=(1+j)/2",
            "elliptic_idempotent_rank": 1,
            "theorem": "Jac(C) is K-isogenous to E_+^2 x E_-^2",
            "E_minus_group_idempotent_definition": "image((1-i)/2*(2-delta-delta^2)/3*(1+j)/2 on Jac(C))",
            "Prym_description_status": "OPEN_NOT_USED_IN_THEOREM_OR_CERTIFICATE",
            "E_plus_validation_model": "Y^2=X^3+69X+22",
            "E_minus_Q_Weierstrass_model_claimed": False,
        },
        "idempotent_matrix_control": idempotent_matrix_certificate(),
        "local_factor_controls": factors,
        "extension_field_Newton_controls": extensions,
        "second_moment_resummation": {
            "curve_trace_identity": "a_C,p=2(a_+,p+a_-,p)",
            "normalized_moment": "c_p,2=-(28+8(a_+,p+a_-,p))/(p-1)",
            "w_substitution": "w=2s+1",
            "F2_definition": "F2(s)=exp(-ell_2(s)/2)",
            "theorem": "F2(s)=zeta_K(2s+1)^7*L(C/K,2s+1)*H2(s)",
            "L_curve_factorization": "L(C/K,w)=[L(E_+/K,w)L(E_-/K,w)]^2",
            "split_prime_first_log_coefficients": {"zeta_power": "14", "curve_L": "4(a_++a_-)"},
            "coefficient_ledger": {
                "c2_constant_numerator": 28,
                "c2_elliptic_trace_multiplier": 8,
                "log_moment_divisor": 2,
                "split_prime_ideals_of_norm_p": 2,
                "Dedekind_zeta_exponent": 7,
                "curve_L_exponent": 1,
            },
            "H2_holomorphic_nonzero_domain": "Re(s)>0",
            "continuation_may_have_zeros": True,
        },
        "fourth_moment_geometry": {
            "chronological_phase": "Phi_4=2*sum_i=0^7 x_i^3+sum_i=0^6 x_i*x_(i+1)+rho*x7*x0",
            "averaged_transition_matrix_used": False,
            "norm_clock": "z_p=p^(-s)",
            "direction_identity": "Z=1+#P7-#S-#Q+p*#X",
            "split_quadric_count": "#Q=(p^3+1)(p^3+p^2+p+1)=#P6+p^3",
            "char0_singular_ideal_reduced_basis_dp": groebner,
            "char0_projective_smooth": True,
            "cubic_sixfold_primitive_b6": 86,
            "complete_intersection_fivefold_b5": 168,
            "Chern_Betti_recomputation": chern_certificate(),
            "moment_identity": "C_p,4=-2-2*alpha_p/p^3-2*beta_p/p^2",
            "good_prime_bound": "|C_p,4|<=174+336*sqrt(p); c_p,4=O(p^(-1/2))",
            "all_split_prime_smoothness": False,
        },
        "exact_fourth_moment_controls": n4_controls(),
        "bad_reduction_control": {
            "p": 181, "rho": 48, "normalized_singular_points": p181_singular_points(),
            "singular_point_count": 12,
            "all_points_C_zero": True, "all_points_Q_zero": True,
            "scope": "bad only for n=4 complete-intersection reduction; C48 curve remains good at p=181",
        },
        "analytic_continuation": {
            "moment_walls": {"n1": "0", "n2_after_resummation": "0", "n3": "1/6", "n4": "1/8", "n_ge_5": "1/5"},
            "holomorphic_continuation_domain": "Re(s)>1/5",
            "continuation_may_have_zeros": True,
            "full_functional_equation": False,
            "elliptic_factor_functional_equation": True,
        },
        "tenth_order_regularized_determinant": {
            "semifinite_criterion": "X_s in L^q(M,tau) iff q*Re(s)>2",
            "tau_L10_domain": "Re(s)>1/5",
            "tau_L9_domain": "Re(s)>2/9",
            "minimal_fixed_order_on_full_domain": 10,
            "raw_germ_identity": "G=exp(-sum_(n=1)^9 ell_n/n)*Det_10^gr(I-X_s)",
            "continued_identity": "G_cont=F2_cont*exp(-sum_(1<=n<=9,n!=2) ell_n/n)*Det_10^gr(I-X_s)",
            "classical_Hilbert_Schatten_criterion": "X_s in S^q iff q*Re(s)>3",
            "classical_S10_domain": "Re(s)>3/10",
            "standard_Hilbert_trace_class_domain": "Re(s)>3",
            "unregularized_tau_trace_class_domain": "Re(s)>2",
            "Hilbert_direct_sum_compact_domain": "Re(s)>0",
            "ordinary_Fredholm_determinant_claimed": False,
            "positive_Fuglede_Kadison_equals_complex_G": False,
        },
        "route_a": {
            "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "A3_evidence": "holomorphic continuation to Re(s)>1/5 with an explicit elliptic arithmetic divisor",
            "full_FE": False, "route_b_invoked": False,
        },
        "scope": {
            "Jacobian_isogeny_theorem": True,
            "global_nonvanishing_claimed": False,
            "Riemann_hypothesis_claimed": False,
            "self_adjoint_Hilbert_Polya_operator_claimed": False,
            "all_split_n4_smoothness_claimed": False,
            "p181_contaminates_C48_curve": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()
    project = Path(__file__).resolve().parents[3]
    payload = build_payload(project)
    certificate = {"schema": SCHEMA, "payload": payload,
                   "payload_sha256": hashlib.sha256(canonical_json(payload)).hexdigest()}
    output = Path(arguments.output)
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
