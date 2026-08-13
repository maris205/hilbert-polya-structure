#!/usr/bin/env bash
set -euo pipefail

paper_dir=$(cd "$(dirname "$0")/.." && pwd)
cd "$paper_dir/code"

python3 -m unittest -v test_koopman_spectral_controls.py
python3 koopman_spectral_controls.py \
  --output-dir "$paper_dir/results" \
  --max-degree 24 \
  --witness-count 12

