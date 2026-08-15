#!/usr/bin/env bash
set -euo pipefail

export PYTHONDONTWRITEBYTECODE=1
if [[ -n "${PYTHONOPTIMIZE:-}" && "${PYTHONOPTIMIZE}" != "0" ]]; then
  echo "PYTHONOPTIMIZE must be unset or zero for certificate replay" >&2
  exit 2
fi
unset PYTHONOPTIMIZE

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON:-python3}"
REFRESH_RESULTS=0
REFRESH_MANIFEST=0

for argument in "$@"; do
  case "$argument" in
    --refresh-results)
      [[ "$REFRESH_RESULTS" -eq 0 ]] || { echo "duplicate --refresh-results" >&2; exit 2; }
      REFRESH_RESULTS=1
      ;;
    --refresh-manifest)
      [[ "$REFRESH_MANIFEST" -eq 0 ]] || { echo "duplicate --refresh-manifest" >&2; exit 2; }
      REFRESH_MANIFEST=1
      ;;
    *)
      echo "usage: $0 [--refresh-results --refresh-manifest] [--refresh-manifest]" >&2
      exit 2
      ;;
  esac
done

if [[ "$REFRESH_RESULTS" -eq 1 && "$REFRESH_MANIFEST" -ne 1 ]]; then
  echo "--refresh-results requires --refresh-manifest" >&2
  exit 2
fi

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT
TMP_CERT="$TMP_DIR/c55_certificate.json"
TMP_CHECK="$TMP_DIR/independent_check.json"
TMP_SCOPED_MANIFEST="$TMP_DIR/CODE_RESULTS_HASHES.sha256"

"$PYTHON_BIN" "$PROJECT_DIR/code/c55_producer.py" --output "$TMP_CERT"
"$PYTHON_BIN" "$PROJECT_DIR/code/c55_checker.py" \
  "$TMP_CERT" --output "$TMP_CHECK"
C55_CERTIFICATE="$TMP_CERT" "$PYTHON_BIN" -m unittest discover \
  -s "$PROJECT_DIR/code" -p 'test_c55.py'

if [[ "$REFRESH_RESULTS" -eq 1 ]]; then
  "$PYTHON_BIN" "$PROJECT_DIR/code/c55_hash_manifest.py" --write --scoped-only \
    --scoped-manifest "$TMP_SCOPED_MANIFEST" \
    --certificate "$TMP_CERT" --check "$TMP_CHECK"
  "$PYTHON_BIN" "$PROJECT_DIR/code/c55_atomic_promote.py" \
    --source "$TMP_CERT" --target "$PROJECT_DIR/results/c55_certificate.json" \
    --source "$TMP_CHECK" --target "$PROJECT_DIR/results/independent_check.json" \
    --source "$TMP_SCOPED_MANIFEST" --target "$PROJECT_DIR/results/CODE_RESULTS_HASHES.sha256"
  cmp "$TMP_CERT" "$PROJECT_DIR/results/c55_certificate.json"
  cmp "$TMP_CHECK" "$PROJECT_DIR/results/independent_check.json"
  echo "running live post-refresh default replay"
  "$0"
elif [[ "$REFRESH_MANIFEST" -eq 1 ]]; then
  cmp "$TMP_CERT" "$PROJECT_DIR/results/c55_certificate.json"
  cmp "$TMP_CHECK" "$PROJECT_DIR/results/independent_check.json"
  "$PYTHON_BIN" "$PROJECT_DIR/code/c55_hash_manifest.py" --write --scoped-only \
    --scoped-manifest "$TMP_SCOPED_MANIFEST"
  "$PYTHON_BIN" "$PROJECT_DIR/code/c55_atomic_promote.py" \
    --source "$TMP_SCOPED_MANIFEST" --target "$PROJECT_DIR/results/CODE_RESULTS_HASHES.sha256"
  echo "running live post-refresh default replay"
  "$0"
else
  cmp "$TMP_CERT" "$PROJECT_DIR/results/c55_certificate.json"
  cmp "$TMP_CHECK" "$PROJECT_DIR/results/independent_check.json"
  "$PYTHON_BIN" "$PROJECT_DIR/code/c55_hash_manifest.py" --scoped-only
  echo "HCS-C55 live default replay PASS (persistent scoped identity verified; verify the current full manifest separately with c55_hash_manifest.py --full-only)"
fi
