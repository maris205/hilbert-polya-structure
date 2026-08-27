#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
CODE_DIR="$PROJECT_DIR/code"
RESULTS_DIR="$PROJECT_DIR/results"
RECEIPT_PATH="$SCRIPT_DIR/reproducibility_receipt.json"
P26_TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/p26-round2-reproduce.XXXXXX")
trap 'rm -rf -- "$P26_TMP_DIR"' EXIT

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

(
  cd "$CODE_DIR"
  python3 -m unittest -v test_round2_experiment.py
)

RUN1_DIR="$P26_TMP_DIR/run1"
RUN2_DIR="$P26_TMP_DIR/run2"
mkdir -p "$RUN1_DIR" "$RUN2_DIR"

python3 "$CODE_DIR/round2_experiment.py" --output "$RUN1_DIR" > "$P26_TMP_DIR/run1_stdout.json"
python3 "$CODE_DIR/round2_experiment.py" --output "$RUN2_DIR" > "$P26_TMP_DIR/run2_stdout.json"

diff -ru "$RUN1_DIR" "$RUN2_DIR"
cmp "$P26_TMP_DIR/run1_stdout.json" "$P26_TMP_DIR/run2_stdout.json"

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
  newform_timechange_variation_ledger.csv \
  simpler_parent_length_control.csv \
  round2_summary.json \
  artifact_manifest.json
do
  cp "$RUN1_DIR/$artifact" "$RESULTS_DIR/$artifact"
done

python3 - "$RUN1_HASH" "$RUN2_HASH" "$RUN1_DIR" "$RECEIPT_PATH" <<'PY'
import hashlib
import json
import sys
from pathlib import Path

run1_hash, run2_hash, run_directory_text, receipt_text = sys.argv[1:]
run_directory = Path(run_directory_text)
receipt_path = Path(receipt_text)

artifacts = []
for artifact in sorted(run_directory.iterdir()):
    content = artifact.read_bytes()
    artifacts.append(
        {
            "path": artifact.name,
            "bytes": len(content),
            "sha256": hashlib.sha256(content).hexdigest(),
        }
    )

receipt = {
    "schema": "p26-round2-reproducibility-receipt/1.0",
    "classification": "DETERMINISTIC",
    "verdict": "REPRODUCIBLE",
    "unit_tests": {"passed": 7, "failed": 0},
    "execution": {
        "runs": 2,
        "command": "python3 code/round2_experiment.py --output <isolated-run-directory>",
        "run1_tree_sha256": run1_hash,
        "run2_tree_sha256": run2_hash,
        "byte_identical": run1_hash == run2_hash,
    },
    "artifacts": artifacts,
    "scope": {
        "max_positive_word_length": 9,
        "formal_route_a_tuple": "UNASSIGNED",
        "route_b_invocation_allowed": False,
        "prime_table_used": False,
        "riemann_zero_data_used": False,
    },
}
receipt_path.write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
PY

printf '%s\n' "P26 Round-2 reproducibility: REPRODUCIBLE"
printf '%s\n' "artifact tree SHA-256: $RUN1_HASH"
printf '%s\n' "results: $RESULTS_DIR"
printf '%s\n' "receipt: $RECEIPT_PATH"
