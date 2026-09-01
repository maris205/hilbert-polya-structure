#!/usr/bin/env python3
"""Deterministic exact/high-precision receipt for HCS-C272."""
from __future__ import annotations

import hashlib
import json
import math
import os
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("C272_OUTPUT_PATH", ROOT / "results/c272_age_evidence.json"))
SOURCE = "9cb7483e97ef82fdc06d45ecb3043f183ce22391"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788134400
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
mp.mp.dps = 90


def qs(x: Q) -> str:
    return f"{x.numerator}/{x.denominator}"


def ds(x: mp.mpf) -> str:
    if abs(x) < mp.mpf("1e-75"):
        x = mp.mpf(0)
    return mp.nstr(x, 70, strip_zeros=False)


def phash(data: dict) -> str:
    payload = dict(data)
    payload.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def polynomial_coefficients(k: int, gamma: Q, mu: Q, beta: Q) -> list[str]:
    c = gamma + mu
    # Descending coefficients of (z+c)^k-beta*gamma^k.
    coeffs = [Q(math.comb(k, j)) * c**j for j in range(0, k + 1)]
    coeffs[-1] -= beta * gamma**k
    return [qs(x) for x in coeffs]


def main() -> None:
    rows = []
    root_cells = 0
    for k in range(1, 13):
        for rho in (Q(1, 2), Q(1), Q(5, 4), Q(3, 2), Q(2)):
            beta = rho**k
            for gamma in (Q(1), Q(2)):
                for mu in (Q(1, 3), Q(1), Q(2)):
                    rr = mp.mpf(rho.numerator) / rho.denominator
                    gg = mp.mpf(gamma.numerator) / gamma.denominator
                    mm = mp.mpf(mu.numerator) / mu.denominator
                    roots = []
                    for j in range(k):
                        theta = 2 * mp.pi * j / k
                        lam = gg * rr * mp.e ** (1j * theta) - gg - mm
                        edge_offset = rr * mp.cos(theta) - 1
                        if abs(edge_offset) < mp.mpf("1e-70"):
                            location = "essential_edge"
                        elif edge_offset > 0:
                            location = "eigenvalue"
                        else:
                            location = "algebraic_root_not_in_L1"
                        roots.append({
                            "j": j,
                            "real": ds(mp.re(lam)),
                            "imag": ds(mp.im(lam)),
                            "edge_offset_over_gamma": ds(edge_offset),
                            "spectral_location": location,
                        })
                    root_cells += len(roots)
                    lambda0 = gamma * (rho - 1) - mu
                    if rho <= 1:
                        population_regime = "essential_decay_no_isolated_pole"
                        spectral_gap = None
                    else:
                        population_regime = "decay" if lambda0 < 0 else ("critical_population" if lambda0 == 0 else "growth")
                        edge_gap = gg * (rr - 1)
                        if k == 1:
                            gap = edge_gap
                        else:
                            root_gap = gg * rr * (1 - mp.cos(2 * mp.pi / k))
                            gap = min(edge_gap, root_gap)
                        spectral_gap = ds(gap)
                    rows.append({
                        "k": k,
                        "rho_beta_root": qs(rho),
                        "beta": qs(beta),
                        "gamma": qs(gamma),
                        "mu": qs(mu),
                        "essential_edge": qs(-mu),
                        "dominant_algebraic_root": qs(lambda0),
                        "dominant_isolated_eigenvalue": rho > 1,
                        "population_regime": population_regime,
                        "stable_age_decay_rate": qs(gamma * (rho - 1)) if rho > 1 else None,
                        "spectral_gap": spectral_gap,
                        "characteristic_polynomial_descending": polynomial_coefficients(k, gamma, mu, beta),
                        "roots": roots,
                    })
    zero_birth = [
        {"k": k, "gamma": qs(gamma), "mu": qs(mu), "semigroup": "mortality-weighted right shift", "essential_edge": qs(-mu)}
        for k in (1, 4, 12) for gamma, mu in ((Q(1), Q(1)), (Q(2), Q(1, 3)))
    ]
    data = {
        "schema": "hcs-c272-erlang-age-transport-v1",
        "candidate_id": "HCS-C272",
        "evaluation_date": "2026-09-01",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "owner": {
            "state_space": "L1(R_+,da)",
            "equation": "partial_t n+partial_a n=-mu*n",
            "boundary": "n(t,0)=integral_0^infinity b_k(a)n(t,a) da",
            "birth_kernel": "b_k(a)=beta*gamma^k*a^(k-1)*exp(-gamma*a)/(k-1)!",
            "parameters": "mu,gamma,beta>0 and integer k>=1",
            "clock": "physical population time",
        },
        "theorem_contract": {
            "characteristics": "transport reduces the boundary births to an Erlang renewal equation",
            "euler_lotka": "Delta(lambda)=1-beta*(gamma/(gamma+lambda+mu))^k",
            "algebraic_roots": "lambda_j=gamma*beta^(1/k)*exp(2*pi*i*j/k)-gamma-mu",
            "eigenvalue_gate": "an algebraic root is an L1 eigenvalue exactly when Re(lambda)>-mu",
            "essential_edge": "the mortality-weighted shift has essential spectral bound -mu",
            "phase_transition": "beta>1 gives one dominant isolated real eigenvalue and rank-one asynchronous growth/decay; beta<=1 has no such universal rank-one term",
            "population_threshold": "lambda_0=0 exactly when beta=(1+mu/gamma)^k",
        },
        "proof_obligations": [
            "characteristic formula and renewal boundary",
            "resolvent denominator and all algebraic roots",
            "L1 integrability gate separating roots from eigenvalues",
            "essential-spectrum witness for the weighted shift",
            "dominant residue and positive stable-age profile for beta>1",
            "separate beta=1, population-critical, and zero-birth faces",
        ],
        "regression": {
            "cases": rows,
            "zero_birth_boundaries": zero_birth,
            "counts": {"parameter_cases": len(rows), "root_cells": root_cells, "zero_birth_boundaries": len(zero_birth)},
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "target_divisor": False,
            "functional_equation": False,
            "hilbert_polya_operator": False,
        },
        "source": {
            "author": "A. G. M'Kendrick",
            "title": "Applications of Mathematics to Medical Problems",
            "journal": "Proceedings of the Edinburgh Mathematical Society 44 (1925), 98-130",
            "doi": "10.1017/S0013091500034428",
            "role": "age-structured transport lineage",
        },
        "nonclaims": [
            "Workspace ownership is not a literature-priority claim.",
            "Algebraic denominator roots below the essential edge are not called L1 eigenvalues.",
            "Renewal poles and population spectra are not target arithmetic determinants or Hilbert-Polya data.",
        ],
    }
    data["payload_sha256"] = phash(data)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C272_PRODUCER_PASS cases={len(rows)} roots={root_cells} payload={data['payload_sha256']}")


if __name__ == "__main__":
    main()
