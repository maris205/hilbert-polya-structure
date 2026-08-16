#!/usr/bin/env bash
set -euo pipefail
project_dir="$(cd "$(dirname "$0")/.." && pwd)"
python -B "$project_dir/code/c76_natural_boundary.py" --output "$project_dir/results/c76_certificate.json"
python -B "$project_dir/code/independent_check.py"
python -B "$project_dir/code/test_c76.py" -v
python -B -O "$project_dir/code/test_c76.py" -v
