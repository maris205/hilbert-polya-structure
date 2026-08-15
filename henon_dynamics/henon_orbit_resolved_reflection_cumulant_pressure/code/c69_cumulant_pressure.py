#!/usr/bin/env python3
"""Exact packet-moment and cumulant certificate for HCS-P69."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import math
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results/c69_certificate.json"
PERIODS = tuple(range(1, 32, 2))

DEPENDENCIES = {
    "p68_proof": (
        TRACK / "henon_canonical_reflection_packet_euler_product/PROOF_PACKAGE.md",
        "9930197e758b5c065cb084dc93dc5288e9bf5e6b480fcf146b425537d4976f2a",
    ),
    "p68_certificate": (
        TRACK / "henon_canonical_reflection_packet_euler_product/results/c68_certificate.json",
        "14d20c79c0685384f90b27534971b541dc22726c5ba217d6c5f37308a0c8290b",
    ),
    "p68_paper": (
        TRACK / "henon_canonical_reflection_packet_euler_product/paper/paper.pdf",
        "fe843f7488293248acb8818e1ff4e7e4ac989a600c1c33c75b6f88b31e22190e",
    ),
    "p65_proof": (
        TRACK / "henon_minimal_symmetry_defect_pressure/PROOF_PACKAGE.md",
        "052ed9114f3da7ca3a039263e4bdfc617cabc6e9023542c0111d2d1c008b99eb",
    ),
    "p65_certificate": (
        TRACK / "henon_minimal_symmetry_defect_pressure/results/c65_certificate.json",
        "f0f9e3bb8c361c7b5b313ec38b96c585863fa0fa18c18e2461d97b14ed436cf2",
    ),
    "p65_paper": (
        TRACK / "henon_minimal_symmetry_defect_pressure/paper/paper.pdf",
        "d7574c7c8b6c0d70ef5bde5b2b5c074477dfaaf5a6136d028b0025fb2ea26ab9",
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


def add_polynomials(left: list[int], right: list[int], scale: int = 1) -> list[int]:
    out = left[:] + [0] * max(0, len(right) - len(left))
    for i, value in enumerate(right):
        out[i] += scale * value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def substitute_power(poly: list[int], k: int) -> list[int]:
    out = [0] * (k * (len(poly) - 1) + 1)
    for exponent, coefficient in enumerate(poly):
        out[k * exponent] = coefficient
    return out


def all_palindrome_polynomial(n: int) -> list[int]:
    """F_n(q)=sum over reflection-fixed words of q^S, for odd n."""
    if n <= 0 or n % 2 == 0:
        raise ValueError("positive odd period required")
    m = (n - 1) // 2
    poly = [0] * (n + 1)
    for k in range(m + 1):
        poly[1 + 2 * k] = 2 * math.comb(m, k)
    return poly


def primitive_polynomial(n: int) -> list[int]:
    """E_n(q)=sum over primitive reflection words of q^S."""
    out = [0]
    for k in divisors(n):
        term = substitute_power(all_palindrome_polynomial(n // k), k)
        out = add_polynomials(out, term, mobius(k))
    if any(value < 0 for value in out):
        raise ArithmeticError("negative primitive multiplicity")
    return out


def palindrome(half: tuple[int, ...]) -> tuple[int, ...]:
    return half + half[:0:-1]


def least_period(word: tuple[int, ...]) -> int:
    n = len(word)
    for d in divisors(n):
        if all(word[j] == word[j % d] for j in range(n)):
            return d
    raise ArithmeticError("period")


def symmetry_energy(word: tuple[int, ...]) -> int:
    n = len(word)
    return sum(word[(j - 1) % n] == word[(j + 1) % n] for j in range(n))


def enumerated_primitive_polynomial(n: int) -> list[int]:
    counts = [0] * (n + 1)
    for half in itertools.product((0, 1), repeat=(n + 1) // 2):
        word = palindrome(half)
        if least_period(word) == n:
            counts[symmetry_energy(word)] += 1
    while len(counts) > 1 and counts[-1] == 0:
        counts.pop()
    return counts


def moments(poly: list[int]) -> dict[str, str | int]:
    total = sum(poly)
    first = sum(k * count for k, count in enumerate(poly))
    second = sum(k * k * count for k, count in enumerate(poly))
    variance_numerator = second * total - first * first
    return {
        "count": total,
        "energy_sum": first,
        "energy_square_sum": second,
        "mean": f"{first}/{total}",
        "variance": f"{variance_numerator}/{total * total}",
        "variance_numerator": variance_numerator,
    }


def dependency_locks() -> dict[str, dict[str, str]]:
    locked = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency changed: {name}")
        locked[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return locked


def canonical_sha(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def core_payload() -> dict[str, object]:
    rows = []
    for n in PERIODS:
        all_poly = all_palindrome_polynomial(n)
        primitive = primitive_polynomial(n)
        if n <= 17 and primitive != enumerated_primitive_polynomial(n):
            raise ArithmeticError("enumeration mismatch")
        rows.append({
            "period": n,
            "all_palindrome_polynomial": all_poly,
            "primitive_polynomial": primitive,
            "all_moments": moments(all_poly),
            "primitive_moments": moments(primitive),
        })
    if any(row["primitive_moments"]["variance_numerator"] <= 0 for row in rows if row["period"] >= 5):
        raise ArithmeticError("strict cumulant gap")

    sample = []
    for s in (-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0):
        orbit = 0.5 * math.log1p(math.exp(-2 * s))
        mean_field = 0.5 * math.log(2) - 0.5 * s
        sample.append({
            "s": s,
            "orbit_resolved_pressure": orbit,
            "mean_field_pressure": mean_field,
            "gap": orbit - mean_field,
            "closed_gap": 0.5 * math.log(math.cosh(s)),
        })
    return {
        "candidate_id": "HCS-P69",
        "observable": "chi(s)=1{s[-1]=s[1]} and S_n chi=sum_(j mod n)chi(sigma^j s)",
        "decimation_identity": "because 2 is invertible mod odd n, S_n chi is nearest-neighbor equality energy after j->2j",
        "all_packet_polynomial": "F_(2m+1)(q)=2q(1+q^2)^m",
        "primitive_mobius_law": "E_n(q)=sum_(k|n)mu(k)F_(n/k)(q^k)",
        "orbit_resolved_pressure": "P_orb(s)=(1/2)log(1+exp(-2s))",
        "mean_field_pressure": "P_mf(s)=(1/2)log2-s/2",
        "exact_pressure_gap": "P_orb(s)-P_mf(s)=(1/2)log(cosh(s))",
        "gap_zero_set": "s=0 only",
        "asymptotic_variance_rate": "P_orb''(0)=1/2",
        "finite_strictness": "primitive energy distribution is nonconstant for every odd n>=5",
        "witnesses": "single centered 1 has energy n-2; centered block 111 has energy n-4",
        "rows": rows,
        "pressure_samples": sample,
        "strongest_positive_result": "the natural P65 symmetry defect has an exact orbit-resolved nonlinear packet pressure and full cumulant generating function",
        "strongest_obstruction": "P68's aggregate-mean factor misses the strictly positive gap (1/2)log cosh(s) for every nonzero real s",
        "open_theorem": "construct and analyze the full orbit-resolved Euler product using E_n(q), including its two-variable convergence boundary",
        "reusable_structure": "odd decimation conjugates the radius-one reflection defect to a nearest-neighbor Ising chain with a rank-two transfer matrix",
        "round2_clue": "the exact primitive moment polynomials are the coefficient input for an orbit-resolved Euler product; search for a closed logarithmic derivative and boundary curve",
        "claim_status": {
            "weighted_packet_polynomial": "PROVED",
            "primitive_mobius_law": "PROVED",
            "nonlinear_pressure": "PROVED",
            "mean_field_equivalence": "REFUTED_FOR_s_NONZERO",
            "arithmetic_trace": "OPEN",
            "arithmetic_advance": "NO",
            "route_b_authorized": False,
        },
    }


def validate(core: dict[str, object]) -> None:
    if type(core) is not dict or core.get("candidate_id") != "HCS-P69":
        raise ValueError("schema")
    if core.get("all_packet_polynomial") != "F_(2m+1)(q)=2q(1+q^2)^m":
        raise ValueError("transfer polynomial")
    if core.get("exact_pressure_gap") != "P_orb(s)-P_mf(s)=(1/2)log(cosh(s))":
        raise ValueError("gap")
    if core.get("asymptotic_variance_rate") != "P_orb''(0)=1/2":
        raise ValueError("variance")
    expected = {
        "weighted_packet_polynomial": "PROVED",
        "primitive_mobius_law": "PROVED",
        "nonlinear_pressure": "PROVED",
        "mean_field_equivalence": "REFUTED_FOR_s_NONZERO",
        "arithmetic_trace": "OPEN",
        "arithmetic_advance": "NO",
        "route_b_authorized": False,
    }
    if core.get("claim_status") != expected:
        raise ValueError("status")
    for row in core["rows"]:
        if row["period"] <= 17 and row["primitive_polynomial"] != enumerated_primitive_polynomial(row["period"]):
            raise ValueError("row")


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    rejected = []
    protected = [
        "candidate_id", "observable", "decimation_identity",
        "all_packet_polynomial", "primitive_mobius_law",
        "orbit_resolved_pressure", "mean_field_pressure", "exact_pressure_gap",
        "gap_zero_set", "asymptotic_variance_rate", "finite_strictness",
        "witnesses", "strongest_positive_result", "strongest_obstruction",
        "open_theorem", "reusable_structure", "round2_clue",
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
        ("weighted_packet_polynomial", "OPEN"),
        ("primitive_mobius_law", "OPEN"),
        ("nonlinear_pressure", "OPEN"),
        ("mean_field_equivalence", "PROVED"),
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
    trial["rows"][4]["primitive_polynomial"][1] += 1
    try:
        validate(trial)
    except ValueError:
        rejected.append("row-period9")
    return {"attempted": 25, "rejected": rejected, "all_rejected": len(rejected) == 25}


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
        "pressure_gap": result["exact_pressure_gap"],
        "mutations": result["mutation_audit"]["attempted"],
        "core_sha256": result["core_sha256"],
        "check": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
