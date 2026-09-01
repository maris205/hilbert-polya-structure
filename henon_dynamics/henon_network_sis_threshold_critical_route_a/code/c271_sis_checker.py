#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C271."""
from __future__ import annotations

import hashlib
import json
import os
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PATH = Path(os.environ.get("C271_EVIDENCE_PATH", ROOT / "results/c271_sis_evidence.json"))
SOURCE = "9cb7483e97ef82fdc06d45ecb3043f183ce22391"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EXPECTED_KEYS = {
    "schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator", "owner", "theorem_contract", "proof_obligations",
    "regression", "route_a", "scope_flags", "source", "nonclaims", "payload_sha256",
}


def phash(data: dict) -> str:
    payload = dict(data)
    payload.pop("payload_sha256", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def q(x: str) -> Q:
    return Q(x)


def main() -> None:
    d = json.loads(PATH.read_text())
    assertions = 0

    def ok(value: bool) -> None:
        nonlocal assertions
        assert value
        assertions += 1

    ok(set(d) == EXPECTED_KEYS)
    ok(d["schema"] == "hcs-c271-network-sis-v1")
    ok(d["candidate_id"] == "HCS-C271")
    ok(d["source_commit"] == SOURCE)
    ok(d["fixed_epoch"] == 1788134400)
    ok(d["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    ok(d["evaluator"]["sha256"] == EVALUATOR)
    ok(d["payload_sha256"] == phash(d))
    ok(d["owner"]["equation"] == "x'=beta*diag(1-x)*A*x-D*x")
    ok(d["theorem_contract"]["critical_limit"].endswith("kappa=beta*w^T*diag(v)*A*v"))
    ok(d["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"])
    ok(d["route_a"]["overall"] == "ROUTE_A_REJECTED")
    ok(d["route_a"]["route_b_invocation_allowed"] is False)
    for value in d["scope_flags"].values():
        ok(value is False)

    graph_keys = set()
    edge_cells = 0
    for row in d["regression"]["cases"]:
        n = row["n"]
        r = row["row_sum"]
        beta, delta, ratio = q(row["beta"]), q(row["delta"]), q(row["threshold_ratio"])
        A = np.zeros((n, n), dtype=int)
        for i, j in row["edges"]:
            ok(0 <= i < n and 0 <= j < n)
            A[i, j] += 1
        edge_cells += len(row["edges"])
        ok(np.all(A.sum(axis=1) == r))
        # Strong connectivity is checked independently by Boolean reachability.
        reach = np.eye(n, dtype=int)
        power = np.eye(n, dtype=int)
        for _ in range(n):
            power = (power @ A > 0).astype(int)
            reach = ((reach + power) > 0).astype(int)
        ok(np.all(reach == 1))
        ok(beta * r / delta == ratio)
        sab = beta * r - delta
        ok(q(row["metzler_spectral_abscissa"]) == sab)
        eig = np.linalg.eigvals(float(beta) * A - float(delta) * np.eye(n))
        ok(abs(max(z.real for z in eig) - float(sab)) < 1e-9)
        regime = "subcritical" if sab < 0 else ("critical" if sab == 0 else "supercritical")
        ok(row["regime"] == regime)
        if sab < 0:
            ok(q(row["disease_free_exponential_gap"]) == -sab)
            ok(row["endemic_coordinate"] is None)
        elif sab == 0:
            ok(q(row["critical_kappa"]) == beta * r == delta)
            ok(q(row["critical_vector_limit_coordinate"]) == 1 / delta)
            ok(row["endemic_coordinate"] is None)
        else:
            xstar = 1 - delta / (beta * r)
            ok(q(row["endemic_coordinate"]) == xstar)
            ok(0 < xstar < 1)
            residual = beta * (1 - xstar) * r * xstar - delta * xstar
            ok(residual == 0)
            ok(q(row["endemic_jacobian_spectral_abscissa"]) == delta - beta * r < 0)
        graph_keys.add((row["family"], n))

    samples = d["regression"]["critical_uniform_samples"]
    for row in samples:
        delta, beta, y0, t, y = map(q, (row["delta"], row["beta"], row["y0"], row["t"], row["y"]))
        family, n = row["family"], row["n"]
        r = 1 if family == "directed_cycle" else (n - 1 if family == "complete_digraph" else 2)
        ok(beta * r == delta)
        ok(y == y0 / (1 + delta * y0 * t))
        ok(-delta * y * y == -beta * r * y * y)
        ok(0 < y <= y0 < 1)

    counts = d["regression"]["counts"]
    ok(counts["graphs"] == len(graph_keys) == 20)
    ok(counts["parameter_cases"] == len(d["regression"]["cases"]) == 240)
    ok(counts["critical_samples"] == len(samples) == 720)
    ok(counts["edge_cells"] == edge_cells)
    print(f"C271 independent checker: PASS ({assertions} assertions; exact threshold/equilibrium/critical receipts)")


if __name__ == "__main__":
    main()
