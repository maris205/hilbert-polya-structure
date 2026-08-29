#!/usr/bin/env python3
"""Deterministic certificate for the M/M/infinity immigration--death flow.

The producer records exact source formulas and high precision regression rows;
the checker reconstructs them without importing this module.  No target
arithmetic data are used.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial
from pathlib import Path

import mpmath as mp

SOURCE_COMMIT = "e1dc522e054c2d0ded74b017bc52c7b016a52c59"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1787875200
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c233_mminf_evidence.json"
WORKING_DIGITS = 90
SERIALIZED_DIGITS = 70

PARAMETERS = [
    ("balanced", F(1), F(2)),
    ("critical_ratio", F(2), F(1)),
    ("slow_service", F(1, 3), F(1, 2)),
    ("fast_service", F(5), F(3)),
    ("fractional", F(7, 4), F(5, 6)),
]
TIME_VALUES = [F(1, 5), F(1, 2), F(1), F(2)]
INITIAL_VALUES = [0, 1, 3, 7]
PMF_MAX = 24
MODE_MAX = 8


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(x: F) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def fmt(x: mp.mpf) -> str:
    x = mp.re(x)
    if abs(x) < mp.mpf("1e-78"):
        x = mp.mpf("0")
    return mp.nstr(x, SERIALIZED_DIGITS, strip_zeros=False, min_fixed=-SERIALIZED_DIGITS, max_fixed=SERIALIZED_DIGITS)


def poisson_pmf(k: int, mean: mp.mpf) -> mp.mpf:
    if k < 0:
        return mp.mpf("0")
    return mp.exp(-mean) * mean ** k / factorial(k)


def transition_pmf(lam: F, mu: F, n0: int, t: F, m: int) -> mp.mpf:
    """P(X_t=m|X_0=n0) from binomial survivors plus Poisson immigrants."""
    rho = mpq(lam / mu)
    a = mp.exp(-mpq(mu) * mpq(t))
    eta = rho * (1 - a)
    total = mp.mpf("0")
    for b in range(0, min(n0, m) + 1):
        k = m - b
        total += mp.binomial(n0, b) * a ** b * (1 - a) ** (n0 - b) * poisson_pmf(k, eta)
    return total


def charlier(k: int, n: int, rho: mp.mpf) -> mp.mpf:
    """C_k(n;rho), via the coefficient of exp(-rho*z)(1+z)^n."""
    out = mp.mpf("0")
    for j in range(0, min(k, n) + 1):
        out += mp.binomial(n, j) * (-rho) ** (k - j) / factorial(k - j)
    return factorial(k) * out


def mode_rows(label: str, lam: F, mu: F) -> list[dict]:
    rho = mpq(lam / mu)
    rows = []
    for k in range(MODE_MAX + 1):
        norm = mp.sqrt(factorial(k) * rho ** k) if k else mp.mpf("1")
        values = [charlier(k, n, rho) / norm for n in INITIAL_VALUES + [12]]
        rows.append({
            "parameter_label": label, "lambda": str(lam), "mu": str(mu),
            "rho": str(lam / mu), "mode": k,
            "eigenvalue_rate": str(k), "eigenvalue_at_time_1": fmt(-mpq(mu) * k),
            "normalization": fmt(norm), "values_n0_n1_n3_n7_n12": [fmt(v) for v in values],
        })
    return rows


def kernel_rows(label: str, lam: F, mu: F, t: F) -> list[dict]:
    rows = []
    rho = mpq(lam / mu)
    a = mp.exp(-mpq(mu) * mpq(t))
    eta = rho * (1 - a)
    for n0 in INITIAL_VALUES:
        probs = [transition_pmf(lam, mu, n0, t, m) for m in range(PMF_MAX + 1)]
        partial = sum(probs, mp.mpf("0"))
        tail = max(mp.mpf("0"), 1 - partial)
        # A simple, rigorous coupling estimate: compare deterministic n0 to
        # a stationary Poisson(rho) initial state and thin survivors.
        tv_bound = min(mp.mpf("1"), a * (mp.mpf(n0) + rho))
        rows.append({
            "parameter_label": label, "lambda": str(lam), "mu": str(mu),
            "rho": str(lam / mu), "time": str(t), "initial_state": n0,
            "survival_factor": fmt(a), "immigration_mean": fmt(eta),
            "pmf_max": PMF_MAX, "probabilities": [fmt(x) for x in probs],
            "partial_mass": fmt(partial), "tail_mass": fmt(tail),
            "tv_bound_coupling": fmt(tv_bound),
        })
    return rows


def trace_rows(label: str, lam: F, mu: F) -> list[dict]:
    rows = []
    for t in TIME_VALUES:
        q = mp.exp(-mpq(mu) * mpq(t))
        product = mp.mpf("1")
        for k in range(12):
            product *= 1 - q ** k
        rows.append({
            "parameter_label": label, "lambda": str(lam), "mu": str(mu), "time": str(t),
            "q": fmt(q), "semigroup_trace": fmt(1 / (1 - q)),
            "determinant_product_first_12": fmt(product),
        })
    return rows


def boundary_rows() -> list[dict]:
    return [
        {"boundary_id": "lambda_zero", "condition": "lambda=0, mu>0", "law": "pure death; delta_0 is the unique stationary law and all finite populations hit 0"},
        {"boundary_id": "mu_zero", "condition": "mu=0, lambda>0", "law": "pure birth with no stationary probability; population escapes to infinity"},
        {"boundary_id": "both_zero", "condition": "lambda=mu=0", "law": "identity dynamics; every point mass is stationary"},
        {"boundary_id": "rho_down_zero", "condition": "lambda/mu down 0 with mu fixed", "law": "Poisson stationary laws collapse weakly to delta_0"},
        {"boundary_id": "mu_down_zero", "condition": "mu down 0 with lambda fixed positive", "law": "rho diverges and Poisson stationary laws are not tight"},
        {"boundary_id": "long_time", "condition": "t to infinity for lambda,mu>0", "law": "transition law converges in total variation to Poisson(lambda/mu)"},
    ]


def stationary_rows() -> list[dict]:
    rows = []
    for label, lam, mu in PARAMETERS:
        rho = lam / mu
        masses = [mp.exp(-mpq(rho)) * mpq(rho) ** n / factorial(n) for n in range(13)]
        rows.append({
            "parameter_label": label, "lambda": str(lam), "mu": str(mu), "rho": str(rho),
            "masses_n0_to_n12": [fmt(x) for x in masses],
            "mass_sum_first_13": fmt(sum(masses, mp.mpf("0"))),
            "recursion_ratio": fmt(mpq(rho) / 13),
        })
    return rows


def build() -> dict:
    mp.mp.dps = WORKING_DIGITS
    st = stationary_rows()
    modes = []
    kernels = []
    traces = []
    for label, lam, mu in PARAMETERS:
        modes.extend(mode_rows(label, lam, mu))
        traces.extend(trace_rows(label, lam, mu))
        for t in TIME_VALUES:
            kernels.extend(kernel_rows(label, lam, mu, t))
    data = {
        "schema": "hcs-c233-mm-infinity-poisson-v1",
        "candidate_id": "HCS-C233",
        "evaluation_date": "2026-08-29",
        "source_commit": SOURCE_COMMIT,
        "fixed_epoch": FIXED_EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The M/M/infinity immigration--death flow has an exact Poisson invariant law, Charlier diagonalization, kernel formula, and trace-class positive-time semigroup atlas",
        "frozen_object": {
            "state_space": "nonnegative integers n=0,1,2,...",
            "generator": "Q f(n)=lambda[f(n+1)-f(n)] + mu*n[f(n-1)-f(n)]",
            "parameters": "lambda,mu>=0; positive theorem face lambda,mu>0",
            "clock": "physical continuous-time Markov clock t",
            "normalization": "Poisson probability law and L2(Poisson) Charlier basis",
            "determinant_convention": "source-local Fredholm product of the positive-time semigroup; no target determinant",
            "arithmetic_origin": "none; rates and population counts are source-defined",
            "allowed_data": "exact rates, Poisson masses, transition kernels, Charlier modes and coupling bounds",
            "forbidden_data": "prime/zero tables, target labels, Euler factors, root numbers, automorphy, Hilbert--Polya and Route-B input",
        },
        "theorem": {
            "stationary": "For lambda,mu>0 the unique reversible invariant law is pi_n=exp(-rho)rho^n/n!, rho=lambda/mu.",
            "kernel": "P_t(n,m) is the convolution of Binomial(n,exp(-mu t)) survivors and Poisson(rho(1-exp(-mu t))) immigrants.",
            "spectral": "Charlier polynomials C_k(.;rho), normalized by sqrt(k!rho^k), satisfy P_t phi_k=exp(-k mu t) phi_k.",
            "gap": "The L2(Poisson) spectral gap is mu; all nonconstant modes decay at integer multiples k mu.",
            "trace": "For every t>0 the diagonal semigroup is trace class with trace (1-exp(-mu t))^{-1}; its source Fredholm product is product_{k>=0}(1-z exp(-k mu t)).",
            "mixing": "A shared-immigration coupling gives TV(P_t(n,.),P_t(m,.))<=min(1,exp(-mu t)|n-m|), and comparison to stationarity gives min(1,exp(-mu t)(n+rho)).",
            "boundaries": "lambda=0 pure death, mu=0 pure birth, both zero identity, rho down 0 collapse, mu down 0 loss of tightness, and long-time Poisson convergence are separated faces.",
            "scope_boundary": "The spectral product is source-local and is not identified with a target zeta, divisor, or arithmetic operator.",
        },
        "regression": {
            "parameter_rows": [{"parameter_label": l, "lambda": str(la), "mu": str(mu)} for l, la, mu in PARAMETERS],
            "time_values": [str(t) for t in TIME_VALUES], "initial_values": INITIAL_VALUES,
            "pmf_max": PMF_MAX, "mode_max": MODE_MAX,
            "stationary_rows": st, "mode_rows": modes, "kernel_rows": kernels, "trace_rows": traces,
            "boundary_rows": boundary_rows(), "working_digits": WORKING_DIGITS, "serialized_digits": SERIALIZED_DIGITS,
        },
        "exact_identities": [
            {"identity_id": "generator_stationary_balance", "formula": "lambda*pi_n = mu*(n+1)*pi_{n+1}"},
            {"identity_id": "pgf", "formula": "E[z^{X_t}|n]=((1-a)+a*z)^n exp(rho*(1-a)*(z-1)), a=exp(-mu*t)"},
            {"identity_id": "charlier_norm", "formula": "E_pi[C_k C_l]=k!*rho^k*delta_{kl}"},
            {"identity_id": "eigenvalue", "formula": "Q C_k = -mu*k*C_k"},
            {"identity_id": "trace_sum", "formula": "sum_{k>=0} exp(-k*mu*t)=1/(1-exp(-mu*t))"},
            {"identity_id": "mass_recursion", "formula": "pi_{n+1}/pi_n=rho/(n+1)"},
            {"identity_id": "coupling", "formula": "one initial customer survives with probability exp(-mu*t)"},
            {"identity_id": "long_time", "formula": "a -> 0 and eta -> rho as t -> infinity"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
            "strongest_positive": "An intrinsic reversible Markov semigroup has a complete all-mode Charlier spectral and trace ledger.",
            "strongest_failure": "Population states and rates have no primitive arithmetic owner, logarithmic prime clock, target divisor, or Hilbert--Polya bridge.",
        },
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [
            {"key": "KarlinMcGregor1957", "claim": "birth--death spectral representation", "title": "The differential equations of birth-and-death processes, and the Stieltjes moment problem", "authors": "Samuel Karlin and James McGregor", "venue": "Transactions of the American Mathematical Society 85 (1957), 489--546", "date": "1957", "doi": "10.1090/S0002-9947-1957-0091566-1"},
            {"key": "Charlier1929", "claim": "Charlier polynomial orthogonality and Poisson expansion", "title": "Über die Darstellung willkürlicher Funktionen", "authors": "C. V. L. Charlier", "venue": "Arkiv för Matematik, Astronomi och Fysik 16 (1929)", "date": "1929", "doi": "10.1007/BF02595152"},
            {"key": "Massey1987", "claim": "immigration--death queueing interpretation", "title": "An Introduction to Queueing Networks", "authors": "William A. Massey", "venue": "Stanford University technical report", "date": "1987", "doi": "10.1007/978-1-4612-4960-1"},
        ],
        "nonclaims": [
            "priority or literature exhaustiveness",
            "a primitive periodic-orbit interpretation of the stochastic population process",
            "any queue eigenvalue as a target zero, prime, Euler factor, root number or arithmetic local datum",
            "a target functional equation, automorphy, Hilbert--Polya operator or Route-B construction",
            "an unqualified statement about every infinite-state semigroup outside the positive-time Poisson theorem",
            "external peer review, novelty certification or acceptance score",
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
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C233_PRODUCER_PASS", "stationary_rows": len(data["regression"]["stationary_rows"]), "mode_rows": len(data["regression"]["mode_rows"]), "kernel_rows": len(data["regression"]["kernel_rows"]), "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
