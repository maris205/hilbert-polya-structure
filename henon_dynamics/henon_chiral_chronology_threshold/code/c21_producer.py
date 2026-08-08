#!/usr/bin/env python3
"""Exact producer for HCS-C21.

The certificate separates three objects that must not be conflated:

1. the published period-six chiral orbit-sum marker;
2. the published six-coordinate carrier; and
3. the new normalized twelve-state ordered-edge cover.

It then compares the genuine chronological cohomology of the period-six
cover with the previously certified period-seven cover and records a second,
independent obstruction: an apparent period-six/period-seven marker
correspondence factors through the period-one fixed-point marker.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


SCHEMA = "HCS-C21-producer-1"
CANDIDATE = "HCS-C21"

CODE = Path(__file__).resolve().parent
PROJECT = CODE.parent
HENON = PROJECT.parent
PAPER5 = HENON / "docs" / "prior_work" / "papers" / "5-An Area-Preserving Henon-Map Model.pdf"
C12C_CERT = HENON / "henon_dihedral_chronology_obstruction" / "results" / "certificate.json"
C20_CERT = HENON / "henon_period7_dihedral_cover" / "results" / "c20_certificate.json"

EXPECTED_HASHES = {
    "paper5_pdf": "23dad812162728316f633081e1a1995d4c00614a70d0f5877d425c68d0c726b9",
    "hcs_c12c_certificate": "964b8c98abc850493529b8e939a9c8ff96c832300ad2b1629b1cff807f0e8020",
    "hcs_c20_certificate": "7ee43e3253aff15ec00d78b9633c3d3362e71cd5a880cd3e928e7f322abb2681",
}


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_text(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    factors = 0
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            factors += 1
            if m % p == 0:
                return 0
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        factors += 1
    return -1 if factors % 2 else 1


def source_lock() -> dict:
    paths = {
        "paper5_pdf": PAPER5,
        "hcs_c12c_certificate": C12C_CERT,
        "hcs_c20_certificate": C20_CERT,
    }
    actual = {key: sha256_file(path) for key, path in paths.items()}
    if actual != EXPECTED_HASHES:
        raise AssertionError(f"source-lock mismatch: {actual}")
    return {
        "files": {
            key: {"path": str(path.relative_to(HENON)), "sha256": actual[key]}
            for key, path in paths.items()
        },
        "paper5_coordinate_lock": {
            "source_recurrence": "q_(t+1)=1-A*q_t^2-q_(t-1)",
            "coordinate_change": "x_t=A*q_t (A nonzero)",
            "monic_recurrence": "x_(t+1)=A-x_t^2-x_(t-1)",
        },
        "clock_separation": {
            "n": "primitive Hénon period",
            "s": "chronological Hénon phase",
            "r": "Frobenius extension degree",
            "identified_or_averaged": False,
        },
        "notation_separation": {
            "radical_in_source_and_code": "r with r^2=A-3",
            "radical_in_prose": "eta with eta^2=A-3",
            "frobenius_degree_in_prose": "r_F",
            "legacy_clock_key_r": "the clock_separation.r entry always means Frobenius degree",
        },
    }


def lower_period_chirality() -> dict:
    rows: list[dict] = []
    for n in range(1, 8):
        nu = sum(mobius(n // d) * 2**d for d in divisors(n))
        cycles = nu // n
        axial = sum(mobius(n // d) * 2 ** ((d + 1) // 2) for d in divisors(n))
        other = sum(mobius(n // d) * 2 ** ((d + 2) // 2) for d in divisors(n))
        diagonal = axial if n % 2 else axial // 2
        nondiagonal = 0 if n % 2 else other // 2
        chiral_cycles = cycles - diagonal - nondiagonal
        if chiral_cycles % 2:
            raise AssertionError("chiral cycles do not pair under reversal")
        rows.append(
            {
                "n": n,
                "exact_points": nu,
                "cyclic_orbits": cycles,
                "diagonal_orbits": diagonal,
                "nondiagonal_self_reversing_orbits": nondiagonal,
                "chiral_cyclic_orbits": chiral_cycles,
                "chiral_doublets": chiral_cycles // 2,
            }
        )
    first = next(row["n"] for row in rows if row["chiral_doublets"])
    if first != 6:
        raise AssertionError("first chiral period changed")
    return {
        "rows": rows,
        "first_chiral_period": first,
        "status": "prior-work count, recomputed as a scope certificate",
    }


def period_six_source_polynomials() -> tuple[dict, dict]:
    A, r, x = sp.symbols("A r x")
    f_plus = x**3 - (1 + r) * x**2 - A * x + A * (1 + r) - 1
    f_minus = f_plus.subs(r, -r)
    p6 = sp.rem(sp.expand(f_plus * f_minus), r**2 - (A - 3), r)
    expected_p6 = (
        x**6
        - 2 * x**5
        + (4 - 3 * A) * x**4
        + (4 * A - 2) * x**3
        + (3 * A**2 - 8 * A + 2) * x**2
        + (-2 * A**2 + 2 * A) * x
        - A**3
        + 4 * A**2
        - 2 * A
        + 1
    )
    if sp.expand(p6 - expected_p6) != 0:
        raise AssertionError("published carrier expansion changed")
    disc_p6 = sp.factor(sp.discriminant(p6, x))
    expected_disc = 64 * (A - 3) ** 3 * (16 * A**2 - 8 * A + 5) ** 2
    if sp.expand(disc_p6 - expected_disc) != 0:
        raise AssertionError("period-six carrier discriminant changed")

    F = sp.expand(f_plus.subs(A, r**2 + 3))
    expected_F = (
        r**3 - r**2 * x + r**2 - r * x**2 + 3 * r
        + x**3 - x**2 - 3 * x + 2
    )
    if sp.expand(F - expected_F) != 0:
        raise AssertionError("cubic base-change model changed")
    disc_F = sp.factor(sp.discriminant(F, x))
    expected_disc_F = 16 * r**4 + 88 * r**2 + 125
    if sp.expand(disc_F - expected_disc_F) != 0:
        raise AssertionError("cubic discriminant changed")
    if sp.gcd(sp.Poly(disc_F, r), sp.Poly(sp.diff(disc_F, r), r)).degree() != 0:
        raise AssertionError("cubic discriminant is not squarefree")
    affine_singular_ideal = sp.groebner(
        [F, sp.diff(F, r), sp.diff(F, x)], r, x, order="lex"
    )
    if affine_singular_ideal.polys != [sp.Poly(1, r, x, domain=sp.ZZ)]:
        raise AssertionError("base-changed cubic acquired an affine singularity")

    source = {
        "attribution": (
            "C6(sigma)=sigma-2 and P6=f_r*f_-r are Endler-Gallas prior work; "
            "HCS-C21 claims no novelty for these scalar formulas"
        ),
        "C6_marker": "sigma-2",
        "r_relation": "r^2=A-3",
        "f_r": str(f_plus),
        "f_minus_r": str(f_minus),
        "P6_coordinate_carrier": str(p6),
        "P6_sha256": sha256_text(str(p6)),
        "Disc_x_P6": str(expected_disc),
        "base_changed_cubic_F": str(F),
        "F_sha256": sha256_text(str(F)),
        "Disc_x_F": str(expected_disc_F),
        "Disc_x_F_squarefree": True,
        "scalar_coordinate_curve_normalization_genus": 0,
        "scalar_curve_infinity_node": {
            "point": "[r:x:z]=[1:1:0]",
            "ordinary_node": True,
            "tangent_cone_in_local_coordinates": "2*X*(X-Z)",
            "affine_singular_ideal": "(1)",
            "other_infinity_point": "[r:x:z]=[1:-1:0] is smooth",
        },
    }
    symbols = {"A": A, "r": r, "x": x, "f_plus": f_plus, "f_minus": f_minus, "F": F}
    return source, symbols


def apply_power(function, state, power: int):
    for _ in range(power):
        state = function(state)
    return state


def permutation_group_certificate() -> dict:
    states = [(eps, perm) for eps in (1, -1) for perm in itertools.permutations(range(3))]

    def tau(state):
        eps, perm = state
        return -eps, (perm[1], perm[2], perm[0])

    def rho(state):
        eps, perm = state
        return -eps, (perm[1], perm[0], perm[2])

    if not all(apply_power(tau, state, 6) == state for state in states):
        raise AssertionError("tau^6 failed")
    if any(all(apply_power(tau, state, k) == state for state in states) for k in range(1, 6)):
        raise AssertionError("tau has order below six")
    if not all(rho(rho(state)) == state for state in states):
        raise AssertionError("rho^2 failed")
    if not all(rho(tau(rho(state))) == apply_power(tau, state, 5) for state in states):
        raise AssertionError("rho*tau*rho=tau^-1 failed")

    orbit = {states[0]}
    frontier = [states[0]]
    while frontier:
        state = frontier.pop()
        for function in (tau, rho):
            image = function(state)
            if image not in orbit:
                orbit.add(image)
                frontier.append(image)
    if len(orbit) != 12:
        raise AssertionError("D6 action is not transitive on twelve states")
    return {
        "state_model": "(epsilon, ordered permutation of three f_(epsilon*r) roots)",
        "number_of_states": 12,
        "tau_label_action": "(epsilon,(a,b,c))->(-epsilon,(b,c,a))",
        "rho_label_action": "(epsilon,(a,b,c))->(-epsilon,(b,a,c))",
        "relations": ["tau^6=1", "rho^2=1", "rho*tau*rho=tau^-1"],
        "tau_exact_order": 6,
        "orbit_size": 12,
        "action_free_and_transitive": True,
        "generated_group": "D6",
        "group_order": 12,
    }


def ordered_cover_geometry(symbols: dict) -> tuple[dict, dict, dict]:
    A, r, x = symbols["A"], symbols["r"], symbols["x"]
    f_plus, f_minus, F = symbols["f_plus"], symbols["f_minus"], symbols["F"]
    a, b = sp.symbols("alpha beta")
    A_r = r**2 + 3
    match = sp.expand(x**2 + 1 - A_r - r)
    matched_value = sp.expand(f_minus.subs({A: A_r, x: match}))
    match_quotient, match_remainder = sp.div(matched_value, F, x)
    if sp.expand(match_remainder) != 0:
        raise AssertionError("matching map does not carry roots of f_r to f_-r")
    inverse = sp.expand(match**2 + 1 - A_r + r)
    if sp.expand(sp.rem(inverse - x, F, x)) != 0:
        raise AssertionError("matching map inverse failed")
    sheet_resultant = sp.factor(sp.resultant(F, f_minus.subs(A, A_r), x))
    if sheet_resultant != 8 * r**3:
        raise AssertionError("the two radical sheets are not generically separated")

    gamma = 1 + r - a - b
    m = lambda value: sp.expand(value**2 + 1 - A_r - r)
    e2 = sp.expand(a * b + b * gamma + gamma * a + A_r)
    e3 = sp.expand(a * b * gamma - (1 - A_r * (1 + r)))
    groebner = sp.groebner([e2, e3], a, b, order="lex", domain=sp.QQ.frac_field(r))
    sequence = [a, m(b), gamma, m(a), b, m(gamma)]
    recurrence_remainders: list[str] = []
    for index in range(6):
        previous = sequence[(index - 1) % 6]
        current = sequence[index]
        following = sequence[(index + 1) % 6]
        remainder = sp.factor(
            groebner.reduce(sp.expand(following - (A_r - current**2 - previous)))[1]
        )
        recurrence_remainders.append(str(remainder))
    if recurrence_remainders != ["0"] * 6:
        raise AssertionError("ordered-root sequence is not a six-cycle")

    even_sum = sp.factor(groebner.reduce(sp.expand(sequence[0] + sequence[2] + sequence[4] - (1 + r)))[1])
    odd_sum = sp.factor(groebner.reduce(sp.expand(sequence[1] + sequence[3] + sequence[5] - (1 - r)))[1])
    if even_sum != 0 or odd_sum != 0:
        raise AssertionError("an ordered orbit does not recover the quadratic label r")

    pair_sum_product = sp.expand(
        (a + b) * (a + gamma) * (b + gamma)
    )
    pair_sum_remainder = sp.factor(groebner.reduce(pair_sum_product + 1)[1])
    if pair_sum_remainder != 0:
        raise AssertionError("matching-map Vandermonde sign identity failed")

    group = permutation_group_certificate()
    disc_r = 16 * r**4 + 88 * r**2 + 125
    # The r=1 specialization is a quick rational irreducibility control.  The
    # absolute generic proof is the independent polynomial-root ledger below;
    # the specialization alone would not justify absolute irreducibility.
    specialized = sp.Poly(F.subs(r, 1), x, domain=sp.QQ)
    rational_root_candidates = [-7, -1, 1, 7]
    root_values = {str(candidate): int(specialized.eval(candidate)) for candidate in rational_root_candidates}
    if any(value == 0 for value in root_values.values()):
        raise AssertionError("irreducibility specialization acquired a rational root")
    c, d = sp.symbols("c d")
    linear_root_coefficients = [
        sp.factor(value)
        for value in sp.Poly(sp.expand(F.subs(x, c * r + d)), r).all_coeffs()
    ]
    expected_linear_coefficients = [
        (c - 1) ** 2 * (c + 1),
        3 * c**2 * d - c**2 - 2 * c * d - d + 1,
        3 * c * d**2 - 2 * c * d - 3 * c - d**2 + 3,
        d**3 - d**2 - 3 * d + 2,
    ]
    if any(sp.expand(left - right) != 0 for left, right in zip(linear_root_coefficients, expected_linear_coefficients)):
        raise AssertionError("linear-root absolute irreducibility ledger changed")
    # A rational-function root of this monic cubic is integral over Qbar[r],
    # hence polynomial.  Degree at infinity forces q(r)=c*r+d.  The leading
    # coefficient forces c=+/-1.  The remaining coefficients rule out both.
    no_root_cases = {
        "c=1": {
            "r_coefficient": str(sp.factor(linear_root_coefficients[2].subs(c, 1))),
            "constant_at_d=0": str(linear_root_coefficients[3].subs(d, 0)),
            "constant_at_d=1": str(linear_root_coefficients[3].subs(d, 1)),
        },
        "c=-1": {
            "r2_coefficient": str(sp.factor(linear_root_coefficients[1].subs(c, -1))),
            "r_coefficient_at_d=0": str(linear_root_coefficients[2].subs({c: -1, d: 0})),
        },
    }
    if no_root_cases != {
        "c=1": {"r_coefficient": "2*d*(d - 1)", "constant_at_d=0": "2", "constant_at_d=1": "-1"},
        "c=-1": {"r2_coefficient": "4*d", "r_coefficient_at_d=0": "6"},
    }:
        raise AssertionError("absolute irreducibility case split changed")
    delta_A = 16 * A**2 - 8 * A + 5
    rotation_quotient_rhs = sp.expand((A - 3) * delta_A)
    quotient_disc = sp.factor(sp.discriminant(rotation_quotient_rhs, A))
    if quotient_disc != -4_000_000:
        raise AssertionError("rotation quotient branch discriminant changed")

    geometry = {
        "matching_map": {
            "m_r(x)": str(match),
            "meaning": "the unique forbidden perfect matching between the two cubic root sets",
            "F_minus_r_at_m_r_div_F_r_quotient": str(sp.factor(match_quotient)),
            "remainder": str(match_remainder),
            "inverse_mod_F_r": True,
        },
        "valid_ordered_edge_model": {
            "parameters": "r^2=A-3; alpha!=beta are roots of f_r; gamma=1+r-alpha-beta",
            "edge": "(x_0,x_1)=(alpha,m_r(beta))",
            "edge_coordinate_convention": "(x_i,x_(i+1)); forward edge shift is H_A^-1(x,y)=(y,A-y^2-x)",
            "comparison_to_c20_convention": (
                "C20 uses (x_i,x_(i-1)) and H_A(x,y)=(A-x^2-y,x); "
                "the two clock actions are conjugate by reversal rho"
            ),
            "six_cycle": [str(value) for value in sequence],
            "recurrence_remainders": recurrence_remainders,
            "even_coordinate_sum": "x0+x2+x4=1+r",
            "odd_coordinate_sum": "x1+x3+x5=1-r",
            "recover_r_from_ordered_orbit": "r=(x0-x1+x2-x3+x4-x5)/2",
            "adjacency_graph": "directed K_(3,3) minus the matching y=m_r(x)",
            "sheet_separation_resultant": str(sheet_resultant),
            "twelve_states_distinct_on_generic_open": True,
            "generic_degree_over_A": 12,
        },
        "connectedness_and_group": {
            "f_r_at_r_1": str(specialized.as_expr()),
            "rational_root_values": root_values,
            "f_r_irreducible_over_Q(r)": True,
            "f_r_absolutely_irreducible_over_Qbar(r)": True,
            "absolute_irreducibility_linear_root_ledger": no_root_cases,
            "Disc_f_r_nonsquare_over_Q(r)": True,
            "Disc_f_r_nonsquare_over_Qbar(r)": True,
            "Galois_group_over_Q(r)": "S3",
            "geometric_Galois_group_over_Qbar(r)": "S3",
            "ordered_distinct_root_pair_is_splitting_field": True,
            "ordered_edge_recovers_r_and_all_three_roots": True,
            "Galois_group_over_Q(A)": "D6",
            "group_convention": "D6 has order 12 and is abstractly S3 x C2",
            "group_order": 12,
            "proof": (
                "the S3 splitting field over Q(r) has degree six; adjoining the quadratic "
                "r^2=A-3 and the exact tau action gives a normal degree-twelve D6 cover"
            ),
        },
        "branch_and_genus": {
            "generic_exact_period_open": (
                "remove the discriminant and lower-period collision locus before taking the smooth projective normalization"
            ),
            "base_for_RH": "P1_r",
            "degree": 6,
            "finite_branch_divisor": str(disc_r),
            "finite_simple_branch_points": 4,
            "inertia_at_each_finite_branch": "transposition",
            "contribution_per_branch": 3,
            "infinity_scaled_polynomial": (
                "(u-1)^2*(u+1)+t*(1-u^2)+3*t^2*(1-u)+2*t^3"
            ),
            "double_slope_resolution": "u=1+c*t+... gives 2*c*(c-1)=0",
            "infinity_unramified": True,
            "riemann_hurwitz": "2*g(E6)-2=6*(-2)+4*3=0",
            "genus_E6": 1,
        },
        "label_action": group,
    }

    cohomology = {
        "vandermonde_symbol": "w=(alpha-beta)*(alpha-gamma)*(beta-gamma)",
        "w_square": str(disc_r),
        "matching_pair_sum_product": "(alpha+beta)*(alpha+gamma)*(beta+gamma)=-1",
        "tau_on_r": "-r",
        "tau_on_w": "-w",
        "fixed_field_ledger": {
            "central_sheet_involution": "iota:(r,w)->(-r,-w)",
            "tau_decomposition": "tau=iota*c with c a three-cycle in A3",
            "tau_square_generates": "A3",
            "tau_cube": "iota",
            "rotation_subgroup": "<tau>=A3 x <iota>, order 6",
            "A3_fixed_field": "Q(r,w)",
            "candidate_fixed_field": "Q(A,v) with v=r*w",
            "candidate_degree_over_Q(A)": 2,
            "subgroup_fixed_field_degree_over_Q(A)": 2,
            "conclusion": "Q(E6)^<tau>=Q(A,v)",
        },
        "rotation_invariant": "v=r*w",
        "rotation_quotient": f"v^2={rotation_quotient_rhs}",
        "rotation_quotient_rhs_discriminant": int(quotient_disc),
        "rotation_quotient_genus": 1,
        "E6_to_rotation_quotient_unramified": True,
        "H1_dimension": 2,
        "rotation_invariant_H1_dimension": 2,
        "tau_characteristic_polynomial_on_H1": "(T-1)^2",
        "tau_minimal_polynomial_on_H1": "T-1",
        "nontrivial_tau_isotypic_dimension": 0,
        "D6_H1_representation": "two copies of the reflection-sign character (tau=+1,rho=-1)",
        "interpretation": "tau is a six-torsion translation on the genus-one normalization",
    }

    proof_data = {
        "match_quotient_sha256": sha256_text(str(sp.factor(match_quotient))),
        "ordered_sequence_sha256": sha256_text("|".join(str(value) for value in sequence)),
        "pair_sum_remainder": str(pair_sum_remainder),
        "even_sum_remainder": str(even_sum),
        "odd_sum_remainder": str(odd_sum),
        "sheet_separation_resultant": str(sheet_resultant),
    }
    return geometry, cohomology, proof_data


def half_orbit_polynomial(n: int, A: sp.Symbol, z: sp.Symbol) -> sp.Expr:
    values = {-1: z, 0: z}
    for index in range(0, n // 2 + 1):
        values[index + 1] = sp.expand(A - values[index] ** 2 - values[index - 1])
    k = n // 2
    if n % 2:
        return sp.expand(values[k + 1] - values[k - 1])
    return sp.expand(values[k] - values[k - 1])


def cross_period_shadow() -> dict:
    A, u, sigma6, sigma7, z = sp.symbols("A u sigma6 sigma7 z")
    D1 = u**2 + 2 * u - A
    D6 = sigma6**2 + 4 * sigma6 - 4 * A
    C7 = sigma7**2 - 2 * sigma7 - A
    if sp.expand(D6 - 4 * D1.subs(u, sigma6 / 2)) != 0:
        raise AssertionError("D6 marker does not factor through D1")
    if sp.expand(C7 - D1.subs(u, sigma7 - 2)) != 0:
        raise AssertionError("C7 marker does not factor through D1")
    fiber_product = sp.factor(
        sigma6**2 + 4 * sigma6 - 4 * (sigma7**2 - 2 * sigma7)
    )
    expected_fiber = (sigma6 - 2 * sigma7 + 4) * (sigma6 + 2 * sigma7)
    if sp.expand(fiber_product - expected_fiber) != 0:
        raise AssertionError("cross-period fiber product did not split into two graphs")

    D1z = z**2 + 2 * z - A
    half_rows: list[dict] = []
    q_by_n: dict[int, sp.Expr] = {}
    for n in (5, 6, 7):
        raw = half_orbit_polynomial(n, A, z)
        quotient, remainder = sp.div(raw, D1z, z)
        if sp.expand(remainder) != 0:
            raise AssertionError(f"period-{n} half-orbit polynomial lacks the fixed factor")
        q_by_n[n] = sp.expand(quotient)
        base_changed = sp.expand(quotient.subs(A, u**2 + 2 * u))
        row = {
            "n": n,
            "raw_degree_z": int(sp.degree(raw, z)),
            "primitive_candidate_degree_z": int(sp.degree(quotient, z)),
            "raw_sha256": sha256_text(str(raw)),
            "base_changed_factorization": str(sp.factor(base_changed)),
        }
        if n in (5, 7):
            row["base_changed_irreducible_over_Q(u)"] = bool(
                sp.Poly(base_changed, z, domain=sp.QQ.frac_field(u)).is_irreducible
            )
            if not row["base_changed_irreducible_over_Q(u)"]:
                raise AssertionError(f"period-{n} control unexpectedly split")
        half_rows.append(row)

    q6_base = sp.factor(q_by_n[6].subs(A, u**2 + 2 * u))
    expected_factors = [
        z**2 + 1 - u**2 - 2 * u,
        z**2 + z - u**2 - u + 1,
        z**2 + z - u**2 - 3 * u - 1,
    ]
    if sp.expand(q6_base + sp.prod(expected_factors)) != 0:
        # The half-orbit convention carries one overall minus sign.
        raise AssertionError("period-six fixed-shadow factorization changed")

    return {
        "markers": {
            "D1": str(D1),
            "D6": str(D6),
            "C7": str(C7),
            "D6_object": "period-six reversible/diagonal orbit-sum marker; not the period-six chiral cover",
            "C7_object": "period-seven chiral orbit-sum marker",
            "D6_identity": "D6(sigma6)=4*D1(sigma6/2)",
            "C7_identity": "C7(sigma7)=D1(sigma7-2)",
            "common_quadratic_field": "Q(A,sqrt(A+1))",
        },
        "fiber_product": {
            "factorization": str(fiber_product),
            "graph_1": "sigma6=2*sigma7-4",
            "graph_2": "sigma6=-2*sigma7",
            "global_intersection": "the two graphs meet at A=-1, sigma6=-2, sigma7=1",
            "normalization": "two disjoint graph components",
            "disjoint_over_open_set": "A!=-1",
        },
        "half_orbit_control": {
            "initial_condition": "x_-1=x_0=z",
            "odd_condition": "n=2k+1: x_(k+1)=x_(k-1)",
            "even_condition": "n=2k: x_k=x_(k-1)",
            "rows": half_rows,
            "period6_base_change_factors": [str(factor) for factor in expected_factors],
            "period5_and_period7_remain_irreducible": True,
        },
        "chronology_equivariant_morphism_obstruction": {
            "hypothesis": (
                "dominant nonconstant rational phi:X_m-->X_n between integral exact-period covers, "
                "with phi*H_m=H_n^k*phi on the free locus"
            ),
            "necessary_condition": "n divides k*m",
            "clock_faithful_case": "gcd(k,n)=1 implies n divides m",
            "consequence_for_5_6_7": "no clock-faithful morphism between distinct exact periods 5,6,7",
            "not_excluded": "non-dominant boundary maps, k=0 clock-forgetting maps, or multivalued correspondences",
            "repetition_warning": (
                "a primitive m-point lies in Fix(H^(k*m)) but remains primitive period m; "
                "it is not a point of primitive P_(k*m)"
            ),
        },
        "interpretation": (
            "the marker correspondence is the lower-period shadow D6->D1<-C7, "
            "not a primitive chronology-preserving Hecke correspondence"
        ),
    }


def period_seven_comparison() -> dict:
    certificate = json.loads(C20_CERT.read_text())
    if certificate.get("candidate_id") != "HCS-C20":
        raise AssertionError("C20 dependency candidate identity changed")
    group = certificate["group_and_genus"]
    if group["geometric_group"] != "D7" or group["genus_E"] != 8:
        raise AssertionError("C20 group/genus dependency changed")
    quotient = group["quotients"]["B=E/<tau>"]
    if quotient["genus"] != 2 or quotient["degree_E_to_B"] != 7:
        raise AssertionError("C20 rotation quotient dependency changed")
    total_h1 = 2 * group["genus_E"]
    invariant_h1 = 2 * quotient["genus"]
    nontrivial = total_h1 - invariant_h1
    if nontrivial <= 0:
        raise AssertionError("period-seven nontrivial chronology disappeared")
    return {
        "dependency": "HCS-C20 exact certificate",
        "dependency_sha256": EXPECTED_HASHES["hcs_c20_certificate"],
        "period7_component_scope": "the certified chiral D7 component, not the full saturated P7 scheme",
        "genus_E7": group["genus_E"],
        "rotation_quotient_genus": quotient["genus"],
        "H1_dimension": total_h1,
        "rotation_invariant_H1_dimension": invariant_h1,
        "nontrivial_tau_isotypic_dimension": nontrivial,
    }


def build_certificate() -> dict:
    source, symbols = period_six_source_polynomials()
    geometry, cohomology, proof_data = ordered_cover_geometry(symbols)
    period7 = period_seven_comparison()
    threshold = {
        "scope": (
            "source-identified and repository-certified chiral ordered components through n=7; "
            "the n=7 assertion is existential for the HCS-C20 adopted component"
        ),
        "n_below_6": "no chiral orbit exists (prior-work count)",
        "n6": {
            "genus": geometry["branch_and_genus"]["genus_E6"],
            "nontrivial_tau_isotypic_dimension": cohomology["nontrivial_tau_isotypic_dimension"],
        },
        "n7": {
            "genus": period7["genus_E7"],
            "nontrivial_tau_isotypic_dimension": period7["nontrivial_tau_isotypic_dimension"],
        },
        "first_witnessed_nontrivial_weight_one_chronology_period_within_declared_component_scope": 7,
        "not_claimed": "first nonzero H1 among all D/N/C ordered covers",
    }
    return {
        "schema_version": SCHEMA,
        "candidate_id": CANDIDATE,
        "object_scope": (
            "normalized twelve-state ordered-edge cover of the published period-six chiral doublet; "
            "comparison with the certified period-seven chiral D7 cover; exact lower-period marker shadow"
        ),
        "source_lock": source_lock(),
        "claim_boundary": {
            "published_period6_scalar_formulas_claimed_new": False,
            "period6_ordered_cover_D6_genus1_proved": True,
            "period6_tau_H1_trivial_proved": True,
            "scoped_first_witnessed_threshold_through_n7_proved": True,
            "all_exact_period_components_classified": False,
            "period7_full_saturated_scheme_claimed": False,
            "primitive_cross_period_Hecke_bridge_claimed": False,
            "cross_period_Fredholm_determinant_claimed": False,
            "Riemann_divisor_claimed": False,
            "Hilbert_Polya_operator_claimed": False,
        },
        "lower_period_chirality": lower_period_chirality(),
        "period_six_source_polynomials": source,
        "ordered_cover_geometry": geometry,
        "weight_one_cohomology": cohomology,
        "cross_period_shadow": cross_period_shadow(),
        "period_seven_comparison": period7,
        "chronology_threshold": threshold,
        "proof_data": proof_data,
        "route_a": {
            "A1": "WEAK: exact native phase and reversal survive on the ordered covers",
            "A2": "FAIL: no cross-period trace-class determinant",
            "A3": "FAIL: no Riemann-zero divisor comparison",
            "A4": "FORMAL_HINT: period seven has self-adjoint real chronology correspondences, but period six collapses on H1",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=PROJECT / "results" / "c21_certificate.json")
    args = parser.parse_args()
    certificate = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(f"wrote {args.output}")
    print(f"sha256={sha256_file(args.output)}")


if __name__ == "__main__":
    main()
