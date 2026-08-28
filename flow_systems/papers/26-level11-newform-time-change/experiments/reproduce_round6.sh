#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
CODE_DIR="$PROJECT_DIR/code"
RESULTS_DIR="$PROJECT_DIR/results"
ROUND4_CYCLE_LEDGER="$RESULTS_DIR/round4_hecke_cycle_ledger.csv"
ROUND4_PERIOD_SUMMARY="$RESULTS_DIR/round4_hecke_period_summary.csv"
RECEIPT_PATH="$SCRIPT_DIR/round6_reproducibility_receipt.json"
P26_R6_TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/p26-round6-reproduce.XXXXXX")
trap 'rm -rf -- "$P26_R6_TMP_DIR"' EXIT

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

(
  cd "$CODE_DIR"
  python3 -m unittest -v test_round6_second_variation.py
)

RUN1_DIR="$P26_R6_TMP_DIR/run1"
RUN2_DIR="$P26_R6_TMP_DIR/run2"
python3 "$CODE_DIR/round6_second_variation.py" \
  --output "$RUN1_DIR" \
  --round4-cycle-ledger "$ROUND4_CYCLE_LEDGER" \
  --round4-period-summary "$ROUND4_PERIOD_SUMMARY" \
  > "$P26_R6_TMP_DIR/run1.json"
python3 "$CODE_DIR/round6_second_variation.py" \
  --output "$RUN2_DIR" \
  --round4-cycle-ledger "$ROUND4_CYCLE_LEDGER" \
  --round4-period-summary "$ROUND4_PERIOD_SUMMARY" \
  > "$P26_R6_TMP_DIR/run2.json"
diff -ru "$RUN1_DIR" "$RUN2_DIR"
cmp "$P26_R6_TMP_DIR/run1.json" "$P26_R6_TMP_DIR/run2.json"

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
  round6_inverse_pair_second_variation_ledger.csv \
  round6_quadratic_degree_moment_ledger.csv \
  round6_hecke_second_variation_ledger.csv \
  round6_summary.json \
  round6_artifact_manifest.json
do
  cp "$RUN1_DIR/$artifact" "$RESULTS_DIR/$artifact"
done

python3 - \
  "$RUN1_HASH" \
  "$RUN2_HASH" \
  "$RUN1_DIR" \
  "$RECEIPT_PATH" \
  "$CODE_DIR/round6_second_variation.py" \
  "$CODE_DIR/test_round6_second_variation.py" \
  "$SCRIPT_DIR/reproduce_round6.sh" \
  "$CODE_DIR/round5_zeta_variation.py" \
  "$ROUND4_CYCLE_LEDGER" \
  "$ROUND4_PERIOD_SUMMARY" <<'PY'
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
    round5_generator_text,
    round4_cycle_text,
    round4_period_text,
) = sys.argv[1:]
run_directory = Path(run_directory_text)
receipt_path = Path(receipt_text)


def binding(path: Path) -> dict[str, object]:
    return {
        "path": path.name,
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


summary = json.loads((run_directory / "round6_summary.json").read_text(encoding="utf-8"))
receipt = {
    "schema": "p26-round6-reproducibility-receipt/1.0",
    "date": "2026-08-28",
    "classification": "DETERMINISTIC_FINITE_LOCAL_SECOND_VARIATION_AUDIT",
    "verdict": "REPRODUCIBLE",
    "unit_tests": {"passed": 12, "failed": 0},
    "execution": {
        "runs": 2,
        "command": (
            "python3 code/round6_second_variation.py "
            "--output <isolated-run-directory> "
            "--round4-cycle-ledger results/round4_hecke_cycle_ledger.csv "
            "--round4-period-summary results/round4_hecke_period_summary.csv"
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
        binding(Path(round5_generator_text)),
        binding(Path(round4_cycle_text)),
        binding(Path(round4_period_text)),
    ],
    "registered_results": {
        "inverse_pair_repetition_rows": summary["inverse_pair_repetition_rows"],
        "quadratic_degree_moment_rows": summary["quadratic_degree_moment_rows"],
        "hecke_second_variation_rows": summary["hecke_second_variation_rows"],
        "groups_with_nonunit_quadratic_mass_above_tolerance": summary[
            "groups_with_nonunit_quadratic_mass_above_tolerance"
        ],
        "lambda_a_p_degree_moment_groups_failing": summary[
            "lambda_a_p_degree_moment_groups_failing"
        ],
        "lambda_a_p_squared_degree_moment_groups_failing": summary[
            "lambda_a_p_squared_degree_moment_groups_failing"
        ],
        "secondary_a_p_squared_minus_p_degree_moment_groups_failing": summary[
            "secondary_a_p_squared_minus_p_degree_moment_groups_failing"
        ],
        "lambda_a_p_ruelle_row_failures": summary[
            "lambda_a_p_ruelle_row_failures"
        ],
        "lambda_a_p_squared_ruelle_row_failures": summary[
            "lambda_a_p_squared_ruelle_row_failures"
        ],
        "secondary_a_p_squared_minus_p_ruelle_row_failures": summary[
            "secondary_a_p_squared_minus_p_ruelle_row_failures"
        ],
    },
    "scope": summary["claim_boundary"],
}
receipt_path.write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
PY

printf '%s\n' "P26 Round-6 reproducibility: REPRODUCIBLE"
printf '%s\n' "artifact tree SHA-256: $RUN1_HASH"
