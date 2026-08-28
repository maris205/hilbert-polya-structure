#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
CODE_DIR="$PROJECT_DIR/code"
RESULTS_DIR="$PROJECT_DIR/results"
ROUND4_CYCLE_LEDGER="$RESULTS_DIR/round4_hecke_cycle_ledger.csv"
ROUND4_PERIOD_SUMMARY="$RESULTS_DIR/round4_hecke_period_summary.csv"
RECEIPT_PATH="$SCRIPT_DIR/round5_reproducibility_receipt.json"
P26_R5_TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/p26-round5-reproduce.XXXXXX")
trap 'rm -rf -- "$P26_R5_TMP_DIR"' EXIT

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

(
  cd "$CODE_DIR"
  python3 -m unittest -v test_round5_zeta_variation.py
)

RUN1_DIR="$P26_R5_TMP_DIR/run1"
RUN2_DIR="$P26_R5_TMP_DIR/run2"
python3 "$CODE_DIR/round5_zeta_variation.py" \
  --output "$RUN1_DIR" \
  --round4-cycle-ledger "$ROUND4_CYCLE_LEDGER" \
  --round4-period-summary "$ROUND4_PERIOD_SUMMARY" \
  > "$P26_R5_TMP_DIR/run1.json"
python3 "$CODE_DIR/round5_zeta_variation.py" \
  --output "$RUN2_DIR" \
  --round4-cycle-ledger "$ROUND4_CYCLE_LEDGER" \
  --round4-period-summary "$ROUND4_PERIOD_SUMMARY" \
  > "$P26_R5_TMP_DIR/run2.json"
diff -ru "$RUN1_DIR" "$RUN2_DIR"
cmp "$P26_R5_TMP_DIR/run1.json" "$P26_R5_TMP_DIR/run2.json"

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
  round5_zeta_repetition_ledger.csv \
  round5_degree_moment_ledger.csv \
  round5_hecke_zeta_variation_ledger.csv \
  round5_summary.json \
  round5_artifact_manifest.json
do
  cp "$RUN1_DIR/$artifact" "$RESULTS_DIR/$artifact"
done

python3 - \
  "$RUN1_HASH" \
  "$RUN2_HASH" \
  "$RUN1_DIR" \
  "$RECEIPT_PATH" \
  "$CODE_DIR/round5_zeta_variation.py" \
  "$CODE_DIR/test_round5_zeta_variation.py" \
  "$SCRIPT_DIR/reproduce_round5.sh" \
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


summary = json.loads((run_directory / "round5_summary.json").read_text(encoding="utf-8"))
receipt = {
    "schema": "p26-round5-reproducibility-receipt/1.0",
    "classification": "DETERMINISTIC",
    "verdict": "REPRODUCIBLE",
    "unit_tests": {"passed": 11, "failed": 0},
    "execution": {
        "runs": 2,
        "command": (
            "python3 code/round5_zeta_variation.py "
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
        binding(Path(round4_cycle_text)),
        binding(Path(round4_period_text)),
    ],
    "registered_results": {
        "orientation_repetition_rows": summary["orientation_repetition_rows"],
        "degree_moment_rows": summary["degree_moment_rows"],
        "hecke_zeta_variation_rows": summary["hecke_zeta_variation_rows"],
        "mixed_degree_groups": summary["mixed_degree_groups"],
        "uniform_nonunit_degree_groups": summary["uniform_nonunit_degree_groups"],
        "naive_ruelle_recurrence_failures": summary[
            "naive_ruelle_recurrence_failures"
        ],
        "naive_selberg_recurrence_failures": summary[
            "naive_selberg_recurrence_failures"
        ],
        "alpha_all_s_degree_moment_groups_failing": summary[
            "alpha_all_s_degree_moment_groups_failing"
        ],
    },
    "scope": {
        "ars_stage": "STAGE_1_RESEARCH",
        "proposal_stage": "STAGE_1_ROUTE_A_A0_A1",
        "formal_route_a_tuple": "UNASSIGNED",
        "a2_dynamical_zeta_evaluation_run": False,
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "complete_primitive_enumeration": False,
        "primitive_euler_factorization": False,
        "prime_target_table_used": False,
        "riemann_zero_data_used": False,
    },
}
receipt_path.write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
PY

printf '%s\n' "P26 Round-5 reproducibility: REPRODUCIBLE"
printf '%s\n' "artifact tree SHA-256: $RUN1_HASH"
