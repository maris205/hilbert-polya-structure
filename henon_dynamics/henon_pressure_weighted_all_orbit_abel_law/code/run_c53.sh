#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

python -B "$PROJECT_DIR/code/c53_all_orbit_abel.py" --max-index 72
python -B "$PROJECT_DIR/code/independent_check.py"
python -B -m unittest discover -s "$PROJECT_DIR/code" -p 'test_c53.py' -v
