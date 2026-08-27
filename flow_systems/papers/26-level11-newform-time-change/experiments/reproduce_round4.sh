#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
CODE_DIR="$PROJECT_DIR/code"
RESULTS_DIR="$PROJECT_DIR/results"
RECEIPT_PATH="$SCRIPT_DIR/round4_reproducibility_receipt.json"
P26_R4_TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/p26-round4-reproduce.XXXXXX")
trap 'rm -rf -- "$P26_R4_TMP_DIR"' EXIT

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

(
  cd "$CODE_DIR"
  python3 -m unittest -v test_round4_hecke_correspondence.py
)

RUN1_DIR="$P26_R4_TMP_DIR/run1"
RUN2_DIR="$P26_R4_TMP_DIR/run2"
python3 "$CODE_DIR/round4_hecke_correspondence.py" --output "$RUN1_DIR" > "$P26_R4_TMP_DIR/run1.json"
python3 "$CODE_DIR/round4_hecke_correspondence.py" --output "$RUN2_DIR" > "$P26_R4_TMP_DIR/run2.json"
diff -ru "$RUN1_DIR" "$RUN2_DIR"
cmp "$P26_R4_TMP_DIR/run1.json" "$P26_R4_TMP_DIR/run2.json"

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
  round4_hecke_branch_owner_ledger.csv \
  round4_hecke_coefficient_ledger.csv \
  round4_hecke_cycle_ledger.csv \
  round4_hecke_period_summary.csv \
  round4_summary.json \
  round4_artifact_manifest.json
do
  cp "$RUN1_DIR/$artifact" "$RESULTS_DIR/$artifact"
done

python3 - \
  "$RUN1_HASH" \
  "$RUN2_HASH" \
  "$RUN1_DIR" \
  "$RECEIPT_PATH" \
  "$CODE_DIR/round4_hecke_correspondence.py" \
  "$CODE_DIR/test_round4_hecke_correspondence.py" \
  "$SCRIPT_DIR/reproduce_round4.sh" <<'PY'
import hashlib
import json
import sys
from pathlib import Path

(
    run1_hash,
    run2_hash,
    run_directory_text,
    receipt_text,
    generator_text,
    tests_text,
    reproduction_text,
) = sys.argv[1:]
run_directory = Path(run_directory_text)
receipt_path = Path(receipt_text)


def binding(path: Path) -> dict[str, object]:
    return {
        "path": path.name,
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


summary = json.loads((run_directory / "round4_summary.json").read_text(encoding="utf-8"))
receipt = {
    "schema": "p26-round4-reproducibility-receipt/1.0",
    "classification": "DETERMINISTIC",
    "verdict": "REPRODUCIBLE",
    "unit_tests": {"passed": 8, "failed": 0},
    "execution": {
        "runs": 2,
        "command": (
            "python3 code/round4_hecke_correspondence.py "
            "--output <isolated-run-directory>"
        ),
        "run1_tree_sha256": run1_hash,
        "run2_tree_sha256": run2_hash,
        "byte_identical": run1_hash == run2_hash,
    },
    "artifacts": [binding(path) for path in sorted(run_directory.iterdir())],
    "source_bindings": [
        binding(Path(generator_text)),
        binding(Path(tests_text)),
        binding(Path(reproduction_text)),
    ],
    "registered_results": {
        "exact_branch_gluing_rows": summary["exact_branch_gluing_rows"],
        "exact_eta_coefficient_passes": summary["exact_eta_coefficient_passes"],
        "closed_cycle_owner_rows": summary["closed_cycle_owner_rows"],
        "primitive_closed_cycle_owners": summary["primitive_closed_cycle_owners"],
        "period_summary_rows": summary["period_summary_rows"],
        "maximum_complex_period_residual": summary[
            "maximum_complex_period_residual"
        ],
        "minimum_nonmodular_control_residual": summary[
            "minimum_nonmodular_control_residual"
        ],
    },
    "scope": {
        "ars_stage": "STAGE_1_RESEARCH",
        "proposal_stage": "STAGE_1_ROUTE_A_A0_A1",
        "formal_route_a_tuple": "UNASSIGNED",
        "a2_dynamical_zeta_evaluation_run": False,
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "complete_conjugacy_class_enumeration": False,
        "single_primitive_orbit_recurrence": False,
        "primitive_euler_factorization": False,
        "riemann_zero_data_used": False,
    },
}
receipt_path.write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
PY

printf '%s\n' "P26 Round-4 reproducibility: REPRODUCIBLE"
printf '%s\n' "artifact tree SHA-256: $RUN1_HASH"
