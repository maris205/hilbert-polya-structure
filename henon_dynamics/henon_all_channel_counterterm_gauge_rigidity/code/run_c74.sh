#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_DIR"

python3 code/c74_gauge_rigidity.py
python3 code/independent_check.py
python3 -m unittest discover -s code -p 'test_c74.py' -v
python3 -O -m unittest discover -s code -p 'test_c74.py' -v

sha256sum \
  results/c74_certificate.json \
  results/c74_independent_check.json \
  paper/paper.pdf \
  PROOF_PACKAGE.md \
  > results/SHA256SUMS

echo '{"candidate_id":"HCS-P74","normal_tests":true,"optimized_tests":true,"independent_check":true,"check":true}'
