#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
python "$here/code/c46_integral_monodromy.py" --max-period 10 --output "$here/results/c46_certificate.json"
PYTHONPATH="$here/code" python -m unittest discover -s "$here/code" -p 'test_c46.py' -v
