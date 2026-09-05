#!/usr/bin/env bash
set -euo pipefail
review_dir="$(cd "$(dirname "$0")/.." && pwd)"
cd "$review_dir"
printf 'Replay 1 start: '
date -u '+%Y-%m-%d %H:%M:%S UTC'
python3 -B verify_independent.py | tee REPLAY1.txt
printf 'Replay 1 end: '
date -u '+%Y-%m-%d %H:%M:%S UTC'
printf 'Replay 2 start: '
date -u '+%Y-%m-%d %H:%M:%S UTC'
python3 -B verify_independent.py | tee REPLAY2.txt
printf 'Replay 2 end: '
date -u '+%Y-%m-%d %H:%M:%S UTC'
cmp REPLAY1.txt REPLAY2.txt
printf 'byte comparison: PASS\n'
sha256sum verify_independent.py REPLAY1.txt REPLAY2.txt
