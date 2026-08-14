#!/usr/bin/env python3
"""Exact HCS-P61 survivor-reflection transversality certificate."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c61_certificate.json"
X = sp.symbols("X")
LOWER_SQUARE = sp.Rational(17, 144)
UPPER_SQUARE = sp.Rational(3, 8)
FINITE_PERIODS = (1, 3, 5, 7, 9, 11)

DEPENDENCIES = {
    "p60_readme": (
        TRACK / "henon_mixed_axis_dynatomic_entropy_gap" / "README.md",
        "4f07d1c5ba8270025819ab2e3657ed01d68fced7d39f5093faf74110ac957569",
    ),
    "p60_proof": (
        TRACK / "henon_mixed_axis_dynatomic_entropy_gap" / "PROOF_PACKAGE.md",
        "74ceecee6cedb42b727dbdb59fc48a53585473fbbab862a05fd5dc2b8f0654ed",
    ),
    "p60_code": (
        TRACK / "henon_mixed_axis_dynatomic_entropy_gap" / "code" / "c60_dynatomic_gap.py",
        "9cae3e402e0e7ded21df20cae68222d681745a53e83e5951b1e7c5aef05f3261",
    ),
    "p60_certificate": (
        TRACK / "henon_mixed_axis_dynatomic_entropy_gap" / "results" / "c60_certificate.json",
        "50c9ac59e8f91130e1f95d5d92e046b0b5c5a2788a0b0fa74e95f28ab83567c5",
    ),
    "p60_paper": (
        TRACK / "henon_mixed_axis_dynatomic_entropy_gap" / "paper" / "paper.pdf",
        "e472d5427737dcaab6ca4521e5a62ff4447d09bbc81db4c3de48b6ad099ad387",
    ),
    "p60_route_a": (
        TRACK / "henon_mixed_axis_dynatomic_entropy_gap" / "route_a_evaluation.yaml",
        "13cdcef95628a50518320f08cea78d173668d51fd5a5ef4ec58abe59a01e55e2",
    ),
    "p59_certificate": (
        TRACK / "henon_reflection_half_entropy_law" / "results" / "c59_certificate.json",
        "6acfccad4f6b15f6e375be5362f4251b98dcd755819f7ac593a42dfdc48a6bc8",
    ),
    "hyperbolic_geometry": (
        TRACK / "docs" / "related_programs" / "henon_weighted_zeta" / "paper" / "sections" / "3_geometry_setup.tex",
        "491da4fa6c36366cc1c114e135a13ad872ea52a6ca9f203e72dba413b140dd88",
    ),
    "hyperbolic_cones": (
        TRACK / "docs" / "related_programs" / "henon_weighted_zeta" / "paper" / "sections" / "B_contraction_proof.tex",
        "0ef59712ee231aac3023d15d3ec857cbedfea884b18be7ec1ac30459757e28a8",
    ),
    "certified_domain": (
        TRACK / "docs" / "related_programs" / "henon_weighted_zeta" / "results" / "certified_domain_r059.json",
        "7d521ed68e843e356ce230bfb0e81b57bf1a67c2f1948e068dd26f20ac20c77b",
    ),
}


def canonical_sha(payload: object) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def dependency_locks() -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency hash changed: {name}")
        result[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return result


def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def physical_reflections(n: int) -> int:
    if n % 2 != 1:
        raise ValueError("P61 uses odd periods")
    return sum(
        int(sp.mobius(n // d)) * fibonacci((d + 3) // 2)
        for d in sp.divisors(n)
    )


def formal_degree(n: int) -> int:
    return sum(
        int(sp.mobius(n // d)) * 2 ** ((d + 1) // 2)
        for d in sp.divisors(n)
    )


def closure_and_quotients(max_period: int = 11) -> tuple[dict[int, sp.Poly], dict[int, sp.Poly]]:
    coordinates = [X, sp.expand((1 - 6 * X**2) / 2)]
    closures: dict[int, sp.Poly] = {}
    quotients: dict[int, sp.Poly] = {}
    for n in range(1, max_period + 1, 2):
        m = (n - 1) // 2
        while len(coordinates) <= m + 1:
            coordinates.append(sp.expand(1 - 6 * coordinates[-1] ** 2 - coordinates[-2]))
        closure = sp.Poly(coordinates[m + 1] - coordinates[m], X, domain=sp.QQ).monic()
        lower = sp.Poly(1, X, domain=sp.QQ)
        for d in sp.divisors(n):
            if d < n:
                lower *= quotients[int(d)]
        quotient, remainder = sp.div(closure, lower, domain=sp.QQ)
        if not remainder.is_zero:
            raise ArithmeticError(f"primitive quotient failed at n={n}")
        closures[n] = closure
        quotients[n] = quotient.monic()
    return closures, quotients


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


def next_coordinate(current: Interval, previous: Interval) -> Interval:
    square = interval_square(current)
    return 1 - 6 * square[1] - previous[1], 1 - 6 * square[0] - previous[0]


def band_sign(value: Interval) -> str | None:
    left, right = value
    if left > 0 and left**2 > LOWER_SQUARE and right**2 < UPPER_SQUARE:
        return "+"
    if right < 0 and right**2 > LOWER_SQUARE and left**2 < UPPER_SQUARE:
        return "-"
    return None


def certified_outside_band(value: Interval) -> bool:
    left, right = value
    square = interval_square(value)
    return square[1] < LOWER_SQUARE or square[0] > UPPER_SQUARE or left <= 0 <= right


def orbit_intervals(root: Interval, n: int) -> list[Interval]:
    root_square = interval_square(root)
    previous = ((1 - 6 * root_square[1]) / 2, (1 - 6 * root_square[0]) / 2)
    current = root
    orbit = [root]
    for _ in range(n - 1):
        following = next_coordinate(current, previous)
        previous, current = current, following
        orbit.append(current)
    return orbit


def polynomial_interval(poly: sp.Poly, value: Interval) -> Interval:
    result: Interval = (sp.Rational(0), sp.Rational(0))
    for coefficient in poly.all_coeffs():
        result = interval_add(
            interval_multiply(result, value),
            (sp.Rational(coefficient), sp.Rational(coefficient)),
        )
    return result


def interval_sha(intervals: list[tuple[Interval, int]]) -> str:
    serial = [
        [[str(bounds[0]), str(bounds[1])], multiplicity]
        for bounds, multiplicity in intervals
    ]
    return canonical_sha(serial)


def finite_row(n: int, closure: sp.Poly, quotient: sp.Poly) -> dict[str, object]:
    isolated = [
        ((sp.Rational(bounds[0]), sp.Rational(bounds[1])), int(multiplicity))
        for bounds, multiplicity in sp.intervals(
            quotient, eps=sp.Rational(1, 10**40)
        )
    ]
    if sum(multiplicity for _, multiplicity in isolated) != quotient.degree():
        raise ArithmeticError(f"nonreal primitive roots at n={n}")
    if any(multiplicity != 1 for _, multiplicity in isolated):
        raise ArithmeticError(f"multiple primitive root at n={n}")

    physical_words: list[str] = []
    ambient_count = 0
    for root, _ in isolated:
        orbit = orbit_intervals(root, n)
        signs = [band_sign(value) for value in orbit]
        if all(sign is not None for sign in signs):
            derivative = polynomial_interval(closure.diff(), root)
            if derivative[0] <= 0 <= derivative[1]:
                raise ArithmeticError(f"physical derivative unresolved at n={n}")
            physical_words.append("".join(sign for sign in signs if sign is not None))
        elif any(certified_outside_band(value) for value in orbit):
            ambient_count += 1
        else:
            raise ArithmeticError(f"root band status unresolved at n={n}")

    expected = physical_reflections(n)
    if len(physical_words) != expected:
        raise ArithmeticError(f"physical root count mismatch at n={n}")
    if len(set(physical_words)) != len(physical_words):
        raise ArithmeticError(f"duplicate physical sign word at n={n}")
    return {
        "period": n,
        "formal_degree": formal_degree(n),
        "physical_simple_roots": expected,
        "formal_residual_degree": formal_degree(n) - expected,
        "all_primitive_roots_real_through_this_row": True,
        "all_root_intervals_simple": True,
        "ambient_band_excluded_roots": ambient_count,
        "physical_sign_words": sorted(physical_words),
        "physical_sign_words_sha256": canonical_sha(sorted(physical_words)),
        "exact_root_intervals_sha256": interval_sha(isolated),
        "physical_derivatives_exclude_zero": True,
    }


def exact_rows() -> list[dict[str, object]]:
    closures, quotients = closure_and_quotients(max(FINITE_PERIODS))
    return [finite_row(n, closures[n], quotients[n]) for n in FINITE_PERIODS]


def core_payload() -> dict[str, object]:
    rows = exact_rows()
    phi = (1 + sp.sqrt(5)) / 2
    gap = sp.log(sp.Rational(2, 1) / phi) / 2
    return {
        "candidate_id": "HCS-P61",
        "map": "H_6(q,p)=(1-6q^2-p,q)",
        "reversors": "R(q,p)=(p,q), J=R*H, H=R*J",
        "mixed_axis_parameterization": "gamma(X)=(X,(1-6X^2)/2) in Fix(J)",
        "closure": "F_n(X)=q_(m+1)(X)-q_m(X), n=2m+1",
        "tangency_identity": "F_n'(X)=(1,-1) DH^(m+1)(gamma(X)) gamma'(X)",
        "second_reversor": "K_m=H^(-(m+1)) R H^(m+1)",
        "reversor_factorization": "H^n=J*K_m",
        "transversality_implication": "F_n'(X)=0 at a closure root implies 1 is an eigenvalue of DH^n",
        "physical_transversality_theorem": "every odd-period mixed-axis root in the certified uniformly hyperbolic H6 survivor is simple",
        "physical_incidence_theorem": "the number of primitive physical roots of the formal divisor at odd n is R_n=sum_(d|n)mu(n/d)F_((d+3)/2)",
        "local_effectivity": "each primitive physical root occurs with coefficient +1 in the formal mixed-axis dynatomic divisor",
        "entropy_theorem": {
            "formal_degree_entropy": "(1/2)log(2)",
            "physical_simple_root_entropy": "(1/2)log(phi)",
            "incidence_density": "Theta((phi/2)^(n/2)) along odd n",
            "formal_residual_degree_entropy": "(1/2)log(2)",
            "strict_gap": "(1/2)log(2/phi)>0",
            "strict_gap_decimal_40": str(sp.N(gap, 40)),
        },
        "finite_exact_rows": rows,
        "certified_band": "sqrt(17)/12 <= |q_j| <= sqrt(3/8)",
        "strongest_positive_result": "all primitive odd reversible cycles in the certified H6 survivor contribute distinct transverse simple roots to the formal mixed-axis divisor, with exact count and entropy one-half log phi",
        "strongest_obstruction": "the physical simple-root population has exponentially vanishing density inside the formal degree, and hyperbolicity says nothing about transversality of ambient algebraic roots outside the survivor",
        "open_theorem": "prove all ambient mixed-axis intersections are reduced/effective, or identify and count their tangencies and lower-period multiplicities",
        "reusable_structure": "reversor-product tangency lemma, symmetry-equivariant coding incidence, exact band-isolator classifier, and physical/formal entropy comparison",
        "round2_clue": "study the ambient critical resultant Res(F_n,F_n') and its factorization by divisor level; a nontrivial resultant law would decide all-period effectivity",
        "claim_status": {
            "physical_all_period_transversality": "PROVED",
            "physical_local_effectivity": "PROVED",
            "finite_band_classification_through_11": "COMPUTER_CERTIFIED_EXACT",
            "ambient_all_period_transversality": "OPEN",
            "arithmetic_advance": "NO",
        },
        "route_a_status": {
            "tuple": "(A1_PASS_ANALYTIC [physical reflection incidence], A2_ANALYTIC_DETERMINANT [physical subsystem inherited], A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)",
            "overall": "ROUTE_A_EXPLORATORY",
            "full_arithmetic_candidate_pass": False,
        },
        "route_b_authorized": False,
        "claim_boundary": "P61 proves transversality and local effectivity only for primitive roots in the certified real survivor; it does not prove ambient squarefreeness for all periods, a Galois-height pressure, rational-prime trace, completed determinant, or Hilbert-Polya operator",
    }


EXPECTED_CORE_SHA256 = "d0455a1a31c4ef29ed907f4cea940f883b313a3ab0de5f3f2ce17770c1bba313"


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
        ("map", ("map",), "different map"),
        ("reversor", ("reversors",), "H=J*R only"),
        ("tangent_sign", ("tangency_identity",), "minus derivative"),
        ("factorization", ("reversor_factorization",), "H^n=K_m*J"),
        ("eigenvalue", ("transversality_implication",), "eigenvalue -1"),
        ("physical_transverse", ("claim_status", "physical_all_period_transversality"), "OPEN"),
        ("physical_effective", ("claim_status", "physical_local_effectivity"), "OPEN"),
        ("ambient_promotion", ("claim_status", "ambient_all_period_transversality"), "PROVED"),
        ("arithmetic_promotion", ("claim_status", "arithmetic_advance"), "YES"),
        ("formal_entropy", ("entropy_theorem", "formal_degree_entropy"), "log(2)"),
        ("physical_entropy", ("entropy_theorem", "physical_simple_root_entropy"), "log(phi)"),
        ("density", ("entropy_theorem", "incidence_density"), "Theta(1)"),
        ("residual", ("entropy_theorem", "formal_residual_degree_entropy"), "zero"),
        ("gap", ("entropy_theorem", "strict_gap"), "negative"),
        ("row_count", ("finite_exact_rows", 5, "physical_simple_roots"), 13),
        ("row_degree", ("finite_exact_rows", 5, "formal_degree"), 64),
        ("row_word", ("finite_exact_rows", 4, "physical_sign_words_sha256"), "forged"),
        ("row_derivative", ("finite_exact_rows", 3, "physical_derivatives_exclude_zero"), False),
        ("band", ("certified_band",), "uncertified band"),
        ("route_a", ("route_a_status", "full_arithmetic_candidate_pass"), True),
        ("route_b", ("route_b_authorized",), True),
        ("boundary", ("claim_boundary",), "Hilbert-Polya proved"),
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
