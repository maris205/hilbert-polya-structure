#!/usr/bin/env python3
"""Producer-independent checker for the HCS-C237 certificate."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c237_kramers_evidence.json"
SOURCE_COMMIT = "0ebc633706bc34b8b915a44749423486fd4cd243"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
mp.mp.dps = 90

TOP_KEYS = {"schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
SCOPE_KEYS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}
HEADLINE = "The harmonic Kramers--Langevin diffusion has an exact all-damping matrix flow and Gaussian Mehler kernel, Gibbs invariant law, Kalman hypoellipticity for positive damping, stationary correlations, and a sharp critical-damping drift rate."
FROZEN = {
    "sde": "dQ=P dt; dP=(-omega^2 Q-gamma P)dt+sqrt(2 gamma/beta)dW_t",
    "drift_matrix": "A=[[0,1],[-omega^2,-gamma]]",
    "state": "x=(Q,P)^T in R^2",
    "parameter_domain": "omega>0,beta>0,gamma>=0; omega=0 is a separate unconfined boundary",
    "clock": "physical time t>=0",
    "gibbs_covariance": "Sigma=diag(1/(beta omega^2),1/beta)",
    "transition": "X_t is Gaussian with mean M_t x and covariance Sigma-M_t Sigma M_t^T for gamma>0,t>0; Dirac when gamma=0",
    "normalization": "Gibbs density beta omega/(2 pi) exp[-beta(omega^2 Q^2+P^2)/2]",
    "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisor/functional equation, Hilbert-Polya operators",
}
THEOREM = {
    "matrix_exponential": "For A=[[0,1],[-omega^2,-gamma]], M_t=exp(tA) is e^{-gamma t/2}[[c+alpha s,s],[-omega^2 s,c-alpha s]], with alpha=gamma/2 and (c,s)=(cos(nu t),sin(nu t)/nu) underdamped, (1,t) critical, or (cosh(delta t),sinh(delta t)/delta) overdamped.",
    "covariance_mehler": "For gamma>0, X_t|X_0=x is N(M_t x,Sigma-M_t Sigma M_t^T), where Sigma=diag(1/(beta omega^2),1/beta); the covariance is positive definite for every t>0. At gamma=0 it is identically zero.",
    "gibbs_invariant": "The centered Gaussian Gibbs law with covariance Sigma and density beta omega/(2 pi) exp[-beta(omega^2 Q^2+P^2)/2] is invariant; it is unique when gamma>0 and omega>0.",
    "kalman_hypoellipticity": "With B=(0,sqrt(2 gamma/beta))^T, [B,AB] has determinant -2 gamma/beta and rank two exactly when gamma>0, giving a smooth positive Gaussian kernel for t>0.",
    "correlations": "Under Gibbs stationarity, Cov(X_t,X_0)=M_t Sigma, hence C_QQ=m11/(beta omega^2), C_QP=m12/beta, C_PQ=m21/(beta omega^2), and C_PP=m22/beta.",
    "rate_atlas": "The drift eigenvalues are -gamma/2 plus or minus sqrt(gamma^2/4-omega^2); the spectral-abscissa decay rate is r=gamma/2 for 0<=gamma<=2 omega and r=gamma/2-sqrt(gamma^2/4-omega^2) for gamma>=2 omega. At gamma=2 omega, M_t has a t exp(-omega t) prefactor and r is maximized at omega.",
    "zero_damping": "At gamma=0 the flow is the deterministic Hamiltonian oscillator, Sigma is preserved but no noise, irreducibility, or mixing is present.",
    "zero_frequency_boundary": "At omega=0 the position is unconfined and no finite Gibbs probability with the displayed covariance exists; this is not silently included in the omega>0 theorem.",
    "l2_boundary": "No full nonnormal L2 spectral decomposition is claimed; only the finite-dimensional drift, Gaussian kernel, invariant covariance and stated correlation/rate identities are certified.",
}
IDENTITIES = [
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
]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def frac(value: str | int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def mpfrac(value: str | int | Fraction) -> mp.mpf:
    z = frac(value)
    return mp.mpf(z.numerator) / z.denominator


def dec(value: mp.mpf, digits: int = 64) -> str:
    if abs(value) < mp.mpf("1e-82"):
        return "0.0"
    return mp.nstr(value, digits, strip_zeros=False, min_fixed=-70, max_fixed=70)


def regime(omega: Fraction, gamma: Fraction) -> str:
    if gamma == 0:
        return "underdamped_zero_damping"
    if gamma * gamma < 4 * omega * omega:
        return "underdamped"
    if gamma * gamma == 4 * omega * omega:
        return "critical"
    return "overdamped"


def matrix_exp(omega: Fraction, gamma: Fraction, time: Fraction) -> list[list[mp.mpf]]:
    om, ga, t = mpfrac(omega), mpfrac(gamma), mpfrac(time)
    alpha = ga / 2
    disc = alpha * alpha - om * om
    if disc < 0:
        nu = mp.sqrt(-disc); c = mp.cos(nu * t); s = mp.sin(nu * t) / nu
    elif disc == 0:
        c = mp.mpf(1); s = t
    else:
        delta = mp.sqrt(disc); c = mp.cosh(delta * t); s = mp.sinh(delta * t) / delta
    e = mp.exp(-alpha * t)
    return [[e * (c + alpha * s), e * s], [e * (-om * om * s), e * (c - alpha * s)]]


def sigma(omega: Fraction, beta: Fraction) -> list[list[mp.mpf]]:
    om, be = mpfrac(omega), mpfrac(beta)
    return [[1 / (be * om * om), mp.mpf(0)], [mp.mpf(0), 1 / be]]


def mmul(a: list[list[mp.mpf]], b: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def tr(a: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    return [[a[j][i] for j in range(2)] for i in range(2)]


def cov(omega: Fraction, beta: Fraction, gamma: Fraction, time: Fraction, m: list[list[mp.mpf]] | None = None) -> list[list[mp.mpf]]:
    if gamma == 0:
        return [[mp.mpf(0), mp.mpf(0)], [mp.mpf(0), mp.mpf(0)]]
    M = matrix_exp(omega, gamma, time) if m is None else m
    S = sigma(omega, beta); MS = mmul(mmul(M, S), tr(M))
    return [[S[i][j] - MS[i][j] for j in range(2)] for i in range(2)]


def eig(omega: Fraction, gamma: Fraction) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    om, ga = mpfrac(omega), mpfrac(gamma); a = ga / 2; d = a * a - om * om
    if d < 0:
        return -a, -a, mp.sqrt(-d)
    if d == 0:
        return -a, -a, mp.mpf(0)
    z = mp.sqrt(d)
    return -a + z, -a - z, mp.mpf(0)


def rate(omega: Fraction, gamma: Fraction) -> mp.mpf:
    om, ga = mpfrac(omega), mpfrac(gamma)
    if ga == 0: return mp.mpf(0)
    a = ga / 2
    return a if ga <= 2 * om else a - mp.sqrt(a * a - om * om)


class Audit:
    def __init__(self) -> None: self.count = 0
    def check(self, ok: bool, msg: str) -> None:
        self.count += 1
        if not ok: raise AssertionError(msg)


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
GIBBS_CASES = [("gibbs_unit", Fraction(1), Fraction(1)), ("gibbs_soft", Fraction(1, 2), Fraction(3, 2)), ("gibbs_stiff", Fraction(3), Fraction(5)), ("gibbs_rational", Fraction(5, 2), Fraction(7, 3))]
BOUNDARY_CASES = [
    ("boundary_under", Fraction(1), Fraction(2), Fraction(1),
     "confining_hypoelliptic_underdamped", "unique_gibbs", "mixing"),
    ("boundary_critical", Fraction(1), Fraction(2), Fraction(2),
     "confining_hypoelliptic_critical", "unique_gibbs", "mixing_with_t_prefactor"),
    ("boundary_over", Fraction(1), Fraction(2), Fraction(3),
     "confining_hypoelliptic_overdamped", "unique_gibbs", "mixing"),
    ("boundary_zero_gamma", Fraction(1), Fraction(2), Fraction(0),
     "hamiltonian_oscillator", "many_invariant_energy_measures", "no_mixing"),
    ("boundary_zero_omega", Fraction(0), Fraction(2), Fraction(1),
     "unconfined_position", "no_probability_gibbs_law", "no_stationary_position"),
]


def validate(data: dict) -> int:
    a = Audit()
    a.check(set(data) == TOP_KEYS, "top-level schema closure")
    a.check(data["schema"] == "hcs-c237-kramers-harmonic-mehler-v1", "schema")
    a.check(data["candidate_id"] == "HCS-C237", "candidate")
    a.check(data["evaluation_date"] == "2026-08-29", "date")
    a.check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    a.check(data["scope_literal"] == SCOPE, "scope")
    a.check(data["evaluator"] == {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator")
    a.check(data["headline"] == HEADLINE, "headline")
    a.check(data["frozen_object"] == FROZEN, "frozen object")
    a.check(data["theorem"] == THEOREM, "theorem lock")
    a.check(data["exact_identities"] == IDENTITIES, "identity lock")
    a.check(data["payload_sha256"] == payload_hash(data), "payload hash")
    r = data["regression"]
    a.check(set(r) == {"regime_rows", "transition_rows", "correlation_rows", "rate_rows", "kalman_rows", "gibbs_rows", "boundary_rows", "working_decimal_digits", "serialized_significant_digits"}, "regression keys")
    a.check(r["working_decimal_digits"] == 90 and r["serialized_significant_digits"] == 64, "precision lock")

    # Matrix/exponential rows.
    a.check(len(r["regime_rows"]) == len(REGIME_CASES), "regime count")
    mkeys = {"case_id", "omega", "beta", "gamma", "time", "regime", "alpha", "m11", "m12", "m21", "m22", "det_M", "trace_M", "eigen_plus_real", "eigen_minus_real", "eigen_imag_abs"}
    for row, (cid, om, be, ga, t) in zip(r["regime_rows"], REGIME_CASES):
        a.check(set(row) == mkeys, f"matrix keys {cid}")
        a.check(row["case_id"] == cid, f"matrix id {cid}")
        a.check(tuple(frac(row[z]) for z in ("omega", "beta", "gamma", "time")) == (om, be, ga, t), f"matrix parameters {cid}")
        a.check(row["regime"] == regime(om, ga), f"regime {cid}")
        M = matrix_exp(om, ga, t); ep, em, ii = eig(om, ga)
        for key, value in (("m11", M[0][0]), ("m12", M[0][1]), ("m21", M[1][0]), ("m22", M[1][1]), ("det_M", mp.exp(-mpfrac(ga) * mpfrac(t))), ("trace_M", M[0][0] + M[1][1]), ("eigen_plus_real", ep), ("eigen_minus_real", em), ("eigen_imag_abs", abs(ii))):
            a.check(row[key] == dec(value), f"matrix value {cid}/{key}")

    # Gaussian transitions and covariance closure.
    a.check(len(r["transition_rows"]) == len(TRANSITION_CASES), "transition count")
    tkeys = {"case_id", "omega", "beta", "gamma", "time", "q0", "p0", "regime", "mean_q", "mean_p", "cov_qq", "cov_qp", "cov_pp", "cov_det", "det_M", "covariance_positive_definite"}
    for row, (cid, om, be, ga, t, q0, p0) in zip(r["transition_rows"], TRANSITION_CASES):
        a.check(set(row) == tkeys, f"transition keys {cid}")
        a.check(row["case_id"] == cid, f"transition id {cid}")
        a.check(tuple(frac(row[z]) for z in ("omega", "beta", "gamma", "time", "q0", "p0")) == (om, be, ga, t, q0, p0), f"transition params {cid}")
        a.check(row["regime"] == regime(om, ga), f"transition regime {cid}")
        M = matrix_exp(om, ga, t); C = cov(om, be, ga, t, M)
        muq = M[0][0] * mpfrac(q0) + M[0][1] * mpfrac(p0)
        mup = M[1][0] * mpfrac(q0) + M[1][1] * mpfrac(p0)
        detc = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        for key, value in (("mean_q", muq), ("mean_p", mup), ("cov_qq", C[0][0]), ("cov_qp", C[0][1]), ("cov_pp", C[1][1]), ("cov_det", detc), ("det_M", mp.exp(-mpfrac(ga) * mpfrac(t)))):
            a.check(row[key] == dec(value), f"transition value {cid}/{key}")
        a.check(row["covariance_positive_definite"] is (ga > 0 and detc > mp.mpf("1e-70")), f"covariance flag {cid}")
        a.check(abs(C[0][1] - C[1][0]) < mp.mpf("1e-80"), f"covariance symmetry {cid}")

    # Stationary correlations.
    a.check(len(r["correlation_rows"]) == len(CORRELATION_CASES), "correlation count")
    ckeys = {"case_id", "omega", "beta", "gamma", "time", "regime", "C_QQ", "C_QP", "C_PQ", "C_PP", "rho_QQ", "rho_PP", "rho_QP", "rho_PQ"}
    for row, (cid, om, be, ga, t) in zip(r["correlation_rows"], CORRELATION_CASES):
        a.check(set(row) == ckeys, f"correlation keys {cid}")
        a.check(tuple(frac(row[z]) for z in ("omega", "beta", "gamma", "time")) == (om, be, ga, t), f"correlation params {cid}")
        M = matrix_exp(om, ga, t); omm, bem = mpfrac(om), mpfrac(be)
        sq, sp = 1 / (bem * omm * omm), 1 / bem
        expected = {"C_QQ": sq * M[0][0], "C_QP": sp * M[0][1], "C_PQ": sq * M[1][0], "C_PP": sp * M[1][1], "rho_QQ": M[0][0], "rho_PP": M[1][1], "rho_QP": omm * M[0][1], "rho_PQ": M[1][0] / omm}
        for key, value in expected.items(): a.check(row[key] == dec(value), f"correlation value {cid}/{key}")
        a.check(row["regime"] == regime(om, ga), f"correlation regime {cid}")

    # Rate and critical optimizer rows.
    a.check(len(r["rate_rows"]) == len(RATE_CASES), "rate count")
    rkeys = {"case_id", "omega", "beta", "gamma", "regime", "rate", "eigen_plus_real", "eigen_minus_real", "eigen_imag_abs", "critical_polynomial_prefactor", "rate_at_critical"}
    for row, (cid, om, be, ga) in zip(r["rate_rows"], RATE_CASES):
        a.check(set(row) == rkeys, f"rate keys {cid}")
        a.check(tuple(frac(row[z]) for z in ("omega", "beta", "gamma")) == (om, be, ga), f"rate params {cid}")
        ep, em, ii = eig(om, ga)
        a.check(row["regime"] == regime(om, ga), f"rate regime {cid}")
        a.check(row["rate"] == dec(rate(om, ga)), f"rate value {cid}")
        a.check(row["eigen_plus_real"] == dec(ep) and row["eigen_minus_real"] == dec(em) and row["eigen_imag_abs"] == dec(abs(ii)), f"rate eigen {cid}")
        a.check(row["critical_polynomial_prefactor"] is (ga == 2 * om), f"critical flag {cid}")
        a.check(row["rate_at_critical"] == dec(mpfrac(om)), f"critical benchmark {cid}")

    # Kalman controllability rows.
    a.check(len(r["kalman_rows"]) == len(KALMAN_CASES), "kalman count")
    kkeys = {"case_id", "omega", "beta", "gamma", "B", "AB", "controllability_rank", "controllability_det", "hypoelliptic_for_t_positive"}
    for row, (cid, om, be, ga) in zip(r["kalman_rows"], KALMAN_CASES):
        a.check(set(row) == kkeys, f"kalman keys {cid}")
        a.check(tuple(frac(row[z]) for z in ("omega", "beta", "gamma")) == (om, be, ga), f"kalman params {cid}")
        noise = mp.sqrt(2 * mpfrac(ga) / mpfrac(be)) if ga > 0 else mp.mpf(0)
        a.check(row["B"] == ["0.0", dec(noise)], f"B {cid}")
        a.check(row["AB"] == [dec(noise), dec(-mpfrac(ga) * noise)], f"AB {cid}")
        a.check(row["controllability_det"] == dec(-2 * mpfrac(ga) / mpfrac(be)), f"Kalman determinant {cid}")
        a.check(row["controllability_rank"] == (2 if ga > 0 else 0), f"Kalman rank {cid}")
        a.check(row["hypoelliptic_for_t_positive"] is (ga > 0), f"hypoellipticity flag {cid}")

    # Gibbs normalization rows.
    a.check(len(r["gibbs_rows"]) == len(GIBBS_CASES), "Gibbs count")
    gkeys = {"case_id", "omega", "beta", "normalization", "variance_Q", "variance_P", "covariance_det", "energy_temperature_identity"}
    for row, (cid, om, be) in zip(r["gibbs_rows"], GIBBS_CASES):
        a.check(set(row) == gkeys, f"Gibbs keys {cid}")
        a.check(tuple(frac(row[z]) for z in ("omega", "beta")) == (om, be), f"Gibbs params {cid}")
        omm, bem = mpfrac(om), mpfrac(be)
        a.check(row["normalization"] == dec(bem * omm / (2 * mp.pi)), f"Gibbs normalization {cid}")
        a.check(row["variance_Q"] == dec(1 / (bem * omm * omm)), f"Gibbs Q variance {cid}")
        a.check(row["variance_P"] == dec(1 / bem), f"Gibbs P variance {cid}")
        a.check(row["covariance_det"] == dec(1 / (bem * bem * omm * omm)), f"Gibbs determinant {cid}")
        equip = bem * (omm * omm * (1 / (bem * omm * omm)) + 1 / bem)
        a.check(row["energy_temperature_identity"] == dec(equip), f"equipartition {cid}")

    # Boundary rows are a semantic atlas, not merely a length/key smoke test.
    # Lock every row to its source-defined parameter sentinel and recompute the
    # variance/classification/stationarity/mixing labels independently.  In
    # particular, the first four rows must not be silently accepted when their
    # labels or parameters drift while the zero-frequency row remains intact.
    bkeys = {"case_id", "omega", "beta", "gamma", "classification", "stationary_law", "mixing", "position_variance"}
    br = r["boundary_rows"]
    a.check(len(br) == len(BOUNDARY_CASES), "boundary count")
    for row, (cid, om, be, ga, classification, stationary, mixing) in zip(br, BOUNDARY_CASES):
        a.check(set(row) == bkeys, f"boundary keys {cid}")
        a.check(row["case_id"] == cid, f"boundary id {cid}")
        a.check(tuple(frac(row[z]) for z in ("omega", "beta", "gamma")) == (om, be, ga), f"boundary parameters {cid}")
        a.check(row["classification"] == classification, f"boundary classification {cid}")
        a.check(row["stationary_law"] == stationary, f"boundary stationarity {cid}")
        a.check(row["mixing"] == mixing, f"boundary mixing {cid}")
        # Boundary variances are serialized as exact rational text (unlike
        # the high-precision decimal regression cells).
        expected_variance = "infinite" if om == 0 else str(Fraction(1, 1) / (be * om * om))
        a.check(row["position_variance"] == expected_variance, f"boundary variance {cid}")

    route = data["route_a"]
    a.check(set(route) == {"tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"}, "route keys")
    a.check(route["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    a.check(route["overall"] == "ROUTE_A_REJECTED" and route["route_b_invocation_allowed"] is False, "route verdict")
    a.check(set(data["scope_flags"]) == SCOPE_KEYS and all(value is False for value in data["scope_flags"].values()), "scope flags")
    expected_citations = [
        {"id": "Kramers1940", "doi": "10.1016/S0031-8914(40)90098-2", "role": "classical Brownian escape/Langevin context"},
        {"id": "OrnsteinUhlenbeck1930", "doi": "10.1103/PhysRev.36.823", "role": "linear Gaussian Markov process and Mehler transition context"},
        {"id": "Hormander1967", "doi": "10.1007/BF02392081", "role": "hypoelliptic bracket condition framework"},
        {"id": "Villani2009", "doi": "", "role": "hypocoercivity context; no unproved L2 spectral theorem imported"},
    ]
    a.check(data["citations"] == expected_citations, "citation ledger")
    a.check(len(data["nonclaims"]) == 5 and all(isinstance(v, str) for v in data["nonclaims"]), "nonclaims")
    return a.count


def main() -> None:
    data = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    count = validate(data)
    print(f"C237 independent checker: PASS ({count} assertions; payload_sha256={data['payload_sha256']})")


if __name__ == "__main__":
    main()
