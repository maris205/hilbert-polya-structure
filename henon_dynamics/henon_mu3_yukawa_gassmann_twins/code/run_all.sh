#!/usr/bin/bash -p
set -euo pipefail
export PATH=/usr/bin:/bin

if [[ -n "${PYTHONOPTIMIZE+x}" ]]; then
  echo "PYTHONOPTIMIZE must be completely unset" >&2
  exit 2
fi
for loader_variable in LD_PRELOAD LD_LIBRARY_PATH; do
  if [[ -n "${!loader_variable+x}" ]]; then
    echo "$loader_variable was present: unsafe parent environment already reached the dynamic loader; abort" >&2
    exit 2
  fi
done
for injected in PYTHONPATH PYTHONHOME PYTHONSAFEPATH BASH_ENV ENV C59_TEST_EVIDENCE_DIR; do
  if [[ -n "${!injected+x}" ]]; then
    echo "$injected must be completely unset" >&2
    exit 2
  fi
done

export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONNOUSERSITE=1
export LANG=C.UTF-8
export LC_ALL=C.UTF-8
export TZ=UTC

MATH_PYTHON=/root/miniconda3/bin/python3
GAP=/usr/bin/gap
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CODE_DIR="$PROJECT_DIR/code"
RESULTS_DIR="$PROJECT_DIR/results"

REFRESH=0
EVIDENCE_DIR=""
while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --refresh-prefreeze)
      [[ "$REFRESH" -eq 0 ]] || { echo "duplicate --refresh-prefreeze" >&2; exit 2; }
      REFRESH=1
      shift
      ;;
    --evidence-dir)
      [[ "$#" -ge 2 && -z "$EVIDENCE_DIR" ]] || { echo "bad --evidence-dir" >&2; exit 2; }
      EVIDENCE_DIR="$2"
      shift 2
      ;;
    *)
      echo "usage: $0 [--refresh-prefreeze --evidence-dir DIR]" >&2
      exit 2
      ;;
  esac
done
if [[ "$REFRESH" -eq 1 && -z "$EVIDENCE_DIR" ]]; then
  echo "refresh requires --evidence-dir" >&2
  exit 2
fi
if [[ "$REFRESH" -eq 0 && -n "$EVIDENCE_DIR" ]]; then
  echo "--evidence-dir is accepted only with --refresh-prefreeze" >&2
  exit 2
fi

for binary in "$MATH_PYTHON" "$GAP"; do
  [[ -x "$binary" && -f "$binary" ]] || {
    echo "missing/nonregular fixed backend: $binary" >&2
    exit 2
  }
done
[[ -d "$RESULTS_DIR" && ! -L "$RESULTS_DIR" ]] || {
  echo "results directory must already be a real directory" >&2
  exit 2
}
exec {RESULTS_FD}<"$RESULTS_DIR"
RESULTS_DEVICE="$(/usr/bin/stat -Lc '%d' "/proc/self/fd/$RESULTS_FD")"
RESULTS_INODE="$(/usr/bin/stat -Lc '%i' "/proc/self/fd/$RESULTS_FD")"
readonly RESULTS_FD RESULTS_DEVICE RESULTS_INODE
verify_results_binding() {
  local path_device path_inode fd_device fd_inode
  [[ -d "$RESULTS_DIR" && ! -L "$RESULTS_DIR" ]] || {
    echo "results pathname no longer names a real directory" >&2
    return 1
  }
  path_device="$(/usr/bin/stat -c '%d' "$RESULTS_DIR")" || return 1
  path_inode="$(/usr/bin/stat -c '%i' "$RESULTS_DIR")" || return 1
  fd_device="$(/usr/bin/stat -Lc '%d' "/proc/self/fd/$RESULTS_FD")" || return 1
  fd_inode="$(/usr/bin/stat -Lc '%i' "/proc/self/fd/$RESULTS_FD")" || return 1
  [[ "$path_device" == "$RESULTS_DEVICE" && "$path_inode" == "$RESULTS_INODE" ]] || {
    echo "results pathname device/inode changed" >&2
    return 1
  }
  [[ "$fd_device" == "$RESULTS_DEVICE" && "$fd_inode" == "$RESULTS_INODE" ]] || {
    echo "results directory fd device/inode changed" >&2
    return 1
  }
}
verify_results_binding

EVIDENCE_NAMES=(
  c59_group_evidence.json
  c59_resolvent_evidence.json
)
GENERATED_NAMES=(c59_schema.json c59_certificate.json c59_check_report.json)
PROMOTED_NAMES=("${EVIDENCE_NAMES[@]}" "${GENERATED_NAMES[@]}" scoped_hash_manifest.json)

PRE_SNAPSHOT=""
POST_SNAPSHOT=""
STAGE_DIR=""
STAGE_DEVICE=""
STAGE_INODE=""
STAGE_SNAPSHOT=""
CHECKED_STAGE_SNAPSHOT=""
RUN_STATE="PRECOMMIT"
STAGE_CLEANUP_ATTEMPTED=0
PROMOTION_ACTIVE=0
classify_promotion_status() {
  case "$1" in
    0) PROMOTION_CLASS=LIVE_COMMITTED ;;
    74) PROMOTION_CLASS=ROLLED_BACK_VERIFIED ;;
    75) PROMOTION_CLASS=LIVE_COMMITTED_WITH_DEBRIS ;;
    *) PROMOTION_CLASS=LIVE_STATE_UNCERTAIN ;;
  esac
}
refresh_stage_snapshot() {
  verify_results_binding
  STAGE_SNAPSHOT="$("$MATH_PYTHON" -s -B "$CODE_DIR/c59_atomic_promote.py" \
    --result-dir "$RESULTS_DIR" \
    --snapshot-stage "$STAGE_DIR" \
    --expected-stage-device "$STAGE_DEVICE" \
    --expected-stage-inode "$STAGE_INODE")"
  verify_results_binding
}
cleanup() {
  local status=$?
  trap - EXIT HUP INT TERM
  if ! verify_results_binding; then
    echo "results parent identity changed; retaining all stage/transaction evidence" >&2
    RUN_STATE="LIVE_STATE_UNCERTAIN"
    STAGE_CLEANUP_ATTEMPTED=1
    status=1
  fi
  if [[ "$PROMOTION_ACTIVE" -eq 1 ]]; then
    RUN_STATE="LIVE_STATE_UNCERTAIN"
    STAGE_CLEANUP_ATTEMPTED=1
  fi
  if [[ -n "$STAGE_DIR" && -n "$STAGE_SNAPSHOT" && "$STAGE_CLEANUP_ATTEMPTED" -eq 0 ]]; then
    if "$MATH_PYTHON" -s -B "$CODE_DIR/c59_atomic_promote.py" \
      --result-dir "$RESULTS_DIR" \
      --cleanup-stage "$STAGE_DIR" \
      --expected-stage-snapshot "$STAGE_SNAPSHOT"; then
      STAGE_DIR=""
    else
      echo "retaining changed/foreign active stage for inspection: $STAGE_DIR" >&2
    fi
  elif [[ -n "$STAGE_DIR" ]]; then
    echo "retaining active stage (cleanup unavailable/already attempted): $STAGE_DIR" >&2
  fi
  if [[ "$status" -ne 0 && "$RUN_STATE" == "LIVE_STATE_UNCERTAIN" ]]; then
    echo "LIVE_STATE_UNCERTAIN—atomic child did not prove rollback or commit; stage retained; DO NOT RETRY; manual recovery required" >&2
  elif [[ "$status" -ne 0 && "$RUN_STATE" == "LIVE_COMMITTED" ]]; then
    echo "POSTCOMMIT_INCOMPLETE—live six-target state has changed; do not assume rollback or retry refresh" >&2
  elif [[ "$status" -ne 0 && "$RUN_STATE" == "LIVE_COMMITTED_WITH_DEBRIS" ]]; then
    echo "COMMITTED_WITH_DEBRIS—live commit is durable; stage retained; DO NOT RETRY" >&2
  fi
  exit "$status"
}
trap cleanup EXIT HUP INT TERM

if [[ "$REFRESH" -eq 0 ]]; then
  verify_results_binding
  "$MATH_PYTHON" -s -B "$CODE_DIR/c59_hash_manifest.py"
  verify_results_binding
  PRE_SNAPSHOT="$("$MATH_PYTHON" -s -B "$CODE_DIR/c59_hash_manifest.py" --snapshot)"
  verify_results_binding
  EVIDENCE_DIR="$RESULTS_DIR"
else
  verify_results_binding
  "$MATH_PYTHON" -s -B "$CODE_DIR/c59_hash_manifest.py" --refresh-hygiene
  verify_results_binding
  [[ -d "$EVIDENCE_DIR" && ! -L "$EVIDENCE_DIR" ]] || {
    echo "evidence directory must be a real directory" >&2
    exit 2
  }
  EVIDENCE_DIR="$(cd "$EVIDENCE_DIR" && pwd -P)"
fi

"$MATH_PYTHON" -s -B "$CODE_DIR/c59_pipeline.py" \
  --preflight \
  --math-python "$MATH_PYTHON" \
  --gap "$GAP"
verify_results_binding

if [[ "$REFRESH" -eq 1 ]]; then
  mapfile -t OBSERVED_EVIDENCE < <(/usr/bin/find "$EVIDENCE_DIR" -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C /usr/bin/sort)
  [[ "${#OBSERVED_EVIDENCE[@]}" -eq 2 ]] || {
    echo "external evidence directory must contain exactly two entries" >&2
    exit 2
  }
  for index in "${!EVIDENCE_NAMES[@]}"; do
    [[ "${OBSERVED_EVIDENCE[$index]}" == "${EVIDENCE_NAMES[$index]}" ]] || {
      echo "external evidence inventory mismatch" >&2
      exit 2
    }
  done
fi
for index in "${!EVIDENCE_NAMES[@]}"; do
  source_path="$EVIDENCE_DIR/${EVIDENCE_NAMES[$index]}"
  [[ -f "$source_path" && ! -L "$source_path" ]] || {
    echo "nonregular evidence input: $source_path" >&2
    exit 2
  }
done

verify_results_binding
STAGE_FD_PATH="$(/usr/bin/mktemp -d "/proc/self/fd/$RESULTS_FD/.c59-stage-XXXXXXXX")"
STAGE_BASENAME="${STAGE_FD_PATH##*/}"
[[ "$STAGE_BASENAME" =~ ^\.c59-stage-[A-Za-z0-9]{8}$ ]] || {
  echo "mktemp returned a noncanonical active-stage basename" >&2
  exit 1
}
STAGE_DIR="$RESULTS_DIR/$STAGE_BASENAME"
verify_results_binding
[[ -d "$STAGE_DIR" && ! -L "$STAGE_DIR" ]] || {
  echo "fd-created active stage did not rebind under canonical results path" >&2
  exit 1
}
[[ "$(/usr/bin/stat -Lc '%d:%i' "$STAGE_FD_PATH")" == "$(/usr/bin/stat -c '%d:%i' "$STAGE_DIR")" ]] || {
  echo "fd-created active stage identity changed during canonical rebound" >&2
  exit 1
}
STAGE_DEVICE="$(/usr/bin/stat -c '%d' "$STAGE_DIR")"
STAGE_INODE="$(/usr/bin/stat -c '%i' "$STAGE_DIR")"
refresh_stage_snapshot
for name in "${EVIDENCE_NAMES[@]}"; do
  verify_results_binding
  /usr/bin/cp --preserve=mode,timestamps -- "$EVIDENCE_DIR/$name" "$STAGE_DIR/$name"
  verify_results_binding
  refresh_stage_snapshot
done

verify_results_binding
C59_TEST_EVIDENCE_DIR="$STAGE_DIR" \
  "$MATH_PYTHON" -s -B -m unittest discover \
  -s "$CODE_DIR" -p 'test_c59.py' -v
verify_results_binding

"$MATH_PYTHON" -s -B "$CODE_DIR/c59_producer.py" \
  --artifact-dir "$STAGE_DIR" \
  --output "$STAGE_DIR/c59_certificate.json" \
  --schema-output "$STAGE_DIR/c59_schema.json" \
  --math-python "$MATH_PYTHON" \
  --gap "$GAP"
verify_results_binding
refresh_stage_snapshot

"$MATH_PYTHON" -s -B "$CODE_DIR/c59_checker.py" \
  "$STAGE_DIR/c59_certificate.json" \
  --schema "$STAGE_DIR/c59_schema.json" \
  --output "$STAGE_DIR/c59_check_report.json" \
  --group-evidence "$STAGE_DIR/c59_group_evidence.json" \
  --resolvent-evidence "$STAGE_DIR/c59_resolvent_evidence.json" \
  --math-python "$MATH_PYTHON" \
  --gap "$GAP"
verify_results_binding
refresh_stage_snapshot
CHECKED_STAGE_SNAPSHOT="$STAGE_SNAPSHOT"

"$MATH_PYTHON" -s -B "$CODE_DIR/c59_hash_manifest.py" \
  --write \
  --stage-dir "$STAGE_DIR" \
  --manifest "$STAGE_DIR/scoped_hash_manifest.json"
verify_results_binding
refresh_stage_snapshot
"$MATH_PYTHON" -s -B "$CODE_DIR/c59_atomic_promote.py" \
  --result-dir "$RESULTS_DIR" \
  --verify-stage-extension \
  --prior-stage-snapshot "$CHECKED_STAGE_SNAPSHOT" \
  --expected-stage-snapshot "$STAGE_SNAPSHOT"
verify_results_binding
"$MATH_PYTHON" -s -B "$CODE_DIR/c59_hash_manifest.py" \
  --stage-dir "$STAGE_DIR" \
  --manifest "$STAGE_DIR/scoped_hash_manifest.json"
verify_results_binding
RUN_STATE="STAGED_VERIFIED"

if [[ "$REFRESH" -eq 1 ]]; then
  ATOMIC_ARGS=(--result-dir "$RESULTS_DIR" --expected-stage-snapshot "$STAGE_SNAPSHOT")
  for name in "${PROMOTED_NAMES[@]}"; do
    ATOMIC_ARGS+=(--source "$STAGE_DIR/$name" --target "$name")
  done
  verify_results_binding
  set +e
  PROMOTION_ACTIVE=1
  "$MATH_PYTHON" -s -B "$CODE_DIR/c59_atomic_promote.py" "${ATOMIC_ARGS[@]}"
  PROMOTION_STATUS=$?
  if ! verify_results_binding; then
    PROMOTION_STATUS=1
  fi
  set -e
  classify_promotion_status "$PROMOTION_STATUS"
  case "$PROMOTION_CLASS" in
    LIVE_COMMITTED)
      RUN_STATE="LIVE_COMMITTED"
      ;;
    ROLLED_BACK_VERIFIED)
      RUN_STATE="ROLLED_BACK_VERIFIED"
      ;;
    LIVE_COMMITTED_WITH_DEBRIS)
      RUN_STATE="LIVE_COMMITTED_WITH_DEBRIS"
      STAGE_CLEANUP_ATTEMPTED=1
      ;;
    LIVE_STATE_UNCERTAIN)
      RUN_STATE="LIVE_STATE_UNCERTAIN"
      STAGE_CLEANUP_ATTEMPTED=1
      ;;
  esac
  PROMOTION_ACTIVE=0
  if [[ "$PROMOTION_CLASS" == "LIVE_COMMITTED_WITH_DEBRIS" ]]; then
    echo "COMMITTED_WITH_DEBRIS—DO NOT RETRY; live six-target commit is durable; active stage retained" >&2
    trap - EXIT HUP INT TERM
    exit 75
  fi
  if [[ "$PROMOTION_CLASS" == "ROLLED_BACK_VERIFIED" ]]; then
    exit "$PROMOTION_STATUS"
  fi
  if [[ "$PROMOTION_CLASS" == "LIVE_STATE_UNCERTAIN" ]]; then
    echo "LIVE_STATE_UNCERTAIN—atomic status $PROMOTION_STATUS; preserving active stage; DO NOT RETRY; manual recovery required" >&2
    trap - EXIT HUP INT TERM
    exit "$PROMOTION_STATUS"
  fi
else
  for name in "${PROMOTED_NAMES[@]}"; do
    verify_results_binding
    /usr/bin/cmp -- "$STAGE_DIR/$name" "$RESULTS_DIR/$name"
    verify_results_binding
  done
fi

STAGE_CLEANUP_ATTEMPTED=1
"$MATH_PYTHON" -s -B "$CODE_DIR/c59_atomic_promote.py" \
  --result-dir "$RESULTS_DIR" \
  --cleanup-stage "$STAGE_DIR" \
  --expected-stage-snapshot "$STAGE_SNAPSHOT"
verify_results_binding
STAGE_DIR=""
STAGE_CLEANUP_ATTEMPTED=0

"$MATH_PYTHON" -s -B "$CODE_DIR/c59_hash_manifest.py"
verify_results_binding
if [[ "$REFRESH" -eq 1 ]]; then
  echo "refresh complete; launching mandatory nonmutating live replay"
  set +e
  /usr/bin/bash -p "$CODE_DIR/run_all.sh"
  REPLAY_STATUS=$?
  set -e
  if [[ "$REPLAY_STATUS" -ne 0 ]]; then
    exit "$REPLAY_STATUS"
  fi
  RUN_STATE="RELEASE_VERIFIED"
  echo "HCS-C59 refresh and mandatory live replay PASS (PREFREEZE code/results; PAPER_PENDING)"
  exit 0
fi

POST_SNAPSHOT="$("$MATH_PYTHON" -s -B "$CODE_DIR/c59_hash_manifest.py" --snapshot)"
verify_results_binding
[[ "$PRE_SNAPSHOT" == "$POST_SNAPSHOT" ]] || {
  echo "default replay changed live bytes/modes/mtimes/inodes" >&2
  exit 1
}
RUN_STATE="RELEASE_VERIFIED"
echo "HCS-C59 live default replay PASS (PREFREEZE code/results; PAPER_PENDING)"
