# Root's UGR candidate-gate replay

2026-09-06 UTC. Root read the complete independent candidate report,
source audit, provenance, execution record and standalone C++ checker,
plus the original UGR temporal and LNR inverse proofs. The gate package's
46 nonself manifest entries and 19 input pins passed before this replay.

The three files `record_gate.py`, `verify_gate.cpp`, `CANONICAL.jsonl`
were copied without changes from the closed gate into this directory.
Actual command: `python record_gate.py pair_01`. The fresh cold compilation
and both separate producer executions succeeded. Each run completed
2,638,324 assertions; both actual raw `cmp` calls exited zero. Complete
commands, settings, source/binary hashes and streams are in
[pair_01/receipt.json](pair_01/receipt.json). Both stdout files are 6,184
bytes, SHA-256
`6beafa58167d74b9db85ca8001b8a54043ad6ffbe493901a6046ead5485e2cb5`;
both stderr files are empty. The C++ source hash is
`dda534f27a47161b4d38e2294c00876a080088ac36d6fd55169ce6c11c91aa1c`.

The inherited harness `kind` describes the checker origin (nonauthor
candidate gate), not the operator of these runs. These executions were
performed by root, a proof contributor, and are root replay evidence,
not another independent review. The original receipts are unchanged.

Root accepts `GO_NARROW_RANK_FAMILY` and assigns P207 to exactly one
UGR/LNR rank-family conjunction. The global upper clock is nonsharp and
computer-assisted; the shared global inverse comparison is counted once.
LNR-S1 remains open for the separate strict-lower iteration; its unread
source body is not claimed to have been obtained or cleared. The gate's
withdrawn provisional HOLD is preserved. No manuscript review or full
batch completion follows from this candidate admission. `HOLD_EXTERNAL`.
