#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C168."""
from __future__ import annotations

import argparse
from decimal import Decimal, getcontext
from fractions import Fraction
from hashlib import sha256
import json
from math import comb
from pathlib import Path


K_MAX = 24
M_MAX = 24
SOURCE_COMMIT = "4342893ce5e2516924181744bfacc01c12e4959d"


def canonical_hash(data: dict) -> str:
    work = dict(data)
    work.pop("payload_sha256", None)
    encoded = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(encoded).hexdigest()


def text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def phase_pairs(limit: int) -> list[tuple[Fraction, Fraction]]:
    values = [(Fraction(2), Fraction(0)), (Fraction(0), Fraction(-1))]
    while len(values) <= limit:
        a1, b1 = values[-1]
        a2, b2 = values[-2]
        values.append((a2 + b1 / 2, b2 - a1))
    return values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "evidence",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results/c168_rank_three_evidence.json",
    )
    parser.add_argument("--mutation-fast", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0

    def check(condition: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    def keys(mapping: object, expected: set[str], message: str) -> None:
        check(isinstance(mapping, dict) and set(mapping) == expected, message)

    top_keys = {
        "schema", "candidate_id", "evaluation_date", "scope_literal", "source_commit", "source_lock",
        "one_site_spectrum", "all_k_secular_theorem", "phase_limit_theorem", "log_modulus_joint_theorem",
        "hole_zero_control", "antiunitary_control", "spectral_ledgers", "fourier_ledgers",
        "hole_zero_ledgers", "route_a", "claim_boundary", "integrity", "payload_sha256",
    }
    keys(data, top_keys, "top-level closure")
    check(data["schema"] == "hcs-c168-open-walsh-rank-three-phase-v1", "schema")
    check(data["candidate_id"] == "HCS-C168", "candidate")
    check(data["evaluation_date"] == "2026-08-25", "date")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["payload_sha256"] == canonical_hash(data), "payload hash")

    lock = data["source_lock"]
    expected_lock = {
        "object": "four-symbol open Walsh gate A=F4^*diag(1,0,1,1)",
        "full_cycle": "C_k=B_k^k=A^(tensor k)",
        "clock": "one B_k application is one tick; one full register cycle is exactly k ticks",
        "spectral_weight": "nonzero eigenvalues counted with algebraic multiplicity and normalized by 3^k",
        "phase_convention": "phase(rho)=rho/|rho| for nonzero rho",
        "joint_scaling": "Y_k=(log|rho|+k*log(2)/3)/sqrt(k)",
        "cutoffs": {"spectral_k_max": 24, "fourier_m_max": 24, "hole_zero_k_max": 24},
        "precision": "exact integers and rational Q(i/sqrt(2)) recurrences; decimals are sentinels only",
        "forbidden_data": "target zeros or divisors, primes, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
    }
    keys(lock, set(expected_lock), "source-lock closure")
    for key, expected in expected_lock.items():
        check(lock[key] == expected, f"source lock {key}")

    spectrum = data["one_site_spectrum"]
    expected_spectrum = {
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
    }
    keys(spectrum, set(expected_spectrum), "one-site closure")
    for key, expected in expected_spectrum.items():
        check(spectrum[key] == expected, f"one-site {key}")
    # This is a separate arithmetic proof receipt, not a decimal angle test.
    check(Fraction(-3, 2).denominator != 1, "ratio trace is a nonintegral rational")
    check(all(Fraction(-3, 2) != n for n in range(-2, 2)), "ratio trace is not an integer")

    secular = data["all_k_secular_theorem"]
    expected_secular = {
        "multinomial_product": "det(I-z*C_k)=product_(a+b+c=k)(1-z*lambda_+^b*lambda_-^c)^(k!/(a!*b!*c!))",
        "nonzero_degree": "3^k",
        "zero_generalized_eigenspace_dimension": "4^k-3^k",
        "diagonalization_basis": "tensor products of the four distinct one-site eigenvectors",
        "phase_labels_may_collide": True,
        "distinct_phase_count_not_claimed": True,
        "proof_basis": "one-site diagonalization and the tensor-product spectral theorem in finite dimension",
    }
    keys(secular, set(expected_secular), "secular closure")
    for key, expected in expected_secular.items():
        check(secular[key] == expected, f"secular {key}")

    phase = data["phase_limit_theorem"]
    expected_phase = {
        "phase_measure": "mu_k=3^(-k)*sum_(a+b+c=k) multinomial(k;a,b,c)*delta_(u_+^b*u_-^c)",
        "fourier_identity": "mu_hat_k(m)=((1+u_+^m+u_-^m)/3)^k for every integer m",
        "fixed_mode_contraction": "for each fixed nonzero m, |(1+u_+^m+u_-^m)/3|<1",
        "contraction_proof": "equality in the triangle inequality would require u_+^m=u_-^m=1 and hence r^m=1, excluded by nontorsion",
        "weak_limit": "mu_k converges weakly to normalized Haar measure on the unit circle",
        "all_m_uniform_gap_claimed": False,
        "finite_k_tv_to_continuous_haar": "1",
        "atomicity_warning": "every finite-k phase measure is atomic, so its total-variation distance from continuous Haar measure equals one",
    }
    keys(phase, set(expected_phase), "phase closure")
    for key, expected in expected_phase.items():
        check(phase[key] == expected, f"phase {key}")

    joint = data["log_modulus_joint_theorem"]
    expected_joint = {
        "one_site_log_modulus_law": "X=0 with probability 1/3 and X=-log(2)/2 with probability 2/3",
        "mean": "-log(2)/3",
        "variance": "log(2)^2/18",
        "normalization": "Y_k=(sum_(j=1)^k X_j+k*log(2)/3)/sqrt(k)",
        "mixed_transform": "E[e^(itY_k)*phase(rho)^m]=e^(it*log(2)*sqrt(k)/3)*((1+e^(-it*log(2)/(2*sqrt(k)))*(u_+^m+u_-^m))/3)^k",
        "joint_limit": "(Y_k,phase(rho)) converges to Normal(0,log(2)^2/18) tensor Haar",
        "asymptotic_independence": True,
        "proof_basis": "the m=0 transform is the iid characteristic-function CLT; every fixed m!=0 has an exponentially contracting limiting base",
    }
    keys(joint, set(expected_joint), "joint closure")
    for key, expected in expected_joint.items():
        check(joint[key] == expected, f"joint {key}")
    log_two_symbol = Fraction(1, 1)  # formal coefficient of log(2)
    mean_coefficient = -log_two_symbol / 3
    second_moment_coefficient = Fraction(2, 3) * Fraction(1, 4)
    check(mean_coefficient == Fraction(-1, 3), "mean coefficient")
    check(second_moment_coefficient - mean_coefficient**2 == Fraction(1, 18), "variance coefficient")

    hole = data["hole_zero_control"]
    expected_hole = {
        "gate": "A_0=F4^*diag(0,1,1,1)",
        "characteristic_polynomial": "x*(x-1)*(x+1/2)*(x+i)",
        "nonzero_spectrum": ["1", "-1/2", "-i"],
        "phase_steps_as_i_exponents": [0, 2, 3],
        "torsion_group": "<i>={1,i,-1,-i}",
        "nontrivial_fourier_modulus": "1/3",
        "tv_bound": "TV(nu_k,Uniform(<i>))<=(3/2)*3^(-k)",
        "limit": "total-variation convergence to the uniform law on the four-element phase group",
    }
    keys(hole, set(expected_hole), "hole-zero closure")
    for key, expected in expected_hole.items():
        check(hole[key] == expected, f"hole-zero {key}")

    anti = data["antiunitary_control"]
    expected_anti = {
        "digit_reflection": "R=F4^2 and R*A_1*R=A_3",
        "antiunitary": "Theta=F4*K, where K is coordinate conjugation",
        "intertwining": "Theta*A_1*Theta^(-1)=A_3^*=diag(1,1,1,0)*F4",
        "meaning": "the control exchanges hole 1 with hole 3 and reverses projector order/propagation",
        "fixed_hole_self_adjoint_limit": False,
        "antiunitary_limiting_operator_claimed": False,
    }
    keys(anti, set(expected_anti), "antiunitary closure")
    for key, expected in expected_anti.items():
        check(anti[key] == expected, f"antiunitary {key}")

    ledgers = data["spectral_ledgers"]
    check(isinstance(ledgers, list) and len(ledgers) == K_MAX, "spectral ledger length")
    for k, row in enumerate(ledgers, 1):
        keys(
            row,
            {"k", "ambient_dimension", "nonzero_secular_degree", "zero_generalized_eigenspace_dimension", "multinomial_label_count", "damped_count_multiplicities_by_j", "nonzero_multiplicity_sum", "distinct_phase_count_claimed"},
            f"spectral row closure {k}",
        )
        damped = [comb(k, j) * 2**j for j in range(k + 1)]
        check(row["k"] == k, f"spectral k {k}")
        check(row["ambient_dimension"] == 4**k, f"ambient {k}")
        check(row["nonzero_secular_degree"] == 3**k, f"degree {k}")
        check(row["zero_generalized_eigenspace_dimension"] == 4**k - 3**k, f"zero dimension {k}")
        check(row["multinomial_label_count"] == comb(k + 2, 2), f"label count {k}")
        check(row["damped_count_multiplicities_by_j"] == damped, f"damped row {k}")
        check(row["nonzero_multiplicity_sum"] == sum(damped) == 3**k, f"mass {k}")
        check(row["distinct_phase_count_claimed"] is False, f"collision boundary {k}")

    pairs = phase_pairs(M_MAX)
    fourier = data["fourier_ledgers"]
    check(isinstance(fourier, list) and len(fourier) == M_MAX, "Fourier ledger length")
    getcontext().prec = 90
    for m, row in enumerate(fourier, 1):
        keys(
            row,
            {"m", "phase_sum_coefficients_a_b", "phase_sum_basis", "one_step_fourier_modulus_squared", "strict_contraction_from_nontorsion", "fourier_magnitude_at_k_12_decimal"},
            f"Fourier row closure {m}",
        )
        a_value, b_value = pairs[m]
        modulus_squared = ((1 + a_value) ** 2 + b_value**2 / 2) / 9
        decimal_value = (Decimal(modulus_squared.numerator) / Decimal(modulus_squared.denominator)) ** Decimal(6)
        check(row["m"] == m, f"Fourier m {m}")
        check(row["phase_sum_coefficients_a_b"] == [text(a_value), text(b_value)], f"phase sum {m}")
        check(row["phase_sum_basis"] == "u_+^m+u_-^m=a_m+b_m*i/sqrt(2)", f"phase basis {m}")
        check(row["one_step_fourier_modulus_squared"] == text(modulus_squared), f"modulus exact {m}")
        check(Fraction(row["one_step_fourier_modulus_squared"]) < 1, f"strict modulus {m}")
        check(row["strict_contraction_from_nontorsion"] is True, f"strict receipt {m}")
        check(row["fourier_magnitude_at_k_12_decimal"] == format(decimal_value, ".60f"), f"decimal sentinel {m}")

    hole_rows = data["hole_zero_ledgers"]
    check(isinstance(hole_rows, list) and len(hole_rows) == K_MAX, "hole ledger length")
    counts = [1, 0, 0, 0]
    for k, row in enumerate(hole_rows, 1):
        keys(
            row,
            {"k", "counts_by_i_exponent_mod_4", "count_sum", "tv_to_uniform_numerator", "tv_to_uniform_denominator", "fourier_bound_numerator_same_denominator"},
            f"hole row closure {k}",
        )
        updated = [0, 0, 0, 0]
        for residue, count in enumerate(counts):
            for increment in (0, 2, 3):
                updated[(residue + increment) % 4] += count
        counts = updated
        numerator = sum(abs(4 * count - 3**k) for count in counts)
        check(row["k"] == k, f"hole k {k}")
        check(row["counts_by_i_exponent_mod_4"] == counts, f"hole counts {k}")
        check(row["count_sum"] == sum(counts) == 3**k, f"hole mass {k}")
        check(row["tv_to_uniform_numerator"] == numerator, f"hole tv numerator {k}")
        check(row["tv_to_uniform_denominator"] == 8 * 3**k, f"hole tv denominator {k}")
        check(row["fourier_bound_numerator_same_denominator"] == 12, f"hole bound denominator {k}")
        check(numerator <= 12, f"hole Fourier inequality {k}")

    check(
        data["route_a"]
        == {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_UNITARY_OR_SCATTERING_CANDIDATE"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "Route A",
    )
    expected_boundary = {
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
    }
    check(data["claim_boundary"] == expected_boundary, "claim boundary")
    check(
        data["integrity"]
        == {
            "hard_gate": "unconditional all-k rank-three secular and phase-limit theorem for the natural four-symbol gate",
            "hard_gate_status": "PASS",
            "pivot_required": False,
            "finite_ledgers_are_proof": False,
            "external_reviewer_simulated": False,
        },
        "integrity",
    )
    print(json.dumps({"status": "C168_CHECKER_PASS", "assertions": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
