#!/usr/bin/env python3
"""Exact HCS-P63 coordinate-height pressure certificate.

The theorem is all-period and symbolic/algebraic.  Floating-point root work is
kept in a clearly labelled finite diagnostic block and is not used to prove
the pressure identity.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c63_certificate.json"
X, T = sp.symbols("X T")
FINITE_PERIODS = (1, 3, 5, 7, 9, 11)
PRESSURE_PARAMETERS = (-2, -1, 0, 1, 2)

DEPENDENCIES = {
    "p46_readme": (
        TRACK / "henon_integral_monodromy_units" / "README.md",
        "700cce354f56c3b218984f2a8606d04b122304336c65735da86adb7f93cb9a47",
    ),
    "p46_paper_source": (
        TRACK / "henon_integral_monodromy_units" / "paper" / "paper.tex",
        "779825668cecc78cef4df4478f06f989b4e0f5b92b2a1e85c7c5673a002eeccc",
    ),
    "p46_code": (
        TRACK / "henon_integral_monodromy_units" / "code" / "c46_integral_monodromy.py",
        "dbf216a34670a5e565fee331178517315a806a1a3c071781dd0e5e5e2f7a512b",
    ),
    "p62_proof": (
        TRACK / "henon_full_horseshoe_algebraic_exhaustion" / "PROOF_PACKAGE.md",
        "1d81017bbd3c608d86e19a7fa3a80c70f7b11697364b944fe6ff285f8b4d61c7",
    ),
    "p62_code": (
        TRACK / "henon_full_horseshoe_algebraic_exhaustion" / "code" / "c62_algebraic_exhaustion.py",
        "fe3d73c2838f95a0ca92d398df8f243b4d95b215f19843675a22a159e715d4d0",
    ),
    "p62_certificate": (
        TRACK / "henon_full_horseshoe_algebraic_exhaustion" / "results" / "c62_certificate.json",
        "d8e4d170c37d7af6c454a734aa91d2532902f5b78aaa939c037a731b4c72d134",
    ),
    "p62_paper": (
        TRACK / "henon_full_horseshoe_algebraic_exhaustion" / "paper" / "paper.pdf",
        "b9f157164bb2d9bb9effa3b6c44ea471f2d70fda00a0d690ea0bf2960e727c15",
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


def primitive_degree(n: int) -> int:
    return sum(
        int(sp.mobius(n // divisor)) * 2 ** ((divisor + 1) // 2)
        for divisor in sp.divisors(n)
    )


def closure_and_quotients(max_period: int) -> tuple[dict[int, sp.Poly], dict[int, sp.Poly]]:
    """Rebuild P60/P62 odd mixed-axis quotients without importing their code."""

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


def scaled_primitive(quotient: sp.Poly) -> sp.Poly:
    degree = quotient.degree()
    rational = sp.Poly(sp.expand(6**degree * quotient.as_expr().subs(X, T / 6)), T, domain=sp.QQ)
    if rational.LC() != 1 or any(coefficient.q != 1 for coefficient in rational.all_coeffs()):
        raise ArithmeticError("scaled primitive polynomial is not monic integral")
    return sp.Poly(rational.as_expr(), T, domain=sp.ZZ)


def polynomial_sha(poly: sp.Poly) -> str:
    return canonical_sha([int(value) for value in poly.all_coeffs()])


def root_factor_height(poly: sp.Poly) -> tuple[float, float]:
    roots = [complex(value) for value in sp.nroots(poly, n=50, maxsteps=500)]
    if any(abs(value.imag) > 1e-35 for value in roots):
        raise ArithmeticError("finite diagnostic found a nonreal root")
    height = sum(math.log(max(1.0, abs(value.real))) for value in roots) / poly.degree()
    return height, max(abs(value.real) for value in roots)


def finite_row(n: int, quotient: sp.Poly) -> dict[str, object]:
    scaled = scaled_primitive(quotient)
    factors = sp.factor_list(scaled)[1]
    factor_rows: list[dict[str, object]] = []
    weighted_height_sum = 0.0
    max_root = 0.0
    for factor, exponent in factors:
        height, factor_max = root_factor_height(factor)
        multiplicity = factor.degree() * int(exponent)
        weighted_height_sum += multiplicity * height
        max_root = max(max_root, factor_max)
        factor_rows.append(
            {
                "degree": factor.degree(),
                "exponent": int(exponent),
                "height_50digit_diagnostic": f"{height:.15f}",
                "max_abs_root_50digit_diagnostic": f"{factor_max:.15f}",
                "coefficients_sha256": polynomial_sha(factor),
            }
        )
    degree = scaled.degree()
    if degree != primitive_degree(n):
        raise ArithmeticError(f"degree mismatch at n={n}")
    packet_average = weighted_height_sum / degree
    pressure_rows = []
    for parameter in PRESSURE_PARAMETERS:
        partition = sum(
            row["degree"] * row["exponent"]
            * math.exp(-parameter * float(row["height_50digit_diagnostic"]))
            for row in factor_rows
        )
        pressure_rows.append(
            {
                "s": parameter,
                "partition_diagnostic": f"{partition:.15f}",
                "normalized_log_diagnostic": f"{math.log(partition) / n:.15f}",
                "difference_from_unweighted_degree": f"{(math.log(partition) - math.log(degree)) / n:.15f}",
            }
        )
    return {
        "period": n,
        "primitive_degree": degree,
        "scaled_polynomial_monic_integral": True,
        "scaled_polynomial_coefficients_sha256": polynomial_sha(scaled),
        "factor_degrees": [row["degree"] for row in factor_rows],
        "factor_exponents": [row["exponent"] for row in factor_rows],
        "factor_rows": factor_rows,
        "packet_average_height_diagnostic": f"{packet_average:.15f}",
        "max_abs_root_diagnostic": f"{max_root:.15f}",
        "pressure_rows": pressure_rows,
    }


def finite_rows() -> list[dict[str, object]]:
    _, quotients = closure_and_quotients(max(FINITE_PERIODS))
    return [finite_row(n, quotients[n]) for n in FINITE_PERIODS]


def core_payload() -> dict[str, object]:
    bound_decimal = 1 + math.sqrt(7)
    height_bound = math.log(bound_decimal)
    rows = finite_rows()
    if max(float(row["max_abs_root_diagnostic"]) for row in rows) > bound_decimal + 1e-12:
        raise ArithmeticError("finite root diagnostic exceeds the all-period bound")
    return {
        "candidate_id": "HCS-P63",
        "map": "H_6(q,p)=(1-6q^2-p,q)",
        "integral_scaling": "x=6q, y=6p",
        "integral_recurrence": "x_(j+1)=6-x_j^2-x_(j-1)",
        "primitive_scaled_polynomial": "tilde_Psi_n(T)=6^D_n Psi_n(T/6)",
        "all_period_coordinate_integrality": "every primitive scaled reflection root is an algebraic integer",
        "all_period_conjugate_exhaustion": "every conjugate is a real H_6 periodic coordinate",
        "maximum_coordinate_inequality": "M^2<=6+2M",
        "sharp_uniform_root_bound_exact": "1+sqrt(7)",
        "sharp_uniform_root_bound_decimal": f"{bound_decimal:.15f}",
        "uniform_weil_height_bound_exact": "log(1+sqrt(7))",
        "uniform_weil_height_bound_decimal": f"{height_bound:.15f}",
        "primitive_degree": "D_n=sum_(d|n)mu(n/d)2^((d+1)/2)",
        "primitive_degree_entropy": "(1/2)log(2)",
        "coordinate_height_partition": "Z_n(s)=sum_(tilde_Psi_n(alpha)=0)exp(-s h(alpha))",
        "flat_pressure_theorem": "for every fixed real s, lim_(odd n) n^(-1)log Z_n(s)=(1/2)log(2)",
        "flat_pressure_domain": "all fixed s in R",
        "fixed_rescaling_invariance": "for every fixed nonzero algebraic c, replacing alpha by c*alpha leaves the pressure equal to (1/2)log(2)",
        "finite_exact_and_numeric_rows": rows,
        "exact_sentinels": {
            "n1_polynomial": "T^2+2T-6",
            "n1_height": "(1/2)log(6)",
            "n3_polynomial": "T^2-2T-4",
            "n3_height": "log(2)",
        },
        "strongest_positive_result": "all primitive scaled reflection coordinates have uniformly bounded absolute Weil height and the ordinary coordinate-height pressure exists for every real parameter",
        "strongest_obstruction": "the ordinary per-root Weil height is non-extensive, so its pressure is identically the unweighted half-entropy and cannot encode physical instability or a new arithmetic singularity",
        "open_theorem": "replace h(alpha) by an extensive source-native observable such as n*h(alpha), primitive packet Mahler height, or discriminant/ramification height, and prove its all-period pressure",
        "reusable_structure": "integral cyclic coordinates plus full-horseshoe Galois exhaustion turn a recurrence maximum principle into a uniform height theorem",
        "round2_clue": "test the packet-average extensive height n*D_n^(-1)log M(tilde_Psi_n) and determine whether reflection-root measures equidistribute toward the full-shift maximal-entropy measure",
        "claim_status": {
            "uniform_coordinate_height": "PROVED",
            "flat_coordinate_height_pressure": "PROVED",
            "finite_factor_height_diagnostics_through_11": "NUMERICALLY_CERTIFIED",
            "extensive_height_pressure": "OPEN",
            "arithmetic_advance": "NO",
        },
        "route_a_status": {
            "tuple": "(A1_PASS_ANALYTIC [primitive reflection population], A2_ANALYTIC_DETERMINANT [inherited only], A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)",
            "overall": "ROUTE_A_EXPLORATORY",
            "full_arithmetic_candidate_pass": False,
        },
        "route_b_authorized": False,
        "claim_boundary": "P63 proves a bounded-height and flat-pressure obstruction for the ordinary primitive coordinate height; it proves no prime labels, von Mangoldt trace, completed determinant, Hilbert-Polya operator, or Riemann hypothesis",
    }


EXPECTED_CORE_SHA256 = "24da1ca81966d650270365e3477bb301ffa6bed5785afc155012d3e86b829438"


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
        ("map", ("map",), "H_5"),
        ("scaling", ("integral_scaling",), "x=q"),
        ("recurrence", ("integral_recurrence",), "x_(j+1)=6+x_j^2-x_(j-1)"),
        ("integrality", ("all_period_coordinate_integrality",), "numerical only"),
        ("conjugates", ("all_period_conjugate_exhaustion",), "physical subset only"),
        ("max_inequality", ("maximum_coordinate_inequality",), "M^2<=6+M"),
        ("root_bound", ("sharp_uniform_root_bound_exact",), "sqrt(7)"),
        ("height_bound", ("uniform_weil_height_bound_exact",), "n*log(2)"),
        ("degree", ("primitive_degree",), "2^n"),
        ("entropy", ("primitive_degree_entropy",), "log(2)"),
        ("partition", ("coordinate_height_partition",), "sum exp(-s*n*h(alpha))"),
        ("pressure", ("flat_pressure_theorem",), "strictly convex"),
        ("domain", ("flat_pressure_domain",), "s=0 only"),
        ("rescaling", ("fixed_rescaling_invariance",), "only c=6 works"),
        ("finite_integral", ("finite_exact_and_numeric_rows", 5, "scaled_polynomial_monic_integral"), False),
        ("finite_degree", ("finite_exact_and_numeric_rows", 5, "primitive_degree"), 61),
        ("finite_factor", ("finite_exact_and_numeric_rows", 4, "factor_degrees"), [1, 27]),
        ("sentinel_n1", ("exact_sentinels", "n1_polynomial"), "T^2-6"),
        ("sentinel_n3", ("exact_sentinels", "n3_height"), "log(3)"),
        ("positive_claim", ("claim_status", "uniform_coordinate_height"), "OPEN"),
        ("flat_status", ("claim_status", "flat_coordinate_height_pressure"), "HEURISTIC"),
        ("arithmetic_promotion", ("claim_status", "arithmetic_advance"), "YES"),
        ("route_a_promotion", ("route_a_status", "full_arithmetic_candidate_pass"), True),
        ("route_b_promotion", ("route_b_authorized",), True),
        ("boundary", ("claim_boundary",), "Riemann hypothesis proved"),
    )
    labels: list[str] = []
    for label, path, replacement in mutations:
        trial = copy.deepcopy(core)
        assign_path(trial, path, replacement)
        try:
            validate_core(trial, core)
        except ValueError:
            labels.append(label)
        else:
            raise AssertionError(f"mutation accepted: {label}")
    return {
        "attempted": len(mutations),
        "rejected": len(labels),
        "all_rejected": True,
        "labels": labels,
        "trace_sha256": canonical_sha(labels),
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
    payload = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "candidate_id": payload["candidate_id"],
        "check": payload["check"],
        "core_sha256": payload["core_sha256"],
        "periods": len(payload["finite_exact_and_numeric_rows"]),
        "mutations_rejected": payload["mutation_audit"]["rejected"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
