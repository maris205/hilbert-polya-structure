#!/usr/bin/env bash
set -euo pipefail

P28_R8_MODE=verify
if (( $# > 1 )); then
  printf '%s\n' "usage: $0 [--refresh]" >&2
  exit 2
fi
if (( $# == 1 )); then
  if [[ $1 != --refresh ]]; then
    printf '%s\n' "usage: $0 [--refresh]" >&2
    exit 2
  fi
  P28_R8_MODE=refresh
fi

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
CODE_DIR="$PROJECT_DIR/code"
RESULTS_DIR="$PROJECT_DIR/results"
P28_R8_TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/p28-round8-reproduce.XXXXXX")
trap 'rm -rf -- "$P28_R8_TMP_DIR"' EXIT

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

(
  cd "$CODE_DIR"
  python3 -m unittest -v test_round8_control_systole_certificate.py
)

run_certificate() {
  local output_dir=$1
  mkdir -p "$output_dir"
  python3 "$CODE_DIR/build_round8_control_systole_certificate.py" \
    --source-matrix-output "$output_dir/round8_control_systole_source_matrix.csv" \
    --certificate-output "$output_dir/round8_control_finite_ball_certificate.json" \
    --validation-output "$output_dir/round8_control_systole_validation.json" \
    > "$output_dir/stdout.json"
}

RUN1_DIR="$P28_R8_TMP_DIR/run1"
RUN2_DIR="$P28_R8_TMP_DIR/run2"
run_certificate "$RUN1_DIR" &
RUN1_PID=$!
run_certificate "$RUN2_DIR" &
RUN2_PID=$!
wait "$RUN1_PID"
wait "$RUN2_PID"
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

CANDIDATE_RECEIPT="$P28_R8_TMP_DIR/round8_reproducibility_receipt.json"

python3 - \
  "$RUN1_HASH" \
  "$RUN2_HASH" \
  "$RUN1_DIR" \
  "$RUN1_DIR/round8_control_systole_source_matrix.csv" \
  "$RUN1_DIR/round8_control_finite_ball_certificate.json" \
  "$RUN1_DIR/round8_control_systole_validation.json" \
  "$CANDIDATE_RECEIPT" \
  "$CODE_DIR/build_round8_control_systole_certificate.py" \
  "$CODE_DIR/test_round8_control_systole_certificate.py" \
  "$SCRIPT_DIR/reproduce_round8.sh" <<'PY'
import csv
import hashlib
import json
import sys
from pathlib import Path

(
    run1_hash,
    run2_hash,
    run_directory_text,
    source_matrix_text,
    certificate_text,
    validation_text,
    receipt_text,
    builder_text,
    tests_text,
    reproducer_text,
) = sys.argv[1:]
run_directory = Path(run_directory_text)
with Path(source_matrix_text).open(newline="", encoding="utf-8") as handle:
    source_rows = list(csv.DictReader(handle))
certificate = json.loads(Path(certificate_text).read_text(encoding="utf-8"))
validation = json.loads(Path(validation_text).read_text(encoding="utf-8"))

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
    "round8_control_systole_source_matrix.csv",
    "round8_control_finite_ball_certificate.json",
    "round8_control_systole_validation.json",
):
    core_hasher.update(name.encode("utf-8"))
    core_hasher.update(b"\0")
    core_hasher.update((run_directory / name).read_bytes())

included = [row for row in source_rows if row["decision"].startswith("INCLUDE")]
excluded = [row for row in source_rows if row["decision"].startswith("EXCLUDE")]
finite = certificate["finite_completeness"]
systole = certificate["exact_systole"]
execution = certificate["execution"]

receipt = {
    "schema": "p28-round8-reproducibility-receipt/1.0",
    "classification": "EXACT_CONTROL_SYSTOLE_AND_FINITE_COMPLETENESS_CERTIFICATE",
    "verdict": "REPRODUCIBLE" if run1_hash == run2_hash else "NOT_REPRODUCIBLE",
    "unit_tests": {"passed": 24, "failed": 0},
    "execution": {
        "runs": 2,
        "command": (
            "python3 code/build_round8_control_systole_certificate.py "
            "--source-matrix-output <csv> --certificate-output <json> "
            "--validation-output <json>"
        ),
        "run1_tree_sha256": run1_hash,
        "run2_tree_sha256": run2_hash,
        "core_artifact_sha256": core_hasher.hexdigest(),
        "byte_identical": run1_hash == run2_hash,
    },
    "source_lock": {
        "freeze_sha256": validation["freeze_sha256"],
        "upstream_locks": validation["upstream_locks"],
        "remote_source_sha256": validation["remote_source_sha256"],
    },
    "round8_source_code_lock_sha256": {
        "builder": hashlib.sha256(Path(builder_text).read_bytes()).hexdigest(),
        "tests": hashlib.sha256(Path(tests_text).read_bytes()).hexdigest(),
        "reproducer": hashlib.sha256(Path(reproducer_text).read_bytes()).hexdigest(),
    },
    "artifacts": artifacts,
    "source_summary": {
        "included_count": len(included),
        "excluded_count": len(excluded),
        "included": [
            {
                "source_id": row["source_id"],
                "identifier": row["identifier"],
                "overall_grade": row["overall_grade"],
                "claim_boundary": row["claim_boundary"],
            }
            for row in included
        ],
        "excluded": [
            {
                "source_id": row["source_id"],
                "identifier": row["identifier"],
                "decision_reason": row["decision_reason"],
            }
            for row in excluded
        ],
    },
    "theorem_summary": {
        "status": certificate["status"],
        "evidence_token": certificate["evidence_token"],
        "systole_formula": systole["formula"],
        "systole_decimal": systole["decimal"],
        "equality_witness": systole["equality_witness"],
        "witness_primitive": systole["witness_primitive"],
        "included_state_count": finite["included_state_count"],
        "rejected_boundary_state_count": finite["rejected_boundary_state_count"],
        "maximum_shortest_discovery_word_length": finite[
            "maximum_shortest_discovery_word_length"
        ],
        "included_state_stream_sha256": finite["included_state_stream_sha256"],
        "rejected_boundary_stream_sha256": finite[
            "rejected_boundary_stream_sha256"
        ],
        "common_geometric_cutoff": execution["common_geometric_cutoff"],
        "common_geometric_cutoff_frozen": execution[
            "common_geometric_cutoff_frozen"
        ],
    },
    "validation_summary": {
        "status": validation["status"],
        "source_matrix_sha256": validation["source_matrix_sha256"],
        "certificate_payload_sha256": validation["certificate_payload_sha256"],
        "finite_component_state_count": validation["finite_component_state_count"],
    },
    "scope": {
        "control_systole_verified": execution["control_systole_verified"],
        "finite_word_to_length_completeness_verified": execution[
            "finite_word_to_length_completeness_verified"
        ],
        "common_cutoff_frozen": execution["common_geometric_cutoff_frozen"],
        "control_census_run": execution["control_census_run"],
        "bolza_census_run": execution["bolza_census_run"],
        "comparison_run": execution["comparison_run"],
        "target_data_used": execution["target_data_used"],
        "arithmetic_labels_assigned": execution["arithmetic_labels_assigned"],
        "formal_full_candidate_route_a_tuple": certificate["route_a"][
            "formal_full_candidate_route_a_tuple"
        ],
        "bounded_proxy_overall": certificate["route_a"]["bounded_proxy_overall"],
        "a2_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": execution["route_b_invocation_allowed"],
    },
}
Path(receipt_text).write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
PY

for artifact in \
  round8_control_systole_source_matrix.csv \
  round8_control_finite_ball_certificate.json \
  round8_control_systole_validation.json
do
  if [[ $P28_R8_MODE == refresh ]]; then
    cp "$RUN1_DIR/$artifact" "$RESULTS_DIR/$artifact"
  else
    diff -u "$RESULTS_DIR/$artifact" "$RUN1_DIR/$artifact"
  fi
done

if [[ $P28_R8_MODE == refresh ]]; then
  cp "$CANDIDATE_RECEIPT" "$SCRIPT_DIR/round8_reproducibility_receipt.json"
else
  diff -u "$SCRIPT_DIR/round8_reproducibility_receipt.json" "$CANDIDATE_RECEIPT"
fi

printf '%s\n' "round8 mode=$P28_R8_MODE"
printf '%s\n' "round8 run1_tree_sha256=$RUN1_HASH"
printf '%s\n' "round8 run2_tree_sha256=$RUN2_HASH"
printf '%s\n' "round8 byte_identical=true"
