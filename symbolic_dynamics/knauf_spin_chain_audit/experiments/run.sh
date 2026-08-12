#!/usr/bin/env bash
set -euo pipefail

EXPERIMENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CANDIDATE_DIR="$(cd "${EXPERIMENT_DIR}/.." && pwd)"
CODE_DIR="${CANDIDATE_DIR}/code"
RESULTS_DIR="${CANDIDATE_DIR}/results"
PROTOCOL="${EXPERIMENT_DIR}/locked_protocol.json"

{
  python -m pytest -q "${CODE_DIR}/test_knauf.py"
  PYTHONPATH="${CODE_DIR}${PYTHONPATH:+:${PYTHONPATH}}" \
    python "${CODE_DIR}/run_experiment.py" \
      --protocol "${PROTOCOL}" \
      --results-dir "${RESULTS_DIR}"
  python "${CODE_DIR}/analyze_results.py" --results-dir "${RESULTS_DIR}"
} 2>&1 | tee "${RESULTS_DIR}/run.log"
