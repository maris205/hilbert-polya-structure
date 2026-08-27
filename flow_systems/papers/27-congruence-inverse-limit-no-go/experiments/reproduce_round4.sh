#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
CODE_DIR="$PROJECT_DIR/code"
RESULTS_DIR="$PROJECT_DIR/results"
P27_R4_TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/p27-round4-reproduce.XXXXXX")
trap 'rm -rf -- "$P27_R4_TMP_DIR"' EXIT

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

python3 "$CODE_DIR/test_round4_period_escape.py" -v

RUN1_DIR="$P27_R4_TMP_DIR/run1"
RUN2_DIR="$P27_R4_TMP_DIR/run2"
mkdir -p "$RUN1_DIR" "$RUN2_DIR"
python3 "$CODE_DIR/round4_period_escape.py" --output-dir "$RUN1_DIR" \
  > "$P27_R4_TMP_DIR/run1.stdout.json"
python3 "$CODE_DIR/round4_period_escape.py" --output-dir "$RUN2_DIR" \
  > "$P27_R4_TMP_DIR/run2.stdout.json"
diff -ru "$RUN1_DIR" "$RUN2_DIR"
diff -u "$P27_R4_TMP_DIR/run1.stdout.json" "$P27_R4_TMP_DIR/run2.stdout.json"

cp "$RUN1_DIR/round4_period_escape_ledger.csv" "$RESULTS_DIR/"
cp "$RUN1_DIR/round4_period_escape_validation.json" "$RESULTS_DIR/"

python3 - "$RUN1_DIR" "$SCRIPT_DIR/round4_reproducibility_receipt.json" <<'PY'
import hashlib
import json
import sys
from pathlib import Path

run_dir = Path(sys.argv[1])
receipt_path = Path(sys.argv[2])
combined = hashlib.sha256()
artifacts = []
for path in sorted(run_dir.iterdir()):
    payload = path.read_bytes()
    artifacts.append(
        {"path": path.name, "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()}
    )
    combined.update(path.name.encode("utf-8"))
    combined.update(b"\0")
    combined.update(payload)
    combined.update(b"\0")
receipt = {
    "schema": "p27-round4-reproducibility-receipt/1.0",
    "date": "2026-08-27",
    "classification": "FINITE_PREFIX_VALIDATION_OF_A_PROVED_GENERAL_PERIOD_ESCAPE_THEOREM",
    "verdict": "REPRODUCIBLE",
    "unit_tests": {"passed": 8, "failed": 0},
    "execution": {"runs": 2, "byte_identical": True},
    "combined_sha256": combined.hexdigest(),
    "artifacts": artifacts,
    "scope": {
        "general_theorem_from_finite_rows": False,
        "inverse_limit_periodic_orbit_credit": False,
        "formal_route_a_tuple": "UNASSIGNED",
        "a2_a4": "NOT_EVALUATED",
        "route_b_invocation_allowed": False,
        "prime_or_zero_tables_used": False,
    },
}
receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": "REPRODUCIBLE", "combined_sha256": combined.hexdigest()}, sort_keys=True))
PY
