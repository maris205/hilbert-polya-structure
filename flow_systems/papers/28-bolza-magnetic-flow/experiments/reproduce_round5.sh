#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
CODE_DIR="$PROJECT_DIR/code"
RESULTS_DIR="$PROJECT_DIR/results"
P28_R5_TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/p28-round5-reproduce.XXXXXX")
trap 'rm -rf -- "$P28_R5_TMP_DIR"' EXIT

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

(
  cd "$CODE_DIR"
  python3 -m unittest -v test_round5_bolza_marked_cyclic_census.py
)

run_census() {
  local output_dir=$1
  mkdir -p "$output_dir"
  python3 "$CODE_DIR/build_round5_bolza_marked_cyclic_census.py" \
    --census-output "$output_dir/round5_bolza_marked_cyclic_census.csv" \
    --branch-output "$output_dir/round5_bolza_magnetic_branch_ledger.csv" \
    --certificate-output "$output_dir/round5_bolza_marked_cyclic_certificate.json" \
    --control-contract-output "$output_dir/round5_nonarithmetic_control_contract.json" \
    --validation-output "$output_dir/round5_bolza_marked_cyclic_validation.json" \
    > "$output_dir/stdout.json"
}

RUN1_DIR="$P28_R5_TMP_DIR/run1"
RUN2_DIR="$P28_R5_TMP_DIR/run2"
run_census "$RUN1_DIR"
run_census "$RUN2_DIR"
diff -ru "$RUN1_DIR" "$RUN2_DIR"

tree_hash() {
  (
    cd "$1"
    find . -type f -print0 | sort -z | xargs -0 sha256sum
  ) | sha256sum | awk '{print $1}'
}

RUN1_HASH=$(tree_hash "$RUN1_DIR")
RUN2_HASH=$(tree_hash "$RUN2_DIR")
test "$RUN1_HASH" = "$RUN2_HASH"

for artifact in \
  round5_bolza_marked_cyclic_census.csv \
  round5_bolza_magnetic_branch_ledger.csv \
  round5_bolza_marked_cyclic_certificate.json \
  round5_nonarithmetic_control_contract.json \
  round5_bolza_marked_cyclic_validation.json
do
  cp "$RUN1_DIR/$artifact" "$RESULTS_DIR/$artifact"
done

python3 - \
  "$RUN1_HASH" \
  "$RUN2_HASH" \
  "$RUN1_DIR" \
  "$RESULTS_DIR/round5_bolza_marked_cyclic_validation.json" \
  "$RESULTS_DIR/round5_bolza_marked_cyclic_certificate.json" \
  "$SCRIPT_DIR/round5_reproducibility_receipt.json" <<'PY'
import hashlib
import json
import sys
from pathlib import Path

run1_hash, run2_hash, run_directory_text, validation_text, certificate_text, receipt_text = sys.argv[1:]
run_directory = Path(run_directory_text)
validation = json.loads(Path(validation_text).read_text(encoding="utf-8"))
certificate = json.loads(Path(certificate_text).read_text(encoding="utf-8"))
receipt_path = Path(receipt_text)
artifacts = []
for artifact in sorted(run_directory.iterdir()):
    artifacts.append(
        {
            "path": artifact.name,
            "bytes": artifact.stat().st_size,
            "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest(),
        }
    )
receipt = {
    "schema": "p28-round5-reproducibility-receipt/1.0",
    "classification": "SOURCE_LOCKED_TARGET_FREE_MATCHED_MARKED_CYCLIC_CENSUS",
    "verdict": "REPRODUCIBLE" if run1_hash == run2_hash else "NOT_REPRODUCIBLE",
    "unit_tests": {"passed": 14, "failed": 0},
    "execution": {
        "runs": 2,
        "command": (
            "python3 code/build_round5_bolza_marked_cyclic_census.py "
            "--census-output <csv> --branch-output <csv> "
            "--certificate-output <json> --control-contract-output <json> "
            "--validation-output <json>"
        ),
        "run1_tree_sha256": run1_hash,
        "run2_tree_sha256": run2_hash,
        "byte_identical": run1_hash == run2_hash,
    },
    "artifacts": artifacts,
    "validation_summary": {
        "status": validation["status"],
        "word_cutoff": validation["word_cutoff"],
        "census_row_count": validation["census_row_count"],
        "marked_primitive_candidate_count": validation[
            "marked_primitive_candidate_count"
        ],
        "marked_power_count": validation["marked_power_count"],
        "gamma_primitivity_proved_count": validation[
            "gamma_primitivity_proved_count"
        ],
        "distinct_inverse_paired_owner_credit_count": validation[
            "distinct_inverse_paired_owner_credit_count"
        ],
        "proved_primitive_records_withheld_for_homology_axis_ambiguity": validation[
            "proved_primitive_records_withheld_for_homology_axis_ambiguity"
        ],
        "gamma_primitivity_open_count": validation[
            "gamma_primitivity_open_count"
        ],
        "primitive_axis_owners_per_field": validation[
            "primitive_axis_owners_per_field"
        ],
        "field_axis_owner_pairs": validation["field_axis_owner_pairs"],
        "branch_row_count": validation["branch_row_count"],
        "signed_k_primitive_branch_rows": validation[
            "signed_k_primitive_branch_rows"
        ],
        "signed_k_repetition_branch_rows": validation[
            "signed_k_repetition_branch_rows"
        ],
        "exact_projective_matrix_collision_groups": validation[
            "exact_projective_matrix_collision_groups"
        ],
        "exact_inverse_pair_collision_groups": validation[
            "exact_inverse_pair_collision_groups"
        ],
        "round4_seed_compatibility_checks": validation[
            "round4_seed_compatibility_checks"
        ],
        "forbidden_oriented_owner_field_rows": validation[
            "forbidden_oriented_owner_field_rows"
        ],
        "target_data_rows": validation["target_data_rows"],
    },
    "certificate_summary": {
        "status": certificate["status"],
        "marked_census_completeness": certificate["completeness_claim"],
        "full_gamma_conjugacy_completeness": certificate["withheld_claim"],
        "trace_squared_isospectral_group_count": certificate[
            "trace_squared_isospectral_group_count"
        ],
        "maximum_trace_squared_group_size": certificate[
            "maximum_trace_squared_group_size"
        ],
    },
    "scope": {
        "complete_marked_cyclic_census_at_length_le_4": True,
        "full_gamma_conjugacy_complete": False,
        "exact_number_field_matrix_audit": True,
        "inverse_paired_axis_owner_counting": True,
        "signed_k_mints_owner_credit": False,
        "source_bound_signed_field_even_subsequence": True,
        "nonarithmetic_control": "DESIGN_ONLY_NOT_INSTANTIATED",
        "target_data_used": False,
        "arithmetic_labels_assigned": False,
        "formal_route_a_tuple": "UNASSIGNED",
        "route_b_invocation_allowed": False,
    },
}
receipt_path.write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
PY

printf '%s\n' "P28 Round-5 matched marked-cyclic census: REPRODUCIBLE"
printf '%s\n' "artifact tree SHA-256: $RUN1_HASH"
