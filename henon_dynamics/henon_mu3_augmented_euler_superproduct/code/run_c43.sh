#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON:-python3}"

REFRESH_MANIFEST=0
if [[ "${1:-}" == "--refresh-manifest" ]]; then
  REFRESH_MANIFEST=1
elif [[ $# -ne 0 ]]; then
  echo "usage: $0 [--refresh-manifest]" >&2
  exit 2
fi

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

"$PYTHON_BIN" "$PROJECT_DIR/code/c43_producer.py" --output "$TMP_DIR/c43_certificate.json"
cmp "$TMP_DIR/c43_certificate.json" "$PROJECT_DIR/results/c43_certificate.json"

"$PYTHON_BIN" "$PROJECT_DIR/code/c43_checker.py" \
  "$PROJECT_DIR/results/c43_certificate.json" \
  --output "$TMP_DIR/independent_check.json"
cmp "$TMP_DIR/independent_check.json" "$PROJECT_DIR/results/independent_check.json"

"$PYTHON_BIN" -m unittest discover -s "$PROJECT_DIR/code" -p 'test_c43.py'
if [[ "$REFRESH_MANIFEST" -eq 1 ]]; then
  "$PYTHON_BIN" "$PROJECT_DIR/code/c43_hash_manifest.py" --write
else
  "$PYTHON_BIN" "$PROJECT_DIR/code/c43_hash_manifest.py"
fi
