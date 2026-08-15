#!/usr/bin/env bash
set -euo pipefail
project_dir="$(cd "$(dirname "$0")/.." && pwd)"
python -B "$project_dir/code/c72_essential_ladder.py" --output "$project_dir/results/c72_certificate.json"
python -B "$project_dir/code/independent_check.py"
python -B "$project_dir/code/test_c72.py" -v
python -B -O "$project_dir/code/test_c72.py" -v
