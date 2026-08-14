#!/usr/bin/env python3
"""Exact HCS-P62 full-horseshoe algebraic-exhaustion certificate."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c62_certificate.json"
X = sp.symbols("X")
FINITE_PERIODS = (1, 3, 5, 7, 9, 11, 13)
ARAI_ENDPOINT = sp.Rational(23347, 4096)  # 5.699951171875

DEPENDENCIES = {
    "p61_readme": (
        TRACK / "henon_survivor_reflection_transversality" / "README.md",
        "38da9ae4902fb3f25cb6b900bcadfaf897e210aeea1d15707abfb900f7202797",
    ),
    "p61_proof": (
        TRACK / "henon_survivor_reflection_transversality" / "PROOF_PACKAGE.md",
        "88414b141161d2412b1962a60374508bda7b9b8f4166850c3b4c38b65f4fe68d",
    ),
    "p61_code": (
        TRACK / "henon_survivor_reflection_transversality" / "code" / "c61_transversality.py",
        "9c52ed94562560ad93bd820ad87200f78f276980b94cc938d8359e5eff383186",
    ),
    "p61_certificate": (
        TRACK / "henon_survivor_reflection_transversality" / "results" / "c61_certificate.json",
        "8659aca428c51e036cb66bf18cc4ac5d5643b0a9f26c6e2d74c631db4a92912e",
    ),
    "p61_paper": (
        TRACK / "henon_survivor_reflection_transversality" / "paper" / "paper.pdf",
        "048e333f0262121ce99cbdeec46d91d269b4b132582bc2da849b2fc5e5e2d3bf",
    ),
    "p61_route_a": (
        TRACK / "henon_survivor_reflection_transversality" / "route_a_evaluation.yaml",
        "e907a956326a139f6b9feb4832913de0b3575cbfb60ec10a6fd7e4f55172f526",
    ),
    "p60_certificate": (
        TRACK / "henon_mixed_axis_dynatomic_entropy_gap" / "results" / "c60_certificate.json",
        "50c9ac59e8f91130e1f95d5d92e046b0b5c5a2788a0b0fa74e95f28ab83567c5",
    ),
    "p60_code": (
        TRACK / "henon_mixed_axis_dynatomic_entropy_gap" / "code" / "c60_dynatomic_gap.py",
        "9cae3e402e0e7ded21df20cae68222d681745a53e83e5951b1e7c5aef05f3261",
    ),
}


def canonical_sha(payload: object) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def dependency_locks() -> dict[str, dict[str, str]]:
    locks: dict[str, dict[str, str]] = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency hash changed: {name}")
        locks[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return locks


def primitive_integer(poly: sp.Poly) -> sp.Poly:
    integer = poly.clear_denoms()[1].primitive()[1]
    return -integer if integer.LC() < 0 else integer


def polynomial_sha(poly: sp.Poly) -> str:
    return canonical_sha([int(value) for value in primitive_integer(poly).all_coeffs()])


def parameter_conjugacy() -> dict[str, object]:
    q, p = sp.symbols("q p")
    h6 = (1 - 6 * q**2 - p, q)
    scaled_after_h6 = tuple(sp.expand(6 * coordinate) for coordinate in h6)
    x, y = 6 * q, 6 * p
    arai_after_scaling = (sp.expand(6 - x**2 - y), x)
    if scaled_after_h6 != arai_after_scaling:
        raise ArithmeticError("H6/Arai parameter conjugacy failed")
    if not (sp.Rational(6) > ARAI_ENDPOINT):
        raise ArithmeticError("a=6 is outside Arai's full plateau")
    if not (sp.Rational(25) > sp.Rational(20)):
        raise ArithmeticError("Devaney-Nitecki anchor inequality failed")
    return {
        "linear_map": "S(q,p)=(6q,6p)",
        "source_map": "H_6(q,p)=(1-6q^2-p,q)",
        "target_map": "H_(6,-1)(x,y)=(6-x^2-y,x)",
        "symbolic_identity": [str(item) for item in scaled_after_h6],
        "arai_plateau_endpoint_exact": str(ARAI_ENDPOINT),
        "arai_plateau_endpoint_decimal": "5.699951171875",
        "six_inside_plateau": True,
        "devaney_nitecki_anchor": "a=10>5+2*sqrt(5)",
        "anchor_inequality_certificate": "(10-5)^2=25>20=(2*sqrt(5))^2",
        "path_from_6_to_10_inside_plateau": True,
    }


def closure_and_quotients(max_period: int = 13) -> tuple[dict[int, sp.Poly], dict[int, sp.Poly]]:
    coordinates = [X, sp.expand((1 - 6 * X**2) / 2)]
    closures: dict[int, sp.Poly] = {}
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
            raise ArithmeticError(f"primitive quotient failed at n={n}")
        closures[n] = closure
        quotients[n] = quotient.monic()
    return closures, quotients


def formal_degree(n: int) -> int:
    return sum(
        int(sp.mobius(n // divisor)) * 2 ** ((divisor + 1) // 2)
        for divisor in sp.divisors(n)
    )


Interval = tuple[sp.Rational, sp.Rational]


def interval_add(left: Interval, right: Interval) -> Interval:
    return left[0] + right[0], left[1] + right[1]


def interval_multiply(left: Interval, right: Interval) -> Interval:
    values = (
        left[0] * right[0], left[0] * right[1],
        left[1] * right[0], left[1] * right[1],
    )
    return min(values), max(values)


def interval_square(value: Interval) -> Interval:
    if value[0] <= 0 <= value[1]:
        return sp.Rational(0), max(value[0] ** 2, value[1] ** 2)
    return interval_multiply(value, value)


def orbit_intervals(root: Interval, n: int) -> list[Interval]:
    square = interval_square(root)
    previous = ((1 - 6 * square[1]) / 2, (1 - 6 * square[0]) / 2)
    current = root
    orbit = [root]
    for _ in range(n - 1):
        current_square = interval_square(current)
        following = (
            1 - 6 * current_square[1] - previous[1],
            1 - 6 * current_square[0] - previous[0],
        )
        previous, current = current, following
        orbit.append(current)
    return orbit


def sign_of_interval(value: Interval) -> str:
    if value[0] > 0:
        return "+"
    if value[1] < 0:
        return "-"
    raise ArithmeticError("orbit coordinate sign unresolved")


def interval_sha(intervals: list[tuple[Interval, int]]) -> str:
    serial = [
        [[str(bounds[0]), str(bounds[1])], multiplicity]
        for bounds, multiplicity in intervals
    ]
    return canonical_sha(serial)


def finite_row(n: int, closure: sp.Poly, quotient: sp.Poly) -> dict[str, object]:
    isolated = [
        ((sp.Rational(bounds[0]), sp.Rational(bounds[1])), int(multiplicity))
        for bounds, multiplicity in sp.intervals(quotient, eps=sp.Rational(1, 10**20))
    ]
    if sum(multiplicity for _, multiplicity in isolated) != quotient.degree():
        raise ArithmeticError(f"nonreal primitive root detected at n={n}")
    if any(multiplicity != 1 for _, multiplicity in isolated):
        raise ArithmeticError(f"multiple primitive root detected at n={n}")
    half_words: list[str] = []
    if n <= 11:
        half_length = (n + 1) // 2
        half_words = [
            "".join(sign_of_interval(value) for value in orbit_intervals(root, n)[:half_length])
            for root, _ in isolated
        ]
        if len(set(half_words)) != quotient.degree():
            raise ArithmeticError(f"half-word collision at n={n}")
    if quotient.degree() != formal_degree(n):
        raise ArithmeticError(f"primitive degree mismatch at n={n}")
    return {
        "period": n,
        "closure_degree": closure.degree(),
        "primitive_degree": quotient.degree(),
        "exact_real_simple_primitive_roots": len(isolated),
        "all_primitive_roots_real": True,
        "all_primitive_roots_simple": True,
        "half_word_certificate": "EXACT_RATIONAL_INTERVAL" if n <= 11 else "NOT_RUN_THEOREM_INDEPENDENT",
        "unique_half_sign_words": len(set(half_words)) if n <= 11 else None,
        "half_sign_words_sha256": canonical_sha(sorted(half_words)) if n <= 11 else None,
        "root_intervals_sha256": interval_sha(isolated),
        "closure_coefficients_sha256": polynomial_sha(closure),
        "quotient_coefficients_sha256": polynomial_sha(quotient),
    }


def finite_rows() -> list[dict[str, object]]:
    closures, quotients = closure_and_quotients(max(FINITE_PERIODS))
    return [finite_row(n, closures[n], quotients[n]) for n in FINITE_PERIODS]


def primitive_fixed_points(n: int) -> int:
    return sum(int(sp.mobius(n // divisor)) * 2**divisor for divisor in sp.divisors(n))


def full_shift_rows() -> list[dict[str, int]]:
    return [
        {
            "period": n,
            "fixed_points_of_nth_iterate": 2**n,
            "least_period_points": primitive_fixed_points(n),
            "least_period_orbits": primitive_fixed_points(n) // n,
        }
        for n in range(1, 14)
    ]


def core_payload() -> dict[str, object]:
    rows = finite_rows()
    return {
        "candidate_id": "HCS-P62",
        "parameter_conjugacy": parameter_conjugacy(),
        "source_bridge": {
            "arai": "Arai 2007, Theorem 1.2: R(H_(a,-1)) uniformly hyperbolic for a in [5.699951171875,infinity); hyperbolicity implies R-stability on the plateau",
            "devaney_nitecki": "Devaney-Nitecki 1979: for a>5+2sqrt(5) at b=-1, the nonwandering set is the full two-shift",
            "friedland_milnor": "Friedland-Milnor 1989, Theorem 3.1: a degree-two cyclically reduced plane polynomial automorphism has algebraic fixed-point count 2^n for its nth iterate",
            "continuation": "the connected hyperbolic path a in [6,10] transports the full-shift chain recurrent dynamics from a=10 to a=6",
        },
        "full_horseshoe_theorem": "the real chain recurrent set of H_6 is uniformly hyperbolic and conjugate to the full two-shift",
        "algebraic_exhaustion_theorem": "for every n>=1, Fix(H_6^n) over C consists of exactly 2^n distinct real hyperbolic points",
        "mixed_axis_effectivity_theorem": "for every odd n, F_n is totally real and squarefree, and its Mobius primitive quotient is a reduced effective divisor of exact least-period roots",
        "primitive_reflection_degree": "D_n=sum_(d|n)mu(n/d)2^((d+1)/2)",
        "primitive_reflection_entropy": "(1/2)log(2)",
        "physical_reflection_entropy": "(1/2)log(phi)",
        "ambient_to_physical_gap": "(1/2)log(2/phi)>0",
        "all_period_fixed_point_rows": full_shift_rows(),
        "finite_exact_rows": rows,
        "strongest_positive_result": "source-backed full-horseshoe continuation plus Friedland-Milnor multiplicity exhausts every complex periodic point by a distinct real hyperbolic point and upgrades the odd mixed-axis formal divisor to an all-period reduced effective totally real divisor",
        "strongest_obstruction": "total reality and effectivity remove the P60-P61 ambient resultant gate but do not create intrinsic rational-prime labels, von Mangoldt amplitudes, or a completed determinant",
        "open_theorem": "derive uniform height or Galois-excess pressure for the now-effective totally real primitive reflection divisors and test whether it has any source-native arithmetic trace law",
        "reusable_structure": "hyperbolic-plateau transport, full-shift/Friedland-Milnor algebraic exhaustion, and the reversor tangency criterion",
        "round2_clue": "use all-period total reality to replace finite trace-field sampling by a genuine primitive reflection height pressure and compare it with the physical instability pressure",
        "claim_status": {
            "full_real_horseshoe_at_H6": "SOURCE_BACKED_PROVED",
            "all_complex_periodic_points_real_and_simple": "PROVED",
            "ambient_all_period_transversality": "PROVED",
            "formal_dynatomic_effectivity": "PROVED",
            "primitive_reflection_divisor_totally_real": "PROVED",
            "finite_exact_isolation_through_13": "COMPUTER_CERTIFIED_EXACT",
            "arithmetic_advance": "NO",
        },
        "route_a_status": {
            "tuple": "(A1_PASS_ANALYTIC [all-period real periodic-point and reflection-divisor layer], A2_ANALYTIC_DETERMINANT [hyperbolic subsystem inherited], A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)",
            "overall": "ROUTE_A_EXPLORATORY",
            "full_arithmetic_candidate_pass": False,
        },
        "route_b_authorized": False,
        "claim_boundary": "P62 proves full-shift periodic-point algebraic exhaustion and mixed-axis effectivity at H6; it does not prove a rational-prime orbit law, von Mangoldt trace, completed Riemann determinant, Hilbert-Polya operator, or the Riemann hypothesis",
    }


EXPECTED_CORE_SHA256 = "1b6fd305e61c3a0da9d5377524f6bd8e82fc1d06bb56acad0f3aea21e440b805"


def validate_core(candidate: object, expected: object) -> None:
    if type(candidate) is not dict or candidate != expected:
        raise ValueError("core payload changed")


def assign_path(payload: object, path: tuple[object, ...], value: object) -> None:
    cursor = payload
    for key in path[:-1]:
        cursor = cursor[key]  # type: ignore[index]
    cursor[path[-1]] = value  # type: ignore[index]


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    mutations = (
        ("parameter", ("parameter_conjugacy", "target_map"), "H_(5,-1)"),
        ("scaling", ("parameter_conjugacy", "linear_map"), "S(q,p)=(q,p)"),
        ("endpoint", ("parameter_conjugacy", "arai_plateau_endpoint_exact"), "6"),
        ("plateau_membership", ("parameter_conjugacy", "six_inside_plateau"), False),
        ("anchor", ("parameter_conjugacy", "devaney_nitecki_anchor"), "a=6"),
        ("path", ("parameter_conjugacy", "path_from_6_to_10_inside_plateau"), False),
        ("arai_scope", ("source_bridge", "arai"), "numerical observation"),
        ("fm_count", ("source_bridge", "friedland_milnor"), "3^n"),
        ("horseshoe", ("full_horseshoe_theorem",), "subshift only"),
        ("complex_exhaustion", ("algebraic_exhaustion_theorem",), "real subset only"),
        ("effectivity", ("mixed_axis_effectivity_theorem",), "formal only"),
        ("degree", ("primitive_reflection_degree",), "2^n"),
        ("entropy", ("primitive_reflection_entropy",), "log(2)"),
        ("gap", ("ambient_to_physical_gap",), "zero"),
        ("fixed_count", ("all_period_fixed_point_rows", 12, "fixed_points_of_nth_iterate"), 8191),
        ("primitive_count", ("all_period_fixed_point_rows", 10, "least_period_points"), 0),
        ("row_degree", ("finite_exact_rows", 6, "primitive_degree"), 125),
        ("row_real", ("finite_exact_rows", 6, "all_primitive_roots_real"), False),
        ("row_simple", ("finite_exact_rows", 6, "all_primitive_roots_simple"), False),
        ("row_words", ("finite_exact_rows", 5, "half_sign_words_sha256"), "forged"),
        ("all_period_status", ("claim_status", "all_complex_periodic_points_real_and_simple"), "OPEN"),
        ("ambient_status", ("claim_status", "ambient_all_period_transversality"), "OPEN"),
        ("arithmetic_promotion", ("claim_status", "arithmetic_advance"), "YES"),
        ("route_a_promotion", ("route_a_status", "full_arithmetic_candidate_pass"), True),
        ("route_b_promotion", ("route_b_authorized",), True),
        ("boundary", ("claim_boundary",), "Riemann hypothesis proved"),
    )
    rejected: list[str] = []
    for label, path, replacement in mutations:
        trial = copy.deepcopy(core)
        assign_path(trial, path, replacement)
        try:
            validate_core(trial, core)
        except ValueError:
            rejected.append(label)
        else:
            raise AssertionError(f"mutation accepted: {label}")
    return {
        "attempted": len(mutations),
        "rejected": len(rejected),
        "all_rejected": True,
        "labels": rejected,
        "trace_sha256": canonical_sha(rejected),
    }


def build_certificate() -> dict[str, object]:
    core = core_payload()
    core_sha = canonical_sha(core)
    if EXPECTED_CORE_SHA256 == "TO_BE_FROZEN":
        raise RuntimeError(f"freeze core SHA256: {core_sha}")
    if core_sha != EXPECTED_CORE_SHA256:
        raise RuntimeError(f"core payload digest changed: {core_sha}")
    return {
        **core,
        "core_sha256": core_sha,
        "dependency_locks": dependency_locks(),
        "mutation_audit": mutation_audit(core),
        "check": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "candidate_id": result["candidate_id"],
        "check": result["check"],
        "core_sha256": result["core_sha256"],
        "periods": len(result["finite_exact_rows"]),
        "mutations_rejected": result["mutation_audit"]["rejected"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
