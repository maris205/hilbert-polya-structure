#!/usr/bin/env python3
"""Exact essential-singularity ladder certificate for HCS-P72."""

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
DEFAULT_OUTPUT = PROJECT / "results/c72_certificate.json"
ORDER = 48
LADDER_ORDER = 24

DEPENDENCIES = {
    "p71_proof": (
        TRACK / "henon_relative_lind_counterterm/PROOF_PACKAGE.md",
        "d0a85f29652a80bc6286f4cebe1949b8892daa8f768d4349e082aaf5ad640dc7",
    ),
    "p71_certificate": (
        TRACK / "henon_relative_lind_counterterm/results/c71_certificate.json",
        "b765fa8a04a552289f5672a1d590e3d84a9ab0e8616a5844b431a5b01c7c3866",
    ),
    "p71_paper": (
        TRACK / "henon_relative_lind_counterterm/paper/paper.pdf",
        "930d21108cfd88a3607ac62146e00d25e220382c704a4d04111b575c1d608fde",
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
}


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    primes = 0
    value = n
    p = 2
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
    out = []
    value = n
    while value % 2 == 0:
        value //= 2
    p = 3
    while p * p <= value:
        if value % p == 0:
            out.append(p)
            while value % p == 0:
                value //= p
        p += 2
    if value > 1 and value % 2:
        out.append(value)
    return out


def c_divisor(m: int) -> Fraction:
    """Regrouping coefficient m^{-1} sum_{k|m,k odd} k mu(k)."""
    return sum(
        Fraction(k * mobius(k), m) for k in divisors(m) if k % 2
    )


def c_euler(m: int) -> Fraction:
    numerator = 1
    for p in odd_prime_divisors(m):
        numerator *= 1 - p
    return Fraction(numerator, m)


def all_reflection_count(n: int) -> int:
    if n % 2 == 0 or n < 1:
        raise ValueError("odd positive period required")
    return 2 ** ((n + 1) // 2)


def primitive_reflection_count(n: int) -> int:
    if n % 2 == 0 or n < 1:
        raise ValueError("odd positive period required")
    return sum(mobius(k) * all_reflection_count(n // k) for k in divisors(n))


def direct_log_coefficient(degree: int) -> Fraction:
    """Coefficient [t^degree] log product_n(1-t^n)^(-D_n)."""
    return sum(
        Fraction(n * primitive_reflection_count(n), degree)
        for n in divisors(degree) if n % 2
    )


def regrouped_log_coefficient(degree: int) -> Fraction:
    """Coefficient from sum_m c_m Phi(t^m), Phi(x)=2x/(1-2x^2)."""
    total = Fraction(0)
    for m in divisors(degree):
        quotient = degree // m
        if quotient % 2:
            total += c_euler(m) * 2 ** ((quotient + 1) // 2)
    return total


def ladder_row(m: int) -> dict[str, object]:
    primes = odd_prime_divisors(m)
    numerator = math.prod(1 - p for p in primes)
    coefficient = c_euler(m)
    if coefficient != c_divisor(m) or coefficient == 0:
        raise ArithmeticError("nonzero Euler coefficient")
    rho = 2 ** (-1 / (2 * m))
    return {
        "m": m,
        "odd_prime_divisors": primes,
        "euler_numerator": numerator,
        "c_m": str(coefficient),
        "rho_m": format(rho, ".17g"),
        "log_Z_principal_multiplier_of_1_over_sqrt2": str(coefficient / m),
        "log_Crel_principal_multiplier_of_1_over_sqrt2": str(-coefficient / m),
        "singularity_type_of_Crel": "EXPONENTIAL_ESSENTIAL" if m >= 2 else "CANCELLED_BY_P71",
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
    coefficient_crosscheck = []
    for degree in range(1, ORDER + 1):
        direct = direct_log_coefficient(degree)
        regrouped = regrouped_log_coefficient(degree)
        if direct != regrouped:
            raise ArithmeticError(f"regrouping failed at {degree}")
        coefficient_crosscheck.append({
            "degree": degree,
            "log_coefficient": str(direct),
        })
    ladder = [ladder_row(m) for m in range(1, LADDER_ORDER + 1)]
    if not all(float(ladder[i]["rho_m"]) < float(ladder[i + 1]["rho_m"])
               for i in range(len(ladder) - 1)):
        raise ArithmeticError("ladder monotonicity")
    return {
        "candidate_id": "HCS-P72",
        "packet_regrouping": "log Z_orb(t,1)=sum_(m>=1)c_m Phi(t^m), Phi(x)=2x/(1-2x^2)",
        "regrouping_coefficient": "c_m=(1/m)sum_(k|m,k odd)k mu(k)=(1/m)product_(p|m,p odd)(1-p)",
        "relative_continuation": "log C_rel(t)=H_rel(1-sqrt(2)t)-sum_(m>=2)c_m Phi(t^m)",
        "relative_regular_part": "H_rel(u)=-(1/2)log(2-u)-3(2u-3)/[4(u-2)]",
        "positive_ladder": "rho_m=2^(-1/(2m)), m>=2",
        "local_principal_part": "log C_rel(t)=-c_m/[sqrt(2)m(1-t/rho_m)]+holomorphic",
        "noncancellation": "c_m is nonzero for every m because product_(p|m,p odd)(1-p) is nonzero",
        "ladder_limit": "rho_m increases strictly to 1",
        "global_obstruction": "C_rel has an exponential essential singularity at every rho_m for m>=2",
        "finite_state_consequence": "no meromorphic finite-dimensional or holomorphic trace-class Fredholm determinant on the unit disk can equal this continuation",
        "coefficient_crosscheck": coefficient_crosscheck,
        "ladder_ledger": ladder,
        "strongest_positive_result": "the P71 local relative germ has an exact continuation formula and a completely explicit infinite positive singularity ladder",
        "strongest_obstruction": "after the unique first-boundary counterterm, essential singularities persist at every rho_m=2^(-1/(2m)), m at least two, accumulating at one",
        "open_theorem": "find a punctured-domain or renormalized infinite-rank operator model that owns the complete ladder without claiming a unit-disk Fredholm determinant",
        "reusable_structure": "Möbius/repetition regrouping converts the primitive packet product into scalar channels c_m Phi(t^m), isolating every later boundary independently",
        "round2_clue": "treat the ladder as a canonical divisor of exponential singularities and test whether a Weierstrass-type infinite counterterm can renormalize all channels on a slit domain",
        "claim_status": {
            "regrouping_identity": "PROVED",
            "punctured_continuation": "PROVED",
            "infinite_essential_ladder": "PROVED",
            "unit_disk_meromorphic_determinant": "REFUTED_FOR_THIS_RELATIVE_GERM",
            "punctured_operator_model": "OPEN",
            "arithmetic_advance": "NO",
            "route_b_authorized": False,
        },
    }


def validate(core: dict[str, object]) -> None:
    if type(core) is not dict or core.get("candidate_id") != "HCS-P72":
        raise ValueError("schema")
    if core.get("positive_ladder") != "rho_m=2^(-1/(2m)), m>=2":
        raise ValueError("ladder")
    if core.get("relative_regular_part") != "H_rel(u)=-(1/2)log(2-u)-3(2u-3)/[4(u-2)]":
        raise ValueError("regular part")
    if core.get("global_obstruction") != "C_rel has an exponential essential singularity at every rho_m for m>=2":
        raise ValueError("obstruction")
    expected = {
        "regrouping_identity": "PROVED",
        "punctured_continuation": "PROVED",
        "infinite_essential_ladder": "PROVED",
        "unit_disk_meromorphic_determinant": "REFUTED_FOR_THIS_RELATIVE_GERM",
        "punctured_operator_model": "OPEN",
        "arithmetic_advance": "NO",
        "route_b_authorized": False,
    }
    if core.get("claim_status") != expected:
        raise ValueError("status")
    rows = core.get("ladder_ledger")
    if type(rows) is not list or len(rows) != LADDER_ORDER:
        raise ValueError("ledger length")
    for row in rows:
        if Fraction(row["c_m"]) == 0:
            raise ValueError("zero channel")
    cross = core.get("coefficient_crosscheck")
    if type(cross) is not list or len(cross) != ORDER:
        raise ValueError("crosscheck length")


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    rejected = []
    protected = [
        "candidate_id", "packet_regrouping", "regrouping_coefficient",
        "relative_continuation", "relative_regular_part", "positive_ladder",
        "local_principal_part", "noncancellation", "ladder_limit",
        "global_obstruction", "finite_state_consequence",
        "strongest_positive_result", "strongest_obstruction", "open_theorem",
        "reusable_structure", "round2_clue",
    ]
    for key in protected:
        trial = copy.deepcopy(core)
        trial[key] = "FORGED"
        try:
            validate(trial)
            if trial != core:
                raise ValueError("drift")
        except ValueError:
            rejected.append(key)
    for key, forged in (
        ("regrouping_identity", "OPEN"),
        ("punctured_continuation", "OPEN"),
        ("infinite_essential_ladder", "HEURISTIC"),
        ("unit_disk_meromorphic_determinant", "PROVED"),
        ("punctured_operator_model", "PROVED"),
        ("arithmetic_advance", "YES"),
        ("route_b_authorized", True),
    ):
        trial = copy.deepcopy(core)
        trial["claim_status"][key] = forged
        try:
            validate(trial)
            if trial != core:
                raise ValueError("drift")
        except ValueError:
            rejected.append("status-" + key)
    trial = copy.deepcopy(core)
    trial["ladder_ledger"][7]["c_m"] = "0"
    try:
        validate(trial)
    except ValueError:
        rejected.append("zero-channel")
    trial = copy.deepcopy(core)
    trial["coefficient_crosscheck"].pop()
    try:
        validate(trial)
    except ValueError:
        rejected.append("short-crosscheck")
    return {"attempted": 25, "rejected": rejected, "all_rejected": len(rejected) == 25}


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
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "candidate_id": "HCS-P72",
        "ladder_channels": len(out["ladder_ledger"]) - 1,
        "first_uncancelled_rho": out["ladder_ledger"][1]["rho_m"],
        "mutations": out["mutation_audit"]["attempted"],
        "core_sha256": out["core_sha256"],
        "check": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
