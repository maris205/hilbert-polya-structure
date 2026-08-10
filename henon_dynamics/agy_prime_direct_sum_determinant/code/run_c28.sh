#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1

refresh_manifest=false
if [[ $# -gt 1 ]]; then
    echo "usage: $0 [--refresh-manifest]" >&2
    exit 2
fi
if [[ $# -eq 1 ]]; then
    if [[ $1 != "--refresh-manifest" ]]; then
        echo "usage: $0 [--refresh-manifest]" >&2
        exit 2
    fi
    refresh_manifest=true
fi

python "$project_dir/code/c28_producer.py"
python "$project_dir/code/c28_independent_check.py"
python -m unittest discover -s "$project_dir/code" -p 'test_c28.py' -v

if [[ $refresh_manifest == true ]]; then
    python "$project_dir/code/c28_hash_manifest.py" --write
fi
python "$project_dir/code/c28_hash_manifest.py"
