#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python "$project_dir/code/c24_producer.py"
python "$project_dir/code/c24_independent_check.py"
python -m unittest discover -s "$project_dir/code" -p 'test_c24.py' -v
