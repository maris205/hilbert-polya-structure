#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
python "$here/code/c45_pressure_clock.py" --output "$here/results/c45_certificate.json"
PYTHONPATH="$here/code" python -m unittest discover -s "$here/code" -p 'test_c45.py' -v
