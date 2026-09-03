#!/usr/bin/env python3
"""Canonical exact event evidence for HCS-C346."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c346_skorokhod_evidence.json"
SOURCE = "1af63b945e19b5f94ac1cb76f93af5ac66d3d562"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
EVAL_RAW = "4cad63c30708b42af42f3ee1f3563e8d31b2de8ae08047170c6b93050474a36c"
EVAL_SEMANTIC = "a9363fdab6fc2cd797ced2beb1d1f277876db3afcd69cbf37a8ad7f9de18fe4a"

CASES = (
    (F(1, 4), F(1, 4), "symmetric_corner", ((0, 0), (-1, 0), (-1, -1), (0, -2), (-3, 1), (1, 1))),
    (F(4, 9), F(1, 4), "asymmetric_corner", ((1, 0), (0, -1), (-2, -1), (1, -3), (-1, 2), (2, 2))),
    (F(9, 16), F(1, 9), "weak_return", ((0, 2), (-1, 1), (-2, -3), (1, -1), (-4, 0), (0, 0))),
    (F(0), F(3, 2), "lower_triangular", ((0, 0), (-1, 0), (0, -2), (-2, -1), (2, -4), (1, 0))),
    (F(2), F(0), "upper_triangular", ((1, 1), (-2, 0), (0, -1), (-3, 2), (1, -4), (0, 0))),
    (F(0), F(0), "normal_reflection", ((0, 0), (-1, 2), (-3, -1), (1, -4), (-2, 0), (2, 2))),
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


def rat(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def pair(v: tuple[F, F]) -> list[str]:
    return [rat(v[0]), rat(v[1])]


def leaves(v) -> int:
    if type(v) is dict:
        return sum(leaves(x) for x in v.values())
    if type(v) is list:
        return sum(leaves(x) for x in v)
    return 1


def semantic_hash(v) -> str:
    raw = json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return semantic_hash(body)


def mat_state(x: tuple[F, F], y: tuple[F, F], rho: F, sigma: F) -> tuple[F, F]:
    return x[0] + y[0] - rho * y[1], x[1] - sigma * y[0] + y[1]


def event_increment(z0: tuple[F, F], rho: F, sigma: F) -> tuple[F, F]:
    """Solve the two-dimensional jump LCP by its four active sets."""
    candidates: list[tuple[F, F]] = []
    tests = [(F(0), F(0))]
    tests.append((-z0[0], F(0)))
    tests.append((F(0), -z0[1]))
    det = 1 - rho * sigma
    if det != 0:
        tests.append(((-z0[0] - rho * z0[1]) / det,
                      (-sigma * z0[0] - z0[1]) / det))
    for d1, d2 in tests:
        if d1 < 0 or d2 < 0:
            continue
        z1 = z0[0] + d1 - rho * d2
        z2 = z0[1] - sigma * d1 + d2
        if z1 >= 0 and z2 >= 0 and d1 * z1 == 0 and d2 * z2 == 0:
            if (d1, d2) not in candidates:
                candidates.append((d1, d2))
    if len(candidates) != 1:
        raise ArithmeticError(f"event LCP has {len(candidates)} candidates")
    return candidates[0]


def solve_path(nodes: tuple[tuple[int, int], ...], rho: F, sigma: F):
    y = (F(0), F(0))
    rows = []
    for index, raw_x in enumerate(nodes):
        x = (F(raw_x[0]), F(raw_x[1]))
        z0 = mat_state(x, y, rho, sigma)
        d = (F(0), F(0)) if index == 0 else event_increment(z0, rho, sigma)
        y = y[0] + d[0], y[1] + d[1]
        z = mat_state(x, y, rho, sigma)
        rows.append({
            "event": index,
            "input": pair(x),
            "regulator_increment": pair(d),
            "regulator": pair(y),
            "state": pair(z),
            "active_axes": [i + 1 for i, value in enumerate(d) if value > 0],
            "nonnegative_and_complementary": z[0] >= 0 and z[1] >= 0 and d[0] * z[0] == 0 and d[1] * z[1] == 0,
        })
    return rows


def running_map(nodes, y_rows, rho: F, sigma: F):
    out1, out2 = [], []
    m1 = m2 = F(0)
    for x, y in zip(nodes, y_rows):
        m1 = max(m1, -F(x[0]) + rho * y[1])
        m2 = max(m2, -F(x[1]) + sigma * y[0])
        out1.append(m1)
        out2.append(m2)
    return list(zip(out1, out2))


def weighted_norm(rows, w1: F, w2: F) -> F:
    return max((max(abs(a) / w1, abs(b) / w2) for a, b in rows), default=F(0))


def rational_sqrt(value: F) -> F:
    p, q = isqrt(value.numerator), isqrt(value.denominator)
    if p * p != value.numerator or q * q != value.denominator:
        raise AssertionError("fixture lacks a rational square root")
    return F(p, q)


def case_row(index, rho: F, sigma: F, label: str, nodes):
    events = solve_path(nodes, rho, sigma)
    fixed = [(F(e["regulator"][0]), F(e["regulator"][1])) for e in events]
    fixed_check = running_map(nodes, fixed, rho, sigma)
    if fixed_check != fixed:
        raise AssertionError("direct event solution is not the running-supremum fixed point")
    stretched = tuple(value for node in nodes for value in (node, node))
    stretched_events = solve_path(stretched, rho, sigma)
    retained = [stretched_events[2 * j + 1]["regulator"] for j in range(len(nodes))]
    if retained != [event["regulator"] for event in events]:
        raise AssertionError("pause insertion changed the regulator")
    picard = []
    if rho > 0 and sigma > 0:
        w1, w2 = rational_sqrt(rho), rational_sqrt(sigma)
        q = w1 * w2
        current = [(F(0), F(0)) for _ in nodes]
        previous_delta = None
        for iteration in range(9):
            nxt = running_map(nodes, current, rho, sigma)
            delta = weighted_norm([(a - c, b - d) for (a, b), (c, d) in zip(nxt, current)], w1, w2)
            contraction = previous_delta is None or delta <= q * previous_delta
            error = weighted_norm([(a - c, b - d) for (a, b), (c, d) in zip(fixed, nxt)], w1, w2)
            picard.append({"iteration": iteration + 1, "successive_norm": rat(delta), "fixed_point_error": rat(error), "contraction_check": contraction})
            current, previous_delta = nxt, delta
    return {
        "case_id": f"sk-{index:02d}",
        "label": label,
        "rho": rat(rho),
        "sigma": rat(sigma),
        "determinant": rat(1 - rho * sigma),
        "well_posed": rho * sigma < 1,
        "event_rows": events,
        "fixed_point_check": True,
        "stretched_event_count": len(stretched_events),
        "pause_reparameterization_check": True,
        "picard_rows": picard,
    }


def threshold_rows():
    nonunique = []
    for h in ((0, 0, 0), (0, 1, 1), (0, 1, 2)):
        y = [[str(v), str(v)] for v in h]
        nonunique.append({"h": [str(v) for v in h], "regulator": y, "state": [["0", "0"] for _ in h], "valid": True})
    no_solution = []
    for rho, sigma, label in ((F(1), F(1), "critical"), (F(2), F(1), "supercritical"), (F(1, 2), F(3), "supercritical_asymmetric")):
        z0 = (F(-1), F(-1))
        candidates = 0
        det = 1 - rho * sigma
        trials = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1))]
        if det:
            trials.append(((-z0[0] - rho * z0[1]) / det, (-sigma * z0[0] - z0[1]) / det))
        for d1, d2 in trials:
            z1, z2 = z0[0] + d1 - rho * d2, z0[1] - sigma * d1 + d2
            if d1 >= 0 and d2 >= 0 and z1 >= 0 and z2 >= 0 and d1 * z1 == d2 * z2 == 0:
                candidates += 1
        no_solution.append({"label": label, "rho": rat(rho), "sigma": rat(sigma), "product": rat(rho * sigma), "negative_jump": ["-1", "-1"], "lcp_candidate_count": candidates})
    return {"critical_nonuniqueness": nonunique, "negative_jump_nonexistence": no_solution}


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C346 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    rows = [case_row(i + 1, *case) for i, case in enumerate(CASES)]
    data = {
        "schema": "hcs-c346-oblique-skorokhod-v1",
        "candidate_id": "HCS-C346",
        "obstruction_id": "HEN-O330",
        "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR},
        "evaluation_lock": {"relative_path": "evaluations/route_a/HCS-C346/2026-09-03.yaml", "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC},
        "model": {
            "equation": "z=x+R y in the nonnegative quadrant, R=[[1,-rho],[-sigma,1]]",
            "regulator": "each y_i is cadlag and nondecreasing with y_i(0)=0",
            "complementarity": "the post-jump Stieltjes integral of z_i against dy_i vanishes",
            "inputs": "two-dimensional cadlag paths with x(0) nonnegative",
        },
        "theorem_contract": {
            "sharp_threshold": "the problem has a unique solution for every input exactly when rho sigma is strictly below one",
            "fixed_point": "y1=L(x1-rho y2) and y2=L(x2-sigma y1), with L(f)(t)=sup over s<=t of [-f(s)] positive part; x(0) nonnegative and rho sigma below one force y(0)=0",
            "contraction": "for positive rho and sigma the weighted sup norm has exact contraction factor sqrt(rho sigma)",
            "stability": "the regulator Lipschitz constant is at most 1/(1-q) and the state constant at most 2/(1-q) in the same weighted norm",
            "structure": "the map is causal, preserves continuous inputs, and commutes with continuous nondecreasing onto time changes",
            "sharp_failure": "at product one zero input has infinitely many regulators, while at product at least one a simultaneous negative jump can have no complementarity solution",
            "boundaries": "normal reflection, one-sided triangular coupling, simultaneous jumps, axes, corner, and the strict threshold are explicit",
        },
        "case_rows": rows,
        "threshold_rows": threshold_rows(),
        "boundary_atlas": [
            {"face": "rho sigma < 1", "status": "global existence and uniqueness for every cadlag input"},
            {"face": "rho sigma = 1", "status": "zero input has a nonunique regulator cone and a simultaneous negative jump has no solution"},
            {"face": "rho sigma > 1", "status": "the simultaneous negative jump supplies a no-solution witness"},
            {"face": "rho=0 or sigma=0", "status": "triangular explicit regulation; the positive-weight contraction formula is replaced by direct substitution"},
            {"face": "rho=sigma=0", "status": "two independent one-dimensional running-supremum reflections"},
            {"face": "jumps", "status": "state and complementarity are evaluated after each regulator jump"},
        ],
        "collision_boundary": {
            "C332": "scalar Moreau play moves an interval and has memory loops rather than a two-axis oblique reflection threshold",
            "C266": "skew Brownian motion uses one stochastic local-time interface rather than a deterministic quadrant path map",
            "C279": "total-variation flow is a spatial subgradient semigroup rather than an oblique Skorokhod regulator",
            "C238": "dry friction is a Filippov capture flow rather than a two-dimensional complementarity map",
        },
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "nonclaims": [
            "No priority is claimed for orthant Skorokhod maps or M-matrix well-posedness.",
            "Finite event paths test implementation conventions and do not prove the all-input theorem.",
            "The matrix determinant is not a dynamical or target determinant.",
            "No stochastic reflected-Brownian limit is claimed for the deterministic input theorem.",
            "No target arithmetic local data, Euler factors, root numbers, automorphy, divisor, functional equation, zero match, Hilbert--Polya operator, or Route B input is asserted.",
        ],
        "references": [
            {"doi": "10.1214/aop/1176994471", "role": "orthant reflected Brownian motion and reflection-matrix source"},
            {"doi": "10.1080/17442509108833688", "role": "Lipschitz continuity and Skorokhod-map well-posedness source"},
        ],
    }
    data["enumeration"] = {
        "case_rows": len(rows),
        "event_rows": sum(len(r["event_rows"]) for r in rows),
        "picard_rows": sum(len(r["picard_rows"]) for r in rows),
        "critical_nonunique_witnesses": len(data["threshold_rows"]["critical_nonuniqueness"]),
        "no_solution_witnesses": len(data["threshold_rows"]["negative_jump_nonexistence"]),
    }
    data["enumeration"]["audited_leaf_count"] = leaves(data) + 1
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C346_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")


if __name__ == "__main__":
    main()
