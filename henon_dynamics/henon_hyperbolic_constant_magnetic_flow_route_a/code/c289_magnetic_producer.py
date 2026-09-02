#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C289."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c289_magnetic_evidence.json"
SOURCE = "7fbe9db30cc460a82883533d7cfb2edd988c5b65"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"

MODEL = {
    "configuration": "the simply connected oriented surface H^2 of curvature -kappa^2",
    "equation": "D_t velocity=b J velocity with constant speed v",
    "parameters": "kappa>0, v>0, and b real",
    "ambient_frame": "e0=kappa X is unit timelike and (e0,T,JT) is Lorentz orthonormal",
    "frame_ode": "for the matrix F=(e0,T,JT) of frame columns, F'=F A with the displayed right-action generator",
    "clock": "physical trajectory time t",
}
THEOREM = {
    "classification": "every nonstationary orbit is exactly a circle, horocycle, hypercycle, or geodesic according to |b| versus kappa v",
    "circle": "if |b|>kappa v every orbit is a hyperbolic circle of primitive period 2 pi/sqrt(b^2-kappa^2 v^2)",
    "critical": "if |b|=kappa v every orbit is a nonclosed horocycle and the Lorentz generator is nonzero nilpotent",
    "subcritical": "if 0<|b|<kappa v every orbit is an unbounded hypercycle and if b=0 it is a geodesic",
    "generator": "the raw Lorentz-frame generator satisfies A^3=(kappa^2 v^2-b^2)A",
    "boundary": "orientation, zero field, zero speed, and the Euclidean curvature limit are kept separate",
}
PROOF = {
    "frenet": "constant speed turns the magnetic equation into signed geodesic curvature b/v",
    "geometry": "the complete classification of constant-geodesic-curvature curves on H^2 gives the four orbit types",
    "lorentz": "differentiate the ambient Lorentz frame and classify its one-parameter subgroup by the cubic identity",
    "period": "the circle relation kappa coth(kappa rho)=|b|/v and its circumference give the primitive period",
    "circle_primitivity": "the embedded circle at nonzero constant speed first returns after one circumference; equivalently its nonzero rotating basepoint component returns iff sqrt(delta)t lies in 2 pi Z",
    "critical_basepoint": "at equality exp(tA)e0 has T-coordinate kappa v t, so no nonzero time returns the base point",
    "completeness": "the frame ODE has a global exponential for every initial frame and exhausts all magnetic initial data",
    "finite_role": "finite cells audit signs, thresholds, and periods but do not prove the all-parameter theorem",
}
ROUTE = {
    "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
    "overall": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
}
SCOPE_FLAGS = {
    "arithmetic_local_data": False,
    "euler_factors": False,
    "root_numbers": False,
    "automorphy": False,
    "target_divisor_or_counting_law": False,
    "target_functional_equation": False,
    "target_zero_match": False,
    "hilbert_polya_operator": False,
    "route_b_input": False,
}
REFERENCES = [
    {
        "id": "Comtet1987",
        "authors": "Alain Comtet",
        "title": "On the Landau Levels on the Hyperbolic Plane",
        "venue": "Annals of Physics 173 (1987), 185-209",
        "identifier": "10.1016/0003-4916(87)90098-4",
        "url": "https://doi.org/10.1016/0003-4916(87)90098-4",
        "ownership": "direct owner of the classical and quantum constant-field problem on the hyperbolic plane",
    },
    {
        "id": "Adachi1995",
        "authors": "Toshiaki Adachi",
        "title": "Kaehler Magnetic Flows for a Manifold of Constant Holomorphic Sectional Curvature",
        "venue": "Tokyo Journal of Mathematics 18 (1995), 473-483",
        "identifier": "10.3836/tjm/1270043477",
        "url": "https://doi.org/10.3836/tjm/1270043477",
        "ownership": "direct geometric owner for magnetic trajectories on constant-curvature Kaehler space forms",
    },
]
NONCLAIMS = [
    "the classical circle-horocycle-hypercycle classification is not claimed as literature originality",
    "finite rational cells are regression evidence and do not replace the all-parameter proof",
    "a magnetic Laplacian is only a formal quantization hint here; no self-adjoint operator or spectrum is constructed",
]


def q(value: Fraction) -> str:
    return str(value)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def orbit_row(kappa: Fraction, speed: Fraction, field: Fraction) -> dict:
    threshold = kappa * speed
    delta = field * field - threshold * threshold
    orientation = 0 if field == 0 else (1 if field > 0 else -1)
    if delta > 0:
        kind = "circle"
        closed = True
        period_sq = 1 / delta
        shape = threshold / abs(field)
    elif delta == 0:
        kind = "horocycle"
        closed = False
        period_sq = None
        shape = Fraction(1)
    elif field == 0:
        kind = "geodesic"
        closed = False
        period_sq = None
        shape = Fraction(0)
    else:
        kind = "hypercycle"
        closed = False
        period_sq = None
        shape = abs(field) / threshold
    return {
        "kappa": q(kappa),
        "speed": q(speed),
        "field": q(field),
        "geodesic_curvature": q(field / speed),
        "discriminant": q(delta),
        "orbit_type": kind,
        "orientation": orientation,
        "closed": closed,
        "period_over_2pi_squared": None if period_sq is None else q(period_sq),
        "shape_tanh": q(shape),
    }


def build() -> dict:
    kappas = (Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3))
    speeds = (Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3))
    fields = tuple(Fraction(x) for x in (-6, -3, -2, -1, 0, 1, 2, 3, 6))
    orbit_cells = [orbit_row(k, v, b) for k in kappas for v in speeds for b in fields]
    counts = {kind: sum(row["orbit_type"] == kind for row in orbit_cells) for kind in ("circle", "horocycle", "hypercycle", "geodesic")}
    boundary_cells = [
        {"name": "zero_speed", "parameters": {"kappa": "1", "speed": "0", "field": "2"}, "conclusion": "stationary curve; the unit-frame theorem is not invoked"},
        {"name": "euclidean_circle", "parameters": {"kappa": "0", "speed": "3", "field": "2"}, "conclusion": "Euclidean circle with period_over_2pi_squared=1/4"},
        {"name": "euclidean_line", "parameters": {"kappa": "0", "speed": "3", "field": "0"}, "conclusion": "Euclidean straight line"},
        {"name": "field_reversal", "parameters": {"kappa": "2", "speed": "1", "field_pair": "-3,3"}, "conclusion": "same unoriented circle and period with opposite orientation"},
        {"name": "critical_nonclosure", "parameters": {"kappa": "2", "speed": "3", "field": "6"}, "conclusion": "horocycle, nonzero nilpotent generator, and no primitive period"},
    ]
    data = {
        "schema": "hcs-c289-hyperbolic-magnetic-flow-v1",
        "candidate_id": "HCS-C289",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": MODEL,
        "theorem_contract": THEOREM,
        "proof_contract": PROOF,
        "route_a": ROUTE,
        "scope_flags": SCOPE_FLAGS,
        "enumeration": {
            "kappa_values": [q(x) for x in kappas],
            "speed_values": [q(x) for x in speeds],
            "field_values": [q(x) for x in fields],
            "orbit_cells": len(orbit_cells),
            "boundary_cells": len(boundary_cells),
            "type_counts": counts,
        },
        "orbit_cells": orbit_cells,
        "boundary_cells": boundary_cells,
        "references": REFERENCES,
        "nonclaims": NONCLAIMS,
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    total = data["enumeration"]["orbit_cells"] + data["enumeration"]["boundary_cells"]
    print(f"C289_PRODUCER_PASS {data['payload_sha256']} cells={total}")


if __name__ == "__main__":
    main()
