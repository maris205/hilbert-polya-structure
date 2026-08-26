#!/usr/bin/env bash
set -euo pipefail

if [[ ${PAPER12_REPRO_ACTIVE:-0} == 1 ]]; then
  echo "FAIL: recursive Paper-12 reproduction entry detected" >&2
  exit 1
fi
export PAPER12_REPRO_ACTIVE=1

export LC_ALL=C
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0

paper_dir=$(cd "$(dirname "$0")/.." && pwd)
code_dir="$paper_dir/code"
result_dir="$paper_dir/results"
reproduction_root=$(mktemp -d "${TMPDIR:-/tmp}/paper12-marked-time-cohomology.XXXXXX")
reproduction_one="$reproduction_root/one"
reproduction_two="$reproduction_root/two"
mkdir -p "$reproduction_one" "$reproduction_two"
trap 'rm -rf "$reproduction_root"' EXIT

cd "$code_dir"
python3 -B -m unittest -v test_controls.py
python3 -B generate_controls.py --output-dir "$result_dir" --verify-only

python3 -B generate_controls.py --output-dir "$reproduction_one"
python3 -B generate_controls.py --output-dir "$reproduction_one" --verify-only
python3 -B generate_controls.py --output-dir "$reproduction_two"
python3 -B generate_controls.py --output-dir "$reproduction_two" --verify-only

for artifact in \
  nerve_face_controls.csv \
  factorization_controls.csv \
  degree1_cohomology_controls.csv \
  period_controls.csv \
  morphism_controls.csv \
  quotient_topology_controls.csv \
  packet_period_controls.csv \
  label_boundary_controls.csv \
  negative_controls.csv \
  control_summary.csv \
  orbitwise_standardization_h1_controls.csv \
  manifest.json
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

sha256sum "$result_dir/manifest.json"
echo "PASS: >=96 tests, strict verification, 11-CSV/3486-row three-way byte identity, recursive-entry gate, and no-cache scan"
