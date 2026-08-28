#!/usr/bin/env python3
"""Canonical certificate for the time-optimal bounded double integrator."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

SOURCE_COMMIT = "86c7bb8a39cdd1b8e941e45833b068170ca06287"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c222_double_integrator_evidence.json"
A_VALUES = [F(1, 2), F(1), F(2)]
X_VALUES = [F(-2), F(-1), F(-1, 2), F(0), F(1, 2), F(1), F(2)]
V_VALUES = [F(-2), F(-1), F(0), F(1), F(2)]
WORKING_DIGITS = 100
SERIALIZED_DIGITS = 82


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def q(value: F) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def fmt(value: mp.mpf) -> str:
    return mp.nstr(value, SERIALIZED_DIGITS, strip_zeros=False)


def sgn(value: F) -> int:
    return (value > 0) - (value < 0)


def row(a: F, x: F, v: F) -> dict:
    switch = x + v * abs(v) / (2 * a)
    if x == 0 and v == 0:
        branch, s, rad = "origin", 0, F(0)
        t1 = t2 = total = mp.mpf(0)
        sx = sv = tx = tv = mp.mpf(0)
        u1 = u2 = 0
        hjb = "not_applicable"
    elif switch == 0:
        branch, s, rad = "direct_brake", 0, F(0)
        total = abs(q(v)) / q(a)
        t1, t2 = total, mp.mpf(0)
        u1, u2 = -sgn(v), 0
        sx, sv, tx, tv = q(x), q(v), mp.mpf(0), mp.mpf(0)
        hjb = "nonsmooth_switching_curve"
    else:
        branch, s = "one_switch", sgn(switch)
        ss = mp.mpf(s)
        rad = v * v / (2 * a * a) + F(s) * x / a
        root = mp.sqrt(q(rad))
        t1 = ss * q(v) / q(a) + root
        t2 = root
        total = t1 + t2
        u1, u2 = -s, s
        sx = ss * q(a) * q(rad) / 2
        sv = -ss * q(a) * root
        tx = sx + sv * t2 + ss * q(a) * t2 * t2 / 2
        tv = sv + ss * q(a) * t2
        tx_grad = ss / (q(a) * root)
        tv_grad = ss / q(a) + q(v) / (q(a) * q(a) * root)
        hjb = fmt(1 + q(v) * tx_grad - q(a) * abs(tv_grad))
    return {
        "case_id": f"a{a}_x{x}_v{v}", "a": str(a), "x": str(x), "v": str(v),
        "switching_function": str(switch), "branch": branch, "side_sign": s,
        "radicand": str(rad), "first_arc_time": fmt(t1), "second_arc_time": fmt(t2),
        "total_time": fmt(total), "first_control_over_a": u1, "second_control_over_a": u2,
        "switch_x": fmt(sx), "switch_v": fmt(sv), "terminal_x": fmt(tx),
        "terminal_v": fmt(tv), "hjb_residual": hjb,
    }


def build() -> dict:
    mp.mp.dps = WORKING_DIGITS
    rows = [row(a, x, v) for a in A_VALUES for x in X_VALUES for v in V_VALUES]
    counts = {name: sum(r["branch"] == name for r in rows) for name in ("origin", "direct_brake", "one_switch")}
    data = {
        "schema": "hcs-c222-double-integrator-v1",
        "candidate_id": "HCS-C222",
        "evaluation_date": "2026-08-28",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "The bounded double integrator admits a global one-switch minimum-time synthesis and closed value function",
        "frozen_object": {
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
        },
        "theorem": {
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
        },
        "regression": {
            "a_values": [str(z) for z in A_VALUES], "x_values": [str(z) for z in X_VALUES],
            "v_values": [str(z) for z in V_VALUES], "state_rows": rows,
            "boundary_rows": [
                {"boundary_id": "origin", "statement": "T(0,0)=0 and the zero-duration control is admissible"},
                {"boundary_id": "switching_curve", "statement": "F=0 is a direct braking branch and the two off-curve formulas meet continuously"},
                {"boundary_id": "zero_acceleration", "statement": "for a=0 only (0,0) reaches rest at the origin in finite time"},
                {"boundary_id": "reflection", "statement": "simultaneous state and control reflection preserves transfer time"},
                {"boundary_id": "parabolic_scaling", "statement": "(x,v,t) maps to (lambda^2*x,lambda*v,lambda*t) at fixed a"},
            ],
        },
        "summary": {"state_row_count": len(rows), "boundary_row_count": 5, "branch_counts": counts, "serialized_decimal_digits": SERIALIZED_DIGITS},
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
            "strongest_positive": "A complete global synthesis, value function and independent optimality certificate are intrinsic to this control system.",
            "strongest_failure": "The Pontryagin Hamiltonian is only a formal variational hint: there is no intrinsic prime carrier, orbit clock, arithmetic divisor, target analytic structure or natural Hilbert-Polya lift.",
        },
        "scope_flags": {k: False for k in ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]},
        "citations": [
            {"key": "RomanoCurti2020", "claim": "minimum-time bounded normal LTI control, reduction to the origin, and double-integrator context", "title": "Time-optimal control of linear time invariant systems between two arbitrary states", "authors": "Marcello Romano and Fabio Curti", "venue": "Automatica 120, 109151", "date": "2020", "url": "https://doi.org/10.1016/j.automatica.2020.109151", "persistent_url": "https://doi.org/10.1016/j.automatica.2020.109151"}
        ],
        "nonclaims": [
            "priority for bang-bang double-integrator synthesis or Pontryagin's maximum principle",
            "the finite rational grid proves the all-state theorem",
            "the nonsmooth value function is a dynamical zeta or spectral determinant",
            "the Pontryagin Hamiltonian is a Hilbert-Polya operator or an arithmetic quantization",
            "a target divisor, Euler factor, root number, automorphy, external peer review, or Route-B authorization",
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
    print(json.dumps({"status": "C222_PRODUCER_PASS", "state_rows": data["summary"]["state_row_count"], "payload_sha256": data["payload_sha256"], "output": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
