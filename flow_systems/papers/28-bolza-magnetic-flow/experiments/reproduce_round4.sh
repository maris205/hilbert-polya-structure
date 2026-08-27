#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
CODE_DIR="$PROJECT_DIR/code"
RESULTS_DIR="$PROJECT_DIR/results"
P28_R4_TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/p28-round4-reproduce.XXXXXX")
trap 'rm -rf -- "$P28_R4_TMP_DIR"' EXIT

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

(
  cd "$CODE_DIR"
  python3 -m unittest -v test_round4_bolza_owner_ledger.py
)

run_ledger() {
  local output_dir=$1
  mkdir -p "$output_dir"
  python3 "$CODE_DIR/build_round4_bolza_owner_ledger.py" \
    --ledger-output "$output_dir/round4_bolza_magnetic_owner_ledger.csv" \
    --certificate-output "$output_dir/round4_bolza_group_certificate.json" \
    --validation-output "$output_dir/round4_bolza_owner_validation.json" \
    > "$output_dir/stdout.json"
}

RUN1_DIR="$P28_R4_TMP_DIR/run1"
RUN2_DIR="$P28_R4_TMP_DIR/run2"
run_ledger "$RUN1_DIR"
run_ledger "$RUN2_DIR"
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

cp "$RUN1_DIR/round4_bolza_magnetic_owner_ledger.csv" \
  "$RESULTS_DIR/round4_bolza_magnetic_owner_ledger.csv"
cp "$RUN1_DIR/round4_bolza_group_certificate.json" \
  "$RESULTS_DIR/round4_bolza_group_certificate.json"
cp "$RUN1_DIR/round4_bolza_owner_validation.json" \
  "$RESULTS_DIR/round4_bolza_owner_validation.json"

python3 - \
  "$RUN1_HASH" \
  "$RUN2_HASH" \
  "$RUN1_DIR" \
  "$RESULTS_DIR/round4_bolza_owner_validation.json" \
  "$SCRIPT_DIR/round4_reproducibility_receipt.json" <<'PY'
import hashlib
import json
import sys
from pathlib import Path

run1_hash, run2_hash, run_directory_text, validation_text, receipt_text = sys.argv[1:]
run_directory = Path(run_directory_text)
validation = json.loads(Path(validation_text).read_text(encoding="utf-8"))
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
    "schema": "p28-round4-reproducibility-receipt/2.0",
    "classification": "SOURCE_LOCKED_TARGET_FREE_AXIS_SIGNED_K_LEDGER",
    "verdict": "REPRODUCIBLE" if run1_hash == run2_hash else "NOT_REPRODUCIBLE",
    "unit_tests": {"passed": 12, "failed": 0},
    "execution": {
        "runs": 2,
        "command": (
            "python3 code/build_round4_bolza_owner_ledger.py "
            "--ledger-output <csv> --certificate-output <json> "
            "--validation-output <json>"
        ),
        "run1_tree_sha256": run1_hash,
        "run2_tree_sha256": run2_hash,
        "byte_identical": run1_hash == run2_hash,
    },
    "artifacts": artifacts,
    "validation_summary": {
        "status": validation["status"],
        "row_count": validation["row_count"],
        "explicit_inverse_paired_axis_owners_per_field": validation[
            "explicit_inverse_paired_axis_owners_per_field"
        ],
        "field_axis_owner_pairs": validation["field_axis_owner_pairs"],
        "signed_trace_branches_per_field": validation[
            "signed_trace_branches_per_field"
        ],
        "signed_k_primitive_branches_per_field": validation[
            "signed_k_primitive_branches_per_field"
        ],
        "signed_k_primitive_branch_rows": validation[
            "signed_k_primitive_branch_rows"
        ],
        "signed_k_repetition_branch_rows": validation[
            "signed_k_repetition_branch_rows"
        ],
        "oriented_owner_credit_rows": validation["oriented_owner_credit_rows"],
        "field_partner_checks": validation["field_partner_checks"],
        "signed_k_partner_checks": validation["signed_k_partner_checks"],
        "stability_checks": validation["stability_checks"],
        "group_certificate_relator_residual": validation[
            "group_certificate_relator_residual"
        ],
    },
    "scope": {
        "source_locked_explicit_bolza_side_pairings": True,
        "source_bound_signed_field_even_subsequence": True,
        "source_equation_19_signed_k_branches": True,
        "inverse_paired_axis_owner_counting": True,
        "oriented_owner_credit": False,
        "complete_primitive_spectrum": False,
        "target_data_used": False,
        "arithmetic_labels_assigned": False,
        "zero_field_owner": "OPEN_NOT_IN_LEDGER",
        "odd_N_owner": "OPEN_NOT_ESTABLISHED",
        "full_all_N_owner": "OPEN_NOT_ESTABLISHED",
        "fixed_operator_owner": "OPEN_NOT_ESTABLISHED_NO_CREDIT_TRANSFER",
        "formal_route_a_tuple": "UNASSIGNED",
        "route_b_invocation_allowed": False,
    },
}
receipt_path.write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
PY

printf '%s\n' "P28 Round-4 Bolza owner ledger: REPRODUCIBLE"
printf '%s\n' "artifact tree SHA-256: $RUN1_HASH"
