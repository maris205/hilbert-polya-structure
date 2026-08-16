#!/usr/bin/env bash
set -euo pipefail
project_dir="$(cd "$(dirname "$0")/.." && pwd)"
python -B "$project_dir/code/c75_weighted_divisor.py" --output "$project_dir/results/c75_certificate.json"
python -B "$project_dir/code/independent_check.py"
python -B "$project_dir/code/test_c75.py" -v
python -B -O "$project_dir/code/test_c75.py" -v
