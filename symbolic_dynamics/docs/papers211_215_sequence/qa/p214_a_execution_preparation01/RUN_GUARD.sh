#!/bin/bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: RUN_GUARD.sh OUTPUT_DIRECTORY" >&2
  exit 64
fi

workspace=/root/autodl-tmp/symbolic_dynamics
review="$workspace/docs/papers211_215_sequence/reviews/p214_a"
output="$1"

case "$output" in
  "$workspace/docs/papers211_215_sequence/qa/p214_a_initial_run01"|\
  "$workspace/docs/papers211_215_sequence/qa/p214_a_strict_run01"|\
  "$workspace/docs/papers211_215_sequence/qa/p214_a_strict_run02") ;;
  *) echo "unapproved output directory: $output" >&2; exit 65 ;;
esac

test ! -e "$output"
cd "$workspace"
sha256sum -c "$review/INPUT_PINS.sha256"
test "$(sha256sum "$review/verify.py" | cut -d' ' -f1)" = \
  90c99adf8c3ee295815bff273c2711b6c43d9c9d0eaa6929a7c4beaaf52bd8cc
mkdir "$output"
printf '%s\n' \
  "python docs/papers211_215_sequence/reviews/p214_a/verify.py" > "$output/request.txt"
sha256sum "$review/verify.py" "$review/PARAMETERS.json" \
  "$review/OUTPUT_SCHEMA.md" "$review/INPUT_PINS.sha256" > "$output/keys.before.sha256"

set +e
python "$review/verify.py" > "$output/stdout.raw" 2> "$output/stderr.raw"
status=$?
set -e
printf '%s\n' "$status" > "$output/python.exit"
sha256sum "$review/verify.py" "$review/PARAMETERS.json" \
  "$review/OUTPUT_SCHEMA.md" "$review/INPUT_PINS.sha256" > "$output/keys.after.sha256"
cmp "$output/keys.before.sha256" "$output/keys.after.sha256"
test "$status" -eq 0
