#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
project_dir="$(cd "${script_dir}/.." && pwd)"
results_dir="${project_dir}/results"
export PYTHONDONTWRITEBYTECODE=1

refresh_manifest=false
if [[ "$#" -gt 1 ]]; then
  echo "usage: $0 [--refresh-manifest]" >&2
  exit 2
fi
if [[ "$#" -eq 1 ]]; then
  if [[ "$1" != "--refresh-manifest" ]]; then
    echo "unknown argument: $1" >&2
    exit 2
  fi
  refresh_manifest=true
fi

temp_dir="$(mktemp -d)"
cleanup() {
  if [[ -n "${temp_dir}" && "${temp_dir}" == /tmp/* ]]; then
    rm -rf -- "${temp_dir}"
  fi
}
trap cleanup EXIT

python "${script_dir}/c32_morse_gate_producer.py" \
  --output "${temp_dir}/c32_morse_gate_certificate.json"

if [[ ! -f "${results_dir}/c32_morse_gate_certificate.json" ]]; then
  echo "released certificate missing; run the producer explicitly during release preparation" >&2
  exit 2
fi

cmp "${temp_dir}/c32_morse_gate_certificate.json" \
  "${results_dir}/c32_morse_gate_certificate.json"

python "${script_dir}/c32_morse_gate_checker.py" \
  "${results_dir}/c32_morse_gate_certificate.json" \
  --output "${temp_dir}/c32_morse_gate_independent_check.json"

if [[ ! -f "${results_dir}/c32_morse_gate_independent_check.json" ]]; then
  echo "released independent check missing" >&2
  exit 2
fi

cmp "${temp_dir}/c32_morse_gate_independent_check.json" \
  "${results_dir}/c32_morse_gate_independent_check.json"

python -m unittest discover -s "${script_dir}" -p 'test_c32_morse_gate.py'

if [[ "${refresh_manifest}" == true ]]; then
  python "${script_dir}/c32_hash_manifest.py" --write
fi

python "${script_dir}/c32_hash_manifest.py"

echo "HCS-C32 Phase-3 exact replay PASS"
