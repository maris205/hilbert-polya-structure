#!/usr/bin/env python3
"""Producer-independent recursive exact-schema checker for C210."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial, floor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c210_delay_evidence.json"
SOURCE_COMMIT = "e8054522273dbd545f9d406978e5d4648c627918"
EVAL = {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
TIMES = [F(i, 4) for i in range(13)]
SPECS = [
    ("a2_b1_tau1", F(2), F(1), F(1)), ("a1_b2_tau1_4", F(1), F(2), F(1, 4)),
    ("a1_b2_tau1", F(1), F(2), F(1)), ("a1_b2_tau2", F(1), F(2), F(2)),
    ("a1_b1_tau3", F(1), F(1), F(3)), ("a0_b2_tau1_4", F(0), F(2), F(1, 4)),
    ("a2_b0_tau1", F(2), F(0), F(1)), ("a0_b0_tau2", F(0), F(0), F(2)),
    ("a0_b1_tau1_4", F(0), F(1), F(1, 4)), ("a3_b1_tau0", F(3), F(1), F(0)),
    ("a1_b3_tau0", F(1), F(3), F(0)), ("a0_b0_tau0", F(0), F(0), F(0)),
]
HEADLINE = "The scalar retarded delay semigroup has a complete Lambert-W characteristic atlas and exact stability/Hopf boundaries"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def q(x: F) -> str:
    return str(x)


def term_string(a: F, b: F, tau: F, t: F) -> str:
    if tau == 0:
        return f"1(t=0); exp(-{q(a + b)}*t)(t>0)"
    if t < 0:
        return "0"
    out = []
    for n in range(floor(t / tau) + 1):
        coeff = (-b) ** n * (t - n * tau) ** n / F(factorial(n))
        out.append(f"{q(coeff)}*exp(-{q(a)}*({q(t)}-{q(n*tau)}))")
    return "+".join(out) or "0"


def regime(a: F, b: F, tau: F) -> str:
    if a == 0 and b == 0:
        return "zero_equation"
    if tau == 0:
        return "zero_delay_ode"
    if b == 0:
        return "no_delayed_feedback"
    if a >= b:
        return "exponentially_stable_all_delays"
    return "stable_before_hopf_or_unstable_after"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(ap.parse_args().evidence.read_text())
    assertions = 0

    def check(cond, msg):
        nonlocal assertions
        assertions += 1
        if not cond:
            raise AssertionError(msg)

    def keys(obj, expected, label):
        check(isinstance(obj, dict), f"{label} mapping")
        check(set(obj) == set(expected), f"{label} keys: {set(obj) ^ set(expected)}")

    keys(data, ["schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "summary", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"], "top")
    keys(data["evaluator"], ["path", "version", "sha256"], "evaluator")
    keys(data["frozen_object"], ["phase_space", "equation", "generator", "parameters", "clock", "normalization", "determinant_convention", "arithmetic_origin", "allowed_data", "forbidden_data"], "frozen_object")
    keys(data["theorem"], ["characteristic_equation", "lambert_w_spectrum", "fundamental_solution", "semigroup", "eventual_compactness", "spectral_mapping", "root_multiplicity", "stability_atlas", "hopf_boundary", "boundary_ledger", "periodic_orbit_status"], "theorem")
    keys(data["regression"], ["time_grid", "cases", "case_count", "hopf_formula_controls"], "regression")
    keys(data["summary"], ["case_count", "time_sample_count", "fundamental_symbolic_cell_count", "hopf_control_count"], "summary")
    keys(data["route_a"], ["tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"], "route_a")
    flag_keys = ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]
    keys(data["scope_flags"], flag_keys, "scope_flags")
    keys(data["citations"][0], ["key", "claim", "title", "authors", "report_number", "date", "url", "persistent_url"], "citation")

    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["schema"] == "hcs-c210-scalar-retarded-delay-v1", "schema")
    check(data["candidate_id"] == "HCS-C210", "candidate")
    check(data["evaluation_date"] == "2026-08-28", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["scope_literal"] == SCOPE, "scope")
    check(data["evaluator"] == EVAL, "evaluator lock")
    check(data["headline"] == HEADLINE, "headline")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "route overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    check(all(v is False for v in data["scope_flags"].values()), "scope flags")
    check(data["frozen_object"]["determinant_convention"].startswith("source characteristic determinant"), "determinant boundary")
    check(data["frozen_object"]["arithmetic_origin"] == "none; this is a scope-locked non-arithmetic control", "arithmetic boundary")
    check(data["theorem"]["root_multiplicity"].startswith("Delta'=1-b*tau"), "multiplicity theorem")
    check(data["theorem"]["hopf_boundary"].startswith("for b>a"), "Hopf theorem")
    check(data["theorem"]["spectral_mapping"] == "for t>tau, sigma(T(t))\\{0}=exp(t*sigma(A)); the algebraic multiplicity at a nonzero mu is the sum of characteristic-root multiplicities over all lambda with exp(t*lambda)=mu (collisions are aggregated)", "spectral mapping collision rule")
    expected_frozen = {
        "phase_space": "X=C([-tau,0],C) for tau>0; X=C({0},C) when tau=0",
        "equation": "x'(t)=-a*x(t)-b*x(t-tau), a>=0,b>=0,tau>=0",
        "generator": "A phi=phi'; D(A)={phi in C^1: phi'(0)=-a phi(0)-b phi(-tau)}",
        "parameters": "real a,b,tau>=0 and continuous initial history phi",
        "clock": "physical elapsed time t; no fitted or logarithmic clock",
        "normalization": "history norm ||phi||_infty and fundamental solution r(0)=1, r(t<0)=0",
        "determinant_convention": "source characteristic determinant Delta(lambda)=lambda+a+b*exp(-lambda*tau); not a target or Fredholm determinant",
        "arithmetic_origin": "none; this is a scope-locked non-arithmetic control",
        "allowed_data": "exact rational parameter sentinels and source-local symbolic identities",
        "forbidden_data": "prime/zero tables, arithmetic labels, fitted parameters, target divisors and external observations",
    }
    check(data["frozen_object"] == expected_frozen, "frozen object lock")
    expected_theorem = {
        "characteristic_equation": "Delta(lambda)=lambda+a+b*exp(-lambda*tau)",
        "lambert_w_spectrum": "for tau>0,b>0 every characteristic root is -a+tau^{-1} W_k(-b*tau*exp(a*tau)), with W_0 and W_-1 merged at -1/e",
        "fundamental_solution": "r(t)=sum_{n=0}^{floor(t/tau)}(-b)^n exp(-a*(t-n*tau))*(t-n*tau)^n/n! for t>=0 and tau>0",
        "semigroup": "the history solution operators T(t) form a strongly continuous retarded semigroup and satisfy T(t+s)=T(t)T(s)",
        "eventual_compactness": "T(t) is compact on C([-tau,0]) for every t>tau by the C^1 smoothing and Arzela-Ascoli",
        "spectral_mapping": "for t>tau, sigma(T(t))\\{0}=exp(t*sigma(A)); the algebraic multiplicity at a nonzero mu is the sum of characteristic-root multiplicities over all lambda with exp(t*lambda)=mu (collisions are aggregated)",
        "root_multiplicity": "Delta'=1-b*tau*exp(-lambda*tau); a multiple root is exactly lambda=-a-1/tau and b*tau*exp(a*tau)=exp(-1), and it is at most double",
        "stability_atlas": "if a>=b, all tau are exponentially stable except the zero equation; if b>a, stability holds exactly for 0<=tau<tau_c",
        "hopf_boundary": "for b>a, omega=sqrt(b^2-a^2), tau_c=acos(-a/b)/omega; at tau_c the only imaginary pair is +/-i omega and crossings are to the right",
        "boundary_ledger": "tau=0 gives x'=-(a+b)x; b=0 removes the delay; a=b=0 is the constant equation; a=b>0 stays stable for each finite tau but its gap tends to zero as tau grows",
        "periodic_orbit_status": "linear histories at a Hopf point form a two-dimensional center family, not isolated primitive cycles",
    }
    check(data["theorem"] == expected_theorem, "theorem lock")
    check(data["citations"][0]["persistent_url"] == "https://doi.org/10.1007/978-1-4612-4342-7", "citation DOI")

    rows = data["regression"]["cases"]
    check(len(rows) == len(SPECS), "case count")
    check(data["regression"]["time_grid"] == [q(t) for t in TIMES], "time grid")
    check(len({r.get("case_id") for r in rows}) == len(rows), "duplicate case ids")
    row_keys = ["case_id", "a", "b", "tau", "regime", "characteristic_equation", "fundamental_solution_terms_t_quarters", "reported_times", "zero_root_condition", "lambert_argument_prefactor", "branch_point_condition"]
    cells = 0
    for i, (cid, a, b, tau) in enumerate(SPECS):
        row = rows[i]
        keys(row, row_keys, f"case[{i}]")
        check(row["case_id"] == cid, f"case {i} id")
        check(F(row["a"]) == a and F(row["b"]) == b and F(row["tau"]) == tau, f"case {i} params")
        check(row["regime"] == regime(a, b, tau), f"case {i} regime")
        check(row["characteristic_equation"] == "lambda+a+b*exp(-lambda*tau)", f"case {i} Delta")
        check(row["reported_times"] == [q(t) for t in TIMES], f"case {i} times")
        terms = row["fundamental_solution_terms_t_quarters"]
        check(len(terms) == len(TIMES), f"case {i} term count")
        check(len(set(row["reported_times"])) == len(TIMES), f"case {i} duplicate times")
        for t, actual in zip(TIMES, terms):
            check(actual == term_string(a, b, tau, t), f"case {i} method-step term")
            cells += 1
        check(F(row["zero_root_condition"]) == a + b, f"case {i} zero root")
        check(F(row["lambert_argument_prefactor"]) == b * tau, f"case {i} Lambert prefactor")
        check(row["branch_point_condition"] == "b*tau*exp(a*tau)=exp(-1)", f"case {i} branch point condition")

    controls = data["regression"]["hopf_formula_controls"]
    control_keys = ["case_id", "a", "b", "omega", "tau_c"]
    expected_controls = [("a0_b1", "0", "1", "1", "pi/2"), ("a1_b2", "1", "2", "sqrt(3)", "acos(-1/2)/sqrt(3)"), ("a2_b3", "2", "3", "sqrt(5)", "acos(-2/3)/sqrt(5)")]
    check(len(controls) == len(expected_controls), "Hopf control count")
    for i, exp in enumerate(expected_controls):
        keys(controls[i], control_keys, f"Hopf[{i}]")
        check(tuple(controls[i][k] for k in control_keys) == exp, f"Hopf[{i}] formula")
    check(data["regression"]["case_count"] == len(rows), "regression case count")
    check(data["summary"]["case_count"] == len(rows), "summary cases")
    check(data["summary"]["time_sample_count"] == len(TIMES), "summary times")
    check(data["summary"]["fundamental_symbolic_cell_count"] == cells, "summary cells")
    check(data["summary"]["hopf_control_count"] == len(controls), "summary controls")
    expected_route = {
        "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "strongest_positive": "Lambert-W branches, exact method-of-steps resolvent, eventual compactness, and a complete nonnegative-parameter Hopf/stability atlas are source-local theorem progress.",
        "strongest_failure": "There is no intrinsic rational-prime carrier, isolated primitive-orbit ledger, target divisor or natural same-clock self-adjoint lift.",
    }
    check(data["route_a"] == expected_route, "route lock")
    expected_nonclaims = ["priority for delay equations or Lambert-W root theory", "a finite rational regression proves the all-parameter semigroup theorem", "Delta is a Fredholm determinant or a dynamical zeta", "any characteristic root is a Riemann zero or arithmetic local datum", "a Hilbert-Polya operator, target divisor, Euler factor, root number, automorphy, external review or Route-B authorization"]
    check(data["nonclaims"] == expected_nonclaims, "nonclaims lock")
    print(json.dumps({"status": "C210_CHECKER_PASS", "assertions": assertions, "fundamental_symbolic_cells": cells, "recursive_key_sets": 8 + len(rows) + len(controls), "producer_imported": False}, sort_keys=True))


if __name__ == "__main__":
    main()
