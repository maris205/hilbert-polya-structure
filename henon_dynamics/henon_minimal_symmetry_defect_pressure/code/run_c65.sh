#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1
p="$(cd "$(dirname "$0")/.." && pwd)"
python3 -B "$p/code/c65_symmetry_pressure.py" --output "$p/results/c65_certificate.json"
python3 -B "$p/code/independent_check.py"
python3 -B -m unittest discover -s "$p/code" -p 'test_c65.py' -v
python3 -B -O -m unittest discover -s "$p/code" -p 'test_c65.py' -v
