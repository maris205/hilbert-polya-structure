#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1
project_dir="$(cd "$(dirname "$0")/.." && pwd)"
python3 -B "$project_dir/code/c73_full_ladder_counterterm.py" --output "$project_dir/results/c73_certificate.json"
python3 -B "$project_dir/code/independent_check.py"
python3 -B -m unittest discover -s "$project_dir/code" -p 'test_c73.py' -v
python3 -B -O -m unittest discover -s "$project_dir/code" -p 'test_c73.py' -v
