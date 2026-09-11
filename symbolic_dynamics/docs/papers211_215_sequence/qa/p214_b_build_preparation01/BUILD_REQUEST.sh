#!/bin/bash
# PROPOSED SOURCE ONLY. Requires root receipt, fresh binding and one-use grant.
set -euo pipefail
umask 077
if [[ "${1-}" != "--execute-under-separate-root-grant" || "$#" != 1 ]]; then
  printf '%s\n' 'P214_B_BUILD_NOT_AUTHORIZED_BY_THIS_SOURCE' >&2
  exit 78
fi
P214_PREP='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p214_b_build_preparation01'
P214_SRC='/root/autodl-tmp/symbolic_dynamics/papers/214-nilpotent-bilinear-clock/frozen_round1'
P214_RUNTIME='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p214_a_build_binding02/RUNTIME_INPUTS.sha256'
P214_OUT='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/reviews/p214_b/build01'
P214_COLD="$P214_OUT/source_only"
[[ -f "$P214_PREP/SOURCE_EXPECTED.sha256" && ! -L "$P214_PREP/SOURCE_EXPECTED.sha256" ]]
[[ -f "$P214_PREP/SCIENCE_AND_HISTORY_INPUTS.sha256" && ! -L "$P214_PREP/SCIENCE_AND_HISTORY_INPUTS.sha256" ]]
[[ -f "$P214_RUNTIME" && ! -L "$P214_RUNTIME" ]]
[[ ! -e "$P214_OUT" && ! -L "$P214_OUT" ]]
mkdir -- "$P214_OUT"
mkdir -- "$P214_OUT/raw" "$P214_OUT/pass_artifacts" "$P214_OUT/pages" "$P214_COLD"
mkdir -- "$P214_COLD/sections"
exec 3>&1 4>&2
set -C
exec > "$P214_OUT/controller.stdout.raw" 2> "$P214_OUT/controller.stderr.raw"
p214_b_finish() {
  local p214_b_rc=$?
  trap - EXIT
  printf '%s\n' "$p214_b_rc" > "$P214_OUT/controller.exit"
  printf 'P214_B_BUILD_SUPERVISOR_EXIT=%s\n' "$p214_b_rc" >&3
  exit "$p214_b_rc"
}
trap p214_b_finish EXIT
P214_SOURCES=(main.tex math_commands.tex references.bib sections/0_abstract.tex sections/1_setup.tex sections/2_clock.tex sections/3_fibres.tex sections/4_controls.tex sections/5_scope.tex)
P214_PRODUCTS=(main.aux main.bbl main.blg main.log main.fls main.out main.toc main.pdf)
cp --no-clobber -- "$P214_PREP/SOURCE_EXPECTED.sha256" "$P214_OUT/SOURCE_EXPECTED.sha256"
cp --no-clobber -- "$P214_RUNTIME" "$P214_OUT/RUNTIME_EXPECTED.sha256"
cp --no-clobber -- "$P214_PREP/SCIENCE_AND_HISTORY_INPUTS.sha256" "$P214_OUT/SCIENCE_AND_HISTORY_INPUTS.sha256"
sha256sum -- "$P214_PREP/BUILD_REQUEST.sh" "$P214_PREP/NATIVE_REQUEST.proposed.json" "$P214_RUNTIME" > "$P214_OUT/REQUEST_AND_BINDING.sha256"
sha256sum -c --strict "$P214_OUT/RUNTIME_EXPECTED.sha256" > "$P214_OUT/runtime.before.stdout" 2> "$P214_OUT/runtime.before.stderr"
sha256sum -c --strict "$P214_OUT/SCIENCE_AND_HISTORY_INPUTS.sha256" > "$P214_OUT/science.before.stdout" 2> "$P214_OUT/science.before.stderr"
(cd "$P214_SRC" && sha256sum -c --strict "$P214_OUT/SOURCE_EXPECTED.sha256") > "$P214_OUT/source.before.stdout" 2> "$P214_OUT/source.before.stderr"
for p214_name in "${P214_SOURCES[@]}"; do
  [[ -f "$P214_SRC/$p214_name" && ! -L "$P214_SRC/$p214_name" ]]
  cp --no-clobber -- "$P214_SRC/$p214_name" "$P214_COLD/$p214_name"
  cmp -- "$P214_SRC/$p214_name" "$P214_COLD/$p214_name"
done
cd "$P214_COLD"
sha256sum -c --strict "$P214_OUT/SOURCE_EXPECTED.sha256" > "$P214_OUT/cold_source.initial.stdout" 2> "$P214_OUT/cold_source.initial.stderr"
P214_PHYSICAL_CWD=$(pwd -P)
shopt -s dotglob nullglob
P214_COLD_MEMBERS=(*)
P214_SECTION_MEMBERS=(sections/*)
shopt -u dotglob nullglob
[[ "$P214_PHYSICAL_CWD" == "$P214_COLD" ]]
[[ "${#P214_COLD_MEMBERS[@]}" == 4 && "${#P214_SECTION_MEMBERS[@]}" == 6 ]]
for p214_name in "${P214_COLD_MEMBERS[@]}"; do
  case "$p214_name" in
    main.tex|math_commands.tex|references.bib) [[ -f "$p214_name" && ! -L "$p214_name" ]] ;;
    sections) [[ -d sections && ! -L sections ]] ;;
    *) exit 94 ;;
  esac
done
for p214_name in "${P214_SECTION_MEMBERS[@]}"; do
  case "$p214_name" in
    sections/0_abstract.tex|sections/1_setup.tex|sections/2_clock.tex|sections/3_fibres.tex|sections/4_controls.tex|sections/5_scope.tex) [[ -f "$p214_name" && ! -L "$p214_name" ]] ;;
    *) exit 94 ;;
  esac
done
[[ ! -e texmf && ! -L texmf && ! -e .texlive2021 && ! -L .texlive2021 ]]
{
  printf 'physical_cwd=%s\n' "$P214_PHYSICAL_CWD"
  printf 'cold_members=%s\n' "${#P214_COLD_MEMBERS[@]}"
  printf 'section_members=%s\n' "${#P214_SECTION_MEMBERS[@]}"
  printf '%s\n' 'EXACT_SOURCE_MEMBERSHIP_AND_RELATIVE_TREE_ABSENCE_PASSED'
} > "$P214_OUT/COLD_CWD.actual.txt"
for p214_name in "${P214_PRODUCTS[@]}"; do [[ ! -e "$p214_name" && ! -L "$p214_name" ]]; done
p214_snapshot() {
  local p214_dest="$P214_OUT/pass_artifacts/$1"
  mkdir -- "$p214_dest"
  for p214_name in "${P214_PRODUCTS[@]}"; do
    if [[ -f "$p214_name" && ! -L "$p214_name" ]]; then
      cp --no-clobber -- "$p214_name" "$p214_dest/$p214_name"
      sha256sum -- "$p214_name" >> "$p214_dest/PRESENT.sha256"
    elif [[ -e "$p214_name" || -L "$p214_name" ]]; then
      printf 'UNEXPECTED_PRODUCT_TYPE %s\n' "$p214_name" >> "$p214_dest/TYPE_FAILURE.txt"
      return 93
    else
      printf '%s\n' "$p214_name" >> "$p214_dest/ABSENT.txt"
    fi
  done
}
P214_STEP_STATUS=0
p214_run() {
  local p214_label=$1 p214_seconds=$2
  shift 2
  printf 'cwd=%s\n' "$P214_COLD" > "$P214_OUT/raw/$p214_label.request.txt"
  printf 'supervisor_argv=' >> "$P214_OUT/raw/$p214_label.request.txt"
  printf '%q ' /usr/bin/timeout --signal=TERM --kill-after=10s "${p214_seconds}s" "$@" >> "$P214_OUT/raw/$p214_label.request.txt"
  printf '\n' >> "$P214_OUT/raw/$p214_label.request.txt"
  set +e
  /usr/bin/timeout --signal=TERM --kill-after=10s "${p214_seconds}s" "$@" < /dev/null > "$P214_OUT/raw/$p214_label.stdout.raw" 2> "$P214_OUT/raw/$p214_label.stderr.raw"
  P214_STEP_STATUS=$?
  set -e
  printf '%s\n' "$P214_STEP_STATUS" > "$P214_OUT/raw/$p214_label.supervisor_exit"
}
p214_build_pass() {
  local p214_label=$1
  shift
  p214_snapshot "$p214_label.before"
  p214_run "$p214_label" 600 "$@"
  p214_snapshot "$p214_label.after"
  sha256sum -c --strict "$P214_OUT/SOURCE_EXPECTED.sha256" > "$P214_OUT/raw/$p214_label.sources.stdout" 2> "$P214_OUT/raw/$p214_label.sources.stderr"
  [[ "$P214_STEP_STATUS" == 0 ]] || exit "$P214_STEP_STATUS"
}
P214_TEX=(/usr/bin/pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex)
p214_build_pass pass1 "${P214_TEX[@]}"
p214_build_pass bibtex /usr/bin/bibtex main
p214_build_pass pass2 "${P214_TEX[@]}"
p214_build_pass pass3 "${P214_TEX[@]}"
[[ -s main.pdf ]]
p214_run pdfinfo 180 /usr/bin/pdfinfo main.pdf
[[ "$P214_STEP_STATUS" == 0 ]] || exit "$P214_STEP_STATUS"
p214_run pdffonts 180 /usr/bin/pdffonts main.pdf
[[ "$P214_STEP_STATUS" == 0 ]] || exit "$P214_STEP_STATUS"
p214_run pdftotext 180 /usr/bin/pdftotext -layout main.pdf -
[[ "$P214_STEP_STATUS" == 0 ]] || exit "$P214_STEP_STATUS"
p214_run final_diagnostics 180 /usr/bin/awk '/Warning|undefined|Overfull|Underfull|Missing character|Rerun|Label.s. may have changed|Error|error|^!/ {print FILENAME ":" FNR ":" $0}' main.log main.blg
[[ "$P214_STEP_STATUS" == 0 ]] || exit "$P214_STEP_STATUS"
P214_PAGES=$(/usr/bin/awk '/^Pages:[[:space:]]/ {print $2}' "$P214_OUT/raw/pdfinfo.stdout.raw")
[[ "$P214_PAGES" =~ ^[1-9][0-9]*$ ]]
printf '%s\n' "$P214_PAGES" > "$P214_OUT/PAGE_COUNT.txt"
for ((p214_page=1; p214_page<=P214_PAGES; p214_page++)); do
  printf -v p214_label 'page-%04d' "$p214_page"
  p214_run "$p214_label" 180 /usr/bin/pdftoppm -f "$p214_page" -l "$p214_page" -singlefile -png -r 150 main.pdf "$P214_OUT/pages/$p214_label"
  [[ "$P214_STEP_STATUS" == 0 ]] || exit "$P214_STEP_STATUS"
  [[ -s "$P214_OUT/pages/$p214_label.png" ]]
  sha256sum -- "$P214_OUT/pages/$p214_label.png" >> "$P214_OUT/PAGES.sha256"
done
sha256sum -c --strict "$P214_OUT/RUNTIME_EXPECTED.sha256" > "$P214_OUT/runtime.after.stdout" 2> "$P214_OUT/runtime.after.stderr"
sha256sum -c --strict "$P214_OUT/SCIENCE_AND_HISTORY_INPUTS.sha256" > "$P214_OUT/science.after.stdout" 2> "$P214_OUT/science.after.stderr"
(cd "$P214_SRC" && sha256sum -c --strict "$P214_OUT/SOURCE_EXPECTED.sha256") > "$P214_OUT/source.after.stdout" 2> "$P214_OUT/source.after.stderr"
sha256sum -c --strict "$P214_OUT/SOURCE_EXPECTED.sha256" > "$P214_OUT/cold_source.final.stdout" 2> "$P214_OUT/cold_source.final.stderr"
sha256sum -- main.pdf main.log main.fls main.aux main.bbl main.blg > "$P214_OUT/FINAL_PRODUCTS.sha256"
printf '%s\n' 'CAPTURED_PENDING_B_ARTIFACT_DATA_AND_ACTUAL_ALL_PAGE_RECEPTION' > "$P214_OUT/STATUS.txt"
# No PDF adoption, final B verdict, Round2, terminal, Git or external action.
