#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python -m unittest discover -s "$project_dir/code" -p 'test_*.py' -v
python "$project_dir/code/run_gauss_experiment.py" \
  --config "$project_dir/experiments/frozen_config.json" \
  --output "$project_dir/results"
