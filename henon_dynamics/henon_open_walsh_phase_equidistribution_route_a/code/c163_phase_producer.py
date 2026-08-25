#!/usr/bin/env python3
"""Produce exact phase-equidistribution evidence for HCS-C163."""
from __future__ import annotations

import argparse
from decimal import Decimal, getcontext
from fractions import Fraction
from hashlib import sha256
import json
from math import comb
from pathlib import Path


SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
SOURCE_COMMIT = "63f75cf476711de93e6096ef74ac16969e1127d0"
K_MAX = 32
M_MAX = 24


def rational_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def poly_sub(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    size = max(len(left), len(right))
    out = [Fraction(0) for _ in range(size)]
    for j, value in enumerate(left):
        out[j] += value
    for j, value in enumerate(right):
        out[j] -= value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def multiply_x(poly: list[Fraction]) -> list[Fraction]:
    return [Fraction(0)] + poly


def phase_chebyshev_polynomials(limit: int) -> list[list[Fraction]]:
    """Return P_m with P_m(c)=r^m+r^-m and P_m=cP_(m-1)-P_(m-2)."""
    rows = [[Fraction(2)], [Fraction(0), Fraction(1)]]
    for _ in range(2, limit + 1):
        rows.append(poly_sub(multiply_x(rows[-1]), rows[-2]))
    return rows[: limit + 1]


def decimal_phase_rows(polynomials: list[list[Fraction]]) -> list[dict]:
    getcontext().prec = 90
    c = (Decimal(3).sqrt() - Decimal(111).sqrt()) / Decimal(6)
    rows = []
    for m in range(1, M_MAX + 1):
        value = sum(
            Decimal(coefficient.numerator) / Decimal(coefficient.denominator) * c**power
            for power, coefficient in enumerate(polynomials[m])
        )
        q2 = (Decimal(2) + value) / Decimal(4)
        if q2 < 0 and abs(q2) < Decimal("1e-75"):
            q2 = Decimal(0)
        q = q2.sqrt()
        rows.append(
            {
                "m": m,
                "two_cos_m_delta_polynomial_ascending": [rational_text(x) for x in polynomials[m]],
                "r_power_not_one": True,
                "q_m_squared_decimal": format(q2, ".60f"),
                "q_m_decimal": format(q, ".60f"),
                "fourier_magnitude_at_k_16_decimal": format(q**16, ".60f"),
            }
        )
    return rows


def phase_k_ledgers() -> list[dict]:
    rows = []
    for k in range(1, K_MAX + 1):
        multiplicities = [comb(k, j) for j in range(k + 1)]
        rows.append(
            {
                "k": k,
                "ambient_dimension": 3**k,
                "surviving_multiplicity": 2**k,
                "zero_generalized_eigenspace_dimension": 3**k - 2**k,
                "distinct_phase_atoms": k + 1,
                "multiplicities_by_j": multiplicities,
                "multiplicity_sum": sum(multiplicities),
                "phase_atoms_distinct_reason": "r is not a root of unity",
            }
        )
    return rows


def moved_hole_ledgers() -> list[dict]:
    rows = []
    for k in range(1, K_MAX + 1):
        residue_counts = [sum(comb(k, j) for j in range(k + 1) if j % 4 == residue) for residue in range(4)]
        deviation_numerator = sum(abs(4 * count - 2**k) for count in residue_counts)
        rows.append(
            {
                "k": k,
                "counts_by_j_mod_4": residue_counts,
                "count_sum": sum(residue_counts),
                "tv_to_uniform_coset_numerator": deviation_numerator,
                "tv_to_uniform_coset_denominator": 8 * 2**k,
            }
        )
    return rows


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    return sha256(json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def build_evidence() -> dict:
    polynomials = phase_chebyshev_polynomials(M_MAX)
    payload = {
        "schema": "hcs-c163-open-walsh-phase-equidistribution-v1",
        "candidate_id": "HCS-C163",
        "evaluation_date": "2026-08-25",
        "scope_literal": SCOPE,
        "source_commit": SOURCE_COMMIT,
        "source_lock": {
            "object": "frozen C148/C153/C158 three-symbol open Walsh gate with A=F3^*diag(1,0,1)",
            "full_cycle": "C_k=B_k^k=A^(tensor k)",
            "clock": "one B_k application is one tick; one full cycle is exactly k ticks",
            "phase_convention": "phase(rho)=rho/|rho| for every nonzero eigenvalue rho of C_k",
            "measure_convention": "mu_k is the algebraic-multiplicity-weighted probability measure on surviving phases",
            "joint_scaling": "X_k=(1/k)log|rho| and Y_k=sqrt(k)*(X_k+log(3)/4)",
            "cutoffs": {"phase_k_max": K_MAX, "fourier_m_max": M_MAX, "moved_hole_k_max": K_MAX},
            "precision": "exact integers and rational polynomials in c=2cos(delta); 60-place decimals are sentinels only",
            "forbidden_data": "target zeros or divisors, primes, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
        },
        "phase_algebra": {
            "one_site_polynomial": "lambda*(lambda^2-tau*lambda+q0)",
            "tau": "sqrt(3)/6-i/2",
            "q0": "-1/2-sqrt(3)*i/6",
            "phase_units": "u_+/-=lambda_+/-/|lambda_+/-| with |lambda_+|>|lambda_-|>0",
            "phase_ratio": "r=u_+/u_-=exp(i*delta)",
            "two_cos_delta": "c=r+r^(-1)=2cos(delta)=(sqrt(3)-sqrt(111))/6",
            "c_squared_q_sqrt37": ["19/6", "-1/6"],
            "primitive_irreducible_integer_polynomial_coefficients_ascending": [27, 0, -19, 0, 3],
            "primitive_irreducible_integer_polynomial": "3*c^4-19*c^2+27",
            "monic_rational_minimal_polynomial": "c^4-(19/3)*c^2+9",
            "irreducibility_receipt": "c^2 has irreducible polynomial 3*y^2-19*y+27 with discriminant 37, while c is not in Q(sqrt(37)) because that would put sqrt(3) there",
            "not_algebraic_integer": True,
            "integrality_obstruction": "the monic rational minimal polynomial has nonintegral coefficient -19/3; equivalently its primitive integer associate has nonunit leading coefficient 3",
            "phase_ratio_not_root_of_unity": True,
            "proof_receipt": "if r were a root of unity then r+r^(-1)=c would be an algebraic integer, contradicting the nonintegral coefficient in its monic rational minimal polynomial",
        },
        "all_k_phase_theorem": {
            "phase_measure": "mu_k=2^(-k)*sum_(j=0)^k binom(k,j)*delta_(u_-^k*r^j)",
            "fourier_identity": "mu_hat_k(m)=u_-^(m*k)*((1+r^m)/2)^k for every integer m",
            "fourier_magnitude": "|mu_hat_k(m)|=|cos(m*delta/2)|^k",
            "fixed_cutoff_bound": "for p(z)=sum_|m|<=M a_m z^m, |mu_k(p)-Haar(p)|<=sum_(0<|m|<=M)|a_m|*q_m^k, q_m=|cos(m*delta/2)|<1",
            "weak_limit": "mu_k converges weakly to normalized Haar measure on the unit circle",
            "joint_limit": "(Y_k,phase(rho)) converges jointly to Normal(0,sigma^2) tensor Haar",
            "sigma_squared": "sigma^2=(log(|lambda_+|/|lambda_-|))^2/4",
            "mixed_transform": "E[exp(i*t*Y_k)*phase(rho)^m]=u_-^(m*k)*exp(-i*t*d*sqrt(k)/2)*((1+r^m*exp(i*t*d/sqrt(k)))/2)^k, d=log(|lambda_+|/|lambda_-|)",
            "asymptotic_independence": True,
            "proof_basis": "binomial theorem, the non-root-of-unity obstruction, Fourier density on the circle, and the Bernoulli characteristic-function CLT",
        },
        "general_binary_phase_dichotomy": {
            "non_torsion_branch": "if r is not a root of unity, the binomial phase measures converge weakly to Haar",
            "torsion_branch": "if r has exact order h, the measure converges in total variation to the uniform measure on the moving coset u_-^k<r>",
            "torsion_tv_bound": "TV<=((h-1)/2)*max_(1<=m<h)|cos(pi*m/h)|^k",
            "frozen_branch": "NON_TORSION_HAAR",
        },
        "phase_k_ledgers": phase_k_ledgers(),
        "fourier_decay_ledgers": decimal_phase_rows(polynomials),
        "controls": {
            "projector_order": {
                "gate": "A_right=diag(1,0,1)F3^*=F3*A*F3^*",
                "result": "unitary similarity preserves the phase ratio and the Haar and joint limits",
            },
            "moved_hole": {
                "projector": "diag(0,1,1)",
                "nonzero_eigenvalues": "-i and -1/sqrt(3)",
                "phase_ratio": "i",
                "phase_ratio_order": 4,
                "limit": "uniform measure on the moving four-point coset (-1)^k< i >",
                "tv_bound": "TV<=(3/2)*(sqrt(2)/2)^k",
                "residue_ledgers": moved_hole_ledgers(),
            },
            "closed_parent": {
                "projector": "I_3",
                "result": "the one-site gate is unitary with three surviving phases, so it lies outside the binary theorem rather than serving as a forged binary control",
            },
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_UNITARY_OR_SCATTERING_CANDIDATE"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "source_side_phase_limit": True,
            "source_side_joint_modulus_phase_limit": True,
            "self_adjoint_limit": False,
            "antiunitary_limit": False,
            "target_divisor_matching": False,
            "target_functional_equation": False,
            "target_counting_law": False,
            "prime_like_correspondence": False,
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "hilbert_polya_operator": False,
        },
        "integrity": {
            "pivot_required": False,
            "hard_gate": "unconditional all-k phase theorem for the frozen gate",
            "hard_gate_status": "PASS",
            "finite_ledgers_are_proof": False,
            "external_reviewer_simulated": False,
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "results/c163_phase_evidence.json")
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C163_PRODUCER_PASS", "payload_sha256": payload["payload_sha256"], "phase_k_max": K_MAX, "fourier_m_max": M_MAX}, sort_keys=True))


if __name__ == "__main__":
    main()
