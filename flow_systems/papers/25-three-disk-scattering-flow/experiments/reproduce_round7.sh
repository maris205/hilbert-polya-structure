#!/usr/bin/env bash
set -euo pipefail

MODE=${1:-verify}
if [[ "${MODE}" != "verify" && "${MODE}" != "--refresh" ]]; then
  echo "usage: $0 [verify|--refresh]" >&2
  exit 2
fi

PROJECT_DIR=$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
TMP_ONE=$(mktemp -d "${TMPDIR:-/tmp}/p25-round7-one.XXXXXX")
TMP_TWO=$(mktemp -d "${TMPDIR:-/tmp}/p25-round7-two.XXXXXX")
trap 'rm -rf -- "${TMP_ONE}" "${TMP_TWO}"' EXIT

export LC_ALL=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1

cd "${PROJECT_DIR}"
python3 code/test_round7_q_symbolic_family.py -v
python3 code/round7_q_symbolic_family.py --output-root "${TMP_ONE}"
python3 code/round7_q_symbolic_family.py --output-root "${TMP_TWO}"
diff -ru "${TMP_ONE}" "${TMP_TWO}"

if [[ "${MODE}" == "--refresh" ]]; then
  python3 code/round7_q_symbolic_family.py --output-root "${PROJECT_DIR}"
else
  python3 code/round7_q_symbolic_family.py --verify-existing
fi
