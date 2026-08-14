#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python_bin="${PYTHON:-python}"

PYTHONDONTWRITEBYTECODE=1 "$python_bin" -B "$project_dir/code/c55_galois_blocks.py" --check
PYTHONDONTWRITEBYTECODE=1 "$python_bin" -B "$project_dir/code/independent_check.py" --check
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$project_dir/code" \
  "$python_bin" -B -m unittest discover -s "$project_dir/code" -p 'test_c55.py' -v
