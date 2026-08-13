#!/usr/bin/env python3
"""Exact producer for the HCS-C35 adelic Hénon--theta certificate.

Only exact rational/integer arithmetic enters the mathematical gates.  The
certificate does not approximate p-adic numbers; it verifies the rational
additive-character product formula from the exact negative-power parts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


SCHEMA = "hcs-c35-adelic-henon-theta-v3"
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
PROJECT = Path(__file__).resolve().parents[1]
REPOSITORY = PROJECT.parents[1]
SOURCE_FILES = {
    "area_preserving_henon_model": REPOSITORY
    / "henon_dynamics/docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf",
    "prior_work_readme": REPOSITORY / "henon_dynamics/docs/prior_work/README.md",
    "related_programs_readme": REPOSITORY
    / "henon_dynamics/docs/related_programs/README.md",
    "route_a_evaluator": REPOSITORY / "henon_dynamics/skills/route-a-evaluator.md",
}


def canonical_json(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")


def frac_text(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def factor_integer(n: int) -> dict[int, int]:
    n = abs(n)
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def padic_fractional_part(x: Fraction, p: int) -> Fraction:
    """Return the standard p-adic negative-power part of x in Q/Z."""

    exponent = factor_integer(x.denominator).get(p, 0)
    if exponent == 0:
        return Fraction(0)
    modulus = p**exponent
    prime_to_p_denominator = x.denominator // modulus
    inverse = pow(prime_to_p_denominator, -1, modulus)
    residue = (x.numerator * inverse) % modulus
    return Fraction(residue, modulus)


def global_character_exponent(x: Fraction) -> Fraction:
    """Exponent for psi_infty(x)*prod_p psi_p(x), with psi_infty=e(-x)."""

    pieces = [padic_fractional_part(x, p) for p in factor_integer(x.denominator)]
    return -x + sum(pieces, Fraction(0))


def phase(x: Fraction) -> Fraction:
    return 2 * x**3 - x


def rational_grid(max_denominator: int = 32) -> list[Fraction]:
    values = {
        Fraction(a, b)
        for b in range(1, max_denominator + 1)
        for a in range(-2 * b, 2 * b + 1)
    }
    return sorted(values)


def additive_record(x: Fraction) -> dict[str, Any]:
    y = phase(x)
    denominator_primes = sorted(factor_integer(y.denominator))
    pieces = {
        str(p): frac_text(padic_fractional_part(y, p)) for p in denominator_primes
    }
    exponent = global_character_exponent(y)
    assert exponent.denominator == 1
    return {
        "rational_point": frac_text(x),
        "phase_value": frac_text(y),
        "finite_fractional_parts": pieces,
        "global_exponent": exponent.numerator,
        "global_character_value": "1",
    }


def cubic_ball_rows() -> list[dict[str, Any]]:
    """Exact consequences of the stationary-digit recurrence.

    For p>3 and m>=1, summing the highest base-p digit first forces the
    residue variable to be divisible by p.  The surviving sum has one
    forced digit and one free digit, so S_m=p^2 S_{m-1}.
    """

    rows: list[dict[str, Any]] = []
    for p in [5, 7, 11, 13]:
        for m in range(0, 7):
            exponential_sum = p ** (2 * m)
            rows.append(
                {
                    "prime": p,
                    "dilation_level": m,
                    "residue_modulus": p ** (3 * m),
                    "exponential_sum": exponential_sum,
                    "haar_cell_volume": frac_text(Fraction(1, p ** (2 * m))),
                    "ball_integral": "1",
                    "normalized_matrix_coefficient": frac_text(Fraction(1, p**m)),
                    "defect_norm_squared": frac_text(Fraction(2) - Fraction(2, p**m)),
                }
            )
    return rows


def cyclotomic_sum_control(p: int, m: int) -> dict[str, Any]:
    """Verify S_(p,m)=p^(2m) in Z[x]/Phi_(p^(3m)) by enumeration."""

    modulus = p ** (3 * m)
    block = modulus // p
    counts = [0] * modulus
    for u in range(modulus):
        exponent = (2 * u**3 - p ** (2 * m) * u) % modulus
        counts[exponent] += 1
    target = p ** (2 * m)
    quotient_coefficients: list[int] = []
    for residue in range(block):
        values = [
            counts[residue + digit * block]
            - (target if residue == 0 and digit == 0 else 0)
            for digit in range(p)
        ]
        assert len(set(values)) == 1
        quotient_coefficients.append(values[0])
    return {
        "prime": p,
        "dilation_level": m,
        "root_of_unity_order": modulus,
        "enumerated_terms": modulus,
        "target_integer": target,
        "cyclotomic_divisibility": True,
        "quotient_nonzero_coefficients": sum(value != 0 for value in quotient_coefficients),
        "quotient_coefficient_sum": sum(quotient_coefficients),
    }


def build_payload() -> dict[str, Any]:
    grid = rational_grid()
    additive_records = [additive_record(x) for x in grid]

    gauges = [Fraction(0), Fraction(1, 2), Fraction(-7, 15), Fraction(41, 19)]
    gauge_records = []
    for value in gauges:
        exponent = global_character_exponent(value)
        assert exponent.denominator == 1
        gauge_records.append(
            {
                "constant": frac_text(value),
                "global_exponent": exponent.numerator,
                "global_character_value": "1",
            }
        )

    vacuum_rows = []
    for p in PRIMES:
        samples = list(range(-2 * p, 2 * p + 1))
        assert all(phase(Fraction(q)).denominator == 1 for q in samples)
        vacuum_rows.append(
            {
                "prime": p,
                "sample_count": len(samples),
                "phase_integral_on_samples": True,
                "theorem_reason": "P6 has integral coefficients, hence P6(Z_p) subset Z_p",
                "vacuum_verdict": "U_H,p 1_Zp = 1_Zp",
            }
        )

    accumulation_rows = []
    for p in PRIMES[2:]:
        accumulation_rows.append(
            {
                "prime": p,
                "local_dimension": p,
                "guaranteed_nearby_zero_count": p,
                "distance_bound": "pi/log(p)",
            }
        )

    return {
        "schema": SCHEMA,
        "source_lock": {
            name: {
                "path": path.relative_to(REPOSITORY).as_posix(),
                "sha256": sha256(path),
            }
            for name, path in SOURCE_FILES.items()
        },
        "object": {
            "field": "Q",
            "phase": "S6(q,Q)=q*Q-q+2*q^3",
            "chirp": "P6(q)=2*q^3-q",
            "classical_map": "H6(q,p)=(1-6*q^2-p,q)",
            "jacobian": [["-12*q", -1], [1, 0]],
            "jacobian_determinant": 1,
            "global_hilbert_space": "L2(A_Q)",
            "global_unitary": "U_H=F_A M_{psi(P6)}",
        },
        "exact_additive_character_gate": {
            "convention": "psi_infty(x)=exp(-2*pi*i*x); psi_p(x)=exp(2*pi*i*{x}_p)",
            "grid_max_denominator": 32,
            "grid_size": len(grid),
            "all_global_values_one": True,
            "records": additive_records,
        },
        "constant_gauge_gate": {
            "rule": "prod_v psi_v(C)=1 for C in Q",
            "records": gauge_records,
            "verdict": "GLOBAL_CONSTANT_GAUGE_CANCELS",
        },
        "finite_spherical_vacuum_gate": {
            "local_character_conductor": "Z_p",
            "self_dual_lattice": "Z_p",
            "rows": vacuum_rows,
            "verdict": "ALL_REGISTERED_PRIMES_FIX_STANDARD_VACUUM",
            "all_prime_theorem": "PROVED_FROM_INTEGRAL_COEFFICIENTS_AND_SELF_DUALITY",
        },
        "theta_gate": {
            "poisson": "Theta(F g)=Theta(g)",
            "rational_phase": "psi(P6(r))=1 for every r in Q",
            "identity": "Theta(U_H f)=Theta(f)",
            "status": "PROVED",
        },
        "boundary_space_gate": {
            "poisson_map": "E_x(g)(x)=|x|^(1/2)*sum_(r in Q^x) g(r*x)",
            "parity_firewall": "positive-integer real half-model is valid only in the even sector, which M_P6 does not preserve",
            "standard": "S0={g:g(0)=0 and hat(g)(0)=0}",
            "henon": "SH={f:f(0)=0 and hat(M_P6 f)(0)=0}",
            "bijection": "M_P6:SH->S0",
            "range_identity": "E_x U_H(SH)=E_x(S0)",
            "status": "PROVED_UNDER_STANDARD_POISSON_DOMAIN",
        },
        "scaling_site_gate": {
            "primitive_orbits": "C_p=R_+^*/p^Z",
            "clock": "ell(C_p)=log(p)",
            "separate_henon_fact": "U_H,p 1_Zp=1_Zp",
            "coupling_status": "FORMAL_TRIVIAL_VACUUM_DECORATION_ONLY",
            "missing_bridge": "no scaling-site bundle/cocycle with U_H,p as orbit holonomy has been constructed",
            "zeta": "the inherited scaling-site mother zeta is zeta(s)",
            "status": "PRIOR_ART_ZETA_AND_SEPARATE_HENON_VACUUM_COMPATIBILITY",
        },
        "raw_finite_quantum_product_kill": {
            "candidate": "prod_p det(I-p^(1/2-s) U_p)",
            "theorem": "p zeros lie within pi/log(p) of 1/2 for every p-dimensional unitary U_p",
            "rows": accumulation_rows,
            "limit": "1/2 is an interior zero accumulation point",
            "verdict": "NOT_A_NONZERO_MEROMORPHIC_GLOBAL_PRODUCT_WITHOUT_EXACT_CANCELLATION",
        },
        "local_dilation_tower_gate": {
            "prime_scope": "p>3",
            "sum_definition": "S_(p,m)=sum_(u mod p^(3m)) exp(2*pi*i*(2*u^3-p^(2m)*u)/p^(3m))",
            "stationary_digit_condition": "sum over the highest base-p digit forces u=0 mod p",
            "recurrence": "S_(p,m)=p^2*S_(p,m-1), S_(p,0)=1",
            "integral_theorem": "integral_(p^(-m) Z_p) psi_p(2*x^3-x) dx=1 for every m>=0",
            "rows": cubic_ball_rows(),
            "direct_cyclotomic_controls": [
                cyclotomic_sum_control(p, m)
                for p, m in [(5, 1), (5, 2), (7, 1), (7, 2), (11, 1), (13, 1)]
            ],
            "weak_null_sequence": "e_(p,m)=p^(-m/2) 1_(p^(-m) Z_p) converges weakly to 0",
            "noncompactness_witness": "||(M_P6-I)e_(p,m)||^2=2-2*p^(-m) -> 2",
            "verdict": "M_P6_MINUS_IDENTITY_IS_NOT_COMPACT_ON_L2_QP",
        },
        "fixed_domain_relative_range_gate": {
            "ambient_test_space": "V={f in S(A_Q):f(0)=0}",
            "functionals": [
                "Lambda_0(f)=integral f",
                "Lambda_(-P)(f)=integral psi(-P6(x))*f(x) dx",
            ],
            "standard_hyperplane": "S0=V intersect ker(Lambda_0)",
            "chirped_hyperplane": "M_P6 S0=V intersect ker(Lambda_(-P))",
            "common_subspace": "W=V intersect ker(Lambda_0) intersect ker(Lambda_(-P))",
            "quotient_bounds": {"dim(S0/W)": 1, "dim(M_P6*S0/W)": 1},
            "range_pair": [
                "R0=closure(E F(S0))",
                "RH=closure(E F(M_P6 S0))",
            ],
            "algebraic_range_quotient_bound": 2,
            "projection_hypothesis": "both images extend to closed subspaces of one scaling Hilbert completion",
            "conditional_projection_difference_rank_bound": 2,
            "status": "PROVED_STATIC_ALGEBRAIC_RANGE_PAIR_BOUND",
            "dynamic_scattering_consequence": "NOT_PROVED",
        },
        "scaling_covariance_gate": {
            "dilation": "D_a f(x)=|a|^(1/2) f(a*x)",
            "conjugated_phase": "D_a M_P6 D_a^(-1)=M_(P_a), P_a(x)=2*a^3*x^3-a*x",
            "boundary_orbit": "Lambda_(-P_a)(f)=integral psi(-P_a(x))*f(x) dx",
            "archimedean_kernels": "phi_a(z)=exp(-2*pi*i*(2*a^3*z^3-a*z))",
            "independence_proof": "on z=r*exp(i*pi/6), the largest a has unique growth exp(4*pi*a^3*r^3+O(r))",
            "registered_positive_a": list(range(1, 9)),
            "registered_cubic_growth_coefficients": [4 * a**3 for a in range(1, 9)],
            "pre_E_boundary_orbit_dimension": "INFINITE",
            "static_rank_two_implies_dynamic_two_channel": False,
            "verdict": "DYNAMIC_FINITE_CHANNEL_INFERENCE_REFUTED",
            "next_gate": "CONSTRUCT_SCALING_COVARIANT_POISSON_RENORMALIZATION_OR_CROSSED_PRODUCT_SCATTERING",
        },
        "poisson_boundary_defect_gate": {
            "full_scaling_map": "E_x(g)(x)=|x|^(1/2)*sum_(r in Q^x) g(r*x)",
            "poisson_identity": "E_x(F g)(x)=E_x(g)(x^(-1))+|x|^(-1/2)*g(0)-|x|^(1/2)*hat(g)(0)",
            "henon_specialization": "if g=M_(P_a)f and f(0)=0 then E_x(F M_(P_a)f)(x)=E_x(M_(P_a)f)(x^(-1))-|x|^(1/2)*Lambda_(P_a)(f)",
            "general_boundary_modes": ["|x|^(-1/2)", "|x|^(1/2)"],
            "zero_input_output_mode": "|x|^(1/2)",
            "fixed_scale_output_defect_dimension": 1,
            "static_boundary_family": "Lambda_(-P_a)",
            "poisson_coefficient_family": "Lambda_(+P_a)",
            "sign_firewall": "the plus and minus families are separately infinite-dimensional and are not identified",
            "coefficient_functional_orbit": "INFINITE_AND_NOT_COLLAPSED_BY_THIS_IDENTITY",
            "boundary_mode_Hilbert_membership": "NOT_ASSERTED",
            "bounded_finite_rank_operator": "NOT_CLAIMED",
            "determinant_class": "OPEN",
            "status": "EXACT_FIXED_SCALE_POISSON_BOUNDARY_IDENTITY",
        },
        "route_a": {
            "current_tuple": [
                "A1_WEAK",
                "A2_FAIL",
                "A3_PARTIAL_ANALYTIC_STRUCTURE",
                "A4_NATURAL_QUANTIZATION",
            ],
            "overall": "ROUTE_A_EXPLORATORY",
            "qualification": "the scaling mother system supplies A1-A3 while H6 supplies A4; coordinatewise maximization is forbidden until one relative scattering object carries all four",
            "route_b_invocation_allowed": False,
        },
        "decisions": {
            "adelic_henon_theta_route": "GO_EXACT_MOTHER_ROUTE",
            "raw_finite_quantum_euler_product": "STOP_THEOREM",
            "henon_vacuum_essentiality": "REFUTED_BY_SIMPLER_PARENT_CONTROL",
            "naive_same_space_relative_fredholm": "STOP_NONCOMPACTNESS_THEOREM",
            "static_fixed_domain_range_pair": "PROVED_ALGEBRAIC_RANK_BOUND_TWO",
            "dynamic_two_channel_scattering": "STOP_INVALID_INFERENCE",
            "henon_scaling_covariant_scattering": "GO_NEXT_BIG_GATE",
        },
        "scope": {
            "no_rh_proof": True,
            "no_new_tate_or_connes_proof": True,
            "finite_field_operator_not_identified_with_p_adic_operator": True,
            "theta_invariance_not_unique_to_H6": True,
            "no_zero_or_prime_fitting": True,
        },
    }


def build_certificate() -> dict[str, Any]:
    payload = build_payload()
    return {
        "schema": SCHEMA,
        "payload_sha256": hashlib.sha256(canonical_json(payload)).hexdigest(),
        "payload": payload,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    certificate = build_certificate()
    encoded = json.dumps(certificate, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
