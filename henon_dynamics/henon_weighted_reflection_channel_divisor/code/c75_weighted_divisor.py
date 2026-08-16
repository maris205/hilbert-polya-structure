#!/usr/bin/env python3
"""Exact weighted-channel and bidisk-divisor certificate for HCS-P75."""

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
DEFAULT_OUTPUT = PROJECT / "results/c75_certificate.json"
COEFFICIENT_ORDER = 48
CHANNEL_ORDER = 32
GEOMETRY_ORDER = 24

DEPENDENCIES = {
    "p69_proof": (
        TRACK / "henon_orbit_resolved_reflection_cumulant_pressure/PROOF_PACKAGE.md",
        "3fc96a72bcd74e2534d6cbdaa719710ab96feb6c53182d62c3ac6ab53030400e",
    ),
    "p69_certificate": (
        TRACK / "henon_orbit_resolved_reflection_cumulant_pressure/results/c69_certificate.json",
        "c7da0eaabbac08e90a3112fd4634fc35f380842c52ddf248872c884c1b9ef8ca",
    ),
    "p69_paper": (
        TRACK / "henon_orbit_resolved_reflection_cumulant_pressure/paper/paper.pdf",
        "1d4772f4c9cf2d3b8133dfd7a09c3dbadf3ad95dcce895358dabe5cf75c6c162",
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
    value = n
    while value % 2 == 0:
        value //= 2
    out: list[int] = []
    p = 3
    while p * p <= value:
        if value % p == 0:
            out.append(p)
            while value % p == 0:
                value //= p
        p += 2
    if value > 1:
        out.append(value)
    return out


def c_divisor(m: int) -> Fraction:
    return sum(Fraction(k * mobius(k), m) for k in divisors(m) if k % 2)


def c_euler(m: int) -> Fraction:
    numerator = 1
    for p in odd_prime_divisors(m):
        numerator *= 1 - p
    return Fraction(numerator, m)


def trim(poly: list[Fraction]) -> list[Fraction]:
    out = poly[:]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_add(
    left: list[Fraction], right: list[Fraction], scale: Fraction = Fraction(1)
) -> list[Fraction]:
    out = left[:] + [Fraction(0)] * max(0, len(right) - len(left))
    for exponent, coefficient in enumerate(right):
        out[exponent] += scale * coefficient
    return trim(out)


def poly_substitute(poly: list[Fraction], power: int) -> list[Fraction]:
    out = [Fraction(0)] * (power * (len(poly) - 1) + 1)
    for exponent, coefficient in enumerate(poly):
        out[power * exponent] = coefficient
    return trim(out)


def all_packet_polynomial(n: int) -> list[Fraction]:
    if n < 1 or n % 2 == 0:
        raise ValueError("positive odd period required")
    half = (n - 1) // 2
    out = [Fraction(0)] * (n + 1)
    for energy_half in range(half + 1):
        out[1 + 2 * energy_half] = Fraction(2 * math.comb(half, energy_half))
    return trim(out)


def primitive_polynomial(n: int) -> list[Fraction]:
    out = [Fraction(0)]
    for k in divisors(n):
        out = poly_add(
            out,
            poly_substitute(all_packet_polynomial(n // k), k),
            Fraction(mobius(k)),
        )
    return trim(out)


def direct_log_polynomial(degree: int) -> list[Fraction]:
    """[z^degree] log Z_orb(z,q), directly from primitive repetitions."""
    out = [Fraction(0)]
    for n in divisors(degree):
        if n % 2:
            repetition = degree // n
            out = poly_add(
                out,
                poly_substitute(primitive_polynomial(n), repetition),
                Fraction(1, repetition),
            )
    return trim(out)


def regrouped_log_polynomial(degree: int) -> list[Fraction]:
    """[z^degree] from sum_m c_m Psi_m(z,qz)."""
    out = [Fraction(0)]
    for m in divisors(degree):
        quotient = degree // m
        if quotient % 2 == 0:
            continue
        geometric_index = (quotient - 1) // 2
        channel = [Fraction(0)] * (degree + 1)
        for h in range(geometric_index + 1):
            q_degree = m + 2 * m * h
            channel[q_degree] = Fraction(2 * math.comb(geometric_index, h))
        out = poly_add(out, trim(channel), c_euler(m))
    return trim(out)


def serialize_poly(poly: list[Fraction]) -> list[str]:
    return [str(value) for value in trim(poly)]


def log_rho(q: float, m: int) -> float:
    """Stable logarithm of (1+q^(2m))^(-1/(2m))."""
    x = 2 * m * math.log(q)
    softplus = max(0.0, x) + math.log1p(math.exp(-abs(x)))
    return -softplus / (2 * m)


def rho(q: float, m: int) -> float:
    return math.exp(log_rho(q, m))


def exact_radius_increase(q: Fraction, m: int, n: int) -> bool:
    """Exact rho_m(q)<rho_n(q), tested without floating-point roots."""
    if q <= 0 or not 0 < m < n:
        raise ValueError("positive rational q and 0<m<n required")
    x = q * q
    return (1 + x ** m) ** n > (1 + x ** n) ** m


def fiber_root(q: float, m: int, ell: int) -> complex:
    radius = rho(q, m)
    angle = math.pi * ell / m
    return radius * complex(math.cos(angle), math.sin(angle))


def hypersurface_residual(q: float, m: int, ell: int) -> float:
    root = fiber_root(q, m, ell)
    return abs(root ** (2 * m) + (q * root) ** (2 * m) - 1)


def local_finiteness_cutoff(rz: Fraction, rw: Fraction) -> int:
    if not (0 <= rz < 1 and 0 <= rw < 1):
        raise ValueError("closed sub-bidisk radii required")
    m = 1
    while rz ** (2 * m) + rw ** (2 * m) >= 1:
        m += 1
    return m


def channel_row(m: int) -> dict[str, object]:
    coefficient = c_euler(m)
    if coefficient != c_divisor(m) or coefficient == 0 or abs(coefficient) > 1:
        raise ArithmeticError("channel coefficient")
    return {
        "m": m,
        "odd_prime_divisors": odd_prime_divisors(m),
        "c_m": str(coefficient),
        "nonzero": True,
        "absolute_bound_at_most_one": True,
    }


def geometry_block(q_value: Fraction) -> dict[str, object]:
    q = float(q_value)
    rows = []
    previous_log = -math.inf
    max_residual = 0.0
    for m in range(1, GEOMETRY_ORDER + 1):
        radius = rho(q, m)
        radius_log = log_rho(q, m)
        if not previous_log < radius_log:
            raise ArithmeticError("radius separation")
        previous_log = radius_log
        residual = max(hypersurface_residual(q, m, ell) for ell in range(2 * m))
        max_residual = max(max_residual, residual)
        rows.append({
            "m": m,
            "rho_m": format(radius, ".17g"),
            "root_count": 2 * m,
            "max_hypersurface_residual": format(residual, ".6e"),
            "principal_absolute_prefactor_without_c_m": format(
                q ** m / (m * math.sqrt(1 + q ** (2 * m))), ".17g"
            ),
        })
    if not all(exact_radius_increase(q_value, m, m + 1) for m in range(1, GEOMETRY_ORDER)):
        raise ArithmeticError("exact radius separation")
    return {
        "q": str(q_value),
        "rows": rows,
        "strict_radius_separation": True,
        "max_hypersurface_residual": format(max_residual, ".6e"),
        "radius_limit": "1" if q <= 1 else str(Fraction(1, 1) / q_value),
    }


def dependency_locks() -> dict[str, dict[str, str]]:
    out = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency changed: {name}")
        out[name] = {
            "path": str(path.relative_to(TRACK)),
            "sha256": observed,
        }
    return out


def canonical_sha(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def core_payload() -> dict[str, object]:
    coefficient_crosscheck = []
    for degree in range(1, COEFFICIENT_ORDER + 1):
        direct = direct_log_polynomial(degree)
        regrouped = regrouped_log_polynomial(degree)
        if direct != regrouped:
            raise ArithmeticError(f"weighted regrouping failed at degree {degree}")
        coefficient_crosscheck.append({
            "degree": degree,
            "q_polynomial": serialize_poly(direct),
        })

    compact_cutoffs = []
    for rz, rw in (
        (Fraction(1, 2), Fraction(1, 2)),
        (Fraction(3, 4), Fraction(2, 3)),
        (Fraction(9, 10), Fraction(4, 5)),
    ):
        cutoff = local_finiteness_cutoff(rz, rw)
        if rz ** (2 * cutoff) + rw ** (2 * cutoff) >= 1:
            raise ArithmeticError("local finiteness cutoff")
        compact_cutoffs.append({
            "r_z": str(rz),
            "r_w": str(rw),
            "first_tail_index_disjoint_from_all_H_m": cutoff,
        })

    return {
        "candidate_id": "HCS-P75",
        "frozen_input": "P69 primitive weighted polynomials plus P70 Euler repetition, with P72 channel coefficient locked",
        "two_fugacity_monomial": "z^n q^S=z^(n-S)w^S on w=qz",
        "lifted_all_word_function": "F_sharp(z,w)=2w/(1-z^2-w^2)",
        "weighted_channel_identity": "log Z_sharp(z,w)=sum_(m>=1)c_m*2w^m/(1-z^(2m)-w^(2m))",
        "positive_weight_fiber_identity": "log Z_orb(z,q)=sum_(m>=1)c_m*2(qz)^m/[1-(1+q^(2m))z^(2m)]",
        "channel_coefficient": "c_m=(1/m)sum_(k|m,k odd)k mu(k)=(1/m)product_(p|m,p odd)(1-p)",
        "channel_nonvanishing": "c_m is nonzero for every m and |c_m|<=1",
        "bidisk": "B^2={(z,w):|z|<1,|w|<1}",
        "hypersurfaces": "H_m={z^(2m)+w^(2m)=1}",
        "hypersurface_smoothness": "grad(z^(2m)+w^(2m)-1) cannot vanish on H_m",
        "divisor_local_finiteness": "on |z|<=r_z<1,|w|<=r_w<1, H_m is absent once r_z^(2m)+r_w^(2m)<1",
        "normal_continuation": "the channel sum converges normally on compact subsets of B^2 minus union_m H_m",
        "fiber_roots": "alpha_(m,l)(q)=rho_m(q)exp(pi*i*l/m), rho_m(q)=(1+q^(2m))^(-1/(2m)), 0<=l<2m",
        "fiber_radius_separation": "for every fixed q>0, rho_m(q) is strictly increasing in m",
        "fiber_radius_limit": "rho_m(q) tends to min(1,q^(-1))",
        "local_principal_part": "log Z_orb(z,q)=c_m*(-1)^l*q^m/[m*sqrt(1+q^(2m))]*(1-z/alpha_(m,l)(q))^(-1)+holomorphic",
        "local_singularity_type": "EXPONENTIAL_ESSENTIAL_AT_EACH_FIXED_POSITIVE_Q_FIBER_ROOT",
        "joint_collision_scope": "intersections H_m cap H_j are not classified; fixed positive-q fibers have no inter-channel collisions",
        "channel_rows": [channel_row(m) for m in range(1, CHANNEL_ORDER + 1)],
        "coefficient_crosscheck": coefficient_crosscheck,
        "geometry": [geometry_block(q) for q in (Fraction(1, 2), Fraction(1), Fraction(2))],
        "compact_local_finiteness_cutoffs": compact_cutoffs,
        "strongest_positive_result": "the entire P70 positive-weight family is the fiber restriction of a normally convergent two-variable scalar-channel germ with an explicit locally finite hypersurface divisor",
        "strongest_obstruction": "every fixed positive-weight channel root has a nonzero logarithmic pole and hence an exponential essential singularity",
        "open_theorem": "determine the boundary accumulation geometry of the complete complex root set without inferring a natural boundary from finite data",
        "reusable_structure": "the substitution w=qz turns weighted orbit energy into a bidisk divisor z^(2m)+w^(2m)=1 while preserving the P72 Mobius-repetition coefficient",
        "round2_clue": "analyze angular accumulation of all 2m roots and prove or refute a fiberwise natural boundary in a separate theorem",
        "claim_status": {
            "weighted_regrouping": "PROVED",
            "two_variable_normal_continuation": "PROVED",
            "smooth_locally_finite_hypersurface_divisor": "PROVED",
            "positive_q_fiber_principal_parts": "PROVED",
            "dense_natural_boundary": "NOT_CLAIMED_RESERVED_FOR_P76",
            "weighted_lind_source_for_q_not_1": "NOT_CLAIMED",
            "operator_model": "OPEN",
            "arithmetic_trace": "OPEN",
            "arithmetic_advance": "NO",
            "route_b_authorized": False,
        },
    }


def validate(core: dict[str, object]) -> None:
    if type(core) is not dict or core != core_payload():
        raise ValueError("exact HCS-P75 schema drift")


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    rejected: list[str] = []
    protected = [
        "candidate_id",
        "frozen_input",
        "two_fugacity_monomial",
        "lifted_all_word_function",
        "weighted_channel_identity",
        "positive_weight_fiber_identity",
        "channel_coefficient",
        "channel_nonvanishing",
        "bidisk",
        "hypersurfaces",
        "hypersurface_smoothness",
        "divisor_local_finiteness",
        "normal_continuation",
        "fiber_roots",
        "fiber_radius_separation",
        "fiber_radius_limit",
        "local_principal_part",
        "local_singularity_type",
        "joint_collision_scope",
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

    status_mutations = {
        "weighted_regrouping": "OPEN",
        "two_variable_normal_continuation": "HEURISTIC",
        "smooth_locally_finite_hypersurface_divisor": "OPEN",
        "positive_q_fiber_principal_parts": "NUMERICAL_ONLY",
        "dense_natural_boundary": "PROVED",
        "weighted_lind_source_for_q_not_1": "SOURCE_VERIFIED",
        "operator_model": "PROVED",
        "arithmetic_trace": "PROVED",
        "arithmetic_advance": "YES",
        "route_b_authorized": True,
    }
    for key, forged in status_mutations.items():
        trial = copy.deepcopy(core)
        trial["claim_status"][key] = forged
        try:
            validate(trial)
        except ValueError:
            rejected.append("status-" + key)

    for label, mutate in (
        ("zero-channel", lambda x: x["channel_rows"][14].update({"c_m": "0"})),
        ("short-crosscheck", lambda x: x["coefficient_crosscheck"].pop()),
        ("forged-root-count", lambda x: x["geometry"][1]["rows"][4].update({"root_count": 9})),
        ("forged-cutoff", lambda x: x["compact_local_finiteness_cutoffs"][0].update({"first_tail_index_disjoint_from_all_H_m": 99})),
    ):
        trial = copy.deepcopy(core)
        mutate(trial)
        try:
            validate(trial)
        except ValueError:
            rejected.append(label)

    attempted = len(protected) + len(status_mutations) + 4
    return {
        "attempted": attempted,
        "rejected": rejected,
        "all_rejected": len(rejected) == attempted,
    }


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
        "candidate_id": out["candidate_id"],
        "weighted_coefficients": len(out["coefficient_crosscheck"]),
        "fiber_geometry_rows": sum(len(block["rows"]) for block in out["geometry"]),
        "mutations": out["mutation_audit"]["attempted"],
        "core_sha256": out["core_sha256"],
        "check": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
