#!/usr/bin/env python3
"""Producer-independent checker for HCS-C277."""
from __future__ import annotations

import hashlib
import json
import math
import os
from fractions import Fraction as Q
from pathlib import Path

from scipy import special

ROOT = Path(__file__).resolve().parents[1]
PATH = Path(os.environ.get("C277_EVIDENCE_PATH", ROOT / "results/c277_caputo_evidence.json"))
SOURCE = "418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EXPECTED_KEYS = {"schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal",
                 "evaluator", "owner", "theorem_contract", "proof_obligations", "regression", "route_a",
                 "scope_flags", "sources", "nonclaims", "payload_sha256"}


def q(x: str) -> Q:
    return Q(x)


def payload_hash(data: dict) -> str:
    d = dict(data); d.pop("payload_sha256", None)
    raw = json.dumps(d, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def ml_double(beta: float, x: float) -> float:
    # Independent double-precision summation; evidence arguments are <=1.
    terms = []
    for k in range(1000):
        term = (-x) ** k / math.gamma(beta * k + 1)
        terms.append(term)
        if k > 20 and abs(term) < 2e-17:
            return math.fsum(terms)
    raise RuntimeError("independent series did not settle")


def main() -> None:
    d = json.loads(PATH.read_text())
    assertions = 0

    def ok(value: bool) -> None:
        nonlocal assertions
        assert value
        assertions += 1

    ok(set(d) == EXPECTED_KEYS)
    ok(d["schema"] == "hcs-c277-caputo-dirichlet-heat-v1")
    ok(d["candidate_id"] == "HCS-C277")
    ok(d["source_commit"] == SOURCE)
    ok(d["fixed_epoch"] == 1788220800)
    ok(d["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    ok(d["evaluator"]["sha256"] == EVALUATOR)
    ok(d["payload_sha256"] == payload_hash(d))
    ok(d["owner"]["state_space"] == "L2((0,pi))")
    ok(d["theorem_contract"]["sharp_smoothing"] ==
       "for beta<1, t>0, and theta>=0, A^theta*S_beta(t) is bounded iff theta<=1")
    ok(d["theorem_contract"]["negative_theta_context"] ==
       "theta<0 also gives a bounded operator because A>=I, but it is outside the declared theta>=0 smoothing domain")
    ok(d["theorem_contract"]["sharp_schatten"].endswith("p>1/2"))
    ok(d["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"])
    ok(d["route_a"]["overall"] == "ROUTE_A_REJECTED")
    ok(d["route_a"]["route_b_invocation_allowed"] is False)
    for value in d["scope_flags"].values():
        ok(value is False)

    for row in d["regression"]["mittag_leffler_scalar_cells"]:
        beta, x = float(q(row["beta"])), float(q(row["x"]))
        ok(abs(float(row["value"]) - ml_double(beta, x)) < 3e-13)
        ok(20 < row["series_terms"] < 1000)

    last_by_beta: dict[str, float] = {}
    for row in d["regression"]["spectral_cells"]:
        beta = float(q(row["beta"])); n = row["mode"]
        scale = q(row["t_power_beta"]); x = q(row["spectral_argument"])
        ok(x == n * n * scale)
        value = float(row["multiplier"])
        ok(abs(value - ml_double(beta, float(x))) < 3e-13)
        ok(0 < value < last_by_beta.get(row["beta"], 2.0))
        last_by_beta[row["beta"]] = value

    for row in d["regression"]["nonsemigroup_witnesses"]:
        beta = float(q(row["beta"])); t = 0.25
        one = ml_double(beta, t**beta); joined = ml_double(beta, (2*t)**beta)
        defect = joined-one*one
        ok(abs(float(row["composition_defect"])-defect) < 3e-13)
        ok(row["semigroup_identity"] is (q(row["beta"]) == 1))
        ok(abs(defect) < 1e-13 if beta == 1 else abs(defect) > 1e-8)

    previous_error = math.inf
    for block in d["regression"]["beta_half_long_time"]:
        qtime = block["t_power_beta"]
        max_error = 0.0
        for row in block["modes"]:
            n = row["mode"]; x = n*n*qtime
            scaled = qtime * special.erfcx(x)
            limit = 1/(n*n*math.sqrt(math.pi))
            error = abs(scaled-limit); max_error=max(max_error,error)
            ok(abs(float(row["scaled_multiplier"])-scaled) < 3e-15)
            ok(abs(float(row["resolvent_limit"])-limit) < 3e-15)
            ok(abs(float(row["absolute_error"])-error) < 3e-15)
        ok(abs(float(block["operator_grid_max_error"])-max_error) < 3e-15)
        ok(max_error < previous_error)
        previous_error = max_error

    for row in d["regression"]["smoothing_threshold_cells"]:
        theta = q(row["theta_A_power"])
        ok(theta >= 0)
        ok(q(row["sobolev_gain"]) == 2*theta)
        ok(q(row["tail_power_in_mode"]) == 2*theta-2)
        ok(row["bounded_L2_operator"] is (theta <= 1))

    for row in d["regression"]["schatten_threshold_cells"]:
        p = q(row["p"])
        ok(q(row["comparison_series_power"]) == 2*p)
        ok(row["in_S_p"] is (p > Q(1, 2)))

    counts = d["regression"]["counts"]
    ok(counts == {"scalar_cells": 24, "spectral_cells": 192, "nonsemigroup_witnesses": 6,
                  "long_time_mode_cells": 96, "smoothing_cells": 35, "schatten_cells": 25})
    dois = {x["doi"] for x in d["sources"]}
    ok("10.1090/S0002-9904-1948-09132-7" in dois)
    ok("10.1016/j.jmaa.2011.04.058" in dois)
    print(f"C277 independent checker: PASS ({assertions} assertions; spectral, smoothing, Schatten, and memory audit)")


if __name__ == "__main__":
    main()
