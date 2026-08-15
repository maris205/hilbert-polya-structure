#!/usr/bin/env bash
set -euo pipefail
PROJECT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT"
PYTHONDONTWRITEBYTECODE=1 python -B code/c70_orbit_euler.py
PYTHONDONTWRITEBYTECODE=1 python -B code/independent_check.py
PYTHONDONTWRITEBYTECODE=1 python -B code/test_c70.py
PYTHONDONTWRITEBYTECODE=1 python -B -O code/test_c70.py
