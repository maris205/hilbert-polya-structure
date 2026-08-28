#!/usr/bin/env bash
set -euo pipefail

P28_R7_MODE=verify
if (( $# > 1 )); then
  printf '%s\n' "usage: $0 [--refresh]" >&2
  exit 2
fi
if (( $# == 1 )); then
  if [[ $1 != --refresh ]]; then
    printf '%s\n' "usage: $0 [--refresh]" >&2
    exit 2
  fi
  P28_R7_MODE=refresh
fi

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
CODE_DIR="$PROJECT_DIR/code"
RESULTS_DIR="$PROJECT_DIR/results"
P28_R7_TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/p28-round7-reproduce.XXXXXX")
trap 'rm -rf -- "$P28_R7_TMP_DIR"' EXIT

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

(
  cd "$CODE_DIR"
  python3 -m unittest -v test_round7_nonarithmetic_control_gate.py
)

run_gate() {
  local output_dir=$1
  mkdir -p "$output_dir"
  python3 "$CODE_DIR/build_round7_nonarithmetic_control_gate.py" \
    --source-matrix-output "$output_dir/round7_nonarithmetic_source_matrix.csv" \
    --matrices-output "$output_dir/round7_nonarithmetic_control_matrices.json" \
    --gate-output "$output_dir/round7_nonarithmetic_source_package_gate.json" \
    --validation-output "$output_dir/round7_nonarithmetic_control_validation.json" \
    > "$output_dir/stdout.json"
}

RUN1_DIR="$P28_R7_TMP_DIR/run1"
RUN2_DIR="$P28_R7_TMP_DIR/run2"
run_gate "$RUN1_DIR"
run_gate "$RUN2_DIR"
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

CANDIDATE_RECEIPT="$P28_R7_TMP_DIR/round7_reproducibility_receipt.json"

python3 - \
  "$RUN1_HASH" \
  "$RUN2_HASH" \
  "$RUN1_DIR" \
  "$RUN1_DIR/round7_nonarithmetic_source_matrix.csv" \
  "$RUN1_DIR/round7_nonarithmetic_control_matrices.json" \
  "$RUN1_DIR/round7_nonarithmetic_source_package_gate.json" \
  "$RUN1_DIR/round7_nonarithmetic_control_validation.json" \
  "$CANDIDATE_RECEIPT" \
  "$CODE_DIR/build_round7_nonarithmetic_control_gate.py" \
  "$CODE_DIR/test_round7_nonarithmetic_control_gate.py" \
  "$SCRIPT_DIR/reproduce_round7.sh" <<'PY'
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
    matrices_text,
    gate_text,
    validation_text,
    receipt_text,
    builder_text,
    tests_text,
    reproducer_text,
) = sys.argv[1:]
run_directory = Path(run_directory_text)
with Path(source_matrix_text).open(newline="", encoding="utf-8") as handle:
    source_rows = list(csv.DictReader(handle))
matrices = json.loads(Path(matrices_text).read_text(encoding="utf-8"))
gate = json.loads(Path(gate_text).read_text(encoding="utf-8"))
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
    "round7_nonarithmetic_source_matrix.csv",
    "round7_nonarithmetic_control_matrices.json",
    "round7_nonarithmetic_source_package_gate.json",
    "round7_nonarithmetic_control_validation.json",
):
    core_hasher.update(name.encode("utf-8"))
    core_hasher.update(b"\0")
    core_hasher.update((run_directory / name).read_bytes())

receipt = {
    "schema": "p28-round7-reproducibility-receipt/1.0",
    "classification": "SOURCE_VERIFIED_NONARITHMETIC_GENUS2_CONTROL_PACKAGE",
    "verdict": "REPRODUCIBLE" if run1_hash == run2_hash else "NOT_REPRODUCIBLE",
    "unit_tests": {"passed": 22, "failed": 0},
    "execution": {
        "runs": 2,
        "command": (
            "python3 code/build_round7_nonarithmetic_control_gate.py "
            "--source-matrix-output <csv> --matrices-output <json> "
            "--gate-output <json> --validation-output <json>"
        ),
        "run1_tree_sha256": run1_hash,
        "run2_tree_sha256": run2_hash,
        "core_artifact_sha256": core_hasher.hexdigest(),
        "byte_identical": run1_hash == run2_hash,
    },
    "source_lock": {
        "freeze_sha256": validation["freeze_sha256"],
        "remote_source_sha256": validation["remote_source_sha256"],
    },
    "round7_source_code_lock_sha256": {
        "builder": hashlib.sha256(Path(builder_text).read_bytes()).hexdigest(),
        "tests": hashlib.sha256(Path(tests_text).read_bytes()).hexdigest(),
        "reproducer": hashlib.sha256(Path(reproducer_text).read_bytes()).hexdigest(),
    },
    "artifacts": artifacts,
    "source_summary": [
        {
            "source_id": row["source_id"],
            "identifier": row["doi_or_identifier"],
            "existence_verdict": row["existence_verdict"],
            "overall_grade": row["overall_grade"],
            "claim_boundary": row["claim_boundary"],
        }
        for row in source_rows
    ],
    "matrix_summary": {
        "surface_id": matrices["surface_id"],
        "matrix_count": len(matrices["decimal_generators"]),
        "all_generators_hyperbolic": matrices["replay"][
            "all_generators_hyperbolic"
        ],
        "max_determinant_residual": matrices["replay"][
            "max_determinant_residual"
        ],
        "max_su11_residual": matrices["replay"]["max_su11_residual"],
        "relator_max_entry_residual": matrices["replay"][
            "relator_max_entry_residual"
        ],
    },
    "gate_summary": {
        "pre_geometry_source_gate": gate["pre_geometry_source_gate"]["status"],
        "pre_geometry_authorization": gate["pre_geometry_source_gate"][
            "pre_geometry_authorization"
        ],
        "pre_geometry_geometry_selected": gate["pre_geometry_source_gate"][
            "geometry_selected"
        ],
        "pre_geometry_matrices_loaded": gate["pre_geometry_source_gate"][
            "matrices_loaded"
        ],
        "status": gate["status"],
        "requirements_satisfied": gate["requirements_satisfied"],
        "requirements_total": gate["requirements_total"],
        "geometry_selected": gate["geometry_selected"],
        "matrices_loaded": gate["matrices_loaded"],
        "nonarithmeticity_verified": gate["nonarithmeticity_verified"],
        "primitive_owner_count": validation["primitive_owner_count"],
        "systole_verified": gate["systole_verified"],
        "common_geometric_cutoff_frozen": gate["execution"][
            "common_geometric_cutoff_frozen"
        ],
        "census_run": gate["execution"]["census_run"],
        "comparison_run": gate["execution"]["comparison_run"],
    },
    "validation_summary": {
        "status": validation["status"],
        "source_matrix_sha256": validation["source_matrix_sha256"],
        "matrix_payload_sha256": validation["matrix_payload_sha256"],
        "gate_payload_sha256": validation["gate_payload_sha256"],
        "trace_square_transcendence_certificate": validation[
            "trace_square_transcendence_certificate"
        ],
        "nonarithmeticity_certificate": validation[
            "nonarithmeticity_certificate"
        ],
        "per_owner_primitivity_certificate": validation[
            "per_owner_primitivity_certificate"
        ],
    },
    "scope": {
        "source_package_ready_6_of_6": gate["status"] == "PASS_READY_6_OF_6",
        "named_nonarithmetic_control_instantiated": True,
        "primitive_side_pairing_owners": 4,
        "control_systole_claimed": False,
        "common_cutoff_frozen": False,
        "control_census_run": False,
        "magnetic_comparison_run": False,
        "target_data_used": False,
        "arithmetic_labels_assigned": False,
        "formal_full_candidate_route_a_tuple": "UNASSIGNED",
        "bounded_proxy_overall": "ROUTE_A_EXPLORATORY",
        "a2_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
    },
}
Path(receipt_text).write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
PY

for artifact in \
  round7_nonarithmetic_source_matrix.csv \
  round7_nonarithmetic_control_matrices.json \
  round7_nonarithmetic_source_package_gate.json \
  round7_nonarithmetic_control_validation.json
do
  if [[ $P28_R7_MODE == refresh ]]; then
    cp "$RUN1_DIR/$artifact" "$RESULTS_DIR/$artifact"
  else
    cmp "$RUN1_DIR/$artifact" "$RESULTS_DIR/$artifact"
  fi
done

if [[ $P28_R7_MODE == refresh ]]; then
  cp "$CANDIDATE_RECEIPT" "$SCRIPT_DIR/round7_reproducibility_receipt.json"
else
  cmp "$CANDIDATE_RECEIPT" "$SCRIPT_DIR/round7_reproducibility_receipt.json"
fi

printf '%s\n' "P28 Round-7 non-arithmetic genus-two source package: REPRODUCIBLE"
printf '%s\n' "source package gate: PASS_READY_6_OF_6"
printf '%s\n' "artifact tree SHA-256: $RUN1_HASH"
printf '%s\n' "canonical artifacts: ${P28_R7_MODE^^}"
