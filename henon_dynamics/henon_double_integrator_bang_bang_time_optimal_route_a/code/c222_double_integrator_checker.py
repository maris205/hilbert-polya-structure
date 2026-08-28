#!/usr/bin/env python3
"""Producer-independent recursive and numerical checker for C222."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c222_double_integrator_evidence.json"
SOURCE_COMMIT = "86c7bb8a39cdd1b8e941e45833b068170ca06287"
EVALUATOR = {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
HEADLINE = "The bounded double integrator admits a global one-switch minimum-time synthesis and closed value function"
A_VALUES = [F(1, 2), F(1), F(2)]
X_VALUES = [F(-2), F(-1), F(-1, 2), F(0), F(1, 2), F(1), F(2)]
V_VALUES = [F(-2), F(-1), F(0), F(1), F(2)]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def q(value: F) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def sgn(value: F) -> int:
    return (value > 0) - (value < 0)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(parser.parse_args().evidence.read_text())
    mp.mp.dps = 100
    assertions = 0

    def check(condition, message: str) -> None:
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(message)

    def keys(obj, expected, where: str) -> None:
        check(isinstance(obj, dict), where + " mapping")
        check(set(obj) == set(expected), where + " keys")

    keys(data, ["schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "summary", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"], "top")
    keys(data["evaluator"], ["path", "version", "sha256"], "evaluator")
    keys(data["frozen_object"], ["state_space", "dynamics", "parameters", "clock", "switching_convention", "normalization", "determinant_convention", "arithmetic_origin", "allowed_data", "forbidden_data"], "frozen")
    keys(data["theorem"], ["switching_curve", "direct_branch", "off_curve_radicand", "arc_times", "control", "switch_state", "terminal_identity", "reachable_set_certificate", "optimality", "hjb", "symmetries", "boundaries"], "theorem")
    keys(data["regression"], ["a_values", "x_values", "v_values", "state_rows", "boundary_rows"], "regression")
    keys(data["summary"], ["state_row_count", "boundary_row_count", "branch_counts", "serialized_decimal_digits"], "summary")
    keys(data["summary"]["branch_counts"], ["origin", "direct_brake", "one_switch"], "branch_counts")
    keys(data["route_a"], ["tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"], "route")
    flags = ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]
    keys(data["scope_flags"], flags, "scope_flags")
    check(data["schema"] == "hcs-c222-double-integrator-v1", "schema")
    check(data["candidate_id"] == "HCS-C222" and data["evaluation_date"] == "2026-08-28", "identity")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["scope_literal"] == SCOPE and data["evaluator"] == EVALUATOR, "locks")
    check(data["headline"] == HEADLINE, "headline")
    expected_frozen = {
        "state_space": "R^2 with state (x,v) and terminal state (0,0)",
        "dynamics": "x_dot=v, v_dot=u with measurable control |u|<=a",
        "parameters": "a>0; physical elapsed time t>=0",
        "clock": "minimum physical transfer time, without fitted or logarithmic reparametrization",
        "switching_convention": "F_a(x,v)=x+v*|v|/(2a); off F=0 let s=sign(F)",
        "normalization": "mass is one and the acceleration bound is a in physical coordinates",
        "determinant_convention": "none; this is a reachable-set and HJB/Pontryagin problem",
        "arithmetic_origin": "none; all rational sentinels are source-local regression inputs",
        "allowed_data": "exact rational a,x,v and independently reconstructed radicals",
        "forbidden_data": "prime or zero tables, target labels, fitted clocks, Euler factors and Route-B input",
    }
    expected_theorem = {
        "switching_curve": "F_a(x,v)=x+v*|v|/(2a)=0",
        "direct_branch": "On F=0, u=-a*sign(v) for T=|v|/a; the origin has T=0",
        "off_curve_radicand": "For s=sign(F), D=v^2/(2a^2)+s*x/a is positive",
        "arc_times": "t1=s*v/a+sqrt(D), t2=sqrt(D), T=s*v/a+2*sqrt(D)",
        "control": "u=-s*a on [0,t1), then u=s*a on [t1,T]",
        "switch_state": "(x1,v1)=(s*a*D/2,-s*a*sqrt(D)), which lies on F_a=0",
        "terminal_identity": "The two arcs give (x(T),v(T))=(0,0), and t1,t2 are nonnegative",
        "reachable_set_certificate": "Any transfer in time T obeys integral(u)=-v and integral(t*u)=x; the sharp rearrangement interval is [-a*T^2/4-v*T/2+v^2/(4a), a*T^2/4-v*T/2-v^2/(4a)], and equality is attained only by one-switch bang-bang controls up to null sets",
        "optimality": "The affine Pontryagin switching function permits at most one switch; the continuous value is the global viscosity solution of min_|u|<=a{1+v*T_x+u*T_v}=0 and the displayed control attains equality",
        "hjb": "Off F=0, T_x=s/(a*sqrt(D)), T_v=s/a+v/(a^2*sqrt(D)), sign(T_v)=s and 1+v*T_x-a*|T_v|=0",
        "symmetries": "T_a(-x,-v)=T_a(x,v); T_a(lambda^2*x,lambda*v)=lambda*T_a(x,v) for lambda>0",
        "boundaries": "At a=0 only the origin has finite rest-to-rest time; all other states have T=infinity",
    }
    check(data["frozen_object"] == expected_frozen, "frozen semantics")
    check(data["theorem"] == expected_theorem, "theorem semantics")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED" and data["route_a"]["route_b_invocation_allowed"] is False, "route verdict")
    check(all(value is False for value in data["scope_flags"].values()), "scope flags")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["regression"]["a_values"] == [str(z) for z in A_VALUES], "a grid")
    check(data["regression"]["x_values"] == [str(z) for z in X_VALUES], "x grid")
    check(data["regression"]["v_values"] == [str(z) for z in V_VALUES], "v grid")

    row_keys = ["case_id", "a", "x", "v", "switching_function", "branch", "side_sign", "radicand", "first_arc_time", "second_arc_time", "total_time", "first_control_over_a", "second_control_over_a", "switch_x", "switch_v", "terminal_x", "terminal_v", "hjb_residual"]
    seen = set()
    counts = {"origin": 0, "direct_brake": 0, "one_switch": 0}
    tol = mp.mpf("1e-70")
    for i, row in enumerate(data["regression"]["state_rows"]):
        keys(row, row_keys, f"row[{i}]")
        a, x, v = F(row["a"]), F(row["x"]), F(row["v"])
        check(a in A_VALUES and x in X_VALUES and v in V_VALUES, f"row[{i}] domain")
        ident = (a, x, v)
        check(ident not in seen, f"row[{i}] duplicate")
        seen.add(ident)
        check(row["case_id"] == f"a{a}_x{x}_v{v}", f"row[{i}] id")
        switch = x + v * abs(v) / (2 * a)
        check(row["switching_function"] == str(switch), f"row[{i}] switching")
        if x == 0 and v == 0:
            expected = "origin"
        elif switch == 0:
            expected = "direct_brake"
        else:
            expected = "one_switch"
        check(row["branch"] == expected, f"row[{i}] branch")
        counts[expected] += 1
        if expected == "origin":
            check(row["side_sign"] == 0 and row["radicand"] == "0", f"row[{i}] origin metadata")
            check(abs(mp.mpf(row["total_time"])) < tol, f"row[{i}] origin time")
            check(row["first_control_over_a"] == 0 and row["second_control_over_a"] == 0, f"row[{i}] origin controls")
            check(all(abs(mp.mpf(row[name])) < tol for name in ["first_arc_time", "second_arc_time", "switch_x", "switch_v", "terminal_x", "terminal_v"]), f"row[{i}] origin numerics")
            check(row["hjb_residual"] == "not_applicable", f"row[{i}] origin HJB label")
        elif expected == "direct_brake":
            T = abs(q(v)) / q(a)
            check(row["side_sign"] == 0 and row["radicand"] == "0", f"row[{i}] direct metadata")
            check(abs(mp.mpf(row["total_time"]) - T) < tol, f"row[{i}] direct time")
            check(abs(mp.mpf(row["first_arc_time"]) - T) < tol and abs(mp.mpf(row["second_arc_time"])) < tol, f"row[{i}] direct arcs")
            check(row["first_control_over_a"] == -sgn(v) and row["second_control_over_a"] == 0, f"row[{i}] direct controls")
            check(abs(mp.mpf(row["switch_x"]) - q(x)) < tol and abs(mp.mpf(row["switch_v"]) - q(v)) < tol, f"row[{i}] direct switch state")
            tx = q(x) + q(v) * T - sgn(v) * q(a) * T * T / 2
            tv = q(v) - sgn(v) * q(a) * T
            check(abs(tx) < tol and abs(tv) < tol, f"row[{i}] direct terminal")
            check(abs(mp.mpf(row["terminal_x"])) < tol and abs(mp.mpf(row["terminal_v"])) < tol, f"row[{i}] direct serialized terminal")
            check(row["hjb_residual"] == "nonsmooth_switching_curve", f"row[{i}] direct HJB label")
        else:
            s = sgn(switch)
            ss = mp.mpf(s)
            D = v * v / (2 * a * a) + F(s) * x / a
            check(D > 0 and row["radicand"] == str(D) and row["side_sign"] == s, f"row[{i}] radicand")
            root = mp.sqrt(q(D))
            t1, t2 = ss * q(v) / q(a) + root, root
            check(t1 >= 0 and t2 > 0, f"row[{i}] nonnegative times")
            check(abs(mp.mpf(row["first_arc_time"]) - t1) < tol, f"row[{i}] t1")
            check(abs(mp.mpf(row["second_arc_time"]) - t2) < tol, f"row[{i}] t2")
            check(abs(mp.mpf(row["total_time"]) - (t1 + t2)) < tol, f"row[{i}] total")
            check(row["first_control_over_a"] == -s and row["second_control_over_a"] == s, f"row[{i}] controls")
            x1 = q(x) + q(v) * t1 - ss * q(a) * t1 * t1 / 2
            v1 = q(v) - ss * q(a) * t1
            check(abs(x1 - ss * q(a) * q(D) / 2) < tol, f"row[{i}] switch x")
            check(abs(v1 + ss * q(a) * root) < tol, f"row[{i}] switch v")
            check(abs(mp.mpf(row["switch_x"]) - x1) < tol and abs(mp.mpf(row["switch_v"]) - v1) < tol, f"row[{i}] serialized switch")
            check(abs(x1 + v1 * t2 + ss * q(a) * t2 * t2 / 2) < tol, f"row[{i}] terminal x")
            check(abs(v1 + ss * q(a) * t2) < tol, f"row[{i}] terminal v")
            check(abs(mp.mpf(row["terminal_x"])) < tol and abs(mp.mpf(row["terminal_v"])) < tol, f"row[{i}] serialized terminal")
            switching_at_one = x1 + v1 * abs(v1) / (2 * q(a))
            check(abs(switching_at_one) < tol, f"row[{i}] switch curve")
            Tx = ss / (q(a) * root)
            Tv = ss / q(a) + q(v) / (q(a) ** 2 * root)
            check(s * Tv > 0, f"row[{i}] gradient sign")
            residual = 1 + q(v) * Tx - q(a) * abs(Tv)
            check(abs(residual) < tol and abs(mp.mpf(row["hjb_residual"])) < tol, f"row[{i}] HJB")
    check(len(seen) == len(A_VALUES) * len(X_VALUES) * len(V_VALUES), "row closure")
    check(data["summary"] == {"state_row_count": len(seen), "boundary_row_count": 5, "branch_counts": counts, "serialized_decimal_digits": 82}, "summary")

    boundaries = {
        "origin": "T(0,0)=0 and the zero-duration control is admissible",
        "switching_curve": "F=0 is a direct braking branch and the two off-curve formulas meet continuously",
        "zero_acceleration": "for a=0 only (0,0) reaches rest at the origin in finite time",
        "reflection": "simultaneous state and control reflection preserves transfer time",
        "parabolic_scaling": "(x,v,t) maps to (lambda^2*x,lambda*v,lambda*t) at fixed a",
    }
    check(len(data["regression"]["boundary_rows"]) == len(boundaries), "boundary count")
    for i, item in enumerate(data["regression"]["boundary_rows"]):
        keys(item, ["boundary_id", "statement"], f"boundary[{i}]")
        check(item["boundary_id"] in boundaries and item["statement"] == boundaries[item["boundary_id"]], f"boundary[{i}] semantics")
    for i, citation in enumerate(data["citations"]):
        keys(citation, ["key", "claim", "title", "authors", "venue", "date", "url", "persistent_url"], f"citation[{i}]")
    check(data["citations"] == [{"key": "RomanoCurti2020", "claim": "minimum-time bounded normal LTI control, reduction to the origin, and double-integrator context", "title": "Time-optimal control of linear time invariant systems between two arbitrary states", "authors": "Marcello Romano and Fabio Curti", "venue": "Automatica 120, 109151", "date": "2020", "url": "https://doi.org/10.1016/j.automatica.2020.109151", "persistent_url": "https://doi.org/10.1016/j.automatica.2020.109151"}], "citation semantics")
    expected_nonclaims = [
        "priority for bang-bang double-integrator synthesis or Pontryagin's maximum principle",
        "the finite rational grid proves the all-state theorem",
        "the nonsmooth value function is a dynamical zeta or spectral determinant",
        "the Pontryagin Hamiltonian is a Hilbert-Polya operator or an arithmetic quantization",
        "a target divisor, Euler factor, root number, automorphy, external peer review, or Route-B authorization",
    ]
    check(data["nonclaims"] == expected_nonclaims, "nonclaims")
    print(json.dumps({"status": "C222_CHECKER_PASS", "assertions": assertions, "state_rows": len(seen), "branch_counts": counts, "producer_imported": False}, sort_keys=True))


if __name__ == "__main__":
    main()
