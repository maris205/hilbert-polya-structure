#!/bin/bash
set -euo pipefail
umask 077
W=/root/autodl-tmp/symbolic_dynamics
A=$W/docs/papers211_215_sequence/qa/p215_initial_artifact_audit01
[[ "$PWD" == "$W" && "$#" == 1 && "$1" == "--consume-grant-v2" ]]
[[ "$(sha256sum "$A/GRANT_V2.md" | cut -d' ' -f1)" == c306f8d4a8b05c53e37588d6a96f6a7fd763b5feeddaae499b4cab5616d59e99 ]]
[[ "$(sha256sum "$A/ARTIFACT_DATA_CHECK.v2.cjs" | cut -d' ' -f1)" == fcfa32d2ca27c847b2c37c91ca410746cce027d44818b86a5402138790c581da ]]
[[ "$(sha256sum "$W/docs/papers211_215_sequence/qa/p215_initial_build_binding02/ACTUAL_NATIVE.json" | cut -d' ' -f1)" == 2398bcbbf0a7e2f0828afc233f33e1c999394a2913de6d7c67d5d2e3c137d763 ]]
[[ "$(sha256sum "$W/docs/papers211_215_sequence/qa/p215_initial_build_binding02/CONTINUATION_NATIVE.json" | cut -d' ' -f1)" == baaa11623fb95c181b60f13d59a20293c05104873ea1862425722ffb6c9911a6 ]]
sha256sum -c --strict "$A/INPUT_PINS_V2.sha256" >/dev/null
(cd "$A" && sha256sum -c --strict SOURCE_SHA256SUMS_V2 >/dev/null)
for f in stdout.v2.raw stderr.v2.raw exit.v2; do [[ ! -e "$A/$f" && ! -L "$A/$f" ]]; done
set -C
set +e
/usr/bin/node "$A/ARTIFACT_DATA_CHECK.v2.cjs" >"$A/stdout.v2.raw" 2>"$A/stderr.v2.raw"
status=$?
set -e
printf '%s\n' "$status" >"$A/exit.v2"
exit "$status"
