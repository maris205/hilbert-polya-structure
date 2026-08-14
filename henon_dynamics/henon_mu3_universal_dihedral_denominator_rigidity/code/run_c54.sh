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
TMP_CERT="$TMP_DIR/c54_certificate.json"
TMP_CHECK="$TMP_DIR/independent_check.json"
TMP_SCOPED_MANIFEST="$TMP_DIR/CODE_RESULTS_HASHES.sha256"
TMP_FULL_MANIFEST="$TMP_DIR/ARTIFACT_HASHES.sha256"

"$PYTHON_BIN" "$PROJECT_DIR/code/c54_producer.py" --output "$TMP_CERT"
"$PYTHON_BIN" "$PROJECT_DIR/code/c54_checker.py" "$TMP_CERT" --output "$TMP_CHECK"
C54_CERTIFICATE="$TMP_CERT" "$PYTHON_BIN" -m unittest discover \
  -s "$PROJECT_DIR/code" -p 'test_c54.py'

cmp "$PROJECT_DIR/route_a_evaluation.yaml" \
  "$PROJECT_DIR/evaluations/route_a/HCS-C54/20260814T134920Z.yaml"
echo "verified Route-A root/archive byte identity"

if [[ "$REFRESH_RESULTS" -eq 1 ]]; then
  "$PYTHON_BIN" "$PROJECT_DIR/code/c54_hash_manifest.py" --write \
    --manifest "$TMP_FULL_MANIFEST" --scoped-manifest "$TMP_SCOPED_MANIFEST" \
    --certificate "$TMP_CERT" --check "$TMP_CHECK"
  "$PYTHON_BIN" "$PROJECT_DIR/code/c54_atomic_promote.py" \
    --source "$TMP_CERT" --target "$PROJECT_DIR/results/c54_certificate.json" \
    --source "$TMP_CHECK" --target "$PROJECT_DIR/results/independent_check.json" \
    --source "$TMP_SCOPED_MANIFEST" --target "$PROJECT_DIR/results/CODE_RESULTS_HASHES.sha256" \
    --source "$TMP_FULL_MANIFEST" --target "$PROJECT_DIR/results/ARTIFACT_HASHES.sha256"

  cmp "$TMP_CERT" "$PROJECT_DIR/results/c54_certificate.json"
  "$PYTHON_BIN" "$PROJECT_DIR/code/c54_checker.py" \
    "$PROJECT_DIR/results/c54_certificate.json" --output "$TMP_DIR/live_check.json"
  cmp "$TMP_DIR/live_check.json" "$PROJECT_DIR/results/independent_check.json"
  C54_CERTIFICATE="$PROJECT_DIR/results/c54_certificate.json" \
    "$PYTHON_BIN" -m unittest discover -s "$PROJECT_DIR/code" -p 'test_c54.py'
  "$PYTHON_BIN" "$PROJECT_DIR/code/c54_hash_manifest.py"
else
  cmp "$TMP_CERT" "$PROJECT_DIR/results/c54_certificate.json"
  cmp "$TMP_CHECK" "$PROJECT_DIR/results/independent_check.json"
  if [[ "$REFRESH_MANIFEST" -eq 1 ]]; then
    "$PYTHON_BIN" "$PROJECT_DIR/code/c54_hash_manifest.py" --write \
      --manifest "$TMP_FULL_MANIFEST" --scoped-manifest "$TMP_SCOPED_MANIFEST"
    "$PYTHON_BIN" "$PROJECT_DIR/code/c54_atomic_promote.py" \
      --source "$TMP_SCOPED_MANIFEST" --target "$PROJECT_DIR/results/CODE_RESULTS_HASHES.sha256" \
      --source "$TMP_FULL_MANIFEST" --target "$PROJECT_DIR/results/ARTIFACT_HASHES.sha256"
    "$PYTHON_BIN" "$PROJECT_DIR/code/c54_hash_manifest.py"
  else
    "$PYTHON_BIN" "$PROJECT_DIR/code/c54_hash_manifest.py"
  fi
fi
