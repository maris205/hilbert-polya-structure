#!/usr/bin/env bash
set -euo pipefail

MODE=verify
if [ "${1:-}" = "--refresh" ]; then
  MODE=refresh
  shift
fi
if [ "$#" -ne 0 ]; then
  printf '%s\n' "usage: $0 [--refresh]" >&2
  exit 2
fi

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
CODE_DIR="$PROJECT_DIR/code"
RESULTS_DIR="$PROJECT_DIR/results"
ROUND4_CYCLE_LEDGER="$RESULTS_DIR/round4_hecke_cycle_ledger.csv"
ROUND6_MOMENT_LEDGER="$RESULTS_DIR/round6_quadratic_degree_moment_ledger.csv"
FREEZE_PATH="$PROJECT_DIR/notes/round7_survivor_classification_freeze.md"
RECEIPT_PATH="$SCRIPT_DIR/round7_reproducibility_receipt.json"
P26_R7_TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/p26-round7-reproduce.XXXXXX")
trap 'rm -rf -- "$P26_R7_TMP_DIR"' EXIT

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

(
  cd "$CODE_DIR"
  python3 -m unittest -v test_round7_exact_survivors.py
)

RUN1_DIR="$P26_R7_TMP_DIR/run1"
RUN2_DIR="$P26_R7_TMP_DIR/run2"
python3 "$CODE_DIR/round7_exact_survivors.py" \
  --output "$RUN1_DIR" \
  --round4-cycle-ledger "$ROUND4_CYCLE_LEDGER" \
  --round6-moment-ledger "$ROUND6_MOMENT_LEDGER" \
  > "$P26_R7_TMP_DIR/run1.json"
python3 "$CODE_DIR/round7_exact_survivors.py" \
  --output "$RUN2_DIR" \
  --round4-cycle-ledger "$ROUND4_CYCLE_LEDGER" \
  --round6-moment-ledger "$ROUND6_MOMENT_LEDGER" \
  > "$P26_R7_TMP_DIR/run2.json"
diff -ru "$RUN1_DIR" "$RUN2_DIR"
cmp "$P26_R7_TMP_DIR/run1.json" "$P26_R7_TMP_DIR/run2.json"

tree_hash() {
  (
    cd "$1"
    find . -type f -print0 | sort -z | xargs -0 sha256sum
  ) | sha256sum | awk '{print $1}'
}

RUN1_HASH=$(tree_hash "$RUN1_DIR")
RUN2_HASH=$(tree_hash "$RUN2_DIR")
test "$RUN1_HASH" = "$RUN2_HASH"

python3 - \
  "$RUN1_HASH" \
  "$RUN2_HASH" \
  "$RUN1_DIR" \
  "$P26_R7_TMP_DIR/receipt.json" \
  "$CODE_DIR/round7_exact_survivors.py" \
  "$CODE_DIR/test_round7_exact_survivors.py" \
  "$SCRIPT_DIR/reproduce_round7.sh" \
  "$FREEZE_PATH" \
  "$ROUND4_CYCLE_LEDGER" \
  "$ROUND6_MOMENT_LEDGER" <<'PY'
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
    freeze_text,
    round4_cycle_text,
    round6_moment_text,
) = sys.argv[1:]
run_directory = Path(run_directory_text)
receipt_path = Path(receipt_text)


def binding(path: Path) -> dict[str, object]:
    return {
        "path": path.name,
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


summary = json.loads((run_directory / "round7_summary.json").read_text(encoding="utf-8"))
receipt = {
    "schema": "p26-round7-reproducibility-receipt/1.0",
    "date": "2026-08-28",
    "classification": "EXACT_TARGET_FREE_GAMMA0_11_HOMOLOGY_AUDIT",
    "verdict": "REPRODUCIBLE",
    "unit_tests": {"passed": 13, "failed": 0},
    "execution": {
        "runs": 2,
        "command": (
            "python3 code/round7_exact_survivors.py "
            "--output <isolated-run-directory> "
            "--round4-cycle-ledger results/round4_hecke_cycle_ledger.csv "
            "--round6-moment-ledger results/round6_quadratic_degree_moment_ledger.csv"
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
        binding(Path(freeze_text)),
        binding(Path(round4_cycle_text)),
        binding(Path(round6_moment_text)),
    ],
    "registered_results": {
        "frozen_survivors": summary["frozen_survivors"],
        "exactly_classified": summary["exactly_classified"],
        "exact_lambda_a_p_squared_group_moment_survivors": summary[
            "exact_lambda_a_p_squared_group_moment_survivors"
        ],
        "exact_full_source_kernels": summary["exact_full_source_kernels"],
        "exact_real_projection_only_kernels": summary[
            "exact_real_projection_only_kernels"
        ],
        "floating_quadrature_artifacts": summary["floating_quadrature_artifacts"],
        "unresolved_fail_closed": summary["unresolved_fail_closed"],
    },
    "scope": summary["claim_boundary"],
}
receipt_path.write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
PY

ARTIFACTS='round7_exact_survivor_classification_ledger.csv round7_exact_homology_model.json round7_summary.json round7_artifact_manifest.json'
if [ "$MODE" = refresh ]; then
  for artifact in $ARTIFACTS; do
    cp "$RUN1_DIR/$artifact" "$RESULTS_DIR/$artifact"
  done
  cp "$P26_R7_TMP_DIR/receipt.json" "$RECEIPT_PATH"
else
  for artifact in $ARTIFACTS; do
    cmp "$RUN1_DIR/$artifact" "$RESULTS_DIR/$artifact"
  done
  cmp "$P26_R7_TMP_DIR/receipt.json" "$RECEIPT_PATH"
fi

printf '%s\n' "P26 Round-7 reproducibility: REPRODUCIBLE ($MODE)"
printf '%s\n' "artifact tree SHA-256: $RUN1_HASH"
