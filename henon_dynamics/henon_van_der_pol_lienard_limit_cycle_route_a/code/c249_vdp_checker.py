#!/usr/bin/env python3
"""Producer-independent checker for the C249 Van der Pol receipt."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
import math
import re
from pathlib import Path

from scipy.integrate import solve_ivp
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c249_vdp_evidence.json"
SOURCE = "3ff451e904f8f063e88c40ef87f4697a6586b1a5"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000
NUM = re.compile(r"^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?$")
TOP = {"schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
FLAGS = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}
MUS = [("-2", "time-reversed negative-damping orientation", "one repelling limit cycle", "one", "repelling"), ("-1", "time-reversed negative-damping orientation", "one repelling limit cycle", "one", "repelling"), ("0", "Hamiltonian center boundary", "continuum of harmonic ovals", "continuum", "neutral"), ("1/10", "strict Lienard positive-damping exterior", "one attracting limit cycle", "one", "attracting"), ("1/2", "strict Lienard positive-damping exterior", "one attracting limit cycle", "one", "attracting"), ("1", "strict Lienard positive-damping exterior", "one attracting limit cycle", "one", "attracting"), ("2", "strict Lienard positive-damping exterior", "one attracting limit cycle", "one", "attracting"), ("4", "strict Lienard positive-damping exterior", "one attracting limit cycle", "one", "attracting")]
CYCLE_MUS = [0.1, 0.5, 1.0, 2.0, 4.0]


def ph(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def numeric(value: object, label: str, ck) -> float:
    ck(isinstance(value, str) and NUM.fullmatch(value) is not None, label + " syntax")
    try:
        out = float(value)
    except Exception:
        out = float("nan")
    ck(math.isfinite(out), label + " finite")
    return out


def return_once(mu: float, y0: float, augmented: bool = False):
    def fun(_t, state):
        x, y = state[0], state[1]
        out = [y, mu * (1.0 - x * x) * y - x]
        if augmented:
            out.extend([mu * (1.0 - x * x), mu * (1.0 - x * x) * y * y, x * x + y * y])
        return out

    def event(_t, state):
        return state[0]

    event.direction = 1
    event.terminal = True
    init = [1.0e-8, float(y0)] + ([0.0, 0.0, 0.0] if augmented else [])
    sol = solve_ivp(fun, (0.0, 120.0), init, events=event, method="DOP853", rtol=3e-12, atol=3e-14, max_step=3e-2)
    if len(sol.t_events[0]) != 1:
        raise AssertionError(f"no upward return for mu={mu}, y={y0}")
    return float(sol.t_events[0][0]), [float(v) for v in sol.y_events[0][0]]


def reconstructed_cycle(mu: float):
    def displacement(y):
        _t, state = return_once(mu, y)
        return state[1] - y

    y = brentq(displacement, 0.05, 8.0, xtol=2e-11, rtol=1e-13, maxiter=100)
    return y, return_once(mu, y, augmented=True)


def validate(data: dict, reconstruct: bool = True) -> int:
    count = 0

    def ck(ok: bool, label: str):
        nonlocal count
        count += 1
        if not ok:
            raise AssertionError(label)

    def eq(actual, expected, label):
        ck(type(actual) is type(expected) and actual == expected, label)

    eq(set(data), TOP, "top-level closure")
    for key, value in (("schema", "hcs-c249-van-der-pol-lienard-limit-cycle-v1"), ("candidate_id", "HCS-C249"), ("evaluation_date", "2026-08-30"), ("source_commit", SOURCE), ("fixed_epoch", EPOCH), ("scope_literal", SCOPE)):
        eq(data[key], value, key)
    eq(data["evaluator"], {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    eq(data["payload_sha256"], ph(data), "payload hash")
    frozen = data["frozen_object"]
    for key, value in {
        "phase_space": "R^2 with coordinates (x,y)",
        "dynamics": "xdot=y, ydot=mu*(1-x^2)*y-x",
        "equivalent_equation": "xddot+mu*(x^2-1)*xdot+x=0",
        "parameters": "mu in R; scaled frequency omega>0 is handled by tau=omega*t",
        "clock": "physical time t",
        "section": "Sigma={(x,y): x=0,y>0}",
        "arithmetic_origin": "none; smooth polynomial Lienard oscillator",
    }.items():
        eq(frozen.get(key), value, "frozen " + key)
    route = data["route_a"]
    eq(route["tuple"], ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    eq(route["overall"], "ROUTE_A_REJECTED", "route verdict")
    eq(route["route_b_invocation_allowed"], False, "route B")
    ck(set(data["scope_flags"]) == FLAGS, "scope-key closure")
    ck(all(v is False for v in data["scope_flags"].values()), "scope flags false")
    for phrase in ("Lienard", "exactly one", "Floquet", "mu=0", "source-local", "no intrinsic rational-prime"):
        ck(phrase.lower() in json.dumps(data["theorem"], ensure_ascii=False).lower() + json.dumps(data["route_a"], ensure_ascii=False).lower(), "theorem phrase " + phrase)
    theorem = data["theorem"]
    for key, value in {
        "lienard_uniqueness": "For every mu>0, F(x)=mu*(x^3/3-x) satisfies the Lienard hypotheses and the flow has exactly one hyperbolic attracting periodic orbit surrounding the origin; every non-equilibrium bounded recurrent trajectory is that cycle.",
        "center_face": "At mu=0 the Hamiltonian E=(x^2+y^2)/2 is conserved, so every positive level is a harmonic oval of period 2*pi and the periodic set is a continuum.",
        "energy_and_floquet": "For mu!=0, E_dot=mu*(1-x^2)y^2; on a periodic cycle the balance integral vanishes, while the nontrivial Floquet multiplier is exp(integral div X dt)=exp(mu*integral(1-x^2)dt).",
        "boundaries": "The mu=0 center, negative-mu time reversal, omega=0 scaling face, and section orientation are separate; no asymptotic period coefficient is inferred from a finite numerical fit.",
    }.items():
        eq(theorem.get(key), value, "theorem " + key)

    reg = data["regression"]
    eq(reg["parameter_row_count"], 8, "parameter count")
    eq(reg["cycle_row_count"], 5, "cycle count")
    eq(len(reg["parameter_rows"]), 8, "parameter rows length")
    pkeys = {"mu", "regime", "equilibrium", "periodic_orbits", "primitive_cycle_count", "cycle_stability", "theorem_source"}
    for i, (mu, regime, cyc, cnt, stab) in enumerate(MUS):
        row = reg["parameter_rows"][i]
        eq(set(row), pkeys, f"parameter {i} keys")
        eq(row["mu"], mu, f"parameter {i} mu")
        eq(row["regime"], regime, f"parameter {i} regime")
        eq(row["periodic_orbits"], cyc, f"parameter {i} cycle")
        eq(row["primitive_cycle_count"], cnt, f"parameter {i} count")
        eq(row["cycle_stability"], stab, f"parameter {i} stability")
        ck("origin" in row["equilibrium"], f"parameter {i} equilibrium")
        ck("Lienard" in row["theorem_source"], f"parameter {i} source")

    ckeys = {"mu", "section", "section_y", "return_y", "return_residual", "period", "divergence_integral", "energy_balance", "floquet_multiplier", "radius_squared_integral", "numerical_method", "status"}
    cycles = reg["cycle_rows"]
    ck(len(cycles) == len(CYCLE_MUS), "cycle rows length")
    for i, mu in enumerate(CYCLE_MUS):
        row = cycles[i]
        eq(set(row), ckeys, f"cycle {i} keys")
        eq(row["section"], "x=0, y>0; upward return", f"cycle {i} section")
        yobs = numeric(row["section_y"], f"cycle {i} section_y", ck)
        yret = numeric(row["return_y"], f"cycle {i} return_y", ck)
        resid = numeric(row["return_residual"], f"cycle {i} residual", ck)
        period = numeric(row["period"], f"cycle {i} period", ck)
        div = numeric(row["divergence_integral"], f"cycle {i} divergence", ck)
        eb = numeric(row["energy_balance"], f"cycle {i} balance", ck)
        floq = numeric(row["floquet_multiplier"], f"cycle {i} floquet", ck)
        rad = numeric(row["radius_squared_integral"], f"cycle {i} radius", ck)
        eq(row["mu"], format(mu, ".15e"), f"cycle {i} mu")
        ck(yobs > 0 and period > 0 and rad > 0, f"cycle {i} positivity")
        ck(abs(yret - yobs) < 3e-8 and abs(resid) < 3e-8, f"cycle {i} return residual")
        ck(abs(eb) < 3e-8, f"cycle {i} energy balance")
        ck(div < 0 and 0 < floq < 1, f"cycle {i} attracting floquet")
        if reconstruct:
            ycalc, state = reconstructed_cycle(mu)
            tcalc = return_once(mu, ycalc, augmented=True)
            for observed, expected, label in ((yobs, ycalc, "section_y"), (period, tcalc[0], "period"), (div, tcalc[1][2], "divergence"), (eb, tcalc[1][3], "energy"), (rad, tcalc[1][4], "radius")):
                ck(abs(observed - expected) <= 2e-7 * max(1.0, abs(expected)), f"cycle {i} {label} reconstruction")
            ck(abs(floq - math.exp(tcalc[1][2])) <= 2e-7 * max(1.0, abs(floq)), f"cycle {i} floquet reconstruction")
        ck("DOP853" in row["numerical_method"] and "finite regression" in row["status"], f"cycle {i} provenance")

    ids = [x.get("identity_id") for x in data["exact_identities"]]
    ck(len(ids) == 12 and len(set(ids)) == 12, "identity ledger")
    for required in ("lienard_form", "energy", "cycle_balance", "floquet", "positive_case", "negative_case", "center_boundary"):
        ck(required in ids, "identity " + required)
    formulas = {x.get("identity_id"): x.get("formula") for x in data["exact_identities"]}
    for key, expected in {
        "vector_field": "xdot=y; ydot=mu*(1-x^2)*y-x",
        "lienard_form": "xddot+mu*(x^2-1)*xdot+x=0",
        "energy": "E=(x^2+y^2)/2; Edot=mu*(1-x^2)*y^2",
        "divergence": "div X=mu*(1-x^2)",
    }.items():
        eq(formulas.get(key), expected, "identity formula " + key)
    ck(len(data["citations"]) == 3, "citation count")
    ck(data["citations"][1]["url"] == "https://doi.org/10.1215/S0012-7094-42-00928-1", "Levinson DOI")
    ck(len(data["nonclaims"]) == 5, "nonclaim count")
    return count


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", type=Path, default=DEFAULT)
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    data = json.loads(args.evidence.read_text())
    if args.quick:
        print(f"C249 quick hostile preflight: PASS ({validate(data, reconstruct=False)} assertions)")
    else:
        print(f"C249 independent checker: PASS ({validate(data)} assertions; Lienard cycle, Floquet, boundaries)")


if __name__ == "__main__":
    main()
