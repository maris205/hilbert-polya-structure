#!/usr/bin/env bash
set -euo pipefail

export LC_ALL=C
export PYTHONDONTWRITEBYTECODE=1

paper_dir=$(cd "$(dirname "$0")/.." && pwd)
result_dir="$paper_dir/results"
code_dir="$paper_dir/code"
reproduction_root=$(mktemp -d "${TMPDIR:-/tmp}/paper9-packet-separation.XXXXXX")
reproduction_one="$reproduction_root/one"
reproduction_two="$reproduction_root/two"
mkdir -p "$reproduction_one" "$reproduction_two"
trap 'rm -rf "$reproduction_root"' EXIT

cd "$code_dir"
python3 -m unittest -v test_packet_separation_controls.py
python3 packet_separation_controls.py --output-dir "$result_dir"
python3 packet_separation_controls.py --output-dir "$result_dir" --verify-only

python3 packet_separation_controls.py --output-dir "$reproduction_one"
python3 packet_separation_controls.py --output-dir "$reproduction_two"

for artifact in \
  simultaneous_approximation.csv \
  finite_cyclic_characters.csv \
  action_sign_controls.csv \
  pz_circle_controls.csv \
  unit_normalization_controls.csv \
  distinctness_controls.csv \
  illegal_kernel_proxy.csv \
  prime_uniformity_summary.csv \
  packet_separation_manifest.json
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

sha256sum "$result_dir/packet_separation_manifest.json"
echo "PASS: tests, verify-only, no-pycache, and two byte-identical fresh generations"
