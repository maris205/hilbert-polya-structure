#!/usr/bin/env python3
"""Independent high-precision checker; imports no producer code."""
from __future__ import annotations

import hashlib
import json
import os
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
P = Path(os.environ.get("C270_EVIDENCE_IN", ROOT / "results/c270_heisenberg_evidence.json"))
SOURCE = "9cb7483e97ef82fdc06d45ecb3043f183ce22391"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
mp.mp.dps = 90
TOL = mp.mpf("1e-65")

# Declared independently of the producer.  It is compared with the evidence
# schema, then used to recount fields actually present in every row.
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
ROW_KEYS = {
    "trajectory_rows": set(NUMERIC_FIELD_SCHEMA["trajectory_rows"]) | {"at_first_cut"},
    "distance_rows": set(NUMERIC_FIELD_SCHEMA["distance_rows"]),
    "vertical_rows": set(NUMERIC_FIELD_SCHEMA["vertical_rows"]),
}


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def q(x: str) -> Q:
    return Q(x)


def m(x: Q) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def close(a, b) -> bool:
    return abs(mp.mpf(a) - mp.mpf(b)) <= TOL * max(1, abs(mp.mpf(a)), abs(mp.mpf(b)))


def main() -> None:
    d = json.loads(P.read_text())
    n = 0

    def ok(value) -> None:
        nonlocal n
        assert value
        n += 1

    ok(d["candidate_id"] == "HCS-C270")
    ok(d["source_commit"] == SOURCE)
    ok(d["fixed_epoch"] == 1788134400)
    ok(d["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    ok(d["evaluator"]["sha256"] == EVAL)
    ok(d["payload_sha256"] == payload_hash(d))
    ok(d["convention"]["frame"] == "X=d_x-(y/2)d_z, Y=d_y+(x/2)d_z, [X,Y]=d_z")
    ok(d["trajectory_contract"]["first_cut_time"] == "2*pi/abs(lambda)")
    ok(d["trajectory_contract"]["first_conjugate_time"] == "2*pi/abs(lambda)")
    ok(d["exponential_contract"]["jacobian"] == "r^3*t*(2-2*cos(s)-s*sin(s))/lambda^4, s=lambda*t")
    ok(d["exponential_contract"]["first_positive_zero"] == "s=2*pi; the first positive tan(s/2)=s/2 root is later")
    ok(d["distance_contract"]["implicit_angle"] == "4*z/rho^2=(theta-sin(theta)*cos(theta))/sin(theta)^2")
    ok(d["distance_contract"]["distance"] == "d=rho*theta/sin(theta)")
    ok(d["distance_contract"]["vertical_face"] == "rho=0 gives d=2*sqrt(pi*abs(z))")
    ok(d["distance_contract"]["cut_locus_from_identity"] == "{(0,0,z): z!=0}")
    ok(d["proof_contract"]["abnormal"] == "no nonconstant abnormal extremals because a covector annihilating X,Y and [X,Y] must vanish")
    ok(d["proof_contract"]["complete_geodesics"] == "there are no nontrivial closed complete geodesics: lambda=0 gives lines, while lambda!=0 has nonzero vertical drift per horizontal period")
    ok(d["proof_contract"]["scope"] == "only standard H^1; no theorem for arbitrary Carnot groups")
    ok(d["proof_contract"]["status"] == "PROVABLE AS STATED")
    ok(d["route_a"] == {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
                         "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False})
    for value in d["scope_flags"].values():
        ok(value is False)
    ok(d["source"]["doi"] == "10.1007/BF02392235")

    rows = d["regression"]["trajectory_rows"]
    for row in rows:
        lam = m(q(row["lambda"]))
        phi = m(q(row["phi_over_pi"])) * mp.pi
        phase = m(q(row["abs_phase_over_pi"])) * mp.pi
        s = mp.sign(lam) * phase
        t = phase / abs(lam)
        h1 = mp.cos(phi+s)
        h2 = mp.sin(phi+s)
        x = (mp.sin(phi+s)-mp.sin(phi))/lam
        y = (mp.cos(phi)-mp.cos(phi+s))/lam
        z = (s-mp.sin(s))/(2*lam**2)
        rho2 = x*x+y*y
        jac = t*(2-2*mp.cos(s)-s*mp.sin(s))/lam**4
        for key, val in (("t", t), ("s", s), ("h1", h1), ("h2", h2), ("x", x), ("y", y),
                         ("z", z), ("rho2", rho2), ("unit_speed", 1), ("jacobian_r_equals_1", jac)):
            ok(close(row[key], val))
        ok(close(rho2, 4*mp.sin(s/2)**2/lam**2))
        ok(close((-y*h1+x*h2)/2, (1-mp.cos(s))/(2*lam)))
        ok(row["at_first_cut"] is (q(row["abs_phase_over_pi"]) == Q(2)))
        if row["at_first_cut"]:
            ok(close(x, 0) and close(y, 0))

    drows = d["regression"]["distance_rows"]
    for row in drows:
        theta = m(q(row["theta_over_pi"])) * mp.pi
        rho = m(q(row["rho"]))
        mu = (theta-mp.sin(theta)*mp.cos(theta))/mp.sin(theta)**2
        z = rho*rho*mu/4
        lam = 2*mp.sin(theta)/rho
        dist = rho*theta/mp.sin(theta)
        ok(-mp.pi < theta < mp.pi and theta != 0)
        for key, val in (("mu", mu), ("z", z), ("lambda", lam), ("distance", dist),
                         ("reconstructed_time", 2*theta/lam), ("distance_squared", dist*dist)):
            ok(close(row[key], val))
        ok(close(4*z/(rho*rho), mu))
        ok(dist > 0)

    vrows = d["regression"]["vertical_rows"]
    for row in vrows:
        z = m(q(row["z"]))
        lam = mp.sign(z)*mp.sqrt(mp.pi/abs(z))
        dist = 2*mp.sqrt(mp.pi*abs(z))
        ok(close(row["lambda"], lam))
        ok(close(row["cut_time"], 2*mp.pi/abs(lam)))
        ok(close(row["distance"], dist))
        ok(close(row["distance_squared"], 4*mp.pi*abs(z)))

    regression = d["regression"]
    ok(regression["numeric_field_schema"] == NUMERIC_FIELD_SCHEMA)
    row_groups = {"trajectory_rows": rows, "distance_rows": drows, "vertical_rows": vrows}
    for row_name, group in row_groups.items():
        ok(all(set(row) == ROW_KEYS[row_name] for row in group))
    numeric_cells = sum(
        sum(field in row for field in NUMERIC_FIELD_SCHEMA[row_name])
        for row_name, group in row_groups.items()
        for row in group
    )
    counts = regression["counts"]
    ok((len(rows), len(drows), len(vrows)) == (800, 64, 12))
    ok(counts == {"trajectory_rows": len(rows), "distance_rows": len(drows),
                  "vertical_rows": len(vrows), "numeric_cells": numeric_cells})
    print(f"C270 independent checker: PASS ({n} assertions; Hamilton endpoints, Jacobian, distance, cut boundary)")


if __name__ == "__main__":
    main()
