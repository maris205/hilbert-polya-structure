#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

python -B "$project_dir/code/c57_five_block_obstruction.py" --check
python -B "$project_dir/code/independent_check.py" --check
python -B -m unittest discover -s "$project_dir/code" -p 'test_c57.py' -v
