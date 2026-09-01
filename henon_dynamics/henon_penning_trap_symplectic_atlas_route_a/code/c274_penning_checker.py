#!/usr/bin/env python3
"""Producer-independent exact/high-precision checker for HCS-C274."""
from __future__ import annotations

import hashlib
import json
import os
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
P = Path(os.environ.get("C274_EVIDENCE_IN", ROOT / "results/c274_penning_evidence.json"))
SOURCE = "418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
mp.mp.dps = 90
TOL = mp.mpf("1e-62")

NUMERIC_FIELD_SCHEMA = {
    "flow_rows": ["c", "zeta", "delta", "t", "matrix", "determinant", "symplectic_defect", "energy_defect", "semigroup_defect"],
    "mode_rows": [
        "c", "zeta", "omega_plus", "omega_minus", "A_plus_re", "A_plus_im",
        "A_minus_re", "A_minus_im", "u0_re", "u0_im", "v0_re", "v0_im",
        "z0", "vz0", "I_plus", "I_minus", "I_z", "radial_energy",
        "axial_energy", "hamiltonian", "normal_form_energy",
    ],
    "strobe_rows": ["c", "zeta", "t", "fixed_dimension"],
    "period_rows": ["c", "zeta", "min_period"],
    "boundary_rows": ["c", "zeta", "delta", "bounded_dimension", "forward_bounded_dimension", "growth_rate"],
}


def case_values(name: str) -> tuple[mp.mpf, mp.mpf]:
    if name == "stable_3_2": return mp.mpf(3), mp.mpf(2)
    if name == "stable_minus3_2": return mp.mpf(-3), mp.mpf(2)
    if name == "stable_9_4": return mp.mpf(9), mp.mpf(4)
    if name == "stable_5_1": return mp.mpf(5), mp.mpf(1)
    if name == "critical_plus": return mp.mpf(2), mp.sqrt(2)
    if name == "critical_minus": return mp.mpf(-2), mp.sqrt(2)
    if name == "unstable_1_1": return mp.mpf(1), mp.mpf(1)
    if name == "zero_B": return mp.mpf(0), mp.mpf(1)
    if name == "unstable_minus1_2": return mp.mpf(-1), mp.mpf(2)
    if name == "zero_axial_plus": return mp.mpf(3), mp.mpf(0)
    if name == "zero_axial_minus": return mp.mpf(-2), mp.mpf(0)
    if name == "free": return mp.mpf(0), mp.mpf(0)
    raise KeyError(name)


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def rational(text: str) -> mp.mpf:
    q = Q(text)
    return mp.mpf(q.numerator)/q.denominator


def close(a, b) -> bool:
    a, b = mp.mpf(a), mp.mpf(b)
    return abs(a-b) <= TOL*max(1, abs(a), abs(b))


def J6() -> mp.matrix:
    J = mp.zeros(6)
    for i in range(3):
        J[i, i+3], J[i+3, i] = 1, -1
    return J


def K6(c: mp.mpf, zeta: mp.mpf) -> mp.matrix:
    K = mp.zeros(6)
    K[0, 0] = K[1, 1] = c*c/4-zeta*zeta/2
    K[2, 2] = zeta*zeta
    K[3, 3] = K[4, 4] = K[5, 5] = 1
    K[1, 3] = K[3, 1] = c/2
    K[0, 4] = K[4, 0] = -c/2
    return K


def generator(c: mp.mpf, zeta: mp.mpf) -> mp.matrix:
    return J6()*K6(c, zeta)


def matrix_from_row(row: dict) -> mp.matrix:
    vals = [mp.mpf(v) for v in row["matrix"]]
    assert len(vals) == 36
    return mp.matrix([[vals[6*i+j] for j in range(6)] for i in range(6)])


def maxabs(M: mp.matrix) -> mp.mpf:
    return max(abs(M[i, j]) for i in range(M.rows) for j in range(M.cols))


def fixed_dimension(c: mp.mpf, zeta: mp.mpf, t: mp.mpf) -> int:
    D = mp.expm(generator(c, zeta)*t)-mp.eye(6)
    _, singular, _ = mp.svd(D)
    rank = sum(abs(singular[i]) > mp.mpf("1e-55") for i in range(len(singular)))
    return 6-rank


def main() -> None:
    d = json.loads(P.read_text())
    n = 0

    def ok(value) -> None:
        nonlocal n
        assert value
        n += 1

    ok(d["schema"] == "hcs-c274-penning-symplectic-atlas-v1")
    ok(d["candidate_id"] == "HCS-C274")
    ok(d["evaluation_date"] == "2026-09-01")
    ok(d["source_commit"] == SOURCE)
    ok(d["fixed_epoch"] == 1788220800)
    ok(d["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    ok(d["evaluator"] == {"version": "0.2.0", "sha256": EVAL})
    ok(d["payload_sha256"] == payload_hash(d))
    ok(d["model_contract"]["state_order"] == "(x,y,z,p_x,p_y,p_z)")
    ok(d["model_contract"]["delta"] == "Delta=c^2-2*zeta^2")
    ok(d["flow_contract"]["dimension"] == 6)
    ok(d["mode_contract"]["normal_form"] == "H=omega_+ I_+-omega_- I_-+zeta I_z")
    assert d["orbit_contract"]["closed_orbit_gate"] == (
        "a nonstationary stable-chamber orbit is closed iff its active labeled modes in "
        "(omega_+,omega_-,zeta) are rationally commensurate"
    )
    assert d["orbit_contract"]["stable_strobe_fixed_dimension"] == (
        "with labeled (f1,f2,f3)=(omega_+,omega_-,zeta), including coincident values, "
        "dim Fix M(t)=2*#{j: f_j*t in 2*pi*Z}"
    )
    ok(d["regime_contract"]["sign_reversal"] == "R(x,y,z,p_x,p_y,p_z)=(x,-y,z,p_x,-p_y,p_z) conjugates c to -c")
    ok(d["proof_contract"]["status"] == "PROVABLE AS STATED")
    ok(d["route_a"] == {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
                         "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False})
    for value in d["scope_flags"].values():
        ok(value is False)
    ok([s["doi"] for s in d["sources"]] == ["10.1103/PhysRevA.25.2423", "10.1103/RevModPhys.58.233"])

    J = J6()
    for row in d["regression"]["flow_rows"]:
        c, zeta = case_values(row["case"])
        t = rational(row["t"])
        delta = c*c-2*zeta*zeta
        M = matrix_from_row(row)
        independent = mp.expm(generator(c, zeta)*t)
        ok(close(row["c"], c) and close(row["zeta"], zeta) and close(row["delta"], delta))
        for i in range(6):
            for j in range(6):
                ok(close(M[i, j], independent[i, j]))
        ok(close(row["determinant"], mp.det(M)))
        ok(close(row["determinant"], 1))
        sym = maxabs(M.T*J*M-J)
        energy = maxabs(M.T*K6(c, zeta)*M-K6(c, zeta))
        semi = maxabs(mp.expm(generator(c, zeta)*t/2)**2-M)
        ok(close(row["symplectic_defect"], sym))
        ok(close(row["energy_defect"], energy))
        ok(close(row["semigroup_defect"], semi))
        ok(sym < mp.mpf("1e-70") and energy < mp.mpf("1e-70") and semi < mp.mpf("1e-70"))

    for row in d["regression"]["mode_rows"]:
        c, zeta = case_values(row["case"])
        root = mp.sqrt(c*c-2*zeta*zeta)
        wp, wm = (abs(c)+root)/2, (abs(c)-root)/2
        sigma = mp.sign(c)
        ap = mp.mpc(rational(row["A_plus_re"]), rational(row["A_plus_im"]))
        am = mp.mpc(rational(row["A_minus_re"]), rational(row["A_minus_im"]))
        u0 = ap+am
        v0 = -1j*sigma*(wp*ap+wm*am)
        z0, vz0 = rational(row["z0"]), rational(row["vz0"])
        ip, im = root*abs(ap)**2/2, root*abs(am)**2/2
        iz = (vz0*vz0+zeta*zeta*z0*z0)/(2*zeta)
        er = (abs(v0)**2-zeta*zeta*abs(u0)**2/2)/2
        ez = (vz0*vz0+zeta*zeta*z0*z0)/2
        expected = {
            "c": c, "zeta": zeta, "omega_plus": wp, "omega_minus": wm,
            "u0_re": mp.re(u0), "u0_im": mp.im(u0), "v0_re": mp.re(v0), "v0_im": mp.im(v0),
            "I_plus": ip, "I_minus": im, "I_z": iz, "radial_energy": er,
            "axial_energy": ez, "hamiltonian": er+ez,
            "normal_form_energy": wp*ip-wm*im+zeta*iz,
        }
        for key, value in expected.items():
            ok(close(row[key], value))
        ok(close(row["hamiltonian"], row["normal_form_energy"]))
        ok(row["krein_signs"] == [1, -1, 1])
        ok(close(wp+wm, abs(c)) and close(wp*wm, zeta*zeta/2) and close(wp-wm, root))

    for row in d["regression"]["strobe_rows"]:
        c, zeta = case_values(row["case"])
        t = mp.mpf(row["t"])
        ok(close(row["c"], c) and close(row["zeta"], zeta))
        ok(fixed_dimension(c, zeta, t) == row["fixed_dimension"])

    period_expected = [
        ("stable_3_2", ["plus", "minus", "axial"], 2*mp.pi, True),
        ("stable_3_2", ["plus"], mp.pi, True),
        ("stable_3_2", ["plus", "axial"], mp.pi, True),
        ("stable_9_4", ["plus", "axial"], mp.pi/2, True),
        ("stable_9_4", ["plus"], mp.pi/4, True),
        ("stable_9_4", ["minus"], 2*mp.pi, True),
        ("stable_5_1", ["plus", "minus", "axial"], None, False),
    ]
    ok(len(period_expected) == len(d["regression"]["period_rows"]))
    for row, expected in zip(d["regression"]["period_rows"], period_expected):
        name, active, period, commensurate = expected
        c, zeta = case_values(name)
        ok(row["case"] == name and row["active_modes"] == active and row["commensurate"] is commensurate)
        ok(close(row["c"], c) and close(row["zeta"], zeta))
        if period is None:
            ok(row["min_period"] is None and row["min_period_label"] is None)
        else:
            ok(close(row["min_period"], period))

    boundary_expected = {
        "stable_3_2": (6, 6, 0), "critical_plus": (4, 4, 0), "critical_minus": (4, 4, 0),
        "unstable_1_1": (2, 4, mp.mpf(1)/2), "zero_B": (2, 4, mp.sqrt(2)/2),
        "unstable_minus1_2": (2, 4, mp.sqrt(7)/2), "zero_axial_plus": (5, 5, 0),
        "zero_axial_minus": (5, 5, 0), "free": (3, 3, 0),
    }
    ok(len(boundary_expected) == len(d["regression"]["boundary_rows"]))
    for row in d["regression"]["boundary_rows"]:
        c, zeta = case_values(row["case"])
        bounded, forward, growth = boundary_expected[row["case"]]
        ok(close(row["c"], c) and close(row["zeta"], zeta) and close(row["delta"], c*c-2*zeta*zeta))
        ok(row["bounded_dimension"] == bounded and row["forward_bounded_dimension"] == forward)
        ok(close(row["growth_rate"], growth))

    # Independent sign-reversal conjugacy at the generator level.
    R = mp.diag([1, -1, 1, 1, -1, 1])
    for c, zeta in ((mp.mpf(3), mp.mpf(2)), (mp.mpf(5), mp.mpf(1)), (mp.mpf(2), mp.sqrt(2))):
        ok(maxabs(R*generator(c, zeta)*R-generator(-c, zeta)) < mp.mpf("1e-75"))

    regression = d["regression"]
    ok(regression["numeric_field_schema"] == NUMERIC_FIELD_SCHEMA)
    cells = 0
    for row_name, fields in NUMERIC_FIELD_SCHEMA.items():
        for row in regression[row_name]:
            for field in fields:
                ok(field in row)
                cells += len(row[field]) if field == "matrix" else 1
    counts = regression["counts"]
    ok(counts == {"flow_rows": 48, "flow_matrix_cells": 1728, "mode_rows": 24,
                  "strobe_rows": 13, "period_rows": 7, "boundary_rows": 9, "numeric_cells": cells})
    print(f"C274 independent checker: PASS ({n} assertions; 6x6 flow, symplecticity, modes, regimes, periods, strobes)")


if __name__ == "__main__":
    main()
