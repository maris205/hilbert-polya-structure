#!/usr/bin/env bash
set -euo pipefail
python -B code/c41_cm_checker.py
python -B -m unittest code/test_c41.py
