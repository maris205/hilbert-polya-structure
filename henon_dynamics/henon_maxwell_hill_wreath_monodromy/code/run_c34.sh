#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
c34_temp_dir="$(mktemp -d)"
trap 'rm -rf -- "$c34_temp_dir"' EXIT
c34_python=(python3 -I -B -X "pycache_prefix=$c34_temp_dir/pycache")

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

if [[ $refresh_manifest == false ]]; then
    "${c34_python[@]}" "$project_dir/code/c34_hash_manifest.py"
fi

"${c34_python[@]}" "$project_dir/code/c34_producer.py" \
    --output "$c34_temp_dir/c34_certificate.json"
"${c34_python[@]}" "$project_dir/code/c34_checker.py" \
    --certificate "$c34_temp_dir/c34_certificate.json" \
    --output "$c34_temp_dir/c34_independent_check.json"

C34_TEST_CERTIFICATE="$c34_temp_dir/c34_certificate.json" \
    "${c34_python[@]}" -m unittest discover \
    -s "$project_dir/code" -p 'test_c34.py' -v

if [[ $refresh_manifest == true ]]; then
    mv "$c34_temp_dir/c34_certificate.json" \
        "$project_dir/results/c34_certificate.json"
    mv "$c34_temp_dir/c34_independent_check.json" \
        "$project_dir/results/c34_independent_check.json"
    "${c34_python[@]}" "$project_dir/code/c34_hash_manifest.py" --write
else
    cmp "$c34_temp_dir/c34_certificate.json" \
        "$project_dir/results/c34_certificate.json"
    cmp "$c34_temp_dir/c34_independent_check.json" \
        "$project_dir/results/c34_independent_check.json"
fi

"${c34_python[@]}" "$project_dir/code/c34_hash_manifest.py"
