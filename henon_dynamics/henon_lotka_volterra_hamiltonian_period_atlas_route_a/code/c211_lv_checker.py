#!/usr/bin/env python3
"""Independent checker for the C211 Lotka--Volterra certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
import re
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import lambertw as scipy_lambertw

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c211_lv_evidence.json"
SOURCE_COMMIT = "e8054522273dbd545f9d406978e5d4648c627918"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PARAMETERS = [
    ("unit", F(1), F(1), F(1), F(1)),
    ("fast_center", F(2), F(1), F(3), F(2)),
    ("slow_center", F(1, 2), F(3), F(2), F(5, 2)),
    ("mixed_scale", F(3, 2), F(2, 3), F(5, 4), F(7, 3)),
    ("large_rates", F(5), F(4, 3), F(7, 2), F(9, 5)),
    ("small_rates", F(2, 5), F(7, 4), F(3, 5), F(11, 6)),
]
ENERGIES = [F(1, 20), F(1, 5), F(1, 2), F(1)]
NUMBER_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+|[eE][+-]?[0-9]+)$")


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def level_hash(level: dict) -> str:
    body = dict(level)
    body.pop("level_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def potential(s: mp.mpf) -> mp.mpf:
    return mp.expm1(s) - s


def branches(r: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    if r < 0:
        r = mp.mpf("0")
    z = -mp.exp(-1 - r)
    # This checker intentionally uses a different variable name and evaluates
    # the two branches independently of the producer implementation.
    left = -mp.lambertw(z, 0) - 1 - r
    right = -mp.lambertw(z, -1) - 1 - r
    return mp.re(left), mp.re(right)


def recompute(a: mp.mpf, c: mp.mpf, h: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    lo, hi = branches(h / c)
    mid = (lo + hi) / 2
    half = (hi - lo) / 2

    def integrand(theta: mp.mpf, want_area: bool) -> mp.mpf:
        jac = mp.cos(theta)
        if abs(jac) < mp.mpf("1e-28"):
            return mp.mpf("0")
        u = mid + half * mp.sin(theta)
        rr = (h - c * potential(u)) / a
        rr = max(rr, mp.mpf("0"))
        lv, uv = branches(rr)
        if want_area:
            return (uv - lv) * half * jac
        return (1 / (1 - mp.exp(lv)) + 1 / (mp.exp(uv) - 1)) * half * jac / a

    area = mp.re(mp.quad(lambda t: integrand(t, True), [-mp.pi / 2, 0, mp.pi / 2]))
    period = mp.re(mp.quad(lambda t: integrand(t, False), [-mp.pi / 2, 0, mp.pi / 2]))
    return lo, hi, area, period


def heterogeneous_ode_period(a: float, c: float, h: float, lo: float, hi: float,
                              period_hint: float) -> float:
    """Integrate the log-flow and detect a transverse section crossing.

    This is intentionally a different numerical path from recompute: it uses
    SciPy's DOP853 event integrator rather than quadrature.  The start is just
    to the right of the midpoint on the lower branch; the first positive
    crossing of that section is one full physical period.
    """
    # Starting at the right turning point avoids a section-time offset.  The
    # initial v=0 event is discarded; the next direction=+1 crossing is one
    # complete orbit (the intervening left turning point has direction -1).
    u0 = hi

    def flow(_time, state):
        u, v = state
        return [a * (1.0 - np.exp(v)), c * (np.exp(u) - 1.0)]

    def section(_time, state):
        return state[1]

    section.direction = 1
    section.terminal = False
    horizon = max(1.5 * period_hint, 1.0)
    max_step = max(period_hint / 200.0, 1.0e-3)
    solution = solve_ivp(flow, (0.0, horizon), [u0, 0.0], method="DOP853",
                         rtol=2.0e-11, atol=2.0e-13, max_step=max_step,
                         events=section)
    noninitial = [float(value) for value in solution.t_events[0] if value > 1.0e-8]
    if not noninitial:
        raise AssertionError("heterogeneous ODE did not find a full-period crossing")
    return noninitial[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(label)

    def exact(actual, expected, label: str) -> None:
        check(type(actual) is type(expected), label + " type")
        check(actual == expected, label)

    def close(actual: str, expected: mp.mpf, label: str, tol=mp.mpf("2e-25")) -> None:
        check(isinstance(actual, str) and NUMBER_RE.fullmatch(actual) is not None, label + " syntax")
        check(abs(mp.mpf(actual) - expected) <= tol * max(1, abs(expected)), label + " value")

    top = {"schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal",
           "evaluator", "headline", "frozen_object", "theorem", "regression",
           "exact_identities", "route_a", "scope_flags", "citations", "nonclaims",
           "payload_sha256"}
    check(set(data) == top, "top-level key closure")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    exact(data["schema"], "hcs-c211-lotka-volterra-v1", "schema")
    exact(data["candidate_id"], "HCS-C211", "candidate")
    exact(data["evaluation_date"], "2026-08-28", "date")
    exact(data["source_commit"], SOURCE_COMMIT, "source commit")
    exact(data["scope_literal"], SCOPE, "scope")
    exact(data["evaluator"], {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False, "route verdict")
    check(all(value is False for value in data["scope_flags"].values()), "scope firewall")
    check("period monotonicity" in data["theorem"]["explicit_nonclaims"], "period monotonicity boundary")
    check("high-energy" in data["theorem"]["explicit_nonclaims"], "high-energy boundary")
    check(len(data["regression"]["parameter_cases"]) == 6, "parameter case count")
    check(data["regression"]["quadrature_level_count"] == 24, "quadrature count")
    check(data["regression"]["working_decimal_digits"] == 45, "working precision")
    check(data["regression"]["serialized_significant_digits"] == 34, "serialized precision")

    # Check every per-level content hash before any expensive quadrature.  This
    # makes repaired-hash numeric mutations fail immediately rather than
    # spending a minute recomputing untouched levels.
    for case_index, case in enumerate(data["regression"]["parameter_cases"]):
        for level_index, level in enumerate(case["levels"]):
            check(isinstance(level["level_sha256"], str)
                  and level["level_sha256"] == level_hash(level),
                  f"level {case_index}/{level_index} hash preflight")

    mp.mp.dps = 45
    for idx, (row, spec) in enumerate(zip(data["regression"]["parameter_cases"], PARAMETERS)):
        case_id, aq, bq, cq, dq = spec
        check(set(row) == {"case_id", "a", "b", "c", "d", "center_x", "center_y", "center_period_limit", "levels"}, f"case {idx} keys")
        exact(row["case_id"], case_id, f"case {idx} id")
        exact([row[k] for k in ("a", "b", "c", "d")], [str(aq), str(bq), str(cq), str(dq)], f"case {idx} parameters")
        a, b, c, d = (mp.mpf(q.numerator) / q.denominator for q in (aq, bq, cq, dq))
        check(a > 0 and b > 0 and c > 0 and d > 0, f"case {idx} positivity")
        close(row["center_x"], c / d, f"case {idx} center x")
        close(row["center_y"], a / b, f"case {idx} center y")
        center_period = 2 * mp.pi / mp.sqrt(a * c)
        close(row["center_period_limit"], center_period, f"case {idx} center period")
        check(len(row["levels"]) == 4, f"case {idx} level count")
        for j, level in enumerate(row["levels"]):
            check(set(level) == {"h", "u_minus", "u_plus", "area", "period", "action", "period_over_center_limit", "branch_residual_minus", "branch_residual_plus", "level_sha256"}, f"level {idx}/{j} keys")
            check(isinstance(level["level_sha256"], str) and level["level_sha256"] == level_hash(level), f"level {idx}/{j} hash")
            hq = ENERGIES[j]
            exact(level["h"], str(hq), f"level {idx}/{j} energy")
            h = mp.mpf(hq.numerator) / hq.denominator
            lo, hi, area, period = recompute(a, c, h)
            close(level["u_minus"], lo, f"level {idx}/{j} lower branch")
            close(level["u_plus"], hi, f"level {idx}/{j} upper branch")
            close(level["area"], area, f"level {idx}/{j} area", mp.mpf("3e-22"))
            close(level["period"], period, f"level {idx}/{j} period", mp.mpf("3e-22"))
            ode_period = heterogeneous_ode_period(float(a), float(c), float(h), float(lo), float(hi), float(period))
            check(abs(ode_period - float(period)) <= 1.0e-8 * max(1.0, float(period)),
                  f"level {idx}/{j} heterogeneous ODE period")
            close(level["action"], area / (2 * mp.pi), f"level {idx}/{j} action", mp.mpf("3e-22"))
            close(level["period_over_center_limit"], period / center_period, f"level {idx}/{j} center ratio", mp.mpf("3e-22"))
            close(level["branch_residual_minus"], potential(lo) - h / c, f"level {idx}/{j} residual-", mp.mpf("1e-20"))
            close(level["branch_residual_plus"], potential(hi) - h / c, f"level {idx}/{j} residual+", mp.mpf("1e-20"))
            check(lo < 0 < hi, f"level {idx}/{j} branch ordering")
            check(area > 0 and period > 0, f"level {idx}/{j} positivity")
            check(period / center_period > mp.mpf("0.9") and period / center_period < mp.mpf("20"), f"level {idx}/{j} ratio sanity")
    check(len(data["exact_identities"]) == 6, "identity rows")
    for row, spec in zip(data["exact_identities"], PARAMETERS):
        check(row["case_id"] == spec[0], "identity case")
        check(row["hamiltonian_time_derivative"].endswith("= 0"), "Hamiltonian cancellation")
        check(row["hessian_determinant"].endswith(">0"), "Hessian positivity")
        check("exp(v)" in row["average_u_identity"] and "exp(u)" in row["average_v_identity"], "average identities")
    for citation in data["citations"]:
        check(set(citation) == {"key", "claim", "title", "authors", "venue", "year", "doi"}, "citation closure")
        check(citation["doi"].startswith("10."), "citation DOI")
    print(f"C211 independent checker: PASS ({checks} assertions; 24 Lambert-W quadrature levels)")
    print("strict positivity, action identity, center limit, and scope firewall: PASS")


if __name__ == "__main__":
    main()
