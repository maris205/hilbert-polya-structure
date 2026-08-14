#!/usr/bin/env bash
set -euo pipefail

project_dir=$(cd "$(dirname "$0")/.." && pwd)
cd "$project_dir/code"
python3 -m unittest -v test_packet_trace_controls.py
python3 packet_trace_controls.py \
  --output-dir "$project_dir/results" \
  --max-prime 100000
