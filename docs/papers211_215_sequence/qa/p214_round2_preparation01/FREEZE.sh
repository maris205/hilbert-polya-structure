#!/bin/bash
set -euo pipefail
umask 077
[[ "$#" == 1 && "$1" == "--execute-under-separate-root-grant" ]] || exit 78
cd /root/autodl-tmp/symbolic_dynamics
P214_PREP=docs/papers211_215_sequence/qa/p214_round2_preparation01
P214_BIND=docs/papers211_215_sequence/qa/p214_round2_binding01
P214_FREEZE=papers/214-nilpotent-bilinear-clock/frozen_round2
sha256sum -c --strict "$P214_BIND/INPUTS.sha256"
[[ ! -e "$P214_FREEZE" && ! -L "$P214_FREEZE" ]]
mkdir -- "$P214_FREEZE"
mkdir -- "$P214_FREEZE/sections" "$P214_FREEZE/sources" "$P214_FREEZE/evidence"
while IFS=$'\t' read -r source dest; do
  [[ -f "$source" && ! -L "$source" && ! -e "$P214_FREEZE/$dest" ]]
  cp --no-clobber -- "$source" "$P214_FREEZE/$dest"
  cmp -- "$source" "$P214_FREEZE/$dest"
done < "$P214_PREP/FILES.tsv"
set -C
(
  cd "$P214_FREEZE"
  while IFS=$'\t' read -r source dest; do sha256sum -- "$dest"; done \
    < "/root/autodl-tmp/symbolic_dynamics/$P214_PREP/FILES.tsv"
) > "$P214_FREEZE/SHA256SUMS"
(cd "$P214_FREEZE" && sha256sum -c --strict SHA256SUMS)
sha256sum -c --strict "$P214_BIND/INPUTS.sha256"
printf '%s\n' COPIED_AND_COMPARED_PENDING_INDEPENDENT_RECEPTION

