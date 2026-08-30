#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR=$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

cd "${PROJECT_DIR}"

# The validator performs two isolated Round-8 builds and compares both with
# the canonical 2,241-row replay.  No --refresh path is exposed here.
python3 code/stage4_reproducibility_lock.py --replay-round8

# Run all historical unit tests plus the direct lock-tamper regressions.  Use
# the source directory as the import root so it cannot collide with Python's
# standard-library ``code`` module.
cd "${PROJECT_DIR}/code"
python3 -m unittest -v \
  test_round2_three_disk_ledger.py \
  test_round3_return_map_validation.py \
  test_round4_conditioning_audit.py \
  test_round5_universal_half_density.py \
  test_round6_symbolic_zeta_calibrator.py \
  test_round7_q_symbolic_family.py \
  test_round8_roof_nontransfer.py \
  test_stage4_reproducibility_lock.py
