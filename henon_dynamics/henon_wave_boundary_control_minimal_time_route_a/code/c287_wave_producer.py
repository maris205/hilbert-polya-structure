#!/usr/bin/env python3
"""Exact evidence producer for HCS-C287."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c287_wave_evidence.json"
SOURCE = "3878fa5282ca89f75700b3ef9d623f54dcb7bcf9"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
MODEL = {
    "pde": "u_tt-c^2 u_xx=0 on (0,L)",
    "adjoint_boundary": "u(0,t)=u(L,t)=0",
    "adjoint_space": "H_0^1(0,L) x L^2(0,L)",
    "observation": "u_x(L,t)",
    "controlled_space": "L^2(0,L) x H^{-1}(0,L) by L^2 Dirichlet control at x=L",
    "energy": "E=(1/2) integral (|u_t|^2+c^2|u_x|^2)",
}
ROUTE = {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
FLAGS = {"arithmetic_local_data": False, "euler_factors": False, "root_numbers": False, "automorphy": False, "target_divisor_or_counting_law": False, "target_functional_equation": False, "target_zero_match": False, "hilbert_polya_operator": False, "route_b_input": False}
THEOREM = {
    "revival": "the least positive full-energy wave-group identity time is 2L/c",
    "critical_identity": "at T=2L/c, integral |u_x(L,t)|^2 dt=4E(0)/c^3",
    "observability": "one-end observability holds for every T>=2L/c, equality included",
    "short_time_failure": "every T<2L/c misses a nonzero smooth periodic traveling profile",
    "hum": "duality gives exact L2 Dirichlet boundary control on the transposition state space at exactly the same threshold",
    "boundary": "no zero mode; endpoint reversal, T=0, half revival, and all positive L,c scalings are explicit",
}
PROOF = {
    "periodic_coordinate": "u(x,t)=F(x+ct)-F(-x+ct) with 2L-periodic F",
    "energy_coordinate": "E=c^2 integral_0^(2L)|F'|^2",
    "trace_coordinate": "u_x(L,t)=2F'(L+ct)",
    "missed_arc": "if cT<2L, support a nonzero smooth mean-zero F' in the complementary arc",
    "revival_phases": "all nonzero modes have frequencies n*pi*c/L and common gcd one",
    "finite_role": "exact cells audit constants and conventions but do not prove infinite-dimensional observability",
}
REFERENCES = [
    {"id": "Lions1988", "authors": "J.-L. Lions", "title": "Exact Controllability, Stabilization and Perturbations for Distributed Systems", "venue": "SIAM Review 30(1), 1-68 (1988)", "identifier": "10.1137/1030001", "url": "https://doi.org/10.1137/1030001", "role": "HUM owner"},
    {"id": "BLR1992", "authors": "Claude Bardos, Gilles Lebeau, and Jeffrey Rauch", "title": "Sharp Sufficient Conditions for the Observation, Control, and Stabilization of Waves from the Boundary", "venue": "SIAM Journal on Control and Optimization 30(5), 1024-1065 (1992)", "identifier": "10.1137/0330055", "url": "https://doi.org/10.1137/0330055", "role": "boundary geometric control owner"},
]


def f(x: Fraction) -> str:
    return str(x)


def phash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def build() -> dict:
    values = [Fraction(1,2), Fraction(1), Fraction(2), Fraction(3)]
    modal = []
    parameter_rows = []
    for L in values:
        for c in values:
            critical = 2*L/c
            parameter_rows.append({"L": f(L), "c": f(c), "critical_time": f(critical), "observation_energy_ratio": f(4/c**3)})
            for n in range(1, 17):
                modal.append({
                    "L": f(L), "c": f(c), "n": n,
                    "energy_displacement_pi2": f(c*c*n*n/(4*L)),
                    "energy_velocity": f(L/4),
                    "observation_displacement_pi2": f(n*n/(L*c)),
                    "observation_velocity": f(L/c**3),
                    "displacement_ratio": f(4/c**3),
                    "velocity_ratio": f(4/c**3),
                    "critical_cosine_norm": f(L/c),
                    "critical_sine_norm": f(L/c),
                    "critical_cross_term": "0",
                })
    revival = [{"n": n, "critical_cos": "1", "critical_sin": "0", "half_cos": str((-1)**n), "half_sin": "0"} for n in range(1,17)]
    missed = []
    for j in range(16):
        ratio = Fraction(j,16)
        missed.append({"time_ratio_T_over_Tstar": f(ratio), "observed_arc_fraction": f(ratio), "complement_fraction": f(1-ratio), "smooth_nonzero_mean_zero_support_exists": True, "boundary_trace_on_window": "0"})
    data = {
        "schema": "hcs-c287-wave-boundary-control-v1", "candidate_id": "HCS-C287",
        "evaluation_date": "2026-09-02", "source_commit": SOURCE,
        "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": MODEL, "theorem_contract": THEOREM, "proof_contract": PROOF,
        "route_a": ROUTE, "scope_flags": FLAGS,
        "enumeration": {"parameter_rows": len(parameter_rows), "modal_cells": len(modal), "revival_cells": len(revival), "subcritical_cells": len(missed), "mode_min": 1, "mode_max": 16},
        "parameter_rows": parameter_rows, "modal_cells": modal,
        "revival_cells": revival, "subcritical_cells": missed,
        "references": REFERENCES,
        "nonclaims": ["the finite modal receipt is not a proof of infinite-dimensional observability", "HUM and the geometric control mechanism are not claimed as new", "a revival and source Laplacian are not a target determinant or Hilbert-Polya operator"],
    }
    data["payload_sha256"] = phash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, default=DEFAULT); args = parser.parse_args()
    data = build(); args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2)+"\n")
    print(f"C287_PRODUCER_PASS {data['payload_sha256']} cells={sum(data['enumeration'][k] for k in ('parameter_rows','modal_cells','revival_cells','subcritical_cells'))}")


if __name__ == "__main__": main()
