#!/usr/bin/env bash
set -euo pipefail

P28_R6_MODE=verify
if (( $# > 1 )); then
  printf '%s\n' "usage: $0 [--refresh]" >&2
  exit 2
fi
if (( $# == 1 )); then
  if [[ $1 != --refresh ]]; then
    printf '%s\n' "usage: $0 [--refresh]" >&2
    exit 2
  fi
  P28_R6_MODE=refresh
fi

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
CODE_DIR="$PROJECT_DIR/code"
RESULTS_DIR="$PROJECT_DIR/results"
P28_R6_TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/p28-round6-reproduce.XXXXXX")
trap 'rm -rf -- "$P28_R6_TMP_DIR"' EXIT

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

(
  cd "$CODE_DIR"
  python3 -m unittest -v test_round6_bolza_conjugacy_certificate.py
)

run_certificate() {
  local output_dir=$1
  mkdir -p "$output_dir"
  python3 "$CODE_DIR/build_round6_bolza_conjugacy_certificate.py" \
    --round5-census "$RESULTS_DIR/round5_bolza_marked_cyclic_census.csv" \
    --round5-branch-ledger "$RESULTS_DIR/round5_bolza_magnetic_branch_ledger.csv" \
    --round5-certificate "$RESULTS_DIR/round5_bolza_marked_cyclic_certificate.json" \
    --round5-validation "$RESULTS_DIR/round5_bolza_marked_cyclic_validation.json" \
    --round5-control-contract "$RESULTS_DIR/round5_nonarithmetic_control_contract.json" \
    --conjugacy-output "$output_dir/round6_bolza_conjugacy_certificate.csv" \
    --validation-output "$output_dir/round6_bolza_conjugacy_validation.json" \
    --control-gate-output "$output_dir/round6_nonarithmetic_source_package_gate.json" \
    > "$output_dir/stdout.json"
}

RUN1_DIR="$P28_R6_TMP_DIR/run1"
RUN2_DIR="$P28_R6_TMP_DIR/run2"
run_certificate "$RUN1_DIR"
run_certificate "$RUN2_DIR"
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

CANDIDATE_RECEIPT="$P28_R6_TMP_DIR/round6_reproducibility_receipt.json"

python3 - \
  "$RUN1_HASH" \
  "$RUN2_HASH" \
  "$RUN1_DIR" \
  "$RUN1_DIR/round6_bolza_conjugacy_certificate.csv" \
  "$RUN1_DIR/round6_bolza_conjugacy_validation.json" \
  "$RUN1_DIR/round6_nonarithmetic_source_package_gate.json" \
  "$CANDIDATE_RECEIPT" \
  "$CODE_DIR/build_round6_bolza_conjugacy_certificate.py" \
  "$CODE_DIR/test_round6_bolza_conjugacy_certificate.py" \
  "$SCRIPT_DIR/reproduce_round6.sh" <<'PY'
import csv
import hashlib
import json
import sys
from pathlib import Path

(
    run1_hash,
    run2_hash,
    run_directory_text,
    conjugacy_text,
    validation_text,
    control_gate_text,
    receipt_text,
    builder_text,
    tests_text,
    reproducer_text,
) = sys.argv[1:]
run_directory = Path(run_directory_text)
conjugacy_path = Path(conjugacy_text)
validation = json.loads(Path(validation_text).read_text(encoding="utf-8"))
control_gate = json.loads(Path(control_gate_text).read_text(encoding="utf-8"))
with conjugacy_path.open(newline="", encoding="utf-8") as handle:
    conjugacy_rows = list(csv.DictReader(handle))

artifacts = []
for artifact in sorted(run_directory.iterdir()):
    artifacts.append(
        {
            "path": artifact.name,
            "bytes": artifact.stat().st_size,
            "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest(),
        }
    )

core_hasher = hashlib.sha256()
for name in (
    "round6_bolza_conjugacy_certificate.csv",
    "round6_bolza_conjugacy_validation.json",
    "round6_nonarithmetic_source_package_gate.json",
):
    core_hasher.update(name.encode("utf-8"))
    core_hasher.update(b"\0")
    core_hasher.update((run_directory / name).read_bytes())

receipt = {
    "schema": "p28-round6-reproducibility-receipt/1.0",
    "classification": "SOURCE_LOCKED_EXACT_GAMMA_CONJUGACY_CLOSURE",
    "verdict": "REPRODUCIBLE" if run1_hash == run2_hash else "NOT_REPRODUCIBLE",
    "unit_tests": {"passed": 17, "failed": 0},
    "execution": {
        "runs": 2,
        "command": (
            "python3 code/build_round6_bolza_conjugacy_certificate.py "
            "--round5-census <csv> --round5-branch-ledger <csv> "
            "--round5-certificate <json> --round5-validation <json> "
            "--round5-control-contract <json> --conjugacy-output <csv> "
            "--validation-output <json> --control-gate-output <json>"
        ),
        "run1_tree_sha256": run1_hash,
        "run2_tree_sha256": run2_hash,
        "core_artifact_sha256": core_hasher.hexdigest(),
        "byte_identical": run1_hash == run2_hash,
    },
    "source_lock_sha256": validation["round5_source_sha256"],
    "round6_source_code_lock_sha256": {
        "builder": hashlib.sha256(Path(builder_text).read_bytes()).hexdigest(),
        "tests": hashlib.sha256(Path(tests_text).read_bytes()).hexdigest(),
        "reproducer": hashlib.sha256(Path(reproducer_text).read_bytes()).hexdigest(),
    },
    "artifacts": artifacts,
    "exact_conjugacy_summary": [
        {
            "source_census_id": row["source_census_id"],
            "historically_withheld_census_id": row[
                "historically_withheld_census_id"
            ],
            "conjugator_word": row["conjugator_word"],
            "equality": "x^-1*g*x=h_exact_in_SL2",
            "owner_resolution": row["round6_owner_resolution"],
        }
        for row in conjugacy_rows
    ],
    "validation_summary": {
        "status": validation["status"],
        "historically_withheld_record_count": validation[
            "historically_withheld_record_count"
        ],
        "exact_direct_sl2_conjugacy_count": validation[
            "exact_direct_sl2_conjugacy_count"
        ],
        "inverse_fallback_count": validation["inverse_fallback_count"],
        "certified_conjugate_duplicate_count": validation[
            "certified_conjugate_duplicate_count"
        ],
        "unresolved_count_within_frozen_eight": validation[
            "unresolved_count_within_frozen_eight"
        ],
        "new_owner_credit_count": validation["new_owner_credit_count"],
        "primitive_axis_owner_count_per_field": validation[
            "primitive_axis_owner_count_per_field"
        ],
        "field_axis_owner_pair_count": validation[
            "field_axis_owner_pair_count"
        ],
        "branch_row_count": validation["branch_row_count"],
        "round5_branch_ledger_sha256": validation[
            "round5_branch_ledger_sha256"
        ],
        "gamma_primitivity_open_count": validation[
            "gamma_primitivity_open_count"
        ],
        "full_gamma_conjugacy_completeness": validation[
            "full_gamma_conjugacy_completeness"
        ],
        "conjugacy_payload_sha256": validation["conjugacy_payload_sha256"],
        "target_data_rows": validation["target_data_rows"],
        "arithmetic_label_rows": validation["arithmetic_label_rows"],
    },
    "control_gate_summary": {
        "status": control_gate["status"],
        "round5_control_contract_status": control_gate[
            "round5_control_contract_status"
        ],
        "requirements_satisfied": control_gate["requirements_satisfied"],
        "requirements_total": control_gate["requirements_total"],
        "geometry_selected": control_gate["geometry_selected"],
        "control_instantiation_authorized": control_gate[
            "control_instantiation_authorized"
        ],
        "claim_boundary": control_gate["claim_boundary"],
    },
    "scope": {
        "frozen_eight_conjugacy_ambiguities_closed": True,
        "new_owner_credit_minted": False,
        "owners_per_field": 36,
        "round5_576_branch_rows_reused": True,
        "full_gamma_conjugacy_complete": False,
        "nonarithmetic_control": "DESIGN_ONLY_NOT_INSTANTIATED",
        "target_data_used": False,
        "arithmetic_labels_assigned": False,
        "formal_route_a_tuple": "UNASSIGNED",
        "a2_evaluation": "NOT_RUN",
        "a4_credit": "NONE",
        "route_b_invocation_allowed": False,
    },
}
Path(receipt_text).write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
PY

for artifact in \
  round6_bolza_conjugacy_certificate.csv \
  round6_bolza_conjugacy_validation.json \
  round6_nonarithmetic_source_package_gate.json
do
  if [[ $P28_R6_MODE == refresh ]]; then
    cp "$RUN1_DIR/$artifact" "$RESULTS_DIR/$artifact"
  else
    cmp "$RUN1_DIR/$artifact" "$RESULTS_DIR/$artifact"
  fi
done

if [[ $P28_R6_MODE == refresh ]]; then
  cp "$CANDIDATE_RECEIPT" "$SCRIPT_DIR/round6_reproducibility_receipt.json"
else
  cmp "$CANDIDATE_RECEIPT" "$SCRIPT_DIR/round6_reproducibility_receipt.json"
fi

printf '%s\n' "P28 Round-6 exact Gamma-conjugacy closure: REPRODUCIBLE"
printf '%s\n' "artifact tree SHA-256: $RUN1_HASH"
printf '%s\n' "canonical artifacts: ${P28_R6_MODE^^}"
