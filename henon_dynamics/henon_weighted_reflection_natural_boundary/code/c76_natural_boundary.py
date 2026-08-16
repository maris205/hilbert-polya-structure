#!/usr/bin/env python3
"""Exact weighted singular-circle certificate for HCS-P76."""

from __future__ import annotations

import argparse
import cmath
import copy
import hashlib
import json
import math
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results/c76_certificate.json"
CHANNEL_ORDER = 40

DEPENDENCIES = {
    "p75_proof": (
        TRACK / "henon_weighted_reflection_channel_divisor/PROOF_PACKAGE.md",
        "f2ee916354ef0c4e7ecd9693826d33752510faf9e7892faf690a56333771ddd4",
    ),
    "p75_certificate": (
        TRACK / "henon_weighted_reflection_channel_divisor/results/c75_certificate.json",
        "2bcae20706f6061636ee9d327810eaf9501e30e8c1583cbc7af860938cc98464",
    ),
    "p75_paper": (
        TRACK / "henon_weighted_reflection_channel_divisor/paper/paper.pdf",
        "da68d4cfea785e121ffff960bebf10a5c0ee5b2ace20f0b81bc81c0c9aa3aa8f",
    ),
    "p70_proof": (
        TRACK / "henon_orbit_resolved_reflection_euler_boundary/PROOF_PACKAGE.md",
        "416fe1466c7dcaeb35c4ab85d4a1cd329e00f9c961c09d490dbbc77a4f1c1a1e",
    ),
    "p70_certificate": (
        TRACK / "henon_orbit_resolved_reflection_euler_boundary/results/c70_certificate.json",
        "35abf7ee3500b8263b885d424644665e3a5a124fdc43ea5d3a933d43cfe16e3c",
    ),
    "p70_paper": (
        TRACK / "henon_orbit_resolved_reflection_euler_boundary/paper/paper.pdf",
        "ab040dceedfaa0db53f55a10c34ebc2a838d999b1e40c0bcde19b591f37fe7de",
    ),
    "p72_proof": (
        TRACK / "henon_relative_lind_essential_ladder/PROOF_PACKAGE.md",
        "b0390d8b8a10160ea0958a4594b54a320566f9f7e0c26138aca11112f33bf018",
    ),
    "p72_certificate": (
        TRACK / "henon_relative_lind_essential_ladder/results/c72_certificate.json",
        "a311c84c88a2cf798767c35e200f3f77de8424f63fa1827472b3f2f81fb772f8",
    ),
    "p72_paper": (
        TRACK / "henon_relative_lind_essential_ladder/paper/paper.pdf",
        "4c89c65983c0d867bd8bb3130c5176705d8e1d05876d7cc67f8b26c77433a5b1",
    ),
}


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    value, primes, p = n, 0, 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            primes += 1
            if value % p == 0:
                return 0
        p += 1
    if value > 1:
        primes += 1
    return -1 if primes % 2 else 1


def odd_prime_divisors(n: int) -> list[int]:
    while n % 2 == 0:
        n //= 2
    out, p = [], 3
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        out.append(n)
    return out


def c_divisor(m: int) -> Fraction:
    return sum(Fraction(k * mobius(k), m) for k in divisors(m) if k % 2)


def c_euler(m: int) -> Fraction:
    numerator = math.prod(1 - p for p in odd_prime_divisors(m))
    return Fraction(numerator, m)


def radius(m: int, q: float) -> float:
    if m < 1 or q <= 0:
        raise ValueError("m positive and q positive required")
    exponent = 2 * m * math.log(q)
    log_denominator = max(0.0, exponent) + math.log1p(math.exp(-abs(exponent)))
    return math.exp(-log_denominator / (2 * m))


def radius_decimal(m: int, q: float | str) -> Decimal:
    if m < 1 or Decimal(str(q)) <= 0:
        raise ValueError("m positive and q positive required")
    with localcontext() as context:
        context.prec = 100
        qd = Decimal(str(q))
        return (-(Decimal(1) + qd ** (2 * m)).ln() / Decimal(2 * m)).exp()


def limiting_radius(q: float) -> float:
    if q <= 0:
        raise ValueError("q positive required")
    return min(1.0, 1.0 / q)


def root(m: int, k: int, q: float) -> complex:
    return radius(m, q) * cmath.exp(1j * math.pi * k / m)


def denominator(z: complex, m: int, q: float) -> complex:
    return 1 - (1 + q ** (2 * m)) * z ** (2 * m)


def principal_coefficient(m: int, k: int, q: float) -> float:
    """Multiplier of (1-z/alpha)^(-1) in log Z."""
    return (
        float(c_euler(m))
        * ((-1) ** k)
        * q**m
        / (m * math.sqrt(1 + q ** (2 * m)))
    )


def channel_row(m: int, q: float) -> dict[str, object]:
    coefficient = c_euler(m)
    if coefficient != c_divisor(m) or coefficient == 0:
        raise ArithmeticError("channel coefficient")
    rho_decimal = radius_decimal(m, q)
    rho = float(rho_decimal)
    residuals = [abs(denominator(root(m, k, q), m, q)) for k in range(2 * m)]
    return {
        "m": m,
        "c_m": str(coefficient),
        "rho_m": format(rho_decimal, "f"),
        "root_count": 2 * m,
        "max_root_residual": format(max(residuals), ".6e"),
        "max_angular_gap": format(math.pi / m, ".17g"),
        "positive_root_principal_coefficient": format(
            principal_coefficient(m, 0, q), ".17g"
        ),
        "singularity_type": "EXPONENTIAL_ESSENTIAL",
    }


def dependency_locks() -> dict[str, dict[str, str]]:
    out = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency changed: {name}")
        out[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return out


def canonical_sha(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def core_payload() -> dict[str, object]:
    fibers = []
    for q in (0.5, 1.0, 2.0):
        rows = [channel_row(m, q) for m in range(1, CHANNEL_ORDER + 1)]
        radii = [Decimal(row["rho_m"]) for row in rows]
        if not all(a < b for a, b in zip(radii, radii[1:])):
            raise ArithmeticError("strict radius ladder")
        limit = Decimal(str(limiting_radius(q)))
        if not radii[-1] < limit:
            raise ArithmeticError("radius must approach from below")
        fibers.append(
            {
                "q": q,
                "limiting_radius": format(limit, "f"),
                "last_radius": rows[-1]["rho_m"],
                "channels": rows,
            }
        )
    return {
        "candidate_id": "HCS-P76",
        "weighted_channel": "Psi_m(z,q)=2(qz)^m/[1-(1+q^(2m))z^(2m)]",
        "coefficient": "c_m=(1/m)sum_(k|m,k odd)k mu(k)=(1/m)product_(p|m,p odd)(1-p)!=0",
        "fiber_roots": "alpha_(m,k)(q)=rho_m(q) exp(pi i k/m), 0<=k<2m",
        "fiber_radius": "rho_m(q)=(1+q^(2m))^(-1/(2m))",
        "radius_monotonicity": "rho_m(q) strictly increases in m for every q>0",
        "accumulation_circle": "L(q)=min(1,q^(-1))",
        "principal_part": "c_m(-1)^k q^m/[m sqrt(1+q^(2m))](1-z/alpha_(m,k))^(-1)",
        "angular_density": "the 2m-th root meshes have maximum gap pi/m and become dense",
        "natural_boundary": "|z|=L(q) is a natural boundary for the explicit unrenormalized punctured continuation",
        "fibers": fibers,
        "strongest_positive_result": "every positive weight fiber has an exact full complex essential divisor whose radii and angular mesh are explicit",
        "strongest_obstruction": "the essential points accumulate densely at every point of |z|=min(1,q^(-1)), forbidding meromorphic continuation across any boundary arc",
        "open_theorem": "construct an independently specified source-native operator after a declared all-channel renormalization",
        "reusable_structure": "strict lp-norm monotonicity separates channel moduli while root-of-unity meshes force a dense limiting circle",
        "round2_clue": "compare the reverse-engineered trace-class channel diagonal with the noncompact direct sum of source-native orbit blocks",
        "claim_status": {
            "strict_weighted_radius_ladder": "PROVED",
            "full_complex_essential_divisor": "PROVED",
            "natural_boundary_for_unrenormalized_continuation": "PROVED",
            "renormalized_natural_boundary": "NOT_CLAIMED",
            "source_native_operator": "OPEN",
            "arithmetic_advance": "NO",
            "route_b_authorized": False,
        },
    }


def validate(core: dict[str, object]) -> None:
    if type(core) is not dict or core.get("candidate_id") != "HCS-P76":
        raise ValueError("schema")
    expected_scalars = {
        "weighted_channel": "Psi_m(z,q)=2(qz)^m/[1-(1+q^(2m))z^(2m)]",
        "coefficient": "c_m=(1/m)sum_(k|m,k odd)k mu(k)=(1/m)product_(p|m,p odd)(1-p)!=0",
        "fiber_roots": "alpha_(m,k)(q)=rho_m(q) exp(pi i k/m), 0<=k<2m",
        "fiber_radius": "rho_m(q)=(1+q^(2m))^(-1/(2m))",
        "radius_monotonicity": "rho_m(q) strictly increases in m for every q>0",
        "accumulation_circle": "L(q)=min(1,q^(-1))",
        "principal_part": "c_m(-1)^k q^m/[m sqrt(1+q^(2m))](1-z/alpha_(m,k))^(-1)",
        "angular_density": "the 2m-th root meshes have maximum gap pi/m and become dense",
        "natural_boundary": "|z|=L(q) is a natural boundary for the explicit unrenormalized punctured continuation",
        "strongest_positive_result": "every positive weight fiber has an exact full complex essential divisor whose radii and angular mesh are explicit",
        "strongest_obstruction": "the essential points accumulate densely at every point of |z|=min(1,q^(-1)), forbidding meromorphic continuation across any boundary arc",
        "open_theorem": "construct an independently specified source-native operator after a declared all-channel renormalization",
        "reusable_structure": "strict lp-norm monotonicity separates channel moduli while root-of-unity meshes force a dense limiting circle",
        "round2_clue": "compare the reverse-engineered trace-class channel diagonal with the noncompact direct sum of source-native orbit blocks",
    }
    for key, value in expected_scalars.items():
        if core.get(key) != value:
            raise ValueError(key)
    expected = {
        "strict_weighted_radius_ladder": "PROVED",
        "full_complex_essential_divisor": "PROVED",
        "natural_boundary_for_unrenormalized_continuation": "PROVED",
        "renormalized_natural_boundary": "NOT_CLAIMED",
        "source_native_operator": "OPEN",
        "arithmetic_advance": "NO",
        "route_b_authorized": False,
    }
    if core.get("claim_status") != expected:
        raise ValueError("status")
    fibers = core.get("fibers")
    if type(fibers) is not list or len(fibers) != 3:
        raise ValueError("fibers")
    for fiber in fibers:
        if len(fiber.get("channels", [])) != CHANNEL_ORDER:
            raise ValueError("channel ledger")
        if any(Fraction(row["c_m"]) == 0 for row in fiber["channels"]):
            raise ValueError("zero channel")


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    rejected = []
    protected = [
        "candidate_id",
        "weighted_channel",
        "coefficient",
        "fiber_roots",
        "fiber_radius",
        "radius_monotonicity",
        "accumulation_circle",
        "principal_part",
        "angular_density",
        "natural_boundary",
        "strongest_positive_result",
        "strongest_obstruction",
        "open_theorem",
        "reusable_structure",
        "round2_clue",
    ]
    for key in protected:
        trial = copy.deepcopy(core)
        trial[key] = "FORGED"
        try:
            validate(trial)
        except ValueError:
            rejected.append(key)
    for key, forged in (
        ("strict_weighted_radius_ladder", "OPEN"),
        ("full_complex_essential_divisor", "HEURISTIC"),
        ("natural_boundary_for_unrenormalized_continuation", "OPEN"),
        ("renormalized_natural_boundary", "PROVED"),
        ("source_native_operator", "PROVED"),
        ("arithmetic_advance", "YES"),
        ("route_b_authorized", True),
    ):
        trial = copy.deepcopy(core)
        trial["claim_status"][key] = forged
        try:
            validate(trial)
        except ValueError:
            rejected.append("status-" + key)
    trial = copy.deepcopy(core)
    trial["fibers"][1]["channels"][4]["c_m"] = "0"
    try:
        validate(trial)
    except ValueError:
        rejected.append("zero-channel")
    trial = copy.deepcopy(core)
    trial["fibers"][0]["channels"].pop()
    try:
        validate(trial)
    except ValueError:
        rejected.append("short-ledger")
    return {"attempted": 24, "rejected": rejected, "all_rejected": len(rejected) == 24}


def build() -> dict[str, object]:
    core = core_payload()
    validate(core)
    out = dict(core)
    out["dependency_locks"] = dependency_locks()
    out["mutation_audit"] = mutation_audit(core)
    if not out["mutation_audit"]["all_rejected"]:
        raise RuntimeError("mutation audit")
    out["core_sha256"] = canonical_sha(core)
    out["check"] = True
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    out = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "candidate_id": "HCS-P76",
                "fibers": len(out["fibers"]),
                "channels_per_fiber": CHANNEL_ORDER,
                "mutations": out["mutation_audit"]["attempted"],
                "core_sha256": out["core_sha256"],
                "check": True,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
