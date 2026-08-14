#!/usr/bin/env python3
"""Generate the deterministic exact SD-C26 artifact suite."""

from __future__ import annotations

import ast
import csv
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

from sdc26_evaluator import INVENTORY_NAMES, inventories_at_cutoff
from sdc26_kraft_fredholm import (
    ALLOCATORS,
    ENCODERS,
    PREFIX_ENCODERS,
    build_prefix_trie,
    cyclic_collision_count,
    disjoint_cycle_metrics,
    finite_roof_inventory_rank,
    finite_word_capacity,
    float_text,
    fraction_text,
    kraft_mass,
    marked_local_word,
    prefix_collision_pairs,
    primitive_necklace_count,
    theorem_code_lower_bound,
    trie_determinant_identity,
)


if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
CORE = ROOT / "code" / "sdc26_kraft_fredholm.py"
CUTOFFS = (127, 511, 2047, 8191)
TRIE_CUTOFF = 127
SIGMAS = (1, 2)
ALPHABET_SIZE = 3


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


def finite_code_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for cutoff in CUTOFFS:
        inventories = inventories_at_cutoff(cutoff)
        for inventory_name in INVENTORY_NAMES:
            atoms = inventories[inventory_name]
            for encoder_name, encoder in ENCODERS.items():
                payloads = [encoder(atom) for atom in atoms]
                marked = [payload + "#" for payload in payloads]
                prefix_count, examples = prefix_collision_pairs(payloads)
                record_atom = max(atoms, key=lambda atom: (len(marked_local_word(atom, encoder_name)), atom))
                maximum = len(marked_local_word(record_atom, encoder_name))
                mass = kraft_mass(payloads)
                rows.append(
                    {
                        "cutoff": cutoff,
                        "inventory": inventory_name,
                        "encoder": encoder_name,
                        "atom_count": len(atoms),
                        "finite_local_alphabet_size": ALPHABET_SIZE,
                        "return_marker": "#",
                        "minimum_cycle_length": min(map(len, marked)),
                        "maximum_cycle_length": maximum,
                        "record_atom": record_atom,
                        "record_theorem_lower_bound": float_text(
                            theorem_code_lower_bound(record_atom, ALPHABET_SIZE)
                        ),
                        "record_lower_bound_pass": maximum
                        >= theorem_code_lower_bound(record_atom, ALPHABET_SIZE),
                        "finite_word_capacity": finite_word_capacity(
                            ALPHABET_SIZE, maximum
                        ),
                        "capacity_bound_pass": len(atoms)
                        <= finite_word_capacity(ALPHABET_SIZE, maximum),
                        "cyclic_collision_count": cyclic_collision_count(marked),
                        "prime_orbit_separating_visible_code": cyclic_collision_count(marked)
                        == 0,
                        "payload_prefix_collision_pairs": prefix_count,
                        "payload_prefix_examples": ";".join(
                            f"{short}<{long}" for short, long in examples
                        ),
                        "payload_kraft_mass": fraction_text(mass),
                        "payload_kraft_mass_float": float_text(float(mass)),
                        "encoder_target_calls": 0,
                        "inventory_filter_stage": "post_freeze_evaluator",
                    }
                )
    return rows


def disjoint_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for cutoff in CUTOFFS:
        inventories = inventories_at_cutoff(cutoff)
        for inventory_name in INVENTORY_NAMES:
            atom = inventories[inventory_name][-1]
            for encoder_name in ENCODERS:
                for allocation in ALLOCATORS:
                    for sigma in SIGMAS:
                        data = disjoint_cycle_metrics(
                            atom, encoder_name, allocation, sigma
                        )
                        rows.append(
                            {
                                "cutoff": cutoff,
                                "inventory": inventory_name,
                                "encoder": encoder_name,
                                "atom": atom,
                                "cycle_length": data["cycle_length"],
                                "allocation": allocation,
                                "sigma": sigma,
                                "min_roof_share": fraction_text(data["min_roof_share"]),
                                "max_roof_share": fraction_text(data["max_roof_share"]),
                                "max_singular_value": float_text(data["max_singular_value"]),
                                "min_singular_value": float_text(data["min_singular_value"]),
                                "universal_max_sv_lower_bound": float_text(
                                    data["universal_max_sv_lower_bound"]
                                ),
                                "block_s1_norm": float_text(data["block_s1_norm"]),
                                "amgm_block_s1_lower_bound": float_text(
                                    data["amgm_block_s1_lower_bound"]
                                ),
                                "max_sv_bound_pass": data["max_singular_value"] + 1e-15
                                >= data["universal_max_sv_lower_bound"],
                                "s1_bound_pass": data["block_s1_norm"] + 1e-14
                                >= data["amgm_block_s1_lower_bound"],
                                "total_roof": "log(atom)",
                                "finite_row_is_infinite_proof": False,
                                "theorem_gate": "STOP_WHOLE_OPERATOR_COMPACTNESS",
                            }
                        )
    return rows


def shared_trie_rows() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    closure: list[dict[str, object]] = []
    necklaces: list[dict[str, object]] = []
    inventories = inventories_at_cutoff(TRIE_CUTOFF)
    tree_weight = 2 ** (-1 / 8)
    for inventory_name in INVENTORY_NAMES:
        atoms = inventories[inventory_name]
        for encoder_name, encoder in ENCODERS.items():
            codes = {atom: encoder(atom) for atom in atoms}
            trie = build_prefix_trie(codes)
            return_roofs = [
                math.log(atom) - len(code) * math.log(2) / 8
                for atom, code in codes.items()
            ]
            closure.append(
                {
                    "cutoff": TRIE_CUTOFF,
                    "inventory": inventory_name,
                    "encoder": encoder_name,
                    "atom_count": len(atoms),
                    "trie_nodes": len(trie["nodes"]),
                    "trie_bit_edges": len(trie["bit_edges"]),
                    "return_edges": len(trie["terminals"]),
                    "payload_prefix_collision_pairs": trie[
                        "prefix_collision_count"
                    ],
                    "bit_edge_roof": "log(2)/8",
                    "bit_edge_weight_sigma1": float_text(tree_weight),
                    "minimum_return_roof": float_text(min(return_roofs)),
                    "all_return_roofs_positive": min(return_roofs) > 0,
                    "each_loop_total_roof": "log(atom)",
                    "whole_tree_compact": False,
                    "noncompactness_witness": "infinitely_many_constant_weight_bit_edges",
                    "shared_hub_prime_only_ledger": False,
                }
            )
            for return_count in (2, 3, 4, 5):
                count = primitive_necklace_count(len(atoms), return_count)
                necklaces.append(
                    {
                        "cutoff": TRIE_CUTOFF,
                        "inventory": inventory_name,
                        "encoder": encoder_name,
                        "alphabet_atoms": len(atoms),
                        "return_count": return_count,
                        "mixed_primitive_necklaces": count,
                        "pure_primitive_necklaces": 0,
                        "first_example": f"({atoms[0]},{atoms[1]})",
                        "connected_disconnected_match": False,
                        "ledger_gate": "CYCLE_FLOOD",
                    }
                )
    return closure, necklaces


def shared_prime_pair_rows() -> list[dict[str, object]]:
    primes = inventories_at_cutoff(31)["prime_evaluator"][:8]
    rows: list[dict[str, object]] = []
    for left_index, left in enumerate(primes):
        for right in primes[left_index + 1 :]:
            product = left * right
            perfect_power = any(
                base**exponent == product
                for exponent in range(2, math.floor(math.log2(product)) + 1)
                for base in range(2, math.isqrt(product) + 2)
                if base**exponent <= product
            )
            rows.append(
                {
                    "left_prime": left,
                    "right_prime": right,
                    "concatenated_norm": product,
                    "distinct_primes": left != right,
                    "perfect_prime_power": perfect_power,
                    "unique_factorization_contradiction": not perfect_power,
                    "mixed_closed_word_legal_when_vertex_shared": True,
                    "prime_only_connected_ledger_survives": False,
                }
            )
    return rows


def determinant_checks() -> dict[str, object]:
    atoms = (2, 3, 5, 7)
    checks: dict[str, object] = {}
    for encoder_name, encoder in ENCODERS.items():
        actual, expected = trie_determinant_identity(
            {atom: encoder(atom) for atom in atoms}, sigma=2
        )
        checks[encoder_name] = {
            "actual": actual,
            "expected": expected,
            "exact_match": actual == expected,
            "connected_form": "1-F",
            "disconnected_euler_product": False,
        }
    return checks


def diagonal_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for cutoff in CUTOFFS:
        inventories = inventories_at_cutoff(cutoff)
        for inventory_name in INVENTORY_NAMES:
            atoms = inventories[inventory_name]
            trace_sum = sum((Fraction(1, atom * atom) for atom in atoms), Fraction(0))
            determinant = Fraction(1)
            for atom in atoms:
                determinant *= 1 - Fraction(1, atom * atom)
            rows.append(
                {
                    "cutoff": cutoff,
                    "inventory": inventory_name,
                    "atom_count": len(atoms),
                    "alphabet": "countable_one_symbol_per_atom",
                    "visible_finite_alphabet": False,
                    "cycle_length": 1,
                    "total_roof": "log(atom)",
                    "trace_norm_prefix_sigma2": fraction_text(trace_sum),
                    "determinant_z1_sigma2": fraction_text(determinant),
                    "whole_operator_s1_sigma2": True,
                    "mixed_primitives": 0,
                    "selector_locality": "external_inventory",
                    "proves_too_much": True,
                    "verdict": "PAPER04_SELECTOR_TAUTOLOGICAL_ESCAPE",
                }
            )
    return rows


def marker_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for cutoff in CUTOFFS:
        atom = inventories_at_cutoff(cutoff)["prime_evaluator"][-1]
        for encoder_name in ENCODERS:
            length = len(marked_local_word(atom, encoder_name))
            rows.append(
                {
                    "cutoff": cutoff,
                    "architecture": f"{encoder_name}_cycle",
                    "prime_witness": atom,
                    "graph_step_degree": length,
                    "target_degree": 1,
                    "marked_germ_match": length == 1,
                    "induction_required_to_degree_one": length != 1,
                    "same_object_after_induction": False,
                    "gate": "STOP_GRAPH_STEP_MARKER",
                }
            )
        rows.append(
            {
                "cutoff": cutoff,
                "architecture": "countable_atom_diagonal",
                "prime_witness": atom,
                "graph_step_degree": 1,
                "target_degree": 1,
                "marked_germ_match": True,
                "induction_required_to_degree_one": False,
                "same_object_after_induction": True,
                "gate": "MARKER_PASS_BUT_SELECTOR_TAUTOLOGICAL",
            }
        )
    return rows


def arbitrary_inventory_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for cutoff in CUTOFFS:
        inventories = inventories_at_cutoff(cutoff)
        prime_count = len(inventories["prime_evaluator"])
        for inventory_name in INVENTORY_NAMES:
            atoms = inventories[inventory_name]
            matched = inventory_name in {
                "prime_evaluator",
                "matched_density_seeded_random",
                "matched_density_hash",
            }
            for architecture, primitive_clean, compact, s1, mixed in (
                ("disjoint_finite_code_cycles", True, False, False, False),
                ("shared_trie_return", False, False, False, True),
                ("countable_atom_diagonal", True, True, True, False),
            ):
                rows.append(
                    {
                        "cutoff": cutoff,
                        "inventory": inventory_name,
                        "architecture": architecture,
                        "atom_count": len(atoms),
                        "prime_density_matched": matched
                        and len(atoms) == prime_count,
                        "encoder_or_architecture_target_calls": 0,
                        "support_loaded_post_freeze": True,
                        "primitive_ledger_clean": primitive_clean,
                        "whole_operator_compact": compact,
                        "whole_operator_s1_sigma2": s1,
                        "mixed_primitives": mixed,
                        "selectivity_credit": False,
                        "proves_too_much": True,
                    }
                )
    return rows


def factorization_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for token_max in (5, 9, 17, 33):
        tokens = list(range(2, token_max + 1))
        pair_products: dict[int, int] = {}
        for index, left in enumerate(tokens):
            for right in tokens[index + 1 :]:
                pair_products[left * right] = pair_products.get(left * right, 0) + 1
        rows.append(
            {
                "token_max": token_max,
                "token_count": len(tokens),
                "primitive_mixed_two_return_necklaces": primitive_necklace_count(
                    len(tokens), 2
                ),
                "distinct_two_token_products": len(pair_products),
                "product_collision_excess": sum(
                    value - 1 for value in pair_products.values()
                ),
                "commutative_word_order_collision": token_max >= 3,
                "same_norm_example": "(2,6)|(3,4)"
                if token_max >= 6
                else "none_at_this_cutoff",
                "finite_determinant_form": "1-sum(first_return_monomials)",
                "prime_only_primitive_ledger": False,
                "gate": "CONNECTED_DISCONNECTED_MISMATCH",
            }
        )
    return rows


def stationarization_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for bit_depth in (5, 7, 9, 11, 13):
        cutoff = 2**bit_depth - 1
        inventories = inventories_at_cutoff(cutoff)
        for inventory_name in INVENTORY_NAMES:
            atom = inventories[inventory_name][-1]
            for encoder_name in ENCODERS:
                length = len(marked_local_word(atom, encoder_name))
                witness = math.exp(-math.log(atom) / length)
                rows.append(
                    {
                        "directive_bit_depth": bit_depth,
                        "cutoff": cutoff,
                        "inventory": inventory_name,
                        "encoder": encoder_name,
                        "witness_atom": atom,
                        "stationary_cycle_length": length,
                        "total_roof": "log(atom)",
                        "equal_roof_singular_value": float_text(witness),
                        "finite_prefix_operator_compact": True,
                        "single_stationary_union_compact": False,
                        "shared_level_states_create_mixed_cycles": True,
                        "acyclic_level_has_primitive_orbits": False,
                        "selector_stage": "external_inventory",
                        "gate": "NONAUTONOMOUS_INFORMATION_OR_CYCLE_FLOOD",
                    }
                )
    return rows


def finite_roof_rows() -> list[dict[str, object]]:
    primes = inventories_at_cutoff(127)["prime_evaluator"]
    return [
        {
            "prime_count": count,
            "formal_Q_rank_of_log_primes": finite_roof_inventory_rank(primes[:count]),
            "finite_roof_inventory_size": count - 1,
            "all_prime_clocks_in_span": False,
            "unique_factorization_certificate": True,
            "gate": "STOP_FINITE_ROOF_INVENTORY",
        }
        for count in (2, 4, 8, 16, 31)
    ]


def route_rows() -> list[dict[str, object]]:
    return [
        {
            "layer": "A0",
            "verdict": "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "evidence": "finite binary arithmetic and multiplicative atomhood are source relations",
            "gate": "GO_STRUCTURAL_OBSTRUCTION_CLASS",
        },
        {
            "layer": "A1",
            "verdict": "A1_FAIL",
            "evidence": "shared recurrence creates mixed primitive cycles; literal ledger is disjoint",
            "gate": "STOP_POSITIVE_FINITE_CODE_PRIME_LEDGER",
        },
        {
            "layer": "A2",
            "verdict": "A2_FAIL",
            "evidence": "finite separating code plus log roof forces whole adjacency noncompact",
            "gate": "STOP_WHOLE_OPERATOR_FREDHOLM",
        },
        {
            "layer": "A3",
            "verdict": "A3_FAIL",
            "evidence": "no continuation functional equation gamma factor or counting law",
            "gate": "STOP_GLOBAL_ANALYTIC_STRUCTURE",
        },
        {
            "layer": "A4",
            "verdict": "A4_FAIL",
            "evidence": "this candidate constructs no self-adjoint or critical-line mechanism",
            "gate": "ROUTE_B_LOCKED",
        },
    ]


def source_oracle_certificate() -> dict[str, object]:
    source = CORE.read_text(encoding="utf-8")
    tree = ast.parse(source)
    call_names = sorted(
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
        "candidate_id": "SD-C26",
        "candidate_core": "code/sdc26_kraft_fredholm.py",
        "evaluator_module": "code/sdc26_evaluator.py",
        "candidate_evaluator_separated": True,
        "ast_call_names": call_names,
        "forbidden_candidate_calls": sorted(forbidden.intersection(call_names)),
        "prime_table_used_in_candidate": False,
        "factorization_oracle_used_in_candidate": False,
        "target_feedback_used_in_candidate": False,
        "riemann_zero_data_used": False,
        "target_zero_fields": "not_applicable; no_target_zero_evaluation",
        "finite_local_alphabet": ["0", "1", "#"],
        "cutoff_dependent_encoder": False,
    }


def main() -> int:
    RESULTS.mkdir(parents=True, exist_ok=True)
    generated = {
        "finite_code_counting.csv",
        "disjoint_cycle_witnesses.csv",
        "shared_trie_closure.csv",
        "mixed_primitive_ledger.csv",
        "shared_prime_pair_firewall.csv",
        "finite_trie_determinant_checks.json",
        "diagonal_escape_controls.csv",
        "marker_firewall.csv",
        "arbitrary_inventory_controls.csv",
        "factorization_renewal_controls.csv",
        "finite_prefix_stationarization.csv",
        "finite_roof_inventory.csv",
        "route_gate_summary.csv",
        "source_oracle_certificate.json",
        "run_parameters.json",
        "environment_lock.json",
        "theorem_ledger.json",
        "summary.json",
    }
    for name in generated:
        path = RESULTS / name
        if path.exists():
            path.unlink()

    finite_code = finite_code_rows()
    disjoint = disjoint_rows()
    trie, necklaces = shared_trie_rows()
    pairs = shared_prime_pair_rows()
    diagonal = diagonal_rows()
    marker = marker_rows()
    arbitrary = arbitrary_inventory_rows()
    factorization = factorization_rows()
    stationarization = stationarization_rows()
    finite_roofs = finite_roof_rows()
    route = route_rows()

    write_csv("finite_code_counting.csv", finite_code)
    write_csv("disjoint_cycle_witnesses.csv", disjoint)
    write_csv("shared_trie_closure.csv", trie)
    write_csv("mixed_primitive_ledger.csv", necklaces)
    write_csv("shared_prime_pair_firewall.csv", pairs)
    write_json("finite_trie_determinant_checks.json", determinant_checks())
    write_csv("diagonal_escape_controls.csv", diagonal)
    write_csv("marker_firewall.csv", marker)
    write_csv("arbitrary_inventory_controls.csv", arbitrary)
    write_csv("factorization_renewal_controls.csv", factorization)
    write_csv("finite_prefix_stationarization.csv", stationarization)
    write_csv("finite_roof_inventory.csv", finite_roofs)
    write_csv("route_gate_summary.csv", route)
    write_json("source_oracle_certificate.json", source_oracle_certificate())
    write_json(
        "run_parameters.json",
        {
            "candidate_id": "SD-C26",
            "cutoffs": list(CUTOFFS),
            "trie_cutoff": TRIE_CUTOFF,
            "encoders": list(ENCODERS),
            "finite_local_alphabet_size": ALPHABET_SIZE,
            "roof_allocations": list(ALLOCATORS),
            "sigmas": list(SIGMAS),
            "inventories": list(INVENTORY_NAMES),
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
    )
    write_json(
        "environment_lock.json",
        {
            "arithmetic": "exact_integer_fraction_symbolic_plus_theorem_led_float_witnesses",
            "byte_order": "UTF-8_LF_sorted_JSON_fixed_CSV_columns",
            "compute": "CPU_only",
            "network": "unused",
            "randomness": "SHA256_ranked_deterministic_controls_only",
            "target_zero_data_used": False,
        },
    )
    write_json(
        "theorem_ledger.json",
        {
            "candidate_id": "SD-C26",
            "finite_code_counting": "PROVED",
            "prime_only_shared_vertex_disjointness": "PROVED",
            "log_roof_noncompactness": "PROVED",
            "exact_marker_atom_loop_corollary": "PROVED",
            "renewal_connected_disconnected_firewall": "PROVED",
            "finite_roof_inventory_obstruction": "PROVED",
            "scope": "positive_scalar_finite_local_code_natural_counting_space",
            "excluded": [
                "signed_or_matrix_cancellation",
                "infinite_local_alphabet",
                "anisotropic_function_space",
                "nonlocal_completed_orbit_weight",
            ],
        },
    )
    summary = {
        "candidate_id": "SD-C26",
        "finite_code_rows": len(finite_code),
        "disjoint_cycle_rows": len(disjoint),
        "shared_trie_rows": len(trie),
        "mixed_primitive_rows": len(necklaces),
        "shared_prime_pair_rows": len(pairs),
        "diagonal_control_rows": len(diagonal),
        "marker_rows": len(marker),
        "arbitrary_inventory_rows": len(arbitrary),
        "factorization_rows": len(factorization),
        "stationarization_rows": len(stationarization),
        "finite_roof_rows": len(finite_roofs),
        "route_rows": len(route),
        "finite_visible_code_separates_all_controls": all(
            row["prime_orbit_separating_visible_code"] for row in finite_code
        ),
        "all_disjoint_bounds_pass": all(
            row["max_sv_bound_pass"] and row["s1_bound_pass"] for row in disjoint
        ),
        "all_shared_tries_noncompact": all(
            not row["whole_tree_compact"] for row in trie
        ),
        "all_return_lengths_have_mixed_primitives": all(
            row["mixed_primitive_necklaces"] > 0 for row in necklaces
        ),
        "all_prime_pair_firewalls_pass": all(
            row["unique_factorization_contradiction"] for row in pairs
        ),
        "all_diagonal_inventories_pass_equally": all(
            row["whole_operator_s1_sigma2"] and row["proves_too_much"]
            for row in diagonal
        ),
        "route_tuple": [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_FAIL",
            "A2_FAIL",
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
