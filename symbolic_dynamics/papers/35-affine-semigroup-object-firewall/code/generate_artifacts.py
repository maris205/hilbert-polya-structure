#!/usr/bin/env python3
"""Generate frozen neutral authority source artifacts for SD-C37."""

from __future__ import annotations

import argparse
import csv
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

import source_core as core


SOURCE_FILES = (
    "admissible_word_census.csv",
    "backtrack_ledger.csv",
    "bc_diagonal_fixtures.json",
    "commutation_witnesses.json",
    "full_monoid_boundary.json",
    "height_dag_ledger.csv",
    "monoid_relation_controls.json",
    "operator_certificates.json",
    "quotient_ledger.csv",
    "relation_witnesses.json",
    "source_parameters.json",
)


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError("CSV rows may not be empty")
    fields = list(rows[0])
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def file_hash(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()
    output = Path(arguments.output)
    output.mkdir(parents=True, exist_ok=True)

    parameters = {
        "schema_version": "SD-C37-source-parameters-v1",
        "baseline_r": 4,
        "r_values": [4, 2, 3, 5],
        "height_b_max": 12,
        "height_k_max": 4,
        "word_bases": [[0, 0], [2, 1]],
        "word_max_length": 8,
        "operator_sequence_count": 12,
        "edge_weight_a": "1/1",
        "edge_weight_b": "1/1",
        "height_definition": "h_r(b,k)=b+r^k",
        "operator_definition": "A_plus=S+T on ell2(P_r)",
        "quotient_moduli": list(range(1, 13)),
        "diagonal_betas": [2, 3],
        "diagonal_cutoff": 12,
        "diagonal_log_power_count": 4,
        "commutation_pairs": [[2, 3], [3, 5], [4, 6], [4, 9]],
        "monoid_relations": [
            ["affine_composite", 1, 4],
            ["mutated_2_5", 2, 5],
            ["mutated_3_7", 3, 7],
            ["mutated_2_8", 2, 8],
        ],
        "external_dependencies": [],
        "network_used": False,
        "gpu_used": False,
        "result_timestamps": False,
    }
    write_json(output / "source_parameters.json", parameters)

    height_rows: list[dict[str, object]] = []
    for r in parameters["r_values"]:
        height_rows.extend(core.positive_edges(r, parameters["height_b_max"], parameters["height_k_max"]))
    write_csv(output / "height_dag_ledger.csv", height_rows)
    write_csv(output / "backtrack_ledger.csv", core.backtrack_rows(height_rows))

    census_rows: list[dict[str, object]] = []
    witnesses: list[dict[str, object]] = []
    a = Fraction(1, 1)
    b = Fraction(1, 1)
    for r in parameters["r_values"]:
        for base_values in parameters["word_bases"]:
            base = (base_values[0], base_values[1])
            census_rows.extend(core.word_census(r, base, parameters["word_max_length"]))
            witnesses.append(core.relation_witness(r, base, a, b))
    write_csv(output / "admissible_word_census.csv", census_rows)
    write_json(
        output / "relation_witnesses.json",
        {"schema_version": "SD-C37-relation-witnesses-v1", "witnesses": witnesses},
    )

    commutations = [core.commutation_record(left, right) for left, right in parameters["commutation_pairs"]]
    write_json(
        output / "commutation_witnesses.json",
        {"schema_version": "SD-C37-commutation-v1", "witnesses": commutations},
    )

    write_json(
        output / "operator_certificates.json",
        {
            "schema_version": "SD-C37-operator-certificates-v1",
            "certificates": [
                core.operator_certificates(r, parameters["operator_sequence_count"], a, b)
                for r in parameters["r_values"]
            ],
        },
    )

    quotient_rows = [
        core.quotient_record(r, q)
        for r in parameters["r_values"]
        for q in parameters["quotient_moduli"]
    ]
    write_csv(output / "quotient_ledger.csv", quotient_rows)

    relations = [
        core.monoid_relation_record(name, left_count, right_count)
        for name, left_count, right_count in parameters["monoid_relations"]
    ]
    write_json(
        output / "monoid_relation_controls.json",
        {"schema_version": "SD-C37-monoid-relations-v1", "controls": relations},
    )

    fixtures = [
        core.bc_fixture(beta, parameters["diagonal_cutoff"], parameters["diagonal_log_power_count"])
        for beta in parameters["diagonal_betas"]
    ]
    write_json(
        output / "bc_diagonal_fixtures.json",
        {"schema_version": "SD-C37-bc-diagonal-v1", "fixtures": fixtures},
    )
    write_json(output / "full_monoid_boundary.json", core.full_monoid_boundary())

    missing = [name for name in SOURCE_FILES if not (output / name).is_file()]
    if missing:
        raise RuntimeError(f"missing source artifacts: {missing}")
    hashes = {name: file_hash(output / name) for name in SOURCE_FILES}
    write_json(
        output / "source_manifest.json",
        {
            "schema_version": "SD-C37-source-manifest-v1",
            "source_frozen_before_evaluator": True,
            "artifact_count": len(SOURCE_FILES),
            "artifacts": list(SOURCE_FILES),
            "sha256": hashes,
            "aggregate_sha256": sha256(
                "".join(f"{hashes[name]}  {name}\n" for name in SOURCE_FILES).encode("utf-8")
            ).hexdigest(),
        },
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
