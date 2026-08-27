#!/usr/bin/env python3
"""Produce the exact C197 Douglas--Rachford principal-angle certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


SOURCE_COMMIT = "c3a5b9bbb3b6d0881f395abe4a01accd322f69cb"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
DEFAULT_OUTPUT = Path(__file__).resolve().parents[1] / "results/c197_douglas_rachford_evidence.json"
ANGLES = [
    ("3-4-5", F(3, 5), F(4, 5)),
    ("5-12-13", F(5, 13), F(12, 13)),
    ("8-15-17", F(8, 17), F(15, 17)),
    ("7-24-25", F(7, 25), F(24, 25)),
]
LAMBDAS = [F(-1), F(0), F(1, 2), F(1), F(3, 2), F(2), F(3)]
PAIRS = [(0, 1), (0, 2), (1, 3)]


def enc(value: F) -> str:
    return str(value)


def mat_mul(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def mat_pow(a: list[list[F]], n: int) -> list[list[F]]:
    out = [[F(int(i == j)) for j in range(len(a))] for i in range(len(a))]
    base = a
    while n:
        if n & 1:
            out = mat_mul(out, base)
        base = mat_mul(base, base)
        n //= 2
    return out


def trace(a: list[list[F]]) -> F:
    return sum(a[i][i] for i in range(len(a)))


def poly_mul(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def block(c: F, s: F, lam: F) -> tuple[list[list[F]], F, F]:
    alpha = F(1) - lam * s * s
    beta = lam * s * c
    matrix = [[alpha, -beta], [beta, alpha]]
    determinant = alpha * alpha + beta * beta
    assert determinant == F(1) - lam * (F(2) - lam) * s * s
    return matrix, alpha, determinant


def regime(lam: F) -> str:
    if lam == 0:
        return "identity_boundary"
    if F(0) < lam < F(2):
        return "strict_contraction"
    if lam == 2:
        return "orthogonal_rotation_boundary"
    return "expansive_off_fixed_space"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def build() -> dict:
    block_rows = []
    for label, c, s in ANGLES:
        assert c * c + s * s == 1
        for lam in LAMBDAS:
            matrix, alpha, determinant = block(c, s, lam)
            block_rows.append({
                "angle_label": label,
                "cosine": enc(c),
                "sine": enc(s),
                "lambda": enc(lam),
                "matrix": [[enc(x) for x in row] for row in matrix],
                "trace": enc(2 * alpha),
                "determinant": enc(determinant),
                "power_traces_0_to_8": [enc(trace(mat_pow(matrix, n))) for n in range(9)],
                "spectral_radius_squared": enc(determinant),
                "fixed_dimension": 2 if lam == 0 else 0,
                "regime": regime(lam),
            })

    composite_rows = []
    for left, right in PAIRS:
        left_label, left_c, left_s = ANGLES[left]
        right_label, right_c, right_s = ANGLES[right]
        for lam in LAMBDAS:
            blocks = [block(left_c, left_s, lam), block(right_c, right_s, lam)]
            fixed_factor = [F(1), F(-1)]
            mismatch_factor = [F(1), -(F(1) - lam)]
            polynomial = [F(1)]
            polynomial = poly_mul(polynomial, poly_mul(fixed_factor, fixed_factor))
            polynomial = poly_mul(polynomial, poly_mul(mismatch_factor, mismatch_factor))
            for matrix, alpha, determinant in blocks:
                polynomial = poly_mul(polynomial, [F(1), -2 * alpha, determinant])
            power_traces = []
            for n in range(9):
                value = F(2) + F(2) * (F(1) - lam) ** n
                value += sum(trace(mat_pow(item[0], n)) for item in blocks)
                power_traces.append(enc(value))
            rates = [(F(1) - lam) ** 2] + [item[2] for item in blocks]
            composite_rows.append({
                "angle_labels": [left_label, right_label],
                "lambda": enc(lam),
                "dimension": 8,
                "fixed_dimension_for_nonzero_lambda": 2,
                "mismatch_dimension": 2,
                "det_I_minus_zT_coefficients": [enc(x) for x in polynomial],
                "power_traces_0_to_8": power_traces,
                "off_fixed_rate_squared": enc(max(rates)),
                "regime": regime(lam),
            })

    data = {
        "schema": "hcs-c197-douglas-rachford-v1",
        "candidate_id": "HCS-C197",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "headline": (
            "Every relaxed Douglas--Rachford map for two finite-dimensional real "
            "subspaces has an exact principal-angle block atlas, a sharp convergence "
            "window and rate, and an orthogonal rotation boundary at lambda=2"
        ),
        "frozen_object": {
            "phase_space": "finite-dimensional real Hilbert space",
            "dynamics": "T_lambda=(1-lambda)I+lambda(I+R_V R_U)/2",
            "clock": "one projection-reflection update",
            "parameters": "two linear subspaces U,V and real lambda",
            "normalization": "orthogonal projections; R_W=2P_W-I",
            "allowed_data": "exact rational principal-angle sentinels only",
            "forbidden_data": "prime tables, target zeros, local factors, root numbers",
        },
        "theorem": {
            "fixed_space_nonzero_lambda": "(U intersect V) direct-sum (U-perp intersect V-perp)",
            "generic_block": "[[1-lambda sin^2(theta),-lambda sin(theta)cos(theta)],[lambda sin(theta)cos(theta),1-lambda sin^2(theta)]]",
            "generic_modulus_squared": "1-lambda(2-lambda)sin^2(theta)",
            "convergence_window": "0<lambda<2",
            "optimal_uniform_relaxation": "lambda=1",
            "lambda_two_boundary": "R_V R_U, an orthogonal direct sum of rotations by twice each principal angle and signs on mismatch spaces",
            "period_boundary": "at lambda=2 the map has finite order iff every generic principal angle is a rational multiple of pi",
            "shadow_limit": "P_U T_lambda^n x tends to P_(U intersect V)x for 0<lambda<2",
        },
        "regression": {
            "angles": [{"label": label, "cosine": enc(c), "sine": enc(s)} for label, c, s in ANGLES],
            "lambdas": [enc(x) for x in LAMBDAS],
            "block_rows": block_rows,
            "composite_rows": composite_rows,
        },
        "summary": {
            "angle_count": len(ANGLES),
            "lambda_count": len(LAMBDAS),
            "block_row_count": len(block_rows),
            "composite_row_count": len(composite_rows),
            "exact_matrix_cells": len(block_rows) * 4,
            "exact_power_trace_cells": (len(block_rows) + len(composite_rows)) * 9,
            "composite_dimension": 8,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "The lambda=2 source boundary is an exact same-clock orthogonal reflection product.",
            "strongest_failure": "Projection geometry supplies no intrinsic rational-prime carrier, logarithmic clock, or arithmetic determinant.",
        },
        "scope_flags": {
            "uses_target_zero_table": False,
            "uses_prime_table": False,
            "claims_arithmetic_local_data": False,
            "claims_euler_factors": False,
            "claims_root_numbers": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False,
            "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "citations": [
            {
                "key": "DouglasRachford1956",
                "claim": "classical alternating-direction splitting source",
                "doi": "10.1090/S0002-9947-1956-0084194-4",
            },
            {
                "key": "BauschkeEtAl2014",
                "claim": "two-subspace convergence and Friedrichs-angle rate",
                "doi": "10.1016/j.jat.2014.06.002",
            },
        ],
        "nonclaims": [
            "priority for Douglas--Rachford splitting or principal-angle convergence",
            "an infinite-dimensional norm-rate theorem without the closed-sum hypothesis",
            "a rational-prime orbit law, Euler product, target divisor, or functional equation",
            "a Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C197_PRODUCER_PASS",
        "block_rows": data["summary"]["block_row_count"],
        "composite_rows": data["summary"]["composite_row_count"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
