#!/usr/bin/env python3
"""Deterministic controls for packet-wise trace normalizations.

The script never uses Riemann-zero data. Rational primes enter only as the
closed-point indices of Spec(Z), after the trace ambiguity has been stated.
Its outputs illustrate exact formulas proved in the accompanying manuscript;
they are not evidence for the existence of a dynamical trace.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for candidate in range(2, math.isqrt(limit) + 1):
        if sieve[candidate]:
            start = candidate * candidate
            sieve[start : limit + 1 : candidate] = b"\x00" * (
                (limit - start) // candidate + 1
            )
    return [n for n in range(2, limit + 1) if sieve[n]]


def packet_mass(model: str, prime: int) -> float:
    if model == "unit":
        return 1.0
    if model == "decay_half":
        return prime ** -0.5
    if model == "growth_linear":
        return float(prime)
    if model == "reciprocal":
        return 1.0 / prime
    if model == "mod4_sign":
        if prime == 2:
            return 0.0
        return 1.0 if prime % 4 == 1 else -1.0
    raise ValueError(f"unknown packet-mass model: {model}")


def packet_log_product(primes: Iterable[int], sigma: float, model: str) -> float:
    """Return log(prod_p (1-p^-sigma)^(-c_p)) for a finite cutoff."""
    return sum(
        -packet_mass(model, prime) * math.log1p(-(prime ** -sigma))
        for prime in primes
    )


def first_return_mass(primes: Iterable[int], sigma: float, model: str) -> float:
    """Return sum_p |c_p| p^-sigma, the absolute first-return majorant."""
    return sum(abs(packet_mass(model, prime)) * prime ** -sigma for prime in primes)


def write_csv(path: Path, fieldnames: list[str], rows: Iterable[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def run(output_dir: Path, max_prime: int) -> dict[str, object]:
    primes = primes_up_to(max_prime)
    cutoffs = sorted(set(value for value in (100, 1_000, 10_000, max_prime) if value <= max_prime))
    sigmas = (0.75, 1.0, 1.25, 1.5, 2.25)
    models = ("unit", "decay_half", "growth_linear", "reciprocal", "mod4_sign")

    multiplicity_path = output_dir / "orbit_multiplicity_divergence.csv"
    write_csv(
        multiplicity_path,
        ["prime", "sigma", "orbit_count", "log_orbitwise_zeta"],
        (
            {
                "prime": prime,
                "sigma": sigma,
                "orbit_count": count,
                "log_orbitwise_zeta": f"{-count * math.log1p(-(prime ** -sigma)):.17g}",
            }
            for prime in (2, 3, 5)
            for sigma in (1.25, 2.0)
            for count in (1, 2, 4, 8, 16, 32, 64, 128)
        ),
    )

    sensitivity_path = output_dir / "packet_weight_sensitivity.csv"
    sensitivity_rows: list[dict[str, object]] = []
    for cutoff in cutoffs:
        prefix = [prime for prime in primes if prime <= cutoff]
        for sigma in sigmas:
            for model in models:
                sensitivity_rows.append(
                    {
                        "prime_cutoff": cutoff,
                        "prime_count": len(prefix),
                        "sigma": sigma,
                        "mass_model": model,
                        "finite_log_product": f"{packet_log_product(prefix, sigma, model):.17g}",
                        "absolute_first_return_mass": f"{first_return_mass(prefix, sigma, model):.17g}",
                    }
                )
    write_csv(
        sensitivity_path,
        [
            "prime_cutoff",
            "prime_count",
            "sigma",
            "mass_model",
            "finite_log_product",
            "absolute_first_return_mass",
        ],
        sensitivity_rows,
    )

    repetition_path = output_dir / "packet_repetition_ledger.csv"
    write_csv(
        repetition_path,
        ["prime", "repetition", "mass_model", "packet_mass", "minus_log_derivative_term_at_s_1"],
        (
            {
                "prime": prime,
                "repetition": repetition,
                "mass_model": model,
                "packet_mass": f"{packet_mass(model, prime):.17g}",
                "minus_log_derivative_term_at_s_1": f"{packet_mass(model, prime) * math.log(prime) * prime ** (-repetition):.17g}",
            }
            for prime in primes[:10]
            for repetition in range(1, 6)
            for model in ("unit", "decay_half", "growth_linear")
        ),
    )

    copied_path = output_dir / "copied_packet_control.csv"
    write_csv(
        copied_path,
        ["prime", "sigma", "copies", "single_packet_log_term", "additive_log_term"],
        (
            {
                "prime": prime,
                "sigma": sigma,
                "copies": copies,
                "single_packet_log_term": f"{-math.log1p(-(prime ** -sigma)):.17g}",
                "additive_log_term": f"{-copies * math.log1p(-(prime ** -sigma)):.17g}",
            }
            for prime in primes[:10]
            for sigma in (1.25, 2.0)
            for copies in (1, 2, 3)
        ),
    )

    artifacts = [multiplicity_path, sensitivity_path, repetition_path, copied_path]
    manifest = {
        "schema": "packet-trace-controls/1",
        "max_prime": max_prime,
        "prime_count": len(primes),
        "sigmas": list(sigmas),
        "mass_models": list(models),
        "forbidden_data": ["Riemann zeros", "fitted packet masses", "fitted scales"],
        "interpretation_boundary": (
            "Finite deterministic illustrations of normalization sensitivity; "
            "not a construction or validation of a dynamical trace."
        ),
        "artifacts": {path.name: sha256(path) for path in artifacts},
    }
    manifest_path = output_dir / "packet_trace_controls_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--max-prime", type=int, default=100_000)
    args = parser.parse_args()
    if args.max_prime < 100:
        parser.error("--max-prime must be at least 100")
    manifest = run(args.output_dir, args.max_prime)
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
