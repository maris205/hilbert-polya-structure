#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

python -B "$project_dir/code/c51_abel_germ.py" \
  --output "$project_dir/results/c51_certificate.json"
python -B "$project_dir/code/independent_check.py" \
  --certificate "$project_dir/results/c51_certificate.json" \
  --output "$project_dir/results/c51_independent_check.json"
python -B -m unittest discover -s "$project_dir/code" -p 'test_c51.py' -v
