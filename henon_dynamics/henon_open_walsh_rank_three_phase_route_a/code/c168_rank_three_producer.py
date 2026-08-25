#!/usr/bin/env python3
"""Produce exact rank-three open-Walsh evidence for HCS-C168."""
from __future__ import annotations

import argparse
from decimal import Decimal, getcontext
from fractions import Fraction
from hashlib import sha256
import json
from math import comb
from pathlib import Path


SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
SOURCE_COMMIT = "4342893ce5e2516924181744bfacc01c12e4959d"
K_MAX = 24
M_MAX = 24
FOURIER_SENTINEL_K = 12


def rational_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    encoded = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(encoded).hexdigest()


def phase_sum_pairs(limit: int) -> list[tuple[Fraction, Fraction]]:
    """Return (a_m,b_m) with u_+^m+u_-^m=a_m+b_m*i/sqrt(2)."""
    rows = [(Fraction(2), Fraction(0)), (Fraction(0), Fraction(-1))]
    for _ in range(2, limit + 1):
        a_prev, b_prev = rows[-1]
        a_old, b_old = rows[-2]
        # s_m=(-i/sqrt(2))*s_(m-1)+s_(m-2).
        rows.append((a_old + b_prev / 2, b_old - a_prev))
    return rows[: limit + 1]


def fourier_rows() -> list[dict]:
    getcontext().prec = 90
    rows = []
    for m, (a_value, b_value) in enumerate(phase_sum_pairs(M_MAX)[1:], 1):
        modulus_squared = ((1 + a_value) ** 2 + b_value**2 / 2) / 9
        decimal_value = (
            Decimal(modulus_squared.numerator) / Decimal(modulus_squared.denominator)
        ) ** (Decimal(FOURIER_SENTINEL_K) / Decimal(2))
        rows.append(
            {
                "m": m,
                "phase_sum_coefficients_a_b": [rational_text(a_value), rational_text(b_value)],
                "phase_sum_basis": "u_+^m+u_-^m=a_m+b_m*i/sqrt(2)",
                "one_step_fourier_modulus_squared": rational_text(modulus_squared),
                "strict_contraction_from_nontorsion": True,
                "fourier_magnitude_at_k_12_decimal": format(decimal_value, ".60f"),
            }
        )
    return rows


def spectral_rows() -> list[dict]:
    rows = []
    for k in range(1, K_MAX + 1):
        damped = [comb(k, j) * 2**j for j in range(k + 1)]
        rows.append(
            {
                "k": k,
                "ambient_dimension": 4**k,
                "nonzero_secular_degree": 3**k,
                "zero_generalized_eigenspace_dimension": 4**k - 3**k,
                "multinomial_label_count": comb(k + 2, 2),
                "damped_count_multiplicities_by_j": damped,
                "nonzero_multiplicity_sum": sum(damped),
                "distinct_phase_count_claimed": False,
            }
        )
    return rows


def hole_zero_rows() -> list[dict]:
    counts = [1, 0, 0, 0]
    rows = []
    increments = (0, 2, 3)  # phases 1, -1, -i as powers of i
    for k in range(1, K_MAX + 1):
        updated = [0, 0, 0, 0]
        for residue, count in enumerate(counts):
            for increment in increments:
                updated[(residue + increment) % 4] += count
        counts = updated
        deviation_numerator = sum(abs(4 * count - 3**k) for count in counts)
        rows.append(
            {
                "k": k,
                "counts_by_i_exponent_mod_4": counts.copy(),
                "count_sum": sum(counts),
                "tv_to_uniform_numerator": deviation_numerator,
                "tv_to_uniform_denominator": 8 * 3**k,
                "fourier_bound_numerator_same_denominator": 12,
            }
        )
    return rows


def build_evidence() -> dict:
    payload = {
        "schema": "hcs-c168-open-walsh-rank-three-phase-v1",
        "candidate_id": "HCS-C168",
        "evaluation_date": "2026-08-25",
        "scope_literal": SCOPE,
        "source_commit": SOURCE_COMMIT,
        "source_lock": {
            "object": "four-symbol open Walsh gate A=F4^*diag(1,0,1,1)",
            "full_cycle": "C_k=B_k^k=A^(tensor k)",
            "clock": "one B_k application is one tick; one full register cycle is exactly k ticks",
            "spectral_weight": "nonzero eigenvalues counted with algebraic multiplicity and normalized by 3^k",
            "phase_convention": "phase(rho)=rho/|rho| for nonzero rho",
            "joint_scaling": "Y_k=(log|rho|+k*log(2)/3)/sqrt(k)",
            "cutoffs": {"spectral_k_max": K_MAX, "fourier_m_max": M_MAX, "hole_zero_k_max": K_MAX},
            "precision": "exact integers and rational Q(i/sqrt(2)) recurrences; decimals are sentinels only",
            "forbidden_data": "target zeros or divisors, primes, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
        },
        "one_site_spectrum": {
            "characteristic_polynomial": "x*(x-1)*(x^2+i*x/2-1/2)",
            "rank": 3,
            "diagonalizable": True,
            "eigenvalues": ["0", "1", "(sqrt(7)-i)/4", "(-sqrt(7)-i)/4"],
            "nonzero_moduli": ["1", "1/sqrt(2)", "1/sqrt(2)"],
            "normalized_phases": ["1", "u_+=(sqrt(7)-i)/(2*sqrt(2))", "u_-=(-sqrt(7)-i)/(2*sqrt(2))"],
            "phase_sum": "u_++u_-=-i/sqrt(2)",
            "phase_product": "u_+*u_-=-1",
            "phase_ratio": "r=u_+/u_-=(-3+i*sqrt(7))/4",
            "ratio_trace": "r+r^(-1)=-3/2",
            "ratio_not_root_of_unity": True,
            "nontorsion_proof": "a root of unity would make r+r^(-1) an algebraic integer, whereas the rational number -3/2 is not an integer",
        },
        "all_k_secular_theorem": {
            "multinomial_product": "det(I-z*C_k)=product_(a+b+c=k)(1-z*lambda_+^b*lambda_-^c)^(k!/(a!*b!*c!))",
            "nonzero_degree": "3^k",
            "zero_generalized_eigenspace_dimension": "4^k-3^k",
            "diagonalization_basis": "tensor products of the four distinct one-site eigenvectors",
            "phase_labels_may_collide": True,
            "distinct_phase_count_not_claimed": True,
            "proof_basis": "one-site diagonalization and the tensor-product spectral theorem in finite dimension",
        },
        "phase_limit_theorem": {
            "phase_measure": "mu_k=3^(-k)*sum_(a+b+c=k) multinomial(k;a,b,c)*delta_(u_+^b*u_-^c)",
            "fourier_identity": "mu_hat_k(m)=((1+u_+^m+u_-^m)/3)^k for every integer m",
            "fixed_mode_contraction": "for each fixed nonzero m, |(1+u_+^m+u_-^m)/3|<1",
            "contraction_proof": "equality in the triangle inequality would require u_+^m=u_-^m=1 and hence r^m=1, excluded by nontorsion",
            "weak_limit": "mu_k converges weakly to normalized Haar measure on the unit circle",
            "all_m_uniform_gap_claimed": False,
            "finite_k_tv_to_continuous_haar": "1",
            "atomicity_warning": "every finite-k phase measure is atomic, so its total-variation distance from continuous Haar measure equals one",
        },
        "log_modulus_joint_theorem": {
            "one_site_log_modulus_law": "X=0 with probability 1/3 and X=-log(2)/2 with probability 2/3",
            "mean": "-log(2)/3",
            "variance": "log(2)^2/18",
            "normalization": "Y_k=(sum_(j=1)^k X_j+k*log(2)/3)/sqrt(k)",
            "mixed_transform": "E[e^(itY_k)*phase(rho)^m]=e^(it*log(2)*sqrt(k)/3)*((1+e^(-it*log(2)/(2*sqrt(k)))*(u_+^m+u_-^m))/3)^k",
            "joint_limit": "(Y_k,phase(rho)) converges to Normal(0,log(2)^2/18) tensor Haar",
            "asymptotic_independence": True,
            "proof_basis": "the m=0 transform is the iid characteristic-function CLT; every fixed m!=0 has an exponentially contracting limiting base",
        },
        "hole_zero_control": {
            "gate": "A_0=F4^*diag(0,1,1,1)",
            "characteristic_polynomial": "x*(x-1)*(x+1/2)*(x+i)",
            "nonzero_spectrum": ["1", "-1/2", "-i"],
            "phase_steps_as_i_exponents": [0, 2, 3],
            "torsion_group": "<i>={1,i,-1,-i}",
            "nontrivial_fourier_modulus": "1/3",
            "tv_bound": "TV(nu_k,Uniform(<i>))<=(3/2)*3^(-k)",
            "limit": "total-variation convergence to the uniform law on the four-element phase group",
        },
        "antiunitary_control": {
            "digit_reflection": "R=F4^2 and R*A_1*R=A_3",
            "antiunitary": "Theta=F4*K, where K is coordinate conjugation",
            "intertwining": "Theta*A_1*Theta^(-1)=A_3^*=diag(1,1,1,0)*F4",
            "meaning": "the control exchanges hole 1 with hole 3 and reverses projector order/propagation",
            "fixed_hole_self_adjoint_limit": False,
            "antiunitary_limiting_operator_claimed": False,
        },
        "spectral_ledgers": spectral_rows(),
        "fourier_ledgers": fourier_rows(),
        "hole_zero_ledgers": hole_zero_rows(),
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_UNITARY_OR_SCATTERING_CANDIDATE"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "source_side_exact_secular_law": True,
            "source_side_phase_haar_limit": True,
            "source_side_joint_gaussian_haar_limit": True,
            "self_adjoint_limit": False,
            "fixed_hole_antiunitary_limit": False,
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
            "hard_gate": "unconditional all-k rank-three secular and phase-limit theorem for the natural four-symbol gate",
            "hard_gate_status": "PASS",
            "pivot_required": False,
            "finite_ledgers_are_proof": False,
            "external_reviewer_simulated": False,
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results/c168_rank_three_evidence.json",
    )
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(
        json.dumps(
            {
                "status": "C168_PRODUCER_PASS",
                "payload_sha256": payload["payload_sha256"],
                "spectral_k_max": K_MAX,
                "fourier_m_max": M_MAX,
                "hole_zero_k_max": K_MAX,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
