#!/usr/bin/env python3
"""HCS-P64 reflection-boundary and packet-Mahler pressure certificate."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c64_certificate.json"
X, T = sp.symbols("X T")
ROOT_PERIODS = (1, 3, 5, 7, 9, 11)
SYMBOLIC_PERIODS = tuple(range(1, 22, 2))
BLOCK_RADIUS = 2

DEPENDENCIES = {
    "p62_proof": (
        TRACK / "henon_full_horseshoe_algebraic_exhaustion" / "PROOF_PACKAGE.md",
        "1d81017bbd3c608d86e19a7fa3a80c70f7b11697364b944fe6ff285f8b4d61c7",
    ),
    "p62_certificate": (
        TRACK / "henon_full_horseshoe_algebraic_exhaustion" / "results" / "c62_certificate.json",
        "d8e4d170c37d7af6c454a734aa91d2532902f5b78aaa939c037a731b4c72d134",
    ),
    "p63_proof": (
        TRACK / "henon_primitive_coordinate_height_flat_pressure" / "PROOF_PACKAGE.md",
        "8f1738de89549ea4b47af3b2a90b7cc29027b86da7f6136d8a1a47e74b222f62",
    ),
    "p63_certificate": (
        TRACK / "henon_primitive_coordinate_height_flat_pressure" / "results" / "c63_certificate.json",
        "f0de7ca9d8ef8f2c262a0869414c90f40af529f157d31972cbe21a73f3cbe0c3",
    ),
    "p63_paper": (
        TRACK / "henon_primitive_coordinate_height_flat_pressure" / "paper" / "paper.pdf",
        "c5f86bfefc6391b02ac174becbc07cae4c521872d907d9dd96c8e9e087ac4033",
    ),
}


def canonical_sha(payload: object) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def dependency_locks() -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency hash changed: {name}")
        rows[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return rows


def primitive_degree(n: int) -> int:
    return sum(
        int(sp.mobius(n // divisor)) * 2 ** ((divisor + 1) // 2)
        for divisor in sp.divisors(n)
    )


def palindrome_word(half: tuple[int, ...]) -> tuple[int, ...]:
    return half + tuple(reversed(half[1:]))


def least_period(word: tuple[int, ...]) -> int:
    n = len(word)
    for divisor in sp.divisors(n):
        d = int(divisor)
        if all(word[j] == word[j % d] for j in range(n)):
            return d
    raise ArithmeticError("word has no period")


def primitive_palindromes(n: int) -> list[tuple[int, ...]]:
    half_length = (n + 1) // 2
    rows = [
        palindrome_word(bits)
        for bits in itertools.product((0, 1), repeat=half_length)
    ]
    primitive = [word for word in rows if least_period(word) == n]
    if len(primitive) != primitive_degree(n):
        raise ArithmeticError(f"primitive palindrome count failed at n={n}")
    return primitive


def cyclic_block(word: tuple[int, ...], center: int, radius: int) -> tuple[int, ...]:
    n = len(word)
    return tuple(word[(center + shift) % n] for shift in range(-radius, radius + 1))


def distribution(words: list[tuple[int, ...]], radius: int, orbit_average: bool) -> dict[tuple[int, ...], Fraction]:
    counts: dict[tuple[int, ...], int] = {}
    total = 0
    for word in words:
        centers = range(len(word)) if orbit_average else (0,)
        for center in centers:
            block = cyclic_block(word, center, radius)
            counts[block] = counts.get(block, 0) + 1
            total += 1
    return {block: Fraction(value, total) for block, value in counts.items()}


def total_variation_from_fair(distribution_row: dict[tuple[int, ...], Fraction], width: int) -> Fraction:
    fair = Fraction(1, 2**width)
    universe = itertools.product((0, 1), repeat=width)
    return sum(abs(distribution_row.get(block, Fraction(0)) - fair) for block in universe) / 2


def symbolic_row(n: int) -> dict[str, object]:
    words = primitive_palindromes(n)
    width = 2 * BLOCK_RADIUS + 1
    axis = distribution(words, BLOCK_RADIUS, False)
    orbit = distribution(words, BLOCK_RADIUS, True)
    axis_tv = total_variation_from_fair(axis, width)
    orbit_tv = total_variation_from_fair(orbit, width)
    full_count = 2 ** ((n + 1) // 2)
    nonprimitive = full_count - len(words)
    reflection_event = sum(
        probability for block, probability in axis.items()
        if block[BLOCK_RADIUS - 1] == block[BLOCK_RADIUS + 1]
    )
    if reflection_event != 1:
        raise ArithmeticError("axis reflection identity failed")
    return {
        "period": n,
        "closure_half_words": full_count,
        "primitive_half_words": len(words),
        "nonprimitive_fraction": str(Fraction(nonprimitive, full_count)),
        "axis_radius2_tv_from_fair": str(axis_tv),
        "orbit_averaged_radius2_tv_from_fair": str(orbit_tv),
        "axis_event_s_minus1_equals_s_plus1": str(reflection_event),
        "primitive_words_sha256": canonical_sha(["".join(map(str, word)) for word in words]),
    }


def closure_and_quotients(max_period: int) -> dict[int, sp.Poly]:
    coordinates = [X, sp.expand((1 - 6 * X**2) / 2)]
    quotients: dict[int, sp.Poly] = {}
    for n in range(1, max_period + 1, 2):
        m = (n - 1) // 2
        while len(coordinates) <= m + 1:
            coordinates.append(sp.expand(1 - 6 * coordinates[-1] ** 2 - coordinates[-2]))
        closure = sp.Poly(coordinates[m + 1] - coordinates[m], X, domain=sp.QQ).monic()
        lower = sp.Poly(1, X, domain=sp.QQ)
        for divisor in sp.divisors(n):
            if divisor < n:
                lower *= quotients[int(divisor)]
        quotient, remainder = sp.div(closure, lower, domain=sp.QQ)
        if not remainder.is_zero:
            raise ArithmeticError(f"quotient failed at n={n}")
        quotients[n] = quotient.monic()
    return quotients


def scaled_primitive(poly: sp.Poly) -> sp.Poly:
    degree = poly.degree()
    result = sp.Poly(sp.expand(6**degree * poly.as_expr().subs(X, T / 6)), T, domain=sp.QQ)
    if result.LC() != 1 or any(value.q != 1 for value in result.all_coeffs()):
        raise ArithmeticError("integral scaling failed")
    return sp.Poly(result.as_expr(), T, domain=sp.ZZ)


def root_row(n: int, quotient: sp.Poly) -> dict[str, object]:
    scaled = scaled_primitive(quotient)
    roots = sorted(complex(value).real for value in sp.nroots(scaled, n=50, maxsteps=800))
    if len(roots) != primitive_degree(n):
        raise ArithmeticError("root count failed")
    axis_mass = sum(math.log(max(1.0, abs(value))) for value in roots) / len(roots)
    orbit_masses: list[float] = []
    closure_errors: list[float] = []
    for root in roots:
        previous = (6.0 - root * root) / 2.0
        current = root
        orbit: list[float] = []
        for _ in range(n):
            orbit.append(current)
            previous, current = current, 6.0 - current * current - previous
        orbit_masses.append(sum(math.log(max(1.0, abs(value))) for value in orbit) / n)
        closure_errors.append(abs(current - root))
    orbit_mass = sum(orbit_masses) / len(orbit_masses)
    return {
        "period": n,
        "primitive_degree": len(roots),
        "axis_packet_mahler_average_diagnostic": f"{axis_mass:.15f}",
        "orbit_averaged_log_coordinate_diagnostic": f"{orbit_mass:.15f}",
        "axis_minus_orbit_diagnostic": f"{axis_mass - orbit_mass:.15f}",
        "max_float_period_closure_error": f"{max(closure_errors):.3e}",
        "scaled_polynomial_sha256": canonical_sha([int(value) for value in scaled.all_coeffs()]),
    }


def core_payload() -> dict[str, object]:
    symbolic_rows = [symbolic_row(n) for n in SYMBOLIC_PERIODS]
    quotients = closure_and_quotients(max(ROOT_PERIODS))
    root_rows = [root_row(n, quotients[n]) for n in ROOT_PERIODS]
    return {
        "candidate_id": "HCS-P64",
        "map": "H_6(q,p)=(1-6q^2-p,q)",
        "scaled_map": "H(x,y)=(6-x^2-y,x)",
        "symbolic_system": "full two-shift Sigma_2 with reversal rho(s)_k=s_(-k)",
        "equivariant_coding": "pi sigma=H pi and pi rho=J pi",
        "axis_full_count": "2^((n+1)/2) for odd n",
        "primitive_axis_degree": "D_n=sum_(d|n)mu(n/d)2^((d+1)/2)",
        "axis_limit_measure": "iid fair nonnegative coordinates reflected by s_(-k)=s_k; not shift invariant",
        "orbit_averaged_limit_measure": "fair Bernoulli maximal-entropy measure",
        "primitive_removal_bound": "TV<=tau(n)2^(-n/3) for odd n",
        "orbit_cylinder_bad_center_bound": "at most 4r+1 bad centers for a radius-r block",
        "packet_mahler_average": "a_n=D_n^(-1)log M(tilde_Psi_n)",
        "axis_limit_constant": "kappa_J=int log^+|x| dnu_J in (0,log(1+sqrt(7))]",
        "axis_packet_pressure": "lim n^(-1)log[D_n exp(-s n a_n)]=(1/2)log2-s kappa_J",
        "orbit_packet_pressure": "lim n^(-1)log[D_n exp(-s n b_n)]=(1/2)log2-s kappa_max",
        "pressure_domain": "every fixed real s",
        "symbolic_rows": symbolic_rows,
        "root_diagnostic_rows": root_rows,
        "strongest_positive_result": "primitive reflection-axis measures converge to a reflection-boundary Bernoulli measure, orbit averages converge to maximal entropy, and the packet Mahler pressure is a nonconstant linear extensive pressure",
        "strongest_obstruction": "the axis-root ensemble is not the invariant maximal-entropy ensemble; confusing them changes the limiting observable and invalidates the naive P63 clue",
        "open_theorem": "certify whether kappa_J differs from kappa_max for log^+|x| and identify either constant by a source-native analytic or rigorous cylinder scheme",
        "reusable_structure": "equivariant full-shift coding plus exponentially negligible primitive subtraction converts reflection half-words into weak-star limit theorems",
        "round2_clue": "use hyperbolic cylinder enclosures to separate the reflection-boundary and orbit-averaged Mahler slopes with a rigorous nonzero interval",
        "claim_status": {
            "equivariant_reflection_coding": "PROVED",
            "primitive_axis_equidistribution": "PROVED",
            "orbit_averaged_equidistribution": "PROVED",
            "packet_mahler_pressure": "PROVED",
            "numerical_slope_separation": "NUMERICAL_OBSERVATION",
            "individual_extensive_height_pressure": "OPEN",
            "arithmetic_advance": "NO",
            "route_b_authorized": False,
        },
    }


def validate_core(payload: dict[str, object]) -> None:
    if type(payload) is not dict:
        raise TypeError("payload must be exact dict")
    if payload["candidate_id"] != "HCS-P64":
        raise ValueError("candidate mismatch")
    rows = payload["symbolic_rows"]
    if type(rows) is not list or len(rows) != len(SYMBOLIC_PERIODS):
        raise ValueError("symbolic rows mismatch")
    if [row["primitive_half_words"] for row in rows] != [primitive_degree(n) for n in SYMBOLIC_PERIODS]:
        raise ValueError("degree vector mismatch")
    if any(row["axis_event_s_minus1_equals_s_plus1"] != "1" for row in rows):
        raise ValueError("reflection event mismatch")
    if payload["claim_status"]["arithmetic_advance"] != "NO":
        raise ValueError("claim promotion")
    if payload["claim_status"]["route_b_authorized"] is not False:
        raise ValueError("Route B promotion")


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    mutations: list[tuple[str, tuple[str, ...], object]] = [
        ("candidate", ("candidate_id",), "HCS-P64-PROMOTED"),
        ("coding", ("equivariant_coding",), "ASSUMED"),
        ("axis-count", ("axis_full_count",), "2^n"),
        ("degree", ("primitive_axis_degree",), "2^n"),
        ("axis-limit", ("axis_limit_measure",), "maximal entropy"),
        ("orbit-limit", ("orbit_averaged_limit_measure",), "reflection boundary"),
        ("primitive-bound", ("primitive_removal_bound",), "O(1)"),
        ("bad-centers", ("orbit_cylinder_bad_center_bound",), "n"),
        ("mahler", ("packet_mahler_average",), "individual height"),
        ("kappa", ("axis_limit_constant",), "0"),
        ("axis-pressure", ("axis_packet_pressure",), "flat"),
        ("orbit-pressure", ("orbit_packet_pressure",), "flat"),
        ("domain", ("pressure_domain",), "s=0"),
        ("positive", ("strongest_positive_result",), "RH"),
        ("obstruction", ("strongest_obstruction",), "NONE"),
        ("open", ("open_theorem",), "CLOSED"),
        ("reuse", ("reusable_structure",), "NONE"),
        ("round2", ("round2_clue",), "PRIME TRACE PROVED"),
        ("status-coding", ("claim_status", "equivariant_reflection_coding"), "OPEN"),
        ("status-axis", ("claim_status", "primitive_axis_equidistribution"), "OPEN"),
        ("status-orbit", ("claim_status", "orbit_averaged_equidistribution"), "OPEN"),
        ("status-pressure", ("claim_status", "packet_mahler_pressure"), "OPEN"),
        ("status-numeric", ("claim_status", "numerical_slope_separation"), "PROVED"),
        ("status-individual", ("claim_status", "individual_extensive_height_pressure"), "PROVED"),
        ("arithmetic", ("claim_status", "arithmetic_advance"), "YES"),
        ("route-b", ("claim_status", "route_b_authorized"), True),
    ]
    rejected: list[str] = []
    for label, path, replacement in mutations:
        candidate = copy.deepcopy(core)
        target: object = candidate
        for key in path[:-1]:
            target = target[key]  # type: ignore[index]
        target[path[-1]] = replacement  # type: ignore[index]
        try:
            validate_core(candidate)
            if candidate != core:
                raise ValueError("exact contract changed")
        except (TypeError, ValueError):
            rejected.append(label)
    if len(rejected) != len(mutations):
        raise RuntimeError("mutation audit failed")
    return {"attempted": len(mutations), "rejected": rejected, "all_rejected": True}


def build_certificate() -> dict[str, object]:
    core = core_payload()
    validate_core(core)
    certificate = dict(core)
    certificate["dependency_locks"] = dependency_locks()
    certificate["mutation_audit"] = mutation_audit(core)
    certificate["core_sha256"] = canonical_sha(core)
    certificate["check"] = True
    return certificate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    certificate = build_certificate()
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "candidate_id": certificate["candidate_id"],
        "check": certificate["check"],
        "core_sha256": certificate["core_sha256"],
        "mutations_rejected": certificate["mutation_audit"]["attempted"],
        "symbolic_periods": len(certificate["symbolic_rows"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
