#!/usr/bin/env python3
"""Deterministic finite receipts for HCS-C332."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c332_moreau_play_evidence.json"
SOURCE = "5ca65027918c0fce7ef9af82f3faf2e46ed6530c"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
EVAL_RAW = "97f9ec8a8abe0c6b4bf1a0a4609467088c6e78638d27329a382bd11068daa86b"
EVAL_SEMANTIC = "454ee341774e7da7c271ce9b88168d9dc0f5fcedf69aa8426cf8e7dd7eec35b9"

CASES = (
    (Fraction(0), Fraction(1), Fraction(1), "cornered"),
    (Fraction(-2), Fraction(3), Fraction(3), "maximum_plateau"),
    (Fraction(1), Fraction(5), Fraction(2), "minimum_plateau"),
    (Fraction(-3), Fraction(3), Fraction(3), "two_plateaus"),
    (Fraction(0), Fraction(5), Fraction(1), "cornered"),
    (Fraction(-2), Fraction(7), Fraction(2), "maximum_plateau"),
    (Fraction(0), Fraction(3), Fraction(0), "zero_radius"),
    (Fraction(2), Fraction(2), Fraction(1), "constant_input"),
    (Fraction(0), Fraction(0), Fraction(0), "constant_zero_radius"),
    (Fraction(-1), Fraction(2), Fraction(1, 2), "minimum_plateau"),
    (Fraction(1, 2), Fraction(5, 2), Fraction(3, 2), "smooth_reparameterization"),
    (Fraction(-5, 2), Fraction(1, 2), Fraction(3, 2), "two_plateaus"),
)

FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}


def rat(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def clamp(value: Fraction, low: Fraction, high: Fraction) -> Fraction:
    return min(high, max(low, value))


def poincare(z: Fraction, m: Fraction, M: Fraction, r: Fraction) -> Fraction:
    up = max(z, M-r)
    return min(up, m+r)


def initial_values(m: Fraction, r: Fraction) -> list[Fraction]:
    if r == 0:
        return [m]
    return [m-r, m-r/2, m, m+r/2, m+r]


def path(levels: list[Fraction], z: Fraction, r: Fraction) -> list[Fraction]:
    out = [z]
    current = z
    for value in levels[1:]:
        current = clamp(current, value-r, value+r)
        out.append(current)
    return out


def variation(values: list[Fraction]) -> Fraction:
    return sum((abs(b-a) for a,b in zip(values, values[1:])), Fraction(0))


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def case_row(index: int, m: Fraction, M: Fraction, r: Fraction, shape: str) -> dict:
    D = M-m
    chamber = "D_lt_2r" if D < 2*r else "D_eq_2r" if D == 2*r else "D_gt_2r"
    initials = []
    for z in initial_values(m, r):
        pz = poincare(z,m,M,r)
        initials.append({"initial": rat(z), "after_one_period": rat(pz), "after_two_periods": rat(poincare(pz,m,M,r))})
    fixed_low = M-r if D <= 2*r else m+r
    fixed_high = m+r
    representative = poincare(m, m, M, r)
    mid = (m+M)/2
    levels = [m, mid, M, M, mid, m]
    play = path(levels, representative, r)
    stop = [u-y for u,y in zip(levels, play)]
    stretched_levels = [m, m, mid, mid, M, M, M, mid, mid, m, m]
    stretched_play = path(stretched_levels, representative, r)
    var_y = variation(play); var_s = variation(stop); var_u = 2*D
    expected_y = 2*max(D-2*r, Fraction(0))
    return {
        "case_id": f"play-{index:02d}",
        "shape_tag": shape,
        "minimum": rat(m),
        "maximum": rat(M),
        "radius": rat(r),
        "range_D": rat(D),
        "chamber": chamber,
        "fixed_set_low": rat(fixed_low),
        "fixed_set_high": rat(fixed_high),
        "initial_rows": initials,
        "periodic_representative": rat(representative),
        "path_levels": [rat(v) for v in levels],
        "periodic_play_nodes": [rat(v) for v in play],
        "periodic_stop_nodes": [rat(v) for v in stop],
        "stretched_levels": [rat(v) for v in stretched_levels],
        "stretched_play_nodes": [rat(v) for v in stretched_play],
        "input_variation": rat(var_u),
        "play_variation": rat(var_y),
        "stop_variation": rat(var_s),
        "dissipation_integral": rat(r*var_y),
        "variation_formula_check": var_y == expected_y and var_u == var_y+var_s,
    }


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C332 producer refuses optimized Python")
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, default=OUTPUT); args = parser.parse_args()
    rows = [case_row(i+1,*case) for i,case in enumerate(CASES)]
    data = {
        "schema": "hcs-c332-moreau-play-v1",
        "candidate_id": "HCS-C332",
        "obstruction_id": "HEN-O316",
        "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR},
        "evaluation_lock": {"relative_path": "evaluations/route_a/HCS-C332/2026-09-03.yaml", "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC},
        "model": {
            "input": "T-periodic W1,1 function starting at minimum m, nondecreasing to maximum M, then nonincreasing to m; plateaus allowed",
            "constraint": "y(t) belongs to [u(t)-r,u(t)+r]",
            "inclusion": "-dy belongs to the normal cone of [u-r,u+r]",
            "stop_variable": "s=u-y belongs to [-r,r]",
            "parameters": "r nonnegative and D=M-m nonnegative",
        },
        "theorem_contract": {
            "segment_projection": "on every monotone segment y(t)=projection of the segment initial state onto [u(t)-r,u(t)+r]",
            "poincare_map": "from a minimum P(z)=min(m+r,max(M-r,z))",
            "chambers": "D<2r has fixed interval [M-r,m+r]; D=2r has one fixed point; D>2r has one fixed point m+r and a nontrivial loop",
            "entrainment": "P composed with P equals P, so every admissible state reaches a periodic response in at most one period",
            "structure": "the flow and P are order preserving and nonexpansive, and orientation-preserving absolutely continuous time changes preserving W1,1 admissibility leave the path response invariant",
            "variation": "Var(u)=Var(y)+Var(s), integral s dy=r Var(y), and on a periodic single excursion Var(y)=2 max(D-2r,0)",
            "boundaries": "r=0, D=0, equality, plateaus, and W1,1 corners are included; no weak-continuation or smoothness claim is needed",
        },
        "case_rows": rows,
        "boundary_atlas": [
            {"face": "D<2r", "status": "a continuum [M-r,m+r] of constant periodic play outputs"},
            {"face": "D=2r", "status": "the fixed interval collapses to one constant periodic output and dissipation remains zero"},
            {"face": "D>2r", "status": "one fixed state m+r and a unique nonconstant periodic play loop"},
            {"face": "r=0", "status": "y=u, s=0, P maps the singleton feasible state to itself, and dissipation is zero"},
            {"face": "D=0", "status": "the input is constant, P is the identity on [m-r,m+r], and every feasible constant output is periodic"},
            {"face": "plateaus and corners", "status": "the W1,1 projection formula holds almost everywhere and is insensitive to plateau duration"},
            {"face": "time reparameterization", "status": "only orientation-preserving absolutely continuous surjections preserving W1,1 admissibility are asserted"},
        ],
        "collision_boundary": {
            "C252": "the hysteretic relay oscillator has discrete guards and a hybrid switching cycle rather than a convex moving interval",
            "C238": "Coulomb dry friction is a forward Filippov capture law rather than a rate-independent play operator",
            "C310": "Dubins synthesis is endpoint-controlled bounded-curvature optimization rather than a constitutive sweeping process",
        },
        "route_a": {"tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "nonclaims": [
            "No priority is claimed for Moreau sweeping processes or scalar play operators.",
            "The analytic periodic classification carries no rational-prime labels.",
            "The normal-cone inclusion is not a natural self-adjoint or unitary quantization.",
            "Finite profiles are regression receipts and do not prove the W1,1 theorem.",
            "No target arithmetic local data, Euler factors, root numbers, automorphy, divisor, functional equation, zero match, or Hilbert--Polya operator is asserted.",
        ],
        "references": [
            {"doi": "10.1016/0022-0396(77)90085-7", "role": "Moreau moving-convex-set evolution source"},
            {"doi": "10.1007/978-3-642-61302-9", "role": "authoritative play and hysteresis monograph"},
            {"doi": "10.1007/978-1-4612-4048-8", "role": "authoritative scalar play, convexity, and dissipation reference"},
        ],
    }
    data["enumeration"] = {
        "case_rows": len(rows),
        "initial_rows": sum(len(row["initial_rows"]) for row in rows),
        "path_nodes": sum(len(row["path_levels"]) for row in rows),
        "reparameterized_nodes": sum(len(row["stretched_levels"]) for row in rows),
        "chambers": {name: sum(row["chamber"] == name for row in rows) for name in ("D_lt_2r", "D_eq_2r", "D_gt_2r")},
    }
    data["enumeration"]["audited_leaf_count"] = leaves(data)+1
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    print(f"C332_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")


if __name__ == "__main__":
    main()
