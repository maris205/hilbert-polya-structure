#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR=$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
TMP_ONE=$(mktemp -d "${TMPDIR:-/tmp}/p24-stage4-lox-one.XXXXXX")
TMP_TWO=$(mktemp -d "${TMPDIR:-/tmp}/p24-stage4-lox-two.XXXXXX")
trap 'rm -rf -- "${TMP_ONE}" "${TMP_TWO}"' EXIT

if [[ $# -gt 1 ]] || [[ $# -eq 1 && $1 != "--refresh" ]]; then
  echo "usage: $0 [--refresh]" >&2
  exit 2
fi

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

cd "${PROJECT_DIR}"
if [[ $# -eq 1 ]]; then
  python3 code/stage4_loxodromic_profile.py --refresh
fi
python3 code/test_stage4_loxodromic_profile.py -v
python3 code/stage4_loxodromic_profile.py --refresh --output-root "${TMP_ONE}"
python3 code/stage4_loxodromic_profile.py --refresh --output-root "${TMP_TWO}"
diff -ru "${TMP_ONE}" "${TMP_TWO}"
python3 code/stage4_loxodromic_profile.py --verify-existing
python3 code/round7_trace_discriminant.py --verify-existing
python3 code/round8_congruence_specificity.py --verify-existing
