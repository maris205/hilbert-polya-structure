#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
python -B "$here/code/c48_pressure_labels.py" --output "$here/results/c48_certificate.json"
PYTHONPATH="$here/code" python -B -m unittest discover -s "$here/code" -p 'test_c48.py' -v
