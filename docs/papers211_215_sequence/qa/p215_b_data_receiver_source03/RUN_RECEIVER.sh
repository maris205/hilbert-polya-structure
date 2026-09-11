#!/bin/bash
set -euo pipefail
[[ "$#" == 1 && "$1" == "--consume-root-correction-grant" ]] || exit 78
umask 077
cd /root/autodl-tmp/symbolic_dynamics
P215_B_RECEIVER=docs/papers211_215_sequence/qa/p215_b_data_receiver_source03
[[ ! -e "$P215_B_RECEIVER/run01" && ! -L "$P215_B_RECEIVER/run01" ]]
/usr/bin/sha256sum -c --strict "$P215_B_RECEIVER/SOURCE_SHA256SUMS"
/usr/bin/mkdir -m 700 -- "$P215_B_RECEIVER/run01"
set +e
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C LC_ALL=C TZ=UTC \
  /usr/bin/node "$P215_B_RECEIVER/RECEIVE_INITIAL.cjs" \
  > "$P215_B_RECEIVER/run01/receiver.stdout.raw" \
  2> "$P215_B_RECEIVER/run01/receiver.stderr.raw"
P215_B_RECEIVER_STATUS=$?
set -e
printf '%s\n' "$P215_B_RECEIVER_STATUS" > "$P215_B_RECEIVER/run01/receiver.exit"
exit "$P215_B_RECEIVER_STATUS"
