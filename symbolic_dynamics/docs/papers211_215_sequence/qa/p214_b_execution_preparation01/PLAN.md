# P214 Review B initial execution preparation

2026-09-11 UTC. `SOURCE_ONLY / NO_OPERATION_AUTHORIZED`.

The eligible B package is fixed by
`docs/papers211_215_sequence/reviews/p214_b/SHA256SUMS`. Its scientific inputs
are exactly the 30 physical Round1 payloads, the Round1 nonself manifest and
`qa/p214_round1_binding01/ROUND1_RECEPTION.md`, all pinned in the B package.

The proposed invocation uses `/usr/bin/python3.10 -I -S -B`, no script
arguments and an empty environment except deterministic locale/time/path.
It would exclusively create `qa/p214_b_initial_run01` and retain complete raw
stdout, stderr, Python status, controller streams, post-run input checks and
output hashes. It cannot overwrite or reuse an existing output path.

Before any grant, root must fully read and accept the B proof/source, verifier,
schema, pins, request and capture recipe; verify exact current interpreter and
ordinary runtime dependencies; confirm the output path is absent; and issue a
new one-use operation-specific grant. This preparation neither performs nor
authorizes those steps.

An actual failure or partial output must be preserved without retry, cleanup,
source repair, normalization or directory reuse. Initial output is not strict
replay credit. No live/frozen edit, build, central index, Git or external action
is in scope. `HOLD_EXTERNAL`.
