#!/usr/bin/env python3
"""Lambert-free Decimal checker for the C198 SIR certificate."""
from __future__ import annotations

import argparse
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c198_sir_evidence.json"
SOURCE_COMMIT = "c3a5b9bbb3b6d0881f395abe4a01accd322f69cb"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EXPECTED_HEADLINE = (
    "Every positive-parameter closed SIR trajectory has one exact "
    "dimensionless phase curve, a complete peak and final-size atlas, "
    "and monotone convergence to the disease-free equilibrium line"
)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def decimal_fraction(value: str) -> D:
    q = F(value)
    return D(q.numerator) / D(q.denominator)


def level(x: D) -> D:
    return x - x.ln()


def lower_root(constant: D, x0: D) -> D:
    lo = D("1e-100")
    hi = min(x0, D(1))
    for _ in range(360):
        mid = (lo + hi) / 2
        if level(mid) > constant:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def upper_root(constant: D, x0: D) -> D:
    lo = max(x0, D(1))
    hi = max(D(2), x0 + D(2))
    while level(hi) <= constant:
        hi *= 2
    for _ in range(360):
        mid = (lo + hi) / 2
        if level(mid) < constant:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    getcontext().prec = 105
    data = json.loads(args.evidence.read_text())
    assertions = 0

    def check(condition, message):
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(message)

    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["schema"] == "hcs-c198-sir-v1", "schema")
    check(data["candidate_id"] == "HCS-C198", "candidate")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["evaluator"]["sha256"] == EVALUATOR_SHA256, "evaluator")
    check(data["headline"] == EXPECTED_HEADLINE, "headline")
    check(data["citations"][0]["doi"] == "10.1098/rspa.1927.0118", "source DOI")
    check(data["citations"][1]["doi"] == "10.1093/imamat/hxu057", "Lambert DOI")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    check(all(value is False for value in data["scope_flags"].values()), "scope flags")

    tolerance = D("2e-79")
    regime_counts = {"sub": 0, "threshold": 0, "super": 0}
    for row in data["regression"]["cases"]:
        x0 = decimal_fraction(row["x0"])
        y0 = decimal_fraction(row["y0"])
        constant = x0 + y0 - x0.ln()
        check(row["invariant_rational_part"] == str(F(row["x0"]) + F(row["y0"])), "invariant rational part")
        check(row["invariant_log_argument"] == row["x0"], "invariant log argument")
        final_x = lower_root(constant, x0)
        companion = upper_root(constant, x0)
        check(abs(final_x - D(row["final_x_W0"])) < tolerance, "lower branch")
        check(abs(companion - D(row["companion_x_Wminus1"])) < tolerance, "upper branch")
        argument = -x0 * (-(x0 + y0)).exp()
        check(abs(argument - D(row["lambert_argument"])) < tolerance, "Lambert argument")
        check(abs(level(final_x) - constant) < D("1e-99"), "final equation")
        check(D(row["absolute_final_equation_residual"]) < D("1e-99"), "reported residual")
        check(0 < final_x < min(x0, D(1)), "lower ordering")
        check(companion > max(x0, D(1)), "upper ordering")
        check(row["final_below_x0_and_one"] is True, "lower flag")
        check(row["companion_above_x0_and_one"] is True, "upper flag")
        if x0 > 1:
            regime_counts["super"] += 1
            peak_x = D(1)
            peak_y = y0 + x0 - 1 - x0.ln()
            expected_regime = "interior_peak_after_initial_growth"
        elif x0 == 1:
            regime_counts["threshold"] += 1
            peak_x, peak_y = x0, y0
            expected_regime = "threshold_tangent_then_decay"
        else:
            regime_counts["sub"] += 1
            peak_x, peak_y = x0, y0
            expected_regime = "monotone_decay_from_initial_time"
        check(row["initial_regime"] == expected_regime, "regime")
        check(abs(D(row["peak_x"]) - peak_x) < tolerance, "peak x")
        check(abs(D(row["peak_y"]) - peak_y) < tolerance, "peak y")
        sensitivity = final_x / (final_x - 1)
        check(abs(D(row["d_final_x_d_y0"]) - sensitivity) < tolerance, "sensitivity")
        check(sensitivity < 0, "sensitivity sign")

    for row in data["regression"]["physical_scalings"]:
        beta, gamma = F(row["beta"]), F(row["gamma"])
        check(beta > 0 and gamma > 0, "positive physical parameters")
        check(F(row["susceptible_threshold_kappa"]) == gamma / beta, "kappa")
        check(F(row["dimensionless_time_tau_per_t"]) == gamma, "time scaling")
        check(F(row["dimensionless_state_scale"]) == beta / gamma, "state scaling")

    summary = data["summary"]
    check(summary["case_count"] == len(data["regression"]["cases"]) == 24, "case count")
    check(summary["subcritical_x_count"] == regime_counts["sub"] == 9, "subcritical count")
    check(summary["threshold_x_count"] == regime_counts["threshold"] == 3, "threshold count")
    check(summary["supercritical_x_count"] == regime_counts["super"] == 12, "supercritical count")
    check(summary["physical_scaling_count"] == len(data["regression"]["physical_scalings"]) == 4, "scaling count")
    check(summary["lambert_branch_values"] == 48, "branch count")
    print(json.dumps({
        "status": "C198_CHECKER_PASS",
        "assertions": assertions,
        "cases": summary["case_count"],
        "branch_values": summary["lambert_branch_values"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
