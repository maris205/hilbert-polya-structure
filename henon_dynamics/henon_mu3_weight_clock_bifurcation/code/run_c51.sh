#!/usr/bin/env bash
set -euo pipefail

export PYTHONDONTWRITEBYTECODE=1
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON:-python3}"
REFRESH_RESULTS=0
REFRESH_MANIFEST=0

for argument in "$@"; do
  case "$argument" in
    --refresh-results) REFRESH_RESULTS=1 ;;
    --refresh-manifest) REFRESH_MANIFEST=1 ;;
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
TMP_CERT="$TMP_DIR/c51_certificate.json"
TMP_CHECK="$TMP_DIR/independent_check.json"
TMP_MANIFEST="$TMP_DIR/ARTIFACT_HASHES.sha256"

"$PYTHON_BIN" "$PROJECT_DIR/code/c51_producer.py" --output "$TMP_CERT"
"$PYTHON_BIN" "$PROJECT_DIR/code/c51_checker.py" "$TMP_CERT" --output "$TMP_CHECK"
C51_CERTIFICATE="$TMP_CERT" "$PYTHON_BIN" -m unittest discover \
  -s "$PROJECT_DIR/code" -p 'test_c51.py'

if [[ "$REFRESH_RESULTS" -eq 1 ]]; then
  "$PYTHON_BIN" "$PROJECT_DIR/code/c51_hash_manifest.py" --write \
    --manifest "$TMP_MANIFEST" --certificate "$TMP_CERT" --check "$TMP_CHECK"
  "$PYTHON_BIN" "$PROJECT_DIR/code/c51_hash_manifest.py" \
    --manifest "$TMP_MANIFEST" --certificate "$TMP_CERT" --check "$TMP_CHECK"

  "$PYTHON_BIN" "$PROJECT_DIR/code/c51_atomic_promote.py" \
    --source "$TMP_CERT" --target "$PROJECT_DIR/results/c51_certificate.json" \
    --source "$TMP_CHECK" --target "$PROJECT_DIR/results/independent_check.json" \
    --source "$TMP_MANIFEST" --target "$PROJECT_DIR/results/ARTIFACT_HASHES.sha256"

  cmp "$TMP_CERT" "$PROJECT_DIR/results/c51_certificate.json"
  "$PYTHON_BIN" "$PROJECT_DIR/code/c51_checker.py" \
    "$PROJECT_DIR/results/c51_certificate.json" --output "$TMP_DIR/live_check.json"
  cmp "$TMP_DIR/live_check.json" "$PROJECT_DIR/results/independent_check.json"
  "$PYTHON_BIN" "$PROJECT_DIR/code/c51_hash_manifest.py"
else
  cmp "$TMP_CERT" "$PROJECT_DIR/results/c51_certificate.json"
  cmp "$TMP_CHECK" "$PROJECT_DIR/results/independent_check.json"
  if [[ "$REFRESH_MANIFEST" -eq 1 ]]; then
    "$PYTHON_BIN" "$PROJECT_DIR/code/c51_hash_manifest.py" --write
  else
    "$PYTHON_BIN" "$PROJECT_DIR/code/c51_hash_manifest.py"
  fi
fi
