#!/usr/bin/env python3
"""Produce the deterministic HCS-C237 Kramers--Langevin certificate.

The object is the classical harmonic Langevin diffusion.  All entries in the
certificate are generated from exact rational controls and high-precision
matrix formulae; no target zeros, primes, or arithmetic labels are read.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp


SOURCE_COMMIT = "0ebc633706bc34b8b915a44749423486fd4cd243"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c237_kramers_evidence.json"
mp.mp.dps = 90


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def q(value: str | int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def mpq(value: str | int | Fraction) -> mp.mpf:
    z = q(value)
    return mp.mpf(z.numerator) / z.denominator


def dec(value: mp.mpf, digits: int = 64) -> str:
    if abs(value) < mp.mpf("1e-82"):
        return "0.0"
    return mp.nstr(value, digits, strip_zeros=False, min_fixed=-70, max_fixed=70)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def regime(omega: Fraction, gamma: Fraction) -> str:
    if gamma == 0:
        return "underdamped_zero_damping"
    lhs = gamma * gamma
    rhs = 4 * omega * omega
    if lhs < rhs:
        return "underdamped"
    if lhs == rhs:
        return "critical"
    return "overdamped"


def matrix_exp(omega: Fraction, gamma: Fraction, time: Fraction) -> list[list[mp.mpf]]:
    """Return exp(t[[0,1],[-omega^2,-gamma]]) in all damping regimes."""
    om, ga, t = mpq(omega), mpq(gamma), mpq(time)
    alpha = ga / 2
    disc = alpha * alpha - om * om
    if disc < 0:
        nu = mp.sqrt(-disc)
        c = mp.cos(nu * t)
        s = mp.sin(nu * t) / nu
    elif disc == 0:
        c = mp.mpf(1)
        s = t
    else:
        delta = mp.sqrt(disc)
        c = mp.cosh(delta * t)
        s = mp.sinh(delta * t) / delta
    factor = mp.exp(-alpha * t)
    return [
        [factor * (c + alpha * s), factor * s],
        [factor * (-om * om * s), factor * (c - alpha * s)],
    ]


def sigma_matrix(omega: Fraction, beta: Fraction) -> list[list[mp.mpf]]:
    om, be = mpq(omega), mpq(beta)
    if om == 0:
        return [[mp.inf, mp.mpf(0)], [mp.mpf(0), mp.mpf(1) / be]]
    return [[1 / (be * om * om), mp.mpf(0)], [mp.mpf(0), 1 / be]]


def matmul(a: list[list[mp.mpf]], b: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def transpose(a: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    return [[a[j][i] for j in range(2)] for i in range(2)]


def covariance(omega: Fraction, beta: Fraction, gamma: Fraction, time: Fraction, m: list[list[mp.mpf]] | None = None) -> list[list[mp.mpf]]:
    if gamma == 0:
        return [[mp.mpf(0), mp.mpf(0)], [mp.mpf(0), mp.mpf(0)]]
    mm = matrix_exp(omega, gamma, time) if m is None else m
    sig = sigma_matrix(omega, beta)
    ms = matmul(matmul(mm, sig), transpose(mm))
    return [[sig[i][j] - ms[i][j] for j in range(2)] for i in range(2)]


def mean_vector(m: list[list[mp.mpf]], q0: Fraction, p0: Fraction) -> tuple[mp.mpf, mp.mpf]:
    qq, pp = mpq(q0), mpq(p0)
    return m[0][0] * qq + m[0][1] * pp, m[1][0] * qq + m[1][1] * pp


def eigen_data(omega: Fraction, gamma: Fraction) -> tuple[str, mp.mpf, mp.mpf, mp.mpf]:
    om, ga = mpq(omega), mpq(gamma)
    alpha = ga / 2
    disc = alpha * alpha - om * om
    if disc < 0:
        nu = mp.sqrt(-disc)
        return regime(omega, gamma), -alpha, -alpha, nu
    if disc == 0:
        return regime(omega, gamma), -alpha, -alpha, mp.mpf(0)
    delta = mp.sqrt(disc)
    return regime(omega, gamma), -alpha + delta, -alpha - delta, mp.mpf(0)


def drift_rate(omega: Fraction, gamma: Fraction) -> mp.mpf:
    om, ga = mpq(omega), mpq(gamma)
    if ga == 0:
        return mp.mpf(0)
    alpha = ga / 2
    if ga <= 2 * om:
        return alpha
    return alpha - mp.sqrt(alpha * alpha - om * om)


def matrix_row(case_id: str, omega: Fraction, beta: Fraction, gamma: Fraction, time: Fraction) -> dict:
    m = matrix_exp(omega, gamma, time)
    reg, ep, em, imag = eigen_data(omega, gamma)
    alpha = mpq(gamma) / 2
    return {
        "case_id": case_id,
        "omega": ftext(omega), "beta": ftext(beta), "gamma": ftext(gamma), "time": ftext(time),
        "regime": reg, "alpha": dec(alpha),
        "m11": dec(m[0][0]), "m12": dec(m[0][1]), "m21": dec(m[1][0]), "m22": dec(m[1][1]),
        "det_M": dec(mp.exp(-mpq(gamma) * mpq(time))),
        "trace_M": dec(m[0][0] + m[1][1]),
        "eigen_plus_real": dec(ep), "eigen_minus_real": dec(em), "eigen_imag_abs": dec(abs(imag)),
    }


def transition_row(case_id: str, omega: Fraction, beta: Fraction, gamma: Fraction, time: Fraction, q0: Fraction, p0: Fraction) -> dict:
    m = matrix_exp(omega, gamma, time)
    muq, mup = mean_vector(m, q0, p0)
    c = covariance(omega, beta, gamma, time, m)
    cdet = c[0][0] * c[1][1] - c[0][1] * c[1][0]
    return {
        "case_id": case_id,
        "omega": ftext(omega), "beta": ftext(beta), "gamma": ftext(gamma), "time": ftext(time),
        "q0": ftext(q0), "p0": ftext(p0), "regime": regime(omega, gamma),
        "mean_q": dec(muq), "mean_p": dec(mup),
        "cov_qq": dec(c[0][0]), "cov_qp": dec(c[0][1]), "cov_pp": dec(c[1][1]),
        "cov_det": dec(cdet), "det_M": dec(mp.exp(-mpq(gamma) * mpq(time))),
        "covariance_positive_definite": bool(gamma > 0 and cdet > mp.mpf("1e-70")),
    }


def correlation_row(case_id: str, omega: Fraction, beta: Fraction, gamma: Fraction, time: Fraction) -> dict:
    m = matrix_exp(omega, gamma, time)
    om, be = mpq(omega), mpq(beta)
    sq, sp = 1 / (be * om * om), 1 / be
    return {
        "case_id": case_id, "omega": ftext(omega), "beta": ftext(beta), "gamma": ftext(gamma), "time": ftext(time),
        "regime": regime(omega, gamma),
        "C_QQ": dec(sq * m[0][0]), "C_QP": dec(sp * m[0][1]),
        "C_PQ": dec(sq * m[1][0]), "C_PP": dec(sp * m[1][1]),
        "rho_QQ": dec(m[0][0]), "rho_PP": dec(m[1][1]),
        "rho_QP": dec(om * m[0][1]), "rho_PQ": dec(m[1][0] / om),
    }


def rate_row(case_id: str, omega: Fraction, beta: Fraction, gamma: Fraction) -> dict:
    reg, ep, em, imag = eigen_data(omega, gamma)
    return {
        "case_id": case_id, "omega": ftext(omega), "beta": ftext(beta), "gamma": ftext(gamma),
        "regime": reg, "rate": dec(drift_rate(omega, gamma)),
        "eigen_plus_real": dec(ep), "eigen_minus_real": dec(em), "eigen_imag_abs": dec(abs(imag)),
        "critical_polynomial_prefactor": bool(gamma == 2 * omega),
        "rate_at_critical": dec(mpq(omega)),
    }


def kalman_row(case_id: str, omega: Fraction, beta: Fraction, gamma: Fraction) -> dict:
    ga, be = mpq(gamma), mpq(beta)
    noise = mp.sqrt(2 * ga / be) if ga > 0 else mp.mpf(0)
    det = -2 * ga / be
    return {
        "case_id": case_id, "omega": ftext(omega), "beta": ftext(beta), "gamma": ftext(gamma),
        "B": ["0.0", dec(noise)], "AB": [dec(noise), dec(-ga * noise)],
        "controllability_rank": 2 if gamma > 0 else 0,
        "controllability_det": dec(det), "hypoelliptic_for_t_positive": bool(gamma > 0),
    }


def gibbs_row(case_id: str, omega: Fraction, beta: Fraction) -> dict:
    om, be = mpq(omega), mpq(beta)
    return {
        "case_id": case_id, "omega": ftext(omega), "beta": ftext(beta),
        "normalization": dec(be * om / (2 * mp.pi)),
        "variance_Q": dec(1 / (be * om * om)), "variance_P": dec(1 / be),
        "covariance_det": dec(1 / (be * be * om * om)),
        "energy_temperature_identity": dec(be * (mpq(omega) * mpq(omega) * (1 / (be * om * om)) + 1 / be)),
    }


def boundary_row(case_id: str, omega: Fraction, beta: Fraction, gamma: Fraction, classification: str, stationary: str, mixing: str) -> dict:
    return {
        "case_id": case_id, "omega": ftext(omega), "beta": ftext(beta), "gamma": ftext(gamma),
        "classification": classification, "stationary_law": stationary, "mixing": mixing,
        "position_variance": "infinite" if omega == 0 else ftext(Fraction(1, 1) / (beta * omega * omega)),
    }


REGIME_CASES = [
    ("under_short", Fraction(1), Fraction(2), Fraction(1), Fraction(1, 3)),
    ("under_long", Fraction(3, 2), Fraction(5, 2), Fraction(1), Fraction(7, 5)),
    ("critical", Fraction(1), Fraction(3), Fraction(2), Fraction(2, 5)),
    ("over_mild", Fraction(1), Fraction(2), Fraction(3), Fraction(3, 4)),
    ("over_strong", Fraction(2), Fraction(7, 3), Fraction(6), Fraction(5, 6)),
    ("zero_damping", Fraction(3, 2), Fraction(5), Fraction(0), Fraction(2, 3)),
]

TRANSITION_CASES = [
    ("tr_under", Fraction(1), Fraction(2), Fraction(1), Fraction(1, 2), Fraction(1, 3), Fraction(-2, 5)),
    ("tr_under2", Fraction(2), Fraction(3), Fraction(1), Fraction(4, 3), Fraction(-1, 2), Fraction(3, 4)),
    ("tr_critical", Fraction(1), Fraction(2), Fraction(2), Fraction(3, 5), Fraction(2), Fraction(-1, 3)),
    ("tr_over", Fraction(1), Fraction(2), Fraction(3), Fraction(2, 3), Fraction(-1), Fraction(1, 2)),
    ("tr_over2", Fraction(3, 2), Fraction(4), Fraction(5), Fraction(7, 6), Fraction(1, 2), Fraction(2)),
    ("tr_zero_damping", Fraction(2), Fraction(3), Fraction(0), Fraction(5, 7), Fraction(1, 3), Fraction(-4, 5)),
    ("tr_small_time", Fraction(5, 2), Fraction(7, 2), Fraction(1, 2), Fraction(1, 20), Fraction(0), Fraction(0)),
    ("tr_long_time", Fraction(1), Fraction(5), Fraction(4), Fraction(11, 4), Fraction(3, 2), Fraction(-1, 2)),
]

CORRELATION_CASES = [
    ("corr_under", Fraction(1), Fraction(2), Fraction(1), Fraction(1, 3)),
    ("corr_critical", Fraction(1), Fraction(2), Fraction(2), Fraction(1, 2)),
    ("corr_over", Fraction(1), Fraction(2), Fraction(3), Fraction(2, 3)),
    ("corr_over2", Fraction(2), Fraction(3), Fraction(7), Fraction(4, 5)),
    ("corr_zero", Fraction(3, 2), Fraction(5), Fraction(0), Fraction(2, 5)),
]

RATE_CASES = [
    ("rate_zero", Fraction(1), Fraction(2), Fraction(0)),
    ("rate_under", Fraction(1), Fraction(2), Fraction(1)),
    ("rate_under_near", Fraction(1), Fraction(2), Fraction(19, 10)),
    ("rate_critical", Fraction(1), Fraction(2), Fraction(2)),
    ("rate_over", Fraction(1), Fraction(2), Fraction(3)),
    ("rate_over_strong", Fraction(1), Fraction(2), Fraction(8)),
    ("rate_scaled", Fraction(3), Fraction(7, 2), Fraction(6)),
]

KALMAN_CASES = [
    ("kalman_zero", Fraction(1), Fraction(2), Fraction(0)),
    ("kalman_under", Fraction(1), Fraction(2), Fraction(1)),
    ("kalman_critical", Fraction(1), Fraction(2), Fraction(2)),
    ("kalman_over", Fraction(1), Fraction(2), Fraction(3)),
    ("kalman_scaled", Fraction(5, 2), Fraction(7, 3), Fraction(9, 2)),
]

GIBBS_CASES = [
    ("gibbs_unit", Fraction(1), Fraction(1)),
    ("gibbs_soft", Fraction(1, 2), Fraction(3, 2)),
    ("gibbs_stiff", Fraction(3), Fraction(5)),
    ("gibbs_rational", Fraction(5, 2), Fraction(7, 3)),
]

BOUNDARY_CASES = [
    ("boundary_under", Fraction(1), Fraction(2), Fraction(1), "confining_hypoelliptic_underdamped", "unique_gibbs", "mixing"),
    ("boundary_critical", Fraction(1), Fraction(2), Fraction(2), "confining_hypoelliptic_critical", "unique_gibbs", "mixing_with_t_prefactor"),
    ("boundary_over", Fraction(1), Fraction(2), Fraction(3), "confining_hypoelliptic_overdamped", "unique_gibbs", "mixing"),
    ("boundary_zero_gamma", Fraction(1), Fraction(2), Fraction(0), "hamiltonian_oscillator", "many_invariant_energy_measures", "no_mixing"),
    ("boundary_zero_omega", Fraction(0), Fraction(2), Fraction(1), "unconfined_position", "no_probability_gibbs_law", "no_stationary_position"),
]


def build() -> dict:
    data = {
        "schema": "hcs-c237-kramers-harmonic-mehler-v1",
        "candidate_id": "HCS-C237", "evaluation_date": "2026-08-29", "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The harmonic Kramers--Langevin diffusion has an exact all-damping matrix flow and Gaussian Mehler kernel, Gibbs invariant law, Kalman hypoellipticity for positive damping, stationary correlations, and a sharp critical-damping drift rate.",
        "frozen_object": {
            "sde": "dQ=P dt; dP=(-omega^2 Q-gamma P)dt+sqrt(2 gamma/beta)dW_t",
            "drift_matrix": "A=[[0,1],[-omega^2,-gamma]]",
            "state": "x=(Q,P)^T in R^2",
            "parameter_domain": "omega>0,beta>0,gamma>=0; omega=0 is a separate unconfined boundary",
            "clock": "physical time t>=0",
            "gibbs_covariance": "Sigma=diag(1/(beta omega^2),1/beta)",
            "transition": "X_t is Gaussian with mean M_t x and covariance Sigma-M_t Sigma M_t^T for gamma>0,t>0; Dirac when gamma=0",
            "normalization": "Gibbs density beta omega/(2 pi) exp[-beta(omega^2 Q^2+P^2)/2]",
            "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisor/functional equation, Hilbert-Polya operators",
        },
        "theorem": {
            "matrix_exponential": "For A=[[0,1],[-omega^2,-gamma]], M_t=exp(tA) is e^{-gamma t/2}[[c+alpha s,s],[-omega^2 s,c-alpha s]], with alpha=gamma/2 and (c,s)=(cos(nu t),sin(nu t)/nu) underdamped, (1,t) critical, or (cosh(delta t),sinh(delta t)/delta) overdamped.",
            "covariance_mehler": "For gamma>0, X_t|X_0=x is N(M_t x,Sigma-M_t Sigma M_t^T), where Sigma=diag(1/(beta omega^2),1/beta); the covariance is positive definite for every t>0. At gamma=0 it is identically zero.",
            "gibbs_invariant": "The centered Gaussian Gibbs law with covariance Sigma and density beta omega/(2 pi) exp[-beta(omega^2 Q^2+P^2)/2] is invariant; it is unique when gamma>0 and omega>0.",
            "kalman_hypoellipticity": "With B=(0,sqrt(2 gamma/beta))^T, [B,AB] has determinant -2 gamma/beta and rank two exactly when gamma>0, giving a smooth positive Gaussian kernel for t>0.",
            "correlations": "Under Gibbs stationarity, Cov(X_t,X_0)=M_t Sigma, hence C_QQ=m11/(beta omega^2), C_QP=m12/beta, C_PQ=m21/(beta omega^2), and C_PP=m22/beta.",
            "rate_atlas": "The drift eigenvalues are -gamma/2 plus or minus sqrt(gamma^2/4-omega^2); the spectral-abscissa decay rate is r=gamma/2 for 0<=gamma<=2 omega and r=gamma/2-sqrt(gamma^2/4-omega^2) for gamma>=2 omega. At gamma=2 omega, M_t has a t exp(-omega t) prefactor and r is maximized at omega.",
            "zero_damping": "At gamma=0 the flow is the deterministic Hamiltonian oscillator, Sigma is preserved but no noise, irreducibility, or mixing is present.",
            "zero_frequency_boundary": "At omega=0 the position is unconfined and no finite Gibbs probability with the displayed covariance exists; this is not silently included in the omega>0 theorem.",
            "l2_boundary": "No full nonnormal L2 spectral decomposition is claimed; only the finite-dimensional drift, Gaussian kernel, invariant covariance and stated correlation/rate identities are certified.",
        },
        "regression": {
            "regime_rows": [matrix_row(*row) for row in REGIME_CASES],
            "transition_rows": [transition_row(*row) for row in TRANSITION_CASES],
            "correlation_rows": [correlation_row(*row) for row in CORRELATION_CASES],
            "rate_rows": [rate_row(*row) for row in RATE_CASES],
            "kalman_rows": [kalman_row(*row) for row in KALMAN_CASES],
            "gibbs_rows": [gibbs_row(*row) for row in GIBBS_CASES],
            "boundary_rows": [boundary_row(*row) for row in BOUNDARY_CASES],
            "working_decimal_digits": 90, "serialized_significant_digits": 64,
        },
        "exact_identities": [
            {"name": "characteristic_polynomial", "formula": "det(lambda I-A)=lambda^2+gamma lambda+omega^2"},
            {"name": "matrix_ode", "formula": "dM_t/dt=A M_t=M_t A and M_0=I"},
            {"name": "determinant_flow", "formula": "det M_t=exp(-gamma t)"},
            {"name": "lyapunov_covariance", "formula": "A Sigma+Sigma A^T+BB^T=0 and integral_0^t M_s BB^T M_s^T ds=Sigma-M_t Sigma M_t^T"},
            {"name": "gibbs_density", "formula": "pi(q,p)=beta omega/(2 pi) exp[-beta(omega^2 q^2+p^2)/2]"},
            {"name": "kalman_determinant", "formula": "det[B,AB]=-2 gamma/beta"},
            {"name": "stationary_cross_covariance", "formula": "Cov(X_t,X_0)=M_t Sigma"},
            {"name": "rate_piecewise", "formula": "r=gamma/2 for gamma<=2 omega; r=gamma/2-sqrt(gamma^2/4-omega^2) for gamma>=2 omega"},
            {"name": "critical_prefactor", "formula": "M_t=exp(-omega t)[I+t(A+omega I)] when gamma=2 omega"},
            {"name": "hamiltonian_face", "formula": "gamma=0 implies M_t Sigma M_t^T=Sigma and transition covariance zero"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
            "strongest_positive": "Exact all-damping Gaussian and drift identities are source-local and independently testable.",
            "strongest_failure": "The diffusion has no intrinsic rational-prime primitive carrier, prime-power repetition law, target divisor, or Hilbert--Polya operator.",
        },
        "scope_flags": {
            "uses_target_zero_table": False, "uses_prime_table": False, "claims_arithmetic_local_data": False,
            "claims_euler_factors": False, "claims_root_numbers": False, "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False, "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "citations": [
            {"id": "Kramers1940", "doi": "10.1016/S0031-8914(40)90098-2", "role": "classical Brownian escape/Langevin context"},
            {"id": "OrnsteinUhlenbeck1930", "doi": "10.1103/PhysRev.36.823", "role": "linear Gaussian Markov process and Mehler transition context"},
            {"id": "Hormander1967", "doi": "10.1007/BF02392081", "role": "hypoelliptic bracket condition framework"},
            {"id": "Villani2009", "doi": "", "role": "hypocoercivity context; no unproved L2 spectral theorem imported"},
        ],
        "nonclaims": [
            "No prime or zero table is used and no arithmetic local datum is inferred from the damping parameter.",
            "The Mehler kernel is a Gaussian Markov transition, not a primitive-orbit zeta or target Fredholm determinant.",
            "The critical rate is a finite-dimensional drift statement; it is not a complete nonnormal L2 spectrum.",
            "The gamma=0 and omega=0 faces are explicit boundaries and do not inherit the positive-damping Gibbs theorem.",
            "Internal exact checks and manuscript builds are reproducibility evidence, not external peer review.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = build()
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": "C237_PRODUCER_PASS", "output": str(args.output), "payload_sha256": data["payload_sha256"], "bytes": args.output.stat().st_size}, sort_keys=True))


if __name__ == "__main__":
    main()
