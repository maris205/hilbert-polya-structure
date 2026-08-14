#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON:-python3}"
REFRESH_RESULTS=0; REFRESH_MANIFEST=0
for argument in "$@"; do
  case "$argument" in
    --refresh-results) REFRESH_RESULTS=1 ;;
    --refresh-manifest) REFRESH_MANIFEST=1 ;;
    *) echo "usage: $0 [--refresh-results --refresh-manifest] [--refresh-manifest]" >&2; exit 2 ;;
  esac
done
if [[ "$REFRESH_RESULTS" -eq 1 && "$REFRESH_MANIFEST" -ne 1 ]]; then
  echo "--refresh-results requires --refresh-manifest" >&2; exit 2
fi
TMP_DIR="$(mktemp -d)"; trap 'rm -rf "$TMP_DIR"' EXIT
"$PYTHON_BIN" "$PROJECT_DIR/code/c50_producer.py" --output "$TMP_DIR/c50_certificate.json"
"$PYTHON_BIN" "$PROJECT_DIR/code/c50_checker.py" "$TMP_DIR/c50_certificate.json" --output "$TMP_DIR/independent_check.json"
C50_CERTIFICATE="$TMP_DIR/c50_certificate.json" "$PYTHON_BIN" -m unittest discover -s "$PROJECT_DIR/code" -p 'test_c50.py'
if [[ "$REFRESH_RESULTS" -eq 1 ]]; then
  cp "$TMP_DIR/c50_certificate.json" "$PROJECT_DIR/results/.c50_certificate.json.new"
  cp "$TMP_DIR/independent_check.json" "$PROJECT_DIR/results/.independent_check.json.new"
  mv "$PROJECT_DIR/results/.c50_certificate.json.new" "$PROJECT_DIR/results/c50_certificate.json"
  mv "$PROJECT_DIR/results/.independent_check.json.new" "$PROJECT_DIR/results/independent_check.json"
else
  cmp "$TMP_DIR/c50_certificate.json" "$PROJECT_DIR/results/c50_certificate.json"
  cmp "$TMP_DIR/independent_check.json" "$PROJECT_DIR/results/independent_check.json"
fi
if [[ "$REFRESH_MANIFEST" -eq 1 ]]; then
  "$PYTHON_BIN" "$PROJECT_DIR/code/c50_hash_manifest.py" --write
else
  "$PYTHON_BIN" "$PROJECT_DIR/code/c50_hash_manifest.py"
fi
