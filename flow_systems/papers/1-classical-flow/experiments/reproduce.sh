#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RESULT_DIR="${PROJECT_DIR}/results"

python3 "${PROJECT_DIR}/code/test_modular_orbits.py"
python3 "${PROJECT_DIR}/code/modular_orbits.py" enumerate \
  --max-blocks 16 \
  --output-dir "${RESULT_DIR}"
python3 "${PROJECT_DIR}/code/modular_orbits.py" audit \
  --ledger "${RESULT_DIR}/modular_orbit_ledger.csv" \
  --manifest "${RESULT_DIR}/orbit_ledger_manifest.json" \
  --repeat-max 5 \
  --trace-scan-max 5000 \
  --output-dir "${RESULT_DIR}"
