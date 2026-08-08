#!/usr/bin/env python3
"""Exact generic-neighbor certificate for the frozen HCS-C19 septic.

This is a producer-side structural probe.  It works over Q(sigma), reduces a
subresultant sequence modulo P(sigma, x), and constructs a finite-field audit
of the resulting two-neighbor graph.  It does not use Riemann data.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

from c19_producer import orbit_polynomial


SCHEMA = "HCS-C19-neighbor-correspondence-1"


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def canonical_cycle(cycle: list[tuple[int, int]]) -> list[list[int]]:
    rotations = [cycle[index:] + cycle[:index] for index in range(len(cycle))]
    chosen = min(rotations)
    return [[int(x), int(y)] for x, y in chosen]


def build_certificate() -> dict:
    x, sigma, a, p_expr = orbit_polynomial()
    y = sp.symbols("y")
    coefficient_field = sp.QQ.frac_field(sigma)
    p_modulus = sp.Poly(p_expr, x, domain=coefficient_field)

    p_y = sp.expand(p_expr.subs(x, y))
    next_coordinate = sp.expand(a - y**2 - x)
    p_next = sp.expand(p_expr.subs(x, next_coordinate))
    subresultants = sp.subresultants(p_y, p_next, y)

    reduction_rows = []
    last_nonzero = None
    for subresultant in subresultants:
        polynomial_y = sp.Poly(subresultant, y)
        reduced_coefficients = [
            sp.Poly(coefficient, x, domain=coefficient_field).rem(p_modulus)
            for coefficient in polynomial_y.all_coeffs()
        ]
        zero_mod_p = all(coefficient.is_zero for coefficient in reduced_coefficients)
        reduction_rows.append(
            {
                "degree_in_y": int(polynomial_y.degree()),
                "zero_mod_Px": bool(zero_mod_p),
            }
        )
        if not zero_mod_p:
            last_nonzero = (polynomial_y, reduced_coefficients)

    if [row["degree_in_y"] for row in reduction_rows] != [14, 7, 6, 5, 4, 3, 2, 1, 0]:
        raise AssertionError("unexpected subresultant degree sequence")
    if [row["zero_mod_Px"] for row in reduction_rows] != [False] * 7 + [True, True]:
        raise AssertionError("generic gcd does not have degree two")
    if last_nonzero is None or last_nonzero[0].degree() != 2:
        raise AssertionError("missing quadratic last nonzero subresultant")

    quadratic, coefficients = last_nonzero
    c2, c1, c0 = coefficients
    if c2.is_zero:
        raise AssertionError("quadratic leading coefficient vanishes modulo P")
    expected_linear_ratio = sp.Poly(x**2 - a, x, domain=coefficient_field)
    neighbor_sum_remainder = (c1 - c2 * expected_linear_ratio).rem(p_modulus)
    if not neighbor_sum_remainder.is_zero:
        raise AssertionError("neighbor-sum identity failed")
    quadratic_discriminant = (c1 * c1 - 4 * c2 * c0).rem(p_modulus)
    loop_value = (
        c2 * sp.Poly(x**2, x, domain=coefficient_field)
        + c1 * sp.Poly(x, x, domain=coefficient_field)
        + c0
    ).rem(p_modulus)
    if quadratic_discriminant.is_zero:
        raise AssertionError("generic neighbor quadratic is inseparable")
    if loop_value.is_zero:
        raise AssertionError("generic neighbor relation consists of loops")

    # One exact good fibre proves that the generic quadratic is separable and
    # loop-free.  It also makes the graph and the two time orientations fully
    # visible without numerical root finding.
    modulus = 103
    sigma_value = 26
    a_value = 6
    roots = [
        value
        for value in range(modulus)
        if int(p_expr.subs({sigma: sigma_value, x: value})) % modulus == 0
    ]
    if roots != [10, 17, 31, 54, 58, 67, 98]:
        raise AssertionError("unexpected F_103 root set")

    root_set = set(roots)
    adjacency: dict[int, list[int]] = {}
    for fixed_x in roots:
        neighbors = sorted(
            candidate_y
            for candidate_y in roots
            if (a_value - candidate_y**2 - fixed_x) % modulus in root_set
        )
        if len(neighbors) != 2 or fixed_x in neighbors:
            raise AssertionError("F_103 neighbor graph is not simple 2-regular")
        if sum(neighbors) % modulus != (a_value - fixed_x**2) % modulus:
            raise AssertionError("F_103 neighbor sum failed")
        adjacency[fixed_x] = neighbors
    for fixed_x, neighbors in adjacency.items():
        if any(fixed_x not in adjacency[neighbor] for neighbor in neighbors):
            raise AssertionError("F_103 adjacency is not symmetric")

    oriented_edges = {(fixed_x, neighbor) for fixed_x in roots for neighbor in adjacency[fixed_x]}

    def tau(state: tuple[int, int]) -> tuple[int, int]:
        current, previous = state
        following = (a_value - current**2 - previous) % modulus
        return following, current

    unseen = set(oriented_edges)
    cycles: list[list[list[int]]] = []
    while unseen:
        start = min(unseen)
        state = start
        cycle: list[tuple[int, int]] = []
        while state not in cycle:
            if state not in oriented_edges:
                raise AssertionError("tau left the oriented-edge set")
            cycle.append(state)
            unseen.discard(state)
            state = tau(state)
        if state != start or len(cycle) != 7:
            raise AssertionError("tau does not give an exact seven-cycle")
        cycles.append(canonical_cycle(cycle))
    cycles.sort()
    if len(cycles) != 2:
        raise AssertionError("expected two reversed orientations")

    # A second, smaller completely split fibre was found without using the
    # source-correction witness.  It is a sealed control for the generic graph
    # interpretation and the exact order of tau.
    control_modulus = 43
    control_sigma = 7
    control_a = 35
    q6 = (
        64 * sigma**6
        - 448 * sigma**5
        + 848 * sigma**4
        + 80 * sigma**3
        - 1048 * sigma**2
        + 152 * sigma
        - 151
    )
    control_discriminant = int(((4 * sigma - 9) ** 2 * q6**3).subs(sigma, control_sigma)) % control_modulus
    if control_discriminant != 13:
        raise AssertionError("F_43 control fibre is not the expected regular fibre")
    control_roots = [
        value
        for value in range(control_modulus)
        if int(p_expr.subs({sigma: control_sigma, x: value})) % control_modulus == 0
    ]
    if control_roots != [8, 16, 23, 24, 29, 38, 41]:
        raise AssertionError("unexpected F_43 split-fibre root set")
    control_root_set = set(control_roots)
    control_adjacency = {
        fixed_x: sorted(
            candidate_y
            for candidate_y in control_roots
            if (control_a - candidate_y**2 - fixed_x) % control_modulus in control_root_set
        )
        for fixed_x in control_roots
    }
    if not all(
        len(neighbors) == 2
        and fixed_x not in neighbors
        and sum(neighbors) % control_modulus == (control_a - fixed_x**2) % control_modulus
        for fixed_x, neighbors in control_adjacency.items()
    ):
        raise AssertionError("F_43 control graph is not simple 2-regular")
    if not all(
        fixed_x in control_adjacency[neighbor]
        for fixed_x, neighbors in control_adjacency.items()
        for neighbor in neighbors
    ):
        raise AssertionError("F_43 control adjacency is not symmetric")
    control_cycle = [8, 16, 29, 38, 24, 23, 41]
    if any(
        control_cycle[(index + 1) % 7]
        != (control_a - control_cycle[index] ** 2 - control_cycle[index - 1]) % control_modulus
        for index in range(7)
    ):
        raise AssertionError("F_43 oriented cycle fails the Henon recurrence")
    if sum(control_cycle) % control_modulus != control_sigma:
        raise AssertionError("F_43 cycle sum mismatch")

    quadratic_text = str(sp.expand(quadratic.as_expr()))
    coefficient_hashes = [sha256_text(str(sp.cancel(value.as_expr()))) for value in coefficients]
    return {
        "schema_version": SCHEMA,
        "candidate_id": "HCS-C19",
        "object_scope": "generic neighbor correspondence of the frozen septic; no Riemann data",
        "symbolic": {
            "base_field": "Q(sigma)",
            "quotient_field": "Q(sigma)[x]/(P(sigma,x))",
            "P_sha256": sha256_text(str(p_expr)),
            "subresultant_reduction": reduction_rows,
            "generic_gcd_degree_in_y": 2,
            "quadratic_subresultant_sha256": sha256_text(quadratic_text),
            "reduced_coefficient_sha256": coefficient_hashes,
            "neighbor_sum_identity": "y_1 + y_2 = a - x^2",
            "neighbor_sum_remainder_zero": True,
            "quadratic_discriminant_nonzero_mod_Px": True,
            "quadratic_discriminant_sha256": sha256_text(
                str(sp.cancel(quadratic_discriminant.as_expr()))
            ),
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
            "sigma": sigma_value,
            "a": a_value,
            "roots": roots,
            "adjacency": {str(key): value for key, value in adjacency.items()},
            "oriented_edge_count": len(oriented_edges),
            "tau_cycles": cycles,
        },
        "regular_split_fibre_control": {
            "field": "F_43",
            "sigma": control_sigma,
            "a": control_a,
            "discriminant_mod_43": control_discriminant,
            "roots": control_roots,
            "adjacency": {str(key): value for key, value in control_adjacency.items()},
            "oriented_cycle": control_cycle,
            "exact_tau_order": 7,
            "cycle_sum": control_sigma,
        },
        "claim_boundary": {
            "generic_henon_recurrence_recovered_from_frozen_P": True,
            "source_literal_formula_refuted": True,
            "published_erratum_claimed": False,
            "selected_prime_good_reduction_claimed": False,
            "riemann_or_hilbert_polya_claimed": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/c19_neighbor_correspondence.json"),
    )
    args = parser.parse_args()
    payload = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "generic_tau_order": 7, "oriented_degree": 14}))


if __name__ == "__main__":
    main()
