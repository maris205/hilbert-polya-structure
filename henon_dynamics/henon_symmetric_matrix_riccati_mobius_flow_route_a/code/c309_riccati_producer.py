#!/usr/bin/env python3
"""Deterministic exact/numerical receipts for HCS-C309."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c309_riccati_evidence.json"
SOURCE = "b3e2f3f7207b85d7be942ff72b1f49e754615c76"
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

SPECS = [
    ("scalar-minus-two", ["-2"]),
    ("scalar-minus-one", ["-1"]),
    ("scalar-zero", ["0"]),
    ("scalar-one", ["1"]),
    ("scalar-three", ["3"]),
    ("two-global", ["-1", "2"]),
    ("two-heteroclinic", ["-1/2", "1/3"]),
    ("two-forward-pole", ["-3", "1/2"]),
    ("two-both-poles", ["-4", "5"]),
    ("three-mixed-global", ["-1", "0", "7/3"]),
    ("three-two-forward-poles", ["-5", "-2", "4"]),
    ("three-repeated", ["-1/3", "-1/3", "2"]),
    ("four-global-boundary", ["-1", "-1", "1", "3"]),
    ("four-interior", ["-3/4", "-1/4", "1/4", "3/4"]),
    ("four-pole-tie", ["-2", "-2", "0", "2"]),
    ("five-spectrum", ["-1", "-2/3", "0", "3/2", "4"]),
]


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def dec(value: mp.mpf) -> str:
    if value == 0:
        return "0.0"
    return mp.nstr(value, 72, strip_zeros=False)


def scalar_flow(lam: Fraction, t: mp.mpf) -> mp.mpf:
    value = mp.mpf(lam.numerator) / lam.denominator
    return (value * mp.cosh(t) + mp.sinh(t)) / (mp.cosh(t) + value * mp.sinh(t))


def pole(lam: Fraction):
    if abs(lam) <= 1:
        return None
    value = mp.mpf(lam.numerator) / lam.denominator
    return mp.atanh(-1 / value)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def leaf_count(value) -> int:
    if type(value) is dict:
        return sum(leaf_count(item) for item in value.values())
    if type(value) is list:
        return sum(leaf_count(item) for item in value)
    return 1


def build_case(case_id: str, raw):
    eigenvalues = [Fraction(item) for item in raw]
    poles = [(index, pole(value)) for index, value in enumerate(eigenvalues) if pole(value) is not None]
    forward = [(index, time) for index, time in poles if time > 0]
    backward = [(index, time) for index, time in poles if time < 0]
    forward_global = not forward
    probes = []
    for text in ("-1", "-1/4", "0", "1/3", "1", "2"):
        time = mp.mpf(Fraction(text).numerator) / Fraction(text).denominator
        if any(abs(time - point) < mp.mpf("0.03") for _, point in poles):
            continue
        values = [scalar_flow(value, time) for value in eigenvalues]
        denominators = [mp.cosh(time) + (mp.mpf(value.numerator) / value.denominator) * mp.sinh(time) for value in eigenvalues]
        residuals = [1 - value * value for value in values]
        probes.append({
            "time": text,
            "flow_eigenvalues": [dec(value) for value in values],
            "denominators": [dec(value) for value in denominators],
            "velocity_eigenvalues": [dec(value) for value in residuals],
            "lyapunov_derivative": dec(-sum(value * value for value in residuals)),
        })
    loewner_time = mp.mpf("0.7")
    c, s = mp.cosh(loewner_time), mp.sinh(loewner_time)
    loewner = []
    for i, left in enumerate(eigenvalues):
        row = []
        lv = mp.mpf(left.numerator) / left.denominator
        for right in eigenvalues:
            rv = mp.mpf(right.numerator) / right.denominator
            row.append(dec(1 / ((c + lv * s) * (c + rv * s))))
        loewner.append(row)
    return {
        "case_id": case_id,
        "dimension": len(eigenvalues),
        "eigenvalues": [q(value) for value in eigenvalues],
        "forward_global": forward_global,
        "forward_poles": [{"index": index, "time": dec(time)} for index, time in forward],
        "backward_poles": [{"index": index, "time": dec(time)} for index, time in backward],
        "forward_limit": (["-1" if value == -1 else "1" for value in eigenvalues] if forward_global else None),
        "probe_rows": probes,
        "loewner_time": "0.7",
        "loewner_factors": loewner,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    cases = [build_case(case_id, values) for case_id, values in SPECS]
    strata = []
    for n in range(1, 9):
        for p in range(n + 1):
            qminus = n - p
            strata.append({
                "n": n, "plus_multiplicity": p, "minus_multiplicity": qminus,
                "stable_dimension": p * (p + 1) // 2,
                "unstable_dimension": qminus * (qminus + 1) // 2,
                "center_dimension": p * qminus,
                "ambient_dimension": n * (n + 1) // 2,
            })
    data = {
        "schema": "hcs-c309-symmetric-matrix-riccati-v1",
        "candidate_id": "HCS-C309",
        "obstruction_id": "HEN-O293",
        "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": {
            "phase_space": "Sym(n,R) for every finite n>=1",
            "dynamics": "Xdot=I-X^2",
            "solution": "(X0 cosh(t)+I sinh(t))(I cosh(t)+X0 sinh(t))^{-1}",
        },
        "theorem_contract": {
            "maximal_interval": "poles occur exactly when cosh(t)+lambda sinh(t)=0 for an initial eigenvalue lambda",
            "forward_atlas": "forward global iff lambda_min(X0)>=-1; its limit is I-2P_{lambda=-1}",
            "gradient": "Phi=tr(X^3/3-X) and Phi_dot=-norm(I-X^2)_F^2",
            "morse_bott": "symmetric involutions form Grassmann strata with exact stable, unstable, and center dimensions",
            "frechet": "the solution-map Loewner factor is the reciprocal product of the two scalar denominators",
            "linear_lift": "X=VU^{-1} lifts to Udot=V, Vdot=U until chart failure",
        },
        "cases": cases,
        "equilibrium_strata": strata,
        "collision_boundary": {
            "C185": "Brockett double-bracket flow is isospectral; C309 moves eigenvalues by one Riccati Mobius map.",
            "C298": "Grassmann projection flow evolves a fixed-rank projector; C309 evolves every symmetric matrix and its involution strata.",
            "C297": "The PT dimer has a scalar projective Riccati coordinate; C309 is an all-dimensional symmetric matrix Riccati flow.",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "nonclaims": [
            "The finite-dimensional symmetric lift is source-local and is not a Hilbert--Polya operator.",
            "No target arithmetic data, Euler factors, root numbers, automorphy, divisor law, functional equation, or zero match is asserted.",
            "No literature novelty or priority is claimed for Riccati linearization.",
        ],
        "references": [
            {"identifier": "10.1016/0167-6911(91)90044-F", "role": "matrix Riccati and symmetric-flow lineage only"},
        ],
    }
    data["enumeration"] = {
        "case_count": len(cases), "stratum_count": len(strata),
        "probe_count": sum(len(case["probe_rows"]) for case in cases),
    }
    data["enumeration"]["audited_leaf_count"] = leaf_count(data) + 1
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C309_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")


if __name__ == "__main__":
    main()
