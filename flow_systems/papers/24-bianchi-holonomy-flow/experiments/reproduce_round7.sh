#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR=$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
TMP_ONE=$(mktemp -d "${TMPDIR:-/tmp}/p24-round7-one.XXXXXX")
TMP_TWO=$(mktemp -d "${TMPDIR:-/tmp}/p24-round7-two.XXXXXX")
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
  python3 code/round7_trace_discriminant.py --refresh
fi
python3 code/test_round7_trace_discriminant.py -v
python3 code/round7_trace_discriminant.py --refresh --output-root "${TMP_ONE}"
python3 code/round7_trace_discriminant.py --refresh --output-root "${TMP_TWO}"
diff -ru "${TMP_ONE}" "${TMP_TWO}"
python3 code/round7_trace_discriminant.py
