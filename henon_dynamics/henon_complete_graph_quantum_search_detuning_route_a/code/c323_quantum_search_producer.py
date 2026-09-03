#!/usr/bin/env python3
"""Deterministic exact receipts for HCS-C323 complete-graph search."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import yaml


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c323_quantum_search_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C323/2026-09-03.yaml"
SOURCE = "1ccbfe2d759fe007c6b53c9646e1ab031878b34a"
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


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def mpf(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def dec(value: mp.mpf) -> str:
    if abs(value) < mp.mpf("1e-78"):
        return "0.0"
    return mp.nstr(value, 72, strip_zeros=False)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def semantic_yaml_hash(raw: str) -> str:
    value = yaml.safe_load(raw)
    canonical = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha(canonical)


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def interior_rows() -> list[dict]:
    drivers = [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2), Fraction(4)]
    rows = []
    for n in range(2, 33):
        for m in range(1, n):
            a = Fraction(m, n)
            for g in drivers:
                omega2 = (g - 1) ** 2 + 4 * g * a
                omega = mp.sqrt(mpf(omega2))
                pmax = a + 4 * g * a * (1 - a) / omega2
                defect = (1 - a) * (g - 1) ** 2 / omega2
                root = mp.sqrt(mpf(omega2))
                rows.append(
                    {
                        "N": n,
                        "M": m,
                        "a": q(a),
                        "g": q(g),
                        "omega_squared": q(omega2),
                        "bright_trace": q(-(g + 1)),
                        "bright_determinant": q(g * (1 - a)),
                        "lambda_minus": dec(-(mpf(g) + 1 + root) / 2),
                        "lambda_plus": dec(-(mpf(g) + 1 - root) / 2),
                        "marked_dark_multiplicity": m - 1,
                        "unmarked_dark_multiplicity": n - m - 1,
                        "success_at_zero": q(a),
                        "success_maximum": q(pmax),
                        "success_maximum_defect": q(defect),
                        "bright_half_period": dec(mp.pi / omega),
                        "resonant": g == 1,
                        "search_oscillation_nonconstant": g > 0,
                        "graph_gamma": q(g / n),
                        "graph_scalar_shift": q(g / n),
                        "zero_driver_minus_one_multiplicity": m if g == 0 else None,
                        "zero_driver_zero_multiplicity": n - m if g == 0 else None,
                    }
                )
    return rows


def window_rows() -> list[dict]:
    rows = []
    for k in (8, 16, 32, 64):
        a = Fraction(1, k * k)
        for c in (Fraction(-4), Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2), Fraction(4)):
            g = 1 + c / k
            omega2 = (g - 1) ** 2 + 4 * g * a
            pmax = a + 4 * g * a * (1 - a) / omega2
            rows.append(
                {
                    "k": k,
                    "c": q(c),
                    "a": q(a),
                    "g": q(g),
                    "omega_squared": q(omega2),
                    "success_maximum": q(pmax),
                    "scaled_peak_time": dec(mp.sqrt(mpf(a)) * mp.pi / mp.sqrt(mpf(omega2))),
                    "limit_success_maximum": dec(4 / (mpf(c) ** 2 + 4)),
                    "limit_scaled_peak_time": dec(mp.pi / mp.sqrt(mpf(c) ** 2 + 4)),
                }
            )
    return rows


def boundary_rows() -> list[dict]:
    rows = []
    drivers = [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2)]
    for n in range(1, 33):
        for g in drivers:
            rows.extend(
                [
                    {
                        "face": "no_marked_states",
                        "N": n,
                        "M": 0,
                        "g": q(g),
                        "uniform_eigenvalue": q(-g),
                        "orthogonal_eigenvalue": "0",
                        "orthogonal_multiplicity": n - 1,
                        "success_probability": "0",
                    },
                    {
                        "face": "all_states_marked",
                        "N": n,
                        "M": n,
                        "g": q(g),
                        "uniform_eigenvalue": q(-(g + 1)),
                        "orthogonal_eigenvalue": "-1",
                        "orthogonal_multiplicity": n - 1,
                        "success_probability": "1",
                    },
                ]
            )
    return rows


def make_data() -> dict:
    evaluation_raw = EVALUATION.read_bytes()
    rows = interior_rows()
    windows = window_rows()
    boundaries = boundary_rows()
    data = {
        "schema": "hcs-c323-quantum-search-v1",
        "candidate_id": "HCS-C323",
        "obstruction_id": "HEN-O307",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "evaluation": {
            "path": "evaluations/route_a/HCS-C323/2026-09-03.yaml",
            "raw_sha256": sha(evaluation_raw),
            "semantic_sha256": semantic_yaml_hash(evaluation_raw.decode()),
        },
        "model": {
            "owner": "permutation-symmetric complete-graph continuous-time quantum search",
            "hamiltonian": "H_g=-g|s><s|-P_W",
            "uniform_state": "|s>=N^(-1/2) sum_x |x>",
            "marked_fraction": "a=M/N",
            "domain": "N>=1, 0<=M<=N, g>=0",
            "success": "squared norm of the projection onto the full marked subspace",
            "clock": "physical unitary time exp(-itH_g)",
        },
        "theorem_contract": {
            "decomposition": "marked dark eigenvalue -1, unmarked dark eigenvalue 0, and a two-dimensional bright block for 0<M<N",
            "bright_spectrum": "lambda_+-lambda_-=sqrt((g-1)^2+4ga), with trace -(g+1) and determinant g(1-a)",
            "success_law": "p_W(t)=a+4ga(1-a)/Omega^2 sin^2(Omega t/2)",
            "perfect_search": "for 0<a<1, perfect success occurs iff g=1 and first occurs at pi/(2sqrt(a))",
            "detuning": "1-p_max=(1-a)(g-1)^2/Omega^2 and g=1+c sqrt(a) has a nontrivial critical window",
            "graph_equivalence": "for g=gamma N, -gamma A(K_N)-P_W=H_g+gamma I",
            "faces": "M=0, M=N, N=1, and g=0 are diagonalized without fictitious negative dark multiplicities",
        },
        "references": [
            {"identifier": "10.1103/PhysRevA.57.2403", "role": "continuous-time analog quantum-search owner"},
            {"identifier": "quant-ph/9612026", "role": "author preprint of the primary source"},
        ],
        "collision_boundary": {
            "C143": "discrete-time inhomogeneous coined five-cycle walk, not a complete-graph oracle Hamiltonian",
            "C171": "stochastic Ehrenfest Krawtchouk Markov operator, not unitary oracle search",
            "C183": "random-transposition Markov operator, not coherent rank-two search",
            "C223": "Jaynes--Cummings excitation blocks, not permutation-symmetric marked-set search",
            "C318": "local one-dimensional SSH bulk--edge chain, not a complete-graph driver and oracle projection",
        },
        "nonclaims": [
            "No literature-priority claim is made for continuous-time search, multimarked reduction, or detuning formulas.",
            "The finite characteristic polynomial is not an Euler factor and the energy levels are not target zeros.",
            "No target arithmetic datum, root number, automorphy, target divisor, functional equation, Hilbert--Polya operator, or Route-B input is claimed.",
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "parameter_grid": {
            "N": "2..32",
            "M": "1..N-1",
            "g": ["0", "1/4", "1/2", "1", "3/2", "2", "4"],
            "window_k": [8, 16, 32, 64],
            "window_c": ["-4", "-2", "-1", "0", "1", "2", "4"],
            "boundary_N": "1..32",
            "boundary_g": ["0", "1/2", "1", "2"],
        },
        "interior_rows": rows,
        "critical_window_rows": windows,
        "boundary_rows": boundaries,
        "enumeration": {
            "interior_rows": len(rows),
            "critical_window_rows": len(windows),
            "boundary_rows": len(boundaries),
            "exact_driver_values": 7,
            "audited_leaf_count": 0,
        },
    }
    before = leaves(data)
    data["enumeration"]["audited_leaf_count"] = before + 1
    body = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha(body)
    return data


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C323 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = make_data()
    raw = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(raw)
    print(
        "C323_PRODUCER_PASS "
        f"{data['enumeration']['interior_rows']} "
        f"{data['enumeration']['audited_leaf_count']} "
        f"{data['payload_sha256']}"
    )


if __name__ == "__main__":
    main()
