#!/usr/bin/env bash
set -euo pipefail

export LC_ALL=C
export PYTHONDONTWRITEBYTECODE=1

paper_dir=$(cd "$(dirname "$0")/.." && pwd)
result_dir="$paper_dir/results"
code_dir="$paper_dir/code"
reproduction_root=$(mktemp -d "${TMPDIR:-/tmp}/paper10-separated-reflection.XXXXXX")
reproduction_one="$reproduction_root/one"
reproduction_two="$reproduction_root/two"
mkdir -p "$reproduction_one" "$reproduction_two"
trap 'rm -rf "$reproduction_root"' EXIT

cd "$code_dir"
python3 -m unittest -v test_separated_reflection_controls.py
python3 separated_reflection_controls.py --output-dir "$result_dir"
python3 separated_reflection_controls.py --output-dir "$result_dir" --verify-only

python3 separated_reflection_controls.py --output-dir "$reproduction_one"
python3 separated_reflection_controls.py --output-dir "$reproduction_two"

for artifact in \
  continuous_map_controls.csv \
  measurable_map_controls.csv \
  dirac_collapse_controls.csv \
  indiscrete_group_characters.csv \
  proxy_direction_controls.csv \
  coproduct_k0_controls.csv \
  component_mass_controls.csv \
  ell1_gate_controls.csv \
  label_neutrality_controls.csv \
  external_log_label_controls.csv \
  separated_reflection_controls_manifest.json
do
  cmp "$result_dir/$artifact" "$reproduction_one/$artifact"
  cmp "$reproduction_one/$artifact" "$reproduction_two/$artifact"
done

if find "$code_dir" "$paper_dir/experiments" "$result_dir" \
  \( -type d -name __pycache__ -o -type f -name '*.pyc' \) -print -quit \
  | grep -q .
then
  echo "FAIL: Python bytecode/cache artifact found" >&2
  exit 1
fi

sha256sum "$result_dir/separated_reflection_controls_manifest.json"
echo "PASS: tests, verify-only, no-pycache, and two byte-identical fresh generations"
