#!/usr/bin/env python3
"""Deterministic exact and high-precision receipts for HCS-C318."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c318_ssh_evidence.json"
SOURCE = "1938bae19e5a92f9ce2411aafdc68323bd641bd0"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
mp.mp.dps = 90

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


def q(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def mpf(x: Fraction) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def dec(x: mp.mpf | mp.mpc) -> str:
    x = mp.re(x) if abs(mp.im(x)) < mp.mpf("1e-78") else x
    if not isinstance(x, mp.mpc) and abs(x) < mp.mpf("1e-78"):
        return "0.0"
    return mp.nstr(x, 72, strip_zeros=False)


def add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def scale(a: list[Fraction], c: Fraction) -> list[Fraction]:
    return [c * value for value in a]


def mul_y_minus(a: list[Fraction], c: Fraction) -> list[Fraction]:
    return add(scale(a, -c), [Fraction(0)] + a)


def q_polynomial(m: int, v: Fraction, w: Fraction) -> list[Fraction]:
    """det(y I - T T*) in ascending powers of y."""
    p0 = [Fraction(1)]
    p1 = [-v * v, Fraction(1)]
    if m == 1:
        return p1
    for _ in range(2, m + 1):
        p0, p1 = p1, add(mul_y_minus(p1, v * v + w * w), scale(p0, -v * v * w * w))
    return p1


def edge_ratio(m: int, z: Fraction) -> Fraction:
    return (Fraction(1, 1) / z) * (1 - z ** (2 * m + 2)) / (1 - z ** (2 * m))


def sinh_from_z(n: int, z: Fraction) -> Fraction:
    return (z ** (-n) - z**n) / 2


def obc_rows() -> list[dict]:
    rows = []
    for m in range(2, 13):
        cases = [
            ("trivial", Fraction(3), Fraction(2), "all_trigonometric"),
            ("bulk_critical", Fraction(1), Fraction(1), "all_trigonometric"),
            ("bulk_topological_finite_subthreshold", Fraction(2 * m), Fraction(2 * m + 1), "all_trigonometric"),
            ("finite_edge_threshold", Fraction(m), Fraction(m + 1), "threshold_x_minus_one"),
            ("hyperbolic_edge", Fraction(1), Fraction(2), "one_hyperbolic_pair"),
        ]
        for label, v, w, zone in cases:
            rows.append(
                {
                    "M": m,
                    "label": label,
                    "v": q(v),
                    "w": q(w),
                    "ratio_w_over_v": q(w / v),
                    "finite_edge_threshold": q(Fraction(m + 1, m)),
                    "root_zone": zone,
                    "q_coefficients_y_ascending": [q(x) for x in q_polynomial(m, v, w)],
                    "det_T": q(v**m),
                    "zero_eigenvalue_multiplicity": 0,
                }
            )
    return rows


def edge_rows() -> tuple[list[dict], list[dict]]:
    exact = []
    threshold = []
    for m in range(2, 13):
        for z in (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)):
            v = Fraction(1)
            w = edge_ratio(m, z)
            x = -(z + 1 / z) / 2
            energy = v * z ** (m - 1) * (1 - z * z) / (1 - z ** (2 * m))
            avec = [(-1) ** (j - 1) * sinh_from_z(m + 1 - j, z) for j in range(1, m + 1)]
            bvec = [(-1) ** (j - 1) * sinh_from_z(j, z) for j in range(1, m + 1)]
            norm_sq = 2 * sum(value * value for value in bvec)
            exact.append(
                {
                    "M": m,
                    "z_exp_minus_kappa": q(z),
                    "v": q(v),
                    "w": q(w),
                    "ratio_w_over_v": q(w / v),
                    "threshold": q(Fraction(m + 1, m)),
                    "x_minus_cosh_kappa": q(x),
                    "edge_energy": q(energy),
                    "edge_energy_squared": q(energy * energy),
                    "a_vector": [q(value) for value in avec],
                    "b_vector": [q(value) for value in bvec],
                    "joint_norm_squared": q(norm_sq),
                    "strict_decay_bound": q(z),
                }
            )
        v = Fraction(m)
        w = Fraction(m + 1)
        avec = [Fraction((-1) ** (j - 1) * (m + 1 - j)) for j in range(1, m + 1)]
        bvec = [Fraction((-1) ** (j - 1) * j) for j in range(1, m + 1)]
        threshold.append(
            {
                "M": m,
                "v": q(v),
                "w": q(w),
                "ratio_w_over_v": q(w / v),
                "x": "-1",
                "band_edge_energy": "1",
                "a_linear_taper": [q(value) for value in avec],
                "b_linear_taper": [q(value) for value in bvec],
            }
        )
    return exact, threshold


def periodic_rows() -> list[dict]:
    rows = []
    cases = [
        ("trivial", Fraction(2), Fraction(1)),
        ("topological", Fraction(1), Fraction(2)),
        ("critical", Fraction(1), Fraction(1)),
        ("v_zero", Fraction(0), Fraction(2)),
        ("w_zero", Fraction(2), Fraction(0)),
    ]
    for m in range(2, 16):
        for label, v, w in cases:
            if w > v:
                winding_defined, winding = True, 1
            elif v > w:
                winding_defined, winding = True, 0
            else:
                winding_defined, winding = False, None
            cells = []
            for n in range(m):
                k = 2 * mp.pi * n / m
                re = mpf(v) + mpf(w) * mp.cos(k)
                im = mpf(w) * mp.sin(k)
                cells.append(
                    {
                        "mode": n,
                        "k_over_2pi": q(Fraction(n, m)),
                        "q_real": dec(re),
                        "q_imag": dec(im),
                        "energy_squared": dec(re * re + im * im),
                    }
                )
            continuum_gap = abs(v - w)
            if m % 2 == 0:
                finite_sampled_gap = mpf(continuum_gap)
            else:
                finite_sampled_gap = mp.sqrt(
                    mpf(v) ** 2
                    + mpf(w) ** 2
                    - 2 * mpf(v) * mpf(w) * mp.cos(mp.pi / m)
                )
            rows.append(
                {
                    "M": m,
                    "label": label,
                    "v": q(v),
                    "w": q(w),
                    "winding_defined": winding_defined,
                    "winding_value": winding,
                    "continuum_bulk_gap_to_zero": q(continuum_gap),
                    "continuum_central_band_gap": q(2 * continuum_gap),
                    "finite_sampled_gap_to_zero": dec(finite_sampled_gap),
                    "finite_sampled_central_band_gap": dec(2 * finite_sampled_gap),
                    "finite_zero_multiplicity": 2 if v == w and v > 0 and m % 2 == 0 else 0,
                    "momentum_cells": cells,
                }
            )
    return rows


def boundary_rows() -> list[dict]:
    rows = []
    for m in range(2, 13):
        rows.extend(
            [
                {
                    "M": m,
                    "face": "w_zero",
                    "v": "2",
                    "w": "0",
                    "kernel_dimension": 0,
                    "positive_energy": "2",
                    "positive_multiplicity": m,
                    "negative_multiplicity": m,
                    "dimer_count": m,
                },
                {
                    "M": m,
                    "face": "v_zero",
                    "v": "0",
                    "w": "3",
                    "kernel_dimension": 2,
                    "positive_energy": "3",
                    "positive_multiplicity": m - 1,
                    "negative_multiplicity": m - 1,
                    "dimer_count": m - 1,
                },
                {
                    "M": m,
                    "face": "both_zero",
                    "v": "0",
                    "w": "0",
                    "kernel_dimension": 2 * m,
                    "positive_energy": "0",
                    "positive_multiplicity": 0,
                    "negative_multiplicity": 0,
                    "dimer_count": 0,
                },
            ]
        )
    return rows


def ssh_matrix(m: int, v: Fraction, w: Fraction) -> mp.matrix:
    h = mp.matrix(2 * m)
    for j in range(m):
        h[j, m + j] = h[m + j, j] = mpf(v)
        if j + 1 < m:
            h[j + 1, m + j] = h[m + j, j + 1] = mpf(w)
    return h


def max_abs(a: mp.matrix) -> mp.mpf:
    return max((abs(a[i, j]) for i in range(a.rows) for j in range(a.cols)), default=mp.mpf(0))


def propagator_rows() -> list[dict]:
    rows = []
    cases = [
        ("trivial", Fraction(2), Fraction(1)),
        ("topological", Fraction(1), Fraction(2)),
        ("critical", Fraction(1), Fraction(1)),
        ("v_zero", Fraction(0), Fraction(2)),
        ("w_zero", Fraction(2), Fraction(0)),
        ("both_zero", Fraction(0), Fraction(0)),
    ]
    for m in range(2, 7):
        t = Fraction(m % 3 + 1, 5)
        for label, v, w in cases:
            h = ssh_matrix(m, v, w)
            u = mp.expm(-mp.j * mpf(t) * h)
            ident = mp.eye(2 * m)
            gram = u.transpose_conj() * u - ident
            gamma = mp.diag([1] * m + [-1] * m)
            chiral = gamma * u * gamma - u.transpose_conj()
            probes = sorted({(0, 0), (0, m), (0, 2 * m - 1), (m - 1, 2 * m - 1), (m, m), (2 * m - 1, 2 * m - 1)})
            rows.append(
                {
                    "M": m,
                    "label": label,
                    "v": q(v),
                    "w": q(w),
                    "time": q(t),
                    "selected_entries": [
                        {"row": i, "column": j, "real": dec(mp.re(u[i, j])), "imag": dec(mp.im(u[i, j]))}
                        for i, j in probes
                    ],
                    "trace_real": dec(mp.re(sum(u[i, i] for i in range(2 * m)))),
                    "trace_imag": dec(mp.im(sum(u[i, i] for i in range(2 * m)))),
                    "unitarity_residual": dec(max_abs(gram)),
                    "chiral_time_reversal_residual": dec(max_abs(chiral)),
                }
            )
    return rows


def quench_rows() -> list[dict]:
    cases = [
        ("grid_hit_cross_phase", 3, 1, 1, 5),
        ("generic_cross_phase", 2, 1, 1, 2),
        ("reverse_cross_phase", 1, 4, 3, 1),
        ("same_trivial", 3, 1, 2, 1),
        ("same_topological", 1, 3, 1, 2),
        ("critical_endpoint_outside_contract", 2, 1, 1, 1),
    ]
    rows = []
    for label, vi0, wi0, vf0, wf0 in cases:
        vi, wi, vf, wf = map(Fraction, (vi0, wi0, vf0, wf0))
        endpoints_gapped = vi != wi and vf != wf
        cross = endpoints_gapped and (vi - wi) * (vf - wf) < 0
        row = {
            "label": label,
            "v_initial": q(vi),
            "w_initial": q(wi),
            "v_final": q(vf),
            "w_final": q(wf),
            "endpoints_gapped": endpoints_gapped,
            "cross_phase": cross,
            "has_continuum_mode_zero": cross,
        }
        if cross:
            c = -(vi * vf + wi * wf) / (vi * wf + wi * vf)
            ef2 = vf * vf + wf * wf + 2 * vf * wf * c
            tpi = 1 / (2 * mp.sqrt(mpf(ef2)))
            hits = []
            for m in range(2, 13):
                hit_modes = [n for n in range(m) if abs(mp.cos(2 * mp.pi * n / m) - mpf(c)) < mp.mpf("1e-70")]
                if hit_modes:
                    hits.append({"M": m, "modes": hit_modes})
            row.update(
                {
                    "cos_k_star": q(c),
                    "critical_energy_squared": q(ef2),
                    "first_zero_time_over_pi": dec(tpi),
                    "finite_grid_hits_M_2_to_12": hits,
                }
            )
        else:
            row.update(
                {
                    "cos_k_star": None,
                    "critical_energy_squared": None,
                    "first_zero_time_over_pi": None,
                    "finite_grid_hits_M_2_to_12": [],
                }
            )
        rows.append(row)
    return rows


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(x) for x in value.values())
    if type(value) is list:
        return sum(leaves(x) for x in value)
    return 1


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C318 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()

    edge, threshold = edge_rows()
    obc = obc_rows()
    periodic = periodic_rows()
    boundaries = boundary_rows()
    propagators = propagator_rows()
    quenches = quench_rows()
    data = {
        "schema": "hcs-c318-ssh-finite-bulk-edge-v1",
        "candidate_id": "HCS-C318",
        "obstruction_id": "HEN-O302",
        "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": {
            "owner": "balanced finite Su--Schrieffer--Heeger single-particle chain",
            "open_size": "M>=2 cells and 2M sites; M=1 is an explicit convention face",
            "hoppings": "real v,w>=0 with v intracell and w intercell",
            "open_block": "H=[[0,T],[T*,0]], T=vI+wS_-",
            "periodic_symbol": "h(k)=[[0,conj(q(k))],[q(k),0]], q(k)=v+w exp(ik)",
            "clock": "physical unitary time i psi_dot=H psi",
        },
        "theorem_contract": {
            "characteristic": "det(EI-H)=(vw)^M[U_M(x)+(w/v)U_(M-1)(x)], x=(E^2-v^2-w^2)/(2vw), for v,w>0",
            "finite_edge": "one hyperbolic pair exists iff w/v>(M+1)/M",
            "bulk": "winding of q(k)=v+w exp(ik) is one for w>v and zero for v>w; continuum and finite sampled gaps are distinguished",
            "threshold_separation": "bulk critical ratio is one; the strict finite hyperbolic threshold is (M+1)/M",
            "periodic_parity": "at v=w>0 a finite ring has a two-dimensional zero sector iff M is even",
            "faces": "w=0 gives M dimers; v=0 gives M-1 dimers plus two exact edge zeros; both zero gives the zero matrix",
            "propagator": "the entire block sinc formula is valid on every singular face",
            "quench": "gapped opposite-phase Bloch quenches and only those have continuum mode Loschmidt zeros; finite rings require momentum-grid incidence",
        },
        "obc_polynomial_rows": obc,
        "exact_edge_witnesses": edge,
        "finite_threshold_rows": threshold,
        "periodic_rows": periodic,
        "boundary_rows": boundaries,
        "propagator_rows": propagators,
        "quench_rows": quenches,
        "one_cell_convention": {
            "M": 1,
            "v": "2",
            "w": "5",
            "open_eigenvalues": ["-2", "2"],
            "periodic_wrap_eigenvalues": ["-7", "7"],
            "statement": "the open intercell bond is absent; the periodic wrap bond merges with the intracell bond",
        },
        "collision_boundary": {
            "C308": "C308 is a one-site non-Hermitian nonreciprocal skin chain and explicitly excludes winding and topological edge modes; C318 is Hermitian, bipartite, chiral, and bulk--edge based.",
            "C267": "C267 is an infinite uniform-field Wannier--Stark ladder with Bessel propagation, not a dimerized finite topological chain.",
            "C297": "C297 is a two-site non-Hermitian PT dimer with an exceptional point, not a many-cell Hermitian bulk--edge system.",
            "C138": "C138 uses flux winding in a metric quantum graph primitive-walk determinant, not Bloch-band winding or SSH edge hybridization.",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "nonclaims": [
            "No literature-priority claim is made for the SSH model, winding, bulk--edge correspondence, or finite edge splitting.",
            "The finite characteristic polynomial is not an Euler factor and the source spectrum is not a target zero set.",
            "No disorder, interaction, self-consistent phonon, many-body DQPT, automorphy, root number, or Hilbert--Polya claim is made.",
        ],
        "references": [
            {"identifier": "10.1103/PhysRevLett.42.1698", "role": "SSH model and polyacetylene provenance"},
            {"identifier": "10.1103/PhysRevB.22.2099", "role": "soliton excitation and localized gap-state lineage"},
            {"identifier": "10.1007/978-3-319-25607-8_1", "role": "chiral, winding, and bulk--boundary exposition"},
        ],
    }
    data["enumeration"] = {
        "obc_polynomial_rows": len(obc),
        "exact_edge_witnesses": len(edge),
        "finite_threshold_rows": len(threshold),
        "periodic_rows": len(periodic),
        "periodic_momentum_cells": sum(len(row["momentum_cells"]) for row in periodic),
        "boundary_rows": len(boundaries),
        "propagator_rows": len(propagators),
        "propagator_selected_entries": sum(len(row["selected_entries"]) for row in propagators),
        "quench_rows": len(quenches),
    }
    # Install both scalar leaves before counting so this receipt audits the
    # final object rather than the pre-hash staging object.
    data["enumeration"]["audited_leaf_count"] = 0
    data["payload_sha256"] = ""
    data["enumeration"]["audited_leaf_count"] = leaves(data)
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C318_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")


if __name__ == "__main__":
    main()
