#!/usr/bin/env bash
set -euo pipefail

export PYTHONDONTWRITEBYTECODE=1
if [[ -n "${PYTHONOPTIMIZE+x}" ]]; then
  echo "PYTHONOPTIMIZE must be completely unset for HCS-C56 replay" >&2
  exit 2
fi

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RESULTS_DIR="$PROJECT_DIR/results"
PYTHON_BIN="${PYTHON:-python3}"
REFRESH=0

if [[ "$#" -gt 1 ]]; then
  echo "usage: $0 [--refresh-prefreeze]" >&2
  exit 2
fi
if [[ "$#" -eq 1 ]]; then
  if [[ "$1" != "--refresh-prefreeze" ]]; then
    echo "usage: $0 [--refresh-prefreeze]" >&2
    exit 2
  fi
  REFRESH=1
fi

if ! "$PYTHON_BIN" -c 'import sys; raise SystemExit(0 if not sys.flags.optimize else 1)'; then
  echo "optimized Python is forbidden for HCS-C56 replay" >&2
  exit 2
fi

mkdir -p "$RESULTS_DIR"
STAGE_DIR="$(mktemp -d "$RESULTS_DIR/.c56-stage-XXXXXXXX")"
cleanup_stage() {
  if [[ -n "${STAGE_DIR:-}" && -d "$STAGE_DIR" ]]; then
    rm -rf -- "$STAGE_DIR"
  fi
}
trap cleanup_stage EXIT HUP INT TERM

STAGED_CERT="$STAGE_DIR/c56_certificate.json"
STAGED_SCHEMA="$STAGE_DIR/c56_schema.json"
STAGED_CHECK="$STAGE_DIR/c56_check_report.json"
STAGED_MANIFEST="$STAGE_DIR/scoped_hash_manifest.json"

"$PYTHON_BIN" "$PROJECT_DIR/code/c56_producer.py" \
  --output "$STAGED_CERT" --schema-output "$STAGED_SCHEMA"
"$PYTHON_BIN" "$PROJECT_DIR/code/c56_checker.py" \
  "$STAGED_CERT" --schema "$STAGED_SCHEMA" --output "$STAGED_CHECK"

C56_CERTIFICATE="$STAGED_CERT" \
C56_SCHEMA="$STAGED_SCHEMA" \
C56_CHECK_REPORT="$STAGED_CHECK" \
  "$PYTHON_BIN" -m unittest discover -s "$PROJECT_DIR/code" -p 'test_c56.py' -v

"$PYTHON_BIN" "$PROJECT_DIR/code/c56_hash_manifest.py" --write \
  --manifest "$STAGED_MANIFEST" \
  --certificate "$STAGED_CERT" \
  --schema-file "$STAGED_SCHEMA" \
  --check-report "$STAGED_CHECK"

LIVE_CERT="$RESULTS_DIR/c56_certificate.json"
LIVE_SCHEMA="$RESULTS_DIR/c56_schema.json"
LIVE_CHECK="$RESULTS_DIR/c56_check_report.json"
LIVE_MANIFEST="$RESULTS_DIR/scoped_hash_manifest.json"

if [[ "$REFRESH" -eq 1 ]]; then
  "$PYTHON_BIN" "$PROJECT_DIR/code/c56_atomic_promote.py" \
    --result-dir "$RESULTS_DIR" \
    --source "$STAGED_CERT" --target c56_certificate.json \
    --source "$STAGED_SCHEMA" --target c56_schema.json \
    --source "$STAGED_CHECK" --target c56_check_report.json \
    --source "$STAGED_MANIFEST" --target scoped_hash_manifest.json
else
  for live in "$LIVE_CERT" "$LIVE_SCHEMA" "$LIVE_CHECK" "$LIVE_MANIFEST"; do
    if [[ ! -f "$live" || -L "$live" ]]; then
      echo "missing/nonregular live PREFREEZE artifact: $live" >&2
      exit 1
    fi
  done
fi

cmp "$STAGED_CERT" "$LIVE_CERT"
cmp "$STAGED_SCHEMA" "$LIVE_SCHEMA"
cmp "$STAGED_CHECK" "$LIVE_CHECK"
cmp "$STAGED_MANIFEST" "$LIVE_MANIFEST"

cleanup_stage
STAGE_DIR=""
"$PYTHON_BIN" "$PROJECT_DIR/code/c56_hash_manifest.py"

if [[ "$REFRESH" -eq 1 ]]; then
  echo "running live post-promotion default replay"
  exec "$0"
fi

echo "HCS-C56 live default replay PASS (PREFREEZE code/results; no release promotion)"
