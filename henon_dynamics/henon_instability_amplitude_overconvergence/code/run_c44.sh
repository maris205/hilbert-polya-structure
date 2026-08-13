#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
python "$here/code/c44_amplitude_gate.py" --prime-limit 1000000 --output "$here/results/c44_certificate.json"
PYTHONPATH="$here/code" python -m unittest discover -s "$here/code" -p 'test_c44.py' -v
