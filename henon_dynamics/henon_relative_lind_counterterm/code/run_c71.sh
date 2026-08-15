#!/usr/bin/env bash
set -euo pipefail
PROJECT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT"
PYTHONDONTWRITEBYTECODE=1 python -B code/c71_relative_lind.py
PYTHONDONTWRITEBYTECODE=1 python -B code/independent_check.py
PYTHONDONTWRITEBYTECODE=1 python -B code/test_c71.py
PYTHONDONTWRITEBYTECODE=1 python -B -O code/test_c71.py
