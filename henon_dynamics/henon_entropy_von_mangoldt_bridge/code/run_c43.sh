#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
python "$here/code/c43_entropy_bridge.py" --max-period 32 --output "$here/results/c43_certificate.json"
PYTHONPATH="$here/code" python -m unittest discover -s "$here/code" -p 'test_c43.py' -v
