#!/usr/bin/env python3
"""Deterministic exact certificate for the exponential linear Hawkes process."""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

SOURCE = "a24c701881d22a4e49eaa2a44b94395c3c540b3d"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000
ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c265_hawkes_evidence.json"
ORDER = 10


def frac(value: Fraction | int) -> str:
    value = value if isinstance(value, Fraction) else Fraction(value)
    return f"{value.numerator}/{value.denominator}"


def parse_frac(value: str) -> Fraction:
    return Fraction(value)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return sha256(raw.encode()).hexdigest()


def stationary_moments(nu: Fraction, a: Fraction, b: Fraction, order: int) -> list[Fraction]:
    """Generator recurrence, with m_0=1."""
    delta = b - a
    assert delta > 0
    moments = [Fraction(1)]
    for n in range(1, order + 1):
        numerator = Fraction(n) * b * nu * moments[n - 1]
        for k in range(0, n - 1):
            numerator += Fraction(math.comb(n, k)) * a ** (n - k) * moments[k + 1]
        moments.append(numerator / (Fraction(n) * delta))
    return moments


def stable_cases() -> list[dict]:
    rows: list[dict] = []
    nus = [Fraction(0), Fraction(1, 3), Fraction(1), Fraction(2), Fraction(5)]
    for b_int in range(1, 9):
        b = Fraction(b_int)
        for j in range(8):
            a = b * Fraction(j, 8)
            for nu in nus:
                delta = b - a
                mean = b * nu / delta
                variance = mean * a * a / (2 * delta)
                count_coefficient = mean * a * (2 * b - a) / (2 * delta)
                spectrum_zero = mean * b * b / (delta * delta)
                moments = stationary_moments(nu, a, b, ORDER)
                window = [mean]
                gain = mean * a * (2 * b - a)
                for n in range(2, ORDER + 1):
                    window.append(gain * Fraction((-1) ** n, math.factorial(n)) * delta ** (n - 3))
                rows.append({
                    "case_id": f"b{b_int}_j{j}_nu{frac(nu).replace('/', '_')}",
                    "nu": frac(nu), "a": frac(a), "b": frac(b), "delta": frac(delta),
                    "branching_ratio": frac(a / b), "mean_intensity": frac(mean),
                    "intensity_variance": frac(variance),
                    "intensity_covariance_coefficient": frac(variance),
                    "counting_continuous_covariance_coefficient": frac(count_coefficient),
                    "counting_dirac_mass": frac(mean),
                    "bartlett_zero_frequency": frac(spectrum_zero),
                    "long_window_variance_rate": frac(spectrum_zero),
                    "moments_m0_to_m10": [frac(x) for x in moments],
                    "window_variance_maclaurin_T1_to_T10": [frac(x) for x in window],
                })
    return rows


def cluster_rows() -> list[dict]:
    rows: list[dict] = []
    for j in range(8):
        ratio = Fraction(j, 8)
        for n in range(1, 21):
            # P(K=n)=coefficient*exp(exponent), kept exact without decimal exponentiation.
            coefficient = Fraction(n ** (n - 1), math.factorial(n)) * ratio ** (n - 1)
            rows.append({
                "branching_ratio": frac(ratio), "n": n,
                "rooted_tree_count": n ** (n - 1),
                "coefficient": frac(coefficient), "exponent": frac(-ratio * n),
            })
    return rows


def boundary_rows() -> list[dict]:
    return [
        {"id": "poisson_a_zero", "nu": "3/2", "a": "0/1", "b": "2/1", "classification": "HOMOGENEOUS_POISSON", "stationary_mean": "3/2"},
        {"id": "empty_nu_zero_subcritical", "nu": "0/1", "a": "1/2", "b": "1/1", "classification": "EMPTY_STATIONARY", "stationary_mean": "0/1"},
        {"id": "empty_nu_zero_critical", "nu": "0/1", "a": "1/1", "b": "1/1", "classification": "EMPTY_STATIONARY_BOUNDARY", "stationary_mean": "0/1"},
        {"id": "critical_positive_immigration", "nu": "1/1", "a": "2/1", "b": "2/1", "classification": "NO_FINITE_INTENSITY_STATIONARY", "mean_growth_slope": "2/1"},
        {"id": "supercritical_positive_immigration", "nu": "1/1", "a": "3/1", "b": "2/1", "classification": "NO_FINITE_INTENSITY_STATIONARY", "mean_exponent": "1/1"},
        {"id": "subcritical_positive_immigration", "nu": "1/1", "a": "1/1", "b": "2/1", "classification": "UNIQUE_FINITE_INTENSITY_STATIONARY", "stationary_mean": "2/1"},
    ]


def build() -> dict:
    cases = stable_cases()
    clusters = cluster_rows()
    boundaries = boundary_rows()
    data = {
        "schema": "hcs-c265-exponential-hawkes-stationary-v1",
        "candidate_id": "HCS-C265",
        "evaluation_date": "2026-08-31",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "scope_flags": {
            "claims_arithmetic_local_data": False,
            "claims_euler_factors": False,
            "claims_root_numbers": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False,
            "claims_hilbert_polya_operator": False,
            "uses_prime_table": False,
            "uses_target_zero_table": False,
            "invokes_route_b": False,
        },
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR,
        },
        "citation": {
            "author": "Alan G. Hawkes",
            "title": "Spectra of some self-exciting and mutually exciting point processes",
            "journal": "Biometrika 58 (1971), 83--90",
            "doi": "10.1093/biomet/58.1.83",
            "use": "definition, complete covariance measure, and spectral-density convention only",
        },
        "frozen_object": {
            "equation": "d lambda_t = -b(lambda_t-nu)dt + a dN_t",
            "predictable_intensity": "lambda_(t-)",
            "parameters": "b>0; a,nu>=0",
            "kernel": "h(t)=a exp(-bt) 1_(t>0)",
            "fourier_convention": "S(omega)=integral exp(-i omega t) Gamma(dt); no 1/(2pi)",
        },
        "headline": "The exponential Hawkes owner closes its joint affine transform, stationary law, all moments, three distinct covariance objects, Bartlett spectrum, window variance, and Borel clusters.",
        "theorem": {
            "status": "PROVABLE_AS_STATED",
            "stationarity": "For nu>0 a finite-intensity stationary law exists exactly when a<b; for nu=0 the empty law remains stationary.",
            "affine_transform": "E_x[z^N_t exp(-s lambda_t)]=exp(-A_t-B_t x), B'=1-bB-z exp(-aB), A'=b nu B.",
            "stationary_laplace_ode": "L'/L=-b nu s/(b s+exp(-a s)-1), L(0)=1.",
            "moment_recurrence": "m_n=[n b nu m_(n-1)+sum_(k=0)^(n-2) binom(n,k) a^(n-k)m_(k+1)]/[n(b-a)].",
            "intensity_covariance": "Cov(lambda_t,lambda_0)=mu a^2 exp(-(b-a)|t|)/(2(b-a)).",
            "complete_counting_covariance": "Gamma(dt)=mu delta_0(dt)+mu a(2b-a)exp(-(b-a)|t|)dt/[2(b-a)].",
            "bartlett_spectrum": "S(omega)=mu(b^2+omega^2)/((b-a)^2+omega^2), with no 1/(2pi).",
            "window_variance": "Var N_T=mu T+mu a(2b-a)[T/delta^2-(1-exp(-delta T))/delta^3].",
            "borel_cluster": "P(K=n)=exp(-mn)(mn)^(n-1)/n!, m=a/b<1.",
        },
        "object_separation": [
            "intensity covariance is an ordinary function and has coefficient mu*a^2/(2*delta)",
            "counting covariance is a measure containing the atom mu*delta_0",
            "the continuous counting covariance coefficient is mu*a*(2*b-a)/(2*delta)",
            "the Bartlett spectrum is the Fourier transform of the complete counting covariance measure",
        ],
        "regression": {
            "moment_order": ORDER,
            "stable_case_count": len(cases),
            "cluster_row_count": len(clusters),
            "boundary_row_count": len(boundaries),
            "stable_cases": cases,
            "cluster_rows": clusters,
            "boundary_rows": boundaries,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "A canonical Markov generator and a complete source-local stationary transform/covariance theorem.",
            "strongest_failure": "Events and cluster genealogy supply no rational-prime owner, logarithmic prime clock, target divisor, or determinant-class Hilbert--Polya operator.",
        },
        "nonclaims": [
            "Workspace ownership is not a literature-priority claim.",
            "Finite rational regression does not prove the all-parameter theorem.",
            "The Markov generator is not promoted to a Hilbert--Polya operator.",
            "The Bartlett spectrum is a source point-process spectrum, not a target divisor or Euler product.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C265_PRODUCER_PASS",
        "stable_cases": data["regression"]["stable_case_count"],
        "moment_cells": data["regression"]["stable_case_count"] * (ORDER + 1),
        "window_cells": data["regression"]["stable_case_count"] * ORDER,
        "cluster_rows": data["regression"]["cluster_row_count"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
