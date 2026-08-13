#!/usr/bin/env bash
set -euo pipefail

project_dir=$(cd "$(dirname "$0")/.." && pwd)
cd "$project_dir/code"

python3 -m unittest -v test_frobenius_suspension_controls.py
python3 frobenius_suspension_controls.py \
  --output-dir "$project_dir/results" \
  --max-degree 12

