#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
paper_dir="$(cd "${script_dir}/.." && pwd)"

cd "${paper_dir}"
python3 -B code/test_trace_certificate_controls.py
python3 -B code/trace_certificate_controls.py --output-dir results
python3 -B code/trace_certificate_controls.py \
  --verify-manifest results/manifest.sha256
