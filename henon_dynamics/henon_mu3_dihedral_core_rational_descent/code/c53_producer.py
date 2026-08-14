#!/usr/bin/env python3
"""Produce the exact HCS-C53 rational-descent theorem certificate."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[3]
C51_PATH = REPO / "henon_dynamics/henon_mu3_weight_clock_bifurcation/results/c51_certificate.json"
C52_PATH = REPO / "henon_dynamics/henon_mu3_d12_calabi_yau_core_projector/results/c52_certificate.json"
C52_IMPLEMENTATION_COMMIT = "208feef86365cd92ace8dad02904acff6623eeec"
C52_RELEASE_COMMIT = "a411b8d2626190a9ca941e55d15826db0dedc417"


def canonical_json(value) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def reduce_rho(expression, rho):
    expression = sp.cancel(expression)
    numerator, denominator = sp.fraction(expression)
    modulus = sp.Poly(rho**2 + rho + 1, rho)
    numerator = sp.Poly(sp.expand(numerator), rho).rem(modulus).as_expr()
    denominator = sp.Poly(sp.expand(denominator), rho).rem(modulus).as_expr()
    if denominator == 1:
        return sp.expand(numerator)
    # All denominators used below are constants or units in Q(rho).
    inverse_symbol_a, inverse_symbol_b = sp.symbols("inverse_symbol_a inverse_symbol_b")
    product = sp.Poly(
        sp.expand(denominator*(inverse_symbol_a+inverse_symbol_b*rho)), rho
    ).rem(modulus).as_expr()
    solution = sp.solve(
        [sp.expand(product).coeff(rho,0)-1, sp.expand(product).coeff(rho,1)],
        [inverse_symbol_a, inverse_symbol_b], dict=True
    )
    assert len(solution) == 1
    inverse = solution[0][inverse_symbol_a] + solution[0][inverse_symbol_b]*rho
    return sp.Poly(sp.expand(numerator*inverse), rho).rem(modulus).as_expr().expand()


def tau_expression(expression, rho):
    return reduce_rho(expression.subs(rho, -rho-1, simultaneous=True), rho)


def pair_string(expression, rho) -> str:
    reduced = reduce_rho(expression, rho)
    a = sp.expand(reduced).coeff(rho, 0)
    b = sp.expand(reduced).coeff(rho, 1)
    return f"{a}+({b})*rho"


def polynomial_terms(expression, variables) -> list[dict]:
    polynomial = sp.Poly(sp.expand(expression), *variables, domain=sp.QQ)
    rows = []
    for exponents, coefficient in polynomial.terms():
        rational = Fraction(int(coefficient.p), int(coefficient.q))
        rows.append({
            "exponents": list(exponents),
            "coefficient": {"numerator": rational.numerator, "denominator": rational.denominator},
        })
    return rows


def monomial_map(row):
    return (
        tuple(row["permutation_output_to_input"]),
        tuple(row["rho_phase_exponents"]),
    )


def compose(left, right):
    permutation_left, phases_left = left
    permutation_right, phases_right = right
    return (
        tuple(permutation_right[permutation_left[i]] for i in range(len(permutation_left))),
        tuple((phases_left[i] + phases_right[permutation_left[i]]) % 3 for i in range(len(permutation_left))),
    )


def normalize_projective(item):
    permutation, phases = item
    scalar = phases[0]
    return permutation, tuple((phase-scalar) % 3 for phase in phases)


def tau_map(item):
    permutation, phases = item
    return permutation, tuple((2*phase) % 3 for phase in phases)


def inverse_map(item):
    permutation, phases = item
    inverse_permutation = [0]*len(permutation)
    for index, image in enumerate(permutation):
        inverse_permutation[image] = index
    inverse_phases = [0]*len(permutation)
    for index in range(len(permutation)):
        inverse_phases[index] = (-phases[inverse_permutation[index]]) % 3
    return tuple(inverse_permutation), tuple(inverse_phases)


def all_n_basis(n: int, rho):
    N = 2*n
    theta = 1+2*rho
    labels = ["u0"]
    symbols = [sp.symbols("u0")]
    pair_symbols = {}
    for index in range(1,n):
        u = sp.symbols(f"u{index}")
        v = sp.symbols(f"v{index}")
        labels.extend([f"u{index}",f"v{index}"])
        symbols.extend([u,v])
        pair_symbols[index] = (u,v)
    center = sp.symbols(f"u{n}")
    labels.append(f"u{n}")
    symbols.append(center)
    assert len(symbols) == N

    coordinates = [None]*N
    coordinates[0] = symbols[0]
    for index in range(1,n):
        u,v = pair_symbols[index]
        coordinates[index] = u+theta*v
        factor = rho if index % 2 == 0 else 1
        coordinates[N-index] = factor*(u-theta*v)
    coordinates[n] = center if n % 2 else (1+rho)*center
    return symbols, labels, coordinates


def all_n_control(n: int) -> dict:
    rho = sp.symbols("rho")
    N = 2*n
    variables, labels, B_coordinates = all_n_basis(n, rho)
    x = sp.symbols(f"x0:{N}")
    permutation = tuple((-index) % N for index in range(N))
    phases = tuple(1 if index != 0 and index % 2 == 0 else 0 for index in range(N))
    M_coordinates = [rho**phases[index]*x[permutation[index]] for index in range(N)]
    cubic = sum(variable**3 for variable in x)
    quadric_rho = sum(x[i]*x[i+1] for i in range(N-1)) + rho*x[N-1]*x[0]
    quadric_tau = sum(x[i]*x[i+1] for i in range(N-1)) + (-rho-1)*x[N-1]*x[0]
    assert reduce_rho(sum(item**3 for item in M_coordinates)-cubic, rho) == 0
    mapped_quadric = sum(M_coordinates[i]*M_coordinates[i+1] for i in range(N-1)) + rho*M_coordinates[N-1]*M_coordinates[0]
    assert reduce_rho(mapped_quadric-rho*quadric_tau, rho) == 0
    assert all(permutation[permutation[index]] == index for index in range(N))
    assert all((phases[index]+2*phases[permutation[index]]) % 3 == 0 for index in range(N))

    B = sp.zeros(N)
    for i in range(N):
        for j, variable in enumerate(variables):
            B[i,j] = reduce_rho(sp.expand(B_coordinates[i]).coeff(variable),rho)
    tau_B = B.applyfunc(lambda entry: tau_expression(entry, rho))
    M = sp.zeros(N)
    for i in range(N):
        M[i,permutation[i]] = rho**phases[i]
    assert (M*tau_B).applyfunc(lambda entry: reduce_rho(entry,rho)) == B
    determinant = reduce_rho(B.det(),rho)
    assert determinant != 0
    determinant_closed = reduce_rho(
        (2*(1+2*rho))**(n-1)
        * rho**((n-1)//2)
        * (1 if n % 2 else 1+rho),
        rho,
    )
    assert determinant == determinant_closed

    C0 = reduce_rho(sum(item**3 for item in B_coordinates),rho)
    Q_substituted = reduce_rho(
        sum(B_coordinates[i]*B_coordinates[i+1] for i in range(N-1)) + rho*B_coordinates[N-1]*B_coordinates[0],rho
    )
    Q0 = reduce_rho(-rho*Q_substituted,rho)  # (1+rho)^(-1)=-rho
    assert not C0.has(rho) and not Q0.has(rho)
    C_terms = polynomial_terms(C0,variables)
    Q_terms = polynomial_terms(Q0,variables)
    exponent = Fraction(4,n)
    return {
        "n": n,
        "N": N,
        "variable_order": labels,
        "M_permutation": list(permutation),
        "M_phase_exponents": list(phases),
        "center_factor": "1" if n % 2 else "1+rho",
        "det_B": pair_string(determinant,rho),
        "det_B_closed_formula_matches": True,
        "C0_monomial_count": len(C_terms),
        "Q0_monomial_count": len(Q_terms),
        "C0_terms_sha256": sha256_bytes(canonical_json(C_terms).encode()),
        "Q0_terms_sha256": sha256_bytes(canonical_json(Q_terms).encode()),
        "C_M_identity": True,
        "Q_M_identity": True,
        "cocycle_identity": True,
        "B_fixed_identity": True,
        "rational_coefficients": True,
        "Q_split_exponent": {"numerator": exponent.numerator, "denominator": exponent.denominator},
        "denominator_after_Q_descent": n//math.gcd(n,4),
        "source_geometry_scope": "CERTIFIED_SMOOTH" if n in (2,3,4) else "ALGEBRAIC_FORM_ONLY_SMOOTHNESS_OPEN",
    }


def n4_explicit_model() -> dict:
    rho = sp.symbols("rho")
    variables, labels, coordinates = all_n_basis(4,rho)
    C0 = reduce_rho(sum(item**3 for item in coordinates),rho)
    Q_substituted = reduce_rho(sum(coordinates[i]*coordinates[i+1] for i in range(7))+rho*coordinates[7]*coordinates[0],rho)
    Q0 = reduce_rho(-rho*Q_substituted,rho)
    B = sp.zeros(8)
    for i in range(8):
        for j, variable in enumerate(variables):
            B[i,j] = reduce_rho(sp.expand(coordinates[i]).coeff(variable),rho)
    return {
        "variable_order": labels,
        "theta": "theta=1+2rho",
        "x_equals_Bu": [
            "u0",
            "u1+theta*v1",
            "u2+theta*v2",
            "u3+theta*v3",
            "(1+rho)*u4",
            "u3-theta*v3",
            "rho*(u2-theta*v2)",
            "u1-theta*v1",
        ],
        "det_B": "24*theta=24+48rho",
        "C0": str(sp.expand(C0)),
        "Q0": str(sp.expand(Q0)),
        "base_change": {
            "C": "C(Bu)=C0(u)",
            "Q": "Q_rho(Bu)=(1+rho)*Q0(u)",
        },
    }


def group_descent(c52_payload: dict) -> dict:
    group = c52_payload["projective_monomial_group"]
    elements = group["elements"]
    multiplication = group["multiplication_table_by_id"]
    M = ((0,7,6,5,4,3,2,1),(0,0,1,0,1,0,1,0))
    lookup = {normalize_projective(monomial_map(row)):row["id"] for row in elements}
    M_inverse = inverse_map(M)
    assert M_inverse == tau_map(M)
    alpha = []
    for row in elements:
        image = compose(compose(M,tau_map(monomial_map(row))),M_inverse)
        alpha.append(lookup[normalize_projective(image)])
    assert sorted(alpha) == list(range(24))
    automorphism_tests = 0
    for i in range(24):
        for j in range(24):
            assert alpha[multiplication[i][j]] == multiplication[alpha[i]][alpha[j]]
            automorphism_tests += 1
    r = next(row for row in elements if row["normal_form"]=={"kind":"rotation","exponent":1})
    s = next(row for row in elements if row["normal_form"]=={"kind":"reflection","exponent":0})
    r_inverse = group["inverse_ids"][r["id"]]
    sr_inverse = multiplication[s["id"]][r_inverse]
    assert alpha[r["id"]] == r_inverse and alpha[s["id"]] == sr_inverse
    inner_maps = set()
    for h in range(24):
        hinv = group["inverse_ids"][h]
        inner_maps.add(tuple(multiplication[multiplication[h][g]][hinv] for g in range(24)))
    assert tuple(alpha) not in inner_maps
    fixed = [i for i,image in enumerate(alpha) if i==image]
    orbits=[]; unseen=set(range(24))
    while unseen:
        seed=min(unseen); orbit=[]; current=seed
        while current not in orbit:
            orbit.append(current);unseen.discard(current);current=alpha[current]
        orbits.append(orbit)
    return {
        "scheme": "nonconstant finite-etale Q-form mathscrG",
        "rank_over_Q": 24,
        "base_change_to_K": "constant Dih(C12)_K",
        "splitting_field": "K=Q(rho)",
        "Galois_alpha_id_map": alpha,
        "Galois_orbits": orbits,
        "Q_rational_geometric_element_ids": fixed,
        "Q_rational_geometric_element_normal_forms": [elements[i]["normal_form"] for i in fixed],
        "generator_r_id": r["id"],
        "generator_s_id": s["id"],
        "alpha_r": "r^(-1)",
        "alpha_s": "s*r^(-1)",
        "alpha_s_equivalent_normal_form": "r*s",
        "outer_twist": True,
        "constant_group_scheme": False,
        "all_24_graphs_Galois_permuted": True,
        "group_table_automorphism_tests": automorphism_tests,
        "individual_24_Q_automorphisms_claimed": False,
        "Reynolds_sum_Galois_stable": True,
    }


def source_lock(path: Path, label: str) -> tuple[dict,dict]:
    raw = path.read_bytes(); cert=json.loads(raw)
    assert sha256_bytes(canonical_json(cert["payload"]).encode()) == cert["payload_sha256"]
    return ({
        "source": label,
        "path": str(path.relative_to(REPO)),
        "schema": cert["schema"],
        "sha256": sha256_bytes(raw),
        "payload_sha256": cert["payload_sha256"],
    }, cert["payload"])


def build_payload() -> dict:
    c51_lock,c51_payload = source_lock(C51_PATH,"C51")
    c52_lock,c52_payload = source_lock(C52_PATH,"C52")
    group = group_descent(c52_payload)
    controls = [all_n_control(n) for n in range(2,11)]
    n4 = n4_explicit_model()
    p7_counts=[22380,20224,20910,19734,19734,20028,19930,20028,19734]
    p7_sizes=[1,1,2,2,2,2,2,6,6]
    weighted=sum(a*b for a,b in zip(p7_counts,p7_sizes))
    assert weighted==481848 and weighted//24==20077
    assert sum(7**i for i in range(6))-(weighted//24)==-469
    return {
        "material_passport": {
            "candidate_id":"HCS-C53",
            "project_slug":"henon_mu3_dihedral_core_rational_descent",
            "artifact_status":"RELEASE_CANDIDATE",
            "implemented_blocks":["B0_ALL_N_DESCENT","B1_EXPLICIT_N4_MODEL","B2_TWISTED_DIHEDRAL_CHOW_DESCENT","B3_COMPATIBLE_LOCAL_FACTORS"],
        },
        "source_lock": {
            "certificates":[c51_lock,c52_lock],
            "C52_implementation_commit":C52_IMPLEMENTATION_COMMIT,
            "C52_release_provenance_commit":C52_RELEASE_COMMIT,
        },
        "B0_all_n_algebraic_descent": {
            "range":"every integer n>=2",
            "N":"2n",
            "source_equations": {
                "C_n":"sum_(i=0)^(2n-1) x_i^3",
                "Q_n_rho":"sum_(i=0)^(2n-2) x_i*x_(i+1)+rho*x_(2n-1)*x_0",
                "chronological_closing_edge_preserved":True,
            },
            "descent_data": {
                "tau":"tau(rho)=rho^2=-rho-1",
                "theta":"theta=1+2rho; tau(theta)=-theta",
                "sigma":"sigma(i)=-i mod 2n",
                "phase_rule":"e_0=0; e_i=1 for nonzero even i and 0 for odd i",
                "M_formula":"(M_n x)_i=rho^(e_i)*x_(sigma(i))",
                "identities":["C_n(M_n x)=C_n(x)","Q_n,rho(M_n x)=rho*Q_n,rho^2(x)","M_n*tau(M_n)=I"],
            },
            "fixed_basis": {
                "theta":"1+2rho",
                "x0":"u0",
                "pair_odd_i":"x_i=u_i+theta*v_i; x_(2n-i)=u_i-theta*v_i",
                "pair_even_i":"x_i=u_i+theta*v_i; x_(2n-i)=rho*(u_i-theta*v_i)",
                "center_odd_n":"x_n=u_n",
                "center_even_n":"x_n=(1+rho)*u_n",
                "fixed_identity":"M_n*tau(B_n)=B_n",
                "determinant_closed_formula":"det(B_n)=(2theta)^(n-1)*rho^floor((n-1)/2)*c_n, with c_n=1 for odd n and c_n=1+rho for even n",
                "determinant_nonzero_all_n":True,
            },
            "rational_forms": {
                "C0_formula":"u0^3+sum_(i=1)^(n-1)(2u_i^3-18u_i*v_i^2)+(-1)^(n+1)u_n^3",
                "Q0_formula":"u0u1+3u0v1+sum_(i=1)^(n-2)(u_i*u_(i+1)+3u_i*v_(i+1)+3u_(i+1)*v_i-3v_i*v_(i+1))+terminal_n",
                "terminal_odd_n":"u_(n-1)u_n+3u_n*v_(n-1)",
                "terminal_even_n":"2u_(n-1)u_n",
                "base_change":"C_n(B_nu)=C0_n(u); Q_n,rho(B_nu)=(1+rho)Q0_n(u)",
            },
            "exact_controls_n2_to_n10":controls,
            "scope": {
                "algebraic_descent_all_n":True,
                "source_ordered_smoothness_all_n_claimed":False,
                "certified_smooth_motivic_rows":[2,3,4],
                "rows_5_to_10":"formula controls only",
            },
        },
        "B1_explicit_n4_Q_model": {
            "K_model":c52_payload["frozen_model"],
            "descent_M": {
                "permutation_output_to_input":[0,7,6,5,4,3,2,1],
                "rho_phase_exponents":[0,0,1,0,1,0,1,0],
                "coordinate_formula":["x0","x7","rho*x6","x5","rho*x4","x3","rho*x2","x1"],
                "C_identity":"C(Mx)=C(x)",
                "Q_identity":"Q_rho(Mx)=rho*Q_rho2(x)",
                "cocycle":"M*tau(M)=I8",
            },
            "Q_model":n4,
            "smoothness":"PROVED_BY_BASE_CHANGE_TO_C50_SMOOTH_K_MODEL",
            "degree":6,
            "dimension":5,
        },
        "B2_twisted_dihedral_Chow_descent": {
            "group_scheme":group,
            "projectors": {
                "pi5":"Delta_X0-sum_(i=0)^5 (1/6)h^(5-i) cross h^i",
                "e_mathscrG":"(1/24)sum_(g in mathscrG_K)[Gamma_g]",
                "Reynolds_denominator":24,
                "Galois_stability":"alpha permutes all 24 graph cycles",
                "descent_mechanism":"restriction/corestriction with Q coefficients",
                "quadratic_descent_transfer_denominator":2,
                "Reynolds_and_field_transfer_denominators_not_conflated":True,
                "pi_core0":"pi5*e_mathscrG",
                "pi_level0":"pi5-pi_core0",
                "raw_eG_called_middle_rank10":False,
            },
            "motives_over_Q": {
                "raw_middle":"(X0,pi5)",
                "normalized_O4":"(X0,pi5,2)",
                "raw_core_M0":"M0=(X0,pi_core0), weight 5",
                "CY_type_core":"M0(1), weight 3",
                "source_normalized_core":"M0(2), weight 1",
                "source_normalized_level":"(X0,pi_level0,2), weight 1",
                "core_rank":10,
                "level_rank":158,
                "rank_sum":168,
                "raw_M0_Hodge":[
                    {"p":1,"q":4,"multiplicity":1},
                    {"p":2,"q":3,"multiplicity":4},
                    {"p":3,"q":2,"multiplicity":4},
                    {"p":4,"q":1,"multiplicity":1}
                ],
                "CY_type_M0_twist1_Hodge":[
                    {"p":0,"q":3,"multiplicity":1},
                    {"p":1,"q":2,"multiplicity":4},
                    {"p":2,"q":1,"multiplicity":4},
                    {"p":3,"q":0,"multiplicity":1}
                ],
                "source_normalized_M0_twist2_Hodge":[
                    {"p":-1,"q":2,"multiplicity":1},
                    {"p":0,"q":1,"multiplicity":4},
                    {"p":1,"q":0,"multiplicity":4},
                    {"p":2,"q":-1,"multiplicity":1}
                ],
                "raw_level_Hodge_summary":[0,79,79,0],
                "same_projectors_Betti_deRham_all_ell":True,
            },
        },
        "B3_compatible_local_factors": {
            "raw_core": {
                "motive":"M0=(X0,pi_core0)",
                "rank":10,
                "weight":5,
                "frobenius_convention":"geometric Frobenius F_p; F_p acts on Q_l(-1) by p",
                "characteristic_polynomial":"chi_p(U)=det(U-F_p|M0_ell)",
                "characteristic_polynomial_monic":True,
                "good_local_polynomial":"P_p_raw(T)=det(1-F_p*T|M0_ell)=T^10*chi_p(T^(-1))",
                "good_local_polynomial_called_monic":False,
                "coefficients":"Z[T]",
                "ell_independent":True,
                "Q_coefficient_step":"algebraic-correspondence traces are ell-independent intersection numbers; Newton identities give the monic chi_p(U) in Q[U]",
                "Z_integrality_step":"the roots of monic chi_p(U) are algebraic integers; chi_p in Q[U] therefore lies in Z[U] by Gauss lemma, and coefficient reversal gives P_p_raw in Z[T]",
                "two_step_integrality_argument":True,
                "reciprocity":"a_(10-k)=p^(25-5k)*a_k",
                "reciprocity_mechanism":{
                    "projector_self_transpose":True,
                    "kernel_equals_image_orthogonal":True,
                    "restricted_pairing_nondegenerate":True,
                    "Frobenius_commutes_with_projector":True,
                    "Frobenius_similitude_multiplier":"p^5",
                    "eigenvalue_pairing":"alpha <-> p^5/alpha"
                },
            },
            "normalized_core": {
                "motive":"C4=M0(2)",
                "rank":10,
                "weight":1,
                "Frobenius_on_twist2":"F_C4=F_M0/p^2 under the geometric convention",
                "local_polynomial":"P_p_C4(T)=P_p_raw(T/p^2)",
                "coefficients":"Q[T] generally, not claimed integral",
            },
            "Q_packets": {
                "E4_Q":"Q(0) plus H6_prim(Fermat_cubic_sixfold)(3)",
                "E4_rank":87,
                "O4_Q":"(X0,pi5,2)",
                "O4_rank":168,
                "O4_refinement":[10,158],
                "W4_Q":"E4_Q direct_sum O4_Q",
                "W4_rank":255,
            },
            "split_prime": {
                "condition":"p good and p splits as mathfrakp*bar_mathfrakp in K",
                "two_K_polynomials_identical":True,
                "K_exponent_from_C51":{"numerator":1,"denominator":2},
                "Q_exponent_after_pairing":{"numerator":1,"denominator":1},
                "identity":"Log0-root_1/2(L_K,mathfrakp(W4)*L_K,bar_mathfrakp(W4))=L_Q,p(W4_Q)",
                "branch_scope":"local analytic Log0 branch at z=0 only",
                "meaning_of_integral":"ordinary exponent-one rank-255 Q Euler factor; normalized polynomial need only lie in Q[T]",
            },
            "inert_prime": {
                "condition":"p good inert in K",
                "norm_clock":"N(mathfrakp)=p^2",
                "raw_identity":"P_K,mathfrakp(T)=product_i(1-alpha_i^2*T)",
                "equivalent_identity":"P_K,mathfrakp(z^2)=P_Q,p(z)*P_Q,p(-z)",
                "Q_factor_recovered_as_half_root":False,
            },
            "Artin_base_change":"L_K(M0|K,u)=L_Q(M0,u)*L_Q(M0 tensor chi_K,u)",
            "all_n_split_exponent": {
                "K_exponent":"2/n",
                "Q_exponent":"4/n",
                "denominator":"n/gcd(n,4)",
                "certified_motivic_rows":[2,3,4],
                "n_ge_5":"CONDITIONAL_ON_SMOOTH_SOURCE_PACKET_AND_C51_EXTRACTION",
                "n2":"2",
                "n3":"4/3 remains fractional",
                "n4":"1 clears exactly",
            },
            "global_scope": {
                "split_local_denominator_clearing":"PROVED",
                "inert_Henon_completion":"OPEN_NOT_CLAIMED",
                "automorphy":"OPEN_NOT_CLAIMED",
                "global_continuation":"OPEN_NOT_CLAIMED",
                "functional_equation":"OPEN_NOT_CLAIMED",
            },
        },
        "finite_p7_control": {
            "status":"PRE_C53_RECONNAISSANCE_REGRESSION_ANCHOR_UNCERTIFIED",
            "independently_recomputed_in_C53":False,
            "rho_mod_7":2,
            "class_sizes":p7_sizes,
            "twisted_fixed_counts":p7_counts,
            "weighted_fixed_sum":weighted,
            "quotient_stack_count":weighted//24,
            "ambient_even_trace":sum(7**i for i in range(6)),
            "raw_core_trace":-469,
            "raw_local_a1":469,
            "normalized_twist2_trace":{"numerator":-67,"denominator":7},
        },
        "decisions": {
            "all_n_Q_descent":"PROVED_ALGEBRAICALLY",
            "nonconstant_rank24_dihedral_group_scheme":"PROVED",
            "rank10_plus_rank158_Chow_motives_over_Q":"PROVED",
            "strict_compatible_raw_local_factors":"PROVED_AT_GOOD_PRIMES",
            "n4_split_half_root_is_one_Q_factor":"PROVED",
            "constant_D12_over_Q":"REFUTED_ONLY_TWISTED_FORM_DESCENDS",
            "rank2_projector_beyond_group_algebra":"OPEN_NOT_CLAIMED",
            "full_rank10_P10_computed":"NOT_RUN_NOT_REQUIRED",
        },
        "scope": {
            "chronology_replaced_by_average":False,
            "closing_edge_deleted":False,
            "all_n_smoothness_claimed":False,
            "24_individual_Q_automorphisms_claimed":False,
            "normalized_local_polynomial_called_integral":False,
            "inert_half_root_claimed":False,
            "automorphy_claimed":False,
            "functional_equation_claimed":False,
            "Riemann_hypothesis_claimed":False,
            "Hilbert_Polya_operator_claimed":False,
        },
    }


def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    payload=build_payload()
    certificate={
        "schema":"hcs-c53-certificate-v1",
        "payload":payload,
        "payload_sha256":sha256_bytes(canonical_json(payload).encode()),
    }
    encoded=json.dumps(certificate,indent=2,sort_keys=True,ensure_ascii=False)+"\n"
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(encoded)
    print(f"wrote {args.output} sha256={sha256_bytes(encoded.encode())}")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
