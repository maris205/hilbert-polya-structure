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
for injected in PYTHONPATH PYTHONHOME PYTHONSAFEPATH BASH_ENV ENV; do
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

PARI_PYTHON=/usr/bin/python3
FLINT_GROUP_PYTHON=/root/miniconda3/bin/python3
SINGULAR=/usr/bin/Singular
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

for binary in "$PARI_PYTHON" "$FLINT_GROUP_PYTHON" "$SINGULAR"; do
  [[ -x "$binary" && -f "$binary" ]] || {
    echo "missing/nonregular fixed backend: $binary" >&2
    exit 2
  }
done
[[ -d "$RESULTS_DIR" && ! -L "$RESULTS_DIR" ]] || {
  echo "results directory must already be a real directory" >&2
  exit 2
}

EVIDENCE_NAMES=(
  a12_crt_transcript.json.gz
  a12_table.json.gz
  delta_crt.json.gz
  incidence_char0_witness.json.gz
  theta_crt.json.gz
)
GENERATED_NAMES=(c57_schema.json c57_certificate.json c57_check_report.json)
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
  STAGE_SNAPSHOT="$("$FLINT_GROUP_PYTHON" -s -B "$CODE_DIR/c57_atomic_promote.py" \
    --result-dir "$RESULTS_DIR" \
    --snapshot-stage "$STAGE_DIR" \
    --expected-stage-device "$STAGE_DEVICE" \
    --expected-stage-inode "$STAGE_INODE")"
}
cleanup() {
  local status=$?
  trap - EXIT HUP INT TERM
  if [[ "$PROMOTION_ACTIVE" -eq 1 ]]; then
    RUN_STATE="LIVE_STATE_UNCERTAIN"
    STAGE_CLEANUP_ATTEMPTED=1
  fi
  if [[ -n "$STAGE_DIR" && -n "$STAGE_SNAPSHOT" && "$STAGE_CLEANUP_ATTEMPTED" -eq 0 ]]; then
    if "$FLINT_GROUP_PYTHON" -s -B "$CODE_DIR/c57_atomic_promote.py" \
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
    echo "POSTCOMMIT_INCOMPLETE—live nine-target state has changed; do not assume rollback or retry refresh" >&2
  elif [[ "$status" -ne 0 && "$RUN_STATE" == "LIVE_COMMITTED_WITH_DEBRIS" ]]; then
    echo "COMMITTED_WITH_DEBRIS—live commit is durable; stage retained; DO NOT RETRY" >&2
  fi
  exit "$status"
}
trap cleanup EXIT HUP INT TERM

if [[ "$REFRESH" -eq 0 ]]; then
  "$FLINT_GROUP_PYTHON" -s -B "$CODE_DIR/c57_hash_manifest.py"
  PRE_SNAPSHOT="$("$FLINT_GROUP_PYTHON" -s -B "$CODE_DIR/c57_hash_manifest.py" --snapshot)"
  EVIDENCE_DIR="$RESULTS_DIR"
else
  "$FLINT_GROUP_PYTHON" -s -B "$CODE_DIR/c57_hash_manifest.py" --refresh-hygiene
  [[ -d "$EVIDENCE_DIR" && ! -L "$EVIDENCE_DIR" ]] || {
    echo "evidence directory must be a real directory" >&2
    exit 2
  }
  EVIDENCE_DIR="$(cd "$EVIDENCE_DIR" && pwd -P)"
fi

"$FLINT_GROUP_PYTHON" -s -B "$CODE_DIR/c57_pipeline.py" \
  --preflight \
  --pari-python "$PARI_PYTHON" \
  --flint-group-python "$FLINT_GROUP_PYTHON" \
  --singular "$SINGULAR"

if [[ "$REFRESH" -eq 1 ]]; then
  mapfile -t OBSERVED_EVIDENCE < <(/usr/bin/find "$EVIDENCE_DIR" -mindepth 1 -maxdepth 1 -printf '%f\n' | LC_ALL=C /usr/bin/sort)
  [[ "${#OBSERVED_EVIDENCE[@]}" -eq 5 ]] || {
    echo "external evidence directory must contain exactly five entries" >&2
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

STAGE_DIR="$(/usr/bin/mktemp -d "$RESULTS_DIR/.c57-stage-XXXXXXXX")"
STAGE_DEVICE="$(/usr/bin/stat -c '%d' "$STAGE_DIR")"
STAGE_INODE="$(/usr/bin/stat -c '%i' "$STAGE_DIR")"
refresh_stage_snapshot
for name in "${EVIDENCE_NAMES[@]}"; do
  /usr/bin/cp --preserve=mode,timestamps -- "$EVIDENCE_DIR/$name" "$STAGE_DIR/$name"
  refresh_stage_snapshot
done

"$FLINT_GROUP_PYTHON" -s -B -m unittest discover \
  -s "$CODE_DIR" -p 'test_c57.py' -v

"$FLINT_GROUP_PYTHON" -s -B "$CODE_DIR/c57_producer.py" \
  --artifact-dir "$STAGE_DIR" \
  --output "$STAGE_DIR/c57_certificate.json" \
  --schema-output "$STAGE_DIR/c57_schema.json" \
  --pari-python "$PARI_PYTHON" \
  --flint-group-python "$FLINT_GROUP_PYTHON" \
  --singular "$SINGULAR"
refresh_stage_snapshot

"$FLINT_GROUP_PYTHON" -s -B "$CODE_DIR/c57_checker.py" \
  "$STAGE_DIR/c57_certificate.json" \
  --schema "$STAGE_DIR/c57_schema.json" \
  --output "$STAGE_DIR/c57_check_report.json" \
  --pari-python "$PARI_PYTHON" \
  --flint-group-python "$FLINT_GROUP_PYTHON" \
  --singular "$SINGULAR"
refresh_stage_snapshot
CHECKED_STAGE_SNAPSHOT="$STAGE_SNAPSHOT"

"$FLINT_GROUP_PYTHON" -s -B "$CODE_DIR/c57_hash_manifest.py" \
  --write \
  --stage-dir "$STAGE_DIR" \
  --manifest "$STAGE_DIR/scoped_hash_manifest.json"
refresh_stage_snapshot
"$FLINT_GROUP_PYTHON" -s -B "$CODE_DIR/c57_atomic_promote.py" \
  --result-dir "$RESULTS_DIR" \
  --verify-stage-extension \
  --prior-stage-snapshot "$CHECKED_STAGE_SNAPSHOT" \
  --expected-stage-snapshot "$STAGE_SNAPSHOT"
"$FLINT_GROUP_PYTHON" -s -B "$CODE_DIR/c57_hash_manifest.py" \
  --stage-dir "$STAGE_DIR" \
  --manifest "$STAGE_DIR/scoped_hash_manifest.json"
RUN_STATE="STAGED_VERIFIED"

if [[ "$REFRESH" -eq 1 ]]; then
  ATOMIC_ARGS=(--result-dir "$RESULTS_DIR" --expected-stage-snapshot "$STAGE_SNAPSHOT")
  for name in "${PROMOTED_NAMES[@]}"; do
    ATOMIC_ARGS+=(--source "$STAGE_DIR/$name" --target "$name")
  done
  set +e
  PROMOTION_ACTIVE=1
  "$FLINT_GROUP_PYTHON" -s -B "$CODE_DIR/c57_atomic_promote.py" "${ATOMIC_ARGS[@]}"
  PROMOTION_STATUS=$?
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
    echo "COMMITTED_WITH_DEBRIS—DO NOT RETRY; live nine-target commit is durable; active stage retained" >&2
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
    /usr/bin/cmp -- "$STAGE_DIR/$name" "$RESULTS_DIR/$name"
  done
fi

STAGE_CLEANUP_ATTEMPTED=1
"$FLINT_GROUP_PYTHON" -s -B "$CODE_DIR/c57_atomic_promote.py" \
  --result-dir "$RESULTS_DIR" \
  --cleanup-stage "$STAGE_DIR" \
  --expected-stage-snapshot "$STAGE_SNAPSHOT"
STAGE_DIR=""
STAGE_CLEANUP_ATTEMPTED=0

"$FLINT_GROUP_PYTHON" -s -B "$CODE_DIR/c57_hash_manifest.py"
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
  echo "HCS-C57 refresh and mandatory live replay PASS (PREFREEZE code/results; PAPER_PENDING)"
  exit 0
fi

POST_SNAPSHOT="$("$FLINT_GROUP_PYTHON" -s -B "$CODE_DIR/c57_hash_manifest.py" --snapshot)"
[[ "$PRE_SNAPSHOT" == "$POST_SNAPSHOT" ]] || {
  echo "default replay changed live bytes/modes/mtimes/inodes" >&2
  exit 1
}
RUN_STATE="RELEASE_VERIFIED"
echo "HCS-C57 live default replay PASS (PREFREEZE code/results; PAPER_PENDING)"
