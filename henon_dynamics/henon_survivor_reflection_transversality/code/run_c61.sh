#!/usr/bin/env bash
set -euo pipefail
project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHONDONTWRITEBYTECODE=1 python -B "$project_dir/code/c61_transversality.py"
PYTHONDONTWRITEBYTECODE=1 python -B "$project_dir/code/independent_check.py"
PYTHONDONTWRITEBYTECODE=1 python -B -m unittest discover -s "$project_dir/code" -p 'test_c61.py' -v
