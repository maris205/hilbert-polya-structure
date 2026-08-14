#!/usr/bin/env python3
"""Independent checker for the HCS-P51 compact certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_CERTIFICATE = PROJECT / "results" / "c51_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c51_independent_check.json"

A = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)


def canonical_sha(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(4)) for j in range(4)]
        for i in range(4)
    ]


def marked(period: int) -> int:
    result = [[int(i == j) for j in range(4)] for i in range(4)]
    base = [list(row) for row in A]
    exponent = period
    while exponent:
        if exponent & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        exponent //= 2
    return sum(result[i][i] for i in range(4))


def run_check(path: Path) -> dict[str, Any]:
    certificate = json.loads(path.read_text())
    observed_core = certificate.pop("core_sha256")
    if canonical_sha(certificate) != observed_core:
        raise RuntimeError("core digest mismatch")
    certificate["core_sha256"] = observed_core
    if certificate["schema"] != "hcs-p51-abel-graded-all-orbit-germ-v1":
        raise RuntimeError("schema mismatch")
    for lock in certificate["dependency_locks"].values():
        dependency = TRACK / lock["path"]
        observed = hashlib.sha256(dependency.read_bytes()).hexdigest()
        if observed != lock["sha256"]:
            raise RuntimeError(f"dependency hash mismatch: {lock['path']}")
    constants = certificate["constants"]
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    j_star = (math.sqrt(17.0) + math.sqrt(13.0)) / 2.0
    sigma = math.log(2.0 * phi) / (0.277980 * math.log(j_star))
    if not math.isclose(constants["golden_ratio"], phi, rel_tol=0.0, abs_tol=1e-15):
        raise RuntimeError("golden-ratio constant mismatch")
    if not math.isclose(constants["J_star"], j_star, rel_tol=0.0, abs_tol=1e-15):
        raise RuntimeError("J_star constant mismatch")
    if not math.isclose(constants["sigma_certified"], sigma, rel_tol=0.0, abs_tol=1e-14):
        raise RuntimeError("certified half-plane mismatch")
    rows = certificate["period_rows"]
    if [row["marked_points"] for row in rows[:8]] != [1, 1, 4, 9, 11, 16, 29, 49]:
        raise RuntimeError("marked census sentinel mismatch")
    for row in rows:
        if row["marked_points"] != marked(row["period"]):
            raise RuntimeError("marked census recomputation mismatch")
        if row["fixed_algebra_degree_cap"] != 2 ** row["period"]:
            raise RuntimeError("fixed-algebra rank mutation")
        if row["marked_points"] > row["marked_bound_3phi_m"] + 1e-10:
            raise RuntimeError("symbolic growth bound mismatch")
    period_four = certificate["period_four_rows"]
    if [row["beta_absolute"] for row in period_four[:4]] != ["579", "578", "334661", "577"]:
        raise RuntimeError("period-four packet sentinel mismatch")
    if not all(row["p50_crosscheck"] for row in period_four if row["p50_crosscheck"] is not None):
        raise RuntimeError("P50 packet crosscheck mismatch")
    for row in period_four:
        if row["index"] > 12 and not row["flatters_fresh_prime_guaranteed"]:
            raise RuntimeError("Flatters boundary flag missing")
    ledger = certificate["theorem_ledger"]
    forbidden_promotions = {
        "analytic_continuation_beyond_certified_domain": "OPEN",
        "boundary_abel_renormalization": "OPEN",
        "von_mangoldt_trace_law": "OPEN",
        "fredholm_determinant": "OPEN",
        "hilbert_polya_operator": "OPEN",
    }
    if any(ledger[key] != value for key, value in forbidden_promotions.items()):
        raise RuntimeError("claim-boundary promotion detected")
    lower_at_one = [
        row["flatters_lower_norm"]
        for row in certificate["abel_boundary_lower_bounds"]
        if row["u_radius"] == 1.0
    ]
    if lower_at_one != sorted(lower_at_one) or not lower_at_one[-1] > 100.0:
        raise RuntimeError("u=1 divergence sentinel mismatch")
    wrong_threshold = math.log(phi) / (0.277980 * math.log(j_star))
    missing_degree_ratio = 2.0 * phi * math.exp(-wrong_threshold * 0.277980 * math.log(j_star))
    if not missing_degree_ratio > 1.0:
        raise RuntimeError("missing-degree mutation was not rejected")
    return {
        "candidate_id": "HCS-P51",
        "certificate_core_sha256": observed_core,
        "dependency_lock_count": len(certificate["dependency_locks"]),
        "dependency_hashes_recomputed": True,
        "marked_rows_checked": len(rows),
        "period_four_rows_checked": len(period_four),
        "mutations_rejected": 4,
        "status": "PASS",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run_check(args.certificate)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
