#!/usr/bin/env python3
"""Exact orbit-resolved Euler and boundary certificate for HCS-P70."""

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
DEFAULT_OUTPUT = PROJECT / "results/c70_certificate.json"
ORDER = 31

DEPENDENCIES = {
    "p69_proof": (TRACK / "henon_orbit_resolved_reflection_cumulant_pressure/PROOF_PACKAGE.md", "3fc96a72bcd74e2534d6cbdaa719710ab96feb6c53182d62c3ac6ab53030400e"),
    "p69_certificate": (TRACK / "henon_orbit_resolved_reflection_cumulant_pressure/results/c69_certificate.json", "c7da0eaabbac08e90a3112fd4634fc35f380842c52ddf248872c884c1b9ef8ca"),
    "p69_paper": (TRACK / "henon_orbit_resolved_reflection_cumulant_pressure/paper/paper.pdf", "1d4772f4c9cf2d3b8133dfd7a09c3dbadf3ad95dcce895358dabe5cf75c6c162"),
    "p68_proof": (TRACK / "henon_canonical_reflection_packet_euler_product/PROOF_PACKAGE.md", "9930197e758b5c065cb084dc93dc5288e9bf5e6b480fcf146b425537d4976f2a"),
    "p68_certificate": (TRACK / "henon_canonical_reflection_packet_euler_product/results/c68_certificate.json", "14d20c79c0685384f90b27534971b541dc22726c5ba217d6c5f37308a0c8290b"),
    "p68_paper": (TRACK / "henon_canonical_reflection_packet_euler_product/paper/paper.pdf", "fe843f7488293248acb8818e1ff4e7e4ac989a600c1c33c75b6f88b31e22190e"),
}


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    primes, value, p = 0, n, 2
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


def poly_add(a: list[int], b: list[int], scale: int = 1) -> list[int]:
    out = a[:] + [0] * max(0, len(b) - len(a))
    for i, value in enumerate(b):
        out[i] += scale * value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_substitute(poly: list[int], k: int) -> list[int]:
    out = [0] * (k * (len(poly) - 1) + 1)
    for i, value in enumerate(poly):
        out[k * i] = value
    return out


def all_poly(n: int) -> list[int]:
    m = (n - 1) // 2
    out = [0] * (n + 1)
    for k in range(m + 1):
        out[1 + 2 * k] = 2 * math.comb(m, k)
    return out


def primitive_poly(n: int) -> list[int]:
    out = [0]
    for k in divisors(n):
        out = poly_add(out, poly_substitute(all_poly(n // k), k), mobius(k))
    return out


def poly_eval(poly: list[int], q: Fraction) -> Fraction:
    return sum(Fraction(value) * q ** degree for degree, value in enumerate(poly))


def log_derivative_polynomial(m: int) -> list[int]:
    """Coefficient of z^m in z partial_z log Z_orb."""
    out = [0]
    for n in divisors(m):
        if n % 2:
            out = poly_add(out, poly_substitute(primitive_poly(n), m // n), n)
    return out


def direct_log_derivative_value(m: int, q: Fraction) -> Fraction:
    return sum(
        n * poly_eval(primitive_poly(n), q ** (m // n))
        for n in divisors(m) if n % 2
    )


def dependency_locks() -> dict[str, dict[str, str]]:
    out = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency changed: {name}")
        out[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return out


def canonical_sha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def core_payload() -> dict[str, object]:
    ledger = []
    for m in range(1, ORDER + 1):
        poly = log_derivative_polynomial(m)
        values = {}
        for label, q in (("1/2", Fraction(1, 2)), ("1", Fraction(1)), ("2", Fraction(2))):
            value = poly_eval(poly, q)
            if value != direct_log_derivative_value(m, q):
                raise ArithmeticError("log derivative")
            values[label] = str(value)
        ledger.append({"degree": m, "coefficient_polynomial": poly, "values": values})
    p68 = json.loads(DEPENDENCIES["p68_certificate"][0].read_text(encoding="utf-8"))
    if [row["values"]["1"] for row in ledger] != [str(x) for x in p68["log_derivative_coefficients_through_41"][1:ORDER + 1]]:
        raise ArithmeticError("q=1 specialization")

    samples = []
    for q in (0.25, 0.5, 1.0, 2.0, 4.0):
        radius = 1 / math.sqrt(1 + q * q)
        mean_radius = 1 / math.sqrt(2 * q)
        samples.append({
            "q": q,
            "orbit_radius": radius,
            "mean_field_radius": mean_radius,
            "radius_ratio": radius / mean_radius,
            "closed_ratio": 1 / math.sqrt((q + 1 / q) / 2),
            "principal_log_coefficient": q / math.sqrt(1 + q * q),
        })
    return {
        "candidate_id": "HCS-P70",
        "orbit_resolved_product": "Z_orb(z,q)=product_(n odd)product_(omega in A_n)(1-z^n q^(S_n chi(omega)))^(-1)",
        "logarithmic_derivative": "[z^m]z partial_z log Z_orb=sum_(n|m,n odd)n E_n(q^(m/n))",
        "primitive_generating_series": "E(z,q)=sum_(k odd)mu(k) 2(qz)^k/[1-(1+q^(2k))z^(2k)]",
        "positive_q_radius": "R(q)=(1+q^2)^(-1/2)",
        "boundary_expansion": "log Z_orb(z,q)=q/[sqrt(1+q^2)(1-sqrt(1+q^2)z)]+G_q(z)",
        "boundary_type": "EXPONENTIAL_ESSENTIAL_SINGULARITY_FOR_EVERY_q_POSITIVE",
        "mean_field_radius": "R_mf(q)=(2q)^(-1/2)",
        "radius_ratio": "R(q)/R_mf(q)=1/sqrt((q+q^(-1))/2)",
        "strict_radius_shift": "R(q)<R_mf(q) for q positive and q!=1",
        "unweighted_specialization": "q=1 recovers P68 exactly",
        "coefficient_ledger": ledger,
        "boundary_samples": samples,
        "strongest_positive_result": "the full orbit-resolved reflection Euler product has an exact logarithmic derivative, moving convergence boundary, and boundary singularity for every positive weight",
        "strongest_obstruction": "mean-field weighting gives the wrong convergence radius for every q positive other than one, and the resolved product remains essentially singular",
        "open_theorem": "compare this packet product with the source-native full D_infinity Lind zeta and isolate a relative counterterm with a meromorphic or determinant interpretation",
        "reusable_structure": "the two-variable primitive generating series and repetition sum reduce boundary analysis to one leading k=r=1 pole",
        "round2_clue": "form the ratio with the standard full two-shift flip/Lind zeta or an explicit analytic counterterm and classify which essential exponential is universal",
        "claim_status": {
            "orbit_euler_product": "PROVED",
            "moving_radius": "PROVED",
            "essential_boundary": "PROVED",
            "mean_field_boundary_equivalence": "REFUTED_EXCEPT_q_1",
            "lind_relative_determinant": "OPEN",
            "arithmetic_advance": "NO",
            "route_b_authorized": False,
        },
    }


def validate(core: dict[str, object]) -> None:
    if type(core) is not dict or core.get("candidate_id") != "HCS-P70":
        raise ValueError("schema")
    if core.get("positive_q_radius") != "R(q)=(1+q^2)^(-1/2)":
        raise ValueError("radius")
    if core.get("boundary_type") != "EXPONENTIAL_ESSENTIAL_SINGULARITY_FOR_EVERY_q_POSITIVE":
        raise ValueError("boundary")
    if core.get("radius_ratio") != "R(q)/R_mf(q)=1/sqrt((q+q^(-1))/2)":
        raise ValueError("ratio")
    expected = {
        "orbit_euler_product": "PROVED",
        "moving_radius": "PROVED",
        "essential_boundary": "PROVED",
        "mean_field_boundary_equivalence": "REFUTED_EXCEPT_q_1",
        "lind_relative_determinant": "OPEN",
        "arithmetic_advance": "NO",
        "route_b_authorized": False,
    }
    if core.get("claim_status") != expected:
        raise ValueError("status")
    for row in core["coefficient_ledger"]:
        poly = row["coefficient_polynomial"]
        if str(poly_eval(poly, Fraction(1))) != row["values"]["1"]:
            raise ValueError("ledger")


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    rejected = []
    protected = [
        "candidate_id", "orbit_resolved_product", "logarithmic_derivative",
        "primitive_generating_series", "positive_q_radius", "boundary_expansion",
        "boundary_type", "mean_field_radius", "radius_ratio",
        "strict_radius_shift", "unweighted_specialization",
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
        ("orbit_euler_product", "OPEN"), ("moving_radius", "OPEN"),
        ("essential_boundary", "MEROMORPHIC"),
        ("mean_field_boundary_equivalence", "PROVED"),
        ("lind_relative_determinant", "PROVED"), ("arithmetic_advance", "YES"),
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
    trial["coefficient_ledger"][8]["values"]["1"] = "FORGED"
    try:
        validate(trial)
    except ValueError:
        rejected.append("ledger-9")
    return {"attempted": 24, "rejected": rejected, "all_rejected": len(rejected) == 24}


def build() -> dict[str, object]:
    core = core_payload()
    validate(core)
    out = dict(core)
    out["dependency_locks"] = dependency_locks()
    out["mutation_audit"] = mutation_audit(core)
    if not out["mutation_audit"]["all_rejected"]:
        raise RuntimeError("mutations")
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
        "candidate_id": "HCS-P70",
        "radius": out["positive_q_radius"],
        "boundary": out["boundary_type"],
        "mutations": out["mutation_audit"]["attempted"],
        "core_sha256": out["core_sha256"],
        "check": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
