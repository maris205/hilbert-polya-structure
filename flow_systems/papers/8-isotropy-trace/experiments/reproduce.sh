#!/usr/bin/env bash
set -euo pipefail

export LC_ALL=C
export PYTHONDONTWRITEBYTECODE=1

paper_dir=$(cd "$(dirname "$0")/.." && pwd)
result_dir="$paper_dir/results"
code_dir="$paper_dir/code"
reproduction_root=$(mktemp -d "${TMPDIR:-/tmp}/paper8-isotropy-trace.XXXXXX")
reproduction_one="$reproduction_root/one"
reproduction_two="$reproduction_root/two"
mkdir -p "$reproduction_one" "$reproduction_two"
trap 'rm -rf "$reproduction_root"' EXIT

cd "$code_dir"
python3 -m unittest -v test_isotropy_trace_controls.py
python3 isotropy_trace_controls.py --output-dir "$result_dir"
python3 isotropy_trace_controls.py --output-dir "$result_dir" --verify-only

python3 isotropy_trace_controls.py --output-dir "$reproduction_one"
python3 isotropy_trace_controls.py --output-dir "$reproduction_two"

for artifact in \
  shifted_poisson_convention.csv \
  finite_character_grid.csv \
  nontrivial_character_phase.csv \
  trace_scale_controls.csv \
  rank_one_corner_peaks.csv \
  linfinity_representatives.csv \
  clock_copy_composite_controls.csv \
  transverse_probability_controls.csv \
  domain_boundary_controls.csv \
  isotropy_trace_manifest.json
do
  cmp "$result_dir/$artifact" "$reproduction_one/$artifact"
  cmp "$reproduction_one/$artifact" "$reproduction_two/$artifact"
done

sha256sum "$result_dir/isotropy_trace_manifest.json"
echo "PASS: tests, hash verification, and two byte-identical fresh generations"
