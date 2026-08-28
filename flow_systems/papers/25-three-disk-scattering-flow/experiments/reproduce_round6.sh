#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR=$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
TMP_ONE=$(mktemp -d "${TMPDIR:-/tmp}/p25-round6-one.XXXXXX")
TMP_TWO=$(mktemp -d "${TMPDIR:-/tmp}/p25-round6-two.XXXXXX")
trap 'rm -rf -- "${TMP_ONE}" "${TMP_TWO}"' EXIT

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

cd "${PROJECT_DIR}"
python3 code/test_round6_symbolic_zeta_calibrator.py -v
python3 code/round6_symbolic_zeta_calibrator.py --output-root "${TMP_ONE}"
python3 code/round6_symbolic_zeta_calibrator.py --output-root "${TMP_TWO}"
diff -ru "${TMP_ONE}" "${TMP_TWO}"
python3 code/round6_symbolic_zeta_calibrator.py --verify-existing
