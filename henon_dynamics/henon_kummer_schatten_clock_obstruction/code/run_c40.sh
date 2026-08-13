#!/usr/bin/env bash
set -euo pipefail
python -B code/c40_schatten_checker.py
python -B -m unittest code/test_c40.py
