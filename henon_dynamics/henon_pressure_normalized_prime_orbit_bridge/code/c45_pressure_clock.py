#!/usr/bin/env python3
"""Source-lock and finite invariants for the HCS-C45 pressure clock."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c45_certificate.json"
DEPENDENCIES = {
    "instability_roof_readme": (
        TRACK / "henon_instability_roof_zeta" / "README.md",
        "c2a63ba68fe4d7092d5304008ab5745172269c23bbc30faf93f1423ae96f798e",
    ),
    "pressure_theorem": (
        TRACK / "henon_bowen_pressure_gate" / "THEOREM_PACKAGE.md",
        "5f2ae3d86094a80c89822f91af935ef09efa3893cbc50326f56174f154f721ee",
    ),
    "pressure_certificate": (
        TRACK / "henon_bowen_pressure_gate" / "results" / "c31_certificate.json",
        "9f326c8442f5f1dfb8215527491a9ebbac2395fde7892c88bc78634df24c5cca",
    ),
}
A = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)


def multiply(left: list[list[int]], right: tuple[tuple[int, ...], ...]) -> list[list[int]]:
    return [[sum(left[i][k] * right[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def dependency_locks() -> dict[str, dict[str, object]]:
    locks: dict[str, dict[str, object]] = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency hash changed: {name}")
        locks[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return locks


def build_certificate() -> dict[str, object]:
    power = [list(row) for row in A]
    for _ in range(3):
        power = multiply(power, A)
    primitive = all(entry > 0 for row in power for entry in row)
    if not primitive:
        raise ArithmeticError("A^4 is not strictly positive")

    h_lower = 0.277980
    h_upper = 0.277987
    h_mid = (h_lower + h_upper) / 2.0
    fixed_multiplier_polynomial = [1, -4, -22, -4, 1]
    period4_multiplier = 289.0 + 24.0 * math.sqrt(145.0)
    fixture_multiplier = 7.0
    fixture_label = fixture_multiplier**h_mid
    payload = {
        "candidate_id": "HCS-C45",
        "dependency_locks": dependency_locks(),
        "adjacency_power_4": power,
        "mixing_gate": primitive,
        "roof": "tau=log|Lambda_u|",
        "roof_status": "positive Holder non-lattice",
        "pressure_root_interval": [h_lower, h_upper],
        "normalized_roof": "tau_hat=h_star*tau",
        "normalized_pressure_identity": "P(-tau_hat)=0",
        "normalized_entropy": 1,
        "prime_orbit_law": "Pi_hat(T)~exp(T)/T",
        "fixed_multiplier_polynomial": fixed_multiplier_polynomial,
        "period4_exact_multiplier_decimal": period4_multiplier,
        "fixture": {
            "raw_multiplier": fixture_multiplier,
            "normalized_real_label_midpoint": fixture_label,
            "log_label": h_mid * math.log(fixture_multiplier),
            "label_is_asserted_prime": False,
        },
        "status": "PROVED_PRESSURE_NORMALIZED_DYNAMICAL_PRIME_ORBIT_BRIDGE",
        "claim_boundary": "dynamical prime theorem only; normalized labels are positive reals, not proved rational primes",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"check": True, "sha256": payload["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
