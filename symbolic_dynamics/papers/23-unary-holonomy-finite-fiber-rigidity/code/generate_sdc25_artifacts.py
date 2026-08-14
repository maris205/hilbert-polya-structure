#!/usr/bin/env python3
"""Generate deterministic exact and diagnostic artifacts for SD-C25."""

from __future__ import annotations

import argparse
import ast
import csv
from fractions import Fraction
from hashlib import sha256
from importlib.metadata import PackageNotFoundError, version
import json
from pathlib import Path
import platform
from typing import Sequence

from sdc25_evaluator import (
    TARGET_NAMES,
    algebraic_control_rows,
    block_fiber_fixtures,
    constructive_composite_witnesses,
    deterministic_matrix_fixtures,
    exhaustive_boolean_relation_rows,
    exhaustive_transformation_rows,
    imported_wrapper_certificates,
    recurrent_wrapper_rows,
    roof_marker_rows,
    target_digest,
    target_vector,
    transient_wrapper_rows,
)
from sdc25_unary_fiber import (
    BLOCK_CUTOFF,
    BLOCK_MAX_POWER,
    CANDIDATE_ID,
    MEMORY_CUTOFFS,
    RECURRENCE_DIMENSIONS,
    SOURCE_AUDIT_CUTOFF,
    STATE_SIZES,
    TRACE_CUTOFFS,
    TRACE_SIGMAS,
    block_adjacency,
    canonical_fiber_trace,
    canonical_mass,
    canonical_word_certificate,
    cayley_hamilton_matrix,
    characteristic_coefficients,
    decimal_edge_prefix_interval,
    finite_power_traces,
    fraction_determinant,
    fraction_text,
    generating_numerator,
    generating_series_from_rational,
    identity_minus_scaled,
    matrix_is_zero,
    matrix_multiply,
    matrix_power,
    matrix_trace,
    matrix_text,
    memorizer_response,
    minimal_recurrence_order,
    newton_determinant_coefficients,
    polynomial_value,
    recurrence_residuals,
    response_sequences,
    vector_text,
)


ROOT = Path(__file__).resolve().parents[1]
SYMBOLIC_ROOT = ROOT.parents[1]
CORE = ROOT / "code" / "sdc25_unary_fiber.py"


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"refusing empty CSV {path.name}")
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0])
    if any(list(row) != fieldnames for row in rows):
        raise ValueError(f"nonuniform fields in {path.name}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _call_name(node: ast.Call) -> str:
    if isinstance(node.func, ast.Name):
        return node.func.id.lower()
    if isinstance(node.func, ast.Attribute):
        return node.func.attr.lower()
    return ""


def source_oracle_certificate(output: Path) -> tuple[dict[str, object], list[dict[str, object]]]:
    source = CORE.read_text(encoding="utf-8")
    tree = ast.parse(source)
    imports = sorted(
        {
            alias.name.split(".", 1)[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.Import)
            for alias in node.names
        }
        | {
            (node.module or "").split(".", 1)[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom)
        }
    )
    calls = sorted({_call_name(node) for node in ast.walk(tree) if isinstance(node, ast.Call)})
    forbidden_modules = sorted(set(imports) & {"sympy", "mpmath", "primesieve", "sage"})
    forbidden_calls = sorted(
        set(calls)
        & {
            "factorint",
            "isprime",
            "mangoldt",
            "nextprime",
            "primepi",
            "primerange",
            "sieve_primes",
            "zeta",
            "zetazero",
        }
    )
    constructor_names = {
        "edge_quotient",
        "canonical_cycle",
        "ordered_quotient_word",
        "canonical_word_certificate",
        "q12_edges",
        "block_adjacency",
    }
    constructor_segments = "\n".join(
        ast.get_source_segment(source, node) or ""
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in constructor_names
    )
    constructor_tree = ast.parse(constructor_segments)
    constructor_calls = sorted(
        {_call_name(node) for node in ast.walk(constructor_tree) if isinstance(node, ast.Call)}
    )
    forbidden_constructor_calls = sorted(
        set(constructor_calls)
        & {"factorint", "isprime", "mangoldt", "primepi", "primerange", "zeta", "zetazero"}
    )

    rows = [canonical_word_certificate(index) for index in range(2, SOURCE_AUDIT_CUTOFF + 1)]
    write_csv(output / "canonical_word_certificates.csv", rows)
    certificate = {
        "candidate_id": CANDIDATE_ID,
        "candidate_source": "code/sdc25_unary_fiber.py",
        "candidate_source_sha256": sha256(CORE.read_bytes()).hexdigest(),
        "evaluator_source": "code/sdc25_evaluator.py",
        "candidate_evaluator_separated": True,
        "cutoff": SOURCE_AUDIT_CUTOFF,
        "cycles_checked": len(rows),
        "edges_checked": sum(int(row["length"]) for row in rows),
        "word_mismatches": sum(not bool(row["ordered_word_match"]) for row in rows),
        "edge_mismatches": sum(not bool(row["all_edges_valid"]) for row in rows),
        "holonomy_mismatches": sum(int(row["holonomy"]) != 2 for row in rows),
        "mark_mismatches": sum(not bool(row["unique_minimum_mark"]) for row in rows),
        "primitive_mismatches": sum(not bool(row["primitive"]) for row in rows),
        "imported_modules": imports,
        "forbidden_modules": forbidden_modules,
        "forbidden_calls": forbidden_calls,
        "constructor_calls": constructor_calls,
        "forbidden_constructor_calls": forbidden_constructor_calls,
        "prime_table_used": False,
        "factorization_oracle_used": False,
        "target_feedback_used": False,
        "riemann_zero_data_used": False,
        "source_policy_pass": not forbidden_modules
        and not forbidden_calls
        and not forbidden_constructor_calls
        and all(
            bool(row["ordered_word_match"])
            and bool(row["all_edges_valid"])
            and int(row["holonomy"]) == 2
            and bool(row["unique_minimum_mark"])
            and bool(row["primitive"])
            for row in rows
        ),
    }
    write_json(output / "source_oracle_certificate.json", certificate)
    return certificate, rows


def finite_state_artifacts(output: Path) -> dict[str, object]:
    transformation_rows, transformation_totals = exhaustive_transformation_rows()
    relation_rows, relation_totals = exhaustive_boolean_relation_rows(2)
    semigroup_rows = algebraic_control_rows()
    witness_rows = constructive_composite_witnesses()
    write_csv(output / "finite_state_periodicity.csv", transformation_rows)
    write_csv(output / "boolean_relation_periodicity.csv", relation_rows)
    write_csv(output / "finite_semigroup_controls.csv", semigroup_rows)
    write_csv(output / "composite_witnesses.csv", witness_rows)
    return {
        "transformation_rows": len(transformation_rows),
        "transformation_totals": transformation_totals,
        "relation_rows": len(relation_rows),
        "relation_totals": relation_totals,
        "semigroup_control_rows": len(semigroup_rows),
        "composite_witness_rows": len(witness_rows),
        "composite_witness_failures": sum(
            not (
                bool(row["same_residue"])
                and bool(row["same_response"])
                and bool(row["composite_verified"])
            )
            for row in witness_rows
        ),
    }


def recurrence_artifacts(output: Path) -> tuple[list[dict[str, object]], dict[str, int]]:
    rows: list[dict[str, object]] = []
    residual_count = 0
    nonzero_residuals = 0
    generating_mismatches = 0
    ch_failures = 0
    for fixture in deterministic_matrix_fixtures():
        dimension = int(fixture["dimension"])
        a_matrix = fixture["A"]
        b_matrix = fixture["B"]
        left = fixture["u"]
        right = fixture["v"]
        count = 4 * dimension + 16
        coefficients = characteristic_coefficients(a_matrix)
        bilinear, traces = response_sequences(a_matrix, b_matrix, left, right, count)
        bilinear_residuals = recurrence_residuals(bilinear, coefficients)
        trace_residuals = recurrence_residuals(traces, coefficients)
        bilinear_numerator = generating_numerator(bilinear, coefficients)
        trace_numerator = generating_numerator(traces, coefficients)
        bilinear_rebuilt = generating_series_from_rational(bilinear_numerator, coefficients, count)
        trace_rebuilt = generating_series_from_rational(trace_numerator, coefficients, count)
        ch_zero = matrix_is_zero(cayley_hamilton_matrix(a_matrix))
        residual_count += len(bilinear_residuals) + len(trace_residuals)
        nonzero_residuals += sum(value != 0 for value in bilinear_residuals + trace_residuals)
        generating_mismatches += int(bilinear_rebuilt != bilinear) + int(trace_rebuilt != traces)
        ch_failures += int(not ch_zero)
        rows.append(
            {
                "dimension": dimension,
                "case": fixture["case"],
                "terms_checked": count,
                "characteristic_coefficients": vector_text(coefficients),
                "cayley_hamilton_zero": ch_zero,
                "bilinear_residual_count": len(bilinear_residuals),
                "bilinear_nonzero_residuals": sum(value != 0 for value in bilinear_residuals),
                "trace_residual_count": len(trace_residuals),
                "trace_nonzero_residuals": sum(value != 0 for value in trace_residuals),
                "bilinear_numerator": vector_text(bilinear_numerator),
                "trace_numerator": vector_text(trace_numerator),
                "denominator": vector_text((Fraction(1), *coefficients)),
                "bilinear_series_match": bilinear_rebuilt == bilinear,
                "trace_series_match": trace_rebuilt == traces,
                "bilinear_minimal_order": minimal_recurrence_order(bilinear, dimension),
                "trace_minimal_order": minimal_recurrence_order(traces, dimension),
                "A": matrix_text(a_matrix),
                "B": matrix_text(b_matrix),
            }
        )
    write_csv(output / "recurrence_certificates.csv", rows)
    return rows, {
        "cases": len(rows),
        "residuals_checked": residual_count,
        "nonzero_residuals": nonzero_residuals,
        "generating_function_mismatches": generating_mismatches,
        "cayley_hamilton_failures": ch_failures,
    }


def memorizer_artifacts(output: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for cutoff in MEMORY_CUTOFFS:
        for target_name in TARGET_NAMES:
            target = target_vector(target_name, cutoff)
            digest = target_digest(target)
            for realization in ("bilinear_nilpotent", "trace_nilpotent"):
                mismatches = sum(
                    memorizer_response(target, index) != target[index - 1]
                    for index in range(1, cutoff + 1)
                )
                post_cutoff_nonzero = sum(
                    memorizer_response(target, index) != 0
                    for index in range(cutoff + 1, cutoff + 5)
                )
                rows.append(
                    {
                        "cutoff": cutoff,
                        "target": target_name,
                        "realization": realization,
                        "fiber_dimension": cutoff,
                        "stored_target_parameters": cutoff,
                        "shift_nonzeros": cutoff - 1,
                        "target_sha256": digest,
                        "prefix_mismatches": mismatches,
                        "post_cutoff_nonzero": post_cutoff_nonzero,
                        "exact_prefix_fit": mismatches == 0 and post_cutoff_nonzero == 0,
                        "label": "oracle-containing memorizer control",
                        "proves_too_much": True,
                    }
                )
    write_csv(output / "nilpotent_memorizer_controls.csv", rows)
    return rows


def block_operator_artifacts(output: Path) -> dict[str, object]:
    canonical_rows: list[dict[str, object]] = []
    trace_rows: list[dict[str, object]] = []
    determinant_rows: list[dict[str, object]] = []
    for fixture in block_fiber_fixtures():
        a_matrix = fixture["A"]
        b_matrix = fixture["B"]
        adjacency = block_adjacency(BLOCK_CUTOFF, a_matrix, b_matrix, 1)
        traces = finite_power_traces(adjacency, BLOCK_MAX_POWER)
        for power, trace in enumerate(traces, start=1):
            trace_rows.append(
                {
                    "fiber": fixture["name"],
                    "cutoff": BLOCK_CUTOFF,
                    "fiber_dimension": len(a_matrix),
                    "power": power,
                    "exact_power_trace": fraction_text(trace),
                    "closed_walk_dynamic_program": True,
                    "maximum_period": BLOCK_MAX_POWER,
                }
            )
        for index in range(2, (BLOCK_CUTOFF + 1) // 2 + 1):
            word_trace, column_trace = canonical_fiber_trace(index, a_matrix, b_matrix)
            column_product = matrix_multiply(b_matrix, matrix_power(a_matrix, index - 1))
            local_power_traces = finite_power_traces(column_product, len(column_product))
            local_factor = newton_determinant_coefficients(local_power_traces)
            second_repetition_trace = matrix_trace(matrix_power(column_product, 2))
            mass = canonical_mass(index)
            scalar = Fraction(1, mass * mass)
            canonical_rows.append(
                {
                    "fiber": fixture["name"],
                    "index": index,
                    "cycle_length": index,
                    "word_trace": fraction_text(word_trace),
                    "column_source_trace": fraction_text(column_trace),
                    "cyclic_trace_match": word_trace == column_trace,
                    "mass": mass,
                    "scalar_cycle_weight": fraction_text(scalar),
                    "primitive_trace_factor": fraction_text(scalar * word_trace),
                    "rooted_power_trace_factor": fraction_text(index * scalar * word_trace),
                    "local_factor_convention": f"det(I-w_{index}*B*A^{index - 1})",
                    "local_factor_coefficients_in_w": vector_text(local_factor),
                    "linear_trace_coefficient": fraction_text(-column_trace),
                    "second_repetition_trace": fraction_text(second_repetition_trace),
                    "first_trace_zero": column_trace == 0,
                    "local_factor_nontrivial": any(value != 0 for value in local_factor[1:]),
                    "trace_zero_repetition_leakage": column_trace == 0 and second_repetition_trace != 0,
                    "scalar_trace_is_full_local_factor": len(local_factor) == 2,
                    "expected_word": f"1^{index - 1}2",
                }
            )
        dimension = len(adjacency)
        determinant_coefficients = newton_determinant_coefficients(traces[:dimension])
        for value in (Fraction(1, 7), Fraction(1, 11), Fraction(2, 13)):
            from_traces = polynomial_value(determinant_coefficients, value)
            direct = fraction_determinant(identity_minus_scaled(adjacency, value))
            determinant_rows.append(
                {
                    "fiber": fixture["name"],
                    "cutoff": BLOCK_CUTOFF,
                    "matrix_dimension": dimension,
                    "z": fraction_text(value),
                    "newton_determinant": fraction_text(from_traces),
                    "direct_determinant": fraction_text(direct),
                    "match": from_traces == direct,
                }
            )
    write_csv(output / "canonical_block_traces.csv", canonical_rows)
    write_csv(output / "finite_block_power_traces.csv", trace_rows)
    write_csv(output / "finite_block_determinants.csv", determinant_rows)
    return {
        "canonical_rows": len(canonical_rows),
        "power_trace_rows": len(trace_rows),
        "determinant_rows": len(determinant_rows),
        "cyclic_trace_mismatches": sum(not bool(row["cyclic_trace_match"]) for row in canonical_rows),
        "determinant_mismatches": sum(not bool(row["match"]) for row in determinant_rows),
        "trace_zero_leakage_rows": sum(bool(row["trace_zero_repetition_leakage"]) for row in canonical_rows),
    }


def trace_class_artifacts(output: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for sigma in TRACE_SIGMAS:
        theorem_class = "trace_class" if Fraction(sigma) > Fraction(1, 2) else "not_trace_class"
        for cutoff in TRACE_CUTOFFS:
            successor_lower, successor_upper = decimal_edge_prefix_interval(cutoff, sigma, "successor")
            return_lower, return_upper = decimal_edge_prefix_interval(cutoff, sigma, "return")
            for control, a_norm, b_norm in (
                ("A_only", 1, 0),
                ("B_only", 0, 1),
                ("A_and_B", 1, 1),
            ):
                lower = a_norm * successor_lower + b_norm * return_lower
                upper = a_norm * successor_upper + b_norm * return_upper
                rows.append(
                    {
                        "sigma": sigma,
                        "cutoff": cutoff,
                        "control": control,
                        "A_trace_norm": a_norm,
                        "B_trace_norm": b_norm,
                        "successor_lower": format(successor_lower, "f"),
                        "successor_upper": format(successor_upper, "f"),
                        "return_lower": format(return_lower, "f"),
                        "return_upper": format(return_upper, "f"),
                        "normalized_total_lower": format(lower, "f"),
                        "normalized_total_upper": format(upper, "f"),
                        "interval_ordered": lower <= upper,
                        "theorem_class": theorem_class,
                        "finite_prefix_is_proof": False,
                    }
                )
    write_csv(output / "trace_class_diagnostics.csv", rows)
    return rows


def wrapper_artifacts(output: Path) -> dict[str, object]:
    structure_rows, trace_rows = transient_wrapper_rows()
    recurrent_rows = recurrent_wrapper_rows()
    imports = imported_wrapper_certificates(SYMBOLIC_ROOT)
    write_csv(output / "transient_wrapper_structure.csv", structure_rows)
    write_csv(output / "transient_wrapper_traces.csv", trace_rows)
    write_csv(output / "recurrent_wrapper_controls.csv", recurrent_rows)
    write_json(output / "wrapper_import_certificates.json", imports)
    return {
        "transient_structure_rows": len(structure_rows),
        "transient_trace_rows": len(trace_rows),
        "recurrent_rows": len(recurrent_rows),
        "imported_certificates": len(imports["imports"]),
        "imported_integrity_pass": imports["all_integrity_pass"],
    }


def environment_lock() -> dict[str, object]:
    packages: dict[str, str] = {}
    for name in ("pytest", "PyYAML"):
        try:
            packages[name] = version(name)
        except PackageNotFoundError:
            packages[name] = "not_installed"
    return {
        "candidate_id": CANDIDATE_ID,
        "python_implementation": platform.python_implementation(),
        "python_version": platform.python_version(),
        "integer_arithmetic": "Python arbitrary precision",
        "rational_arithmetic": "fractions.Fraction exact",
        "interval_diagnostics": "decimal.Decimal precision=60 directed rounding",
        "external_numeric_dependencies": [],
        "test_and_schema_packages": packages,
        "python_hash_seed": "0 in canonical runner",
        "bytecode_cache": "disabled in canonical runner",
    }


def route_gate_rows() -> list[dict[str, object]]:
    return [
        {
            "gate": gate,
            "verdict": verdict,
            "evidence_status": status,
            "strongest_reason": reason,
        }
        for gate, verdict, status, reason in (
            ("A0", "A0_STRUCTURAL_ARITHMETIC_RELATION", "PROVED", "ordered quotient word is source-derived"),
            ("A1", "A1_WEAK", "PROVED_OBSTRUCTION", "fixed finite fibers are eventually periodic"),
            ("A2", "A2_ANALYTIC_DETERMINANT", "PROVED", "fixed blocks retain the honest S1 half-plane"),
            ("A3", "A3_FAIL", "STOP_SCOPED", "finite support is periodic, growing memory memorizes, and roof remains factorial"),
            ("A4", "A4_FAIL", "NOT_TESTABLE", "no self-adjoint or critical-line mechanism"),
        )
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "results")
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)

    source, word_rows = source_oracle_certificate(output)
    finite_state = finite_state_artifacts(output)
    recurrence_rows, recurrence = recurrence_artifacts(output)
    memorizer_rows = memorizer_artifacts(output)
    blocks = block_operator_artifacts(output)
    trace_rows = trace_class_artifacts(output)
    wrappers = wrapper_artifacts(output)
    roof_rows = roof_marker_rows(SOURCE_AUDIT_CUTOFF)
    write_csv(output / "roof_marker_mismatch.csv", roof_rows)
    gates = route_gate_rows()
    write_csv(output / "route_gate_summary.csv", gates)
    write_json(output / "environment_lock.json", environment_lock())
    parameters = {
        "candidate_id": CANDIDATE_ID,
        "source_cutoff": SOURCE_AUDIT_CUTOFF,
        "state_sizes": list(STATE_SIZES),
        "recurrence_dimensions": list(RECURRENCE_DIMENSIONS),
        "memorizer_cutoffs": list(MEMORY_CUTOFFS),
        "target_families": list(TARGET_NAMES),
        "block_cutoff": BLOCK_CUTOFF,
        "block_max_power": BLOCK_MAX_POWER,
        "trace_sigmas": list(TRACE_SIGMAS),
        "trace_cutoffs": list(TRACE_CUTOFFS),
        "wrapper_supports": ["prime", "square", "power_of_two", "ultimately_periodic", "seeded_total"],
        "recurrent_padding": "ell(n)=n+17 acceptance-independent",
        "target_zero_evaluation": "not_applicable; no_target_zero_evaluation",
        "route_b_invocation_allowed": False,
    }
    write_json(output / "run_parameters.json", parameters)

    summary = {
        "candidate_id": CANDIDATE_ID,
        "source_cutoff": SOURCE_AUDIT_CUTOFF,
        "source_cycles_checked": len(word_rows),
        "source_edges_checked": source["edges_checked"],
        "source_policy_pass": source["source_policy_pass"],
        "finite_state": finite_state,
        "recurrence": recurrence,
        "recurrence_rows": len(recurrence_rows),
        "memorizer_rows": len(memorizer_rows),
        "memorizer_prefix_failures": sum(not bool(row["exact_prefix_fit"]) for row in memorizer_rows),
        "block_operator": blocks,
        "trace_class_rows": len(trace_rows),
        "trace_interval_failures": sum(not bool(row["interval_ordered"]) for row in trace_rows),
        "wrappers": wrappers,
        "roof_rows": len(roof_rows),
        "roof_identity_failures": sum(not bool(row["edge_monomial_identity"]) for row in roof_rows),
        "post_freeze_selected_count": sum(bool(row["post_freeze_selected"]) for row in roof_rows),
        "first_marker_or_roof_mismatch": 2,
        "route_tuple": [row["verdict"] for row in gates],
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "target_zero_evaluation": "not_applicable; no_target_zero_evaluation",
    }
    write_json(output / "summary.json", summary)
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
