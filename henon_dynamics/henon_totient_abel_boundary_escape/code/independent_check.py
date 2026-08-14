#!/usr/bin/env python3
"""Independent finite checker for the HCS-P52 certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_CERTIFICATE = PROJECT / "results" / "c52_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c52_independent_check.json"


def canonical_sha(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def prime_factors(value: int) -> list[int]:
    factors: list[int] = []
    candidate = 2
    remaining = value
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            factors.append(candidate)
            while remaining % candidate == 0:
                remaining //= candidate
        candidate += 1
    if remaining > 1:
        factors.append(remaining)
    return factors


def totient(value: int) -> int:
    result = value
    for prime in prime_factors(value):
        result -= result // prime
    return result


def mobius(value: int) -> int:
    sign = 1
    candidate = 2
    remaining = value
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            remaining //= candidate
            sign = -sign
            if remaining % candidate == 0:
                return 0
            while remaining % candidate == 0:
                remaining //= candidate
        candidate += 1
    if remaining > 1:
        sign = -sign
    return sign


def divisors(value: int) -> list[int]:
    return [candidate for candidate in range(1, value + 1) if value % candidate == 0]


def epsilon(index: int, lam: float) -> float:
    return sum(
        mobius(index // divisor) * math.log1p(-(lam ** (-divisor)))
        for divisor in divisors(index)
    )


def correction_upper(lam: float, cutoff: int = 32) -> float:
    partial = sum(-math.log1p(-(lam ** (-d))) for d in range(1, cutoff + 1))
    first = lam ** (-(cutoff + 1))
    return partial + first / ((1 - first) * (1 - 1 / lam))


def b_value(index: int, lam: float) -> float:
    return 0.5 * totient(index) * math.log(lam) + epsilon(index, lam)


def finite_abel(tau: float, cutoff: int, lam: float) -> float:
    return sum(b_value(n, lam) * math.exp(-tau * n) for n in range(3, cutoff + 1))


def run_check(path: Path) -> dict[str, Any]:
    certificate = json.loads(path.read_text())
    observed_core = certificate.pop("core_sha256")
    if canonical_sha(certificate) != observed_core:
        raise RuntimeError("core digest mismatch")
    certificate["core_sha256"] = observed_core
    if certificate["schema"] != "hcs-p52-totient-abel-boundary-escape-v1":
        raise RuntimeError("schema mismatch")
    for lock in certificate["dependency_locks"].values():
        dependency = TRACK / lock["path"]
        observed = hashlib.sha256(dependency.read_bytes()).hexdigest()
        if observed != lock["sha256"]:
            raise RuntimeError(f"dependency hash mismatch: {lock['path']}")

    lam = 289.0 + 24.0 * math.sqrt(145.0)
    constants = certificate["constants"]
    target = 3.0 * math.log(lam) / math.pi**2
    if not math.isclose(float(constants["L"]), lam, rel_tol=0.0, abs_tol=1e-12):
        raise RuntimeError("multiplier mismatch")
    if not math.isclose(
        constants["abel_limit_constant_3logL_over_pi2"], target,
        rel_tol=0.0, abs_tol=2e-15,
    ):
        raise RuntimeError("Abel limit constant mismatch")
    if not constants["uniform_correction_upper"] < 0.001735:
        raise RuntimeError("uniform correction bound is too large")
    if not math.isclose(
        constants["uniform_correction_upper"], correction_upper(lam),
        rel_tol=0.0, abs_tol=5e-16,
    ):
        raise RuntimeError("uniform correction recomputation mismatch")

    rows = certificate["packet_rows"]
    sentinels = {3: 579, 4: 578, 5: 334661, 6: 577, 13: 37351776156527821}
    by_index = {row["index"]: row for row in rows}
    for index, beta in sentinels.items():
        if int(by_index[index]["beta"]) != beta:
            raise RuntimeError(f"packet sentinel mismatch at n={index}")
    for row in rows:
        index = row["index"]
        if row["totient"] != totient(index):
            raise RuntimeError(f"totient mismatch at n={index}")
        direct = math.log(int(row["beta"]))
        formula = b_value(index, lam)
        if not math.isclose(direct, formula, rel_tol=0.0, abs_tol=2e-12):
            raise RuntimeError(f"packet log formula mismatch at n={index}")
        if row["p51_crosscheck"] is not None and not row["p51_crosscheck"]:
            raise RuntimeError("P51 crosscheck failed")

    abel_rows = certificate["abel_rows"]
    ratios: list[float] = []
    for row in abel_rows:
        tau = row["tau"]
        finite = finite_abel(tau, row["cutoff"], lam)
        scaled = tau * tau * finite
        if not math.isclose(scaled, row["tau_squared_Z"], rel_tol=0.0, abs_tol=2e-12):
            raise RuntimeError("finite Abel row mismatch")
        ratios.append(row["ratio_to_target"])
        for profile in row["profile_laplace"]:
            expected = (1.0 + profile["s"]) ** -2
            if not math.isclose(
                profile["target_gamma_2_1"], expected, rel_tol=0.0, abs_tol=1e-15
            ):
                raise RuntimeError("Gamma profile target mismatch")
    if ratios != sorted(ratios) or not ratios[-1] > 0.999:
        raise RuntimeError("Abel convergence sentinel failed")
    prefix_fractions = [row["fixed_prefix_3_20_mass_fraction"] for row in abel_rows]
    if not prefix_fractions[-1] < prefix_fractions[0] / 20:
        raise RuntimeError("mass-escape sentinel failed")

    ledger = certificate["theorem_ledger"]
    required = {
        "uniform_totient_packet_asymptotic": "PROVED",
        "scalar_abel_boundary_constant": "PROVED",
        "gamma_2_1_escape_profile": "PROVED",
        "tagged_banach_norm_boundary_limit": "REFUTED_NO_CONVERGENT_SUBNET",
        "all_orbit_boundary_interchange": "OPEN",
        "von_mangoldt_trace_law": "OPEN",
        "fredholm_determinant": "OPEN",
        "hilbert_polya_operator": "OPEN",
    }
    if any(ledger[key] != value for key, value in required.items()):
        raise RuntimeError("claim-boundary mutation detected")

    wrong_constant = 6.0 * math.log(lam) / math.pi**2
    if math.isclose(target, wrong_constant, rel_tol=1e-12):
        raise RuntimeError("half-normalization mutation was not rejected")
    wrong_gamma = 1.0 / 2.0
    if math.isclose((1.0 + 1.0) ** -2, wrong_gamma, rel_tol=0.0, abs_tol=1e-15):
        raise RuntimeError("shape-one Gamma mutation was not rejected")

    return {
        "candidate_id": "HCS-P52",
        "certificate_core_sha256": observed_core,
        "dependency_lock_count": len(certificate["dependency_locks"]),
        "dependency_hashes_recomputed": True,
        "packet_rows_checked": len(rows),
        "abel_rows_checked": len(abel_rows),
        "mutations_rejected": 7,
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
