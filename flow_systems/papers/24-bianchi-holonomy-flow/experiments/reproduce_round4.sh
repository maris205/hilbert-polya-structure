#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP_ONE="$(mktemp -d)"
TMP_TWO="$(mktemp -d)"
trap 'rm -rf "${TMP_ONE}" "${TMP_TWO}"' EXIT

cd "${PROJECT_DIR}"
export PYTHONDONTWRITEBYTECODE=1

python3 code/test_round4_finite_volume_control.py -v
python3 code/round4_finite_volume_control.py --output-root "${TMP_ONE}"
python3 code/round4_finite_volume_control.py --output-root "${TMP_TWO}"
diff -qr "${TMP_ONE}" "${TMP_TWO}"
python3 code/round4_finite_volume_control.py --verify-existing
