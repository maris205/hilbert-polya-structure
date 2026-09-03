#!/usr/bin/env python3
"""Deterministic finite receipts for HCS-C331."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c331_dirac_monopole_evidence.json"
SOURCE = "5ca65027918c0fce7ef9af82f3faf2e46ed6530c"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
EVAL_RAW = "02af8e9102ec43a62b69b5131952ff6e49f83e0ab1826b9a916ed32a953abd4a"
EVAL_SEMANTIC = "03ca40b5c17fa8858846885ae2c4a48375c114b71594550f3896ab4b69779a21"
SPEEDS = (Fraction(1, 2), Fraction(1), Fraction(3, 2))
HEAT_TIMES = (Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2))
HEAT_CUTOFF = 80
mp.mp.dps = 110

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


def dec(value: mp.mpf) -> str:
    return mp.nstr(value, 80, strip_zeros=False, min_fixed=-120, max_fixed=120)


def mpq(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def classical_row(index: int, q: int, speed: Fraction) -> dict:
    b = Fraction(q, 2)
    energy = speed * speed / 2
    w2 = speed * speed + b * b
    w = mp.sqrt(mpq(w2))
    ss, bb = mpq(speed), mpq(b)
    samples = []
    for phase, (cosine, sine) in enumerate(((1, 0), (0, 1), (-1, 0), (0, -1), (1, 0))):
        c, s = mp.mpf(cosine), mp.mpf(sine)
        x = ss * s / w
        y = ss * bb * (1-c) / (w*w)
        z = c + bb*bb*(1-c)/(w*w)
        samples.append({"quarter_phase": phase, "x": dec(x), "y": dec(y), "z": dec(z)})
    return {
        "row_id": f"mag-{index:03d}",
        "q": q,
        "speed": rat(speed),
        "energy": rat(energy),
        "magnetic_charge": rat(b),
        "angular_norm_squared": rat(w2),
        "period": dec(2*mp.pi/w),
        "plane_height": dec(bb/w),
        "orbit_radius_squared": rat(speed*speed/w2),
        "quarter_positions": samples,
    }


def spectral_row(q: int, n: int) -> dict:
    aq = abs(q)
    value = Fraction(n*(n+aq+1), 1) + Fraction(aq, 2)
    return {"q": q, "n": n, "eigenvalue": rat(value), "multiplicity": 2*n+aq+1}


def heat_row(aq: int, time: Fraction) -> dict:
    tt = mpq(time)
    total = mp.mpf("0")
    for n in range(HEAT_CUTOFF+1):
        eigenvalue = mp.mpf(n*(n+aq+1)) + mp.mpf(aq)/2
        total += (2*n+aq+1)*mp.exp(-tt*eigenvalue)
    next_eigenvalue = mp.mpf((HEAT_CUTOFF+1)*(HEAT_CUTOFF+aq+2)) + mp.mpf(aq)/2
    return {
        "abs_q": aq,
        "time": rat(time),
        "cutoff": HEAT_CUTOFF,
        "partial_heat_trace": dec(total),
        "first_omitted_eigenvalue": dec(next_eigenvalue),
    }


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C331 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()

    classical = []
    for q in range(-6, 7):
        for speed in SPEEDS:
            classical.append(classical_row(len(classical)+1, q, speed))
    spectral = [spectral_row(q, n) for q in range(-10, 11) for n in range(17)]
    heat = [heat_row(q, t) for q in range(9) for t in HEAT_TIMES]
    chern = [{"q": q, "flux_over_two_pi": q, "charge": rat(Fraction(q, 2))} for q in range(-12, 13)]
    time_reversal = []
    for q in range(1, 7):
        for speed in SPEEDS:
            b = Fraction(q, 2)
            time_reversal.append({
                "q": q,
                "speed": rat(speed),
                "original_charge": rat(b),
                "paired_charge": rat(-b),
                "original_tangent_x": rat(speed),
                "paired_tangent_x": rat(-speed),
                "original_K": ["0", rat(speed), rat(b)],
                "paired_K": ["0", rat(-speed), rat(-b)],
                "same_geometric_plane": True,
                "opposite_traversal": True,
                "period_equal": True,
            })

    data = {
        "schema": "hcs-c331-dirac-monopole-v1",
        "candidate_id": "HCS-C331",
        "obstruction_id": "HEN-O315",
        "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR},
        "evaluation_lock": {
            "relative_path": "evaluations/route_a/HCS-C331/2026-09-03.yaml",
            "raw_sha256": EVAL_RAW,
            "semantic_sha256": EVAL_SEMANTIC,
        },
        "model": {
            "manifold": "unit oriented two-sphere",
            "connection_curvature": "i*(q/2)*dA on the degree-q Hermitian line bundle",
            "classical_equation": "nabla_t xdot=(q/2)*J*xdot with speed squared 2E",
            "quantum_operator": "Friedrichs realization of the nonnegative covariant-Laplacian form on smooth sections",
            "parameters": "q integral and E nonnegative",
        },
        "theorem_contract": {
            "poincare_vector": "K=x cross xdot+(q/2)x is conserved with K dot x=q/2 and norm squared 2E+q^2/4",
            "positive_energy_orbits": "every E>0 trajectory is a primitive oriented small circle of period 2pi/sqrt(2E+q^2/4)",
            "bundle_connection_bridge": "degree-q line bundles on S^2 are classified by c1 and every unitary connection with curvature i*(q/2)*dA is unitary-gauge equivalent to the standard homogeneous monopole connection because H^1_dR(S^2)=0",
            "operator_realization": "Delta_q is the Friedrichs realization of the nonnegative form integral |nabla s|^2 dA on smooth sections and equals the unique self-adjoint closure of the compact boundaryless elliptic covariant Laplacian",
            "spectrum": "lambda_nq=n(n+abs(q)+1)+abs(q)/2 with multiplicity 2n+abs(q)+1 for every n>=0",
            "heat_trace": "Tr exp(-t Delta_q)=sum_n>=0 (2n+abs(q)+1) exp(-t lambda_nq) for t>0",
            "sign_reversal": "x_q(-t) with reversed initial velocity solves charge -q and traverses the same geometric circle oppositely; bundle conjugation preserves spectrum",
            "boundaries": "q=0 is the round geodesic and spherical-harmonic case; E=0 is stationary; nonintegral q has no frozen global line bundle",
        },
        "classical_rows": classical,
        "spectral_rows": spectral,
        "heat_rows": heat,
        "chern_rows": chern,
        "time_reversal_rows": time_reversal,
        "boundary_atlas": [
            {"face": "q=0", "status": "great-circle geodesic flow and ordinary spherical harmonics"},
            {"face": "E=0", "status": "stationary classical points; no primitive orbit is counted"},
            {"face": "q changes sign", "status": "time reversal pairs charge q with charge -q after reversing initial velocity on the same geometric circle; the conjugate bundle has identical spectrum"},
            {"face": "q nonintegral", "status": "the classical equation is local but the frozen global degree-q line bundle does not exist"},
            {"face": "positive energy", "status": "orbits occur in clean continuous circle families and are not isolated hyperbolic cycles"},
            {"face": "n=0", "status": "lowest monopole level has eigenvalue abs(q)/2 and multiplicity abs(q)+1"},
            {"face": "connection gauge class", "status": "fixed curvature on the unique degree-q line bundle determines one unitary gauge class because H^1_dR(S^2)=0; the spectrum is gauge invariant"},
            {"face": "operator domain", "status": "the smooth-section energy form has the Friedrichs realization, equal to the unique self-adjoint elliptic closure on compact boundaryless S^2"},
        ],
        "collision_boundary": {
            "C313": "round-sphere geodesic and Laplacian dynamics is exactly the q=0 boundary only",
            "C289": "hyperbolic magnetic flow is noncompact and has no monopole line-bundle spectrum",
            "C293": "magnetic Grushin dynamics has a singular cylinder geometry and flux channels",
            "C274": "the Euclidean Penning trap has no Chern-degree quantization on a sphere",
        },
        "route_a": {
            "tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "nonclaims": [
            "No priority is claimed for monopole harmonics, Dirac quantization, or magnetic small circles.",
            "Chern integrality is not a rational-prime or prime-power carrier.",
            "Clean circle families are not an isolated hyperbolic primitive-orbit ledger.",
            "The covariant Laplacian is not asserted to be a Hilbert--Polya operator.",
            "Finite grids are regression receipts and do not prove the all-q and all-n theorem.",
            "No target arithmetic local data, Euler factors, root numbers, automorphy, divisor, functional equation, or zero match is asserted.",
        ],
        "references": [
            {"doi": "10.1098/rspa.1931.0130", "role": "Dirac quantization and integral magnetic charge source"},
            {"doi": "10.1016/0550-3213(76)90143-7", "role": "Wu--Yang global monopole-harmonic construction"},
            {"doi": "10.1103/PhysRevD.14.437", "role": "Wu--Yang classical global monopole dynamics source"},
            {"doi": "10.1103/PhysRevD.16.1018", "role": "further monopole-harmonic properties source"},
        ],
    }
    data["enumeration"] = {
        "classical_rows": len(classical),
        "quarter_samples": sum(len(row["quarter_positions"]) for row in classical),
        "spectral_rows": len(spectral),
        "heat_rows": len(heat),
        "chern_rows": len(chern),
        "time_reversal_rows": len(time_reversal),
    }
    data["enumeration"]["audited_leaf_count"] = leaves(data) + 1
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C331_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")


if __name__ == "__main__":
    main()
