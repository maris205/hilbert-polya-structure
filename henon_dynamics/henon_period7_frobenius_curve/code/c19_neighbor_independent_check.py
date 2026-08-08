#!/usr/bin/env python3
"""Independent exact checker for the HCS-C19 neighbor correspondence.

This file deliberately does not import the producer, the neighbor-certificate
producer, or ``galois``.  It reconstructs the frozen septic, performs the
generic subresultant reduction over Q(sigma), and checks the exact F_103 and
F_43 fibres from first principles.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import time
from typing import Any, Iterable

import sympy as sp


SOURCE_SCHEMA = "HCS-C19-neighbor-correspondence-1"
CHECK_SCHEMA = "HCS-C19-neighbor-independent-check-1"
HASH_KEYS = {
    "P_sha256",
    "quadratic_subresultant_sha256",
    "quadratic_discriminant_sha256",
    "generic_loop_value_sha256",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_type(value: Any, expected: type, path: str) -> None:
    require(type(value) is expected, f"{path}: expected {expected.__name__}, got {type(value).__name__}")


def require_exact_keys(value: Any, expected: Iterable[str], path: str) -> dict[str, Any]:
    require_type(value, dict, path)
    expected_set = set(expected)
    actual_set = set(value)
    require(
        actual_set == expected_set,
        f"{path}: missing={sorted(expected_set - actual_set)}, extra={sorted(actual_set - expected_set)}",
    )
    return value


def require_list(value: Any, item_type: type, length: int, path: str) -> list[Any]:
    require_type(value, list, path)
    require(len(value) == length, f"{path}: expected length {length}, got {len(value)}")
    for index, item in enumerate(value):
        require_type(item, item_type, f"{path}[{index}]")
    return value


def require_sha256(value: Any, path: str) -> None:
    require_type(value, str, path)
    require(len(value) == 64 and all(character in "0123456789abcdef" for character in value), f"{path}: invalid SHA-256")


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def orbit_polynomial() -> tuple[sp.Symbol, sp.Symbol, sp.Expr, sp.Expr]:
    """Reconstruct (x, sigma, a, P) without importing a project module."""
    x, sigma = sp.symbols("x sigma")
    a = sigma**2 - 2 * sigma
    polynomial = (
        x**7
        - sigma * x**6
        - (3 * a - 2 * sigma) * x**5
        - (2 * a - (3 * a - 4) * sigma - 4) * x**4
        + (3 * a**2 - 2 * (2 * a - 1) * sigma + 1) * x**3
        + (4 * a**2 - 10 * a - (3 * a**2 - 8 * a + 1) * sigma - 2) * x**2
        - (a - 1) * (a**2 - 2 * a * sigma + a + 2) * x
        - 2 * a**3
        + 6 * a**2
        + 2 * a
        + 3
        + (a**3 - 4 * a**2 + a - 2) * sigma
    )
    return x, sigma, a, sp.expand(polynomial)


def validate_adjacency(value: Any, roots: list[int], path: str) -> None:
    adjacency = require_exact_keys(value, {str(root) for root in roots}, path)
    for root in roots:
        neighbors = require_list(adjacency[str(root)], int, 2, f"{path}.{root}")
        require(neighbors == sorted(set(neighbors)), f"{path}.{root}: neighbors are not sorted and distinct")
        require(root not in neighbors and all(neighbor in roots for neighbor in neighbors), f"{path}.{root}: invalid neighbor")
    for root in roots:
        for neighbor in adjacency[str(root)]:
            require(root in adjacency[str(neighbor)], f"{path}: adjacency is not symmetric")


def validate_neighbor_certificate_schema(payload: Any) -> None:
    top = require_exact_keys(
        payload,
        {
            "schema_version",
            "candidate_id",
            "object_scope",
            "symbolic",
            "exact_fibre_witness",
            "regular_split_fibre_control",
            "claim_boundary",
        },
        "$",
    )
    require(top["schema_version"] == SOURCE_SCHEMA, "neighbor source schema mismatch")
    require(top["candidate_id"] == "HCS-C19", "neighbor candidate mismatch")
    require(
        top["object_scope"] == "generic neighbor correspondence of the frozen septic; no Riemann data",
        "neighbor object scope changed",
    )

    symbolic = require_exact_keys(
        top["symbolic"],
        {
            "base_field",
            "quotient_field",
            "P_sha256",
            "subresultant_reduction",
            "generic_gcd_degree_in_y",
            "quadratic_subresultant_sha256",
            "reduced_coefficient_sha256",
            "neighbor_sum_identity",
            "neighbor_sum_remainder_zero",
            "quadratic_discriminant_nonzero_mod_Px",
            "quadratic_discriminant_sha256",
            "generic_loop_value_nonzero_mod_Px",
            "generic_loop_value_sha256",
            "generic_graph_argument",
            "oriented_edge_cover",
        },
        "$.symbolic",
    )
    require(symbolic["base_field"] == "Q(sigma)", "base-field declaration mismatch")
    require(symbolic["quotient_field"] == "Q(sigma)[x]/(P(sigma,x))", "quotient-field declaration mismatch")
    for key in HASH_KEYS:
        require_sha256(symbolic[key], f"$.symbolic.{key}")
    coefficient_hashes = require_list(symbolic["reduced_coefficient_sha256"], str, 3, "$.symbolic.reduced_coefficient_sha256")
    for index, value in enumerate(coefficient_hashes):
        require_sha256(value, f"$.symbolic.reduced_coefficient_sha256[{index}]")
    reductions = require_list(symbolic["subresultant_reduction"], dict, 9, "$.symbolic.subresultant_reduction")
    expected_degrees = [14, 7, 6, 5, 4, 3, 2, 1, 0]
    expected_zero = [False] * 7 + [True, True]
    for index, row in enumerate(reductions):
        require_exact_keys(row, {"degree_in_y", "zero_mod_Px"}, f"$.symbolic.subresultant_reduction[{index}]")
        require_type(row["degree_in_y"], int, f"$.symbolic.subresultant_reduction[{index}].degree_in_y")
        require_type(row["zero_mod_Px"], bool, f"$.symbolic.subresultant_reduction[{index}].zero_mod_Px")
        require(row["degree_in_y"] == expected_degrees[index], "subresultant degree ledger mismatch")
        require(row["zero_mod_Px"] is expected_zero[index], "subresultant zero ledger mismatch")
    require(symbolic["generic_gcd_degree_in_y"] == 2, "generic neighbor gcd degree mismatch")
    require(symbolic["neighbor_sum_identity"] == "y_1 + y_2 = a - x^2", "neighbor-sum declaration mismatch")
    for key in (
        "neighbor_sum_remainder_zero",
        "quadratic_discriminant_nonzero_mod_Px",
        "generic_loop_value_nonzero_mod_Px",
    ):
        require_type(symbolic[key], bool, f"$.symbolic.{key}")
        require(symbolic[key], f"$.symbolic.{key} is false")
    require(
        symbolic["generic_graph_argument"]
        == {
            "vertices": 7,
            "degree": 2,
            "simple_on_a_good_fibre": True,
            "geometric_monodromy_transitive": True,
            "prime_degree_forces_one_component": True,
            "generic_component": "7-cycle",
        },
        "generic graph argument ledger mismatch",
    )
    require(
        symbolic["oriented_edge_cover"]
        == {
            "generic_degree_over_sigma": 14,
            "tau": "tau(x,y) = (a - x^2 - y, x)",
            "generic_tau_order": 7,
            "time_reversal": "R(x,y) = (y,x)",
            "dihedral_relation": "R tau R = tau^-1",
        },
        "oriented-edge-cover ledger mismatch",
    )

    exact = require_exact_keys(
        top["exact_fibre_witness"],
        {"field", "sigma", "a", "roots", "adjacency", "oriented_edge_count", "tau_cycles"},
        "$.exact_fibre_witness",
    )
    require(exact["field"] == "F_103" and exact["sigma"] == 26 and exact["a"] == 6, "F_103 witness parameters mismatch")
    roots103 = require_list(exact["roots"], int, 7, "$.exact_fibre_witness.roots")
    require(roots103 == [10, 17, 31, 54, 58, 67, 98], "F_103 root ledger mismatch")
    validate_adjacency(exact["adjacency"], roots103, "$.exact_fibre_witness.adjacency")
    require(exact["oriented_edge_count"] == 14, "F_103 oriented-edge count mismatch")
    cycles = require_list(exact["tau_cycles"], list, 2, "$.exact_fibre_witness.tau_cycles")
    for cycle_index, cycle in enumerate(cycles):
        require_list(cycle, list, 7, f"$.exact_fibre_witness.tau_cycles[{cycle_index}]")
        for state_index, state in enumerate(cycle):
            require_list(state, int, 2, f"$.exact_fibre_witness.tau_cycles[{cycle_index}][{state_index}]")

    control = require_exact_keys(
        top["regular_split_fibre_control"],
        {"field", "sigma", "a", "discriminant_mod_43", "roots", "adjacency", "oriented_cycle", "exact_tau_order", "cycle_sum"},
        "$.regular_split_fibre_control",
    )
    require(control["field"] == "F_43" and control["sigma"] == 7 and control["a"] == 35, "F_43 control parameters mismatch")
    require(control["discriminant_mod_43"] == 13, "F_43 discriminant ledger mismatch")
    roots43 = require_list(control["roots"], int, 7, "$.regular_split_fibre_control.roots")
    require(roots43 == [8, 16, 23, 24, 29, 38, 41], "F_43 root ledger mismatch")
    validate_adjacency(control["adjacency"], roots43, "$.regular_split_fibre_control.adjacency")
    require(control["oriented_cycle"] == [8, 16, 29, 38, 24, 23, 41], "F_43 oriented cycle mismatch")
    require(control["exact_tau_order"] == 7 and control["cycle_sum"] == 7, "F_43 tau/cycle-sum ledger mismatch")

    require(
        top["claim_boundary"]
        == {
            "generic_henon_recurrence_recovered_from_frozen_P": True,
            "source_literal_formula_refuted": True,
            "published_erratum_claimed": False,
            "selected_prime_good_reduction_claimed": False,
            "riemann_or_hilbert_polya_claimed": False,
        },
        "neighbor claim boundary changed",
    )


def canonical_cycle(cycle: list[tuple[int, int]]) -> list[list[int]]:
    rotations = [cycle[index:] + cycle[:index] for index in range(len(cycle))]
    return [[int(x), int(y)] for x, y in min(rotations)]


def finite_fibre_audit(
    polynomial: sp.Expr,
    x: sp.Symbol,
    sigma: sp.Symbol,
    modulus: int,
    sigma_value: int,
    a_value: int,
) -> tuple[list[int], dict[str, list[int]], list[list[list[int]]]]:
    roots = [
        value
        for value in range(modulus)
        if int(polynomial.subs({sigma: sigma_value, x: value})) % modulus == 0
    ]
    require(len(roots) == 7 and len(set(roots)) == 7, f"F_{modulus} fibre is not split with seven distinct roots")
    root_set = set(roots)
    adjacency = {
        str(fixed_x): sorted(
            candidate_y
            for candidate_y in roots
            if (a_value - candidate_y**2 - fixed_x) % modulus in root_set
        )
        for fixed_x in roots
    }
    for fixed_x in roots:
        neighbors = adjacency[str(fixed_x)]
        require(len(neighbors) == 2 and fixed_x not in neighbors, f"F_{modulus} graph is not simple 2-regular")
        require(sum(neighbors) % modulus == (a_value - fixed_x**2) % modulus, f"F_{modulus} neighbor sum failed")
        require(all(fixed_x in adjacency[str(neighbor)] for neighbor in neighbors), f"F_{modulus} adjacency is not symmetric")

    oriented_edges = {(fixed_x, neighbor) for fixed_x in roots for neighbor in adjacency[str(fixed_x)]}

    def tau(state: tuple[int, int]) -> tuple[int, int]:
        current, previous = state
        return (a_value - current**2 - previous) % modulus, current

    unseen = set(oriented_edges)
    cycles: list[list[list[int]]] = []
    while unseen:
        start = min(unseen)
        state = start
        cycle: list[tuple[int, int]] = []
        while state not in cycle:
            require(state in oriented_edges, f"tau leaves the F_{modulus} oriented-edge cover")
            cycle.append(state)
            unseen.discard(state)
            state = tau(state)
        require(state == start and len(cycle) == 7, f"tau does not have exact order seven over F_{modulus}")
        cycles.append(canonical_cycle(cycle))
    cycles.sort()
    require(len(cycles) == 2, f"F_{modulus} oriented-edge cover does not have two orientation cycles")
    return roots, adjacency, cycles


def compute_neighbor_audit() -> dict[str, Any]:
    x, sigma, a, polynomial = orbit_polynomial()
    y = sp.symbols("y")
    coefficient_field = sp.QQ.frac_field(sigma)
    p_modulus = sp.Poly(polynomial, x, domain=coefficient_field)
    p_y = sp.expand(polynomial.subs(x, y))
    p_next = sp.expand(polynomial.subs(x, a - y**2 - x))
    subresultants = sp.subresultants(p_y, p_next, y)

    reduction_rows: list[dict[str, Any]] = []
    last_nonzero: tuple[sp.Poly, list[sp.Poly]] | None = None
    for subresultant in subresultants:
        polynomial_y = sp.Poly(subresultant, y)
        reduced = [
            sp.Poly(coefficient, x, domain=coefficient_field).rem(p_modulus)
            for coefficient in polynomial_y.all_coeffs()
        ]
        zero = all(coefficient.is_zero for coefficient in reduced)
        reduction_rows.append({"degree_in_y": int(polynomial_y.degree()), "zero_mod_Px": bool(zero)})
        if not zero:
            last_nonzero = polynomial_y, reduced
    require(
        reduction_rows
        == [
            {"degree_in_y": degree, "zero_mod_Px": zero}
            for degree, zero in zip([14, 7, 6, 5, 4, 3, 2, 1, 0], [False] * 7 + [True, True])
        ],
        "independent generic subresultant degree pattern failed",
    )
    require(last_nonzero is not None and last_nonzero[0].degree() == 2, "missing independent quadratic subresultant")
    quadratic, coefficients = last_nonzero
    c2, c1, c0 = coefficients
    require(not c2.is_zero, "quadratic leading coefficient vanishes modulo P")
    neighbor_sum_remainder = (
        c1 - c2 * sp.Poly(x**2 - a, x, domain=coefficient_field)
    ).rem(p_modulus)
    require(neighbor_sum_remainder.is_zero, "independent neighbor-sum identity failed")
    discriminant = (c1 * c1 - 4 * c2 * c0).rem(p_modulus)
    loop_value = (
        c2 * sp.Poly(x**2, x, domain=coefficient_field)
        + c1 * sp.Poly(x, x, domain=coefficient_field)
        + c0
    ).rem(p_modulus)
    require(not discriminant.is_zero, "independent quadratic discriminant vanishes")
    require(not loop_value.is_zero, "independent generic loop value vanishes")

    roots103, adjacency103, cycles103 = finite_fibre_audit(polynomial, x, sigma, 103, 26, 6)
    roots43, adjacency43, cycles43 = finite_fibre_audit(polynomial, x, sigma, 43, 7, 35)
    q6 = 64 * sigma**6 - 448 * sigma**5 + 848 * sigma**4 + 80 * sigma**3 - 1048 * sigma**2 + 152 * sigma - 151
    discriminant43 = int(((4 * sigma - 9) ** 2 * q6**3).subs(sigma, 7)) % 43
    require(discriminant43 == 13, "F_43 control is not a regular fibre")
    chosen_cycle = [8, 16, 29, 38, 24, 23, 41]
    require(
        all(
            chosen_cycle[(index + 1) % 7]
            == (35 - chosen_cycle[index] ** 2 - chosen_cycle[index - 1]) % 43
            for index in range(7)
        ),
        "F_43 chosen orientation fails tau recurrence",
    )
    require(sum(chosen_cycle) % 43 == 7, "F_43 chosen orientation has wrong sigma sum")
    require(
        canonical_cycle([(chosen_cycle[index], chosen_cycle[index - 1]) for index in range(7)]) in cycles43,
        "F_43 chosen orientation is absent from the oriented-edge cycles",
    )

    quadratic_text = str(sp.expand(quadratic.as_expr()))
    return {
        "symbolic": {
            "base_field": "Q(sigma)",
            "quotient_field": "Q(sigma)[x]/(P(sigma,x))",
            "P_sha256": sha256_text(str(polynomial)),
            "subresultant_reduction": reduction_rows,
            "generic_gcd_degree_in_y": 2,
            "quadratic_subresultant_sha256": sha256_text(quadratic_text),
            "reduced_coefficient_sha256": [
                sha256_text(str(sp.cancel(coefficient.as_expr()))) for coefficient in coefficients
            ],
            "neighbor_sum_identity": "y_1 + y_2 = a - x^2",
            "neighbor_sum_remainder_zero": True,
            "quadratic_discriminant_nonzero_mod_Px": True,
            "quadratic_discriminant_sha256": sha256_text(str(sp.cancel(discriminant.as_expr()))),
            "generic_loop_value_nonzero_mod_Px": True,
            "generic_loop_value_sha256": sha256_text(str(sp.cancel(loop_value.as_expr()))),
            "generic_graph_argument": {
                "vertices": 7,
                "degree": 2,
                "simple_on_a_good_fibre": True,
                "geometric_monodromy_transitive": True,
                "prime_degree_forces_one_component": True,
                "generic_component": "7-cycle",
            },
            "oriented_edge_cover": {
                "generic_degree_over_sigma": 14,
                "tau": "tau(x,y) = (a - x^2 - y, x)",
                "generic_tau_order": 7,
                "time_reversal": "R(x,y) = (y,x)",
                "dihedral_relation": "R tau R = tau^-1",
            },
        },
        "exact_fibre_witness": {
            "field": "F_103",
            "sigma": 26,
            "a": 6,
            "roots": roots103,
            "adjacency": adjacency103,
            "oriented_edge_count": 14,
            "tau_cycles": cycles103,
        },
        "regular_split_fibre_control": {
            "field": "F_43",
            "sigma": 7,
            "a": 35,
            "discriminant_mod_43": discriminant43,
            "roots": roots43,
            "adjacency": adjacency43,
            "oriented_cycle": chosen_cycle,
            "exact_tau_order": 7,
            "cycle_sum": 7,
        },
        "claim_boundary": {
            "generic_henon_recurrence_recovered_from_frozen_P": True,
            "source_literal_formula_refuted": True,
            "published_erratum_claimed": False,
            "selected_prime_good_reduction_claimed": False,
            "riemann_or_hilbert_polya_claimed": False,
        },
    }


def compare_certificate_to_audit(certificate: dict[str, Any], audit: dict[str, Any]) -> None:
    for key in ("symbolic", "exact_fibre_witness", "regular_split_fibre_control", "claim_boundary"):
        require(certificate[key] == audit[key], f"neighbor certificate mismatch in {key}")


def validate_neighbor_independent_report(
    report: Any,
    certificate: dict[str, Any],
    certificate_bytes: bytes,
) -> None:
    top = require_exact_keys(
        report,
        {
            "schema_version",
            "candidate_id",
            "all_checks_passed",
            "implementation",
            "source_certificate",
            "verified_certificate_content",
            "runtime_seconds",
        },
        "$report",
    )
    require(top["schema_version"] == CHECK_SCHEMA and top["candidate_id"] == "HCS-C19", "neighbor report identity mismatch")
    require_type(top["all_checks_passed"], bool, "$report.all_checks_passed")
    require(top["all_checks_passed"], "neighbor independent report does not pass")
    require_type(top["runtime_seconds"], float, "$report.runtime_seconds")
    require(math.isfinite(top["runtime_seconds"]) and top["runtime_seconds"] >= 0.0, "invalid neighbor report runtime")
    require(
        top["implementation"]
        == {
            "producer_imported": False,
            "galois_imported": False,
            "method": "exact SymPy subresultants over Q(sigma), quotient reduction, and direct prime-field enumeration",
        },
        "neighbor report implementation mismatch",
    )
    source = require_exact_keys(top["source_certificate"], {"path", "sha256", "schema_version"}, "$report.source_certificate")
    require_type(source["path"], str, "$report.source_certificate.path")
    require(source["sha256"] == hashlib.sha256(certificate_bytes).hexdigest(), "neighbor report source hash mismatch")
    require(source["schema_version"] == SOURCE_SCHEMA, "neighbor report source schema mismatch")
    validate_neighbor_certificate_schema(certificate)
    require(
        top["verified_certificate_content"]
        == {key: certificate[key] for key in ("symbolic", "exact_fibre_witness", "regular_split_fibre_control", "claim_boundary")},
        "neighbor report verified content mismatch",
    )


def run(certificate_path: Path, output_path: Path) -> dict[str, Any]:
    started = time.perf_counter()
    certificate_bytes = certificate_path.read_bytes()
    certificate = json.loads(certificate_bytes)
    validate_neighbor_certificate_schema(certificate)
    audit = compute_neighbor_audit()
    compare_certificate_to_audit(certificate, audit)
    payload = {
        "schema_version": CHECK_SCHEMA,
        "candidate_id": "HCS-C19",
        "all_checks_passed": True,
        "implementation": {
            "producer_imported": False,
            "galois_imported": False,
            "method": "exact SymPy subresultants over Q(sigma), quotient reduction, and direct prime-field enumeration",
        },
        "source_certificate": {
            "path": str(certificate_path.resolve()),
            "sha256": hashlib.sha256(certificate_bytes).hexdigest(),
            "schema_version": certificate["schema_version"],
        },
        "verified_certificate_content": audit,
        "runtime_seconds": time.perf_counter() - started,
    }
    validate_neighbor_independent_report(payload, certificate, certificate_bytes)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    project = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--certificate",
        type=Path,
        default=project / "results" / "c19_neighbor_correspondence.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=project / "results" / "c19_neighbor_independent_check.json",
    )
    arguments = parser.parse_args()
    payload = run(arguments.certificate, arguments.output)
    print(
        json.dumps(
            {
                "all_checks_passed": True,
                "output": str(arguments.output),
                "runtime_seconds": payload["runtime_seconds"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
