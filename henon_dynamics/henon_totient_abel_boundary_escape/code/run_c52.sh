#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

python -B "$project_dir/code/c52_abel_escape.py" \
  --output "$project_dir/results/c52_certificate.json" \
  --max-index 72
python -B "$project_dir/code/independent_check.py" \
  --certificate "$project_dir/results/c52_certificate.json" \
  --output "$project_dir/results/c52_independent_check.json"
python -B -m unittest discover -s "$project_dir/code" -p 'test_c52.py' -v
