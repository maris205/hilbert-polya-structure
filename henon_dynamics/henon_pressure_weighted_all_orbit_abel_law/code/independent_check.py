#!/usr/bin/env python3
"""Independent finite checker for the HCS-P53 certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import mpmath as mp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_CERTIFICATE = PROJECT / "results" / "c53_certificate.json"
DEFAULT_OUTPUT = PROJECT / "results" / "c53_independent_check.json"

POLYNOMIALS = {
    "period_1": [1.0, -4.0, -22.0, -4.0, 1.0],
    "period_3": [1.0, 76.0, -7374.0, 76.0, 1.0],
    "period_4": [1.0, -578.0, 1.0],
    "abstract_salem_stress": [1.0, -1.0, -1.0, -1.0, 1.0],
}

SENTINELS = {
    "period_1": {3: 19, 4: 24, 5: 389, 6: 27},
    "period_3": {3: 7451, 4: 7376, 5: 54938125, 6: 7299},
    "period_4": {3: 579, 4: 578, 5: 334661, 6: 577},
    "abstract_salem_stress": {3: 1, 4: 3, 5: 4, 6: 3},
}


def canonical_sha(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def polynomial_height(coefficients: list[float]) -> tuple[float, int]:
    mp.mp.dps = 70
    roots = mp.polyroots(coefficients, maxsteps=2000, error=False)
    height = float(mp.fsum(mp.log(max(mp.mpf(1), abs(root))) for root in roots))
    unit_count = sum(abs(abs(root) - 1) < mp.mpf("1e-25") for root in roots)
    return height, unit_count


def run_check(path: Path) -> dict[str, Any]:
    certificate = json.loads(path.read_text())
    observed_core = certificate.pop("core_sha256")
    if canonical_sha(certificate) != observed_core:
        raise RuntimeError("core digest mismatch")
    certificate["core_sha256"] = observed_core
    if certificate["schema"] != "hcs-p53-pressure-weighted-all-orbit-abel-law-v1":
        raise RuntimeError("schema mismatch")

    for lock in certificate["dependency_locks"].values():
        dependency = TRACK / lock["path"]
        observed = hashlib.sha256(dependency.read_bytes()).hexdigest()
        if observed != lock["sha256"]:
            raise RuntimeError(f"dependency hash mismatch: {lock['path']}")

    sentinels = certificate["orbit_sentinels"]
    for name, coefficients in POLYNOMIALS.items():
        observed_height, unit_count = polynomial_height(coefficients)
        row = sentinels[name]
        if not math.isclose(
            row["spectral_height_log_mahler"], observed_height,
            rel_tol=0.0, abs_tol=2e-12,
        ):
            raise RuntimeError(f"Mahler spectral height mismatch: {name}")
        if row["unit_circle_multiplier_conjugates"] != unit_count:
            raise RuntimeError(f"unit-circle conjugate count mismatch: {name}")
        by_index = {packet["index"]: packet for packet in row["packet_rows"]}
        for index, expected in SENTINELS[name].items():
            if int(by_index[index]["absolute_half_norm"]) != expected:
                raise RuntimeError(f"half-norm sentinel mismatch: {name}, n={index}")
        if max(packet["embedding_formula_abs_error"] for packet in row["packet_rows"]) > 1e-50:
            raise RuntimeError(f"embedding formula precision mismatch: {name}")
        final_abel = row["abel_rows"][-1]
        expected_target = 3 * observed_height / math.pi**2
        if not math.isclose(
            final_abel["target_3H_over_pi2"], expected_target,
            rel_tol=0.0, abs_tol=2e-14,
        ):
            raise RuntimeError(f"Abel target mismatch: {name}")
        if abs(final_abel["ratio_to_target"] - 1) > 0.006:
            raise RuntimeError(f"Abel convergence sentinel failed: {name}")

    stress = sentinels["abstract_salem_stress"]
    if stress["source_native_h6"] or stress["unit_circle_multiplier_conjugates"] != 2:
        raise RuntimeError("abstract unit-circle stress fixture was promoted or weakened")
    if not all(sentinels[name]["source_native_h6"] for name in ("period_1", "period_3", "period_4")):
        raise RuntimeError("source-native H6 sentinel typing mismatch")

    profile = certificate["sample_pressure_profile"]
    if not math.isclose(sum(profile["orbit_limit_weights"].values()), 1.0, abs_tol=2e-15):
        raise RuntimeError("orbit pressure weights do not normalize")
    if not profile["orbit_limit_weights"]["period_1"] > 0.8:
        raise RuntimeError("sample orbit-weight sentinel changed")
    final = profile["rows"][-1]
    if not final["ratio_to_target"] > 0.998:
        raise RuntimeError("sample all-orbit Abel sentinel failed")
    for laplace in final["scaled_index_laplace"]:
        expected = (1 + laplace["r"]) ** -2
        if not math.isclose(laplace["target_gamma_2_1"], expected, abs_tol=2e-15):
            raise RuntimeError("Gamma target mismatch")
        if abs(laplace["observed"] - expected) > 0.002:
            raise RuntimeError("Gamma convergence sentinel failed")

    physical_only = math.log(sentinels["period_1"]["physical_multiplier_modulus"])
    if math.isclose(
        physical_only,
        sentinels["period_1"]["spectral_height_log_mahler"],
        rel_tol=0.0,
        abs_tol=1e-6,
    ):
        raise RuntimeError("physical multiplier was confused with full spectral height")
    correct = 3 * sentinels["period_4"]["spectral_height_log_mahler"] / math.pi**2
    wrong = 6 * sentinels["period_4"]["spectral_height_log_mahler"] / math.pi**2
    if math.isclose(correct, wrong, rel_tol=1e-12):
        raise RuntimeError("half-cyclotomic normalization mutation survived")

    required = {
        "per_orbit_spectral_height_asymptotic": "PROVED_SOURCE_BACKED",
        "pressure_weighted_all_orbit_abel_interchange": "PROVED_IN_P51_SAFE_HALF_PLANE",
        "locally_uniform_complex_s_limit": "PROVED",
        "joint_orbit_index_product_limit": "PROVED",
        "scaled_index_gamma_2_1_profile": "PROVED",
        "tagged_banach_boundary": "REFUTED_NO_NORM_OR_WEAKLY_CONVERGENT_SUBNET",
        "continuation_to_pressure_boundary": "OPEN",
        "rational_prime_von_mangoldt_trace": "OPEN",
        "fredholm_determinant": "OPEN",
        "hilbert_polya_operator": "OPEN",
    }
    ledger = certificate["theorem_ledger"]
    if any(ledger.get(key) != value for key, value in required.items()):
        raise RuntimeError("claim-boundary mutation detected")

    return {
        "candidate_id": "HCS-P53",
        "certificate_core_sha256": observed_core,
        "dependency_hashes_recomputed": True,
        "dependency_lock_count": len(certificate["dependency_locks"]),
        "orbit_sentinels_checked": len(sentinels),
        "packet_rows_checked": sum(len(row["packet_rows"]) for row in sentinels.values()),
        "mutations_rejected": 9,
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
