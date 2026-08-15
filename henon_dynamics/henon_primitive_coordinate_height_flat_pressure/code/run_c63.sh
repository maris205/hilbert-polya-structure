#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1
project_dir="$(cd "$(dirname "$0")/.." && pwd)"
python3 -B "$project_dir/code/c63_height_flat_pressure.py" --output "$project_dir/results/c63_certificate.json"
python3 -B "$project_dir/code/independent_check.py"
python3 -B -m unittest -v "$project_dir/code/test_c63.py"
python3 -B -O -m unittest -v "$project_dir/code/test_c63.py"
