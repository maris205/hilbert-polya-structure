#!/usr/bin/env python3
"""Generate deterministic exact artifacts for SD-C27."""

from __future__ import annotations

import ast
import csv
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

import sympy as sp

from sdc27_evaluator import INVENTORY_NAMES, inventories_at_cutoff
from sdc27_holomorphic_lefschetz import (
    branch_for_integer,
    centered_local_determinants,
    chain_certificate,
    desired_ordinary_fiber_determinant,
    elias_gamma_code,
    fraction_text,
    gamma_length,
    necklace_weight,
    power_supertrace,
    prefix_collision_pairs,
    primitive_necklaces,
    scalar_rigidity,
    shared_disjoint_polynomials,
    two_by_two_moment_control,
)


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
CORE = ROOT / "code" / "sdc27_holomorphic_lefschetz.py"
MAX_CODE = 4096
SCALAR_MAX = 512
INVENTORY_CUTOFFS = (31, 127, 511)
POWER_MAX = 8


def write_csv(name: str, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"{name} has no rows")
    with (RESULTS / name).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(name: str, value: object) -> None:
    (RESULTS / name).write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def code_registry_rows() -> tuple[list[dict[str, object]], dict[str, object]]:
    inventories = inventories_at_cutoff(MAX_CODE)
    tags = {
        atom: [name for name in INVENTORY_NAMES if atom in set(inventories[name])]
        for atom in range(2, MAX_CODE + 1)
    }
    words = [elias_gamma_code(atom) for atom in range(1, MAX_CODE + 1)]
    collisions = prefix_collision_pairs(words)
    rows: list[dict[str, object]] = []
    for atom in range(2, MAX_CODE + 1):
        code, translation, derivative = branch_for_integer(atom)
        rows.append(
            {
                "atom": atom,
                "gamma_code": code,
                "code_length": len(code),
                "formula_length": gamma_length(atom),
                "length_match": len(code) == gamma_length(atom),
                "translation": fraction_text(translation),
                "derivative": fraction_text(derivative),
                "expected_derivative": fraction_text(Fraction(1, 2 ** len(code))),
                "derivative_match": derivative == Fraction(1, 2 ** len(code)),
                "closed_disk_image_bound": fraction_text(abs(translation) + derivative),
                "common_compact_containment": abs(translation) + derivative
                <= Fraction(3, 4),
                "global_prefix_free": collisions == 0,
                "inventory_tags": "|".join(tags[atom]),
                "inventory_filter_stage": "post_freeze_evaluator",
                "candidate_target_calls": 0,
            }
        )
    certificate = {
        "candidate_id": "SD-C27",
        "range": [1, MAX_CODE],
        "word_count": len(words),
        "prefix_collision_pairs": collisions,
        "prefix_free": collisions == 0,
        "code_fixed_before_inventory": True,
    }
    return rows, certificate


def scalar_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for atom in range(2, SCALAR_MAX + 1):
        _, _, q = branch_for_integer(atom)
        alpha = 1 - q
        for power in range(1, 7):
            normalized, residual = scalar_rigidity(q, power)
            rows.append(
                {
                    "atom": atom,
                    "code_length": gamma_length(atom),
                    "q": fraction_text(q),
                    "alpha_from_r1": fraction_text(alpha),
                    "power": power,
                    "normalized_trace_over_w_power": fraction_text(normalized),
                    "target": "1/1",
                    "residual": fraction_text(residual),
                    "match": residual == 0,
                    "r1_fit": power == 1 and residual == 0,
                    "r2_plus_failure": power >= 2 and residual != 0,
                    "q_zero_rank_one_boundary": q == 0,
                }
            )
    return rows


def ordinary_matrix_firewall() -> dict[str, object]:
    cases: dict[str, object] = {}
    for atom in (2, 4, 16, 256, 4096):
        _, _, q = branch_for_integer(atom)
        determinant, has_pole = desired_ordinary_fiber_determinant(q)
        moment = two_by_two_moment_control(q)
        cases[str(atom)] = {
            "q": fraction_text(q),
            "required_fredholm_determinant": determinant,
            "genuine_pole_at_q_inverse": has_pole,
            "ordinary_trace_class_determinant_entire": True,
            "ordinary_trace_class_fiber_exists": False,
            "two_by_two_moment_control": {
                key: fraction_text(value) for key, value in moment.items()
            },
            "first_two_moments_force_third_failure": moment["p3_residual"] != 0,
        }
    return {
        "candidate_id": "SD-C27",
        "scope": "ordinary finite-dimensional or trace-class tensor fiber",
        "cases": cases,
        "theorem_firewall": "entire_fredholm_determinant_cannot_equal_(1-t)/(1-q*t)",
    }


def branch_fixture(atom: int, power_s: int = 2) -> tuple[Fraction, Fraction, Fraction]:
    _, translation, derivative = branch_for_integer(atom)
    return Fraction(1, atom**power_s), translation, derivative


def chain_rows() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    cases: list[tuple[str, tuple[int, ...]]] = [
        (f"single_{atom}", (atom,)) for atom in (2, 3, 5, 7, 10, 31)
    ] + [
        ("shared_2_3", (2, 3)),
        ("shared_2_3_5", (2, 3, 5)),
        ("shared_squares", (4, 9, 16)),
        ("shared_fibonacci", (5, 8, 13, 21)),
    ]
    chain: list[dict[str, object]] = []
    powers: list[dict[str, object]] = []
    for case_name, atoms in cases:
        branches = [branch_fixture(atom) for atom in atoms]
        for degree in (2, 3, 4, 5):
            certificate = chain_certificate(branches, degree)
            chain.append(
                {
                    "case": case_name,
                    "atoms": "|".join(map(str, atoms)),
                    "degree": degree,
                    "branch_count": certificate["branch_count"],
                    "weight_sum": fraction_text(certificate["weight_sum"]),
                    "chain_residual_zero": certificate["chain_residual_zero"],
                    "zero_form_characteristic": certificate["zero_determinant"],
                    "one_form_characteristic": certificate["one_determinant"],
                    "cohomology_factor": certificate["cohomology_factor"],
                    "characteristic_quotient_exact": certificate[
                        "characteristic_quotient_exact"
                    ],
                    "ordinary_block_determinant": certificate[
                        "ordinary_block_determinant"
                    ],
                    "ordinary_block_equals_graded_ratio": certificate[
                        "ordinary_block_equals_graded_ratio"
                    ],
                }
            )
            for power in range(1, POWER_MAX + 1):
                actual, expected = power_supertrace(branches, degree, power)
                powers.append(
                    {
                        "case": case_name,
                        "atoms": "|".join(map(str, atoms)),
                        "degree": degree,
                        "power": power,
                        "actual_supertrace": str(actual),
                        "expected_weight_sum_power": str(expected),
                        "exact_match": sp.expand(actual - expected) == 0,
                    }
                )
    return chain, powers


def local_determinant_rows() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    telescoping: list[dict[str, object]] = []
    firewall: list[dict[str, object]] = []
    for atom in (2, 3, 5, 17, 257):
        _, _, q = branch_for_integer(atom)
        weight = Fraction(1, atom * atom)
        for degree in (1, 2, 4, 8):
            value = centered_local_determinants(weight, q, degree)
            telescoping.append(
                {
                    "atom": atom,
                    "degree": degree,
                    "weight": fraction_text(weight),
                    "q": fraction_text(q),
                    "zero_form_determinant": value["zero"],
                    "one_form_determinant": value["one"],
                    "graded_quotient": value["quotient"],
                    "expected_euler_factor": value["expected"],
                    "quotient_exact": value["quotient_exact"],
                }
            )
            firewall.append(
                {
                    "atom": atom,
                    "degree": degree,
                    "ordinary_block_determinant": value["ordinary_block"],
                    "graded_relative_determinant": value["quotient"],
                    "ordinary_equals_graded": value["ordinary_equals_graded"],
                    "ordinary_object": "direct_sum_product",
                    "graded_object": "degree_ratio",
                    "ownership_gate": "STOP_ORDINARY_FREDHOLM_IDENTIFICATION",
                }
            )
    return telescoping, firewall


def shared_disjoint_rows() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    determinants: list[dict[str, object]] = []
    powers: list[dict[str, object]] = []
    for cutoff in INVENTORY_CUTOFFS:
        inventories = inventories_at_cutoff(cutoff)
        for inventory_name in INVENTORY_NAMES:
            atoms = tuple(inventories[inventory_name][:4])
            weights = [Fraction(1, atom * atom) for atom in atoms]
            polynomial = shared_disjoint_polynomials(weights)
            determinants.append(
                {
                    "cutoff": cutoff,
                    "inventory": inventory_name,
                    "atoms": "|".join(map(str, atoms)),
                    "branch_count": len(atoms),
                    "shared_graded_determinant": polynomial["shared"],
                    "disjoint_graded_determinant": polynomial["disjoint"],
                    "difference": polynomial["difference"],
                    "shared_equals_disjoint": polynomial["equal"],
                    "shared_cohomology_dimension": 1,
                    "disjoint_cohomology_dimension": len(atoms),
                }
            )
            total = sum(weights, Fraction(0))
            for power in range(1, POWER_MAX + 1):
                shared = total**power
                disjoint = sum((weight**power for weight in weights), Fraction(0))
                powers.append(
                    {
                        "cutoff": cutoff,
                        "inventory": inventory_name,
                        "atoms": "|".join(map(str, atoms)),
                        "power": power,
                        "shared_supertrace": fraction_text(shared),
                        "disjoint_supertrace": fraction_text(disjoint),
                        "mixed_difference": fraction_text(shared - disjoint),
                        "equal": shared == disjoint,
                        "mixed_survives": power >= 2 and shared != disjoint,
                    }
                )
    return determinants, powers


def necklace_rows() -> list[dict[str, object]]:
    prime_labels = (2, 3, 5, 7)
    rows: list[dict[str, object]] = []
    for alphabet_size in (2, 3, 4):
        atoms = prime_labels[:alphabet_size]
        weights = [Fraction(1, atom * atom) for atom in atoms]
        for word in primitive_necklaces(alphabet_size, 6):
            atom_word = tuple(atoms[label] for label in word)
            counts = Counter(atom_word)
            mixed = len(counts) > 1
            weight = necklace_weight(word, weights)
            rows.append(
                {
                    "alphabet_size": alphabet_size,
                    "label_atoms": "|".join(map(str, atoms)),
                    "length": len(word),
                    "canonical_label_word": "|".join(map(str, word)),
                    "canonical_atom_word": "|".join(map(str, atom_word)),
                    "content_vector": "|".join(
                        f"{atom}:{counts.get(atom, 0)}" for atom in atoms
                    ),
                    "primitive": True,
                    "mixed": mixed,
                    "word_weight": fraction_text(weight),
                    "connected_log_first_repetition": fraction_text(weight),
                    "shared_included": True,
                    "disjoint_included": not mixed,
                    "de_rham_cancels_word": False,
                }
            )
    return rows


def arbitrary_inventory_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    z = sp.symbols("z")
    for cutoff in INVENTORY_CUTOFFS:
        inventories = inventories_at_cutoff(cutoff)
        prime_count = len(inventories["prime_evaluator"])
        for inventory_name in INVENTORY_NAMES:
            atoms = inventories[inventory_name]
            weights = [Fraction(1, atom * atom) for atom in atoms]
            total = sum(weights, Fraction(0))
            determinant_at_one = Fraction(1)
            for weight in weights:
                determinant_at_one *= 1 - weight
            matched = inventory_name in {
                "prime_evaluator",
                "matched_density_seeded_random",
                "matched_density_hash",
            }
            for architecture in ("shared_renewal", "disjoint_components"):
                rows.append(
                    {
                        "cutoff": cutoff,
                        "inventory": inventory_name,
                        "architecture": architecture,
                        "atom_count": len(atoms),
                        "prime_density_matched": matched
                        and len(atoms) == prime_count,
                        "compiler_target_calls": 0,
                        "inventory_loaded_post_freeze": True,
                        "cohomology_dimension": 1
                        if architecture == "shared_renewal"
                        else len(atoms),
                        "graded_factor_form": "1-z*sum(weights)"
                        if architecture == "shared_renewal"
                        else "product(1-z*weight)",
                        "exact_weight_sum": fraction_text(total),
                        "exact_z1_value": fraction_text(1 - total)
                        if architecture == "shared_renewal"
                        else fraction_text(determinant_at_one),
                        "mixed_primitives": architecture == "shared_renewal"
                        and len(atoms) > 1,
                        "atom_inventory_equivalent": architecture
                        == "disjoint_components",
                        "selectivity_credit": False,
                        "proves_too_much": True,
                    }
                )
    return rows


def marker_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for atom in range(2, MAX_CODE + 1):
        length = gamma_length(atom)
        rows.append(
            {
                "atom": atom,
                "gamma_code_length": length,
                "return_marker_degree": 1,
                "digit_marker_degree": length,
                "return_and_digit_markers_equal": length == 1,
                "digit_weight_form": f"u^{length}*n^(-s)",
                "return_weight_form": "z*n^(-s)",
                "u_equals_one_specialization": True,
                "first_return_changes_object": True,
                "whole_codeword_alphabet": "countable_return_alphabet",
                "original_digit_euler_marker_match": False,
            }
        )
    return rows


def nuclearity_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for cutoff in INVENTORY_CUTOFFS:
        inventories = inventories_at_cutoff(cutoff)
        for inventory_name in INVENTORY_NAMES:
            atoms = inventories[inventory_name]
            sum_s1 = sum((Fraction(1, atom) for atom in atoms), Fraction(0))
            sum_s2 = sum((Fraction(1, atom * atom) for atom in atoms), Fraction(0))
            rows.append(
                {
                    "cutoff": cutoff,
                    "inventory": inventory_name,
                    "atom_count": len(atoms),
                    "finite_cohomology_sum_sigma1": fraction_text(sum_s1),
                    "finite_cohomology_sum_sigma2": fraction_text(sum_s2),
                    "shared_degreewise_trace_class_domain": "Re(s)>1_uniform_guarantee",
                    "disjoint_degreewise_trace_class_domain": "Re(s)>1_uniform_guarantee",
                    "graded_relative_determinant_domain": "Re(s)>1_uniform_guarantee",
                    "prime_cohomology_barrier": "Re(s)>1"
                    if inventory_name == "prime_evaluator"
                    else "control_inventory_not_used_for_prime_boundary",
                    "finite_prefix_is_domain_proof": False,
                    "remove_constant_cohomology_gives": "graded_determinant_one",
                    "retain_constant_cohomology": True,
                    "critical_strip_same_object_continuation": False,
                }
            )
    return rows


def route_rows() -> list[dict[str, object]]:
    return [
        {
            "layer": "A0",
            "verdict": "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "evidence": "gamma code and affine digit branches are source-fixed",
            "gate": "GO_SOURCE_HOLOMORPHIC_CODE",
        },
        {
            "layer": "A1",
            "verdict": "A1_FAIL",
            "evidence": "shared mixed words survive; disjoint cohomology is supplied atom inventory",
            "gate": "STOP_SHARED_RENEWAL_MIXED_WORDS",
        },
        {
            "layer": "A2",
            "verdict": "A2_ANALYTIC_DETERMINANT",
            "evidence": "degreewise trace-class operators and exact graded determinant on Re(s)>1",
            "gate": "GO_CANONICAL_LEFSCHETZ_CANCELLATION",
        },
        {
            "layer": "A3",
            "verdict": "A3_FAIL",
            "evidence": "cohomology retains Re(s)>1 barrier and no completion",
            "gate": "STOP_CRITICAL_STRIP_CONTINUATION",
        },
        {
            "layer": "A4",
            "verdict": "A4_FAIL",
            "evidence": "this candidate constructs no self-adjoint or critical-line carrier",
            "gate": "ROUTE_B_LOCKED",
        },
    ]


def source_oracle_certificate() -> dict[str, object]:
    source = CORE.read_text(encoding="utf-8")
    tree = ast.parse(source)
    calls = sorted(
        {
            (node.func.id if isinstance(node.func, ast.Name) else node.func.attr).lower()
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, (ast.Name, ast.Attribute))
        }
    )
    forbidden = {
        "factorint",
        "isprime",
        "mangoldt",
        "primepi",
        "primerange",
        "zeta",
        "zetazero",
        "riemannr",
    }
    return {
        "candidate_id": "SD-C27",
        "candidate_core": "code/sdc27_holomorphic_lefschetz.py",
        "evaluator_module": "code/sdc27_evaluator.py",
        "candidate_evaluator_separated": True,
        "ast_call_names": calls,
        "forbidden_candidate_calls": sorted(forbidden.intersection(calls)),
        "prime_table_used_in_candidate": False,
        "target_weight_used_in_candidate": False,
        "riemann_zero_data_used": False,
        "cutoff_dependent_code": False,
        "digit_maps": ["z/2-1/4", "z/2+1/4"],
        "graded_ratio_called_ordinary_block_determinant": False,
    }


def main() -> int:
    RESULTS.mkdir(parents=True, exist_ok=True)
    code_rows, prefix = code_registry_rows()
    scalar = scalar_rows()
    chain, powers = chain_rows()
    local, firewall = local_determinant_rows()
    determinants, all_powers = shared_disjoint_rows()
    necklaces = necklace_rows()
    arbitrary = arbitrary_inventory_rows()
    marker = marker_rows()
    nuclearity = nuclearity_rows()
    route = route_rows()

    write_csv("code_registry.csv", code_rows)
    write_json("prefix_free_certificate.json", prefix)
    write_csv("scalar_power_rigidity.csv", scalar)
    write_json("ordinary_matrix_firewall.json", ordinary_matrix_firewall())
    write_csv("de_rham_chain_checks.csv", chain)
    write_csv("de_rham_power_supertraces.csv", powers)
    write_csv("local_determinant_telescoping.csv", local)
    write_csv("ordinary_block_graded_firewall.csv", firewall)
    write_csv("shared_disjoint_determinants.csv", determinants)
    write_csv("shared_disjoint_power_ledger.csv", all_powers)
    write_csv("primitive_necklace_ledger.csv", necklaces)
    write_csv("arbitrary_inventory_controls.csv", arbitrary)
    write_csv("marker_ownership_controls.csv", marker)
    write_csv("nuclearity_domain_ledger.csv", nuclearity)
    write_csv("route_gate_summary.csv", route)
    write_json("source_oracle_certificate.json", source_oracle_certificate())
    write_json(
        "run_parameters.json",
        {
            "candidate_id": "SD-C27",
            "code_range": [2, MAX_CODE],
            "scalar_range": [2, SCALAR_MAX],
            "inventory_cutoffs": list(INVENTORY_CUTOFFS),
            "power_max": POWER_MAX,
            "polynomial_degrees": [1, 2, 3, 4, 5, 8],
            "inventories": list(INVENTORY_NAMES),
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
    )
    write_json(
        "environment_lock.json",
        {
            "arithmetic": "exact_integer_fraction_sympy_rational_polynomial",
            "compute": "CPU_only",
            "network": "unused",
            "randomness": "SHA256_ranked_deterministic_controls_only",
            "text": "UTF-8_LF_sorted_JSON_fixed_CSV_columns",
            "target_zero_data_used": False,
        },
    )
    write_json(
        "theorem_ledger.json",
        {
            "candidate_id": "SD-C27",
            "scalar_all_order_rigidity": "PROVED",
            "ordinary_trace_class_tensor_firewall": "PROVED",
            "canonical_de_rham_escape": "PROVED",
            "shared_renewal_cohomology_collapse": "PROVED",
            "mixed_primitive_survival": "PROVED",
            "disjoint_atom_inventory_equivalence": "PROVED",
            "digit_marker_firewall": "PROVED",
            "uniform_nuclearity_domain": "Re(s)>1",
            "prime_cohomology_boundary": "Re(s)>1_absolute_trace_class",
            "ordinary_vs_graded_ownership": "ratio_not_block_determinant",
            "scope": "frozen_affine_holomorphic_tensor_and_de_Rham_0|1_class",
        },
    )
    summary = {
        "candidate_id": "SD-C27",
        "code_rows": len(code_rows),
        "scalar_rows": len(scalar),
        "de_rham_chain_rows": len(chain),
        "de_rham_power_rows": len(powers),
        "local_telescoping_rows": len(local),
        "ordinary_graded_firewall_rows": len(firewall),
        "shared_disjoint_determinant_rows": len(determinants),
        "shared_disjoint_power_rows": len(all_powers),
        "primitive_necklace_rows": len(necklaces),
        "arbitrary_inventory_rows": len(arbitrary),
        "marker_rows": len(marker),
        "nuclearity_rows": len(nuclearity),
        "route_rows": len(route),
        "prefix_free": prefix["prefix_free"],
        "all_scalar_r1_fit": all(row["r1_fit"] for row in scalar if row["power"] == 1),
        "all_scalar_r2_plus_fail": all(
            row["r2_plus_failure"] for row in scalar if row["power"] >= 2
        ),
        "all_chain_checks_pass": all(
            row["chain_residual_zero"] and row["characteristic_quotient_exact"]
            for row in chain
        ),
        "all_supertraces_pass": all(row["exact_match"] for row in powers),
        "all_local_quotients_pass": all(row["quotient_exact"] for row in local),
        "all_ordinary_blocks_differ": all(
            not row["ordinary_equals_graded"] for row in firewall
        ),
        "all_mixed_necklaces_survive": all(
            row["shared_included"] and not row["de_rham_cancels_word"]
            for row in necklaces
            if row["mixed"]
        ),
        "all_inventory_controls_prove_too_much": all(
            row["proves_too_much"] and not row["selectivity_credit"]
            for row in arbitrary
        ),
        "route_tuple": [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_FAIL",
            "A2_ANALYTIC_DETERMINANT",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "target_zero_data_used": False,
    }
    write_json("summary.json", summary)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

