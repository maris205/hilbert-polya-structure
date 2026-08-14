#!/usr/bin/env python3
"""Generate deterministic exact ledgers for frozen candidate SD-C24.

All graph exploration is sparse.  The short atom list below is a post-freeze
evaluation fixture: it never enters the graph constructor or edge predicate.
"""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from fractions import Fraction
from math import cos, exp, lgamma, log, sin, sqrt
from pathlib import Path

from sdc24_cofactor_holonomy import (
    GROUP_MAX_POWER,
    INVENTORY_NAMES,
    ROOTED_MAX_POWER,
    SIMPLE_CYCLE_CUTOFFS,
    SOURCE_AUDIT_CUTOFF,
    TRACE_DIAGNOSTIC_CUTOFFS,
    TRACE_INTEGER_S_VALUES,
    TRACE_PARAMETER_POINTS,
    atomic_family_cycle,
    atomic_family_mass,
    canonical_primitive_root,
    canonical_rotation,
    cofactor_word,
    complex_character_matrix,
    complex_determinant,
    complex_identity_minus_scaled,
    complex_source_gauge_matrix,
    cycle_holonomy,
    cycle_mass,
    diagonal_gauge_conjugate,
    edge_identity_audit,
    edge_quotient,
    edges_from,
    enumerate_rooted_closed_walks,
    enumerate_simple_cycles,
    expected_atomic_trace,
    factor_exponents,
    finite_trace_powers,
    fixed_row_squared_prefix,
    fraction_determinant,
    fraction_fields,
    fraction_matrix,
    identity_minus_scaled,
    inventory_cycle_product,
    is_rotation_of,
    max_entry_difference,
    minimal_temporal_period,
    newton_determinant_coefficients,
    polynomial_value,
    row_nuclear_prefix,
    rotations,
    sparse_group_trace,
    successor_trace_prefix,
    telescoping_holonomy,
    trace_class_failure_mode,
    trace_class_membership,
    transported_cycle,
    word_text,
    character_fourier_reconstruction,
)


POST_FREEZE_TEST_ATOMS = (2, 3, 5, 7)
PURE_COFACTOR_A_VALUES = (0.0, 0.75, 1.25, 2.0)
UNITARY_T_VALUES = (0.0, 0.5, 1.0, sqrt(2.0))
GAUGE_INTEGER_U_VALUES = (-2, -1, 0, 1, 2)
GAUGE_CUTOFFS = (12, 20, 30)
FINITE_DETERMINANT_CASES = ((12, 1, 0), (12, 1, 1), (20, 1, 0), (20, 1, 1))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"refusing to write empty ledger: {path.name}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        fieldnames = list(rows[0])
        for row in rows[1:]:
            fieldnames.extend(key for key in row if key not in fieldnames)
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def integer_power_fraction(base: int, exponent: int) -> Fraction:
    return Fraction(base**exponent) if exponent >= 0 else Fraction(1, base ** (-exponent))


def source_certificate(results: Path) -> dict[str, object]:
    audit = edge_identity_audit(SOURCE_AUDIT_CUTOFF)
    write_json(results / "source_oracle_certificate.json", audit)
    return audit


def simple_cycle_ledgers(results: Path) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    simple_rows: list[dict[str, object]] = []
    atomic_rows: list[dict[str, object]] = []
    for cutoff in SIMPLE_CYCLE_CUTOFFS:
        cycles = enumerate_simple_cycles(cutoff)
        by_word = set(cycles)
        for cycle in cycles:
            holonomy = cycle_holonomy(cycle)
            telescoped = telescoping_holonomy(cycle)
            simple_rows.append(
                {
                    "cutoff": cutoff,
                    "cycle": word_text(cycle),
                    "length": len(cycle),
                    "cofactor_word": word_text(cofactor_word(cycle)),
                    "holonomy": holonomy,
                    "telescoped": str(telescoped),
                    "integer_ge_two": holonomy >= 2,
                    "q2_canonical": holonomy != 2
                    or is_rotation_of(cycle, atomic_family_cycle(len(cycle), 2)),
                }
            )
        for atom in POST_FREEZE_TEST_ATOMS:
            found = [cycle for cycle in cycles if cycle_holonomy(cycle) == atom]
            predicted = [
                atomic_family_cycle(k, atom)
                for k in range(2, cutoff + 1)
                if atom * k - 1 <= cutoff
            ]
            for cycle in found:
                k = len(cycle) // (atom - 1) if len(cycle) % (atom - 1) == 0 else 0
                expected = atomic_family_cycle(k, atom) if k >= 2 else ()
                atomic_rows.append(
                    {
                        "cutoff": cutoff,
                        "atom": atom,
                        "kind": "enumerated",
                        "k": k,
                        "cycle": word_text(cycle),
                        "classification_match": bool(expected) and is_rotation_of(cycle, expected),
                        "predicted_in_cutoff": bool(expected) and max(expected) <= cutoff,
                    }
                )
            for expected in predicted:
                atomic_rows.append(
                    {
                        "cutoff": cutoff,
                        "atom": atom,
                        "kind": "predicted",
                        "k": expected[0],
                        "cycle": word_text(expected),
                        "classification_match": canonical_rotation(expected) in by_word,
                        "predicted_in_cutoff": True,
                    }
                )
    write_csv(results / "simple_cycle_holonomy.csv", simple_rows)
    write_csv(results / "atomic_holonomy_witnesses.csv", atomic_rows)
    return simple_rows, atomic_rows


def rooted_cycle_ledger(results: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for length in range(1, ROOTED_MAX_POWER + 1):
        walks = enumerate_rooted_closed_walks(length)
        for word in walks:
            period = minimal_temporal_period(word)
            root = canonical_primitive_root(word)
            rooted_block = tuple(word[:period])
            rotation_index = rotations(root).index(rooted_block)
            rows.append(
                {
                    "power": length,
                    "rooted_word": word_text(word),
                    "primitive_root": word_text(root),
                    "primitive_period": period,
                    "repetition": length // period,
                    "rotation_index": rotation_index,
                    "holonomy": cycle_holonomy(word),
                    "mass": cycle_mass(word),
                    "cofactor_word": word_text(cofactor_word(word)),
                    "rotation_repetition_match": word == rooted_block * (length // period),
                }
            )
    write_csv(results / "rooted_cycle_ledger.csv", rows)
    return rows


def trace_ledgers(results: Path) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    group_rows: list[dict[str, object]] = []
    atomic_rows: list[dict[str, object]] = []
    neutral_rows: list[dict[str, object]] = []
    group_cache: dict[tuple[int, int], dict[int, Fraction]] = {}
    for s_integer in TRACE_INTEGER_S_VALUES:
        traces: list[Fraction] = []
        for power in range(1, GROUP_MAX_POWER + 1):
            coefficients = sparse_group_trace(power, s_integer)
            group_cache[(power, s_integer)] = coefficients
            neutral = coefficients.get(1, Fraction(0))
            traces.append(neutral)
            neutral_rows.append(
                {
                    "s_integer": s_integer,
                    "degree": power,
                    "neutral_trace": str(neutral),
                    "expected_trace": "0",
                    "match": neutral == 0,
                }
            )
            if not coefficients:
                group_rows.append(
                    {
                        "power": power,
                        "s_integer": s_integer,
                        "holonomy": 0,
                        "coefficient": "0",
                        "numerator": 0,
                        "denominator": 1,
                        "neutral": False,
                    }
                )
            for holonomy, coefficient in coefficients.items():
                group_rows.append(
                    {
                        "power": power,
                        "s_integer": s_integer,
                        "holonomy": holonomy,
                        "coefficient": str(coefficient),
                        "numerator": coefficient.numerator,
                        "denominator": coefficient.denominator,
                        "neutral": holonomy == 1,
                    }
                )
            for atom in POST_FREEZE_TEST_ATOMS:
                observed = coefficients.get(atom, Fraction(0))
                expected = expected_atomic_trace(power, s_integer, atom)
                atomic_rows.append(
                    {
                        "power": power,
                        "s_integer": s_integer,
                        "atom": atom,
                        "observed": str(observed),
                        "expected": str(expected),
                        "match": observed == expected,
                        "repetition_contamination": observed != 0
                        and expected == 0,
                    }
                )
        determinant_coefficients = newton_determinant_coefficients(traces)
        for degree, coefficient in enumerate(determinant_coefficients):
            neutral_rows.append(
                {
                    "s_integer": s_integer,
                    "degree": degree,
                    "neutral_trace": "not_applicable",
                    "expected_trace": "not_applicable",
                    "match": coefficient == (1 if degree == 0 else 0),
                    "determinant_coefficient": str(coefficient),
                }
            )
    write_csv(results / "group_trace_coefficients.csv", group_rows)
    write_csv(results / "atomic_trace_coefficients.csv", atomic_rows)
    write_csv(results / "neutral_determinant.csv", neutral_rows)

    fourier_rows: list[dict[str, object]] = []
    for power in range(2, 7):
        coefficients = group_cache[(power, 1)]
        reconstructed, grid_size = character_fourier_reconstruction(coefficients)
        for row in reconstructed:
            fourier_rows.append({"power": power, "s_integer": 1, "grid_size_check": grid_size, **row})
    write_csv(results / "fourier_reconstruction.csv", fourier_rows)
    return group_rows, atomic_rows, neutral_rows


def gauge_ledgers(results: Path) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    exact_rows: list[dict[str, object]] = []
    for cutoff in GAUGE_CUTOFFS:
        for u_integer in GAUGE_INTEGER_U_VALUES:
            mismatch = 0
            checked = 0
            for source in range(2, cutoff + 1):
                for target, _quotient in edges_from(source, cutoff=cutoff):
                    quotient = edge_quotient(source, target)
                    endpoint = Fraction(1, source * target)
                    twisted = endpoint * integer_power_fraction(quotient, -u_integer)
                    conjugated = (
                        integer_power_fraction(target, -u_integer)
                        * twisted
                        * integer_power_fraction(source, u_integer)
                    )
                    source_weight = endpoint * Fraction(source, source + 1) ** u_integer
                    mismatch += int(conjugated != source_weight)
                    checked += 1
            exact_rows.append(
                {
                    "cutoff": cutoff,
                    "s_integer": 1,
                    "u_integer": u_integer,
                    "edges_checked": checked,
                    "mismatches": mismatch,
                    "exact_match": mismatch == 0,
                    "infinite_nonunitary_similarity_claimed": False,
                }
            )
    write_csv(results / "gauge_identity.csv", exact_rows)

    unitary_rows: list[dict[str, object]] = []
    for cutoff in GAUGE_CUTOFFS:
        for t in UNITARY_T_VALUES:
            twisted = complex_character_matrix(cutoff, 1, t)
            conjugated = diagonal_gauge_conjugate(twisted, t)
            source = complex_source_gauge_matrix(cutoff, 1, t)
            entry_error = max_entry_difference(conjugated, source)
            z = 0.1
            det_twisted = complex_determinant(complex_identity_minus_scaled(twisted, z))
            det_source = complex_determinant(complex_identity_minus_scaled(source, z))
            determinant_error = abs(det_twisted - det_source)
            unitary_rows.append(
                {
                    "cutoff": cutoff,
                    "s_integer": 1,
                    "t": format(t, ".17g"),
                    "z": z,
                    "entry_error": format(entry_error, ".17g"),
                    "determinant_error": format(determinant_error, ".17g"),
                    "unitary_similarity_match": entry_error < 1e-12 and determinant_error < 1e-11,
                }
            )
    write_csv(results / "unitary_gauge.csv", unitary_rows)
    return exact_rows, unitary_rows


def trace_class_ledgers(results: Path) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    rows: list[dict[str, object]] = []
    for point_index, (sigma, a, declared) in enumerate(TRACE_PARAMETER_POINTS):
        theorem = trace_class_failure_mode(sigma, a)
        for cutoff in TRACE_DIAGNOSTIC_CUTOFFS:
            row_sum = row_nuclear_prefix(cutoff, sigma, a)
            fixed_row = fixed_row_squared_prefix(3, cutoff, sigma, a)
            successor = successor_trace_prefix(cutoff, sigma)
            rows.append(
                {
                    "point": point_index,
                    "sigma": sigma,
                    "a": a,
                    "cutoff": cutoff,
                    "row_nuclear_prefix": format(row_sum, ".17g"),
                    "fixed_row_3_squared_prefix": format(fixed_row, ".17g"),
                    "successor_trace_prefix": format(successor, ".17g"),
                    "declared_class": declared,
                    "theorem_class": theorem,
                    "classification_match": declared.startswith(theorem)
                    or (
                        declared == "bounded_control_noncompact"
                        and theorem == "not_trace_class_successor"
                    ),
                    "trace_class_iff": trace_class_membership(sigma, a),
                    "finite_prefix_is_proof": False,
                }
            )
    write_csv(results / "trace_class_diagnostics.csv", rows)

    spine_rows: list[dict[str, object]] = []
    for a in PURE_COFACTOR_A_VALUES:
        if a <= 0.5:
            theorem = "unbounded_fixed_row"
        elif a <= 1:
            theorem = "boundedness_unclaimed_if_bounded_noncompact"
        else:
            theorem = "bounded_noncompact"
        for cutoff in TRACE_DIAGNOSTIC_CUTOFFS:
            fixed_row = fixed_row_squared_prefix(3, cutoff, 0.0, a)
            spine_rows.append(
                {
                    "a": a,
                    "cutoff": cutoff,
                    "successor_spine_edges": cutoff - 1,
                    "successor_weight": 1,
                    "fixed_row_3_squared_prefix": format(fixed_row, ".17g"),
                    "theorem_status": theorem,
                    "bounded_extension_proved": a > 1,
                    "compact_if_bounded": False,
                    "trace_class": False,
                }
            )
    write_csv(results / "pure_cofactor_spine.csv", spine_rows)
    return rows, spine_rows


def determinant_ledgers(results: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for cutoff, s_integer, u_integer in FINITE_DETERMINANT_CASES:
        matrix = fraction_matrix(cutoff, s_integer, u_integer)
        traces = finite_trace_powers(matrix, len(matrix))
        coefficients = newton_determinant_coefficients(traces)
        z = Fraction(1, 10)
        trace_value = polynomial_value(coefficients, z)
        direct = fraction_determinant(identity_minus_scaled(matrix, z))
        rows.append(
            {
                "cutoff": cutoff,
                "dimension": len(matrix),
                "s_integer": s_integer,
                "u_integer": u_integer,
                "z": str(z),
                "trace_expansion": str(trace_value),
                "direct_determinant": str(direct),
                "match": trace_value == direct,
                "coefficient_count": len(coefficients),
            }
        )
    write_csv(results / "finite_determinant_checks.csv", rows)
    return rows


def spine_and_control_ledgers(results: Path) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    pure_rows: list[dict[str, object]] = []
    for z in (Fraction(1, 2), Fraction(3, 4), Fraction(1, 1)):
        for max_k in (8, 16, 32):
            partial = sum(z**k for k in range(2, max_k + 1))
            expected = z * z / (1 - z) if z < 1 else None
            pure_rows.append(
                {
                    "z": str(z),
                    "u_integer": 1,
                    "max_k": max_k,
                    "partial": str(Fraction(1, 2) * partial),
                    "infinite_closed_form": str(Fraction(1, 2) * expected) if expected is not None else "diverges",
                    "convergent": z < 1,
                    "at_z1_nondecaying_term": z == 1,
                }
            )
    write_csv(results / "pure_cofactor_series.csv", pure_rows)

    return_rows: list[dict[str, object]] = []
    for k in range(2, 33):
        mass = atomic_family_mass(k, 2)
        for s_integer in (0, 1):
            for z in (Fraction(1, 1), Fraction(1, 2)):
                coefficient = Fraction(1, 2) * z**k / (mass ** (2 * s_integer))
                return_rows.append(
                    {
                        "k": k,
                        "s_integer": s_integer,
                        "u_integer": 1,
                        "z": str(z),
                        "mass": mass,
                        "coefficient": str(coefficient),
                        "pure_at_z1_constant": s_integer == 0 and z == 1 and coefficient == Fraction(1, 2),
                        "factorial_damping": s_integer > 0,
                    }
                )
    write_csv(results / "induced_return_exact.csv", return_rows)

    damping_rows: list[dict[str, object]] = []
    previous = None
    for k in range(2, 65):
        log_mass = lgamma(2 * k) - lgamma(k)
        log_weight = -1.2 * log_mass
        weight = exp(log_weight) if log_weight > -745 else 0.0
        damping_rows.append(
            {
                "k": k,
                "sigma": 0.6,
                "log_mass": format(log_mass, ".17g"),
                "log_weight": format(log_weight, ".17g"),
                "weight": format(weight, ".17g"),
                "strictly_decreasing": previous is None or log_weight < previous,
            }
        )
        previous = log_weight
    write_csv(results / "factorial_damping.csv", damping_rows)

    phase_rows: list[dict[str, object]] = []
    for t in UNITARY_T_VALUES:
        phase = complex(cos(-t * log(2)), sin(-t * log(2)))
        for k in range(2, 33):
            phase_rows.append(
                {
                    "t": format(t, ".17g"),
                    "k": k,
                    "holonomy": 2,
                    "phase_real": format(phase.real, ".17g"),
                    "phase_imag": format(phase.imag, ".17g"),
                    "absolute_value": format(abs(phase), ".17g"),
                    "selected_out": False,
                    "same_phase_for_all_k": True,
                }
            )
    write_csv(results / "unitary_phase_spine.csv", phase_rows)

    inventory_rows: list[dict[str, object]] = []
    for name in INVENTORY_NAMES:
        for k in range(2, 33):
            cycle = atomic_family_cycle(k, 2)
            product_value = inventory_cycle_product(name, cycle)
            inventory_rows.append(
                {
                    "inventory": name,
                    "k": k,
                    "cycle": word_text(cycle),
                    "holonomy": cycle_holonomy(cycle),
                    "support_present": True,
                    "positive_weight": product_value > 0,
                    "inventory_product": str(product_value),
                    "composite_length_witness": k >= 4 and any(k % divisor == 0 for divisor in range(2, k)),
                }
            )
    write_csv(results / "inventory_controls.csv", inventory_rows)

    presentation_rows: list[dict[str, object]] = []
    for k in range(2, 33):
        cycle = atomic_family_cycle(k, 2)
        transported = transported_cycle(cycle)
        transported_q = cofactor_word(cycle)
        presentation_rows.append(
            {
                "k": k,
                "source_cycle": word_text(cycle),
                "transported_cycle": word_text(transported),
                "transported_cofactor_word": word_text(transported_q),
                "source_holonomy": cycle_holonomy(cycle),
                "transported_holonomy": 2,
                "transported_successor_and_tensor_together": True,
                "match": cycle_holonomy(cycle) == 2,
            }
        )
    write_csv(results / "presentation_transport.csv", presentation_rows)
    return pure_rows, return_rows, damping_rows, inventory_rows


def main() -> None:
    project = Path(__file__).resolve().parents[1]
    results = project / "results"
    results.mkdir(parents=True, exist_ok=True)

    audit = source_certificate(results)
    simple_rows, atomic_witnesses = simple_cycle_ledgers(results)
    rooted_rows = rooted_cycle_ledger(results)
    group_rows, atomic_trace_rows, neutral_rows = trace_ledgers(results)
    gauge_rows, unitary_rows = gauge_ledgers(results)
    trace_rows, pure_spine_rows = trace_class_ledgers(results)
    determinant_rows = determinant_ledgers(results)
    pure_rows, return_rows, damping_rows, inventory_rows = spine_and_control_ledgers(results)

    simple_counts = {
        str(cutoff): sum(int(row["cutoff"]) == cutoff for row in simple_rows)
        for cutoff in SIMPLE_CYCLE_CUTOFFS
    }
    q2_counts = {
        str(cutoff): sum(
            int(row["cutoff"]) == cutoff and int(row["holonomy"]) == 2
            for row in simple_rows
        )
        for cutoff in SIMPLE_CYCLE_CUTOFFS
    }
    rooted_counts = {
        str(power): sum(int(row["power"]) == power for row in rooted_rows)
        for power in range(1, ROOTED_MAX_POWER + 1)
    }
    summary = {
        "candidate_id": "SD-C24",
        "source_cutoff": SOURCE_AUDIT_CUTOFF,
        "source_edges_audited": audit["edge_count"],
        "simple_cycle_counts": simple_counts,
        "q2_cycle_counts": q2_counts,
        "rooted_cycle_counts": rooted_counts,
        "rooted_cycle_rows": len(rooted_rows),
        "atomic_witness_rows": len(atomic_witnesses),
        "group_trace_rows": len(group_rows),
        "atomic_trace_rows": len(atomic_trace_rows),
        "neutral_ledger_rows": len(neutral_rows),
        "gauge_cases": len(gauge_rows),
        "unitary_gauge_cases": len(unitary_rows),
        "trace_class_diagnostic_rows": len(trace_rows),
        "pure_cofactor_spine_rows": len(pure_spine_rows),
        "finite_determinant_cases": len(determinant_rows),
        "pure_cofactor_series_rows": len(pure_rows),
        "induced_return_rows": len(return_rows),
        "factorial_damping_rows": len(damping_rows),
        "inventory_control_rows": len(inventory_rows),
        "target_zero_evaluation": "not_applicable; no_target_zero_evaluation",
        "target_root_metrics": "not_applicable; no_target_zero_evaluation",
        "graph_search": "sparse_dfs_and_sparse_dynamic_programming",
        "cartesian_cycle_enumeration": False,
    }
    write_json(results / "summary.json", summary)
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
