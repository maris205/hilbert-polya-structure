#!/usr/bin/env python3
"""Produce the exact HCS-C49 third-moment/Fano-threefold certificate.

The program has two deliberately separate finite-field lanes.

* ``chronological_zero_count`` is a literal six-step integer dynamic program.
  It retains the start point, current endpoint, and phase residue.  No edge or
  transition matrix is averaged.
* ``intersection_count_first_nonzero`` counts the projective complete
  intersection S cap Q using disjoint charts on the split quadric.  It is an
  independent direction-count control and never calls the chronological DP.

All finite divisibility patterns are serialized as observations only.  The
generic smoothness claim is kept separate from the finite-field controls.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


SCHEMA = "hcs-c49-certificate-v1"
GEOMETRY_BOUND = 199
CHRONOLOGY_PRIMES = (7, 13, 19, 31, 37, 43, 61)
EXPECTED_SOURCE_HASHES = {
    "henon_dynamics/henon_mu3_normalized_trace_operator_gate/results/c47_certificate.json":
        "2c30a488f675bb68af17b2567c81946188525d007188c91b058c964c0ed7c09e",
    "henon_dynamics/henon_mu3_genus4_second_moment/results/c48_certificate.json":
        "92cd5c1079ebbaeaa27fc32e617852ae5d5989500ff3a816dd9fe306c32a32a8",
}

# Exact finite ledger, frozen only as a regression oracle.  Every entry is
# independently recomputed below.  Columns are p,rho,Z,S,Q,X,alpha,beta,Cnum,
# Cden, a_CM_observed,b_X_observed.
EXPECTED_ROWS = (
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

R_COEFFICIENTS_DESCENDING = (
    1, -32, 432, -3200, 14192, -38960, 68992, -93280, 128846,
    -167888, 176266, -130240, 17436, -160, -31172, -5384, -4090,
    -3640, -948, -96, -1, -1,
)
H_INTEGER_COEFFICIENTS_DESCENDING = (
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
H_COMMON_DENOMINATOR = 279120457625197909574647915374957709828779
PROJECTION_DENOMINATOR_FACTORS = (
    (3, 4), (11, 1), (17, 1), (61, 1), (139, 1), (1777, 1),
    (14243, 1), (14431, 1), (14503, 1), (29303, 1), (50119, 1),
    (279359053, 1),
)
SPLIT_DENOMINATOR_PRIMES = (61, 139, 1777, 14431, 14503, 50119, 279359053)


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


def cyclic_convolution(left: list[int], right: list[int]) -> list[int]:
    p = len(left)
    answer = [0] * p
    nonzero_right = [(index, value) for index, value in enumerate(right) if value]
    for a, multiplicity in enumerate(left):
        if multiplicity:
            for b, other in nonzero_right:
                answer[(a + b) % p] += multiplicity * other
    return answer


def fermat_projective_count(p: int, variables: int) -> int:
    cube_histogram = [0] * p
    for x in range(p):
        cube_histogram[pow(x, 3, p)] += 1
    distribution = [0] * p
    distribution[0] = 1
    for _ in range(variables):
        distribution = cyclic_convolution(distribution, cube_histogram)
    return (distribution[0] - 1) // (p - 1)


def depressed_cubic_root_table(p: int) -> list[list[int]]:
    """Return R[P][Q]=#{z:z^3+P*z+Q=0}."""
    table = [[0] * p for _ in range(p)]
    cubes = [pow(z, 3, p) for z in range(p)]
    for coefficient in range(p):
        row = table[coefficient]
        for z in range(p):
            row[(-cubes[z] - coefficient * z) % p] += 1
    return table


def quadratic_character_table(p: int) -> list[int]:
    answer = [-1] * p
    answer[0] = 0
    for x in range(1, p):
        answer[x * x % p] = 1
    return answer


def even_cubic(p: int, rho: int, a: int, b: int, c: int) -> int:
    """Cubic in even coordinates after u=(x0+x2,x2+x4,x4+rho*x0)."""
    x0 = (c - b + a) * pow(1 + rho, -1, p) % p
    x2 = (a - x0) % p
    x4 = (b - a + x0) % p
    return (pow(x0, 3, p) + pow(x2, 3, p) + pow(x4, 3, p)) % p


def lower_polynomial_root_count(
    p: int, bb: int, cc: int, dd: int, chi: list[int]
) -> int:
    """Count roots of bb*z^2+cc*z+dd when the cubic term vanishes."""
    bb %= p
    cc %= p
    dd %= p
    if bb:
        return 1 + chi[(cc * cc - 4 * bb * dd) % p]
    if cc:
        return 1
    return p if dd == 0 else 0


def intersection_count_first_nonzero(
    p: int, rho: int
) -> tuple[int, tuple[int, int, int, int]]:
    """Count X=S cap Q by the first nonzero coordinate of u.

    The linear change sends Q to u0*v0+u1*v1+u2*v2.  General cubic
    equations are depressed and queried in an exact root table, giving
    O(p^3) time and O(p^2) memory.
    """
    roots = depressed_cubic_root_table(p)
    chi = quadratic_character_table(p)
    inv3 = pow(3, -1, p)
    inv27 = pow(27, -1, p)
    y2 = [y * y % p for y in range(p)]
    y3 = [y2[y] * y % p for y in range(p)]

    chart0 = 0
    for b in range(p):
        b2, b3 = b * b % p, pow(b, 3, p)
        for c in range(p):
            c2, c3 = c * c % p, pow(c, 3, p)
            constant = even_cubic(p, rho, 1, b, c)
            leading = (1 - c3) % p
            b1 = -3 * b * c2 % p
            c2coefficient = -3 * b2 * c % p
            d3 = (1 - b3) % p
            if leading:
                inverse = pow(leading, -1, p)
                aa = b1 * inverse % p
                bb = c2coefficient * inverse % p
                cc = d3 * inverse % p
                constant = constant * inverse % p
                p_coefficient = (bb - aa * aa * inv3) % p
                q_coefficient = (
                    2 * aa * aa * aa * inv27 - aa * bb * inv3 + cc
                ) % p
                for y in range(p):
                    chart0 += roots[p_coefficient * y2[y] % p][
                        (q_coefficient * y3[y] + constant) % p
                    ]
            else:
                for y in range(p):
                    chart0 += lower_polynomial_root_count(
                        p,
                        b1 * y,
                        c2coefficient * y2[y],
                        d3 * y3[y] + constant,
                        chi,
                    )

    chart1 = 0
    for c in range(p):
        leading = (1 - pow(c, 3, p)) % p
        constant = even_cubic(p, rho, 0, 1, c)
        if leading:
            inverse = pow(leading, -1, p)
            for y in range(p):
                chart1 += roots[0][(y3[y] + constant) * inverse % p]
        else:
            for y in range(p):
                chart1 += p if (y3[y] + constant) % p == 0 else 0

    chart2 = 0
    constant = even_cubic(p, rho, 0, 0, 1)
    for y in range(p):
        chart2 += roots[0][(y3[y] + constant) % p]

    chart3 = fermat_projective_count(p, 3)
    charts = (chart0, chart1, chart2, chart3)
    return sum(charts), charts


def chronological_zero_count(p: int, rho: int) -> int:
    """Literal integer DP for the ordered six-variable phase."""
    cubes = [2 * pow(x, 3, p) % p for x in range(p)]
    total = 0
    for start in range(p):
        states = [[0] * p for _ in range(p)]
        states[start][cubes[start]] = 1
        for _ in range(1, 6):
            following = [[0] * p for _ in range(p)]
            for previous in range(p):
                shifts = [
                    (previous * current + cubes[current]) % p
                    for current in range(p)
                ]
                for residue, multiplicity in enumerate(states[previous]):
                    if multiplicity:
                        for current, shift in enumerate(shifts):
                            following[current][(residue + shift) % p] += multiplicity
            states = following
        for endpoint in range(p):
            total += states[endpoint][(-rho * endpoint * start) % p]
    return total


def normalized_singularity_count_forward(p: int, rho: int) -> int:
    """Finite control for singular points, using the normalized gradient recurrence."""
    singular = 0
    for x0 in range(p):
        for x1 in range(p):
            x2 = (x1 * x1 - x0) % p
            x3 = (x2 * x2 - x1) % p
            x4 = (x3 * x3 - x2) % p
            x5 = (x4 * x4 - x3) % p
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


def build_geometry_control(expected: tuple[int, ...]) -> dict[str, Any]:
    p, expected_rho, expected_z, expected_s, expected_q, expected_x, expected_alpha, expected_beta, cnum, cden, expected_a, expected_b = expected
    generator = primitive_root(p)
    rho = pow(generator, (p - 1) // 3, p)
    assert rho == expected_rho and rho != 1 and pow(rho, 3, p) == 1
    assert pow(rho, (p - 1) // 2, p) == 1

    surface = fermat_projective_count(p, 6)
    quadric = (p * p + 1) * (p * p + p + 1)
    intersection, charts = intersection_count_first_nonzero(p, rho)
    p5 = sum(p**power for power in range(6))
    p4 = sum(p**power for power in range(5))
    p3 = sum(p**power for power in range(4))
    direction = 1 + p5 - surface - quadric + p * intersection
    alpha = surface - p4
    beta = p3 - intersection
    traced = Fraction(2 * direction, p * p) - 2 * p**3
    normalized = traced / ((p - 1) // 2)
    formula = -2 - Fraction(2 * alpha, p * p) - Fraction(2 * beta, p)
    assert (
        direction, surface, quadric, intersection, alpha, beta, traced
    ) == (
        expected_z, expected_s, expected_q, expected_x,
        expected_alpha, expected_beta, Fraction(cnum, cden),
    )
    assert traced == formula

    alpha_divisible = (alpha - 20 * p * p) % p == 0
    beta_divisible = beta % p == 0
    a_observed = (alpha - 20 * p * p) // p
    b_observed = beta // p
    assert alpha_divisible and beta_divisible
    assert (a_observed, b_observed) == (expected_a, expected_b)
    assert alpha * alpha <= 22 * 22 * p**4
    assert beta * beta <= 40 * 40 * p**3
    singular_count = normalized_singularity_count_forward(p, rho)
    assert singular_count == 0

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
        "galois_traced_third_moment_C_p_3": fraction_record(traced),
        "normalized_third_moment_c_p_3": fraction_record(normalized),
        "exact_direction_moment_formula_holds": traced == formula,
        "integer_Weil_controls": {
            "alpha_squared": alpha * alpha,
            "484_p4": 22 * 22 * p**4,
            "beta_squared": beta * beta,
            "1600_p3": 40 * 40 * p**3,
            "passes": True,
        },
        "arithmetic_divisibility_controls": {
            "alpha_minus_20p2_divisible_by_p": alpha_divisible,
            "beta_divisible_by_p": beta_divisible,
            "a_p_quotient": a_observed,
            "b_p_quotient": b_observed,
            "matches_all_prime_theorem_formulas": True,
        },
        "finite_observation_only": {
            "a_p_quotient_value": a_observed,
            "b_p_quotient_value": b_observed,
            "finer_quotient_distribution_promoted_to_theorem": False,
        },
        "normalized_singularity_candidates_forward_recurrence": singular_count,
    }


def source_lock(project_root: Path) -> list[dict[str, str]]:
    repository = project_root.parents[1]
    answer = []
    for relative, expected_hash in EXPECTED_SOURCE_HASHES.items():
        source = repository / relative
        actual = sha256_file(source)
        if actual != expected_hash:
            raise AssertionError(f"source lock changed: {relative}: {actual}")
        answer.append({"path": relative, "sha256": actual})
    return answer


def elimination_firewall() -> dict[str, Any]:
    resultant = 2**21 * 3**12 * 23**3
    denominator = 1
    for prime, exponent in PROJECTION_DENOMINATOR_FACTORS:
        denominator *= prime**exponent
    split = [prime for prime, _ in PROJECTION_DENOMINATOR_FACTORS if prime % 3 == 1]
    inert = [prime for prime, _ in PROJECTION_DENOMINATOR_FACTORS if prime % 3 == 2]
    assert split == list(SPLIT_DENOMINATOR_PRIMES)
    assert 23 % 3 == 2
    assert denominator == H_COMMON_DENOMINATOR
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
        "elimination_polynomial_R_coefficients_descending": list(R_COEFFICIENTS_DESCENDING),
        "R_degree": 21,
        "L_remainder_H_integer_coefficients_descending": list(
            H_INTEGER_COEFFICIENTS_DESCENDING
        ),
        "L_remainder_formula": "H(t)=(2/D)*H_integer(t)",
        "L_remainder_H_degree": 20,
        "recorded_resultant_Res_R_H": resultant,
        "recorded_resultant_factorization": {"2": 21, "3": 12, "23": 3},
        "resultant_nonzero_in_characteristic_zero": True,
        "projection_denominator": denominator,
        "projection_denominator_factorization": [
            {"prime": prime, "exponent": exponent}
            for prime, exponent in PROJECTION_DENOMINATOR_FACTORS
        ],
        "split_projection_denominator_primes": split,
        "inert_projection_denominator_primes": inert,
        "resultant_exception_23_is_inert": True,
        "x0_zero_case": "direct contradiction in characteristic not 2",
        "rho_conjugation_isomorphism": "x=(rho^2*y5,y0,y1,y2,y3,y4) maps Q_rho to Q_(rho^2) and preserves C",
        "direct_modular_Groebner_records_at_split_denominators": [
            {"prime": prime, "recorded_outcome": "EMPTY_SINGULAR_LOCUS"}
            for prime in SPLIT_DENOMINATOR_PRIMES
        ],
        "checker_scope": "the independent checker recomputes Res(R,H_integer), rational scaling by (2/D)^21, integer factorization, split/inert classification, and finite controls; derivation of the triangular Groebner remainder from F,G,L is recorded as an external exact-elimination artifact",
        "all_split_prime_smoothness_promoted_by_this_certificate": False,
    }


def build_payload(project_root: Path) -> dict[str, Any]:
    primes = split_primes_through(GEOMETRY_BOUND)
    assert primes == tuple(row[0] for row in EXPECTED_ROWS)
    geometry = [build_geometry_control(row) for row in EXPECTED_ROWS]
    chronology = []
    by_prime = {row["prime"]: row for row in geometry}
    for p in CHRONOLOGY_PRIMES:
        row = by_prime[p]
        zero_count = chronological_zero_count(p, row["rho_order_3"])
        assert zero_count == row["direction_formula_zero_count_Z_p_3"]
        chronology.append({
            "prime": p,
            "rho_order_3": row["rho_order_3"],
            "literal_six_step_DP_zero_count_Z_p_3": zero_count,
            "direction_count_Z_p_3": row["direction_formula_zero_count_Z_p_3"],
            "counts_match": True,
        })

    return {
        "material_passport": {
            "candidate_id": "HCS-C49",
            "project": "henon_mu3_fano_threefold_third_moment",
            "ai_assistance_disclosed": True,
            "evidence_policy": "generic algebraic theorem, exact projective controls through 199, and exact literal chronology through 61; no Riemann-zero data",
            "freeze_status": "RELEASE_CANDIDATE_CODE_RESULTS_DOCS_AND_PAPER_PRESENT",
        },
        "source_lock": source_lock(project_root),
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
        "generic_fano_threefold_theorem": {
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
            "finite_characteristic_firewall": elimination_firewall(),
            "all_split_prime_smoothness_status": "NOT_PROMOTED_IN_HCS_C49",
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
                "n_equals_1": fraction_record(Fraction(0)),
                "n_equals_2": fraction_record(Fraction(1, 4)),
                "n_equals_3": fraction_record(Fraction(1, 6)),
                "n_at_least_4_uniform_wall": fraction_record(Fraction(1, 4)),
                "combined_log_Euler_germ": fraction_record(Fraction(1, 4)),
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
        "exact_geometry_controls": geometry,
        "exact_chronology_controls": chronology,
        "aggregate_control": {
            "geometry_bound_inclusive": GEOMETRY_BOUND,
            "geometry_control_primes": list(primes),
            "number_of_geometry_controls": len(geometry),
            "chronology_control_primes": list(CHRONOLOGY_PRIMES),
            "number_of_chronology_controls": len(chronology),
            "all_direction_moment_identities_hold": all(row["exact_direction_moment_formula_holds"] for row in geometry),
            "all_chronology_counts_match_direction_counts": all(row["counts_match"] for row in chronology),
            "all_integer_Weil_controls_pass": all(row["integer_Weil_controls"]["passes"] for row in geometry),
            "all_finite_singularity_controls_empty": all(row["normalized_singularity_candidates_forward_recurrence"] == 0 for row in geometry),
            "all_Fermat_Jacobi_divisibility_controls_hold": all(row["arithmetic_divisibility_controls"]["alpha_minus_20p2_divisible_by_p"] for row in geometry),
            "all_Chevalley_Warning_divisibility_controls_hold": all(row["arithmetic_divisibility_controls"]["beta_divisible_by_p"] for row in geometry),
            "finite_observation_warning": "the theorem-level divisibilities are proved separately; only the displayed quotient values and any finer distribution inferred from this ledger remain finite observations",
            "C_p_3_ledger": [row["galois_traced_third_moment_C_p_3"] for row in geometry],
            "c_p_3_ledger": [row["normalized_third_moment_c_p_3"] for row in geometry],
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
            "fermat_Jacobi_formula_all_split_theorem": True,
            "chevalley_Warning_beta_divisibility_all_good_split_theorem": True,
            "finer_quotient_ledger_distribution_promoted_to_theorem": False,
            "finite_smoothness_controls_used_as_all_prime_proof": False,
            "unregularized_tau_L1_determinant_claimed_on_Re_s_gt_one_fourth": False,
            "classical_Fredholm_determinant_claimed_on_Re_s_gt_one_fourth": False,
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
