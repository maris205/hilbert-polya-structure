#!/usr/bin/env python3
"""Produce the exact HCS-C178 harmonic-strobe certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
from math import factorial, gcd
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c178_harmonic_strobe_evidence.json"
SOURCE_COMMIT = "100e5f601a0196710d53784bdeef40d2bff89fa8"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
N_MAX = 36
B_MAX = 12
M_MAX = 9
RADIAL_MAX = 10
LEVEL_MAX = 15


def canonical_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()


def rational_angles() -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    for b in range(1, B_MAX + 1):
        for a in range(b):
            if gcd(a, b) == 1:
                result.append((a, b))
    return result


def build() -> dict:
    angles = rational_angles()
    rational_fixed_rows = []
    for a, b in angles:
        for n in range(1, N_MAX + 1):
            resonant = (n * a) % b == 0
            rational_fixed_rows.append(
                {
                    "a": a,
                    "b": b,
                    "n": n,
                    "reduced": gcd(a, b) == 1,
                    "resonant": resonant,
                    "fixed_set": "entire_plane" if resonant else "origin",
                    "finite_fixed_count": None if resonant else 1,
                }
            )

    irrational_fixed_rows = []
    for label, polynomial in (
        ("sqrt(2)", "x^2-2"),
        ("sqrt(3)", "x^2-3"),
        ("golden_ratio", "x^2-x-1"),
    ):
        for n in range(1, N_MAX + 1):
            irrational_fixed_rows.append(
                {
                    "alpha": label,
                    "minimal_polynomial": polynomial,
                    "n": n,
                    "n_alpha_is_integer": False,
                    "fixed_set": "origin",
                    "finite_fixed_count": 1,
                }
            )

    laguerre_rows = []
    for m in range(-M_MAX, M_MAX + 1):
        ell = abs(m)
        for k in range(RADIAL_MAX + 1):
            normalization_squared = Fraction(factorial(k), factorial(k + ell))
            orthogonality_integral = Fraction(factorial(k + ell), factorial(k))
            laguerre_rows.append(
                {
                    "m": m,
                    "k": k,
                    "laguerre_parameter": ell,
                    "normalization_squared": str(normalization_squared),
                    "orthogonality_integral": str(orthogonality_integral),
                    "normalized_product": str(
                        normalization_squared * orthogonality_integral
                    ),
                    "koopman_angular_exponent": m,
                }
            )

    koopman_phase_rows = []
    for a, b in angles:
        for m in range(-M_MAX, M_MAX + 1):
            koopman_phase_rows.append(
                {
                    "a": a,
                    "b": b,
                    "m": m,
                    "root_order": b,
                    "root_exponent": (a * m) % b,
                    "eigenvalue": "exp(2*pi*i*root_exponent/root_order)",
                    "radial_multiplicity": "countably_infinite",
                }
            )

    quantum_phase_rows = []
    for a, b in angles:
        for level in range(LEVEL_MAX + 1):
            energy_twice = 2 * level + 1
            root_order = 2 * b
            root_exponent = (-a * energy_twice) % root_order
            shifted_exponent = (-(a + b) * energy_twice) % root_order
            quantum_phase_rows.append(
                {
                    "a": a,
                    "b": b,
                    "level": level,
                    "energy_twice": energy_twice,
                    "root_order": root_order,
                    "root_exponent": root_exponent,
                    "eigenvalue": "exp(2*pi*i*root_exponent/root_order)",
                    "representative_is_real_time": True,
                    "two_pi_shifted_numerator": a + b,
                    "two_pi_shifted_root_exponent": shifted_exponent,
                    "two_pi_phase_ratio_exponent": (shifted_exponent - root_exponent) % root_order,
                    "four_pi_shifted_numerator": a + 2 * b,
                    "four_pi_shifted_root_exponent": (-(a + 2 * b) * energy_twice) % root_order,
                }
            )

    data = {
        "schema": "hcs-c178-harmonic-strobe-v1",
        "candidate_id": "HCS-C178",
        "evaluation_date": "2026-08-26",
        "source_commit": SOURCE_COMMIT,
        "evaluator": {
            "skill": "route-a-evaluator",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "phase_space": "X=R^2 with canonical coordinates (q,p)",
            "hamiltonian": "H(q,p)=(q^2+p^2)/2",
            "flow": "Phi_theta(q,p)=(q*cos(theta)+p*sin(theta),-q*sin(theta)+p*cos(theta))",
            "angle_coordinate": "q-i*p=r*exp(i*phi), so phi advances by theta",
            "parameter_domain": "theta is physical real time in R; only the classical and Gaussian Koopman projections are taken modulo 2*pi",
            "strobe": "T_theta=Phi_theta for every physical theta in R and T_(theta+2*pi)=T_theta",
            "clock": "theta in R is the physical Hamiltonian time at unit frequency",
            "gaussian_measure": "dgamma=pi^(-1)*exp(-(q^2+p^2))*dq*dp",
            "koopman_convention": "U_theta*f=f after T_theta",
            "quantum_hamiltonian": "Hhat=(-d^2/dx^2+x^2)/2 on L^2(R)",
            "quantum_propagator": "Q_theta=exp(-i*theta*Hhat)",
            "quantum_cover": "Q_(theta+2*pi)=-Q_theta and Q_(theta+4*pi)=Q_theta; the unitary family is 4*pi-periodic and only projectively 2*pi-periodic",
            "determinant_convention": "classical Artin--Mazur cardinality series and ordinary trace-class Fredholm determinant only",
            "precision": "exact integer, rational, symbolic, Laguerre, Hermite, and cyclotomic algebra",
            "training_data": "none",
            "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya claims, heat/Wick clock substitution, and Route B",
        },
        "classical_theorem": {
            "iterate": "T_theta^n=R_(n*theta)",
            "fixed_set_dichotomy": "Fix(T_theta^n)=R^2 if n*theta is in 2*pi*Z and {(0,0)} otherwise",
            "irrational_case": "if alpha=theta/(2*pi) is irrational, #Fix(T_theta^n)=1 for every n>=1 and zeta_AM(z)=1/(1-z)",
            "rational_case": "if alpha=a/b in lowest terms, Fix(T_theta^n)=R^2 exactly when b divides n; the classical Artin--Mazur series is undefined",
            "period_structure": "irrational angles have only the origin as a periodic point; a reduced rational angle of order b>1 gives the origin plus an uncountable continuum of exact period-b points",
            "zero_angle_edge": "theta=0 has the entire plane fixed at n=1 and the classical Artin--Mazur series is undefined",
            "reversor": "S(q,p)=(q,-p) is involutive and S*T_theta*S=T_theta^(-1)",
        },
        "gaussian_koopman_theorem": {
            "invariance": "T_theta preserves the normalized Gaussian measure for every theta",
            "basis": "psi_(k,m)=sqrt(k!/(k+|m|)!)*r^|m|*L_k^|m|(r^2)*exp(i*m*phi)",
            "basis_range": "k>=0 and m in Z form a complete orthonormal basis of L^2(R^2,gamma)",
            "basis_action": "U_theta*psi_(k,m)=exp(i*m*theta)*psi_(k,m)",
            "irrational_spectrum": "for irrational theta/(2*pi), the eigenvalues exp(i*m*theta) are distinct and dense on the unit circle, each with countably infinite radial multiplicity",
            "rational_spectrum": "for reduced theta/(2*pi)=a/b, the spectrum is the b-th roots of unity and each eigenspace has countably infinite multiplicity",
            "noncompact": True,
            "finite_schatten_class": False,
            "trace_class": False,
            "ordinary_fredholm_determinant_available": False,
            "antiunitary_reversal": "Theta_G=V_S*K satisfies Theta_G*U_theta*Theta_G^(-1)=U_theta^(-1)",
        },
        "quantum_theorem": {
            "self_adjoint_generator": "Hhat is self-adjoint on its standard oscillator domain",
            "parameter_domain": "Q_theta is an operator family on physical real time theta in R, not a single-valued unitary family on R/(2*pi*Z)",
            "same_clock": "Q_theta=exp(-i*theta*Hhat) uses the same physical real time theta as the classical strobe",
            "hermite_basis": "Hhat*h_j=(j+1/2)*h_j for j>=0",
            "hermite_spectrum": "Q_theta*h_j=exp(-i*theta*(j+1/2))*h_j",
            "rational_spectrum": "for the exact real-time representative theta/(2*pi)=a/b in lowest terms, the spectrum is exp(-i*pi*a/b) times the b-th roots, each with infinite multiplicity",
            "metaplectic_periodicity": "Q_(theta+2*pi)=-Q_theta and Q_(theta+4*pi)=Q_theta, so the lift is 4*pi-periodic and projectively 2*pi-periodic without discarding the global sign",
            "egorov_q": "Q_theta^* qhat Q_theta=qhat*cos(theta)+phat*sin(theta)",
            "egorov_p": "Q_theta^* phat Q_theta=-qhat*sin(theta)+phat*cos(theta)",
            "conjugation_reversal": "K*Q_theta*K=Q_theta^(-1)",
            "noncompact": True,
            "finite_schatten_class": False,
            "trace_class": False,
            "ordinary_fredholm_determinant_available": False,
            "heat_wick_boundary": "exp(-t*Hhat) for t>0 is a different imaginary-time heat clock and cannot replace Q_theta in this evaluation",
        },
        "finite_regression_sentinels": {
            "sentinels_are_proof": False,
            "n_max": N_MAX,
            "b_max": B_MAX,
            "m_max": M_MAX,
            "radial_max": RADIAL_MAX,
            "level_max": LEVEL_MAX,
            "rational_angle_count": len(angles),
            "rational_fixed_rows": rational_fixed_rows,
            "irrational_fixed_rows": irrational_fixed_rows,
            "laguerre_rows": laguerre_rows,
            "koopman_phase_rows": koopman_phase_rows,
            "quantum_phase_rows": quantum_phase_rows,
        },
        "progress_and_boundary": {
            "progress": "one all-angle theorem unifies the classical fixed-set transition, exact Gaussian Koopman spectrum, and same-clock quantum oscillator spectrum",
            "operator_boundary": "both natural unitary lifts are noncompact and outside every finite Schatten class, so neither owns an ordinary trace-class Fredholm determinant",
            "clock_boundary": "heat damping, Wick rotation, Hermite truncation, and finite-rank compression define different clocks or operators",
            "cover_boundary": "the classical and Gaussian families are 2*pi-periodic, while the quantum unitary family retains its metaplectic sign and is 4*pi-periodic",
            "route_boundary": "the natural quantum lift cannot compensate for failed arithmetic, primitive-orbit, target-divisor, or global-analytic gates",
        },
        "route_a": {
            "tuple": [
                "A0_FAIL",
                "A1_FAIL",
                "A2_FAIL",
                "A3_FAIL",
                "A4_NATURAL_QUANTIZATION",
            ],
            "overall": "ROUTE_A_REJECTED",
            "A0_qualification": "NO_INTRINSIC_ARITHMETIC_OR_PRIME_POWER_ORIGIN",
            "A1_qualification": "ONLY_ONE_PERIODIC_POINT_AT_IRRATIONAL_ANGLES_AND_UNCOUNTABLE_CLEAN_FAMILIES_AT_RATIONAL_ANGLES",
            "A2_qualification": "IRRATIONAL_SOURCE_ZETA_IS_ELEMENTARY_AND_RATIONAL_ANGLES_HAVE_NO_CLASSICAL_ARTIN_MAZUR_SERIES",
            "A3_qualification": "NO_TARGET_DIVISOR_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_WEIL_COMPRESSION",
            "A4_qualification": "NATURAL_SAME_CLOCK_OSCILLATOR_PROPAGATOR_WITH_EXACT_EGOROV_AND_TIME_REVERSAL",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "used_target_zero_table": False,
            "used_target_prime_table": False,
            "used_arithmetic_local_data": False,
            "claimed_target_divisor_match": False,
            "claimed_target_functional_equation": False,
            "claimed_euler_factor": False,
            "claimed_root_number": False,
            "claimed_automorphy": False,
            "claimed_hilbert_polya": False,
            "used_heat_or_wick_as_same_clock": False,
            "silently_quotiented_quantum_global_phase": False,
            "route_b_invocation_allowed": False,
        },
        "integrity": {
            "finite_ledgers_are_proof": False,
            "citation_population": 0,
            "reference_population": 0,
            "external_reviewer_simulated": False,
            "acceptance_score_claimed": False,
            "model_rejected_as_primary_route_a_candidate": True,
        },
        "nonclaims": [
            "finite fixed counts at rational resonant iterates",
            "an ordinary Fredholm determinant for either non-trace-class unitary",
            "a heat-regularized determinant as a determinant of the physical strobe",
            "a single-valued quantum unitary family on the classical 2*pi time quotient",
            "a prime correspondence, target divisor, functional equation, or counting-law match",
            "arithmetic local data, Euler factors, root numbers, or automorphy",
            "a Hilbert--Polya operator, Route-B authorization, novelty priority, external peer review, or acceptance score",
        ],
    }
    data["payload_sha256"] = sha256(canonical_bytes(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    )
    sentinels = data["finite_regression_sentinels"]
    print(
        json.dumps(
            {
                "status": "C178_PRODUCER_PASS",
                "rational_fixed_rows": len(sentinels["rational_fixed_rows"]),
                "irrational_fixed_rows": len(sentinels["irrational_fixed_rows"]),
                "laguerre_rows": len(sentinels["laguerre_rows"]),
                "koopman_phase_rows": len(sentinels["koopman_phase_rows"]),
                "quantum_phase_rows": len(sentinels["quantum_phase_rows"]),
                "payload_sha256": data["payload_sha256"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
