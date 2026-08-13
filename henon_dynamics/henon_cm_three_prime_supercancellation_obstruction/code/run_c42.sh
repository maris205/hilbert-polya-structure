#!/usr/bin/env bash
set -euo pipefail
python -B code/c42_rigidity_checker.py
python -B -m unittest code/test_c42.py
