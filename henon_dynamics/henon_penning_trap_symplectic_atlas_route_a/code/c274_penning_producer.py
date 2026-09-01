#!/usr/bin/env python3
"""Produce the deterministic HCS-C274 ideal-Penning-trap certificate."""
from __future__ import annotations

import hashlib
import json
import os
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("C274_EVIDENCE_OUT", ROOT / "results/c274_penning_evidence.json"))
SOURCE = "418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788220800
mp.mp.dps = 90


def values(name: str) -> tuple[mp.mpf, mp.mpf]:
    table = {
        "stable_3_2": (mp.mpf(3), mp.mpf(2)),
        "stable_minus3_2": (mp.mpf(-3), mp.mpf(2)),
        "stable_9_4": (mp.mpf(9), mp.mpf(4)),
        "stable_5_1": (mp.mpf(5), mp.mpf(1)),
        "critical_plus": (mp.mpf(2), mp.sqrt(2)),
        "critical_minus": (mp.mpf(-2), mp.sqrt(2)),
        "unstable_1_1": (mp.mpf(1), mp.mpf(1)),
        "zero_B": (mp.mpf(0), mp.mpf(1)),
        "unstable_minus1_2": (mp.mpf(-1), mp.mpf(2)),
        "zero_axial_plus": (mp.mpf(3), mp.mpf(0)),
        "zero_axial_minus": (mp.mpf(-2), mp.mpf(0)),
        "free": (mp.mpf(0), mp.mpf(0)),
    }
    return table[name]


FLOW_CASES = tuple(
    "stable_3_2 stable_minus3_2 stable_9_4 stable_5_1 critical_plus critical_minus "
    "unstable_1_1 zero_B unstable_minus1_2 zero_axial_plus zero_axial_minus free".split()
)
FLOW_TIMES = (Q(1, 7), Q(2, 5), Q(1), Q(3, 2))
MODE_CASES = ("stable_3_2", "stable_minus3_2", "stable_9_4", "stable_5_1")
AMPLITUDES = (
    (Q(1), Q(0), Q(0), Q(0), Q(0), Q(0)),
    (Q(0), Q(0), Q(1), Q(0), Q(0), Q(0)),
    (Q(1), Q(1, 2), Q(-1, 3), Q(2, 3), Q(1, 2), Q(-1, 4)),
    (Q(-2, 3), Q(1, 5), Q(3, 4), Q(-1, 2), Q(1), Q(2, 5)),
    (Q(1, 4), Q(-3, 5), Q(-2, 5), Q(-1, 3), Q(-3, 4), Q(5, 6)),
    (Q(2), Q(-1), Q(1, 2), Q(3, 2), Q(2, 3), Q(-4, 5)),
)

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


def qstr(x: Q) -> str:
    return f"{x.numerator}/{x.denominator}"


def mq(x: Q) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def ds(x) -> str:
    x = mp.mpf(x)
    if abs(x) < mp.mpf("1e-82"):
        x = mp.mpf(0)
    return mp.nstr(x, 76, strip_zeros=False)


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def regime(c: mp.mpf, zeta: mp.mpf) -> str:
    delta = c*c - 2*zeta*zeta
    if zeta == 0:
        return "free" if c == 0 else "zero_axial_landau"
    if delta > 0:
        return "stable"
    if delta == 0:
        return "critical_jordan"
    return "radially_unstable"


def cs(delta: mp.mpf, t: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    if delta > 0:
        a = mp.sqrt(delta) / 2
        return mp.cos(a*t), mp.sin(a*t)/a
    if delta < 0:
        a = mp.sqrt(-delta) / 2
        return mp.cosh(a*t), mp.sinh(a*t)/a
    return mp.mpf(1), t


def complex_matrix(a: mp.mpc) -> mp.matrix:
    return mp.matrix([[mp.re(a), -mp.im(a)], [mp.im(a), mp.re(a)]])


def velocity_flow(c: mp.mpf, zeta: mp.mpf, t: mp.mpf) -> mp.matrix:
    delta = c*c - 2*zeta*zeta
    C, S = cs(delta, t)
    phase = mp.e**(-1j*c*t/2)
    a = phase*(C + 1j*c*S/2)
    b = phase*S
    d = phase*(zeta*zeta*S/2)
    e = phase*(C - 1j*c*S/2)
    V = mp.zeros(6)
    aa, bb, dd, ee = map(complex_matrix, (a, b, d, e))
    for i in range(2):
        for j in range(2):
            V[i, j] = aa[i, j]
            V[i, j+3] = bb[i, j]
            V[i+3, j] = dd[i, j]
            V[i+3, j+3] = ee[i, j]
    if zeta:
        cz, sz = mp.cos(zeta*t), mp.sin(zeta*t)/zeta
        V[2, 2], V[2, 5] = cz, sz
        V[5, 2], V[5, 5] = -zeta*mp.sin(zeta*t), cz
    else:
        V[2, 2], V[2, 5], V[5, 5] = 1, t, 1
    return V


def canonical_to_velocity(c: mp.mpf) -> mp.matrix:
    T = mp.eye(6)
    T[3, 1] = c/2
    T[4, 0] = -c/2
    return T


def canonical_flow(c: mp.mpf, zeta: mp.mpf, t: mp.mpf) -> mp.matrix:
    T = canonical_to_velocity(c)
    return T**-1 * velocity_flow(c, zeta, t) * T


def hessian(c: mp.mpf, zeta: mp.mpf) -> mp.matrix:
    K = mp.zeros(6)
    radial = c*c/4 - zeta*zeta/2
    K[0, 0] = K[1, 1] = radial
    K[2, 2] = zeta*zeta
    K[3, 3] = K[4, 4] = K[5, 5] = 1
    K[1, 3] = K[3, 1] = c/2
    K[0, 4] = K[4, 0] = -c/2
    return K


def symplectic_j() -> mp.matrix:
    J = mp.zeros(6)
    for i in range(3):
        J[i, i+3] = 1
        J[i+3, i] = -1
    return J


def maxabs(M: mp.matrix) -> mp.mpf:
    return max(abs(M[i, j]) for i in range(M.rows) for j in range(M.cols))


def flat(M: mp.matrix) -> list[str]:
    return [ds(M[i, j]) for i in range(M.rows) for j in range(M.cols)]


def flow_rows() -> list[dict]:
    rows = []
    J = symplectic_j()
    for name in FLOW_CASES:
        c, zeta = values(name)
        delta = c*c - 2*zeta*zeta
        K = hessian(c, zeta)
        for tq in FLOW_TIMES:
            t = mq(tq)
            M = canonical_flow(c, zeta, t)
            half = canonical_flow(c, zeta, t/2)
            rows.append({
                "case": name, "regime": regime(c, zeta), "c": ds(c), "zeta": ds(zeta),
                "delta": ds(delta), "t": qstr(tq), "matrix": flat(M),
                "determinant": ds(mp.det(M)),
                "symplectic_defect": ds(maxabs(M.T*J*M-J)),
                "energy_defect": ds(maxabs(M.T*K*M-K)),
                "semigroup_defect": ds(maxabs(half*half-M)),
            })
    return rows


def mode_rows() -> list[dict]:
    rows = []
    for name in MODE_CASES:
        c, zeta = values(name)
        sigma = mp.sign(c)
        root = mp.sqrt(c*c-2*zeta*zeta)
        wp, wm = (abs(c)+root)/2, (abs(c)-root)/2
        for ap_re, ap_im, am_re, am_im, zq, vzq in AMPLITUDES:
            ap = mp.mpc(mq(ap_re), mq(ap_im))
            am = mp.mpc(mq(am_re), mq(am_im))
            z0, vz0 = mq(zq), mq(vzq)
            u0 = ap + am
            v0 = -1j*sigma*(wp*ap+wm*am)
            ip = root*abs(ap)**2/2
            im = root*abs(am)**2/2
            iz = (vz0*vz0+zeta*zeta*z0*z0)/(2*zeta)
            er = (abs(v0)**2-zeta*zeta*abs(u0)**2/2)/2
            ez = (vz0*vz0+zeta*zeta*z0*z0)/2
            normal = wp*ip-wm*im+zeta*iz
            rows.append({
                "case": name, "c": ds(c), "zeta": ds(zeta), "omega_plus": ds(wp),
                "omega_minus": ds(wm), "A_plus_re": qstr(ap_re), "A_plus_im": qstr(ap_im),
                "A_minus_re": qstr(am_re), "A_minus_im": qstr(am_im),
                "u0_re": ds(mp.re(u0)), "u0_im": ds(mp.im(u0)),
                "v0_re": ds(mp.re(v0)), "v0_im": ds(mp.im(v0)), "z0": qstr(zq),
                "vz0": qstr(vzq), "I_plus": ds(ip), "I_minus": ds(im), "I_z": ds(iz),
                "radial_energy": ds(er), "axial_energy": ds(ez),
                "hamiltonian": ds(er+ez), "normal_form_energy": ds(normal),
                "krein_signs": [1, -1, 1],
            })
    return rows


def strobe_rows() -> list[dict]:
    specs = [
        ("stable_3_2", Q(1), 4, "pi"), ("stable_3_2", Q(2), 6, "pi"),
        ("stable_3_2", Q(1, 2), 0, "pi"),
        ("stable_9_4", Q(1, 4), 2, "pi"), ("stable_9_4", Q(1, 2), 4, "pi"),
        ("stable_9_4", Q(2), 6, "pi"),
        ("critical_plus", Q(2), 2, "pi"), ("critical_plus", Q(2), 2, "pi_over_sqrt2"),
        ("unstable_1_1", Q(2), 2, "pi"), ("zero_B", Q(2), 2, "pi"),
        ("zero_axial_plus", Q(2, 3), 5, "pi"), ("zero_axial_plus", Q(1), 3, "unit"),
        ("free", Q(1), 3, "unit"),
    ]
    rows = []
    for name, multiplier, dimension, scale in specs:
        c, zeta = values(name)
        if scale == "pi":
            t = mq(multiplier)*mp.pi
            label = f"{qstr(multiplier)}*pi"
        elif scale == "pi_over_sqrt2":
            t = mq(multiplier)*mp.pi/mp.sqrt(2)
            label = f"{qstr(multiplier)}*pi/sqrt(2)"
        else:
            t = mq(multiplier)
            label = qstr(multiplier)
        rows.append({"case": name, "c": ds(c), "zeta": ds(zeta), "t": ds(t),
                     "t_label": label, "fixed_dimension": dimension})
    return rows


def period_rows() -> list[dict]:
    specs = [
        ("stable_3_2", ["plus", "minus", "axial"], Q(2), True),
        ("stable_3_2", ["plus"], Q(1), True),
        ("stable_3_2", ["plus", "axial"], Q(1), True),
        ("stable_9_4", ["plus", "axial"], Q(1, 2), True),
        ("stable_9_4", ["plus"], Q(1, 4), True),
        ("stable_9_4", ["minus"], Q(2), True),
        ("stable_5_1", ["plus", "minus", "axial"], None, False),
    ]
    rows = []
    for name, active, p, commensurate in specs:
        c, zeta = values(name)
        rows.append({"case": name, "c": ds(c), "zeta": ds(zeta), "active_modes": active,
                     "commensurate": commensurate,
                     "min_period": (ds(mq(p)*mp.pi) if p is not None else None),
                     "min_period_label": (f"{qstr(p)}*pi" if p is not None else None)})
    return rows


def boundary_rows() -> list[dict]:
    specs = [
        ("stable_3_2", 6, 6, 0), ("critical_plus", 4, 4, 0),
        ("critical_minus", 4, 4, 0), ("unstable_1_1", 2, 4, mp.sqrt(1)/2),
        ("zero_B", 2, 4, mp.sqrt(2)/2), ("unstable_minus1_2", 2, 4, mp.sqrt(7)/2),
        ("zero_axial_plus", 5, 5, 0), ("zero_axial_minus", 5, 5, 0),
        ("free", 3, 3, 0),
    ]
    rows = []
    for name, bounded, forward, growth in specs:
        c, zeta = values(name)
        rows.append({"case": name, "regime": regime(c, zeta), "c": ds(c), "zeta": ds(zeta),
                     "delta": ds(c*c-2*zeta*zeta), "bounded_dimension": bounded,
                     "forward_bounded_dimension": forward, "growth_rate": ds(growth)})
    return rows


def numeric_cell_count(regression: dict) -> int:
    total = 0
    for row_name, fields in NUMERIC_FIELD_SCHEMA.items():
        for row in regression[row_name]:
            for field in fields:
                if field in row:
                    total += len(row[field]) if field == "matrix" else 1
    return total


def main() -> None:
    regression = {
        "numeric_field_schema": NUMERIC_FIELD_SCHEMA,
        "flow_rows": flow_rows(), "mode_rows": mode_rows(), "strobe_rows": strobe_rows(),
        "period_rows": period_rows(), "boundary_rows": boundary_rows(),
    }
    regression["counts"] = {
        "flow_rows": len(regression["flow_rows"]), "flow_matrix_cells": 36*len(regression["flow_rows"]),
        "mode_rows": len(regression["mode_rows"]), "strobe_rows": len(regression["strobe_rows"]),
        "period_rows": len(regression["period_rows"]), "boundary_rows": len(regression["boundary_rows"]),
        "numeric_cells": numeric_cell_count(regression),
    }
    data = {
        "schema": "hcs-c274-penning-symplectic-atlas-v1", "candidate_id": "HCS-C274",
        "evaluation_date": "2026-09-01", "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "The ideal Penning trap has an exact six-dimensional symplectic flow, a sharp magnetic-confinement/Jordan/instability atlas, signed mode actions, and a complete resonance and strobe classification.",
        "evaluator": {"version": "0.2.0", "sha256": EVAL},
        "model_contract": {
            "state_order": "(x,y,z,p_x,p_y,p_z)",
            "hamiltonian": "H=((p_x+c*y/2)^2+(p_y-c*x/2)^2+p_z^2)/2+zeta^2*(z^2-(x^2+y^2)/2)/2",
            "physical_velocities": "v_x=p_x+c*y/2; v_y=p_y-c*x/2; v_z=p_z",
            "equations": "u''+i*c*u'-zeta^2*u/2=0 for u=x+i*y; z''+zeta^2*z=0",
            "parameters": "c is signed cyclotron frequency; zeta>=0 is axial frequency",
            "delta": "Delta=c^2-2*zeta^2",
        },
        "flow_contract": {
            "radial_reduction": "u=e^{-i*c*t/2}w gives w''+Delta*w/4=0",
            "entire_functions": "C=cos(sqrt(Delta)t/2), S=sin(sqrt(Delta)t/2)/(sqrt(Delta)/2), continued by C=1,S=t at Delta=0 and by cosh/sinh for Delta<0",
            "radial_flow": "u(t)=e^{-ict/2}[(C+i*c*S/2)u0+S*v0]; v(t)=e^{-ict/2}[zeta^2*S*u0/2+(C-i*c*S/2)v0]",
            "axial_flow": "z(t)=cos(zeta*t)z0+sin(zeta*t)vz0/zeta with the zeta=0 free limit",
            "canonical_flow": "M_c(t)=T_c^{-1} V_c(t) T_c, T_c(q,p)=(q,v), and M_c(t)^T J M_c(t)=J",
            "dimension": 6,
        },
        "regime_contract": {
            "stable": "zeta>0 and Delta>0: every orbit is bounded",
            "critical": "zeta>0 and Delta=0: generic radial amplitude grows linearly; bounded iff v0=-i*c*u0/2",
            "unstable": "zeta>0 and Delta<0: generic radial growth rate sqrt(-Delta)/2; the forward-stable radial plane has v0=-(sqrt(-Delta)/2+i*c/2)u0",
            "zero_axial": "zeta=0,c!=0: Landau cyclotron plus a fixed guiding centre and free axial drift",
            "free": "zeta=c=0: free three-dimensional motion",
            "sign_reversal": "R(x,y,z,p_x,p_y,p_z)=(x,-y,z,p_x,-p_y,p_z) conjugates c to -c",
        },
        "mode_contract": {
            "domain": "zeta>0 and Delta>0", "frequencies": "omega_+ = (abs(c)+sqrt(Delta))/2; omega_-=(abs(c)-sqrt(Delta))/2",
            "amplitudes": "u=A_+ exp(-i*sgn(c)*omega_+ t)+A_- exp(-i*sgn(c)*omega_- t)",
            "actions": "I_+=sqrt(Delta)|A_+|^2/2; I_-=sqrt(Delta)|A_-|^2/2; I_z=(v_z^2+zeta^2 z^2)/(2 zeta)",
            "normal_form": "H=omega_+ I_+-omega_- I_-+zeta I_z",
            "krein_signs": ["positive modified-cyclotron", "negative magnetron", "positive axial"],
        },
        "orbit_contract": {
            "closed_orbit_gate": "a nonstationary stable-chamber orbit is closed iff its active labeled modes in (omega_+,omega_-,zeta) are rationally commensurate",
            "minimal_period": "if active frequencies are integer multiples n_j*g with gcd(n_j)=1, T_min=2*pi/g",
            "stable_strobe_fixed_dimension": "with labeled (f1,f2,f3)=(omega_+,omega_-,zeta), including coincident values, dim Fix M(t)=2*#{j: f_j*t in 2*pi*Z}",
            "critical_strobe": "the radial fixed dimension is two only when c*t/2 is in 2*pi*Z; the Jordan direction never fixes",
            "zero_axial_strobe": "for c!=0 the fixed dimension is three, plus two when abs(c)*t is in 2*pi*Z",
        },
        "proof_contract": {
            "status": "PROVABLE AS STATED",
            "dependencies": ["constant Hamiltonian block flow", "real symplectic linear algebra", "elementary commensurability"],
            "scope": "ideal axially symmetric trap only; no imperfections, damping, many-body effects, or experimental accuracy claim",
            "quantization_boundary": "the canonical ideal-trap quantization is natural but its signed magnetron ladder is not promoted to a target spectrum or determinant",
        },
        "analytic_proof_obligations": [
            "derive the Hamilton equations in the frozen symmetric gauge", "prove the rotating-frame entire flow across all signs of Delta",
            "prove canonical symplecticity and energy conservation", "derive the stable signed action normal form",
            "classify bounded subspaces on stable, Jordan, unstable, zero-axial, and free faces",
            "prove active-mode commensurability, minimal periods, and strobe fixed dimensions", "prove signed-field conjugacy",
        ],
        "regression": regression,
        "route_a": {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": {"arithmetic_local_data": False, "euler_factors": False, "root_numbers": False,
                        "automorphy": False, "target_divisor": False, "target_counting_law": False,
                        "hilbert_polya_operator": False, "route_b": False},
        "nonclaims": [
            "No literature-priority or experimental-performance claim is made.",
            "Clean resonant tori are not replaced by isolated primitive orbits.",
            "The natural Penning Hamiltonian is not a Hilbert--Polya operator and supplies no target divisor.",
        ],
        "sources": [
            {"authors": "Lowell S. Brown and Gerald Gabrielse", "title": "Precision spectroscopy of a charged particle in an imperfect Penning trap", "journal": "Physical Review A 25 (1982), 2423(R)", "doi": "10.1103/PhysRevA.25.2423", "role": "primary Penning eigenfrequency and invariance lineage"},
            {"authors": "Lowell S. Brown and Gerald Gabrielse", "title": "Geonium theory: Physics of a single electron or ion in a Penning trap", "journal": "Reviews of Modern Physics 58 (1986), 233--311", "doi": "10.1103/RevModPhys.58.233", "role": "authoritative ideal-trap convention and mode terminology"},
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    c = regression["counts"]
    print(f"C274_PRODUCER_PASS flow={c['flow_rows']} mode={c['mode_rows']} strobe={c['strobe_rows']} period={c['period_rows']} boundary={c['boundary_rows']} numeric_cells={c['numeric_cells']} payload={data['payload_sha256']}")


if __name__ == "__main__":
    main()
