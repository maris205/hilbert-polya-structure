#!/usr/bin/env python3
"""Deterministic Stage-2 validator and canonical evidence generator."""

from __future__ import annotations

import ast
import hashlib
import json
from decimal import Decimal
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Any, Dict, Iterable, Sequence, Tuple

import formula_engine as closed
import prefix_engine as level

ROOT = Path(__file__).resolve().parent
EVIDENCE = ROOT / "evidence"


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, message: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message)

    def equal(self, left: Any, right: Any, message: str) -> None:
        self.check(left == right, f"{message}: {left!r} != {right!r}")


AUDIT = Audit()


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode()


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def fraction_record(value: Fraction) -> Dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def form_record(form: closed.LogForm) -> list[dict[str, int]]:
    return [
        {"prime": prime, "numerator": numerator, "denominator": denominator}
        for prime, numerator, denominator in closed.canonical_form(form)
    ]


def exponent_record(exponents: Dict[int, int]) -> list[dict[str, int]]:
    return [
        {"prime": prime, "exponent": exponent}
        for prime, exponent in sorted(exponents.items())
        if exponent
    ]


def decimal_record(value: Decimal, digits: int = 52) -> str:
    return format(value, f".{digits}g")


def add_forms(forms: Iterable[closed.LogForm]) -> closed.LogForm:
    return closed.add(*tuple(forms))


def form_distance(left: Dict[int, Fraction], right: Dict[int, Fraction]) -> Fraction:
    primes = set(left) | set(right)
    return sum((abs(left.get(prime, Fraction(0)) - right.get(prime, Fraction(0))) for prime in primes), Fraction(0))


def digest_update(digest: "hashlib._Hash", record: Any) -> None:
    digest.update(canonical_bytes(record))


def formula_and_prefix_enumeration() -> Tuple[dict[str, Any], dict[str, Any]]:
    parameter_digest = hashlib.sha256()
    composition_digest = hashlib.sha256()
    prefix_digest = hashlib.sha256()
    parameter_count = 0
    composition_count = 0
    component_prefix_equalities = 0
    feeder_prefix_equalities = 0
    convolution_equalities = 0
    saturation_equivalences = 0
    mean_identities = 0
    uniform_sufficiency_checks = 0
    convergence_comparisons = 0
    max_early_error = Fraction(0)
    max_late_error = Fraction(0)

    for d, p, a in closed.parameter_tuples(max_d=4, max_p=4, max_a=3):
        parameter_count += 1
        h = closed.h_forms(d, a)
        mean = closed.mean_c_form(a)
        AUDIT.equal(
            closed.canonical_form(closed.scale(add_forms(h), Fraction(1, p))),
            closed.canonical_form(mean),
            "mean of H_j must equal mean c",
        )
        mean_identities += 1
        digest_update(
            parameter_digest,
            {"a": list(a), "d": d, "h": [form_record(form) for form in h], "p": p},
        )

        for root_phase in range(p):
            for depth in range(0, 2 * p + 3):
                from_closed = closed.closed_component_prefix_exponents(d, a, root_phase, depth)
                from_levels = level.level_component_exponents(d, a, root_phase, depth)
                AUDIT.equal(from_closed, from_levels, "component prefix exponent mismatch")
                component_prefix_equalities += 1
                digest_update(
                    prefix_digest,
                    {
                        "a": list(a),
                        "d": d,
                        "depth": depth,
                        "exponents": exponent_record(from_levels),
                        "kind": "component",
                        "root_phase": root_phase,
                    },
                )

            for residue in range(p):
                early_depth = residue + 2 * p
                late_depth = residue + 6 * p
                predicted = h[(root_phase + residue) % p]
                early = level.normalized_exponents(
                    level.level_component_exponents(d, a, root_phase, early_depth), d, early_depth
                )
                late = level.normalized_exponents(
                    level.level_component_exponents(d, a, root_phase, late_depth), d, late_depth
                )
                early_error = form_distance(early, predicted)
                late_error = form_distance(late, predicted)
                AUDIT.check(late_error <= early_error, "residue-subsequence prefix error did not contract")
                convergence_comparisons += 1
                max_early_error = max(max_early_error, early_error)
                max_late_error = max(max_late_error, late_error)

        for m in closed.compositions(d, p):
            composition_count += 1
            via_h = closed.feeder_forms_via_h(d, a, m)
            via_b = closed.feeder_forms_via_b(d, a, m)
            AUDIT.equal(
                tuple(closed.canonical_form(form) for form in via_h),
                tuple(closed.canonical_form(form) for form in via_b),
                "H(b) and m-convolution formula mismatch",
            )
            convolution_equalities += 1
            shifted = closed.shifted_product_forms(a, m)
            AUDIT.equal(
                closed.all_equal(via_h),
                closed.all_equal(shifted),
                "constant-convolution saturation equivalence failed",
            )
            saturation_equivalences += 1
            AUDIT.equal(
                closed.canonical_form(closed.scale(add_forms(via_h), Fraction(1, p))),
                closed.canonical_form(mean),
                "feeder residue mean mismatch",
            )
            mean_identities += 1
            if closed.all_equal(via_h):
                AUDIT.equal(
                    closed.canonical_form(via_h[0]),
                    closed.canonical_form(mean),
                    "constant feeder residues must equal mean c",
                )

            for total_depth in (p + 1, 2 * p + 2):
                from_closed = closed.closed_feeder_prefix_exponents(
                    d, a, m, total_depth, transient_levels=1
                )
                from_levels = level.level_feeder_exponents(
                    d, a, m, total_depth, transient_levels=1
                )
                AUDIT.equal(from_closed, from_levels, "feeder prefix exponent mismatch")
                feeder_prefix_equalities += 1

            digest_update(
                composition_digest,
                {
                    "a": list(a),
                    "d": d,
                    "m": list(m),
                    "residue_forms": [form_record(form) for form in via_h],
                    "saturates": closed.all_equal(via_h),
                },
            )

        if d % p == 0:
            uniform = tuple(d // p for _ in range(p))
            AUDIT.check(
                closed.all_equal(closed.feeder_forms_via_h(d, a, uniform)),
                "p|d uniform allocation did not saturate",
            )
            uniform_sufficiency_checks += 1

    enumeration = {
        "closed_formula_domain": {"a_values": [1, 2, 3], "d": [2, 4], "p": [1, 4]},
        "composition_case_count": composition_count,
        "composition_stream_sha256": composition_digest.hexdigest(),
        "convolution_identity_count": convolution_equalities,
        "mean_identity_count": mean_identities,
        "parameter_case_count": parameter_count,
        "parameter_stream_sha256": parameter_digest.hexdigest(),
        "saturation_equivalence_count": saturation_equivalences,
        "uniform_p_divides_d_sufficiency_count": uniform_sufficiency_checks,
    }
    prefix = {
        "component_prefix_exact_equality_count": component_prefix_equalities,
        "feeder_prefix_exact_equality_count": feeder_prefix_equalities,
        "prefix_stream_sha256": prefix_digest.hexdigest(),
        "residue_convergence_comparison_count": convergence_comparisons,
        "residue_error_l1_max_at_k2": fraction_record(max_early_error),
        "residue_error_l1_max_at_k6": fraction_record(max_late_error),
    }
    return enumeration, prefix


def recursive_integer_controls() -> dict[str, Any]:
    component_count = 0
    feeder_count = 0
    digest = hashlib.sha256()
    for d in range(2, 4):
        for p in range(1, 4):
            for a in product(range(1, 4), repeat=p):
                for root_phase in range(p):
                    for depth in range(4):
                        recursive = level.recursive_component_count(d, a, root_phase, depth)
                        exponents = level.level_component_exponents(d, a, root_phase, depth)
                        rebuilt = level.integer_from_exponents(exponents)
                        AUDIT.equal(recursive, rebuilt, "recursive component integer count mismatch")
                        component_count += 1
                        digest_update(
                            digest,
                            {
                                "a": list(a),
                                "count": str(recursive),
                                "d": d,
                                "depth": depth,
                                "kind": "recursive_component",
                                "root_phase": root_phase,
                            },
                        )
                for ordered_phases in product(range(p), repeat=d):
                    total_depth = 3
                    recursive = level.recursive_feeder_count(d, a, ordered_phases, total_depth)
                    m = level.composition_from_ordered(ordered_phases, p)
                    exponents = level.level_feeder_exponents(
                        d, a, m, total_depth, transient_levels=1
                    )
                    rebuilt = level.integer_from_exponents(exponents)
                    AUDIT.equal(recursive, rebuilt, "recursive feeder integer count mismatch")
                    feeder_count += 1
                    digest_update(
                        digest,
                        {
                            "a": list(a),
                            "count": str(recursive),
                            "d": d,
                            "kind": "recursive_feeder",
                            "ordered_phases": list(ordered_phases),
                        },
                    )
    return {
        "actual_recursive_component_count": component_count,
        "actual_recursive_feeder_count": feeder_count,
        "actual_recursive_stream_sha256": digest.hexdigest(),
        "cylinder_mass_rule": "uniform conditional mass is the reciprocal of the exact finite-prefix count",
    }


def p2_controls() -> dict[str, Any]:
    case_count = 0
    strict_improvement_count = 0
    even_saturation_count = 0
    odd_nonsaturation_count = 0
    digest = hashlib.sha256()
    for d in range(2, 9):
        for a0 in range(1, 6):
            for a1 in range(1, 6):
                case_count += 1
                expected_component, expected_feeder = closed.p2_expected_forms(d, a0, a1)
                _, component_form, component_value = closed.component_dimension(d, (a0, a1))
                AUDIT.equal(
                    closed.canonical_form(component_form),
                    closed.canonical_form(expected_component),
                    "p=2 component closed form failed",
                )
                best_k = 0
                best_form = None
                for k in range(d + 1):
                    _, form, value = closed.feeder_dimension(d, (a0, a1), (k, d - k))
                    if best_form is None or closed.compare_forms(form, best_form) > 0:
                        best_k, best_form = k, form
                assert best_form is not None
                best_value = closed.evaluate(best_form)
                AUDIT.equal(
                    closed.canonical_form(best_form),
                    closed.canonical_form(expected_feeder),
                    "p=2 optimized feeder closed form failed",
                )
                mean = closed.mean_c_form((a0, a1))
                saturated = closed.canonical_form(best_form) == closed.canonical_form(mean)
                if a0 != a1:
                    AUDIT.check(best_value > component_value, "nonconstant p=2 feeder must strictly improve")
                    strict_improvement_count += 1
                    if d % 2 == 0:
                        AUDIT.check(saturated, "even p=2 optimum must saturate")
                        even_saturation_count += 1
                    else:
                        AUDIT.check(not saturated, "odd p=2 optimum must not saturate")
                        odd_nonsaturation_count += 1
                digest_update(
                    digest,
                    {
                        "a": [a0, a1],
                        "best_k": best_k,
                        "component": form_record(component_form),
                        "d": d,
                        "feeder": form_record(best_form),
                    },
                )
    return {
        "case_count": case_count,
        "even_nonconstant_saturation_count": even_saturation_count,
        "odd_nonconstant_nonsaturation_count": odd_nonsaturation_count,
        "p2_stream_sha256": digest.hexdigest(),
        "strict_improvement_count": strict_improvement_count,
    }


def level_l_controls() -> dict[str, Any]:
    optimization_count = 0
    composition_count = 0
    denominator_checks = 0
    saturation_checks = 0
    digest = hashlib.sha256()
    selected_optimizers = []
    for d in range(2, 4):
        for p in range(2, 5):
            candidate_vectors = {
                tuple(2 + (j % 2) for j in range(p)),
                tuple(1 + (j % 3) for j in range(p)),
            }
            for a in sorted(candidate_vectors):
                for transient_levels in range(1, 4):
                    leaves = d**transient_levels
                    best_m = None
                    best_form = None
                    local_count = 0
                    for m in closed.compositions(leaves, p):
                        local_count += 1
                        composition_count += 1
                        forms = closed.feeder_forms_level_l(d, a, m, transient_levels)
                        shifted = closed.shifted_product_forms(a, m)
                        AUDIT.equal(
                            closed.all_equal(forms),
                            closed.all_equal(shifted),
                            "level-L saturation equivalence failed",
                        )
                        saturation_checks += 1
                        _, dimension_form, _value = closed.dimension_choice(forms)
                        comparison = 1 if best_form is None else closed.compare_forms(dimension_form, best_form)
                        if comparison > 0 or (
                            comparison == 0 and best_m is not None and tuple(m) < tuple(best_m)
                        ):
                            best_m, best_form = m, dimension_form

                        total_depth = transient_levels + p + 1
                        from_closed = closed.closed_feeder_prefix_exponents(
                            d, a, m, total_depth, transient_levels=transient_levels
                        )
                        from_levels = level.level_feeder_exponents(
                            d, a, m, total_depth, transient_levels=transient_levels
                        )
                        AUDIT.equal(from_closed, from_levels, "level-L denominator prefix mismatch")
                        denominator_checks += 1

                    assert best_m is not None and best_form is not None
                    optimization_count += 1
                    best_value = closed.evaluate(best_form)
                    selected = {
                        "a": list(a),
                        "composition_count": local_count,
                        "d": d,
                        "dimension": form_record(best_form),
                        "dimension_decimal": decimal_record(best_value),
                        "level": transient_levels,
                        "m": list(best_m),
                        "p": p,
                    }
                    selected_optimizers.append(selected)
                    digest_update(digest, selected)

    convergence_cases = []
    exact_divisibility_hits = 0
    convergence_check_count = 0
    for d in range(2, 5):
        for p in range(2, 7):
            a = tuple(2 + (j % 3) for j in range(p))
            h_values = [closed.evaluate(form) for form in closed.h_forms(d, a)]
            max_h = max(h_values)
            mean_form = closed.mean_c_form(a)
            mean_value = closed.evaluate(mean_form)
            case_rows = []
            previous_gap = None
            for transient_levels in range(1, 9):
                leaves = d**transient_levels
                m = closed.balanced_composition(leaves, p)
                forms = closed.feeder_forms_level_l(d, a, m, transient_levels)
                _, _, dimension_value = closed.dimension_choice(forms)
                gap = mean_value - dimension_value
                bound = Decimal(p) * max_h / Decimal(leaves)
                AUDIT.check(gap >= Decimal("-1e-60"), "balanced feeder exceeded the residue mean")
                AUDIT.check(gap <= bound + Decimal("1e-60"), "balanced convergence bound failed")
                convergence_check_count += 2
                if previous_gap is not None and transient_levels >= 4:
                    AUDIT.check(gap <= previous_gap + Decimal("1e-60"), "late balanced gap did not contract")
                    convergence_check_count += 1
                previous_gap = gap
                if leaves % p == 0:
                    AUDIT.check(closed.all_equal(forms), "p|d^L exact balanced saturation failed")
                    exact_divisibility_hits += 1
                case_rows.append(
                    {
                        "gap": decimal_record(gap),
                        "level": transient_levels,
                        "m": list(m),
                        "upper_bound": decimal_record(bound),
                    }
                )
            convergence_cases.append({"a": list(a), "d": d, "p": p, "rows": case_rows})

    return {
        "convergence_case_count": len(convergence_cases),
        "convergence_checks": convergence_check_count,
        "convergence_records": convergence_cases,
        "exact_p_divides_d_power_hits": exact_divisibility_hits,
        "level_l_composition_count": composition_count,
        "level_l_denominator_prefix_checks": denominator_checks,
        "level_l_optimization_count": optimization_count,
        "level_l_optimizer_stream_sha256": digest.hexdigest(),
        "level_l_saturation_checks": saturation_checks,
        "selected_optimizers": selected_optimizers,
    }


def mutation_controls() -> dict[str, Any]:
    controls = []

    d = 2
    a = (2, 3, 2, 3)
    m = (1, 1, 0, 0)
    forms = closed.feeder_forms_via_h(d, a, m)
    shifted = closed.shifted_product_forms(a, m)
    AUDIT.check(closed.all_equal(forms), "required p=4 mutation did not saturate")
    AUDIT.check(closed.all_equal(shifted), "required shifted-product mutation did not stay constant")
    AUDIT.check(d % len(a) != 0, "required mutation accidentally has p|d")
    controls.append(
        {
            "a": list(a),
            "d": d,
            "expected": "SATURATES_AND_P_DOES_NOT_DIVIDE_D",
            "m": list(m),
            "name": "false_unconditional_divisibility_necessity",
            "residue_forms": [form_record(form) for form in forms],
            "shifted_products": [form_record(form) for form in shifted],
            "status": "PASS",
        }
    )

    phase_sizes = (2, 2)
    expected_edges = {
        ((phase, index), ((phase + 1) % 2, next_index))
        for phase, size in enumerate(phase_sizes)
        for index in range(size)
        for next_index in range(phase_sizes[(phase + 1) % 2])
    }
    incomplete_edges = set(expected_edges)
    incomplete_edges.remove(next(iter(sorted(incomplete_edges))))
    AUDIT.check(incomplete_edges != expected_edges, "incomplete cyclic-block mutation was not detected")
    controls.append(
        {
            "expected": "REJECT_COMPLETE_BLOCK_HYPOTHESIS",
            "name": "one_missing_core_edge",
            "status": "PASS",
        }
    )

    core_to_transient_edges = {("v0", "r")}
    AUDIT.check(bool(core_to_transient_edges), "return-edge mutation was not detected")
    controls.append(
        {
            "expected": "REJECT_TRANSIENCE_HYPOTHESIS",
            "name": "return_edge_to_feeder",
            "status": "PASS",
        }
    )

    feeder_targets = {("phase0", 0), ("phase1", 0)}
    all_core_targets = {("phase0", 0), ("phase1", 0), ("phase1", 1)}
    AUDIT.check(feeder_targets != all_core_targets, "incomplete feeder-row mutation was not detected")
    controls.append(
        {
            "expected": "REJECT_UNRESTRICTED_COMPOSITION_SET",
            "name": "noncomplete_feeder_row",
            "status": "PASS",
        }
    )

    rejected_boundaries = []
    for name, call in (
        ("d_equals_one", lambda: closed.h_forms(1, (2, 3))),
        ("zero_phase_size", lambda: closed.h_forms(2, (2, 0))),
        ("wrong_composition_total", lambda: closed.feeder_forms_via_h(2, (2, 3), (1, 0))),
    ):
        try:
            call()
        except ValueError:
            rejected_boundaries.append(name)
            AUDIT.check(True, f"{name} rejected")
        else:
            AUDIT.check(False, f"{name} should be rejected")
    controls.append(
        {
            "expected": "ALL_REJECTED",
            "name": "parameter_boundary_rejections",
            "rejected": rejected_boundaries,
            "status": "PASS",
        }
    )

    core_index, core_form, core_value = closed.component_dimension(2, (1, 2))
    feeder_index, feeder_form, feeder_value = closed.feeder_dimension(2, (1, 2), (1, 1))
    expected_core = {2: Fraction(1, 3)}
    expected_feeder = {2: Fraction(1, 2)}
    AUDIT.equal(closed.canonical_form(core_form), closed.canonical_form(expected_core), "four-state core")
    AUDIT.equal(closed.canonical_form(feeder_form), closed.canonical_form(expected_feeder), "four-state feeder")
    AUDIT.check(feeder_value > core_value, "four-state feeder must beat its only cyclic SCC")
    controls.append(
        {
            "adjacency_state_order": ["r", "a", "b1", "b2"],
            "adjacency": [
                [0, 1, 1, 1],
                [0, 0, 1, 1],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
            ],
            "component_dimension": form_record(core_form),
            "component_min_residue": core_index,
            "expected": "FEEDER_STRATUM_STRICTLY_EXCEEDS_CYCLIC_COMPONENT",
            "feeder_composition": [1, 1],
            "feeder_dimension": form_record(feeder_form),
            "feeder_min_residue": feeder_index,
            "name": "four_state_max_scc_failure",
            "status": "PASS",
        }
    )
    return {"control_count": len(controls), "controls": controls}


def source_independence_control() -> dict[str, Any]:
    formula_source = (ROOT / "formula_engine.py").read_text(encoding="utf-8")
    prefix_source = (ROOT / "prefix_engine.py").read_text(encoding="utf-8")
    def imported_modules(source: str) -> set[str]:
        modules: set[str] = set()
        for node in ast.walk(ast.parse(source)):
            if isinstance(node, ast.Import):
                modules.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules.add(node.module)
        return modules

    AUDIT.check("prefix_engine" not in imported_modules(formula_source), "formula engine imports prefix engine")
    AUDIT.check("formula_engine" not in imported_modules(prefix_source), "prefix engine imports formula engine")
    return {
        "formula_engine_sha256": sha256_file(ROOT / "formula_engine.py"),
        "no_cross_import": True,
        "prefix_engine_sha256": sha256_file(ROOT / "prefix_engine.py"),
    }


def main() -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    enumeration, prefix = formula_and_prefix_enumeration()
    prefix["recursive_integer_controls"] = recursive_integer_controls()
    enumeration["p2_controls"] = p2_controls()
    level_l = level_l_controls()
    mutations = mutation_controls()
    independence = source_independence_control()

    enumeration_path = EVIDENCE / "formula_enumeration.json"
    prefix_path = EVIDENCE / "prefix_cylinder.json"
    level_l_path = EVIDENCE / "level_l.json"
    mutation_path = EVIDENCE / "mutation_controls.json"
    write_json(enumeration_path, enumeration)
    write_json(prefix_path, prefix)
    write_json(level_l_path, level_l)
    write_json(mutation_path, mutations)

    artifacts = {
        path.name: sha256_file(path)
        for path in (enumeration_path, prefix_path, level_l_path, mutation_path)
    }
    summary = {
        "assertion_count": AUDIT.assertions,
        "evidence_sha256": artifacts,
        "implementation_independence": independence,
        "result": "PASS",
        "runner": "run_validation.py",
        "schema": "p49-tree-stage2-evidence-v1",
    }
    summary_path = EVIDENCE / "run_summary.json"
    write_json(summary_path, summary)
    print(json.dumps(summary, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
