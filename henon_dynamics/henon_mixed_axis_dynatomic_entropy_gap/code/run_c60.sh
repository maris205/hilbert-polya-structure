#!/usr/bin/env bash
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1
python -B code/c60_dynatomic_gap.py --output results/c60_certificate.json
python -B code/independent_check.py \
  --certificate results/c60_certificate.json \
  --output results/c60_independent_check.json
python -B -m unittest discover -s code -p 'test_c60.py' -v
