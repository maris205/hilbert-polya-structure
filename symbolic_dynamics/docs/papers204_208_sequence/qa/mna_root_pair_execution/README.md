# MNA root actual independent-code pair and original inspection

2026-09-07 UTC. Root actually launched the separate prepared runner after
reading its complete source and receiving a successful native preflight.
`RUN_LAUNCH.actual.json` and `RUN_COMPLETION.actual.json` preserve the actual
tool returns; `preflight_01/` and `run_01/` retain complete child streams,
attempts and receipts. The actual run ended at 11:44:25 UTC with exit 0.

The immutable scientific pair is in
`../root_replays/mna_gate_pair_01/`: 56 nonself payloads, sealed by
`3a5e964b14738093160c2f52910dc682f4ea76f81ad1bcc782383bb166c5fdc0`.
Its two fresh executions of the unchanged gate verifier each check 115,680
predicates on the same original 4,095 states, total masses 1 through 12.
The complete 1,562,038-byte canonical has SHA-256
`233944c44f8b72ce17495c0f16665dcaac77974c60251275403b98118f68a731`.
Actual raw comparisons of both outputs to that canonical and to each other
returned 0. No experiment cutoff was enlarged.

This pair uses system Python 3.10 with isolated mode, no site and no bytecode
cache, rather than reusing the gate's Python 3.12 runtime claim. Its 4,237
known inputs retain all 997 original gate keys and add the new runtime's
source/library/configuration closure. Full before/after records and observed
runtime file identities are in the sealed pair. This is a bounded runtime
inventory, not an OS/startup/continuous syscall trace or hermeticity proof.

Root then read and actually executed `inspect_pair.py`. Its separate PASS in
`PAIR_ROOT_INSPECTION.json` checks 22,558 documentary predicates, all 56 pair,
4 preparation and 309 original gate payloads, complete receipts/runtime
records and three new raw comparisons. All 4,302 actually consumed paths
were rechecked twice; `PAIR_ROOT_READS.json` records each length/hash with
ledger SHA-256
`7559e4f9551cc1845ac4a1cc35905e7ca2694312826ac2a19bea5881bdcb67aa`.
`PAIR_INSPECTION.actual_tool_return.json` preserves the actual inspection
return. The inspection is not an additional scientific execution.

Root is a proof contributor, so neither action is an independent candidate
or manuscript review. The original gate's failed locale/gconv attempts remain
unchanged. Admission also requires the separate proof/source and complete
original gate-artifact reception; no paper number or completed fifth paper
is conferred by this replay package alone. OWNER_AMBER / HOLD_EXTERNAL.
