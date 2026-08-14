#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

python -B "$project_dir/code/c56_incidence_ladder.py" --check --output "$project_dir/results/c56_certificate.json"
python -B "$project_dir/code/independent_check.py" --check --output "$project_dir/results/c56_independent_check.json"
python -B "$project_dir/code/test_c56.py"
