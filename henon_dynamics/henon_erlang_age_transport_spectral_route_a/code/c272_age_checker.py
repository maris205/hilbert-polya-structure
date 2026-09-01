#!/usr/bin/env python3
"""Producer-independent checker for HCS-C272."""
from __future__ import annotations

import cmath
import hashlib
import json
import math
import os
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = Path(os.environ.get("C272_EVIDENCE_PATH", ROOT / "results/c272_age_evidence.json"))
SOURCE = "9cb7483e97ef82fdc06d45ecb3043f183ce22391"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EXPECTED_KEYS = {"schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator", "owner", "theorem_contract", "proof_obligations", "regression", "route_a", "scope_flags", "source", "nonclaims", "payload_sha256"}


def q(x: str) -> Q:
    return Q(x)


def phash(data: dict) -> str:
    payload = dict(data); payload.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def poly_coeffs(k: int, gamma: Q, mu: Q, beta: Q) -> list[Q]:
    c = gamma + mu
    out = [Q(math.comb(k, j)) * c**j for j in range(k + 1)]
    out[-1] -= beta * gamma**k
    return out


def polyval(coeffs: list[Q], z: complex) -> complex:
    value = 0j
    for c in coeffs:
        value = value * z + float(c)
    return value


def main() -> None:
    d = json.loads(PATH.read_text())
    assertions = 0

    def ok(v: bool) -> None:
        nonlocal assertions
        assert v
        assertions += 1

    ok(set(d) == EXPECTED_KEYS)
    ok(d["schema"] == "hcs-c272-erlang-age-transport-v1")
    ok(d["candidate_id"] == "HCS-C272")
    ok(d["source_commit"] == SOURCE)
    ok(d["fixed_epoch"] == 1788134400)
    ok(d["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    ok(d["evaluator"]["sha256"] == EVALUATOR)
    ok(d["payload_sha256"] == phash(d))
    ok(d["owner"]["state_space"] == "L1(R_+,da)")
    ok(d["theorem_contract"]["eigenvalue_gate"] == "an algebraic root is an L1 eigenvalue exactly when Re(lambda)>-mu")
    ok(d["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"])
    ok(d["route_a"]["overall"] == "ROUTE_A_REJECTED")
    ok(d["route_a"]["route_b_invocation_allowed"] is False)
    for value in d["scope_flags"].values():
        ok(value is False)

    roots_total = 0
    for row in d["regression"]["cases"]:
        k = row["k"]
        rho, beta, gamma, mu = map(q, (row["rho_beta_root"], row["beta"], row["gamma"], row["mu"]))
        ok(beta == rho**k)
        ok(q(row["essential_edge"]) == -mu)
        lam0 = gamma * (rho - 1) - mu
        ok(q(row["dominant_algebraic_root"]) == lam0)
        ok(row["dominant_isolated_eigenvalue"] is (rho > 1))
        coeffs = poly_coeffs(k, gamma, mu, beta)
        ok(list(map(q, row["characteristic_polynomial_descending"])) == coeffs)
        if rho <= 1:
            ok(row["population_regime"] == "essential_decay_no_isolated_pole")
            ok(row["stable_age_decay_rate"] is None)
            ok(row["spectral_gap"] is None)
        else:
            regime = "decay" if lam0 < 0 else ("critical_population" if lam0 == 0 else "growth")
            ok(row["population_regime"] == regime)
            ok(q(row["stable_age_decay_rate"]) == gamma * (rho - 1) > 0)
            gap_edge = float(gamma * (rho - 1))
            gap_root = math.inf if k == 1 else float(gamma * rho) * (1 - math.cos(2 * math.pi / k))
            ok(abs(float(row["spectral_gap"]) - min(gap_edge, gap_root)) < 1e-12)
        ok(len(row["roots"]) == k)
        for root in row["roots"]:
            j = root["j"]
            z = float(gamma * rho) * cmath.exp(2j * math.pi * j / k) - float(gamma + mu)
            stored = complex(float(root["real"]), float(root["imag"]))
            ok(abs(stored - z) < 1e-12)
            scale = 1.0 + sum(abs(float(c)) * abs(z) ** (k - i) for i, c in enumerate(coeffs))
            ok(abs(polyval(coeffs, z)) < 2e-12 * scale)
            off = float(rho) * math.cos(2 * math.pi * j / k) - 1
            if abs(off) < 1e-12:
                location = "essential_edge"
            elif off > 0:
                location = "eigenvalue"
            else:
                location = "algebraic_root_not_in_L1"
            ok(root["spectral_location"] == location)
            ok(abs(float(root["edge_offset_over_gamma"]) - off) < 1e-12)
            roots_total += 1
    counts = d["regression"]["counts"]
    ok(counts["parameter_cases"] == len(d["regression"]["cases"]) == 360)
    ok(counts["root_cells"] == roots_total == 2340)
    ok(counts["zero_birth_boundaries"] == len(d["regression"]["zero_birth_boundaries"]) == 6)
    for row in d["regression"]["zero_birth_boundaries"]:
        ok(row["semigroup"] == "mortality-weighted right shift")
        ok(q(row["essential_edge"]) == -q(row["mu"]))
    print(f"C272 independent checker: PASS ({assertions} assertions; exact polynomial/root/eigenvalue-gate audit)")


if __name__ == "__main__":
    main()
