#!/usr/bin/env python3
"""Generate deterministic exact artifacts for SD-C32."""

from __future__ import annotations

import argparse
import csv
from fractions import Fraction
import json
from pathlib import Path

from coherence_core import (
    PREDICATES,
    canonical_statistic,
    divisibility_inventory,
    exact_projector_checks,
    finite_poset_record,
    formal_divisibility_record,
    formal_free_record,
    fraction_record,
    free_control_rows,
    generic_dag_poset,
    mutated_cover_poset,
    permute_poset,
    predicate_mask_rows,
    random_inventory_poset,
    random_permutation,
    tail_certificates,
)


CANDIDATE = "SD-C32"
SCHEMA = "SD-C32-exact-v1"
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
        "schema_version": SCHEMA,
        "candidate_id": CANDIDATE,
        "artifact_kind": kind,
        "target_zero_data_used": False,
        "route_b_invocation_allowed": False,
    }


def fraction_from(record: dict[str, object]) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def restrict_canonical(
    record: dict[str, object], allowed_weights: set[int]
) -> dict[str, object]:
    return {
        "atom_weights": sorted(allowed_weights),
        "pairs": [
            row
            for row in record["pairs"]
            if set(int(value) for value in row["atom_weights"]).issubset(allowed_weights)
        ],
        "triples": [
            row
            for row in record["triples"]
            if set(int(value) for value in row["atom_weights"]).issubset(allowed_weights)
        ],
    }


def canonical_prefix_equal(
    small: dict[str, object], large: dict[str, object]
) -> bool:
    allowed = set(int(value) for value in small["atom_weights"])
    restricted = restrict_canonical(large, allowed)
    return (
        restricted["atom_weights"] == small["atom_weights"]
        and restricted["pairs"] == small["pairs"]
        and restricted["triples"] == small["triples"]
    )


def write_csv(path: Path, fieldnames: tuple[str, ...], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build(output: Path) -> dict[str, object]:
    output.mkdir(parents=True, exist_ok=True)
    cutoffs = (12, 18, 30)
    baselines = [formal_divisibility_record(cutoff) for cutoff in cutoffs]
    baseline_canonical = [canonical_statistic(record) for record in baselines]
    relabels = [
        formal_free_record(
            record["atom_weights"],
            f"integer_divisibility_relabel_{cutoff}",
            alias="free_commutative",
            relabel_seed=30000 + cutoff,
        )
        for cutoff, record in zip(cutoffs, baselines)
    ]
    relabel_equal = [
        canonical_statistic(record) == canonical_statistic(relabel)
        for record, relabel in zip(baselines, relabels)
    ]
    prefix_rows = [
        {
            "small_cutoff": cutoffs[index],
            "large_cutoff": cutoffs[index + 1],
            "canonical_prefix_equal": canonical_prefix_equal(
                baseline_canonical[index], baseline_canonical[index + 1]
            ),
        }
        for index in range(len(cutoffs) - 1)
    ]
    baseline_payload = {
        **header("integer_divisibility_baseline"),
        "eta": 2,
        "normalization": "C_eta factored out; triangle coefficients factor C_eta^3",
        "records": baselines,
        "canonical_records": baseline_canonical,
        "relabel_canonical_equal": relabel_equal,
        "active_cutoff_prefix_checks": prefix_rows,
        "all_pairs_full": all(
            row["qualified_pairs"] == len(row["pair_rows"]) for row in baselines
        ),
        "all_triples_full": all(
            row["qualified_triples"] == len(row["triple_rows"]) for row in baselines
        ),
        "all_statistics_nonzero": all(
            row["C2_nonzero"]
            and row["theta3_nonzero"]
            and fraction_from(row["auxiliary_det_e2"]) != 0
            and row["auxiliary_e3_nonzero"]
            for row in baselines
        ),
        "all_relabels_equal": all(relabel_equal),
        "all_prefix_checks_pass": all(row["canonical_prefix_equal"] for row in prefix_rows),
    }
    write_json(output / "baseline.json", baseline_payload)

    controls_posets = (
        mutated_cover_poset(18),
        divisibility_inventory((1, 4, 6, 9, 12, 18, 36), "composite_only"),
        generic_dag_poset(29031),
        random_inventory_poset(29032),
    )
    sanity_rows = [exact_projector_checks(poset) for poset in controls_posets]
    control_records = [finite_poset_record(poset) for poset in controls_posets]
    generic = controls_posets[2]
    generic_order = random_permutation(generic.size, 30331)
    generic_copy = permute_poset(generic, generic_order, "generic_DAG_relabel")
    generic_copy_record = finite_poset_record(generic_copy)
    generic_relabel_equal = (
        canonical_statistic(control_records[2])
        == canonical_statistic(generic_copy_record)
    )
    full_pair_survivors = {
        record["source"]: [
            row["atom_weights"] for row in record["pair_rows"] if row["filtered"]
        ]
        for record in control_records
    }
    full_triple_survivors = {
        record["source"]: [
            row["atom_weights"]
            for row in record["triple_rows"]
            if row["coherence"]["full"]
        ]
        for record in control_records
    }
    finite_payload = {
        **header("finite_non_UFD_controls"),
        "records": control_records,
        "compiler_sanity": sanity_rows,
        "generic_relabel_canonical_equal": generic_relabel_equal,
        "full_pair_survivors": full_pair_survivors,
        "full_triple_survivors": full_triple_survivors,
        "all_compilers_pass": all(row["all_pass"] for row in sanity_rows),
        "all_four_pair_zero": all(record["qualified_pairs"] == 0 for record in control_records),
        "all_four_triple_zero": all(record["qualified_triples"] == 0 for record in control_records),
        "minimal_pair_counterexample": {
            "source": "mutated_cover_promote_6",
            "surviving_pairs": full_pair_survivors["mutated_cover_promote_6"],
            "reason": "their generated Boolean intervals are disjoint from the promoted-six defect",
            "smallest_survivor": full_pair_survivors["mutated_cover_promote_6"][0],
        },
    }
    write_json(output / "finite_controls.json", finite_payload)

    baseline_weights = tuple(int(value) for value in baselines[-1]["atom_weights"])
    clones = [
        formal_free_record(
            record["atom_weights"],
            f"transported_free_commutative_clone_{cutoff}",
            alias="free_commutative",
        )
        for cutoff, record in zip(cutoffs, baselines)
    ]
    polynomial_clones = [
        formal_free_record(
            record["atom_weights"],
            f"polynomial_UFD_clone_{cutoff}",
            alias="polynomial_UFD_monomials",
            relabel_seed=31000 + cutoff,
        )
        for cutoff, record in zip(cutoffs, baselines)
    ]
    clone_equal = [
        canonical_statistic(base) == canonical_statistic(clone)
        for base, clone in zip(baselines, clones)
    ]
    polynomial_equal = [
        canonical_statistic(base) == canonical_statistic(clone)
        for base, clone in zip(baselines, polynomial_clones)
    ]
    generic_weights = (10, 14, 21, 25, 33, 38)
    free_rows = free_control_rows(baseline_weights, generic_weights)
    free_payload = {
        **header("free_commutative_and_UFD_controls"),
        "rows": free_rows,
        "row_count": len(free_rows),
        "all_pairs_fully_coherent": all(row["all_pairs_fully_coherent"] for row in free_rows),
        "all_triples_fully_coherent": all(row["all_triples_fully_coherent"] for row in free_rows),
        "all_caps_locally_compatible": all(row["cap_independent_local_intervals"] for row in free_rows),
        "aliases": sorted(set(row["alias"] for row in free_rows)),
    }
    write_json(output / "free_monoid_controls.json", free_payload)

    clone_payload = {
        **header("free_commutative_clone_theorem"),
        "baseline_canonical": baseline_canonical,
        "clone_canonical": [canonical_statistic(record) for record in clones],
        "polynomial_UFD_canonical": [
            canonical_statistic(record) for record in polynomial_clones
        ],
        "baseline_clone_equal_by_cutoff": clone_equal,
        "baseline_polynomial_UFD_equal_by_cutoff": polynomial_equal,
        "all_clone_ledgers_equal": all(clone_equal) and all(polynomial_equal),
        "minimal_pair_clone": {
            "integer_atoms": [2, 3],
            "formal_atoms": ["x_2", "x_3"],
            "join_correspondence": "6 <-> x_2*x_3",
            "interval": "B2",
            "mobius": 1,
            "roof": 6,
        },
        "minimal_triple_clone": {
            "integer_atoms": [2, 3, 5],
            "formal_atoms": ["x_2", "x_3", "x_5"],
            "join_correspondence": "30 <-> x_2*x_3*x_5",
            "interval": "B3",
            "mobius": -1,
            "roof": 30,
        },
        "theorem_certificate": {
            "statement": "N_{>0} under multiplication is the free commutative monoid on its source covers; a UFD factorization monoid modulo units is free commutative on irreducibles",
            "isomorphism": "n maps to its finite exponent vector; divisibility maps to coordinatewise order",
            "preserved_data": [
                "bottom covers",
                "finite joins/lcm",
                "Boolean generated intervals",
                "Mobius values",
                "compatible exponent-box cutoffs",
                "transported roof character",
                "transported Gram kernel",
                "markers",
            ],
            "consequence": "every natural invariant of the frozen data has identical baseline and transported-clone values",
            "status": "PROVES_TOO_MUCH",
        },
    }
    write_json(output / "clone_certificate.json", clone_payload)

    mask_records = [baselines[-1], *control_records, clones[-1]]
    masks = predicate_mask_rows(mask_records)
    pair_separating_masks = [
        mask
        for mask in range(1, 32)
        if next(
            row["qualified_pairs"]
            for row in masks
            if row["mask"] == mask and row["source"] == baselines[-1]["source"]
        )
        > 0
        and all(
            next(
                row["qualified_pairs"]
                for row in masks
                if row["mask"] == mask and row["source"] == control["source"]
            )
            == 0
            for control in control_records
        )
    ]
    triple_separating_masks = [
        mask
        for mask in range(1, 32)
        if next(
            row["qualified_triples"]
            for row in masks
            if row["mask"] == mask and row["source"] == baselines[-1]["source"]
        )
        > 0
        and all(
            next(
                row["qualified_triples"]
                for row in masks
                if row["mask"] == mask and row["source"] == control["source"]
            )
            == 0
            for control in control_records
        )
    ]
    mask_payload = {
        **header("predicate_mask_enumeration"),
        "predicate_order": list(PREDICATES),
        "frozen_full_mask": 31,
        "rows": masks,
        "row_count": len(masks),
        "pair_separating_masks_for_four_finite_controls": pair_separating_masks,
        "triple_separating_masks_for_four_finite_controls": triple_separating_masks,
        "pair_separator_exists": bool(pair_separating_masks),
        "triple_separator_exists": bool(triple_separating_masks),
        "every_mask_copied_by_transported_clone": all(
            next(
                row
                for row in masks
                if row["mask"] == mask and row["source"] == baselines[-1]["source"]
            )["qualified_pairs"]
            == next(
                row
                for row in masks
                if row["mask"] == mask and row["source"] == clones[-1]["source"]
            )["qualified_pairs"]
            and next(
                row
                for row in masks
                if row["mask"] == mask and row["source"] == baselines[-1]["source"]
            )["qualified_triples"]
            == next(
                row
                for row in masks
                if row["mask"] == mask and row["source"] == clones[-1]["source"]
            )["qualified_triples"]
            for mask in range(1, 32)
        ),
    }
    write_json(output / "predicate_masks.json", mask_payload)

    marker_rows = []
    for row in baselines[-1]["pair_rows"]:
        marker_rows.append(
            {
                "kind": "pair",
                "atom_weights": row["atom_weights"],
                "marker_exponent": row["marker_exponent"],
                "formula": "ell(a)+ell(b)",
                "theorem_u": 1,
            }
        )
    for row in baselines[-1]["triple_rows"]:
        marker_rows.append(
            {
                "kind": "connected_triangle",
                "atom_weights": row["atom_weights"],
                "marker_exponent": row["marker_exponent"],
                "formula": "2*(ell(a)+ell(b)+ell(c))",
                "theorem_u": 1,
            }
        )
    analytic_payload = {
        **header("analytic_marker_and_ownership"),
        "eta": 2,
        "C2_holomorphic_strip": "-3 < Re(s) < 4",
        "C2_reflection": "C2(1-s)=C2(s)",
        "contains_inherited_det3_strip": True,
        "tail_certificates": [tail_certificates(cutoff) for cutoff in cutoffs],
        "auxiliary_H": {
            "definition": "zero-diagonal Boolean-pair-filtered normalized Gram matrix",
            "absolute_entry_sum_finite": True,
            "trace_class": True,
            "ordinary_Fredholm_determinant": "det(I+zH) exists and is entire in z",
            "e2": baselines[-1]["auxiliary_det_e2"],
            "e3": baselines[-1]["auxiliary_det_e3"],
            "phase_dependence": False,
            "ownership": "auxiliary atom-Gram determinant, not the original chiral transfer determinant",
        },
        "connected_theta3": {
            "value": baselines[-1]["theta3"],
            "entire_in_s": True,
            "ownership": "source-filtered connected coefficient; not the full Tr(B^6) or a chiral determinant coefficient",
        },
        "chiral_det3": {
            "status": "inherited honest determinant",
            "quadratic_term": "deleted in full",
            "ownership_changed_by_filter": False,
        },
        "new_functional_firewall": "exponentiating C2 or Theta3 creates a declared new functional",
        "marker_rows": marker_rows,
        "marker_row_count": len(marker_rows),
        "all_marker_exponents_positive": all(row["marker_exponent"] > 0 for row in marker_rows),
        "main_theorem_u": 1,
    }
    write_json(output / "analytic_ownership.json", analytic_payload)

    sanity_payload = {
        **header("sanity"),
        "compiler_rows": sanity_rows,
        "all_compilers_pass": all(row["all_pass"] for row in sanity_rows),
        "boolean_pair_sanity": baselines[0]["pair_rows"][0]["coherence"],
        "boolean_triple_sanity": baselines[0]["triple_rows"][0]["coherence"],
        "all_pass": all(row["all_pass"] for row in sanity_rows)
        and baselines[0]["pair_rows"][0]["coherence"]["full"]
        and baselines[0]["triple_rows"][0]["coherence"]["full"],
    }
    write_json(output / "sanity.json", sanity_payload)

    summary = {
        **header("summary"),
        "candidate_title": "Boolean-Join Coherence Filters and the Free-Commutative Clone Obstruction",
        "strongest_go": "GO_BOOLEAN_TRIPLE_FINITE_FIXTURE_SEPARATOR_AND_AUXILIARY_TRACE_CLASS_DETERMINANT",
        "strongest_stop": "STOP_SOURCE_SPECIFICITY_BY_FREE_COMMUTATIVE_UFD_CLONE",
        "finite_pair_separator": False,
        "finite_triple_separator": finite_payload["all_four_triple_zero"]
        and baseline_payload["all_triples_full"],
        "all_UFD_controls_zero": False,
        "clone_proves_too_much": clone_payload["all_clone_ledgers_equal"],
        "claims": {
            "C1_as_preregistered_full_pair_and_triple_separator": False,
            "C1_triple_substatistic_finite_fixture_separator": finite_payload["all_four_triple_zero"],
            "C2_free_commutative_clone_obstruction": clone_payload["all_clone_ledgers_equal"],
            "analytic_ownership_firewalls": True,
        },
        "minimal_counterexample": finite_payload["minimal_pair_counterexample"],
        "route_tuple": ROUTE_TUPLE,
        "overall_status": "REJECTED_AS_RH_COMPLETION",
        "route_b": False,
        "paper31_minimum_obligation": "Introduce a canonically source-derived operation absent from the free-commutative/UFD clone, most plausibly additive or archimedean-multiplicative coupling; prove exact clone separation before any determinant or RH claim.",
    }
    write_json(output / "summary.json", summary)

    baseline_rows = []
    for cutoff, record in zip(cutoffs, baselines):
        for row in record["pair_rows"]:
            baseline_rows.append(
                {
                    "cutoff": cutoff,
                    "kind": "pair",
                    "atom_weights": "*".join(str(value) for value in row["atom_weights"]),
                    "full": str(bool(row["coherence"]["full"])).lower(),
                    "coefficient": row["H_squared"]["text"],
                    **{
                        predicate: str(bool(row["coherence"]["predicates"][predicate])).lower()
                        for predicate in PREDICATES
                    },
                }
            )
        for row in record["triple_rows"]:
            baseline_rows.append(
                {
                    "cutoff": cutoff,
                    "kind": "triple",
                    "atom_weights": "*".join(str(value) for value in row["atom_weights"]),
                    "full": str(bool(row["coherence"]["full"])).lower(),
                    "coefficient": row["connected_coefficient"]["text"],
                    **{
                        predicate: str(bool(row["coherence"]["predicates"][predicate])).lower()
                        for predicate in PREDICATES
                    },
                }
            )
    write_csv(
        output / "baseline_subset_ledger.csv",
        ("cutoff", "kind", "atom_weights", *PREDICATES, "full", "coefficient"),
        baseline_rows,
    )

    control_rows = []
    for record in control_records:
        for row in record["pair_rows"]:
            control_rows.append(
                {
                    "source": record["source"],
                    "kind": "pair",
                    "atom_weights": "*".join(str(value) for value in row["atom_weights"]),
                    "full": str(bool(row["coherence"]["full"])).lower(),
                    "coefficient": row["H_squared"]["text"],
                    **{
                        predicate: str(bool(row["coherence"]["predicates"][predicate])).lower()
                        for predicate in PREDICATES
                    },
                }
            )
        for row in record["triple_rows"]:
            control_rows.append(
                {
                    "source": record["source"],
                    "kind": "triple",
                    "atom_weights": "*".join(str(value) for value in row["atom_weights"]),
                    "full": str(bool(row["coherence"]["full"])).lower(),
                    "coefficient": row["connected_coefficient"]["text"],
                    **{
                        predicate: str(bool(row["coherence"]["predicates"][predicate])).lower()
                        for predicate in PREDICATES
                    },
                }
            )
    write_csv(
        output / "finite_control_subset_ledger.csv",
        ("source", "kind", "atom_weights", *PREDICATES, "full", "coefficient"),
        control_rows,
    )
    write_csv(
        output / "free_monoid_control_ledger.csv",
        (
            "name",
            "alias",
            "rank",
            "exponent_cap",
            "element_count",
            "generator_weights",
            "pair_count",
            "triple_count",
            "all_pairs_fully_coherent",
            "all_triples_fully_coherent",
            "cap_independent_local_intervals",
        ),
        [
            {
                **row,
                "generator_weights": "*".join(str(value) for value in row["generator_weights"]),
                "all_pairs_fully_coherent": str(bool(row["all_pairs_fully_coherent"])).lower(),
                "all_triples_fully_coherent": str(bool(row["all_triples_fully_coherent"])).lower(),
                "cap_independent_local_intervals": str(bool(row["cap_independent_local_intervals"])).lower(),
            }
            for row in free_rows
        ],
    )
    write_csv(
        output / "predicate_mask_ledger.csv",
        (
            "mask",
            "predicates",
            "source",
            "qualified_pairs",
            "qualified_triples",
            "is_frozen_full_selector",
        ),
        [
            {
                **row,
                "predicates": "+".join(row["predicates"]),
                "is_frozen_full_selector": str(bool(row["is_frozen_full_selector"])).lower(),
            }
            for row in masks
        ],
    )
    write_csv(
        output / "marker_ownership_ledger.csv",
        ("kind", "atom_weights", "marker_exponent", "formula", "theorem_u"),
        [
            {
                **row,
                "atom_weights": "*".join(str(value) for value in row["atom_weights"]),
            }
            for row in marker_rows
        ],
    )
    comparison_rows = []
    for cutoff, record in zip(cutoffs, baselines):
        comparison_rows.append(
            {
                "source": f"baseline_{cutoff}",
                "class": "integer_divisibility",
                "atoms": record["atom_count"],
                "qualified_pairs": record["qualified_pairs"],
                "qualified_triples": record["qualified_triples"],
                "C2_nonzero": str(bool(record["C2_nonzero"])).lower(),
                "theta3_nonzero": str(bool(record["theta3_nonzero"])).lower(),
            }
        )
    for record in control_records:
        comparison_rows.append(
            {
                "source": record["source"],
                "class": "finite_control",
                "atoms": record["atom_count"],
                "qualified_pairs": record["qualified_pairs"],
                "qualified_triples": record["qualified_triples"],
                "C2_nonzero": str(bool(record["C2_nonzero"])).lower(),
                "theta3_nonzero": str(bool(record["theta3_nonzero"])).lower(),
            }
        )
    comparison_rows.append(
        {
            "source": clones[-1]["source"],
            "class": "transported_free_clone",
            "atoms": clones[-1]["atom_count"],
            "qualified_pairs": clones[-1]["qualified_pairs"],
            "qualified_triples": clones[-1]["qualified_triples"],
            "C2_nonzero": str(bool(clones[-1]["C2_nonzero"])).lower(),
            "theta3_nonzero": str(bool(clones[-1]["theta3_nonzero"])).lower(),
        }
    )
    write_csv(
        output / "comparison_table.csv",
        (
            "source",
            "class",
            "atoms",
            "qualified_pairs",
            "qualified_triples",
            "C2_nonzero",
            "theta3_nonzero",
        ),
        comparison_rows,
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build(args.output)


if __name__ == "__main__":
    main()
