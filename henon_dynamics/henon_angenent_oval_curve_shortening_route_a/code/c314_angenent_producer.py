#!/usr/bin/env python3
"""Produce deterministic analytic/numerical receipts for HCS-C314."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c314_angenent_evidence.json"
SOURCE = "1938bae19e5a92f9ce2411aafdc68323bd641bd0"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
mp.mp.dps = 90

R_VALUES = [
    "1/64", "1/32", "1/16", "1/12", "1/10", "1/8", "1/6", "1/5",
    "1/4", "1/3", "2/5", "1/2", "3/5", "2/3", "3/4", "4/5",
    "7/8", "9/10", "15/16", "31/32",
]
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


def dec(x: mp.mpf) -> str:
    return mp.nstr(x, 72, strip_zeros=False)


def mfrac(q: Fraction) -> mp.mpf:
    return mp.mpf(q.numerator) / q.denominator


def point_row(r: mp.mpf, c: mp.mpf, index: int) -> dict:
    x = mp.acos(c)
    y = mp.acosh(c / r)
    a = mp.sqrt(1 - r * r)
    sx = mp.sin(x)
    shy = mp.sinh(y)
    q2 = sx * sx + r * r * shy * shy
    kappa = c / a
    tx, ty = -mp.tan(x), -mp.tanh(y)
    g2 = tx * tx + ty * ty
    ax = -(1 / mp.cos(x) ** 2)
    by = -(1 / mp.cosh(y) ** 2)
    arrival = -(ax * ty * ty + by * tx * tx) / g2
    return {
        "point_index": index,
        "cos_x": dec(c),
        "x": dec(x),
        "y_upper": dec(y),
        "level_residual": dec(mp.cos(x) - r * mp.cosh(y)),
        "gradient_norm_squared": dec(q2),
        "curvature": dec(kappa),
        "inward_speed": dec(kappa),
        "arrival_time": dec(mp.log(mp.cos(x)) - mp.log(mp.cosh(y))),
        "arrival_pde_lhs": dec(arrival),
    }


def parameter_row(text: str) -> dict:
    q = Fraction(text)
    r = mfrac(q)
    t = mp.log(r)
    a = mp.sqrt(1 - r * r)
    alpha = mp.acos(r)
    height_half = mp.acosh(1 / r)
    area_formula = -2 * mp.pi * t
    # Endpoint roundoff can move cos(alpha)/r below one by a few ulps;
    # clamp that endpoint and discard the corresponding zero imaginary fuzz.
    area_quad = mp.re(4 * mp.quad(lambda xx: mp.acosh(max(mp.mpf(1), mp.cos(xx) / r)), [0, alpha]))
    length_formula = 4 * a * mp.ellipk(a * a)
    length_quad = 4 * mp.quad(
        lambda phi: a / mp.sqrt(1 - a * a * mp.sin(phi) ** 2),
        [0, mp.pi / 2],
    )
    points = []
    for j in range(11):
        c = r + (1 - r) * mp.mpf(j) / 10
        points.append(point_row(r, c, j))
    return {
        "r": text,
        "time": dec(t),
        "horizontal_width": dec(2 * alpha),
        "vertical_height": dec(2 * height_half),
        "area_formula": dec(area_formula),
        "area_quadrature": dec(area_quad),
        "length_formula": dec(length_formula),
        "length_quadrature": dec(length_quad),
        "curvature_min": dec(r / a),
        "curvature_max": dec(1 / a),
        "point_rows": points,
    }


def asymptotic_rows() -> tuple[list[dict], list[dict]]:
    extinction = []
    for k in (4, 5, 6, 7, 8, 9, 10, 12):
        tau = mp.mpf(2) ** (-k)
        t = -tau
        r = mp.e ** t
        ratios = []
        for j in range(17):
            theta = 2 * mp.pi * j / 17
            k2 = 1 / (1 - r * r) - mp.sin(theta) ** 2
            ratios.append(mp.sqrt(2 * tau * k2))
        extinction.append({
            "tau": dec(tau),
            "scaled_curvature_min": dec(min(ratios)),
            "scaled_curvature_max": dec(max(ratios)),
            "max_distance_from_one": dec(max(abs(v - 1) for v in ratios)),
        })
    grim = []
    for k in (4, 6, 8, 10, 12, 16, 20):
        r = mp.mpf(2) ** (-k)
        samples = []
        for x in (mp.mpf("0"), mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("0.75"), mp.mpf("1.0")):
            y = mp.acosh(mp.cos(x) / r)
            centered = y - mp.acosh(1 / r)
            target = mp.log(mp.cos(x))
            samples.append({"x": dec(x), "centered_upper": dec(centered), "grim_target": dec(target), "error": dec(centered - target)})
        grim.append({"r": dec(r), "samples": samples})
    return extinction, grim


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C314 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    rows = [parameter_row(text) for text in R_VALUES]
    extinction, grim = asymptotic_rows()
    data = {
        "schema": "hcs-c314-angenent-oval-v1",
        "candidate_id": "HCS-C314",
        "obstruction_id": "HEN-O298",
        "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": {
            "flow": "planar curve-shortening flow with inward normal velocity equal to curvature",
            "time_domain": "-infinity<t<0",
            "implicit_curve": "central component {cos(x)=exp(t) cosh(y), |x|<pi/2}; the unrestricted level set is the disjoint union of its 2pi-translates",
            "arrival_time": "T(x,y)=log(cos(x))-log(cosh(y)) on |x|<pi/2",
        },
        "theorem_contract": {
            "solution": "the central component is a smooth embedded strictly convex compact ancient solution with extinction at t=0; the unrestricted periodic level set is not a single curve",
            "geometry": "width, height, curvature extrema, area, and elliptic-integral length are exact",
            "foliation": "the central negative-time ovals foliate the open strip minus the origin; the extinction point is the zero-time leaf, and the arrival equation holds away from it",
            "forward_limit": "parabolic extinction rescaling converges smoothly to the unit circle",
            "backward_limit": "the two tips converge after translation to opposite Grim-Reaper profiles on compact sub-strips",
        },
        "parameter_rows": rows,
        "extinction_rows": extinction,
        "grim_rows": grim,
        "boundary_atlas": [
            {"face": "t=0", "status": "single extinction point, not a smooth timeslice"},
            {"face": "t=-infinity", "status": "strip and two-tip asymptotic limit, not an added timeslice"},
            {"face": "classification", "status": "the package does not reprove the literature-wide classification of convex ancient solutions"},
            {"face": "dimension", "status": "planar curve shortening only; no higher-dimensional ancient-oval theorem"},
        ],
        "collision_boundary": {
            "C281": "homogeneous Ricci flow on products of spheres, not a planar embedded curve flow",
            "C299": "a radial Navier--Stokes self-similar vortex, not ancient curve shortening",
            "C304": "a periodic linear Cahn--Hilliard semigroup; its idea report reserved but did not package the Grim Reaper",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "nonclaims": [
            "No novelty or priority is claimed for the Angenent oval or its classical formulas.",
            "No all-solution classification, nonlinear stability theorem, or higher-dimensional extension is claimed.",
            "No target arithmetic datum, Euler factor, root number, automorphy, divisor law, functional equation, zero match, or Hilbert--Polya operator is asserted.",
        ],
        "references": [
            {"doi": "10.1007/978-1-4612-0393-3_2", "role": "Angenent 1992 explicit oval-formula ownership"},
            {"arxiv": "0806.1757", "role": "compact convex ancient-solution classification boundary"},
            {"arxiv": "1903.02022", "role": "modern convex ancient-solution classification and explicit equation"},
        ],
    }
    data["enumeration"] = {
        "parameter_rows": len(rows),
        "point_rows": sum(len(row["point_rows"]) for row in rows),
        "extinction_rows": len(extinction),
        "grim_parameter_rows": len(grim),
        "grim_sample_rows": sum(len(row["samples"]) for row in grim),
    }
    data["enumeration"]["audited_leaf_count"] = leaves(data) + 1
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C314_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")


if __name__ == "__main__":
    main()
