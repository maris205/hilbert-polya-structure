#!/usr/bin/env bash
set -euo pipefail

export LC_ALL=C
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0

paper_dir=$(cd "$(dirname "$0")/.." && pwd)
result_dir="$paper_dir/results"
code_dir="$paper_dir/code"
reproduction_root=$(mktemp -d "${TMPDIR:-/tmp}/paper11-indiscrete-convolution.XXXXXX")
reproduction_one="$reproduction_root/one"
reproduction_two="$reproduction_root/two"
mkdir -p "$reproduction_one" "$reproduction_two"
trap 'rm -rf "$reproduction_root"' EXIT

cd "$code_dir"
python3 -B -m unittest -v test_indiscrete_convolution_controls.py
python3 -B indiscrete_convolution_controls.py --output-dir "$result_dir"
python3 -B indiscrete_convolution_controls.py --output-dir "$result_dir" --verify-only

python3 -B indiscrete_convolution_controls.py --output-dir "$reproduction_one"
python3 -B indiscrete_convolution_controls.py --output-dir "$reproduction_one" --verify-only
python3 -B indiscrete_convolution_controls.py --output-dir "$reproduction_two"
python3 -B indiscrete_convolution_controls.py --output-dir "$reproduction_two" --verify-only

for artifact in \
  arrow_topology_controls.csv \
  t0_time_factorization_controls.csv \
  measurable_time_factorization_controls.csv \
  support_projection_controls.csv \
  convolution_controls.csv \
  involution_controls.csv \
  convention_negative_controls.csv \
  unit_regular_controls.csv \
  hopen_zero_controls.csv \
  proxy_strictness_controls.csv \
  action_blind_controls.csv \
  label_period_independence_controls.csv \
  indiscrete_convolution_controls_manifest.json
do
  cmp "$result_dir/$artifact" "$reproduction_one/$artifact"
  cmp "$reproduction_one/$artifact" "$reproduction_two/$artifact"
done

if find "$code_dir" "$paper_dir/experiments" "$result_dir" \
  \( -type d -name __pycache__ -o -type f \( -name '*.pyc' -o -name '*.pyo' \) \) \
  -print -quit | grep -q .
then
  echo "FAIL: forbidden Python bytecode/cache artifact found" >&2
  exit 1
fi

sha256sum "$result_dir/indiscrete_convolution_controls_manifest.json"
echo "PASS: tests, strict verify-only, checked-in/fresh byte identity, and forbidden-artifact scan"
