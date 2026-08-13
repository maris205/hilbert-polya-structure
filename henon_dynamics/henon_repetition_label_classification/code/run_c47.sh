#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
python "$here/code/c47_label_classifier.py" --output "$here/results/c47_certificate.json"
PYTHONPATH="$here/code" python -m unittest discover -s "$here/code" -p 'test_c47.py' -v
