#!/usr/bin/env python3
"""Canonical exact/high-precision ledger for the finite M/M/1/K queue.

The producer is deliberately a data generator, not the proof: the checker
reconstructs every formula independently. Rates are exact Fractions and all
serialized transcendental values use a fixed mpmath precision.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

SOURCE_COMMIT = "489672bd36abd3a4f6da92d1446a0af575917959"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1787875200
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c225_mm1k_evidence.json"
PARAMETERS = [
    ("subcritical", F(1), F(2)),
    ("critical", F(1), F(1)),
    ("supercritical", F(2), F(1)),
    ("asymmetric", F(3, 2), F(1)),
]
K_VALUES = [0, 1, 2, 4, 8]
TIME_VALUES = [F(1, 5), F(1, 2), F(1)]
LIMIT_K_VALUES = [4, 8, 16, 32]
WORKING_DIGITS = 100
SERIALIZED_DIGITS = 82


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(x: F) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def fmt(x: mp.mpf) -> str:
    return mp.nstr(x, SERIALIZED_DIGITS, strip_zeros=False)


def finite_stationary(lam: F, mu: F, K: int) -> list[F]:
    if K == 0:
        return [F(1)]
    rho = lam / mu
    weights = [rho**n for n in range(K + 1)]
    Z = sum(weights, F(0))
    return [w / Z for w in weights]


def gap(lam: F, mu: F, K: int) -> mp.mpf | None:
    if K == 0:
        return None
    return mpq(lam + mu) - 2 * mp.sqrt(mpq(lam * mu)) * mp.cos(mp.pi / (K + 1))


def spectral_rows(label: str, lam: F, mu: F, K: int) -> list[dict]:
    if K == 0:
        return []
    r = mp.sqrt(mpq(lam * mu))
    alpha = mp.sqrt(mpq(mu / lam))
    rows: list[dict] = []
    for j in range(1, K + 1):
        theta = mp.pi * j / (K + 1)
        eig = -mpq(lam + mu) + 2 * r * mp.cos(theta)
        raw = [mp.sin((n + 1) * theta) - alpha * mp.sin(n * theta) for n in range(K + 1)]
        norm = mp.sqrt(sum(x * x for x in raw))
        vec = [x / norm for x in raw]
        rows.append({
            "parameter_label": label, "lambda": str(lam), "mu": str(mu), "K": K, "mode": j,
            "theta": fmt(theta), "eigenvalue": fmt(eig), "eigenvector": [fmt(x) for x in vec],
            "norm_squared": fmt(sum(x * x for x in vec)),
        })
    return rows


def transition_matrix(lam: F, mu: F, K: int, t: F) -> list[list[mp.mpf]]:
    if K == 0:
        return [[mp.mpf(1)]]
    pi = [mpq(x) for x in finite_stationary(lam, mu, K)]
    r = mp.sqrt(mpq(lam * mu))
    alpha = mp.sqrt(mpq(mu / lam))
    vectors: list[list[mp.mpf]] = [[mp.sqrt(x) for x in pi]]
    eigs: list[mp.mpf] = [mp.mpf(0)]
    for j in range(1, K + 1):
        theta = mp.pi * j / (K + 1)
        raw = [mp.sin((n + 1) * theta) - alpha * mp.sin(n * theta) for n in range(K + 1)]
        norm = mp.sqrt(sum(x * x for x in raw))
        vectors.append([x / norm for x in raw])
        eigs.append(-mpq(lam + mu) + 2 * r * mp.cos(theta))
    tt = mpq(t)
    return [[sum(vectors[m][i] * vectors[m][j] * mp.exp(eigs[m] * tt) for m in range(K + 1)) * mp.sqrt(pi[j] / pi[i]) for j in range(K + 1)] for i in range(K + 1)]


def kernel_rows(label: str, lam: F, mu: F, K: int, t: F) -> list[dict]:
    P = transition_matrix(lam, mu, K, t)
    pi = [mpq(x) for x in finite_stationary(lam, mu, K)]
    rows = []
    for i, row in enumerate(P):
        tv = mp.mpf("0.5") * sum(abs(row[j] - pi[j]) for j in range(K + 1))
        bound = mp.mpf("0") if K == 0 else mp.mpf("0.5") * mp.sqrt((1 / pi[i]) - 1) * mp.exp(-gap(lam, mu, K) * mpq(t))
        rows.append({
            "parameter_label": label, "lambda": str(lam), "mu": str(mu), "K": K, "time": str(t), "initial_state": i,
            "probabilities": [fmt(x) for x in row], "row_sum": fmt(sum(row)), "min_probability": fmt(min(row)),
            "tv_distance": fmt(tv), "tv_bound": fmt(bound), "bound_slack": fmt(bound - tv),
        })
    return rows


def boundary_rows() -> list[dict]:
    return [
        {"boundary_id": "K_zero", "condition": "K=0", "law": "single state 0; Q=[0], P_t(0,0)=1 and stationary mass is 1"},
        {"boundary_id": "lambda_zero", "condition": "lambda=0, mu>0", "law": "state 0 is absorbing; every state reaches 0 deterministically through deaths"},
        {"boundary_id": "mu_zero", "condition": "mu=0, lambda>0", "law": "state K is absorbing; every state reaches K deterministically through births"},
        {"boundary_id": "both_zero", "condition": "lambda=mu=0", "law": "every state is absorbing; each point mass is stationary and no unique stationary law exists"},
        {"boundary_id": "equal_rates", "condition": "lambda=mu>0", "law": "finite stationary law is uniform; infinite chain is null recurrent and has no probability stationary law"},
        {"boundary_id": "infinite_subcritical", "condition": "K to infinity with rho=lambda/mu<1", "law": "finite pi converges coordinatewise to (1-rho)rho^n and finite gap converges to (sqrt(mu)-sqrt(lambda))^2"},
        {"boundary_id": "infinite_critical", "condition": "K to infinity with rho=1", "law": "gap_K=2lambda(1-cos(pi/(K+1))) ~ lambda*pi^2/(K+1)^2; null-recurrent boundary"},
        {"boundary_id": "infinite_supercritical", "condition": "K to infinity with rho>1", "law": "finite stationary mass at every fixed state tends to 0 (mass escapes); no infinite stationary probability"},
    ]


def limit_rows(label: str, lam: F, mu: F) -> list[dict]:
    rho = lam / mu
    inf_gap = (mp.sqrt(mpq(mu)) - mp.sqrt(mpq(lam))) ** 2
    rows = []
    for K in LIMIT_K_VALUES:
        pi0 = mpq(finite_stationary(lam, mu, K)[0])
        pi_last = mpq(finite_stationary(lam, mu, K)[-1])
        g = gap(lam, mu, K)
        rows.append({
            "parameter_label": label, "lambda": str(lam), "mu": str(mu), "rho": str(rho), "K": K,
            "pi_state0": fmt(pi0), "pi_stateK": fmt(pi_last), "finite_gap": fmt(g),
            "infinite_gap_reference": fmt(inf_gap), "gap_ratio_to_reference": None if rho == 1 else fmt(g / inf_gap),
            "critical_scaled_gap": fmt(g * (K + 1) ** 2) if rho == 1 else None,
        })
    return rows


def build() -> dict:
    mp.mp.dps = WORKING_DIGITS
    stationary_rows: list[dict] = []
    spectra: list[dict] = []
    kernels: list[dict] = []
    mix_rows: list[dict] = []
    limits: list[dict] = []
    for label, lam, mu in PARAMETERS:
        for K in K_VALUES:
            pi = finite_stationary(lam, mu, K)
            rho = lam / mu
            stationary_rows.append({
                "parameter_label": label, "lambda": str(lam), "mu": str(mu), "K": K,
                "rho": str(rho), "weights": [str(rho**n) for n in range(K + 1)],
                "stationary": [str(x) for x in pi], "normalization": str(sum(pi, F(0))),
                "pi0": str(pi[0]), "piK": str(pi[-1]),
            })
            spectra.extend(spectral_rows(label, lam, mu, K))
            for t in TIME_VALUES:
                rows = kernel_rows(label, lam, mu, K, t)
                kernels.extend(rows)
                for row in rows:
                    mix_rows.append({
                        "parameter_label": label, "K": K, "time": str(t), "initial_state": row["initial_state"],
                        "tv_distance": row["tv_distance"], "tv_bound": row["tv_bound"],
                        "gap": None if K == 0 else fmt(gap(lam, mu, K)),
                    })
        limits.extend(limit_rows(label, lam, mu))
    data = {
        "schema": "hcs-c225-mm1k-queue-v1", "candidate_id": "HCS-C225", "evaluation_date": "2026-08-29",
        "source_commit": SOURCE_COMMIT, "fixed_epoch": FIXED_EPOCH, "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "Finite-capacity M/M/1/K birth--death queues admit an exact reversible kernel, full spectral gap atlas, and controlled infinite-capacity boundaries",
        "frozen_object": {
            "state_space": "{0,1,...,K}, where K includes the customer in service",
            "generator": "Q_{0,0}=-lambda,Q_{0,1}=lambda; Q_{n,n-1}=mu,Q_{n,n}=-(lambda+mu),Q_{n,n+1}=lambda (0<n<K); Q_{K,K-1}=mu,Q_{K,K}=-mu",
            "parameters": "lambda,mu>=0 rates, integer capacity K>=0, physical time t>=0",
            "clock": "continuous-time Markov semigroup exp(tQ)",
            "normalization": "row-stochastic transition kernel and probability stationary vector",
            "symmetrization": "S=D_pi^(1/2) Q D_pi^(-1/2), with off-diagonal sqrt(lambda*mu)",
            "determinant_convention": "finite characteristic polynomial only; no infinite Fredholm determinant",
            "arithmetic_origin": "none; queue states and rates are source-defined",
            "allowed_data": "exact rates, finite generators, stationary probabilities, eigenmodes, kernels and mixing bounds",
            "forbidden_data": "prime or zero tables, target labels, Euler factors, root numbers, automorphy and Route-B input",
        },
        "theorem": {
            "stationary": "For lambda,mu>0 and K>=1, pi_n=(lambda/mu)^n / sum_{r=0}^K(lambda/mu)^r; at equal rates pi is uniform; K=0 is singleton.",
            "jacobi": "D_pi^(1/2) Q D_pi^(-1/2) is a symmetric tridiagonal Jacobi matrix with off-diagonal sqrt(lambda*mu).",
            "spectrum": "For K>=1 the eigenvalues are 0 and nu_j=-(lambda+mu)+2sqrt(lambda*mu)cos(j*pi/(K+1)), j=1,...,K.",
            "eigenbasis": "A normalized eigenvector for nu_j has components proportional to sin((n+1)theta_j)-sqrt(mu/lambda)sin(n theta_j), theta_j=j*pi/(K+1).",
            "kernel": "P_t(i,j)=sqrt(pi_j/pi_i) sum_{m=0}^K v_m(i)v_m(j)exp(nu_m t), with v_0=sqrt(pi) and nu_0=0.",
            "mixing": "The spectral gap is gamma_K=lambda+mu-2sqrt(lambda*mu)cos(pi/(K+1)); TV distance from i is at most 1/2 sqrt(pi_i^{-1}-1) exp(-gamma_K t).",
            "boundaries": "K=0, lambda=0, mu=0 and both-zero faces are absorbing degeneracies; equal rates are finite uniform but infinite null recurrent.",
            "infinite_capacity": "As K->infinity, rho<1 has geometric stationary convergence and gap limit (sqrt(mu)-sqrt(lambda))^2; rho=1 has gamma_K~lambda*pi^2/(K+1)^2 and no stationary probability; rho>1 finite stationary mass escapes and no stationary probability exists.",
            "infinite_scope": "No assertion is made here about a continuous-spectrum decomposition of the infinite generator; only the stated stationary and gap/boundary limits are claimed.",
            "distinction": "This is a reversible birth--death semigroup with capacity reflection, not the branching PGF of C208 and not the interacting-particle matrix-ansatz phase atlas of C220.",
        },
        "regression": {
            "parameter_rows": [{"parameter_label": l, "lambda": str(la), "mu": str(mu)} for l, la, mu in PARAMETERS],
            "K_values": K_VALUES, "time_values": [str(t) for t in TIME_VALUES], "limit_K_values": LIMIT_K_VALUES,
            "stationary_rows": stationary_rows, "spectral_rows": spectra, "kernel_rows": kernels,
            "mixing_rows": mix_rows, "limit_rows": limits, "boundary_rows": boundary_rows(),
        },
        "summary": {
            "parameter_count": len(PARAMETERS), "stationary_row_count": len(stationary_rows),
            "spectral_row_count": len(spectra), "kernel_row_count": len(kernels), "mixing_row_count": len(mix_rows),
            "limit_row_count": len(limits), "boundary_row_count": len(boundary_rows()), "max_K": max(K_VALUES),
            "serialized_decimal_digits": SERIALIZED_DIGITS,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
            "strongest_positive": "The finite generator has an intrinsic reversible Jacobi realization and an exact semigroup spectral atlas.",
            "strongest_failure": "Queue state labels and rates carry no primitive arithmetic owner, target divisor or Hilbert--Polya bridge; the Jacobi matrix is a formal finite-dimensional analogy only.",
        },
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [
            {"key": "KarlinMcGregor1957", "claim": "spectral representation and Stieltjes moment framework for birth--death processes", "title": "The differential equations of birth-and-death processes, and the Stieltjes moment problem", "authors": "Samuel Karlin and James McGregor", "venue": "Transactions of the American Mathematical Society 85 (1957), 489--546", "date": "1957", "url": "https://doi.org/10.1090/S0002-9947-1957-0091566-1", "persistent_url": "https://doi.org/10.1090/S0002-9947-1957-0091566-1"},
            {"key": "EkstromGaroniJozefiakPerla2021", "claim": "tau-matrix spectral calculations with applications to Markov processes", "title": "Eigenvalues and eigenvectors of tau matrices with applications to Markov processes and economics", "authors": "Sven-Erik Ekström, Carlo Garoni, Adam Jozefiak and Jesse Perla", "venue": "Linear Algebra and its Applications 627 (2021), 41--71", "date": "2021", "url": "https://doi.org/10.1016/j.laa.2021.06.005", "persistent_url": "https://doi.org/10.1016/j.laa.2021.06.005"},
            {"key": "CallaertKeilson1973", "claim": "exponential ergodicity and spectral-structure boundary context for birth--death processes", "title": "On exponential ergodicity and spectral structure for birth-death processes, II", "authors": "Herman Callaert and Julian Keilson", "venue": "Stochastic Processes and their Applications 1(3) (1973), 217--235", "date": "1973", "url": "https://doi.org/10.1016/0304-4149(73)90001-X", "persistent_url": "https://doi.org/10.1016/0304-4149(73)90001-X"},
        ],
        "nonclaims": [
            "priority for the finite M/M/1/K spectrum or queueing boundary classification",
            "the finite ledger is a proof of an unqualified infinite-dimensional spectral theorem",
            "any queue eigenvalue or state label is a target zero, prime, Euler factor or arithmetic local datum",
            "an infinite Fredholm determinant, target divisor, functional equation or automorphy statement",
            "a Hilbert--Polya operator, Route-B construction or external peer review",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    path = parser.parse_args().output
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(build(), sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    data = json.loads(path.read_text())
    print(json.dumps({"status": "C225_PRODUCER_PASS", "stationary_rows": data["summary"]["stationary_row_count"], "spectral_rows": data["summary"]["spectral_row_count"], "kernel_rows": data["summary"]["kernel_row_count"], "payload_sha256": data["payload_sha256"], "output": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
