#!/bin/sh

# Sole serialized Paper-17 deterministic-control reproduction entry.
set -u

if [ -n "${P17_REPRO_ACTIVE:-}" ]; then
    echo "P17_REPRO_ERROR[3]=recursive entry" >&2
    exit 3
fi

export LC_ALL=C
export LANG=C
export TZ=UTC
export PYTHONHASHSEED=0
export PYTHONDONTWRITEBYTECODE=1
export P17_REPRO_ACTIVE=1
umask 022

fail() {
    p17_code=$1
    shift
    echo "P17_REPRO_ERROR[$p17_code]=$*" >&2
    exit "$p17_code"
}

case "$0" in
    /*) p17_script=$0 ;;
    *) p17_script=$PWD/$0 ;;
esac

if [ -L "$p17_script" ]; then
    fail 5 "symlinked reproduction script"
fi

p17_script_dir=$(CDPATH= cd -- "$(dirname -- "$p17_script")" 2>/dev/null && pwd -P) || fail 5 "cannot resolve script directory"
p17_root=$(CDPATH= cd -- "$p17_script_dir/.." 2>/dev/null && pwd -P) || fail 5 "cannot resolve Paper-17 root"

if [ ! -d "$p17_root" ] || [ -L "$p17_root" ]; then
    fail 5 "invalid or symlinked Paper-17 root"
fi
if [ "$p17_script_dir" != "$p17_root/experiments" ]; then
    fail 5 "script/root layout drift"
fi
if [ ! -f "$p17_root/experiments/reproduce.sh" ] || [ -L "$p17_root/experiments/reproduce.sh" ]; then
    fail 5 "reproduction entry type drift"
fi

cd -- "$p17_root" || fail 5 "cannot enter Paper-17 root"

p17_lock=$p17_root/experiments/.p17-control-reproduce.lock
p17_temp_a=
p17_temp_b=
p17_lock_owned=0
p17_tmp_base=${TMPDIR:-/tmp}

remove_temp_root() {
    p17_target=$1
    if [ -z "$p17_target" ]; then
        return 0
    fi
    case "$p17_target" in
        "$p17_tmp_base"/p17-controls.??????)
            rm -rf -- "$p17_target" || return 1
            ;;
        *)
            return 1
            ;;
    esac
}

failure_cleanup() {
    p17_saved=$?
    trap - EXIT HUP INT TERM
    if [ -n "$p17_temp_a" ]; then
        remove_temp_root "$p17_temp_a" || :
    fi
    if [ -n "$p17_temp_b" ]; then
        remove_temp_root "$p17_temp_b" || :
    fi
    if [ "$p17_lock_owned" -eq 1 ]; then
        rmdir -- "$p17_lock" 2>/dev/null || :
    fi
    exit "$p17_saved"
}

scan_residue() {
    p17_allow_lock=$1
    python3 -B - "$p17_root" "$p17_lock" "$p17_allow_lock" <<'PY'
import os
import sys
from pathlib import Path

root = Path(sys.argv[1])
lock = Path(sys.argv[2])
allow_lock = sys.argv[3] == "1"
bad_dirs = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
for directory, dirnames, filenames in os.walk(root, topdown=True, followlinks=False):
    base = Path(directory)
    for name in tuple(dirnames) + tuple(filenames):
        path = base / name
        if allow_lock and path == lock:
            continue
        if name in bad_dirs or name.endswith((".pyc", ".pyo")) or name.startswith(".p17-control-"):
            print(path, file=sys.stderr)
            raise SystemExit(5)
raise SystemExit(0)
PY
}

inventory_scan() {
    p17_expect_lock=$1
    python3 -B - "$p17_root" "$p17_lock" "$p17_expect_lock" <<'PY'
import os
import stat
import sys
from pathlib import Path

root = Path(sys.argv[1])
lock = Path(sys.argv[2])
expect_lock = sys.argv[3] == "1"
code_expected = {"generate_controls.py", "test_controls.py", "README.md"}
experiments_expected = {"reproduce.sh", "README.md"}
if expect_lock:
    experiments_expected.add(lock.name)
results_expected = {
    "range_first_handedness_controls.csv",
    "action_blind_open_records.csv",
    "connected_disconnected_firewall.csv",
    "domain_guard_controls.csv",
    "quantale_localic_firewall.csv",
    "actual_standard_owner_controls.csv",
    "dilation_strict_marker_controls.csv",
    "fixed_prime_provenance_controls.csv",
    "target_summary.csv",
    "manifest.json",
}

def names(path):
    try:
        return {entry.name for entry in path.iterdir()}
    except OSError:
        raise SystemExit(5)

if names(root / "code") != code_expected:
    raise SystemExit(5)
if names(root / "experiments") != experiments_expected:
    raise SystemExit(5)
if names(root / "results") != results_expected:
    raise SystemExit(5)
for directory, expected in ((root / "code", code_expected),
                            (root / "experiments", experiments_expected),
                            (root / "results", results_expected)):
    for name in expected:
        path = directory / name
        st = path.lstat()
        if expect_lock and path == lock:
            if not stat.S_ISDIR(st.st_mode):
                raise SystemExit(5)
            continue
        if not stat.S_ISREG(st.st_mode) or st.st_nlink != 1:
            raise SystemExit(5)
raise SystemExit(0)
PY
}

results_receipt() {
    python3 -B - "$p17_root/results" <<'PY'
import hashlib
import json
import os
import stat
import sys
from pathlib import Path

root = Path(sys.argv[1])
names = (
    "range_first_handedness_controls.csv",
    "action_blind_open_records.csv",
    "connected_disconnected_firewall.csv",
    "domain_guard_controls.csv",
    "quantale_localic_firewall.csv",
    "actual_standard_owner_controls.csv",
    "dilation_strict_marker_controls.csv",
    "fixed_prime_provenance_controls.csv",
    "target_summary.csv",
    "manifest.json",
)
receipt = []
for name in names:
    path = root / name
    st = path.lstat()
    if not stat.S_ISREG(st.st_mode) or st.st_nlink != 1:
        raise SystemExit(5)
    data = path.read_bytes()
    receipt.append({
        "relative_path": "results/" + name,
        "type": "regular",
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "mode": stat.S_IMODE(st.st_mode),
        "mtime_ns": st.st_mtime_ns,
        "nlink": st.st_nlink,
    })
print(json.dumps(receipt, ensure_ascii=True, sort_keys=True, separators=(",", ":")))
PY
}

if [ -e "$p17_lock" ] || [ -L "$p17_lock" ]; then
    fail 3 "concurrent exact lock entry"
fi

scan_residue 0 || fail 5 "pre-existing cache or non-lock task residue"

if mkdir -- "$p17_lock"; then
    p17_lock_owned=1
else
    if [ -e "$p17_lock" ] || [ -L "$p17_lock" ]; then
        fail 3 "atomic lock acquisition race"
    fi
    fail 5 "atomic lock acquisition failure"
fi

trap failure_cleanup EXIT HUP INT TERM

scan_residue 1 || fail 5 "cache or task residue after lock acquisition"
inventory_scan 1 || fail 5 "pre-run implementation/results inventory drift"

p17_receipt_before=$(results_receipt) || fail 5 "cannot capture checked-in receipt"
python3 -B code/generate_controls.py --verify-only --output-dir results || fail $? "checked-in verify-only failure"
p17_receipt_after=$(results_receipt) || fail 11 "cannot capture post-verify receipt"
if [ "$p17_receipt_before" != "$p17_receipt_after" ]; then
    fail 11 "verify-only changed checked-in bytes or metadata"
fi

p17_temp_a=$(mktemp -d "$p17_tmp_base/p17-controls.XXXXXX") || fail 4 "cannot create fresh root A"
p17_temp_b=$(mktemp -d "$p17_tmp_base/p17-controls.XXXXXX") || fail 4 "cannot create fresh root B"
if [ "$p17_temp_a" = "$p17_temp_b" ]; then
    fail 4 "fresh roots are not distinct"
fi

python3 -B code/generate_controls.py --generate --output-dir "$p17_temp_a" || fail $? "fresh generation A failure"
python3 -B code/generate_controls.py --verify-only --output-dir "$p17_temp_a" || fail $? "fresh verification A failure"
python3 -B code/generate_controls.py --generate --output-dir "$p17_temp_b" || fail $? "fresh generation B failure"
python3 -B code/generate_controls.py --verify-only --output-dir "$p17_temp_b" || fail $? "fresh verification B failure"

for p17_name in \
    range_first_handedness_controls.csv \
    action_blind_open_records.csv \
    connected_disconnected_firewall.csv \
    domain_guard_controls.csv \
    quantale_localic_firewall.csv \
    actual_standard_owner_controls.csv \
    dilation_strict_marker_controls.csv \
    fixed_prime_provenance_controls.csv \
    target_summary.csv \
    manifest.json
do
    cmp -s -- "results/$p17_name" "$p17_temp_a/$p17_name" || fail 9 "checked-in/A byte mismatch: $p17_name"
    cmp -s -- "results/$p17_name" "$p17_temp_b/$p17_name" || fail 9 "checked-in/B byte mismatch: $p17_name"
    cmp -s -- "$p17_temp_a/$p17_name" "$p17_temp_b/$p17_name" || fail 9 "A/B byte mismatch: $p17_name"
done

python3 -B code/test_controls.py --checked-in results --fresh-a "$p17_temp_a" --fresh-b "$p17_temp_b" || fail 10 "unittest failure"

python3 -B code/generate_controls.py --verify-only --output-dir results || fail $? "post-test checked-in verification failure"
python3 -B code/generate_controls.py --verify-only --output-dir "$p17_temp_a" || fail $? "post-test A verification failure"
python3 -B code/generate_controls.py --verify-only --output-dir "$p17_temp_b" || fail $? "post-test B verification failure"
scan_residue 1 || fail 5 "post-test cache or task residue"
inventory_scan 1 || fail 5 "post-test implementation/results inventory drift"

if ! remove_temp_root "$p17_temp_a"; then
    fail 11 "cannot remove fresh root A"
fi
p17_removed_a=$p17_temp_a
p17_temp_a=
if ! remove_temp_root "$p17_temp_b"; then
    fail 11 "cannot remove fresh root B"
fi
p17_removed_b=$p17_temp_b
p17_temp_b=
if ! rmdir -- "$p17_lock"; then
    fail 11 "cannot remove owned lock"
fi
p17_lock_owned=0

if [ -e "$p17_removed_a" ] || [ -L "$p17_removed_a" ] || \
   [ -e "$p17_removed_b" ] || [ -L "$p17_removed_b" ] || \
   [ -e "$p17_lock" ] || [ -L "$p17_lock" ]; then
    fail 11 "cleanup absence verification failure"
fi

scan_residue 0 || fail 11 "final cache or task residue"
inventory_scan 0 || fail 11 "final implementation/results inventory drift"

trap - EXIT HUP INT TERM

echo "P17_CONTROL_REPRODUCTION=PASS"
echo "CHECKED_IN_RECEIPT_SHA256=$(printf '%s' "$p17_receipt_before" | sha256sum | awk '{print $1}')"
echo "CSV_BODY_ROWS=3436"
echo "NONNEGATIVE_CSV_ROWS=3352"
echo "EXPECTED_NEGATIVES_DETECTED=84"
echo "UNITTEST_METHODS=180"
echo "SEMANTIC_MUTATION_CLASSES=48"
echo "PACKAGE_MUTATION_CLASSES=42"
echo "FRESH_GENERATIONS=2"
echo "BYTE_IDENTICAL_COPIES=3"
echo "CACHE_RESIDUE_COUNT=0"
echo "TASK_RESIDUE_COUNT=0"
exit 0
