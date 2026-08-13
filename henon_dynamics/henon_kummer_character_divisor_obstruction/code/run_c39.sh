#!/usr/bin/env bash
set -euo pipefail
python -B code/c39_character_checker.py
python -B -m unittest code/test_c39.py
