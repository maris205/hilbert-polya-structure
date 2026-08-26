#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C178 evidence."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
from math import factorial, gcd
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c178_harmonic_strobe_evidence.json"
SOURCE_COMMIT = "100e5f601a0196710d53784bdeef40d2bff89fa8"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    blob = json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    return sha256(blob).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    assertions = 0

    def check(condition: bool, label: str) -> None:
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(label)

    check(data["payload_sha256"] == canonical_hash(data), "canonical hash")
    check(data["schema"] == "hcs-c178-harmonic-strobe-v1", "schema")
    check(data["candidate_id"] == "HCS-C178", "candidate")
    check(data["evaluation_date"] == "2026-08-26", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["evaluator"]["skill"] == "route-a-evaluator", "evaluator skill")
    check(data["evaluator"]["version"] == "0.2.0", "evaluator version")
    check(data["evaluator"]["sha256"] == EVALUATOR_SHA256, "evaluator hash")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")

    lock_expected = {
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
    }
    for key, expected in lock_expected.items():
        check(data["source_lock"][key] == expected, f"source lock {key}")

    classical_expected = {
        "iterate": "T_theta^n=R_(n*theta)",
        "fixed_set_dichotomy": "Fix(T_theta^n)=R^2 if n*theta is in 2*pi*Z and {(0,0)} otherwise",
        "irrational_case": "if alpha=theta/(2*pi) is irrational, #Fix(T_theta^n)=1 for every n>=1 and zeta_AM(z)=1/(1-z)",
        "rational_case": "if alpha=a/b in lowest terms, Fix(T_theta^n)=R^2 exactly when b divides n; the classical Artin--Mazur series is undefined",
        "period_structure": "irrational angles have only the origin as a periodic point; a reduced rational angle of order b>1 gives the origin plus an uncountable continuum of exact period-b points",
        "zero_angle_edge": "theta=0 has the entire plane fixed at n=1 and the classical Artin--Mazur series is undefined",
        "reversor": "S(q,p)=(q,-p) is involutive and S*T_theta*S=T_theta^(-1)",
    }
    for key, expected in classical_expected.items():
        check(data["classical_theorem"][key] == expected, f"classical {key}")

    gaussian_expected = {
        "invariance": "T_theta preserves the normalized Gaussian measure for every theta",
        "basis": "psi_(k,m)=sqrt(k!/(k+|m|)!)*r^|m|*L_k^|m|(r^2)*exp(i*m*phi)",
        "basis_range": "k>=0 and m in Z form a complete orthonormal basis of L^2(R^2,gamma)",
        "basis_action": "U_theta*psi_(k,m)=exp(i*m*theta)*psi_(k,m)",
        "irrational_spectrum": "for irrational theta/(2*pi), the eigenvalues exp(i*m*theta) are distinct and dense on the unit circle, each with countably infinite radial multiplicity",
        "rational_spectrum": "for reduced theta/(2*pi)=a/b, the spectrum is the b-th roots of unity and each eigenspace has countably infinite multiplicity",
        "antiunitary_reversal": "Theta_G=V_S*K satisfies Theta_G*U_theta*Theta_G^(-1)=U_theta^(-1)",
    }
    for key, expected in gaussian_expected.items():
        check(data["gaussian_koopman_theorem"][key] == expected, f"Gaussian {key}")
    for key, expected in (
        ("noncompact", True),
        ("finite_schatten_class", False),
        ("trace_class", False),
        ("ordinary_fredholm_determinant_available", False),
    ):
        check(data["gaussian_koopman_theorem"][key] is expected, f"Gaussian {key}")

    quantum_expected = {
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
        "heat_wick_boundary": "exp(-t*Hhat) for t>0 is a different imaginary-time heat clock and cannot replace Q_theta in this evaluation",
    }
    for key, expected in quantum_expected.items():
        check(data["quantum_theorem"][key] == expected, f"quantum {key}")
    for key, expected in (
        ("noncompact", True),
        ("finite_schatten_class", False),
        ("trace_class", False),
        ("ordinary_fredholm_determinant_available", False),
    ):
        check(data["quantum_theorem"][key] is expected, f"quantum {key}")

    finite = data["finite_regression_sentinels"]
    check(finite["sentinels_are_proof"] is False, "sentinel boundary")
    check(finite["n_max"] == 36, "n max")
    check(finite["b_max"] == 12, "b max")
    check(finite["m_max"] == 9, "m max")
    check(finite["radial_max"] == 10, "radial max")
    check(finite["level_max"] == 15, "level max")

    angles = [
        (a, b)
        for b in range(1, 13)
        for a in range(b)
        if gcd(a, b) == 1
    ]
    check(finite["rational_angle_count"] == len(angles), "rational angle count")
    fixed_rows = finite["rational_fixed_rows"]
    check(len(fixed_rows) == len(angles) * 36, "rational fixed row count")
    position = 0
    for a, b in angles:
        for n in range(1, 37):
            row = fixed_rows[position]
            position += 1
            resonant = (n * a) % b == 0
            check(row["a"] == a, f"fixed a {position}")
            check(row["b"] == b, f"fixed b {position}")
            check(row["n"] == n, f"fixed n {position}")
            check(row["reduced"] is True, f"fixed reduced {position}")
            check(row["resonant"] is resonant, f"fixed resonance {position}")
            check(
                row["fixed_set"] == ("entire_plane" if resonant else "origin"),
                f"fixed set {position}",
            )
            check(
                row["finite_fixed_count"] == (None if resonant else 1),
                f"fixed count {position}",
            )

    irrational_rows = finite["irrational_fixed_rows"]
    labels = [
        ("sqrt(2)", "x^2-2"),
        ("sqrt(3)", "x^2-3"),
        ("golden_ratio", "x^2-x-1"),
    ]
    check(len(irrational_rows) == 3 * 36, "irrational row count")
    position = 0
    for label, polynomial in labels:
        for n in range(1, 37):
            row = irrational_rows[position]
            position += 1
            check(row["alpha"] == label, f"irrational alpha {position}")
            check(row["minimal_polynomial"] == polynomial, f"irrational polynomial {position}")
            check(row["n"] == n, f"irrational n {position}")
            check(row["n_alpha_is_integer"] is False, f"irrational integrality {position}")
            check(row["fixed_set"] == "origin", f"irrational set {position}")
            check(row["finite_fixed_count"] == 1, f"irrational count {position}")

    laguerre_rows = finite["laguerre_rows"]
    check(len(laguerre_rows) == 19 * 11, "Laguerre row count")
    position = 0
    for m in range(-9, 10):
        ell = abs(m)
        for k in range(11):
            row = laguerre_rows[position]
            position += 1
            norm = Fraction(factorial(k), factorial(k + ell))
            integral = Fraction(factorial(k + ell), factorial(k))
            check(row["m"] == m, f"Laguerre m {position}")
            check(row["k"] == k, f"Laguerre k {position}")
            check(row["laguerre_parameter"] == ell, f"Laguerre parameter {position}")
            check(Fraction(row["normalization_squared"]) == norm, f"Laguerre norm {position}")
            check(Fraction(row["orthogonality_integral"]) == integral, f"Laguerre integral {position}")
            check(Fraction(row["normalized_product"]) == 1, f"Laguerre product {position}")
            check(row["koopman_angular_exponent"] == m, f"Laguerre exponent {position}")

    koopman_rows = finite["koopman_phase_rows"]
    check(len(koopman_rows) == len(angles) * 19, "Koopman phase row count")
    position = 0
    for a, b in angles:
        for m in range(-9, 10):
            row = koopman_rows[position]
            position += 1
            check((row["a"], row["b"], row["m"]) == (a, b, m), f"Koopman indices {position}")
            check(row["root_order"] == b, f"Koopman order {position}")
            check(row["root_exponent"] == (a * m) % b, f"Koopman exponent {position}")
            check(row["eigenvalue"] == "exp(2*pi*i*root_exponent/root_order)", f"Koopman value {position}")
            check(row["radial_multiplicity"] == "countably_infinite", f"Koopman multiplicity {position}")

    quantum_rows = finite["quantum_phase_rows"]
    check(len(quantum_rows) == len(angles) * 16, "quantum phase row count")
    position = 0
    for a, b in angles:
        for level in range(16):
            row = quantum_rows[position]
            position += 1
            check((row["a"], row["b"], row["level"]) == (a, b, level), f"quantum indices {position}")
            check(row["energy_twice"] == 2 * level + 1, f"quantum energy {position}")
            check(row["root_order"] == 2 * b, f"quantum order {position}")
            check(row["root_exponent"] == (-a * (2 * level + 1)) % (2 * b), f"quantum exponent {position}")
            check(row["eigenvalue"] == "exp(2*pi*i*root_exponent/root_order)", f"quantum value {position}")
            check(row["representative_is_real_time"] is True, f"quantum representative {position}")
            check(row["two_pi_shifted_numerator"] == a + b, f"quantum 2pi numerator {position}")
            shifted = (-(a + b) * (2 * level + 1)) % (2 * b)
            check(row["two_pi_shifted_root_exponent"] == shifted, f"quantum 2pi exponent {position}")
            check(row["two_pi_phase_ratio_exponent"] == b, f"quantum 2pi sign {position}")
            check(row["four_pi_shifted_numerator"] == a + 2 * b, f"quantum 4pi numerator {position}")
            check(
                row["four_pi_shifted_root_exponent"]
                == (-a * (2 * level + 1)) % (2 * b),
                f"quantum 4pi return {position}",
            )

    progress = data["progress_and_boundary"]
    check("all-angle theorem" in progress["progress"], "progress headline")
    check("noncompact" in progress["operator_boundary"], "operator boundary")
    check("different clocks" in progress["clock_boundary"], "clock boundary")
    check("4*pi-periodic" in progress["cover_boundary"], "cover boundary")
    check("cannot compensate" in progress["route_boundary"], "route boundary")

    route = data["route_a"]
    check(
        route["tuple"]
        == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
        "Route tuple",
    )
    check(route["overall"] == "ROUTE_A_REJECTED", "Route overall")
    check(route["A0_qualification"] == "NO_INTRINSIC_ARITHMETIC_OR_PRIME_POWER_ORIGIN", "A0")
    check("UNCOUNTABLE_CLEAN_FAMILIES" in route["A1_qualification"], "A1")
    check("NO_CLASSICAL_ARTIN_MAZUR_SERIES" in route["A2_qualification"], "A2")
    check("NO_TARGET_DIVISOR" in route["A3_qualification"], "A3")
    check("SAME_CLOCK_OSCILLATOR_PROPAGATOR" in route["A4_qualification"], "A4")
    check(route["route_b_invocation_allowed"] is False, "Route B")

    for key, value in data["scope_flags"].items():
        check(value is False, f"scope flag {key}")
    integrity = data["integrity"]
    check(integrity["finite_ledgers_are_proof"] is False, "integrity finite")
    check(integrity["citation_population"] == 0, "integrity citations")
    check(integrity["reference_population"] == 0, "integrity references")
    check(integrity["external_reviewer_simulated"] is False, "integrity external review")
    check(integrity["acceptance_score_claimed"] is False, "integrity acceptance")
    check(integrity["model_rejected_as_primary_route_a_candidate"] is True, "integrity rejection")
    check(len(data["nonclaims"]) == 7, "nonclaim population")

    print(
        json.dumps(
            {
                "status": "C178_CHECKER_PASS",
                "assertions": assertions,
                "payload_sha256": data["payload_sha256"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
