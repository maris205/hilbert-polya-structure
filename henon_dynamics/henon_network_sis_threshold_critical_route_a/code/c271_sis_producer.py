#!/usr/bin/env python3
"""Deterministic exact receipt for the HCS-C271 network SIS theorem."""
from __future__ import annotations

import hashlib
import json
import os
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("C271_OUTPUT_PATH", ROOT / "results/c271_sis_evidence.json"))
SOURCE = "9cb7483e97ef82fdc06d45ecb3043f183ce22391"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788134400
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


def qs(x: Q) -> str:
    return f"{x.numerator}/{x.denominator}"


def phash(data: dict) -> str:
    payload = dict(data)
    payload.pop("payload_sha256", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def graph(family: str, n: int) -> tuple[list[list[int]], int]:
    A = [[0 for _ in range(n)] for _ in range(n)]
    if family == "directed_cycle":
        for i in range(n):
            A[i][(i + 1) % n] = 1
        return A, 1
    if family == "complete_digraph":
        for i in range(n):
            for j in range(n):
                A[i][j] = int(i != j)
        return A, n - 1
    if family == "two_out_circulant":
        for i in range(n):
            A[i][(i + 1) % n] = 1
            A[i][(i + 2) % n] = 1
        return A, 2
    raise ValueError(family)


def main() -> None:
    cases = []
    critical_samples = []
    specs = [
        ("directed_cycle", range(2, 10)),
        ("complete_digraph", range(3, 9)),
        ("two_out_circulant", range(5, 11)),
    ]
    ratios = (Q(1, 2), Q(1), Q(3, 2), Q(2))
    for family, ns in specs:
        for n in ns:
            A, r = graph(family, n)
            edges = [[i, j] for i in range(n) for j in range(n) if A[i][j]]
            for delta in (Q(1), Q(2), Q(3)):
                for ratio in ratios:
                    beta = ratio * delta / r
                    sab = beta * r - delta
                    regime = "subcritical" if sab < 0 else ("critical" if sab == 0 else "supercritical")
                    case = {
                        "family": family,
                        "n": n,
                        "row_sum": r,
                        "edges": edges,
                        "beta": qs(beta),
                        "delta": qs(delta),
                        "threshold_ratio": qs(ratio),
                        "metzler_spectral_abscissa": qs(sab),
                        "regime": regime,
                        "disease_free_exponential_gap": qs(-sab) if sab < 0 else None,
                        "endemic_coordinate": qs(1 - 1 / ratio) if ratio > 1 else None,
                        "endemic_jacobian_spectral_abscissa": qs(delta - beta * r) if ratio > 1 else None,
                        "critical_kappa": qs(beta * r) if ratio == 1 else None,
                        "critical_vector_limit_coordinate": qs(1 / delta) if ratio == 1 else None,
                    }
                    cases.append(case)
                    if ratio == 1:
                        for y0 in (Q(1, 5), Q(1, 2), Q(4, 5)):
                            for t in (Q(0), Q(1), Q(3), Q(10)):
                                y = y0 / (1 + delta * y0 * t)
                                critical_samples.append({
                                    "family": family,
                                    "n": n,
                                    "delta": qs(delta),
                                    "beta": qs(beta),
                                    "y0": qs(y0),
                                    "t": qs(t),
                                    "y": qs(y),
                                })
    data = {
        "schema": "hcs-c271-network-sis-v1",
        "candidate_id": "HCS-C271",
        "evaluation_date": "2026-09-01",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "owner": {
            "state_space": "[0,1]^n",
            "equation": "x'=beta*diag(1-x)*A*x-D*x",
            "assumptions": "A nonnegative irreducible, beta>0, D=diag(delta_i) with delta_i>0",
            "clock": "physical ODE time",
        },
        "theorem_contract": {
            "invariance": "the cube is forward invariant and every nonzero orbit is strongly positive for t>0",
            "threshold": "sign s(beta*A-D) separates extinction from the unique endemic equilibrium",
            "subcritical": "s<0 gives global exponential extinction; s=0 gives global extinction with a sharp Perron 1/t law",
            "supercritical": "s>0 gives one x* in (0,1)^n attracting every nonzero initial state",
            "critical_limit": "if Mv=0, w^T M=0, w^T v=1, then t*x(t)->v/kappa with kappa=beta*w^T*diag(v)*A*v",
            "endemic_stability": "the endemic Jacobian is irreducible Metzler Hurwitz and x* increases strictly with beta",
        },
        "proof_obligations": [
            "positive invariance and irreducible strong positivity",
            "Perron-Frobenius threshold equivalence",
            "cooperative strictly subhomogeneous global convergence",
            "critical center projection and stable-complement estimate",
            "Metzler inverse monotonicity at the endemic equilibrium",
        ],
        "regression": {
            "cases": cases,
            "critical_uniform_samples": critical_samples,
            "counts": {
                "graphs": sum(len(tuple(ns)) for _, ns in specs),
                "parameter_cases": len(cases),
                "critical_samples": len(critical_samples),
                "edge_cells": sum(len(c["edges"]) for c in cases),
            },
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "target_divisor": False,
            "functional_equation": False,
            "hilbert_polya_operator": False,
        },
        "source": {
            "authors": "Ana Lajmanovich and James A. Yorke",
            "title": "A deterministic model for gonorrhea in a nonhomogeneous population",
            "journal": "Mathematical Biosciences 28 (1976), 221-236",
            "doi": "10.1016/0025-5564(76)90125-5",
            "role": "classical irreducible multigroup SIS lineage",
        },
        "nonclaims": [
            "Workspace ownership is not a literature-priority claim.",
            "Finite regular-graph receipts are regression oracles, not proofs of the all-network theorem.",
            "The epidemic threshold is not an arithmetic prime clock or target determinant.",
        ],
    }
    data["payload_sha256"] = phash(data)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(
        "C271_PRODUCER_PASS "
        f"cases={len(cases)} critical_samples={len(critical_samples)} payload={data['payload_sha256']}"
    )


if __name__ == "__main__":
    main()
