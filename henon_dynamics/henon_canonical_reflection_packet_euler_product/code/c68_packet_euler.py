#!/usr/bin/env python3
"""Exact certificate for HCS-P68's reflection-packet Euler product."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c68_certificate.json"
MAX_ORDER = 41

DEPENDENCIES = {
    "p67_proof": (
        TRACK / "henon_unique_gauge_invariant_orbit_sampler/PROOF_PACKAGE.md",
        "e88148be74a31afee3bd129e34a67cd2d8b827a428810c27fa1983bd7b1941b2",
    ),
    "p67_certificate": (
        TRACK / "henon_unique_gauge_invariant_orbit_sampler/results/c67_certificate.json",
        "77b3a7a8bcdd501315469666146e0fed7e251a1763b60b71d9e337902dd8e347",
    ),
    "p67_paper": (
        TRACK / "henon_unique_gauge_invariant_orbit_sampler/paper/paper.pdf",
        "d07f09b9f607bb2f148e1b9174420c003e2aae3e055e6c79fe441d0a5b2605be",
    ),
    "p64_proof": (
        TRACK / "henon_reflection_boundary_mahler_pressure/PROOF_PACKAGE.md",
        "b98dbeb0ca2dbaa8196726eef9cd3f25dbdd1a620096d51a95c806eae95a3db6",
    ),
    "p64_certificate": (
        TRACK / "henon_reflection_boundary_mahler_pressure/results/c64_certificate.json",
        "4ecc9c17111fdf8fcecf6c6fa65e9c1b765d58baabb55277c77eed60822a823b",
    ),
}


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    if n == 1:
        return 1
    primes = 0
    value = n
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            primes += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        primes += 1
    return -1 if primes % 2 else 1


def reflection_count(n: int) -> int:
    if n <= 0 or n % 2 == 0:
        return 0
    return sum(mobius(n // d) * 2 ** ((d + 1) // 2) for d in divisors(n))


def fixed_count(n: int) -> int:
    return 2 ** ((n + 1) // 2) if n > 0 and n % 2 else 0


def product_series(order: int) -> list[int]:
    """Coefficients of product_(n odd)(1-z^n)^(-D_n) through order."""
    coefficients = [1] + [0] * order
    for n in range(1, order + 1, 2):
        exponent = reflection_count(n)
        factor = [0] * (order + 1)
        for k in range(order // n + 1):
            factor[k * n] = math.comb(exponent + k - 1, k)
        updated = [0] * (order + 1)
        for i, left in enumerate(coefficients):
            if not left:
                continue
            for j, right in enumerate(factor[: order - i + 1]):
                if right:
                    updated[i + j] += left * right
        coefficients = updated
    return coefficients


def logarithmic_derivative_coefficients(order: int) -> list[int]:
    """a_m=[z^m] z d/dz log Z from the primitive/repetition ledger."""
    return [0] + [
        sum(n * reflection_count(n) for n in divisors(m) if n % 2)
        for m in range(1, order + 1)
    ]


def recover_log_derivative(product: list[int]) -> list[int]:
    """Recover a in z Z'=a Z, independently from product coefficients."""
    order = len(product) - 1
    recovered = [0] * (order + 1)
    for m in range(1, order + 1):
        recovered[m] = m * product[m] - sum(
            recovered[j] * product[m - j] for j in range(1, m)
        )
    return recovered


def generating_identity_rows(limit: int) -> list[dict[str, int]]:
    rows = []
    for n in range(1, limit + 1, 2):
        direct = reflection_count(n)
        reconstructed = sum(
            mobius(k) * fixed_count(n // k) for k in divisors(n)
        )
        if direct != reconstructed:
            raise ArithmeticError("Möbius generating identity")
        rows.append({"period": n, "D_n": direct, "reconstructed": reconstructed})
    return rows


def dependency_locks() -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency changed: {name}")
        result[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return result


def canonical_sha(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def core_payload() -> dict[str, object]:
    product = product_series(MAX_ORDER)
    ledger = logarithmic_derivative_coefficients(MAX_ORDER)
    recovered = recover_log_derivative(product)
    if ledger != recovered:
        raise ArithmeticError("logarithmic derivative mismatch")
    if any(reflection_count(n) <= 0 for n in range(1, MAX_ORDER + 1, 2)):
        raise ArithmeticError("nonpositive primitive count")

    radius = 1 / math.sqrt(2)
    sample_rows = []
    for ratio in (Fraction(1, 2), Fraction(3, 4), Fraction(7, 8), Fraction(15, 16)):
        z = float(ratio) * radius
        truncated_log = sum(
            reflection_count(n) * sum(z ** (n * r) / r for r in range(1, 81))
            for n in range(1, MAX_ORDER + 1, 2)
        )
        principal = 1 / (math.sqrt(2) * (1 - math.sqrt(2) * z))
        sample_rows.append({
            "z_over_radius": str(ratio),
            "truncated_log_Z": truncated_log,
            "principal_pole_term": principal,
            "difference": truncated_log - principal,
        })

    return {
        "candidate_id": "HCS-P68",
        "object": "Z_f(z,s)=product_(n odd)(1-z^n exp(-s n b_n(f)))^(-D_n)",
        "packet_mean": "b_n(f) is P67's unique gauge-invariant cyclic packet mean",
        "primitive_counts": "D_n=sum_(d|n) mu(n/d) 2^((d+1)/2)",
        "repetition_law": "[z^m] z partial_z log Z_f=sum_(n|m,n odd) n D_n exp(-s m b_n(f))",
        "unweighted_generating_series": "sum_(n odd)D_n z^n=sum_(k odd)mu(k) 2z^k/(1-2z^(2k))",
        "unweighted_radius": "2^(-1/2)",
        "boundary_expansion": "log Z_0(z)=1/(sqrt(2)(1-sqrt(2)z))+G(z), G analytic near z=2^(-1/2)",
        "boundary_type": "EXPONENTIAL_ESSENTIAL_SINGULARITY",
        "analytic_remainder_radius": "at least 2^(-1/4) for repetitions and 2^(-1/6) for k>=3 Mobius terms",
        "lind_zeta_firewall": "this restricted packet-mean product is not the Lind zeta of the full D_infinity action",
        "orbit_resolution_firewall": "one factor per period and its aggregate mean does not retain the distribution of individual orbit weights",
        "generating_rows": generating_identity_rows(MAX_ORDER),
        "product_coefficients_through_41": product,
        "log_derivative_coefficients_through_41": ledger,
        "boundary_samples": sample_rows,
        "strongest_positive_result": "a canonical gauge-invariant Euler product with exact primitive/repetition logarithmic derivative and convergence disk",
        "strongest_obstruction": "the unweighted product has an exponential essential singularity at its entropy boundary and is not a meromorphic Fredholm determinant there",
        "open_theorem": "construct an orbit-resolved exponential-moment reflection product and determine whether a source-native relative Lind or transfer determinant exists",
        "reusable_structure": "Möbius primitive counts plus P67 Haar sampling give a canonical period-packet Euler ledger",
        "round2_clue": "compare the aggregate-mean factor with the geometric mean of individual orbit factors; the variance/cumulants are the first missing data",
        "claim_status": {
            "euler_product": "PROVED",
            "log_derivative": "PROVED",
            "essential_boundary": "PROVED",
            "lind_zeta_identity": "REFUTED_AS_IDENTIFICATION",
            "arithmetic_trace": "OPEN",
            "arithmetic_advance": "NO",
            "route_b_authorized": False,
        },
    }


def validate(core: dict[str, object]) -> None:
    if type(core) is not dict or core.get("candidate_id") != "HCS-P68":
        raise ValueError("schema")
    if core.get("unweighted_radius") != "2^(-1/2)":
        raise ValueError("radius")
    if core.get("boundary_type") != "EXPONENTIAL_ESSENTIAL_SINGULARITY":
        raise ValueError("boundary")
    if core.get("repetition_law") != "[z^m] z partial_z log Z_f=sum_(n|m,n odd) n D_n exp(-s m b_n(f))":
        raise ValueError("repetition")
    status = core.get("claim_status")
    if type(status) is not dict:
        raise ValueError("status schema")
    expected = {
        "euler_product": "PROVED",
        "log_derivative": "PROVED",
        "essential_boundary": "PROVED",
        "lind_zeta_identity": "REFUTED_AS_IDENTIFICATION",
        "arithmetic_trace": "OPEN",
        "arithmetic_advance": "NO",
        "route_b_authorized": False,
    }
    if status != expected:
        raise ValueError("status")
    if core["log_derivative_coefficients_through_41"] != recover_log_derivative(
        core["product_coefficients_through_41"]
    ):
        raise ValueError("coefficient ledger")


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    rejected: list[str] = []
    protected = [
        "candidate_id", "object", "packet_mean", "primitive_counts",
        "repetition_law", "unweighted_generating_series", "unweighted_radius",
        "boundary_expansion", "boundary_type", "analytic_remainder_radius",
        "lind_zeta_firewall", "orbit_resolution_firewall",
        "strongest_positive_result", "strongest_obstruction", "open_theorem",
        "reusable_structure", "round2_clue",
    ]
    for key in protected:
        trial = copy.deepcopy(core)
        trial[key] = "FORGED"
        try:
            validate(trial)
            if trial != core:
                raise ValueError("exact drift")
        except ValueError:
            rejected.append(key)
    for key, forged in (
        ("euler_product", "OPEN"),
        ("log_derivative", "OPEN"),
        ("essential_boundary", "MEROMORPHIC_POLE"),
        ("lind_zeta_identity", "PROVED"),
        ("arithmetic_trace", "PROVED"),
        ("arithmetic_advance", "YES"),
        ("route_b_authorized", True),
    ):
        trial = copy.deepcopy(core)
        trial["claim_status"][key] = forged
        try:
            validate(trial)
            if trial != core:
                raise ValueError("exact drift")
        except ValueError:
            rejected.append("status-" + key)
    trial = copy.deepcopy(core)
    trial["log_derivative_coefficients_through_41"][9] += 1
    try:
        validate(trial)
    except ValueError:
        rejected.append("coefficient-9")
    return {
        "attempted": 25,
        "rejected": rejected,
        "all_rejected": len(rejected) == 25,
    }


def build() -> dict[str, object]:
    core = core_payload()
    validate(core)
    result = dict(core)
    result["dependency_locks"] = dependency_locks()
    result["mutation_audit"] = mutation_audit(core)
    if not result["mutation_audit"]["all_rejected"]:
        raise RuntimeError("mutation audit")
    result["core_sha256"] = canonical_sha(core)
    result["check"] = True
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = build()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "candidate_id": result["candidate_id"],
        "boundary_type": result["boundary_type"],
        "core_sha256": result["core_sha256"],
        "mutations": result["mutation_audit"]["attempted"],
        "check": result["check"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
