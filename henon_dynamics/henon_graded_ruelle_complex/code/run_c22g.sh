#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_dir"

python code/c22g_producer.py --output results/c22g_certificate.json
python code/c22g_independent_check.py \
  results/c22g_certificate.json \
  --output results/c22g_independent_check.json
python -m unittest discover -s code -p 'test_c22g.py' -v
