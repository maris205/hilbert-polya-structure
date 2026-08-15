#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1
project_dir="$(cd "$(dirname "$0")/.." && pwd)"
python3 -B "$project_dir/code/c63_height_flat_pressure.py" --output "$project_dir/results/c63_certificate.json"
python3 -B "$project_dir/code/independent_check.py"
python3 -B -m unittest discover -s "$project_dir/code" -p "test_c63.py" -v
python3 -B -O -m unittest discover -s "$project_dir/code" -p "test_c63.py" -v
