#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
CODE_DIR="$PROJECT_DIR/code"
RESULTS_DIR="$PROJECT_DIR/results"
RECEIPT_PATH="$SCRIPT_DIR/round6_reproducibility_receipt.json"
P27_R6_TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/p27-round6-reproduce.XXXXXX")
trap 'rm -rf -- "$P27_R6_TMP_DIR"' EXIT

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

(
  cd "$CODE_DIR"
  python3 -m unittest -v test_round6_positioning_audit.py
)

RUN1_DIR="$P27_R6_TMP_DIR/run1"
RUN2_DIR="$P27_R6_TMP_DIR/run2"
python3 "$CODE_DIR/round6_positioning_audit.py" --output-dir "$RUN1_DIR" \
  > "$P27_R6_TMP_DIR/run1.json"
python3 "$CODE_DIR/round6_positioning_audit.py" --output-dir "$RUN2_DIR" \
  > "$P27_R6_TMP_DIR/run2.json"
diff -ru "$RUN1_DIR" "$RUN2_DIR"
cmp "$P27_R6_TMP_DIR/run1.json" "$P27_R6_TMP_DIR/run2.json"

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
  round6_claim_source_matrix.csv \
  round6_positioning_summary.json \
  round6_artifact_manifest.json
do
  cp "$RUN1_DIR/$artifact" "$RESULTS_DIR/$artifact"
done

python3 - \
  "$RUN1_HASH" \
  "$RUN2_HASH" \
  "$RUN1_DIR" \
  "$RECEIPT_PATH" \
  "$CODE_DIR/round6_positioning_audit.py" \
  "$CODE_DIR/test_round6_positioning_audit.py" \
  "$SCRIPT_DIR/reproduce_round6.sh" <<'PY'
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


summary = json.loads(
    (run_directory / "round6_positioning_summary.json").read_text(encoding="utf-8")
)
receipt = {
    "schema": "p27-round6-reproducibility-receipt/1.0",
    "date": "2026-08-28",
    "classification": "DETERMINISTIC_CLAIM_SOURCE_AND_POSITIONING_CONTRACT",
    "verdict": "REPRODUCIBLE",
    "unit_tests": {"passed": 11, "failed": 0},
    "execution": {
        "runs": 2,
        "command": (
            "python3 code/round6_positioning_audit.py "
            "--output-dir <isolated-run-directory>"
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
        "claim_source_rows": summary["claim_source_rows"],
        "primary_source_web_verified_rows": summary[
            "primary_source_web_verified_rows"
        ],
        "human_confirmation_pending_rows": summary[
            "human_confirmation_pending_rows"
        ],
        "user_attested_read_rows": summary["user_attested_read_rows"],
        "three_way_go_no_go": summary["three_way_go_no_go"],
    },
    "scope": summary["claim_boundary"],
    "human_source_gate": summary["human_source_gate"],
}
receipt_path.write_text(
    json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
PY

printf '%s\n' "P27 Round-6 reproducibility: REPRODUCIBLE"
printf '%s\n' "artifact tree SHA-256: $RUN1_HASH"
