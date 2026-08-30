#!/usr/bin/env bash
set -euo pipefail

MODE=verify
if [ "${1:-}" = "--refresh-support" ]; then
  MODE=refresh-support
  shift
fi
if [ "$#" -ne 0 ]; then
  printf '%s\n' "usage: $0 [--refresh-support]" >&2
  exit 2
fi

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
CODE_DIR="$PROJECT_DIR/code"
RESULTS_DIR="$PROJECT_DIR/results"
NOTES_DIR="$PROJECT_DIR/notes"
SUPPORT_SCRIPT="$CODE_DIR/stage4_round8_support.py"
MANIFEST_PATH="$NOTES_DIR/stage4_round8_dependency_manifest.json"
LEDGER_NAME=stage4_matched_exact_control_decomposition.csv
SUMMARY_NAME=stage4_matched_exact_control_summary.json
RECEIPT_NAME=stage4_round8_support_receipt.json

P26_STAGE4_TMP_DIR=$(mktemp -d "${TMPDIR:-/tmp}/p26-stage4-support.XXXXXX")
trap 'rm -rf -- "$P26_STAGE4_TMP_DIR"' EXIT

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

if [ "$MODE" = refresh-support ]; then
  python3 "$SUPPORT_SCRIPT" build-manifest --output "$MANIFEST_PATH"
fi
python3 "$SUPPORT_SCRIPT" verify-manifest --manifest "$MANIFEST_PATH"

LEGACY_LOG="$P26_STAGE4_TMP_DIR/legacy-tests.log"
bash "$SCRIPT_DIR/reproduce_round8.sh" 2>&1 | tee "$LEGACY_LOG"
LEGACY_TESTS_PASSED=$(sed -n 's/^Ran \([0-9][0-9]*\) tests.*$/\1/p' "$LEGACY_LOG" | tail -n 1)
if [ -z "$LEGACY_TESTS_PASSED" ]; then
  printf '%s\n' "could not determine executed legacy Round-8 test count" >&2
  exit 2
fi

SUPPORT_LOG="$P26_STAGE4_TMP_DIR/support-tests.log"
(
  cd "$CODE_DIR"
  python3 -m unittest -v test_stage4_round8_support.py
) 2>&1 | tee "$SUPPORT_LOG"
SUPPORT_TESTS_PASSED=$(sed -n 's/^Ran \([0-9][0-9]*\) tests.*$/\1/p' "$SUPPORT_LOG" | tail -n 1)
if [ -z "$SUPPORT_TESTS_PASSED" ]; then
  printf '%s\n' "could not determine executed Stage-4 support test count" >&2
  exit 2
fi

RUN1_DIR="$P26_STAGE4_TMP_DIR/run1"
RUN2_DIR="$P26_STAGE4_TMP_DIR/run2"
python3 "$SUPPORT_SCRIPT" build-results \
  --manifest "$MANIFEST_PATH" \
  --output-dir "$RUN1_DIR"
python3 "$SUPPORT_SCRIPT" build-results \
  --manifest "$MANIFEST_PATH" \
  --output-dir "$RUN2_DIR"
cmp "$RUN1_DIR/$LEDGER_NAME" "$RUN2_DIR/$LEDGER_NAME"
cmp "$RUN1_DIR/$SUMMARY_NAME" "$RUN2_DIR/$SUMMARY_NAME"

GENERATED_RECEIPT="$P26_STAGE4_TMP_DIR/$RECEIPT_NAME"
python3 "$SUPPORT_SCRIPT" build-receipt \
  --manifest "$MANIFEST_PATH" \
  --run1-dir "$RUN1_DIR" \
  --run2-dir "$RUN2_DIR" \
  --legacy-tests-passed "$LEGACY_TESTS_PASSED" \
  --support-tests-passed "$SUPPORT_TESTS_PASSED" \
  --output "$GENERATED_RECEIPT"

# Recheck every manifest-bound source/input/canonical byte after execution.
python3 "$SUPPORT_SCRIPT" verify-manifest --manifest "$MANIFEST_PATH"

if [ "$MODE" = refresh-support ]; then
  cp "$RUN1_DIR/$LEDGER_NAME" "$RESULTS_DIR/$LEDGER_NAME"
  cp "$RUN1_DIR/$SUMMARY_NAME" "$RESULTS_DIR/$SUMMARY_NAME"
  cp "$GENERATED_RECEIPT" "$SCRIPT_DIR/$RECEIPT_NAME"
else
  cmp "$RUN1_DIR/$LEDGER_NAME" "$RESULTS_DIR/$LEDGER_NAME"
  cmp "$RUN1_DIR/$SUMMARY_NAME" "$RESULTS_DIR/$SUMMARY_NAME"
  cmp "$GENERATED_RECEIPT" "$SCRIPT_DIR/$RECEIPT_NAME"
fi

printf '%s\n' "P26 Stage-4 Round-8 support: REPRODUCIBLE ($MODE)"
sha256sum \
  "$MANIFEST_PATH" \
  "$RESULTS_DIR/$LEDGER_NAME" \
  "$RESULTS_DIR/$SUMMARY_NAME" \
  "$SCRIPT_DIR/$RECEIPT_NAME"
