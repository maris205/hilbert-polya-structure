#!/usr/bin/env python3
"""Deterministic high-precision receipt producer for HCS-C270."""
from __future__ import annotations

import hashlib
import json
import os
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("C270_EVIDENCE_OUT", ROOT / "results/c270_heisenberg_evidence.json"))
SOURCE = "9cb7483e97ef82fdc06d45ecb3043f183ce22391"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788134400
mp.mp.dps = 90

LAMBDAS = (Q(-5), Q(-3), Q(-2), Q(-1), Q(-1, 2), Q(1, 2), Q(1), Q(2), Q(3), Q(5))
PHI_PI = (Q(-3, 4), Q(-1, 2), Q(-1, 3), Q(0), Q(1, 5), Q(1, 2), Q(3, 4), Q(1))
PHASE_PI = (Q(1, 6), Q(1, 4), Q(1, 3), Q(1, 2), Q(2, 3), Q(1), Q(4, 3), Q(3, 2), Q(11, 6), Q(2))
THETA_PI = (Q(-7, 8), Q(-3, 4), Q(-2, 3), Q(-1, 2), Q(-1, 3), Q(-1, 4), Q(-1, 6), Q(-1, 8),
            Q(1, 8), Q(1, 6), Q(1, 4), Q(1, 3), Q(1, 2), Q(2, 3), Q(3, 4), Q(7, 8))
RADII = (Q(1, 2), Q(1), Q(2), Q(3))
VERTICAL_Z = (Q(-9), Q(-4), Q(-1), Q(-1, 4), Q(-1, 16), Q(-1, 100),
              Q(1, 100), Q(1, 16), Q(1, 4), Q(1), Q(4), Q(9))

# This schema is part of the evidence contract.  In particular, rational input
# coordinates such as ``lambda`` and ``rho`` are numeric cells too; counting
# only the derived decimal fields would under-report the receipt.
NUMERIC_FIELD_SCHEMA = {
    "trajectory_rows": [
        "lambda", "phi_over_pi", "abs_phase_over_pi", "t", "s", "h1", "h2",
        "x", "y", "z", "rho2", "unit_speed", "jacobian_r_equals_1",
    ],
    "distance_rows": [
        "theta_over_pi", "rho", "mu", "z", "lambda", "distance",
        "reconstructed_time", "distance_squared",
    ],
    "vertical_rows": ["z", "lambda", "cut_time", "distance", "distance_squared"],
}


def qstr(x: Q) -> str:
    return f"{x.numerator}/{x.denominator}"


def m(x: Q) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def ds(x: mp.mpf) -> str:
    if abs(x) < mp.mpf("1e-82"):
        x = mp.mpf(0)
    return mp.nstr(x, 76, strip_zeros=False)


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def numeric_cell_count(regression: dict, schema: dict[str, list[str]]) -> int:
    """Count present numeric fields from the explicit row schema."""
    return sum(
        sum(field in row for field in fields)
        for row_name, fields in schema.items()
        for row in regression[row_name]
    )


def trajectory_rows() -> list[dict]:
    rows = []
    for lq in LAMBDAS:
        lam = m(lq)
        sign = mp.sign(lam)
        for pq in PHI_PI:
            phi = m(pq) * mp.pi
            for aq in PHASE_PI:
                q = m(aq) * mp.pi
                s = sign * q
                t = q / abs(lam)
                h1 = mp.cos(phi + s)
                h2 = mp.sin(phi + s)
                x = (mp.sin(phi + s) - mp.sin(phi)) / lam
                y = (mp.cos(phi) - mp.cos(phi + s)) / lam
                z = (s - mp.sin(s)) / (2 * lam**2)
                rho2 = x*x + y*y
                jac = t * (2 - 2*mp.cos(s) - s*mp.sin(s)) / lam**4
                rows.append({
                    "lambda": qstr(lq), "phi_over_pi": qstr(pq), "abs_phase_over_pi": qstr(aq),
                    "t": ds(t), "s": ds(s), "h1": ds(h1), "h2": ds(h2),
                    "x": ds(x), "y": ds(y), "z": ds(z), "rho2": ds(rho2),
                    "unit_speed": ds(h1*h1+h2*h2), "jacobian_r_equals_1": ds(jac),
                    "at_first_cut": aq == Q(2),
                })
    return rows


def distance_rows() -> list[dict]:
    rows = []
    for tq in THETA_PI:
        theta = m(tq) * mp.pi
        mu = (theta - mp.sin(theta)*mp.cos(theta)) / mp.sin(theta)**2
        for rq in RADII:
            rho = m(rq)
            z = rho*rho*mu/4
            distance = rho*theta/mp.sin(theta)
            lam = 2*mp.sin(theta)/rho
            time = 2*theta/lam
            rows.append({
                "theta_over_pi": qstr(tq), "rho": qstr(rq), "mu": ds(mu), "z": ds(z),
                "lambda": ds(lam), "distance": ds(distance), "reconstructed_time": ds(time),
                "distance_squared": ds(distance*distance),
            })
    return rows


def vertical_rows() -> list[dict]:
    rows = []
    for zq in VERTICAL_Z:
        z = m(zq)
        lam = mp.sign(z) * mp.sqrt(mp.pi / abs(z))
        cut_time = 2*mp.pi/abs(lam)
        rows.append({"z": qstr(zq), "lambda": ds(lam), "cut_time": ds(cut_time),
                     "distance": ds(2*mp.sqrt(mp.pi*abs(z))), "distance_squared": ds(4*mp.pi*abs(z))})
    return rows


def main() -> None:
    tr = trajectory_rows()
    dr = distance_rows()
    vr = vertical_rows()
    data = {
        "schema": "hcs-c270-heisenberg-cut-locus-v1",
        "candidate_id": "HCS-C270",
        "evaluation_date": "2026-09-01",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {"version": "0.2.0", "sha256": EVAL},
        "convention": {
            "manifold": "standard real Heisenberg H^1 in coordinates (x,y,z)",
            "frame": "X=d_x-(y/2)d_z, Y=d_y+(x/2)d_z, [X,Y]=d_z",
            "metric": "X,Y orthonormal; all displayed geodesics have unit speed",
            "hamiltonian": "H=((p_x-y p_z/2)^2+(p_y+x p_z/2)^2)/2",
            "lambda": "p_z is constant",
        },
        "trajectory_contract": {
            "lambda_zero": "x=t cos(phi), y=t sin(phi), z=0",
            "lambda_nonzero": "x=(sin(phi+lambda t)-sin(phi))/lambda; y=(cos(phi)-cos(phi+lambda t))/lambda; z=(lambda t-sin(lambda t))/(2 lambda^2)",
            "horizontal_controls": "h1=cos(phi+lambda t), h2=sin(phi+lambda t)",
            "first_cut_time": "2*pi/abs(lambda)",
            "first_conjugate_time": "2*pi/abs(lambda)",
        },
        "exponential_contract": {
            "parameters": "initial horizontal norm r, angle phi, vertical momentum lambda, time t",
            "jacobian": "r^3*t*(2-2*cos(s)-s*sin(s))/lambda^4, s=lambda*t",
            "factorization": "4*r^3*t*sin(s/2)*(sin(s/2)-(s/2)*cos(s/2))/lambda^4",
            "lambda_zero_limit": "r^3*t^5/12",
            "first_positive_zero": "s=2*pi; the first positive tan(s/2)=s/2 root is later",
        },
        "distance_contract": {
            "nonvertical_domain": "rho=sqrt(x^2+y^2)>0 and unique theta in (-pi,pi)",
            "implicit_angle": "4*z/rho^2=(theta-sin(theta)*cos(theta))/sin(theta)^2",
            "distance": "d=rho*theta/sin(theta)",
            "horizontal_face": "z=0 gives theta=0 and d=rho",
            "vertical_face": "rho=0 gives d=2*sqrt(pi*abs(z))",
            "cut_locus_from_identity": "{(0,0,z): z!=0}",
            "maxwell_boundary": "theta approaches sign(z)*pi and the endpoint loses the angle phi",
        },
        "proof_contract": {
            "abnormal": "no nonconstant abnormal extremals because a covector annihilating X,Y and [X,Y] must vanish",
            "minimality": "horizontal length equals planar length and z is signed planar area; the unique sub-full-turn Dido arcs and full circles give the stated minimizers",
            "uniqueness_before_cut": "the implicit-angle function is strictly increasing on (-pi,pi)",
            "complete_geodesics": "there are no nontrivial closed complete geodesics: lambda=0 gives lines, while lambda!=0 has nonzero vertical drift per horizontal period",
            "scope": "only standard H^1; no theorem for arbitrary Carnot groups",
            "status": "PROVABLE AS STATED",
        },
        "regression": {},
        "analytic_proof_obligations": [
            "canonical Hamilton equations and contact bracket", "closed-form exponential map",
            "Jacobian zero ordering", "Dido minimality and Maxwell merger", "implicit-angle monotonicity",
            "horizontal and vertical distance boundaries", "left-translation propagation of the identity cut locus",
        ],
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": {"arithmetic_local_data": False, "euler_factors": False, "root_numbers": False,
                        "automorphy": False, "target_divisor": False, "functional_equation": False,
                        "hilbert_polya_operator": False, "general_carnot_group_theorem": False},
        "nonclaims": ["No literature-priority claim is made.", "No result is asserted for arbitrary Carnot groups.",
                      "The sub-Riemannian Hamiltonian is not a target Hilbert--Polya operator."],
        "source": {"author": "Bernard Gaveau",
                   "title": "Principe de moindre action, propagation de la chaleur et estimees sous elliptiques sur certains groupes nilpotents",
                   "journal": "Acta Mathematica 139 (1977), 95--153", "doi": "10.1007/BF02392235",
                   "role": "primary classical lineage for the nilpotent sub-Riemannian model"},
    }
    regression = {
        "numeric_field_schema": NUMERIC_FIELD_SCHEMA,
        "trajectory_rows": tr,
        "distance_rows": dr,
        "vertical_rows": vr,
    }
    regression["counts"] = {
        "trajectory_rows": len(tr),
        "distance_rows": len(dr),
        "vertical_rows": len(vr),
        "numeric_cells": numeric_cell_count(regression, NUMERIC_FIELD_SCHEMA),
    }
    data["regression"] = regression
    data["payload_sha256"] = payload_hash(data)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C270_PRODUCER_PASS trajectories={len(tr)} distance={len(dr)} vertical={len(vr)} "
          f"numeric_cells={regression['counts']['numeric_cells']} payload={data['payload_sha256']}")


if __name__ == "__main__":
    main()
