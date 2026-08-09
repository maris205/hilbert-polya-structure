#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_dir"

python code/c23_producer.py \
  --output results/c23_first_gate_certificate.json \
  --prime-bound 43 \
  --max-repetition 12
python code/c23_independent_check.py \
  results/c23_first_gate_certificate.json \
  --output results/c23_first_gate_independent_check.json
python -m unittest discover -s code -p 'test_c23.py' -v
