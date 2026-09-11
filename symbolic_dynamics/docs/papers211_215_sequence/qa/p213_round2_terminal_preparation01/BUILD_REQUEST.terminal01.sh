#!/bin/bash
# PROPOSED SOURCE ONLY. Never run before root receives the strict pair,
# documentary delta, exact request and finite runtime/trust binding.
# Not a grant, observer, scientific verifier, reviewer or terminal build.
set -euo pipefail
umask 077
if [[ "${1-}" != "--execute-under-separate-root-grant" || "$#" != 1 ]]; then
  printf '%s\n' 'P213_BUILD_NOT_AUTHORIZED_BY_THIS_SOURCE' >&2
  exit 78
fi
P213_PREP='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p213_round2_terminal_preparation01'
P213_SRC='/root/autodl-tmp/symbolic_dynamics/papers/213-receiver-limited-cyclic-transfer/frozen_round2'
P213_BIND='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p213_round2_terminal_preparation01'
P213_OUT='/root/autodl-tmp/symbolic_dynamics/papers/213-receiver-limited-cyclic-transfer/qa_final/cold_build_1'
P213_COLD="$P213_OUT/source_only"
P213_PINFILE="$P213_PREP/PROPOSED_SOURCE_ONLY.sha256"
# These paths are proposals, not observed or created by preparation.
# Root pins the whole exact manifest and source/request in its later grant.
[[ -f "$P213_BIND/RUNTIME_INPUTS.sha256" && ! -L "$P213_BIND/RUNTIME_INPUTS.sha256" ]]
[[ -f "$P213_PINFILE" && ! -L "$P213_PINFILE" ]]
# Exclusive new tree only. Existing/failed tree is never cleaned or resumed.
mkdir -- "$P213_OUT"
mkdir -- "$P213_OUT/raw" "$P213_OUT/pass_artifacts" "$P213_OUT/pages" "$P213_COLD"
mkdir -- "$P213_COLD/sections"
exec 3>&1 4>&2
set -C
exec > "$P213_OUT/controller.stdout.raw" 2> "$P213_OUT/controller.stderr.raw"
p213_finish() {
  local p213_rc=$?
  trap - EXIT
  printf '%s\n' "$p213_rc" > "$P213_OUT/controller.exit"
  printf 'P213_INITIAL_BUILD_SUPERVISOR_EXIT=%s\n' "$p213_rc" >&3
  exit "$p213_rc"
}
trap p213_finish EXIT
P213_SOURCES=(main.tex math_commands.tex references.bib
  sections/00_abstract.tex sections/01_introduction.tex
  sections/02_temporal.tex sections/03_inverse.tex
  sections/04_fibres.tex sections/05_verification.tex)
P213_PRODUCTS=(main.aux main.bbl main.blg main.log main.fls main.out main.toc main.pdf)
cp --no-clobber -- "$P213_PINFILE" "$P213_OUT/SOURCE_EXPECTED.sha256"
cp --no-clobber -- "$P213_BIND/RUNTIME_INPUTS.sha256" "$P213_OUT/RUNTIME_EXPECTED.sha256"
sha256sum -- "$P213_PREP/BUILD_REQUEST.terminal01.sh" "$P213_PREP/NATIVE_REQUESTS.terminal01.proposed.json" "$P213_BIND/RUNTIME_INPUTS.sha256" > "$P213_OUT/REQUEST_AND_BINDING.sha256"
# Fixed selected runtime paths come from root's separately received manifest.
# No which/help/version/proc query, recursive discovery, package installation,
# dynamic FLS-path following or P211 observer is hidden in this script.
sha256sum -c --strict "$P213_OUT/RUNTIME_EXPECTED.sha256" > "$P213_OUT/runtime.before.stdout" 2> "$P213_OUT/runtime.before.stderr"
(cd "$P213_SRC" && sha256sum -c --strict "$P213_OUT/SOURCE_EXPECTED.sha256") > "$P213_OUT/live_source.before.stdout" 2> "$P213_OUT/live_source.before.stderr"
for p213_name in "${P213_SOURCES[@]}"; do
  [[ -f "$P213_SRC/$p213_name" && ! -L "$P213_SRC/$p213_name" ]]
  cp --no-clobber -- "$P213_SRC/$p213_name" "$P213_COLD/$p213_name"
  cmp -- "$P213_SRC/$p213_name" "$P213_COLD/$p213_name"
done
cd "$P213_COLD"
sha256sum -c --strict "$P213_OUT/SOURCE_EXPECTED.sha256" > "$P213_OUT/cold_source.initial.stdout" 2> "$P213_OUT/cold_source.initial.stderr"
for p213_name in "${P213_PRODUCTS[@]}"; do
  [[ ! -e "$p213_name" && ! -L "$p213_name" ]]
done
p213_snapshot() {
  local p213_dest="$P213_OUT/pass_artifacts/$1"
  mkdir -- "$p213_dest"
  for p213_name in "${P213_PRODUCTS[@]}"; do
    if [[ -f "$p213_name" && ! -L "$p213_name" ]]; then
      cp --no-clobber -- "$p213_name" "$p213_dest/$p213_name"
      sha256sum -- "$p213_name" >> "$p213_dest/PRESENT.sha256"
    elif [[ -e "$p213_name" || -L "$p213_name" ]]; then
      printf 'UNEXPECTED_PRODUCT_TYPE %s\n' "$p213_name" >> "$p213_dest/TYPE_FAILURE.txt"
      return 93
    else
      printf '%s\n' "$p213_name" >> "$p213_dest/ABSENT.txt"
    fi
  done
}
P213_STEP_STATUS=0
p213_run() {
  local p213_label=$1 p213_seconds=$2
  shift 2
  printf 'cwd=%s\n' "$P213_COLD" > "$P213_OUT/raw/$p213_label.request.txt"
  printf 'supervisor_argv=' >> "$P213_OUT/raw/$p213_label.request.txt"
  printf '%q ' /usr/bin/timeout --signal=TERM --kill-after=10s "${p213_seconds}s" "$@" >> "$P213_OUT/raw/$p213_label.request.txt"
  printf '\n' >> "$P213_OUT/raw/$p213_label.request.txt"
  set +e
  /usr/bin/timeout --signal=TERM --kill-after=10s "${p213_seconds}s" "$@" < /dev/null > "$P213_OUT/raw/$p213_label.stdout.raw" 2> "$P213_OUT/raw/$p213_label.stderr.raw"
  P213_STEP_STATUS=$?
  set -e
  printf '%s\n' "$P213_STEP_STATUS" > "$P213_OUT/raw/$p213_label.supervisor_exit"
  # A timeout/launch failure is not assigned an invented native TeX exit.
}
p213_build_pass() {
  local p213_label=$1
  shift
  p213_snapshot "$p213_label.before"
  p213_run "$p213_label" 600 "$@"
  p213_snapshot "$p213_label.after"
  sha256sum -c --strict "$P213_OUT/SOURCE_EXPECTED.sha256" > "$P213_OUT/raw/$p213_label.sources.stdout" 2> "$P213_OUT/raw/$p213_label.sources.stderr"
  if [[ "$P213_STEP_STATUS" != 0 ]]; then exit "$P213_STEP_STATUS"; fi
}
P213_TEX=(/usr/bin/pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex)
p213_build_pass pass1 "${P213_TEX[@]}"
p213_build_pass bibtex /usr/bin/bibtex main
p213_build_pass pass2 "${P213_TEX[@]}"
p213_build_pass pass3 "${P213_TEX[@]}"
[[ -s main.pdf ]]
p213_run pdfinfo 180 /usr/bin/pdfinfo main.pdf
[[ "$P213_STEP_STATUS" == 0 ]] || exit "$P213_STEP_STATUS"
p213_run pdffonts 180 /usr/bin/pdffonts main.pdf
[[ "$P213_STEP_STATUS" == 0 ]] || exit "$P213_STEP_STATUS"
p213_run pdftotext 180 /usr/bin/pdftotext -layout main.pdf -
[[ "$P213_STEP_STATUS" == 0 ]] || exit "$P213_STEP_STATUS"
p213_run final_diagnostics 180 /usr/bin/awk '/Warning|undefined|Overfull|Underfull|Missing character|Rerun|Label.s. may have changed|Error|error|^!/ {print FILENAME ":" FNR ":" $0}' main.log main.blg
[[ "$P213_STEP_STATUS" == 0 ]] || exit "$P213_STEP_STATUS"
P213_PAGES=$(/usr/bin/awk '/^Pages:[[:space:]]/ {print $2}' "$P213_OUT/raw/pdfinfo.stdout.raw")
[[ "$P213_PAGES" =~ ^[1-9][0-9]*$ ]]
printf '%s\n' "$P213_PAGES" > "$P213_OUT/PAGE_COUNT.txt"
for ((p213_page=1; p213_page<=P213_PAGES; p213_page++)); do
  printf -v p213_label 'page-%04d' "$p213_page"
  p213_run "$p213_label" 180 /usr/bin/pdftoppm -f "$p213_page" -l "$p213_page" -singlefile -png -r 150 main.pdf "$P213_OUT/pages/$p213_label"
  [[ "$P213_STEP_STATUS" == 0 ]] || exit "$P213_STEP_STATUS"
  [[ -s "$P213_OUT/pages/$p213_label.png" ]]
  sha256sum -- "$P213_OUT/pages/$p213_label.png" >> "$P213_OUT/PAGES.sha256"
done
sha256sum -c --strict "$P213_OUT/RUNTIME_EXPECTED.sha256" > "$P213_OUT/runtime.after.stdout" 2> "$P213_OUT/runtime.after.stderr"
(cd "$P213_SRC" && sha256sum -c --strict "$P213_OUT/SOURCE_EXPECTED.sha256") > "$P213_OUT/live_source.after.stdout" 2> "$P213_OUT/live_source.after.stderr"
sha256sum -c --strict "$P213_OUT/SOURCE_EXPECTED.sha256" > "$P213_OUT/cold_source.final.stdout" 2> "$P213_OUT/cold_source.final.stderr"
sha256sum -- main.pdf main.log main.fls main.aux main.bbl main.blg > "$P213_OUT/FINAL_PRODUCTS.sha256"
printf '%s\n' 'CAPTURED_PENDING_FULL_LOG_FLS_CONFIG_PDF_AND_ACTUAL_ALL_PAGE_RECEPTION' > "$P213_OUT/STATUS.txt"
# No PDF adoption, Round0, visual PASS or package seal is produced here.
