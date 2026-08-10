#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

python "$project_dir/code/c27_producer.py" --bridge-max-length 12 --power-window 24
python "$project_dir/code/c27_independent_check.py"
python -m unittest discover -s "$project_dir/code" -p 'test_c27.py' -v
python "$project_dir/code/c27_hash_manifest.py"
