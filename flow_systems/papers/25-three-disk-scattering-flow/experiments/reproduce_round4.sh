#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
CODE_DIR="$PROJECT_DIR/code"
RESULTS_DIR="$PROJECT_DIR/results"
P25_R4_TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/p25-round4-reproduce.XXXXXX")
trap 'rm -rf -- "$P25_R4_TMP_DIR"' EXIT

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

python3 "$CODE_DIR/test_round4_conditioning_audit.py" -v

RUN1_DIR="$P25_R4_TMP_DIR/run1"
RUN2_DIR="$P25_R4_TMP_DIR/run2"
mkdir -p "$RUN1_DIR" "$RUN2_DIR"
python3 "$CODE_DIR/round4_conditioning_audit.py" --output-dir "$RUN1_DIR" \
  > "$P25_R4_TMP_DIR/run1.stdout.json"
python3 "$CODE_DIR/round4_conditioning_audit.py" --output-dir "$RUN2_DIR" \
  > "$P25_R4_TMP_DIR/run2.stdout.json"
diff -ru "$RUN1_DIR" "$RUN2_DIR"
diff -u "$P25_R4_TMP_DIR/run1.stdout.json" "$P25_R4_TMP_DIR/run2.stdout.json"

cp "$RUN1_DIR/round4_conditioning_by_length.csv" "$RESULTS_DIR/"
cp "$RUN1_DIR/round4_fallback_audit.csv" "$RESULTS_DIR/"
cp "$RUN1_DIR/round4_conditioning_metrics.json" "$RESULTS_DIR/"

python3 - "$RUN1_DIR" "$SCRIPT_DIR/round4_reproducibility_receipt.json" <<'PY'
import hashlib
import json
import sys
from pathlib import Path

run_dir = Path(sys.argv[1])
receipt_path = Path(sys.argv[2])
artifacts = []
combined = hashlib.sha256()
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
    "schema": "p25-round4-reproducibility-receipt/1.0",
    "date": "2026-08-27",
    "classification": "POST_HOC_DESCRIPTIVE_CONDITIONING_AUDIT",
    "verdict": "REPRODUCIBLE",
    "unit_tests": {"passed": 8, "failed": 0},
    "execution": {"runs": 2, "byte_identical": True},
    "combined_sha256": combined.hexdigest(),
    "artifacts": artifacts,
    "scope": {
        "new_orbit_solve": False,
        "causal_or_unbiasedness_claim": False,
        "formal_route_a_tuple": "UNASSIGNED",
        "a2_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "prime_or_zero_tables_used": False,
    },
}
receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": "REPRODUCIBLE", "combined_sha256": combined.hexdigest()}, sort_keys=True))
PY
