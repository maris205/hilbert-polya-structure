#!/usr/bin/env python3
"""Deterministic high-precision receipt for HCS-C277."""
from __future__ import annotations

import hashlib
import json
import os
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("C277_OUTPUT_PATH", ROOT / "results/c277_caputo_evidence.json"))
SOURCE = "418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788220800
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
mp.mp.dps = 90


def qs(x: Q) -> str:
    return f"{x.numerator}/{x.denominator}"


def ds(x: mp.mpf) -> str:
    if abs(x) < mp.mpf("1e-78"):
        x = mp.mpf(0)
    return mp.nstr(x, 72, strip_zeros=False)


def payload_hash(data: dict) -> str:
    payload = dict(data)
    payload.pop("payload_sha256", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def ml_series(beta: mp.mpf, x: mp.mpf) -> tuple[mp.mpf, int]:
    """E_beta(-x), used only for 0<=x<=1 where the defining series is stable."""
    total = mp.mpf(0)
    for k in range(5000):
        term = (-x) ** k / mp.gamma(beta * k + 1)
        total += term
        if k > 20 and abs(term) < mp.mpf("1e-82"):
            return total, k + 1
    raise RuntimeError("Mittag-Leffler series did not settle")


def erfcx(x: mp.mpf) -> mp.mpf:
    return mp.exp(x * x) * mp.erfc(x)


def main() -> None:
    betas = (Q(1, 4), Q(1, 3), Q(1, 2), Q(2, 3), Q(3, 4), Q(1))
    x_values = (Q(1, 64), Q(1, 16), Q(1, 4), Q(1))

    scalar_cells = []
    for beta in betas:
        bb = mp.mpf(beta.numerator) / beta.denominator
        previous = mp.mpf(2)
        for x in x_values:
            xx = mp.mpf(x.numerator) / x.denominator
            value, terms = ml_series(bb, xx)
            assert 0 < value < previous <= 2
            previous = value
            scalar_cells.append({
                "beta": qs(beta), "x": qs(x), "value": ds(value),
                "series_terms": terms,
            })

    spectral_cells = []
    scale = Q(1, 1024)  # t^beta; n<=32 keeps x=n^2*t^beta<=1.
    for beta in betas:
        bb = mp.mpf(beta.numerator) / beta.denominator
        last = mp.mpf(2)
        for n in range(1, 33):
            x = Q(n * n) * scale
            xx = mp.mpf(x.numerator) / x.denominator
            value, terms = ml_series(bb, xx)
            assert 0 < value < last
            last = value
            spectral_cells.append({
                "beta": qs(beta), "mode": n, "t_power_beta": qs(scale),
                "spectral_argument": qs(x), "multiplier": ds(value),
                "series_terms": terms,
            })

    nonsemigroup = []
    t = mp.mpf(1) / 4
    for beta in betas:
        bb = mp.mpf(beta.numerator) / beta.denominator
        xt = t ** bb
        xsum = (2 * t) ** bb
        one, _ = ml_series(bb, xt)
        joined, _ = ml_series(bb, xsum)
        defect = joined - one * one
        if beta == 1:
            assert abs(defect) < mp.mpf("1e-75")
        else:
            assert abs(defect) > mp.mpf("1e-8")
        nonsemigroup.append({
            "beta": qs(beta), "t": "1/4", "s": "1/4",
            "E_beta_minus_t_beta": ds(one),
            "E_beta_minus_t_plus_s_beta": ds(joined),
            "composition_defect": ds(defect),
            "semigroup_identity": beta == 1,
        })

    # beta=1/2 has E_{1/2}(-x)=exp(x^2)erfc(x), so large arguments
    # can be audited without an unstable alternating series.
    long_time_half = []
    limit_constant = 1 / mp.sqrt(mp.pi)
    for q in (2, 4, 8, 16, 32, 64):  # q=t^beta=sqrt(t)
        max_error = mp.mpf(0)
        cells = []
        for n in range(1, 17):
            x = mp.mpf(n * n * q)
            scaled = q * erfcx(x)
            limit = limit_constant / (n * n)
            error = abs(scaled - limit)
            max_error = max(max_error, error)
            cells.append({"mode": n, "scaled_multiplier": ds(scaled),
                          "resolvent_limit": ds(limit), "absolute_error": ds(error)})
        long_time_half.append({"t_power_beta": q, "t": q * q,
                               "operator_grid_max_error": ds(max_error), "modes": cells})

    smoothing = []
    thetas = (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1), Q(5, 4), Q(3, 2))
    for beta in betas[:-1]:
        for theta in thetas:
            tail_power = 2 * theta - 2
            smoothing.append({
                "beta": qs(beta), "theta_A_power": qs(theta),
                "sobolev_gain": qs(2 * theta), "tail_power_in_mode": qs(tail_power),
                "bounded_L2_operator": theta <= 1,
            })

    schatten = []
    for beta in betas[:-1]:
        for p in (Q(1, 4), Q(1, 2), Q(3, 4), Q(1), Q(2)):
            schatten.append({
                "beta": qs(beta), "p": qs(p), "comparison_series_power": qs(2 * p),
                "in_S_p": p > Q(1, 2),
            })

    data = {
        "schema": "hcs-c277-caputo-dirichlet-heat-v1",
        "candidate_id": "HCS-C277",
        "evaluation_date": "2026-09-01",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "owner": {
            "state_space": "L2((0,pi))",
            "spatial_operator": "A=-d^2/dx^2 with Dirichlet domain H^2 cap H_0^1",
            "equation": "Caputo_D_t^beta u + A u = 0",
            "parameter": "0<beta<=1",
            "clock": "physical Caputo memory time",
        },
        "theorem_contract": {
            "spectral_solution": "S_beta(t)e_n=E_beta(-n^2*t^beta)e_n",
            "subordination": "for beta<1 S_beta is the inverse-stable subordination of the Dirichlet heat semigroup",
            "positivity_contraction": "S_beta(t) is positivity preserving, self-adjoint, positive, and contractive",
            "nonsemigroup": "for beta<1 the strongly continuous solution family is not a semigroup",
            "sharp_smoothing": "for beta<1, t>0, and theta>=0, A^theta*S_beta(t) is bounded iff theta<=1",
            "negative_theta_context": "theta<0 also gives a bounded operator because A>=I, but it is outside the declared theta>=0 smoothing domain",
            "sharp_schatten": "for beta<1 and t>0, S_beta(t) belongs to S_p exactly when p>1/2",
            "long_time": "t^beta*S_beta(t) converges in operator norm to A^{-1}/Gamma(1-beta)",
            "heat_face": "beta=1 gives exp(-tA), all-order smoothing, every S_p, and norm exp(-t)",
        },
        "proof_obligations": [
            "Caputo scalar-mode solution and strong L2 reconstruction",
            "inverse-stable subordination and positivity/contraction",
            "non-semigroup category boundary for beta<1",
            "within theta>=0, endpoint A*S_beta bounded and every theta>1 failure; theta<0 is bounded but outside the declared domain",
            "Schatten threshold including p=1/2 divergence",
            "operator-norm scaled resolvent limit and separate beta=1 face",
        ],
        "regression": {
            "mittag_leffler_scalar_cells": scalar_cells,
            "spectral_cells": spectral_cells,
            "nonsemigroup_witnesses": nonsemigroup,
            "beta_half_long_time": long_time_half,
            "smoothing_threshold_cells": smoothing,
            "schatten_threshold_cells": schatten,
            "counts": {
                "scalar_cells": len(scalar_cells), "spectral_cells": len(spectral_cells),
                "nonsemigroup_witnesses": len(nonsemigroup),
                "long_time_mode_cells": sum(len(x["modes"]) for x in long_time_half),
                "smoothing_cells": len(smoothing), "schatten_cells": len(schatten),
            },
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "arithmetic_local_data": False, "euler_factors": False,
            "root_numbers": False, "automorphy": False, "target_divisor": False,
            "functional_equation": False, "hilbert_polya_operator": False,
        },
        "sources": [
            {"author": "H. Pollard", "title": "The completely monotonic character of the Mittag-Leffler function E_a(-x)",
             "journal": "Bulletin of the American Mathematical Society 54 (1948), 1115-1116",
             "doi": "10.1090/S0002-9904-1948-09132-7", "role": "complete monotonicity"},
            {"author": "K. Sakamoto and M. Yamamoto",
             "title": "Initial value/boundary value problems for fractional diffusion-wave equations and applications to some inverse problems",
             "journal": "Journal of Mathematical Analysis and Applications 382 (2011), 426-447",
             "doi": "10.1016/j.jmaa.2011.04.058", "role": "bounded-domain spectral well-posedness and long time"},
        ],
        "nonclaims": [
            "Workspace ownership is not a literature-priority claim.",
            "The solution family for beta<1 is not called a semigroup.",
            "Trace-ideal membership is source-local operator theory, not a target determinant or Hilbert-Polya construction.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    c = data["regression"]["counts"]
    print(f"C277_PRODUCER_PASS spectral={c['spectral_cells']} long={c['long_time_mode_cells']} payload={data['payload_sha256']}")


if __name__ == "__main__":
    main()
