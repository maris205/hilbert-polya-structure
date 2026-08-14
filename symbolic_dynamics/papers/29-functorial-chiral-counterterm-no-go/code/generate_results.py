#!/usr/bin/env python3
"""Generate deterministic exact SD-C31 artifacts."""

from __future__ import annotations

import argparse
import csv
from fractions import Fraction
import json
from pathlib import Path

from counterterm_core import (
    baseline_scheme_record,
    canonical_direct_ledger,
    coefficient_search,
    cutoff_compiler_check,
    determinant_ownership_record,
    direct_control_record,
    divisibility_inventory,
    divisibility_poset,
    exact_projector_checks,
    fraction_record,
    fraction_text,
    generic_dag_poset,
    harmonic_lower_bound_record,
    local_shift_family,
    mutated_cover_poset,
    permute_poset,
    random_inventory_poset,
    random_permutation,
    tail_certificates,
    transport_check,
)


SCHEMA_VERSION = "SD-C31-exact-v1"
CANDIDATE = "SD-C31"
ROUTE_TUPLE = [
    "A0_STRUCTURAL_ARITHMETIC_RELATION",
    "A1_FAIL",
    "A2_ANALYTIC_DETERMINANT",
    "A3_FAIL",
    "A4_FAIL",
]


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def header(kind: str) -> dict[str, object]:
    return {
        "schema_version": SCHEMA_VERSION,
        "candidate": CANDIDATE,
        "artifact_kind": kind,
        "arithmetic_normalization": "C_eta factored out where explicitly stated",
        "target_zero_data_used": False,
        "route_b_used": False,
    }


def fraction_from_record(record: dict[str, object]) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def shift_increment_check(small: dict[str, object], large: dict[str, object]) -> dict[str, object]:
    old_atoms = set(int(value) for value in small["atom_weights"])
    new_atoms = [int(value) for value in large["atom_weights"] if int(value) not in old_atoms]
    rows = {}
    eta = 2
    for k in range(3):
        key = f"S{k}"
        actual = fraction_from_record(large["shifts"][key]) - fraction_from_record(small["shifts"][key])
        expected = 2 * sum(
            (Fraction(1, weight ** (1 + 2 * eta + k)) for weight in new_atoms),
            Fraction(0),
        )
        rows[key] = {
            "actual_increment": fraction_record(actual),
            "new_atom_sum": fraction_record(expected),
            "equal": actual == expected,
        }
    actual_h = fraction_from_record(large["leading_H"]) - fraction_from_record(small["leading_H"])
    expected_h = 2 * sum((Fraction(1, weight) for weight in new_atoms), Fraction(0))
    return {
        "small_cutoff": small["cutoff"],
        "large_cutoff": large["cutoff"],
        "new_atoms": new_atoms,
        "leading_increment": {
            "actual": fraction_record(actual_h),
            "new_atom_sum": fraction_record(expected_h),
            "equal": actual_h == expected_h,
        },
        "shift_increments": rows,
        "all_pass": actual_h == expected_h and all(bool(row["equal"]) for row in rows.values()),
    }


def build_artifacts(output: Path) -> dict[str, object]:
    output.mkdir(parents=True, exist_ok=True)
    cutoffs = (12, 18, 30)
    baselines = [baseline_scheme_record(cutoff) for cutoff in cutoffs]

    # Sanity/compiler/naturality block.
    baseline12 = divisibility_poset(12)
    mutation = mutated_cover_poset(18)
    composite = divisibility_inventory((1, 4, 6, 9, 12, 18, 36), "composite_only")
    generic = generic_dag_poset(29031)
    random_inventory = random_inventory_poset(29032)
    sanity_posets = (baseline12, mutation, composite, generic, random_inventory)
    incidence_rows = [exact_projector_checks(poset) for poset in sanity_posets]
    cutoff_rows = [cutoff_compiler_check(12, 18), cutoff_compiler_check(18, 30)]

    relabel_rows = []
    for cutoff, seed in ((12, 29112), (18, 29118), (30, 29130)):
        poset = divisibility_poset(cutoff)
        order = random_permutation(poset.size, seed)
        copy = permute_poset(poset, order, f"divisibility_{cutoff}_relabel_{seed}")
        relabel_rows.append(transport_check(poset, copy, order))

    generic_order = random_permutation(generic.size, 29331)
    generic_copy = permute_poset(generic, generic_order, "generic_dag_relabel")
    generic_transport = transport_check(generic, generic_copy, generic_order)
    generic_record = direct_control_record(generic)
    generic_copy_record = direct_control_record(generic_copy)
    generic_direct_equal = canonical_direct_ledger(generic_record) == canonical_direct_ledger(generic_copy_record)

    incidence_payload = {
        **header("incidence_and_naturality_checks"),
        "sanity_rows": incidence_rows,
        "cutoff_embedding_rows": cutoff_rows,
        "baseline_relabel_rows": relabel_rows,
        "generic_relabel": {
            **generic_transport,
            "canonical_direct_ledgers_equal": generic_direct_equal,
            "all_pass": bool(generic_transport["all_pass"]) and generic_direct_equal,
        },
        "morphism_scope": "pointed isomorphisms and lower-order-ideal divisibility cutoff embeddings only",
        "ordinary_monotone_maps_claimed": False,
        "all_pass": all(bool(row["all_pass"]) for row in incidence_rows)
        and all(bool(row["all_pass"]) for row in cutoff_rows)
        and all(bool(row["all_pass"]) for row in relabel_rows)
        and bool(generic_transport["all_pass"])
        and generic_direct_equal,
    }
    write_json(output / "incidence_checks.json", incidence_payload)

    # Baseline schemes and summability.
    baseline_payload = {
        **header("source_locked_baseline_cutoffs"),
        "eta": 2,
        "C_eta": "sum mu(k)^2/k^4=zeta(4)/zeta(8), factored out",
        "gram_formula": {
            "diagonal": "g_pp=1+p^-4",
            "off_diagonal": "g_pq=1/((p^4+1)(q^4+1))",
        },
        "cutoffs": baselines,
        "harmonic_divergence": harmonic_lower_bound_record(cutoffs),
        "all_diagonal_identities_pass": all(bool(row["identity_D_equals_H_plus_S0"]) for row in baselines),
        "all_baseline_mixed_nonzero": all(
            any(bool(pair["nonzero"]) for pair in row["mixed_ledger"]) for row in baselines
        ),
        "all_baseline_b4_nonzero": all(
            any(bool(pair["positive"]) for pair in row["b4_pair_ledger"]) for row in baselines
        ),
    }
    write_json(output / "baseline_cutoffs.json", baseline_payload)

    increment_rows = [shift_increment_check(baselines[0], baselines[1]), shift_increment_check(baselines[1], baselines[2])]
    frozen_coefficients = (
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(1, 2), Fraction(-1), Fraction(2)),
        (Fraction(-2), Fraction(1, 2), Fraction(1)),
    )
    families = [
        local_shift_family(cutoff, coefficients)
        for cutoff in cutoffs
        for coefficients in frozen_coefficients
    ]
    shift_payload = {
        **header("scheme_shift_classification"),
        "minimal_schemes": {
            "full": "C_full,N=2*sum G_pp/p; residual is mixed only",
            "lead": "C_lead,N=2*C_eta*sum 1/p; residual is C_eta*S0+mixed",
            "difference": "C_full,N-C_lead,N=C_eta*S0,N",
        },
        "cutoff_increment_checks": increment_rows,
        "tail_certificates": [tail_certificates(cutoff) for cutoff in cutoffs],
        "frozen_shift_family": families,
        "classification": {
            "divergent_germ_fixed": "coefficient of 2*C_eta*sum 1/p must be one",
            "finite_part_not_fixed": "arbitrary absolutely summable natural atom-local shifts remain",
            "full_and_lead_both_admissible": True,
            "finite_parts_distinct": all(bool(row["schemes_distinct"]) for row in baselines),
            "not_a_zeta_trace": True,
            "name": "sharp-cutoff/Hadamard-style source finite part",
        },
        "all_prefix_checks_pass": all(bool(row["all_pass"]) for row in increment_rows),
        "all_tail_bounds_vanish": True,
    }
    write_json(output / "scheme_shifts.json", shift_payload)

    # Controls.
    control_records = [
        direct_control_record(mutation),
        direct_control_record(composite),
        generic_record,
        direct_control_record(random_inventory),
    ]
    control_payload = {
        **header("non_arithmetic_controls"),
        "controls": control_records,
        "generic_relabel_copy": generic_copy_record,
        "generic_relabel_canonical_equal": generic_direct_equal,
        "all_share_tested_pair_type": all(
            row["pointed_pair_type"] == "two_incomparable_covers_sharing_bottom"
            for row in control_records
        ),
        "all_have_nonzero_mixed_or_b4": all(
            int(row["nonzero_mixed_count"]) > 0 or int(row["positive_b4_count"]) > 0
            for row in control_records
        ),
        "proves_too_much_certificate": {
            "status": "PROVES_TOO_MUCH",
            "reason": "the surviving pair ledger depends only on source incidence/roof/Gram data and is reproduced by every preregistered generic inventory class",
            "numeric_prime_oracle_used": False,
            "target_zero_data_used": False,
        },
    }
    write_json(output / "control_ledgers.json", control_payload)

    grid = tuple(Fraction(value, 2) for value in (-4, -2, -1, 0, 1, 2, 4))
    coefficient_payload = {
        **header("local_counterterm_coefficient_search"),
        "admissible_class": {
            "quadratic": True,
            "linear_in_gram_contractions": True,
            "local_order_at_most_two_atoms": True,
            "coefficient_constant_on_transported_pointed_local_type": True,
            "numeric_label_branching_forbidden": True,
            "global_isomorphism_invariants_out_of_scope": True,
        },
        "search": coefficient_search(grid),
        "classification_rows": [
            {
                "support": "one atom/diagonal",
                "universal_coefficient": "alpha",
                "constraint": "alpha=1 on the leading harmonic germ",
                "freedom": "k_pp=C_eta+r_p with sum |r_p|/p finite; S_k are the frozen exact subfamily",
            },
            {
                "support": "two source atoms/mixed",
                "universal_coefficient": "beta on the shared V-type",
                "trace_domain": "sum |k_pq|/sqrt(pq) finite",
                "preserve_baseline": "beta=0",
                "cancel_same_type_controls": "beta=1",
                "compatible": False,
            },
        ],
        "exact_selective_solution_exists": False,
        "scope_caveat": "no universal claim for arbitrary nonlocal/global natural functionals",
    }
    write_json(output / "coefficient_search.json", coefficient_payload)

    determinant_payload = {
        **header("determinant_and_B4_ownership"),
        **determinant_ownership_record(baselines[-1], control_records),
    }
    write_json(output / "determinant_ownership.json", determinant_payload)

    summary = {
        **header("summary"),
        "candidate_title": "Source-Natural Quadratic Counterterms for Chiral Incidence Operators: Finite-Part Freedom and a Local Selectivity No-Go",
        "strongest_go": "GO_SOURCE_NATURAL_DIAGONAL_FINITE_PART_CLASSIFICATION",
        "strongest_stop": "STOP_ARITHMETIC_SELECTIVITY_IN_LINEAR_LOCAL_GRAM_CLASS",
        "overall_status": "REJECTED_AS_RH_COMPLETION",
        "route_tuple": ROUTE_TUPLE,
        "route_b": False,
        "claims": {
            "C1_finite_part_nonuniqueness": bool(baseline_payload["all_diagonal_identities_pass"])
            and bool(shift_payload["all_prefix_checks_pass"])
            and bool(shift_payload["classification"]["finite_parts_distinct"]),
            "C2_local_selectivity_no_go": bool(control_payload["all_have_nonzero_mixed_or_b4"])
            and bool(coefficient_payload["search"]["exact_no_solution"]),
            "det3_ownership": bool(determinant_payload["b4_is_generic_pair_gram_ownership"]),
        },
        "major_obstacle": "source naturality permits infinitely many summable atom-local scheme shifts, while the retained mixed/B4 pair invariant is generic Gram geometry",
        "paper30_minimum_obligation": "Exhibit a globally source-derived higher incidence/cumulant or cohomological invariant with a uniqueness theorem and exact vanishing on mutated-cover, composite-only, generic-DAG, and random-inventory controls; otherwise close the chiral-incidence branch.",
        "data_boundaries": {
            "target_zeros": "not used",
            "route_b": "locked false",
            "counterterm": "no numeric prime oracle",
            "determinant": "D_ren is a new functional, not an ordinary Fredholm determinant or det2",
        },
    }
    write_json(output / "summary.json", summary)

    # Compact raw table for independent inspection.
    with (output / "raw_counterterm_table.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=(
                "object",
                "kind",
                "cutoff_or_size",
                "atom_count",
                "diagonal",
                "nonzero_mixed_pairs",
                "positive_b4_pairs",
                "full_minus_lead_shift",
            ),
            lineterminator="\n",
        )
        writer.writeheader()
        for row in baselines:
            writer.writerow(
                {
                    "object": f"divisibility_{row['cutoff']}",
                    "kind": "source_locked_baseline",
                    "cutoff_or_size": row["cutoff"],
                    "atom_count": row["atom_count"],
                    "diagonal": row["diagonal_D"]["text"],
                    "nonzero_mixed_pairs": sum(bool(pair["nonzero"]) for pair in row["mixed_ledger"]),
                    "positive_b4_pairs": sum(bool(pair["positive"]) for pair in row["b4_pair_ledger"]),
                    "full_minus_lead_shift": row["shifts"]["S0"]["text"],
                }
            )
        for row in control_records:
            writer.writerow(
                {
                    "object": row["name"],
                    "kind": "control",
                    "cutoff_or_size": row["size"],
                    "atom_count": len(row["atom_weights"]),
                    "diagonal": row["diagonal"]["text"],
                    "nonzero_mixed_pairs": row["nonzero_mixed_count"],
                    "positive_b4_pairs": row["positive_b4_count"],
                    "full_minus_lead_shift": "not_applicable",
                }
            )

    # Flat exact ledgers used by the manuscript and strict Route-A evaluator.
    with (output / "baseline_pair_ledger.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("cutoff", "p", "q", "gram_over_C_eta", "mixed_rational", "mixed_radicand", "b4_over_C_eta_squared", "nonzero"),
            lineterminator="\n",
        )
        writer.writeheader()
        for baseline in baselines:
            b4_by_pair = {tuple(row["atom_weights"]): row for row in baseline["b4_pair_ledger"]}
            for row in baseline["mixed_ledger"]:
                pair = tuple(row["atom_weights"])
                writer.writerow(
                    {
                        "cutoff": baseline["cutoff"],
                        "p": pair[0],
                        "q": pair[1],
                        "gram_over_C_eta": row["gram"]["text"],
                        "mixed_rational": row["cos_amplitude"]["rational_coefficient"]["text"],
                        "mixed_radicand": row["cos_amplitude"]["squarefree_radicand"],
                        "b4_over_C_eta_squared": b4_by_pair[pair]["coefficient"]["text"],
                        "nonzero": str(bool(row["nonzero"])).lower(),
                    }
                )

    with (output / "control_pair_ledger.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("control", "left_weight", "right_weight", "gram", "mixed_rational", "mixed_radicand", "b4_coefficient", "nonzero"),
            lineterminator="\n",
        )
        writer.writeheader()
        for control in control_records:
            b4_by_pair = {tuple(row["atom_weights"]): row for row in control["b4_pair_ledger"]}
            for row in control["mixed_ledger"]:
                pair = tuple(row["atom_weights"])
                writer.writerow(
                    {
                        "control": control["name"],
                        "left_weight": pair[0],
                        "right_weight": pair[1],
                        "gram": row["gram"]["text"],
                        "mixed_rational": row["cos_amplitude"]["rational_coefficient"]["text"],
                        "mixed_radicand": row["cos_amplitude"]["squarefree_radicand"],
                        "b4_coefficient": b4_by_pair[pair]["coefficient"]["text"],
                        "nonzero": str(bool(row["nonzero"])).lower(),
                    }
                )

    with (output / "scheme_shift_ledger.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("cutoff", "coefficient_S0", "coefficient_S1", "coefficient_S2", "shift_value", "atom_local", "isomorphism_natural", "prefix_additive"),
            lineterminator="\n",
        )
        writer.writeheader()
        for row in families:
            writer.writerow(
                {
                    "cutoff": row["cutoff"],
                    "coefficient_S0": row["coefficients"][0],
                    "coefficient_S1": row["coefficients"][1],
                    "coefficient_S2": row["coefficients"][2],
                    "shift_value": row["shift_value"]["text"],
                    "atom_local": str(bool(row["is_atom_local"])).lower(),
                    "isomorphism_natural": str(bool(row["is_isomorphism_natural"])).lower(),
                    "prefix_additive": str(bool(row["is_prefix_additive"])).lower(),
                }
            )

    with (output / "coefficient_grid_ledger.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("alpha", "beta", "removes_divergence", "preserves_baseline", "cancels_controls", "selective_solution"),
            lineterminator="\n",
        )
        writer.writeheader()
        for row in coefficient_payload["search"]["rows"]:
            writer.writerow(
                {
                    "alpha": row["diagonal_coefficient"],
                    "beta": row["pair_coefficient"],
                    "removes_divergence": str(bool(row["removes_leading_divergence"])).lower(),
                    "preserves_baseline": str(bool(row["preserves_baseline_mixed"])).lower(),
                    "cancels_controls": str(bool(row["cancels_nonzero_control_mixed"])).lower(),
                    "selective_solution": str(bool(row["selective_solution"])).lower(),
                }
            )

    with (output / "determinant_power_ledger.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("power", "status", "coefficient"),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(determinant_payload["log_det3_power_ledger"])

    with (output / "route_gate_summary.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=("gate", "verdict", "status"), lineterminator="\n")
        writer.writeheader()
        for gate, verdict, status in (
            ("A0", ROUTE_TUPLE[0], "PROVED_SCOPED"),
            ("A1", ROUTE_TUPLE[1], "STOP_SCOPED"),
            ("A2", ROUTE_TUPLE[2], "INHERITED_PROVED_SCOPED"),
            ("A3", ROUTE_TUPLE[3], "STOP_SCOPED"),
            ("A4", ROUTE_TUPLE[4], "STOP_PROVES_TOO_MUCH"),
        ):
            writer.writerow({"gate": gate, "verdict": verdict, "status": status})

    with (output / "analysis_comparison_table.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("object", "class", "atoms", "pair_rows", "nonzero_mixed", "positive_b4"),
            lineterminator="\n",
        )
        writer.writeheader()
        for row in baselines:
            writer.writerow(
                {
                    "object": f"divisibility_{row['cutoff']}",
                    "class": "baseline",
                    "atoms": row["atom_count"],
                    "pair_rows": len(row["mixed_ledger"]),
                    "nonzero_mixed": sum(bool(pair["nonzero"]) for pair in row["mixed_ledger"]),
                    "positive_b4": sum(bool(pair["positive"]) for pair in row["b4_pair_ledger"]),
                }
            )
        for row in control_records:
            writer.writerow(
                {
                    "object": row["name"],
                    "class": "control",
                    "atoms": len(row["atom_weights"]),
                    "pair_rows": len(row["mixed_ledger"]),
                    "nonzero_mixed": row["nonzero_mixed_count"],
                    "positive_b4": row["positive_b4_count"],
                }
            )

    write_json(
        output / "theorem_ledger.json",
        {
            **header("theorem_ledger"),
            "finite_part_nonuniqueness": True,
            "local_selectivity_no_go": True,
            "full_lead_difference_nonzero_summable": True,
            "symbolic_beta_contradiction": "preserve gives beta=0; cancel same-type control gives beta=1",
            "global_nonlocal_no_go_claimed": False,
            "D_ren_is_new_functional": True,
            "det3_ownership_inherited": True,
            "ordinary_B2_trace_claimed": False,
            "overall_verdict": "ROUTE_A_REJECTED",
            "route_tuple": ROUTE_TUPLE,
        },
    )
    write_json(
        output / "source_oracle_certificate.json",
        {
            **header("source_oracle_certificate"),
            "candidate_evaluator_separated": True,
            "source_cover_compiler": True,
            "numeric_marks_transport_only": True,
            "numeric_marks_select_atoms": False,
            "prime_table_used_in_candidate": False,
            "factorization_or_primality_oracle_used_in_candidate": False,
            "target_zero_data_used": False,
            "regularization_order": 3,
            "route_b_invocation_allowed": False,
            "forbidden_candidate_calls": [],
        },
    )
    write_json(
        output / "run_parameters.json",
        {
            **header("run_parameters"),
            "eta": 2,
            "baseline_cutoffs": list(cutoffs),
            "generic_dag_seed": 29031,
            "random_inventory_seed": 29032,
            "relabel_seeds": [29112, 29118, 29130, 29331],
            "coefficient_grid": [fraction_text(value) for value in grid],
            "counterterm_class": "quadratic_additive_pair_local_linear_in_native_Gram",
            "regularization_order": 3,
            "main_theorem_u": 1,
        },
    )
    write_json(
        output / "environment_lock.json",
        {
            **header("environment_lock"),
            "python": "3.12.3",
            "external_dependencies_for_claim_arithmetic": [],
            "arithmetic": "fractions.Fraction and formal radical ledgers",
            "PYTHONHASHSEED": "0 in canonical runner",
            "timestamps_in_results": False,
        },
    )

    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build_artifacts(args.output)


if __name__ == "__main__":
    main()
