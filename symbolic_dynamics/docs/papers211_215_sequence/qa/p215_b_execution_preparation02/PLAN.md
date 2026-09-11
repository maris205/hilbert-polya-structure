# P215 Review B initial execution preparation

2026-09-11 UTC. `SOURCE_ONLY / NO_OPERATION_AUTHORIZED`.

Root accepted the complete B SOURCE package in
`qa/p215_b_source_root01/SOURCE_RECEPTION.md`. The proposed initial capture
binds that receipt, the nine sealed B payloads, all 43 fixed input pins and the
current ordinary Node runtime. It does not read a canonical or any prior or
future B output.

The proposed child has no arguments or declared external reads. It runs from
the workspace root with `/usr/bin/node`, stdin `/dev/null`, umask 077 and an
environment containing only `PATH=/usr/bin:/bin`, `LANG=C`, `LC_ALL=C` and
`TZ=UTC`. The exact interpreter, capture tools and Node shared objects are
recorded in `RUNTIME_BINDING.json` and pinned in `RUNTIME_BINARIES.sha256`.

Only a separate root one-use grant may invoke `RUN.initial.proposed.sh.txt`.
At that time the recipe must find `qa/p215_b_initial_run01` absent, verify the
preparation inputs, runtime binaries, review package and all input pins, then
create the output directory without overwrite. It captures complete raw
stdout/stderr and child/controller exits, repeats all checks after the child,
and records output hashes. Any partial or failed tree is retained without
cleanup, retry or directory reuse.

`OUTPUT_CONTRACT.md` fixes the deterministic 34-line wire shape.
`DATA_RECEIVER_PLAN.md` precommits a distinct root receiver that checks the
capture envelope and independently reconstructs all 30 carriers and 5,704
states. A printed `PASS` is not by itself DATA acceptance.

No execution, canonical query/adoption, strict replay, manuscript change,
build, Round2, terminal action, central-index edit, Git or external action is
authorized. `OWNER_AMBER / HOLD_EXTERNAL`.
