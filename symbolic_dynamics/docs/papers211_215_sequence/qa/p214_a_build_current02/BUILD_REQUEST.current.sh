#!/bin/bash
# PROPOSED SOURCE ONLY. Never run before root receives the author strict pair,
# current source, exact request and fresh finite runtime/trust binding.
# Not a grant, observer, scientific verifier, reviewer or terminal build.
set -euo pipefail
umask 077
if [[ "${1-}" != "--execute-under-separate-root-grant" || "$#" != 1 ]]; then
  printf '%s\n' 'P214_BUILD_NOT_AUTHORIZED_BY_THIS_SOURCE' >&2
  exit 78
fi
P214_PREP='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p214_a_build_current02'
P214_SRC='/root/autodl-tmp/symbolic_dynamics/papers/214-nilpotent-bilinear-clock'
P214_BIND='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p214_a_build_binding02'
P214_OUT='/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/reviews/p214_a/build02'
P214_COLD="$P214_OUT/source_only"
P214_PINFILE="$P214_PREP/SOURCE_EXPECTED.sha256"
# These paths are proposals, not observed or created by preparation.
# Root pins the whole exact manifest and source/request in its later grant.
[[ -f "$P214_BIND/RUNTIME_INPUTS.sha256" && ! -L "$P214_BIND/RUNTIME_INPUTS.sha256" ]]
[[ -f "$P214_PINFILE" && ! -L "$P214_PINFILE" ]]
# Exclusive new tree only. Existing/failed tree is never cleaned or resumed.
mkdir -- "$P214_OUT"
mkdir -- "$P214_OUT/raw" "$P214_OUT/pass_artifacts" "$P214_OUT/pages" "$P214_COLD"
mkdir -- "$P214_COLD/sections"
exec 3>&1 4>&2
set -C
exec > "$P214_OUT/controller.stdout.raw" 2> "$P214_OUT/controller.stderr.raw"
p214_finish() {
  local p214_rc=$?
  trap - EXIT
  printf '%s\n' "$p214_rc" > "$P214_OUT/controller.exit"
  printf 'P214_A_BUILD_SUPERVISOR_EXIT=%s\n' "$p214_rc" >&3
  exit "$p214_rc"
}
trap p214_finish EXIT
P214_SOURCES=(main.tex math_commands.tex references.bib sections/0_abstract.tex sections/1_setup.tex sections/2_clock.tex sections/3_fibres.tex sections/4_controls.tex sections/5_scope.tex)
P214_PRODUCTS=(main.aux main.bbl main.blg main.log main.fls main.out main.toc main.pdf)
cp --no-clobber -- "$P214_PINFILE" "$P214_OUT/SOURCE_EXPECTED.sha256"
cp --no-clobber -- "$P214_BIND/RUNTIME_INPUTS.sha256" "$P214_OUT/RUNTIME_EXPECTED.sha256"
sha256sum -- "$P214_PREP/BUILD_REQUEST.current.sh" "$P214_PREP/NATIVE_REQUEST.current.json" "$P214_BIND/RUNTIME_INPUTS.sha256" > "$P214_OUT/REQUEST_AND_BINDING.sha256"
# Fixed selected runtime paths come from root's separately received manifest.
# No which/help/version/proc query, recursive discovery, package installation,
# dynamic FLS-path following or P211 observer is hidden in this script.
sha256sum -c --strict "$P214_OUT/RUNTIME_EXPECTED.sha256" > "$P214_OUT/runtime.before.stdout" 2> "$P214_OUT/runtime.before.stderr"
(cd "$P214_SRC" && sha256sum -c --strict "$P214_OUT/SOURCE_EXPECTED.sha256") > "$P214_OUT/live_source.before.stdout" 2> "$P214_OUT/live_source.before.stderr"
for p214_name in "${P214_SOURCES[@]}"; do
  [[ -f "$P214_SRC/$p214_name" && ! -L "$P214_SRC/$p214_name" ]]
  cp --no-clobber -- "$P214_SRC/$p214_name" "$P214_COLD/$p214_name"
  cmp -- "$P214_SRC/$p214_name" "$P214_COLD/$p214_name"
done
cd "$P214_COLD"
sha256sum -c --strict "$P214_OUT/SOURCE_EXPECTED.sha256" > "$P214_OUT/cold_source.initial.stdout" 2> "$P214_OUT/cold_source.initial.stderr"
# Prospective fixed fresh-cwd evidence; not observed by source preparation.
P214_PHYSICAL_CWD=$(pwd -P)
shopt -s dotglob nullglob
P214_COLD_MEMBERS=(*)
P214_SECTION_MEMBERS=(sections/*)
shopt -u dotglob nullglob
{
  printf '%s\n' 'commands=Bash pwd -P; dotglob/nullglob fixed (*) and (sections/*); exact membership/type/absence tests'
  printf 'expected_cwd=%q\nactual_physical_cwd=%q\n' "$P214_COLD" "$P214_PHYSICAL_CWD"
  printf 'cold_member_count=%s\n' "${#P214_COLD_MEMBERS[@]}"
  for p214_name in "${P214_COLD_MEMBERS[@]}"; do printf 'cold_member=%q\n' "$p214_name"; done
  printf 'section_member_count=%s\n' "${#P214_SECTION_MEMBERS[@]}"
  for p214_name in "${P214_SECTION_MEMBERS[@]}"; do printf 'section_member=%q\n' "$p214_name"; done
  for p214_name in texmf .texlive2021; do
    if [[ -e "$p214_name" || -L "$p214_name" ]]; then
      printf 'relative_tree=%q PRESENT_OR_LINK\n' "$p214_name"
    else
      printf 'relative_tree=%q ABSENT\n' "$p214_name"
    fi
  done
} > "$P214_OUT/COLD_CWD.actual.txt"
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
    sections/0_abstract.tex|sections/1_setup.tex|sections/2_clock.tex|sections/3_fibres.tex|sections/4_controls.tex|sections/5_scope.tex)
      [[ -f "$p214_name" && ! -L "$p214_name" ]] ;;
    *) exit 94 ;;
  esac
done
[[ ! -e texmf && ! -L texmf && ! -e .texlive2021 && ! -L .texlive2021 ]]
printf '%s\n' 'EXACT_TWO_DIRECTORY_MEMBERSHIP_TYPES_AND_RELATIVE_TREE_ABSENCE_CHECKS_PASSED' >> "$P214_OUT/COLD_CWD.actual.txt"
for p214_name in "${P214_PRODUCTS[@]}"; do
  [[ ! -e "$p214_name" && ! -L "$p214_name" ]]
done
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
  # A timeout/launch failure is not assigned an invented native TeX exit.
}
p214_build_pass() {
  local p214_label=$1
  shift
  p214_snapshot "$p214_label.before"
  p214_run "$p214_label" 600 "$@"
  p214_snapshot "$p214_label.after"
  sha256sum -c --strict "$P214_OUT/SOURCE_EXPECTED.sha256" > "$P214_OUT/raw/$p214_label.sources.stdout" 2> "$P214_OUT/raw/$p214_label.sources.stderr"
  if [[ "$P214_STEP_STATUS" != 0 ]]; then exit "$P214_STEP_STATUS"; fi
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
(cd "$P214_SRC" && sha256sum -c --strict "$P214_OUT/SOURCE_EXPECTED.sha256") > "$P214_OUT/live_source.after.stdout" 2> "$P214_OUT/live_source.after.stderr"
sha256sum -c --strict "$P214_OUT/SOURCE_EXPECTED.sha256" > "$P214_OUT/cold_source.final.stdout" 2> "$P214_OUT/cold_source.final.stderr"
sha256sum -- main.pdf main.log main.fls main.aux main.bbl main.blg > "$P214_OUT/FINAL_PRODUCTS.sha256"
printf '%s\n' 'CAPTURED_PENDING_FULL_LOG_FLS_CONFIG_PDF_AND_ACTUAL_ALL_PAGE_RECEPTION' > "$P214_OUT/STATUS.txt"
# No PDF adoption, final Review A acceptance, Round1 or package seal is produced here.
