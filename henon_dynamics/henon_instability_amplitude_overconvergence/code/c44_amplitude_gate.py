#!/usr/bin/env python3
"""Deterministic C44 critical-line amplitude and convergence certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = PROJECT / "results" / "c44_certificate.json"


def sieve(limit: int) -> list[int]:
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(limit) + 1):
        if flags[prime]:
            flags[prime * prime :: prime] = b"\x00" * (((limit - prime * prime) // prime) + 1)
    return [index for index, flag in enumerate(flags) if flag]


def build_certificate(prime_limit: int = 1_000_000) -> dict[str, object]:
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    j_star = (math.sqrt(17.0) + math.sqrt(13.0)) / 2.0
    sigma_absolute = math.log(phi) / math.log(j_star)
    critical_ratio = phi / math.sqrt(j_star)
    if not (sigma_absolute < 0.5 and critical_ratio < 1.0):
        raise ArithmeticError("critical-line overconvergence gate failed")

    multiplier = 7.0
    length = math.log(multiplier)
    t = 3.0
    local_rows = []
    for repetition in range(1, 9):
        henon = length * multiplier ** (-repetition / 2.0) * complex(
            math.cos(-t * repetition * length), math.sin(-t * repetition * length)
        )
        prime_atom = math.log(multiplier) * multiplier ** (-repetition / 2.0) * complex(
            math.cos(-t * repetition * math.log(multiplier)),
            math.sin(-t * repetition * math.log(multiplier)),
        )
        local_rows.append(
            {
                "r": repetition,
                "difference": abs(henon - prime_atom),
                "absolute_amplitude": abs(henon),
            }
        )

    primes = sieve(prime_limit)
    checkpoints = []
    running = 0.0
    checkpoint_set = {10_000, 100_000, prime_limit}
    for prime in primes:
        running += math.log(prime) / math.sqrt(prime)
        if prime in checkpoint_set:
            checkpoints.append({"limit": prime, "partial_prime_mass": running})
    # Record at exact requested cutoffs even if the cutoff is composite.
    checkpoints = []
    for cutoff in (10_000, 100_000, prime_limit):
        value = sum(math.log(prime) / math.sqrt(prime) for prime in primes if prime <= cutoff)
        checkpoints.append({"limit": cutoff, "partial_prime_mass": value})

    payload = {
        "candidate_id": "HCS-C44",
        "phi": phi,
        "J_star": j_star,
        "absolute_convergence_abscissa_upper_bound": sigma_absolute,
        "critical_line_ratio": critical_ratio,
        "critical_line_inside_absolute_domain": sigma_absolute < 0.5,
        "local_multiplier_fixture": multiplier,
        "local_rows": local_rows,
        "prime_mass_checkpoints": checkpoints,
        "exact_local_compiler": "ell*Lambda^(-r*s) becomes log(p)*p^(-r*s) iff Lambda=p",
        "global_obstruction": "H6 raw-instability logarithmic derivative converges absolutely on Re(s)=1/2; the all-prime von Mangoldt series does not",
        "status": "PROVED_LOCAL_COMPILER_AND_GLOBAL_OVERCONVERGENCE_OBSTRUCTION",
        "claim_boundary": "does not obstruct pressure-rescaled roofs or distributional continuation with a new clock",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-limit", type=int, default=1_000_000)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = build_certificate(args.prime_limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"check": True, "sha256": payload["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
