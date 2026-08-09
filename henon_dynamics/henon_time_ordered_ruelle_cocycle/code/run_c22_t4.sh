#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_dir"

python code/c22_t4_producer.py
python code/c22_t4_independent_check.py
pytest -q code/test_c22_t4.py
