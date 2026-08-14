#!/usr/bin/env python3
"""Independent, fail-closed checker for the HCS-C49 certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable


SCHEMA = "hcs-c49-certificate-v1"
GEOMETRY_BOUND = 199
CHRONOLOGY_PRIMES = (7, 13, 19, 31, 37, 43, 61)
SOURCE_HASHES = {
    "henon_dynamics/henon_mu3_normalized_trace_operator_gate/results/c47_certificate.json":
        "2c30a488f675bb68af17b2567c81946188525d007188c91b058c964c0ed7c09e",
    "henon_dynamics/henon_mu3_genus4_second_moment/results/c48_certificate.json":
        "92cd5c1079ebbaeaa27fc32e617852ae5d5989500ff3a816dd9fe306c32a32a8",
}
ROWS = (
    (7, 2, 16849, 3690, 2850, 540, 889, -140, 12, 7, -13, -20),
    (13, 3, 372151, 34308, 31110, 2718, 3367, -338, 132, 13, -1, -26),
    (19, 7, 2476612, 144990, 137922, 7677, 7429, -437, 54, 19, 11, -23),
    (31, 25, 28644031, 972099, 955266, 31869, 17794, -1085, 960, 31, -46, -35),
    (37, 26, 69332635, 1955340, 1927590, 52578, 29119, -518, -612, 37, 47, -14),
    (43, 36, 147074104, 3536235, 3502050, 83808, 36034, -2408, 3054, 43, -22, -56),
    (61, 47, 844700428, 14143644, 14080326, 233631, 67039, -2867, 3414, 61, -121, -47),
    (67, 37, 1350235657, 20538918, 20460930, 308268, 82477, -2948, 3300, 67, -109, -44),
    (73, 8, 2073041371, 28892160, 28797990, 395442, 99499, -1022, -828, 73, -97, -14),
    (79, 23, 3076927471, 39584610, 39455682, 499518, 135169, -158, -3264, 79, 131, -2),
    (97, 35, 8587399330, 89655840, 89460870, 924993, 204379, -2813, 1218, 97, 167, -29),
    (103, 56, 11592797599, 113862690, 113664930, 1106118, 208369, -2678, 1104, 103, -37, -26),
    (109, 63, 15386286637, 142679475, 142477062, 1309527, 214294, -2507, 864, 109, -214, -23),
    (127, 107, 33037802479, 262550403, 262225410, 2062989, 341122, 1651, -8928, 127, 146, 13),
    (139, 96, 51888906415, 376427430, 376025442, 2708694, 421309, -3614, 888, 139, 251, -26),
    (151, 32, 78502488832, 523816434, 523374306, 3467565, 464929, -1661, -3138, 151, 59, -11),
    (157, 12, 95389578010, 611942355, 611492550, 3901608, 474454, -6908, 7458, 157, -118, -44),
    (163, 104, 115064577928, 710849358, 710295810, 4367097, 580117, -9617, 11790, 163, 299, -59),
    (181, 48, 194264072227, 1079844372, 1079278566, 5965218, 598567, -2534, -1908, 181, -313, -14),
    (193, 84, 267785342839, 1395487080, 1394751750, 7231518, 772579, -5018, 1644, 193, 143, -26),
    (199, 106, 312077953279, 1576896498, 1576199202, 7916022, 736897, 4378, -16560, 199, -277, 22),
)
R_DESC = (
    1, -32, 432, -3200, 14192, -38960, 68992, -93280, 128846,
    -167888, 176266, -130240, 17436, -160, -31172, -5384, -4090,
    -3640, -948, -96, -1, -1,
)
H_DESC = (
    -145703718178631335347220360120867024686272,
    4661621627370767144604796374178029740390040,
    -62914860378264924680387224058288372737725792,
    465850852912341040228649592911850402799054888,
    -2064782131154121039518642129245474075586073728,
    5662673110832763888691094375596214849508927114,
    -10012578031308468751424550008795016454979710640,
    13518153111230074404047331240689196360536155048,
    -18675246318538570340741709291221417666189160704,
    24332710732466401909973892445306875547645241013,
    -25510683268342422614780199514657030683736782968,
    18791793976603365518470373078374490339615195656,
    -2408254480046539911408547106092940172750841792,
    13315783568860964077537982156297694958567245,
    4509667199840392042860762933446160050690341084,
    807275697640248175371636276793663742605516944,
    596601679510299209195816160742317568708953968,
    523424587800883936267583272067364863644382706,
    135985127526255609704800607472185819916305952,
    13732724459598184161838717552260124522717626,
    137707195104673694663949192867180643480421,
)
D_FACTORS = (
    (3, 4), (11, 1), (17, 1), (61, 1), (139, 1), (1777, 1),
    (14243, 1), (14431, 1), (14503, 1), (29303, 1), (50119, 1),
    (279359053, 1),
)
SPLIT_D = (61, 139, 1777, 14431, 14503, 50119, 279359053)


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


def fermat_count_by_sparse_dictionaries(p: int, variables: int) -> int:
    cube_histogram: dict[int, int] = {}
    for x in range(p):
        residue = x**3 % p
        cube_histogram[residue] = cube_histogram.get(residue, 0) + 1
    distribution = {0: 1}
    for _ in range(variables):
        following: dict[int, int] = {}
        for left, multiplicity in distribution.items():
            for right, other in cube_histogram.items():
                key = (left + right) % p
                following[key] = following.get(key, 0) + multiplicity * other
        distribution = following
    return (distribution[0] - 1) // (p - 1)


def root_table(p: int) -> list[list[int]]:
    table = [[0 for _ in range(p)] for _ in range(p)]
    for z in range(p):
        z3 = z**3 % p
        for coefficient in range(p):
            constant = -(z3 + coefficient * z) % p
            table[coefficient][constant] += 1
    return table


def character_table(p: int) -> list[int]:
    squares = {x * x % p for x in range(1, p)}
    return [0 if x == 0 else (1 if x in squares else -1) for x in range(p)]


def even_part(p: int, rho: int, a: int, b: int, c: int) -> int:
    inverse = pow(1 + rho, -1, p)
    x0 = (a - b + c) * inverse % p
    x2 = (a - x0) % p
    x4 = (b - x2) % p
    return (x0**3 + x2**3 + x4**3) % p


def roots_of_lower(p: int, quadratic: int, linear: int, constant: int, chi: list[int]) -> int:
    quadratic %= p
    linear %= p
    constant %= p
    if quadratic:
        return 1 + chi[(linear * linear - 4 * quadratic * constant) % p]
    if linear:
        return 1
    return p if constant == 0 else 0


@lru_cache(maxsize=None)
def intersection_count_last_nonzero(p: int, rho: int) -> tuple[int, tuple[int, int, int, int]]:
    """Independent Q charting: normalize the last nonzero u-coordinate."""
    roots = root_table(p)
    chi = character_table(p)
    inv3, inv27 = pow(3, -1, p), pow(27, -1, p)
    powers2 = [x * x % p for x in range(p)]
    powers3 = [powers2[x] * x % p for x in range(p)]

    big = 0
    for a in range(p):
        a2, a3 = a * a % p, a**3 % p
        for b in range(p):
            b2, b3 = b * b % p, b**3 % p
            constant = even_part(p, rho, a, b, 1)
            leading = (1 - b3) % p
            q2 = -3 * a * b2 % p
            q1 = -3 * a2 * b % p
            q0 = (1 - a3) % p
            if leading:
                inverse = pow(leading, -1, p)
                aa = q2 * inverse % p
                bb = q1 * inverse % p
                cc = q0 * inverse % p
                constant = constant * inverse % p
                depressed_linear = (bb - aa * aa * inv3) % p
                depressed_constant = (
                    2 * aa**3 * inv27 - aa * bb * inv3 + cc
                ) % p
                for x in range(p):
                    big += roots[depressed_linear * powers2[x] % p][
                        (depressed_constant * powers3[x] + constant) % p
                    ]
            else:
                for x in range(p):
                    big += roots_of_lower(
                        p,
                        q2 * x,
                        q1 * powers2[x],
                        q0 * powers3[x] + constant,
                        chi,
                    )

    middle = 0
    for a in range(p):
        constant = even_part(p, rho, a, 1, 0)
        coefficient = (1 - a**3) % p
        for x in range(p):
            middle += roots[0][(coefficient * powers3[x] + constant) % p]

    small_constant = even_part(p, rho, 1, 0, 0)
    small = sum(roots[0][(powers3[x] + small_constant) % p] for x in range(p))
    isotropic = fermat_count_by_sparse_dictionaries(p, 3)
    charts = (big, middle, small, isotropic)
    return sum(charts), charts


@lru_cache(maxsize=None)
def chronological_dictionary_dp(p: int, rho: int) -> int:
    """Independent dictionary DP for the literal ordered six-step phase."""
    cube = [2 * x**3 % p for x in range(p)]
    total = 0
    for start in range(p):
        states: dict[tuple[int, int], int] = {(start, cube[start]): 1}
        for _ in range(1, 6):
            following: dict[tuple[int, int], int] = {}
            for (previous, residue), multiplicity in states.items():
                for current in range(p):
                    key = (
                        current,
                        (residue + previous * current + cube[current]) % p,
                    )
                    following[key] = following.get(key, 0) + multiplicity
            states = following
        for (endpoint, residue), multiplicity in states.items():
            if (residue + rho * endpoint * start) % p == 0:
                total += multiplicity
    return total


def reverse_singularity_count(p: int, rho: int) -> int:
    """Reverse the normalized gradient recurrence, unlike the producer."""
    singular = 0
    for x5 in range(p):
        for x4 in range(p):
            x3 = (x4 * x4 - x5) % p
            x2 = (x3 * x3 - x4) % p
            x1 = (x2 * x2 - x3) % p
            x0 = (x1 * x1 - x2) % p
            if (x0 * x0 - x1 - rho * x5) % p:
                continue
            if (x5 * x5 - x4 - rho * x0) % p:
                continue
            q = (
                x0 * x1 + x1 * x2 + x2 * x3 + x3 * x4
                + x4 * x5 + rho * x5 * x0
            ) % p
            if q == 0 and any((x0, x1, x2, x3, x4, x5)):
                singular += 1
    return singular


def bareiss_determinant(matrix: list[list[int]]) -> int:
    data = [row[:] for row in matrix]
    size = len(data)
    previous = 1
    sign = 1
    for pivot_index in range(size - 1):
        if data[pivot_index][pivot_index] == 0:
            replacement = next(
                (row for row in range(pivot_index + 1, size)
                 if data[row][pivot_index]),
                None,
            )
            if replacement is None:
                return 0
            data[pivot_index], data[replacement] = data[replacement], data[pivot_index]
            sign *= -1
        pivot = data[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            entry = data[row][pivot_index]
            for column in range(pivot_index + 1, size):
                numerator = data[row][column] * pivot - entry * data[pivot_index][column]
                require(numerator % previous == 0, "Bareiss exact division")
                data[row][column] = numerator // previous
            data[row][pivot_index] = 0
        previous = pivot
    return sign * data[-1][-1]


@lru_cache(maxsize=None)
def exact_resultant_R_H_integer() -> int:
    degree_r, degree_h = len(R_DESC) - 1, len(H_DESC) - 1
    matrix = []
    for shift in range(degree_h):
        matrix.append([0] * shift + list(R_DESC) + [0] * (degree_h - shift - 1))
    for shift in range(degree_r):
        matrix.append([0] * shift + list(H_DESC) + [0] * (degree_r - shift - 1))
    return bareiss_determinant(matrix)


def expected_firewall() -> dict[str, Any]:
    denominator = 1
    for prime, exponent in D_FACTORS:
        require(is_prime(prime), f"D factor primality {prime}")
        denominator *= prime**exponent
    require(denominator == 279120457625197909574647915374957709828779, "D product")
    integral_resultant = exact_resultant_R_H_integer()
    rational_resultant = Fraction(integral_resultant * 2**21, denominator**21)
    target = 2**21 * 3**12 * 23**3
    require(rational_resultant == target, "exact rational resultant")
    split = [prime for prime, _ in D_FACTORS if prime % 3 == 1]
    inert = [prime for prime, _ in D_FACTORS if prime % 3 == 2]
    require(split == list(SPLIT_D), "split D classification")
    require(23 % 3 == 2, "23 inert")
    return {
        "normalization_for_x0_nonzero": {
            "variables": "t=x0^3 and u=x1/x0^2",
            "recurrence": [
                "A2=t*u^2-1", "B3=A2^2-u", "A4=t*B3^2-A2",
                "B5=A4^2-B3",
            ],
            "boundary_equations": ["F=u+rho*B5-1", "G=A4+rho-t*B5^2"],
            "cubic_equation": "L=1+A2^3+A4^3+t*(u^3+B3^3+B5^3)",
        },
        "elimination_polynomial_R_coefficients_descending": list(R_DESC),
        "R_degree": 21,
        "L_remainder_H_integer_coefficients_descending": list(H_DESC),
        "L_remainder_formula": "H(t)=(2/D)*H_integer(t)",
        "L_remainder_H_degree": 20,
        "recorded_resultant_Res_R_H": target,
        "recorded_resultant_factorization": {"2": 21, "3": 12, "23": 3},
        "resultant_nonzero_in_characteristic_zero": True,
        "projection_denominator": denominator,
        "projection_denominator_factorization": [
            {"prime": prime, "exponent": exponent} for prime, exponent in D_FACTORS
        ],
        "split_projection_denominator_primes": split,
        "inert_projection_denominator_primes": inert,
        "resultant_exception_23_is_inert": True,
        "x0_zero_case": "direct contradiction in characteristic not 2",
        "rho_conjugation_isomorphism": "x=(rho^2*y5,y0,y1,y2,y3,y4) maps Q_rho to Q_(rho^2) and preserves C",
        "direct_modular_Groebner_records_at_split_denominators": [
            {"prime": prime, "recorded_outcome": "EMPTY_SINGULAR_LOCUS"}
            for prime in SPLIT_D
        ],
        "checker_scope": "the independent checker recomputes Res(R,H_integer), rational scaling by (2/D)^21, integer factorization, split/inert classification, and finite controls; derivation of the triangular Groebner remainder from F,G,L is recorded as an external exact-elimination artifact",
        "all_split_prime_smoothness_promoted_by_this_certificate": False,
    }


@lru_cache(maxsize=None)
def rebuild_geometry(expected: tuple[int, ...]) -> dict[str, Any]:
    p, rho_expected, z_expected, s_expected, q_expected, x_expected, alpha_expected, beta_expected, cnum, cden, a_expected, b_expected = expected
    require(type(p) is int and is_prime(p) and p % 3 == 1, "geometry prime")
    generator = least_primitive_root(p)
    rho = pow(generator, (p - 1) // 3, p)
    require(rho == rho_expected and multiplicative_order(rho, p) == 3, "rho")
    require(pow(rho, (p - 1) // 2, p) == 1, "rho square")
    surface = fermat_count_by_sparse_dictionaries(p, 6)
    intersection, charts = intersection_count_last_nonzero(p, rho)
    quadric = (p * p + 1) * (p * p + p + 1)
    p5, p4, p3 = (sum(p**j for j in range(limit)) for limit in (6, 5, 4))
    direction = 1 + p5 - surface - quadric + p * intersection
    alpha, beta = surface - p4, p3 - intersection
    traced = Fraction(2 * direction, p * p) - 2 * p**3
    normalized = traced / ((p - 1) // 2)
    require((direction, surface, quadric, intersection, alpha, beta, traced) ==
            (z_expected, s_expected, q_expected, x_expected, alpha_expected, beta_expected, Fraction(cnum, cden)), "finite ledger")
    require(traced == -2 - Fraction(2 * alpha, p * p) - Fraction(2 * beta, p), "moment")
    require((alpha - 20 * p * p) % p == 0 and beta % p == 0, "divisibility")
    a_value, b_value = (alpha - 20 * p * p) // p, beta // p
    require((a_value, b_value) == (a_expected, b_expected), "quotient ledger")
    singular = reverse_singularity_count(p, rho)
    require(singular == 0, "finite singularity")
    return {
        "prime": p,
        "least_primitive_root": generator,
        "rho_order_3": rho,
        "rho_is_square": True,
        "real_cyclotomic_degree_d_p": (p - 1) // 2,
        "projective_counts": {
            "P5": p5,
            "Fermat_cubic_fourfold_S": surface,
            "split_quadric_Q4": quadric,
            "complete_intersection_X": intersection,
        },
        "first_nonzero_u_chart_counts_for_X": list(charts),
        "direction_formula_zero_count_Z_p_3": direction,
        "alpha_p": alpha,
        "beta_p": beta,
        "galois_traced_third_moment_C_p_3": record(traced),
        "normalized_third_moment_c_p_3": record(normalized),
        "exact_direction_moment_formula_holds": True,
        "integer_Weil_controls": {
            "alpha_squared": alpha * alpha,
            "484_p4": 484 * p**4,
            "beta_squared": beta * beta,
            "1600_p3": 1600 * p**3,
            "passes": alpha * alpha <= 484 * p**4 and beta * beta <= 1600 * p**3,
        },
        "arithmetic_divisibility_controls": {
            "alpha_minus_20p2_divisible_by_p": True,
            "beta_divisible_by_p": True,
            "a_p_quotient": a_value,
            "b_p_quotient": b_value,
            "matches_all_prime_theorem_formulas": True,
        },
        "finite_observation_only": {
            "a_p_quotient_value": a_value,
            "b_p_quotient_value": b_value,
            "finer_quotient_distribution_promoted_to_theorem": False,
        },
        "normalized_singularity_candidates_forward_recurrence": singular,
    }


def static_expected_sections() -> dict[str, Any]:
    return {
        "finite_field_model": {
            "prime_scope": "p>3 prime and p=1 mod 3",
            "rho_convention": "rho is the nontrivial cube root from the least primitive root",
            "norm_clock": "z_p=p^(-s)",
            "chronological_phase": "Phi_3=2*sum_(i=0)^5 x_i^3+x0*x1+x1*x2+x2*x3+x3*x4+x4*x5+rho*x5*x0",
            "chronological_algorithm": "literal integer DP on (start,current,phase residue) for six ordered variables, followed by the rho-twisted closure",
            "chronology_preserved": True,
            "averaged_transition_matrix_used": False,
        },
        "projective_direction_theorem": {
            "homogeneous_parts": "C=sum_(i=0)^5 x_i^3 and Q=x0*x1+x1*x2+x2*x3+x3*x4+x4*x5+rho*x5*x0",
            "radial_identity": "Phi_3(lambda*v)=lambda^2*(2*lambda*C(v)+Q(v))",
            "exact_count": "Z_p,3=1+#P5-#S-#Q+p*#X",
            "X_definition": "X=V(C,Q) in P5",
            "quadric_determinant": "det(Q_matrix)=-(rho+1)^2=-rho",
            "hyperbolic_discriminant": "(-1)^3*det=rho",
            "rho_square_reason": "an element of order 3 lies in (F_p^*)^2 when p=1 mod 3",
            "split_Q4_count": "#Q=(p^2+1)*(p^2+p+1)",
            "status": "PROVED_FOR_EVERY_SPLIT_PRIME_P_GREATER_THAN_3",
        },
        "third_moment_theorem": {
            "definitions": "alpha_p=#S-P4, beta_p=P3-#X, C_p,3=2*Z_p,3/p^2-2*p^3, c_p,3=C_p,3/d_p, d_p=(p-1)/2",
            "exact_identity": "C_p,3=-2-2*alpha_p/p^2-2*beta_p/p",
            "Fermat_Jacobi_all_split_formula": "alpha_p=20*p^2+p*a_p with a_p the rank-two Jacobi-sum trace",
            "Fermat_Jacobi_formula_all_split_theorem": True,
            "Chevalley_Warning_formula": "p divides beta_p=P3-#X(F_p)",
            "Chevalley_Warning_beta_divisibility_all_good_split_theorem": True,
            "refined_identity": "C_p,3=-42-2*a_p/p-2*b_p",
            "Fermat_fourfold_primitive_rank": 22,
            "Fermat_Weil_bound": "|alpha_p|<=22*p^2",
            "good_reduction_Fano_Weil_bound": "|beta_p|<=40*p^(3/2)",
            "derived_bound": "|C_p,3|<=46+80*sqrt(p)",
            "normalized_bound": "|c_p,3|<=(92+160*sqrt(p))/(p-1)=O(p^(-1/2))",
            "bound_scope": "split primes of good reduction; finite exceptional characteristics are firewalled separately",
            "finer_quotient_distribution_used_in_theorem": False,
        },
        "analytic_upgrade": {
            "first_moment": "c_p,1=-12/(p-1)=O(p^-1)",
            "second_moment": "c_p,2=O(p^-1/2) from HCS-C48",
            "third_moment": "c_p,3=O(p^-1/2) at good split primes",
            "generic_higher_bound": "|c_p,n|<=4*4^n for n>=4",
            "absolute_convergence_abscissae": {
                "n_equals_1": record(Fraction(0)),
                "n_equals_2": record(Fraction(1, 4)),
                "n_equals_3": record(Fraction(1, 6)),
                "n_at_least_4_uniform_wall": record(Fraction(1, 4)),
                "combined_log_Euler_germ": record(Fraction(1, 4)),
            },
            "normal_convergence": "the normalized logarithmic Euler series converges locally uniformly for Re(s)>1/4",
            "Euler_germ": "canonical normalized Euler product is holomorphic and nonzero for Re(s)>1/4",
            "first_active_unresolved_wall": "n=2 and n=4",
            "continuation_through_one_fourth": "NOT_PROVED",
        },
        "eighth_order_regularized_determinant": {
            "inherited_semifinite_ideal_criterion": "X_s in L^q(M,tau) iff q*Re(s)>2",
            "tau_L8_domain": "Re(s)>1/4",
            "tau_L7_domain": "Re(s)>2/7",
            "counterterms": "ell_n(s)=sum_p c_p,n*p^(-n*s), n=1,2,3,4,5,6,7",
            "det8_definition": "det8_tau_gr(I-X_s)=exp(-sum_(n>=8) str_tau(X_s^n)/n)",
            "exact_factorization": "G(s)=exp(-sum_(n=1)^7 ell_n(s)/n)*det8_tau_gr(I-X_s)",
            "minimal_fixed_tau_Lq_order_on_full_domain": 8,
            "unregularized_tau_trace_class_domain": "Re(s)>2",
            "classical_Hilbert_trace_identity": "Tr_H(|X_s|^q)=sum_(p=1 mod 3) d_p*((8p+4)/3)*p^(-q*Re(s))",
            "classical_Schatten_criterion": "X_s in classical S^q(H) iff q*Re(s)>3",
            "classical_trace_class_domain": "Re(s)>3",
            "classical_determinant_warning": "the classical Hilbert trace does not implement the field-degree-normalized root G",
            "determinant_category": "semifinite tau-associated graded regularization, not a classical Fredholm determinant",
            "counterterm_status": "seven source-native chronological Galois-supertrace moments, not fitted prefactors",
        },
        "decisions": {
            "third_moment_arithmetic_structure": "GENERIC_SMOOTH_FANO_THREEFOLD_WITH_B3_40",
            "all_split_prime_smoothness": "NOT_CLAIMED",
            "normalized_Euler_germ_domain": "IMPROVED_FROM_RE_S_GT_ONE_THIRD_TO_RE_S_GT_ONE_FOURTH",
            "eighth_order_regularized_graded_determinant": "CONSTRUCTED_IN_SEMIFINITE_TAU_CATEGORY_ON_RE_S_GT_ONE_FOURTH",
            "classical_Fredholm_determinant_on_that_domain": "NOT_CLAIMED",
            "next_large_gate": "RESOLVE_THE_N4_ARITHMETIC_WALL_OR_BUILD_A_GLOBAL_FUNCTIONAL_EQUATION_MECHANISM",
        },
        "route_a": {
            "A1": "A1_WEAK",
            "A2": "A2_ANALYTIC_DETERMINANT",
            "A2_reason": "the exact third-moment Fano cancellation yields a canonical tau-Det8 realization and a nonzero Euler germ on Re(s)>1/4",
            "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "A3_reason": "the arithmetic cohomology improves the analytic half-plane, but no continuation, functional equation, Gamma factor, or Riemann divisor is proved",
            "A4": "A4_NATURAL_QUANTIZATION",
            "overall": "ROUTE_A_EXPLORATORY",
            "scoped_status": "ROUTE_A_EXPLORATORY_FANO_THREEFOLD_QUARTER_ABSCISSA",
            "route_b_invocation_allowed": False,
        },
        "scope": {
            "rh_proved": False,
            "hilbert_polya_self_adjoint_operator_constructed": False,
            "global_meromorphic_continuation_claimed": False,
            "continuation_through_Re_s_one_fourth_claimed": False,
            "functional_equation_claimed": False,
            "gamma_factor_claimed": False,
            "riemann_divisor_claimed": False,
            "riemann_zero_data_used": False,
            "all_split_prime_smoothness_claimed": False,
            "finite_smoothness_controls_used_as_all_prime_proof": False,
            "unregularized_tau_L1_determinant_claimed_on_Re_s_gt_one_fourth": False,
            "classical_Fredholm_determinant_claimed_on_Re_s_gt_one_fourth": False,
            "classical_Schatten_criterion_claimed_qRe_s_gt_2": False,
            "fermat_Jacobi_formula_all_split_theorem": True,
            "chevalley_Warning_beta_divisibility_all_good_split_theorem": True,
            "finer_quotient_ledger_distribution_promoted_to_theorem": False,
        },
    }


def expected_generic_theorem() -> dict[str, Any]:
    return {
        "ambient": "P5 over Q(rho)",
        "complete_intersection_degrees": [2, 3],
        "generic_characteristic_zero_smooth": True,
        "canonical_bundle_by_adjunction": "K_X=O_X(-1)",
        "classification": "smooth (2,3) Fano threefold",
        "total_chern_class_through_degree_3": "1+H+4*H^2-6*H^3",
        "degree_H3": 6,
        "topological_Euler_characteristic": -36,
        "betti_numbers_except_middle": {"b0": 1, "b1": 0, "b2": 1, "b4": 1, "b5": 0, "b6": 1},
        "middle_betti_number_b3": 40,
        "hodge_number_h12": 20,
        "finite_characteristic_firewall": expected_firewall(),
        "all_split_prime_smoothness_status": "NOT_PROMOTED_IN_HCS_C49",
    }


def audit_certificate(certificate: dict[str, Any], project_root: Path) -> tuple[list[dict[str, str]], bool]:
    gates: list[dict[str, str]] = []

    def run(name: str, check: Callable[[], None]) -> None:
        try:
            check()
        except GateFailure as exc:
            gates.append({"gate": name, "status": "FAIL", "detail": str(exc)})
        except Exception as exc:  # fail closed, but expose implementation errors
            gates.append({"gate": name, "status": "ERROR", "detail": f"{type(exc).__name__}: {exc}"})
        else:
            gates.append({"gate": name, "status": "PASS", "detail": "exact check passed"})

    def schema_gate() -> None:
        require(type(certificate) is dict, "certificate type")
        require(set(certificate) == {"schema", "payload", "payload_sha256"}, "top-level keys")
        require(certificate["schema"] == SCHEMA, "schema")
        payload = certificate["payload"]
        require(type(payload) is dict, "payload type")
        require(set(payload) == {
            "material_passport", "source_lock", "finite_field_model",
            "projective_direction_theorem", "generic_fano_threefold_theorem",
            "third_moment_theorem", "analytic_upgrade",
            "eighth_order_regularized_determinant", "exact_geometry_controls",
            "exact_chronology_controls", "aggregate_control", "decisions",
            "route_a", "scope",
        }, "payload keys")
        require(strict_equal(payload["material_passport"], {
            "candidate_id": "HCS-C49",
            "project": "henon_mu3_fano_threefold_third_moment",
            "ai_assistance_disclosed": True,
            "evidence_policy": "generic algebraic theorem, exact projective controls through 199, and exact literal chronology through 61; no Riemann-zero data",
            "freeze_status": "RELEASE_CANDIDATE_CODE_RESULTS_DOCS_AND_PAPER_PRESENT",
        }), "passport")

    def digest_gate() -> None:
        require(type(certificate["payload_sha256"]) is str, "digest type")
        actual = hashlib.sha256(canonical_json(certificate["payload"])).hexdigest()
        require(certificate["payload_sha256"] == actual, "payload digest")

    def source_gate() -> None:
        repository = project_root.parents[1]
        expected = []
        for relative, frozen in SOURCE_HASHES.items():
            actual = sha256_file(repository / relative)
            require(actual == frozen, f"source changed {relative}")
            expected.append({"path": relative, "sha256": actual})
        require(strict_equal(certificate["payload"]["source_lock"], expected), "source lock")

    geometry_expected: list[dict[str, Any]] = []

    def model_and_prime_gate() -> None:
        static = static_expected_sections()
        require(strict_equal(certificate["payload"]["finite_field_model"], static["finite_field_model"]), "finite model")
        require([row[0] for row in ROWS] == split_primes_through(GEOMETRY_BOUND), "complete split prime ledger")

    def projective_gate() -> None:
        static = static_expected_sections()
        geometry_expected[:] = [rebuild_geometry(row) for row in ROWS]
        require(strict_equal(certificate["payload"]["projective_direction_theorem"], static["projective_direction_theorem"]), "direction theorem")
        require(strict_equal(certificate["payload"]["exact_geometry_controls"], geometry_expected), "independent geometry replay")

    def smoothness_and_fano_gate() -> None:
        require(strict_equal(certificate["payload"]["generic_fano_threefold_theorem"], expected_generic_theorem()), "Fano theorem/firewall")
        require(all(row["normalized_singularity_candidates_forward_recurrence"] == 0 for row in geometry_expected), "finite singularity controls")

    def chronology_gate() -> None:
        by_prime = {row["prime"]: row for row in geometry_expected}
        expected = []
        for p in CHRONOLOGY_PRIMES:
            row = by_prime[p]
            zero_count = chronological_dictionary_dp(p, row["rho_order_3"])
            require(zero_count == row["direction_formula_zero_count_Z_p_3"], f"chronology p={p}")
            expected.append({
                "prime": p,
                "rho_order_3": row["rho_order_3"],
                "literal_six_step_DP_zero_count_Z_p_3": zero_count,
                "direction_count_Z_p_3": row["direction_formula_zero_count_Z_p_3"],
                "counts_match": True,
            })
        require(strict_equal(certificate["payload"]["exact_chronology_controls"], expected), "chronology controls")

    def moment_gate() -> None:
        expected = static_expected_sections()["third_moment_theorem"]
        require(strict_equal(certificate["payload"]["third_moment_theorem"], expected), "third moment theorem")
        require(all(row["exact_direction_moment_formula_holds"] for row in geometry_expected), "moment controls")
        require(all(row["arithmetic_divisibility_controls"]["matches_all_prime_theorem_formulas"] for row in geometry_expected), "divisibility controls")

    def analytic_gate() -> None:
        expected = static_expected_sections()["analytic_upgrade"]
        require(strict_equal(certificate["payload"]["analytic_upgrade"], expected), "one-fourth analytic upgrade")

    def determinant_gate() -> None:
        expected = static_expected_sections()["eighth_order_regularized_determinant"]
        require(strict_equal(certificate["payload"]["eighth_order_regularized_determinant"], expected), "tau Det8")

    def aggregate_gate() -> None:
        chronology = certificate["payload"]["exact_chronology_controls"]
        expected = {
            "geometry_bound_inclusive": GEOMETRY_BOUND,
            "geometry_control_primes": [row[0] for row in ROWS],
            "number_of_geometry_controls": len(ROWS),
            "chronology_control_primes": list(CHRONOLOGY_PRIMES),
            "number_of_chronology_controls": len(CHRONOLOGY_PRIMES),
            "all_direction_moment_identities_hold": True,
            "all_chronology_counts_match_direction_counts": all(row["counts_match"] for row in chronology),
            "all_integer_Weil_controls_pass": all(row["integer_Weil_controls"]["passes"] for row in geometry_expected),
            "all_finite_singularity_controls_empty": all(row["normalized_singularity_candidates_forward_recurrence"] == 0 for row in geometry_expected),
            "all_Fermat_Jacobi_divisibility_controls_hold": all(row["arithmetic_divisibility_controls"]["alpha_minus_20p2_divisible_by_p"] for row in geometry_expected),
            "all_Chevalley_Warning_divisibility_controls_hold": all(row["arithmetic_divisibility_controls"]["beta_divisible_by_p"] for row in geometry_expected),
            "finite_observation_warning": "the theorem-level divisibilities are proved separately; only the displayed quotient values and any finer distribution inferred from this ledger remain finite observations",
            "C_p_3_ledger": [row["galois_traced_third_moment_C_p_3"] for row in geometry_expected],
            "c_p_3_ledger": [row["normalized_third_moment_c_p_3"] for row in geometry_expected],
        }
        require(strict_equal(certificate["payload"]["aggregate_control"], expected), "aggregate")

    def decisions_gate() -> None:
        expected = static_expected_sections()
        require(strict_equal(certificate["payload"]["decisions"], expected["decisions"]), "decisions")

    def route_scope_gate() -> None:
        expected = static_expected_sections()
        require(strict_equal(certificate["payload"]["route_a"], expected["route_a"]), "Route A")
        require(strict_equal(certificate["payload"]["scope"], expected["scope"]), "scope")

    run("G01_SCHEMA_TYPES_AND_PASSPORT", schema_gate)
    run("G02_PAYLOAD_DIGEST", digest_gate)
    run("G03_FROZEN_SOURCE_LOCK", source_gate)
    run("G04_MODEL_AND_COMPLETE_PRIME_SCOPE", model_and_prime_gate)
    run("G05_PROJECTIVE_DIRECTION_AND_LAST_CHART_REPLAY", projective_gate)
    run("G06_GENERIC_FANO_AND_EXACT_RESULTANT_FIREWALL", smoothness_and_fano_gate)
    run("G07_LITERAL_SIX_STEP_CHRONOLOGY_DICTIONARY_DP", chronology_gate)
    run("G08_THIRD_MOMENT_JACOBI_CHEVALLEY_WEIL", moment_gate)
    run("G09_ONE_FOURTH_ANALYTIC_UPGRADE", analytic_gate)
    run("G10_MINIMAL_SEMIFINITE_TAU_DET8", determinant_gate)
    run("G11_AGGREGATE_LEDGERS", aggregate_gate)
    run("G12_DECISIONS", decisions_gate)
    run("G13_ROUTE_A_AND_SCOPE_FIREWALL", route_scope_gate)
    return gates, all(row["status"] == "PASS" for row in gates)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate")
    parser.add_argument("--output")
    arguments = parser.parse_args()
    path = Path(arguments.certificate)
    project_root = Path(__file__).resolve().parents[1]
    certificate = json.loads(path.read_text(encoding="utf-8"))
    gates, passed = audit_certificate(certificate, project_root)
    report = {
        "schema": "hcs-c49-independent-check-v1",
        "certificate_sha256": sha256_file(path),
        "gates": gates,
        "passed": passed,
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if arguments.output:
        Path(arguments.output).write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
