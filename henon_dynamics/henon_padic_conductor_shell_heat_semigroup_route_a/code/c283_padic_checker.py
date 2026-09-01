#!/usr/bin/env python3
"""Producer-independent semantic checker for HCS-C283."""
from __future__ import annotations

import hashlib
import json
import math
import os
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PATH = Path(os.environ.get("C283_EVIDENCE_PATH", ROOT / "results/c283_padic_evidence.json"))
SOURCE = "51fb3d46f96b854314811c1ad62d3103cd5d54e5"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EXPECTED_KEYS = {
    "schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator", "owner", "theorem_contract", "proof_obligations",
    "regression", "route_a", "scope_flags", "sources", "collision_audit", "nonclaims",
    "payload_sha256",
}


def q(text: str) -> Q:
    return Q(text)


def payload_hash(data: dict) -> str:
    copy = dict(data)
    copy.pop("payload_sha256", None)
    raw = json.dumps(copy, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def vp(k: int, p: int) -> int:
    answer = 0
    while k and not k % p:
        answer += 1
        k //= p
    return answer


def average_on_cosets(x: np.ndarray, modulus: int) -> np.ndarray:
    # Standalone filtration implementation, not imported from the producer.
    out = np.zeros(x.size, dtype=np.complex128)
    for residue in range(modulus):
        indices = np.arange(residue, x.size, modulus)
        out[indices] = np.sum(x[indices]) / indices.size
    return out


def reconstruct(p: int, level: int, alpha: Q) -> tuple[float, float]:
    order = p**level
    aa = float(alpha)
    j = np.arange(order, dtype=np.float64)
    x = (np.cos((j + 1) * math.sqrt(2))
         + 0.25 * np.sin((j + 2) * math.sqrt(3))
         + 1j * np.cos((j + 3) * math.sqrt(5)))
    symbol = np.array([
        0.0 if k == 0 else p ** (aa * (level - vp(k, p)))
        for k in range(order)
    ])
    fourier = np.fft.ifft(np.fft.fft(x) * symbol)
    filtration = np.zeros(order, dtype=np.complex128)
    old = average_on_cosets(x, 1)
    for n in range(1, level + 1):
        new = average_on_cosets(x, p**n)
        filtration += p ** (aa * n) * (new - old)
        old = new
    trace = sum((p - 1) * p ** (n - 1) * p ** (aa * n)
                for n in range(1, level + 1))
    return float(np.max(np.abs(fourier - filtration))), trace


def heat_double(p: int, alpha: Q, mu: Q, t: Q) -> float:
    aa, mm, tt = float(alpha), float(mu), float(t)
    terms = [1.0]
    for n in range(1, 1000):
        exponent = aa * n * math.log(p)
        eig = math.exp(exponent) if exponent < 700 else math.inf
        term = (p - 1) * p ** (n - 1) * math.exp(-tt * eig)
        terms.append(term)
        if n > 20 and term < 1e-16 and all(x < 1e-14 for x in terms[-6:]):
            return math.exp(-mm * tt) * math.fsum(terms)
    raise RuntimeError("independent heat sum did not settle")


def main() -> None:
    data = json.loads(PATH.read_text())
    assertions = 0

    def ok(value: bool) -> None:
        nonlocal assertions
        assert value
        assertions += 1

    ok(set(data) == EXPECTED_KEYS)
    ok(data["schema"] == "hcs-c283-padic-conductor-shell-heat-v1")
    ok(data["candidate_id"] == "HCS-C283")
    ok(data["evaluation_date"] == "2026-09-01")
    ok(data["source_commit"] == SOURCE)
    ok(data["fixed_epoch"] == 1788220800)
    ok(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    ok(data["evaluator"]["sha256"] == EVALUATOR)
    ok(data["payload_sha256"] == payload_hash(data))
    ok(data["owner"]["normalization"].startswith("explicit Fourier multiplier"))
    ok(data["owner"]["prime_parameter"] == "p is an arbitrary but fixed rational prime")
    ok("A=D+mu*I has mu simple" in data["theorem_contract"]["spectrum"])
    ok(data["theorem_contract"]["schatten"].endswith("equality diverges"))
    ok(data["theorem_contract"]["boundaries"].startswith("alpha=0 gives I-P0"))
    ok(data["route_a"]["tuple"] == [
        "A0_WEAK_ARITHMETIC_RELATION", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"
    ])
    ok(data["route_a"]["overall"] == "ROUTE_A_REJECTED")
    ok(data["route_a"]["route_b_invocation_allowed"] is False)
    for value in data["scope_flags"].values():
        ok(value is False)

    for row in data["regression"]["shell_cells"]:
        p, alpha, n = row["p"], q(row["alpha"]), row["conductor"]
        expected = p ** (float(alpha) * n)
        ok(abs(float(row["eigenvalue"]) - expected) <= 2e-13 * expected)
        ok(row["multiplicity"] == (p - 1) * p ** (n - 1))
        ok(row["cumulative_mean_zero_count"] == p**n - 1)

    for row in data["regression"]["finite_quotient_cells"]:
        p, level, alpha = row["p"], row["level"], q(row["alpha"])
        error, trace = reconstruct(p, level, alpha)
        ok(row["quotient_order"] == p**level)
        ok(abs(float(row["dft_hierarchical_max_error"]) - error) < 2e-12)
        normalized = error / p ** (float(alpha) * level)
        ok(abs(float(row["dft_error_over_top_eigenvalue"]) - normalized) < 2e-15)
        ok(normalized < 2e-14)
        ok(abs(float(row["trace_D"]) - trace) <= 3e-13 * max(1.0, trace))
        ok(row["nonzero_character_count"] == p**level - 1)
        ok(row["top_shell_multiplicity"] == (p - 1) * p ** (level - 1))

    for row in data["regression"]["heat_trace_cells"]:
        expected = heat_double(row["p"], q(row["alpha"]), q(row["mu"]), q(row["t"]))
        observed = float(row["heat_trace"])
        ok(math.isfinite(observed) and observed > 0)
        ok(abs(observed - expected) <= 3e-12 * max(1.0, expected))
        ok(8 <= row["shells_summed"] < 1000)

    for row in data["regression"]["zeta_cells"]:
        p = row["p"]
        alpha, alpha_s = q(row["alpha"]), q(row["alpha_times_s"])
        ok(alpha * float(row["s"]) > 1)
        cc = float(alpha_s)
        ratio = p ** (1 - cc)
        expected = (1 - 1 / p) * ratio / (1 - ratio)
        ok(abs(float(row["closed_value"]) - expected) < 2e-14)
        ok(0 <= float(row["partial_160_error"]) < 2e-24)

    for row in data["regression"]["pole_cells"]:
        p, alpha, k = row["p"], float(q(row["alpha"])), row["k"]
        ok(abs(float(row["real_part"]) - 1 / alpha) < 2e-14)
        ok(abs(float(row["imaginary_part"]) - 2 * math.pi * k / (alpha * math.log(p))) < 3e-13)
        ok(abs(float(row["residue"]) - (1 - 1 / p) / (alpha * math.log(p))) < 3e-14)

    for row in data["regression"]["counting_cells"]:
        p, m = row["p"], row["shell"]
        count = p**m - 1
        ok(row["N_at_eigenvalue"] == count)
        ok(q(row["scaled_ratio_at_eigenvalue"]) == Q(count, p**m))
        ok(q(row["scaled_ratio_before_next_shell"]) == Q(count, p ** (m + 1)))

    for row in data["regression"]["schatten_cells"]:
        product = q(row["alpha"]) * q(row["sigma"]) * q(row["q"])
        ok(q(row["alpha_sigma_q"]) == product)
        ok(row["in_S_q"] is (product > 1))
        ok(row["endpoint_diverges"] is (product == 1))

    for row in data["regression"]["control_cells"]:
        b, m = row["branching"], row["shell"]
        ok(b in (4, 6, 10))
        ok(row["multiplicity"] == (b - 1) * b ** (m - 1))
        ok(row["cumulative_count"] == b**m - 1)
        ok(row["same_closed_form"] is True)

    boundaries = {row["face"]: row for row in data["regression"]["boundaries"]}
    ok(set(boundaries) == {"alpha=0", "mu=0", "t=0", "alpha_to_infinity"})
    ok(boundaries["alpha=0"]["convergence_from_alpha_positive"] == "strong_not_norm")
    ok(boundaries["mu=0"]["determinant_convention"] == "mean_zero_primed")
    ok(boundaries["t=0"]["finite_S_q"] is False)

    expected_counts = {
        "shell_cells": 96, "finite_quotient_cells": 36, "heat_trace_cells": 72,
        "zeta_cells": 36, "pole_cells": 84, "counting_cells": 72,
        "schatten_cells": 27, "control_cells": 15,
    }
    ok(data["regression"]["counts"] == expected_counts)
    ok(sum(expected_counts.values()) == 438)
    dois = {row.get("doi") for row in data["sources"]}
    ok("10.1070/IM2002v066n02ABEH000381" in dois)
    ok("10.1070/RM2014v069n04ABEH004907" in dois)
    ok("10.1090/spmj/1505" in dois)
    ok(len(data["collision_audit"]) == 5)
    print(f"C283 independent checker: PASS ({assertions} assertions; DFT, trace, zeta, counting, Schatten, boundaries)")


if __name__ == "__main__":
    main()
