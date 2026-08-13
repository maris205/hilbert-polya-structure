#!/usr/bin/env bash
set -euo pipefail
python -B code/c38_kummer_checker.py
python -B -m unittest code/test_c38.py
