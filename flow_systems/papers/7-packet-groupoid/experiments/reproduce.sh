#!/usr/bin/env bash
set -euo pipefail

export LC_ALL=C
export PYTHONDONTWRITEBYTECODE=1

paper_dir=$(cd "$(dirname "$0")/.." && pwd)
result_dir="$paper_dir/results"
code_dir="$paper_dir/code"
reproduction_root=$(mktemp -d "${TMPDIR:-/tmp}/paper7-packet-trace.XXXXXX")
reproduction_one="$reproduction_root/one"
reproduction_two="$reproduction_root/two"
mkdir -p "$reproduction_one" "$reproduction_two"
trap 'rm -rf "$reproduction_root"' EXIT

cd "$code_dir"
python3 -m unittest -v test_packet_trace_controls.py
python3 packet_trace_controls.py \
  --output-dir "$result_dir" \
  --max-prime 5000
python3 packet_trace_controls.py \
  --output-dir "$result_dir" \
  --verify-only

python3 packet_trace_controls.py \
  --output-dir "$reproduction_one" \
  --max-prime 5000
python3 packet_trace_controls.py \
  --output-dir "$reproduction_two" \
  --max-prime 5000

for artifact in \
  poisson_convention.csv \
  trace_norm_riemann.csv \
  prime_power_von_mangoldt.csv \
  finite_prime_d_z_ledger.csv \
  mass_copy_controls.csv \
  probability_base_blindness.csv \
  clock_compiler_controls.csv \
  hilbert_vs_tau_projection.csv \
  zero_time_partial_divergence.csv \
  packet_trace_manifest.json
do
  cmp "$result_dir/$artifact" "$reproduction_one/$artifact"
  cmp "$reproduction_one/$artifact" "$reproduction_two/$artifact"
done

sha256sum "$result_dir/packet_trace_manifest.json"
echo "PASS: tests, implementation verification, and two independent byte-for-byte regenerations"
